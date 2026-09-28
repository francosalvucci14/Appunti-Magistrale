import xml.etree.ElementTree as ET
import requests
import time
from rdflib import Graph, URIRef, Namespace, RDF, Literal
from rdflib.namespace import RDFS  # Importato per usare rdfs:label

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
    "Per le Autonomie (SVP-PATT, Campobase)": "Südtiroler Volkspartei"
    # "Misto" è stato rimosso da qui perché lo gestiamo come caso speciale nel codice
}

def ottieni_allineamento_api_rest(nome_partito):
    """
    Usa l'API REST nativa di Wikidata per ottenere l'ID, e successivamente
    estrae la label in italiano dell'allineamento politico.
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
            
        entity_id = data["search"][0]["id"] 
        
        time.sleep(1) # Pausa di cortesia
        
        # PASSO 2: Cerca la proprietà P1387 (allineamento politico)
        claims_url = f"https://www.wikidata.org/w/api.php?action=wbgetclaims&entity={entity_id}&property=P1387&format=json"
        claims_resp = requests.get(claims_url, headers=headers)
        claims_data = claims_resp.json()
        
        try:
            alignment_id = claims_data["claims"]["P1387"][0]["mainsnak"]["datavalue"]["value"]["id"]
        except KeyError:
            print(f"  Nessun Allineamento Politico (P1387) trovato per {nome_partito} ({entity_id})")
            return None

        time.sleep(1) # Altra pausa di cortesia per l'API
        
        # PASSO 3: Recupera l'etichetta (label) in italiano dell'allineamento (es: da Q76074 a "destra")
        label_url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={alignment_id}&props=labels&languages=it&format=json"
        label_resp = requests.get(label_url, headers=headers)
        label_data = label_resp.json()
        
        try:
            label_text = label_data["entities"][alignment_id]["labels"]["it"]["value"]
            # Formattiamo con l'iniziale maiuscola (es. "destra" diventa "Destra")
            return label_text.title() 
        except KeyError:
            print(f"  Nessuna label italiana trovata per l'allineamento {alignment_id}")
            return None
            
    except Exception as e:
        print(f"  Errore API per {nome_partito}: {e}")
        return None

def genera_allineamenti_politici():
    g_enrichment = Graph()
    g_enrichment.bind("osr", OSR)
    g_enrichment.bind("wd", WD)
    g_enrichment.bind("owl-senato", SCHEMA_PROGETTO)
    # Aggiungiamo anche rdfs al bind per GraphDB
    g_enrichment.bind("rdfs", RDFS)
    
    print("Estrazione gruppi unici in corso...")
    tree = ET.parse('../composizione_gruppi_data.xml') 
    root = tree.getroot()
    
    gruppi_gia_inseriti = set()

    for result in root.findall('sp:results/sp:result', SPARQL_NS):
        gruppo_uri = result.find('sp:binding[@name="gruppo"]/sp:uri', SPARQL_NS).text
        nome_gruppo = result.find('sp:binding[@name="nomeGruppo"]/sp:literal', SPARQL_NS).text
        
        if gruppo_uri not in gruppi_gia_inseriti:
            alignment_label = None
            
            # -----------------------------------------------------
            # GESTIONE SPECIALE: Assegnazione manuale per il gruppo Misto
            # -----------------------------------------------------
            if nome_gruppo == "Misto":
                print(f"Gestione speciale per: {nome_gruppo}...")
                alignment_label = "Trasversalismo"
            else:
                partito_standard = MAPPATURA_GRUPPI_WIKIDATA.get(nome_gruppo)
                if partito_standard:
                    print(f"Cerco allineamento per: {partito_standard}...")
                    alignment_label = ottieni_allineamento_api_rest(partito_standard)
            
            # Se abbiamo trovato un'etichetta (da API o manuale), generiamo le triple
            if alignment_label:
                gruppo_ref = URIRef(gruppo_uri)
                
                # Creiamo un'URI dinamica personalizzata leggibile eliminando gli spazi
                # (es: "Trasversalismo" -> http://example.com/OWL-Senato/#Trasversalismo)
                safe_uri_suffix = alignment_label.replace(" ", "_")
                align_ref = URIRef(f"http://example.com/OWL-Senato/#{safe_uri_suffix}")
                
                # 1. Leghiamo il gruppo al nuovo URL dell'allineamento
                g_enrichment.add((gruppo_ref, SCHEMA_PROGETTO.haAllineamentoPolitico, align_ref))
                
                # 2. Definiamo l'allineamento come individuo dell'ontologia
                g_enrichment.add((align_ref, RDF.type, SCHEMA_PROGETTO.AllineamentoPolitico))
                
                # 3. Aggiungiamo anche il valore letterale (Literal) tramite RDFS.label
                g_enrichment.add((align_ref, RDFS.label, Literal(alignment_label, lang="it")))
                
                print(f"  --> Successo! Collegato a: {align_ref} (Valore: '{alignment_label}')")
                 
            gruppi_gia_inseriti.add(gruppo_uri)

    g_enrichment.serialize(destination='allineamenti_politici2.ttl', format='turtle')

    print("\nFile 'allineamenti_politici2.ttl' generato con successo!")

if __name__ == "__main__":
    genera_allineamenti_politici()