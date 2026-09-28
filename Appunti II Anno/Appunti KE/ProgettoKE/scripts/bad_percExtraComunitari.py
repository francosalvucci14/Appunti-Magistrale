import time
from SPARQLWrapper import SPARQLWrapper, JSON

# ==========================================
# 1. RECUPERO DATI DAL DATABASE LOCALE
# ==========================================
# Sostituisci l'URL se la porta o il nome del repository sono diversi
repo_locale_url = "http://localhost:7200/repositories/ProgettoKE"
sparql_locale = SPARQLWrapper(repo_locale_url)

query_locale = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX osr: <http://dati.senato.it/osr/>
SELECT ?nome ?cognome WHERE {
    ?s a osr:Senatore .
    ?s foaf:firstName ?nome .
    ?s foaf:familyName ?cognome .
}
"""
sparql_locale.setQuery(query_locale)
sparql_locale.setReturnFormat(JSON)

print("Scaricando la lista dei senatori dal database locale...")
risultati_locali = sparql_locale.query().convert()

senatori = []
for r in risultati_locali["results"]["bindings"]:
    # Uniamo nome e cognome
    nome = r['nome']['value']
    cognome = r['cognome']['value']
    nome_completo = f"{nome} {cognome}"
    senatori.append(nome_completo)

# ==========================================
# 2. INTERROGAZIONE A WIKIDATA
# ==========================================
sparql_wd = SPARQLWrapper("https://query.wikidata.org/sparql")
# ECCO LA MAGIA: Impostiamo l'User-Agent esplicitamente per aggirare il blocco
sparql_wd.addCustomHttpHeader("User-Agent", "ProgettoSenato/1.0 (tua_email@email.it)")
sparql_wd.setReturnFormat(JSON)

totale_trovati_wd = 0
totale_extra_ue = 0

print(f"Trovati {len(senatori)} senatori locali. Inizio interrogazione Wikidata...")

for senatore in senatori:
    # Query per Wikidata: verifica se la persona esiste, preleva il luogo di nascita
    # e controlla (tramite BIND EXISTS) se lo stato è membro dell'UE (Q458)
    query_wd = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>

    SELECT ?isUE WHERE {{
        ?p wdt:P31 wd:Q5 ;
           rdfs:label "{senatore}"@it .
        ?p wdt:P19 ?luogoNascita .
        ?luogoNascita wdt:P17 ?statoNascita .
        
        # BIND genera 'true' se lo stato è nell'UE, 'false' altrimenti
        BIND(EXISTS {{ ?statoNascita wdt:P463 wd:Q458 }} AS ?isUE)
    }} LIMIT 1
    """
    
    sparql_wd.setQuery(query_wd)
    
    try:
        risultati_wd = sparql_wd.query().convert()
        bindings = risultati_wd["results"]["bindings"]
        
        if bindings:
            totale_trovati_wd += 1
            is_ue = bindings[0]["isUE"]["value"] == "true"
            
            # Se la variabile is_ue è falsa, il senatore è extra-comunitario
            if not is_ue:
                totale_extra_ue += 1
                
        # PAUSA OBBLIGATORIA: Wikidata permette al massimo 5-10 richieste al secondo
        # time.sleep assicura che il nostro script si comporti in modo educato e non venga bloccato
        time.sleep(0.2)
        
    except Exception as e:
        print(f"Errore durante l'interrogazione di '{senatore}': {e}")

# ==========================================
# 3. CALCOLO PERCENTUALE E OUTPUT
# ==========================================
if totale_trovati_wd > 0:
    percentuale = (totale_extra_ue / totale_trovati_wd) * 100
    print("\n--- RISULTATI FINALI ---")
    print(f"Senatori analizzati con successo su Wikidata: {totale_trovati_wd} su {len(senatori)}")
    print(f"Senatori nati fuori dall'UE: {totale_extra_ue}")
    print(f"Percentuale Extra-UE: **{percentuale:.2f}%**")
else:
    print("\nNessun senatore trovato su Wikidata o errore di rete.")