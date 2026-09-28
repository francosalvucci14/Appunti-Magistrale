import xml.etree.ElementTree as ET
import requests
import time
from rdflib import Graph, URIRef, Namespace, RDF

# Definizioni dei Namespace
OSR = Namespace("http://dati.senato.it/osr/")
WD = Namespace("http://www.wikidata.org/entity/")
SCHEMA_PROGETTO = Namespace("http://example.com/OWL-Senato/#")
SPARQL_NS = {'sp': 'http://www.w3.org/2005/sparql-results#'} 

MAPPATURA_GRUPPI_WIKIDATA = {
    "Fratelli d'Italia": "Fratelli d'Italia",
    "MoVimento 5 Stelle": "Movimento 5 Stelle",
    "Lega Salvini Premier - Partito Sardo d'Azione": "Lega Nord",
    "Partito Democratico - Italia Democratica e Progressista": "Partito Democratico",
    "Forza Italia - Berlusconi Presidente - PPE": "Forza Italia",
    "Italia Viva - Casa Riformista": "Italia Viva",
    "Per le Autonomie (SVP-PATT, Campobase)": "Südtiroler Volkspartei",
    "Misto": None # Per gruppo misto mettere in automatico stesso allineamento di MV5 - trasversalismo id Q3289782
}

def ottieni_allineamento_api_rest(nome_partito):
    """
    Usa l'API REST nativa di Wikidata (Action API) invece dell'endpoint SPARQL 
    per evitare l'errore HTTP 429.
    """
    if not nome_partito:
        return None
        
    headers = {"User-Agent": "ProgettoEsameUni_KnowledgeEngineering/1.0 (studente@uni.it)"}
    
    # PASSO 1: Cerca l'ID dell'entità Wikidata a partire dal nome
    search_url = "https://www.wikidata.org/w/api.php"
    search_params = {
        "action": "wbsearchentities",
        "format": "json",
        "language": "it",
        "search": nome_partito
    }
    
    try:
        resp = requests.get(search_url, params=search_params, headers=headers)
        data = resp.json()
        
        if not data.get("search"):
            print(f"  Nessuna entità trovata per: {nome_partito}")
            return None
            
        entity_id = data["search"][0]["id"] # Estrae l'ID (es. Q220, Q47774)
        
        # Pausa di cortesia per l'API
        time.sleep(1)
        
        # PASSO 2: Cerca la proprietà P1387 (allineamento politico) per quell'entità
        claims_url = f"https://www.wikidata.org/w/api.php?action=wbgetclaims&entity={entity_id}&property=P1387&format=json"
        claims_resp = requests.get(claims_url, headers=headers)
        claims_data = claims_resp.json()
        
        # Naviga il JSON di Wikidata per estrarre il valore del claim
        try:
            alignment_id = claims_data["claims"]["P1387"][0]["mainsnak"]["datavalue"]["value"]["id"]
            return f"http://www.wikidata.org/entity/{alignment_id}"
        except KeyError:
            print(f"  Nessun Allineamento Politico (P1387) trovato per {nome_partito} ({entity_id})")
            return None
            
    except Exception as e:
        print(f"  Errore API per {nome_partito}: {e}")
        return None

def genera_allineamenti_politici():
    g_enrichment = Graph()
    g_enrichment.bind("osr", OSR)
    g_enrichment.bind("wd", WD)
    g_enrichment.bind("owl-senato", SCHEMA_PROGETTO)
    
    print("Estrazione gruppi unici in corso...")
    # Sostituisci il nome del file se necessario
    tree = ET.parse('../composizione_gruppi_data.xml') 
    root = tree.getroot()
    
    gruppi_gia_inseriti = set()

    for result in root.findall('sp:results/sp:result', SPARQL_NS):
        gruppo_uri = result.find('sp:binding[@name="gruppo"]/sp:uri', SPARQL_NS).text
        nome_gruppo = result.find('sp:binding[@name="nomeGruppo"]/sp:literal', SPARQL_NS).text
        
        if gruppo_uri not in gruppi_gia_inseriti:
            partito_standard = MAPPATURA_GRUPPI_WIKIDATA.get(nome_gruppo)
            
            if partito_standard:
                print(f"Cerco allineamento per: {partito_standard}...")
                alignment_uri = ottieni_allineamento_api_rest(partito_standard) # TODO: prendere il label dell'allineamento politico da Wikidata e inserirlo come literal in RDF
                
                if alignment_uri:
                    gruppo_ref = URIRef(gruppo_uri)
                    align_ref = URIRef(alignment_uri)
                    
                    g_enrichment.add((gruppo_ref, SCHEMA_PROGETTO.haAllineamentoPolitico, align_ref))
                    g_enrichment.add((align_ref, RDF.type, SCHEMA_PROGETTO.AllineamentoPolitico))
                    
                    print(f"  --> Successo! Collegato a: {alignment_uri}")
                 
            gruppi_gia_inseriti.add(gruppo_uri)

    g_enrichment.serialize(destination='allineamenti_politici.ttl', format='turtle')

    print("\nFile 'allineamenti_politici.ttl' generato con successo!")

if __name__ == "__main__":
    genera_allineamenti_politici()