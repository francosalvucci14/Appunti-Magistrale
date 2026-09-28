import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD, FOAF

# 1. Definizione dei Namespace
OSR = Namespace("http://dati.senato.it/osr/")
SCHEMA_PROGETTO = Namespace("http://example.com/OWL-Senato/#")
# Namespace standard dei risultati SPARQL XML
SPARQL_NS = {'sp': 'http://www.w3.org/2005/sparql-results#'} 

def get_value(binding, var_name, is_uri=False):
    """Funzione helper per estrarre il testo da un nodo XML SPARQL in modo sicuro."""
    node = binding.find(f'sp:binding[@name="{var_name}"]', SPARQL_NS)
    if node is not None:
        if is_uri:
            uri_node = node.find('sp:uri', SPARQL_NS)
            return uri_node.text if uri_node is not None else None
        else:
            lit_node = node.find('sp:literal', SPARQL_NS)
            return lit_node.text if lit_node is not None else None
    return None

def genera_grafo_senatori():
    # Inizializza il grafo
    g = Graph()
    g.bind("osr", OSR)
    g.bind("owl-senato", SCHEMA_PROGETTO)
    g.bind("foaf", FOAF)

    # --- PARSING SENATORI ---
    print("Elaborazione senatori_legislatura.xml...")
    tree = ET.parse('../senatori_legislatura.xml')
    root = tree.getroot()

    for result in root.findall('sp:results/sp:result', SPARQL_NS):
        senatore_uri = get_value(result, 'senatore', is_uri=True)
        if not senatore_uri:
            continue
            
        senatore_ref = URIRef(senatore_uri)
        
        # Aggiungiamo il tipo
        g.add((senatore_ref, RDF.type, OSR.Senatore))
        
        # Nome e Cognome
        nome = get_value(result, 'nome')
        cognome = get_value(result, 'cognome')
        if nome: g.add((senatore_ref, FOAF.firstName, Literal(nome)))
        if cognome: g.add((senatore_ref, FOAF.familyName, Literal(cognome)))
        
        # Dati anagrafici e di genere
        sesso = get_value(result, 'sesso')
        if sesso: g.add((senatore_ref, OSR.sesso, Literal(sesso))) # Assumendo tu abbia creato osr:sesso
        
        data_nascita = get_value(result, 'dataNascita')
        if data_nascita:
            # Notare l'uso di XSD.date per specificare il tipo di dato!
            g.add((senatore_ref, OSR.dataNascita, Literal(data_nascita, datatype=XSD.date)))
            
        nazione = get_value(result, 'nazioneNascita')
        if nazione:
            g.add((senatore_ref, OSR.nazioneNascita, Literal(nazione)))
        
        cittaNascita = get_value(result, 'cittaNascita')
        if cittaNascita:
            g.add((senatore_ref, OSR.cittaNascita, Literal(cittaNascita)))
        
        provinciaNascita = get_value(result, 'provinciaNascita')
        if provinciaNascita:
            g.add((senatore_ref, OSR.provinciaNascita, Literal(provinciaNascita)))
        
        ### AGGIUGNERE PIÙ AVANTI ALTRI DATI, COME LEGISLATURA, MANDATI, ETC. SE DISPONIBILI NEL FILE XML

    # --- PARSING GRUPPI (per creare il legame Senatore -> Gruppo) ---
    print("Elaborazione composizione_gruppi_data.xml...")
    tree_gruppi = ET.parse('../composizione_gruppi_data.xml')
    root_gruppi = tree_gruppi.getroot()

    for result in root_gruppi.findall('sp:results/sp:result', SPARQL_NS):
        senatore_uri = get_value(result, 'senatore', is_uri=True)
        gruppo_uri = get_value(result, 'gruppo', is_uri=True)
        nome_gruppo = get_value(result, 'nomeGruppo')
        carica = get_value(result, 'carica')
        inizioAdesione = get_value(result, 'inizioAdesione')

        if senatore_uri and gruppo_uri:
            senatore_ref = URIRef(senatore_uri)
            gruppo_ref = URIRef(gruppo_uri)
            
            # Dichiariamo che il Gruppo è di tipo GruppoParlamentare (la classe che hai creato su VocBench)
            g.add((gruppo_ref, RDF.type, SCHEMA_PROGETTO.GruppoParlamentare))
            if nome_gruppo:
                g.add((gruppo_ref, OSR.titolo, Literal(nome_gruppo)))
            
            if carica:
                g.add((senatore_ref, OSR.carica, Literal(carica)))
            
            if inizioAdesione:
                g.add((senatore_ref, SCHEMA_PROGETTO.inizioAdesione, Literal(inizioAdesione, datatype=XSD.date)))

            # Creiamo il link inventato su VocBench
            g.add((senatore_ref, SCHEMA_PROGETTO.appartieneAGruppo, gruppo_ref))

    # Salvataggio su file
    g.serialize(destination='dati_senato.ttl', format='turtle')
    print("File 'dati_senato.ttl' generato con successo!")

if __name__ == "__main__":
    genera_grafo_senatori()