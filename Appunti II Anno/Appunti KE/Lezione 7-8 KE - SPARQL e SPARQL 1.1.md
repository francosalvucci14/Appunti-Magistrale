```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# SPARQL

Per capire cos'è SPARQL, dobbiamo fare un passo indietro fino al 1998, anno in cui **RDF (Resource Description Framework)** è diventato una raccomandazione ufficiale del W3C (World Wide Web Consortium). RDF è il modello standard per la rappresentazione dei dati nel Web Semantico, basato su "triple" (Soggetto, Predicato, Oggetto).

Una volta introdotto RDF, è nata l'esigenza di poter estrarre e interrogare queste informazioni, simili a come facciamo con i normali database. Negli anni successivi, la comunità scientifica ha proposto diverse filosofie di interrogazione:

- **Linguaggi simili a SQL** (RDQL, SeRQL, ecc.), pensati per chi era già abituato ai database relazionali.
    
- **Linguaggi basati su regole** (N3QL, DQL).
    
- **Linguaggi basati su XML** (sfruttando XSLT o XPath) e **simili a XPath** (RDFPath).
    

Tra questi approcci, i linguaggi **SQL-like** si sono rivelati i più intuitivi e supportati. Il W3C ha quindi istituito un gruppo di lavoro (il _Data Access Working Group_) per standardizzare un unico linguaggio di interrogazione per RDF, prendendo il meglio delle proposte esistenti. Da questo sforzo, il **15 Gennaio 2008**, è nato ufficialmente **SPARQL** come raccomandazione W3C.

## Introduzione

**SPARQL** è un acronimo ricorsivo che sta per _SPARQL Protocol and RDF Query Language_. Come suggerisce il nome, ha una doppia anima: è sia un linguaggio di interrogazione che un protocollo.

**SPARQL come Linguaggio:**

A prima vista, la sua sintassi ricorda molto da vicino SQL (con comandi come `SELECT` e `WHERE`). Tuttavia, i due mondi si basano su paradigmi radicalmente diversi:

- In un **Database Relazionale (SQL)**, i dati sono rigidamente strutturati in tabelle (righe e colonne) e i collegamenti tra le informazioni avvengono tramite chiavi primarie e chiavi esterne.
    
- Nel mondo **RDF**, i dati sono organizzati a **Grafo**. Ogni risorsa è identificata da un **URI** (Uniform Resource Identifier, simile agli URL dei siti web). I dati sono liberi di espandersi: più grafi possono essere uniti tra loro e per recuperare le informazioni si usa un meccanismo di _unificazione degli URI_.
    

**SPARQL come Protocollo:**

SPARQL è progettato per funzionare "on top" (al di sopra) dei protocolli web esistenti, principalmente **HTTP**. Questo significa che puoi interrogare un "Triple Store" (un database progettato per RDF) semplicemente inviando una richiesta web. Nella slide viene mostrato un esempio di URL dove la query stessa viene passata come parametro (`?query=PREFIX...`), rendendo i database semantici facilmente interrogabili via web tramite semplici API REST.

## Graph Pattern e Unificazione

Il concetto fondamentale per capire come funziona SPARQL è il **Graph Pattern** (Pattern di Grafo) e il processo di **Unificazione (Matching)**.

A differenza di SQL dove cerchi righe in una tabella, in SPARQL tu definisci un "sottografo ideale" (il _template_ o _Graph Pattern_) contenente delle variabili. Il motore SPARQL prende questo tuo pattern e cerca di sovrapporlo (unificarlo) con il grande grafo dei dati reale.

Due termini "unificano" se:

1. Sono identici (es: cerco esattamente l'URI della città di Roma e trovo l'URI della città di Roma).
    
2. Uno dei due è una **variabile** e può essere sostituito con un termine reale presente nel grafo.

Matematicamente:
- Una unificazione gi un graph pattern $GP$ su un grafo $G$ è fornita da una sostituzione di variaibli $S$ tale che $S(GP)$ sia un sottografo di $G$

In pratica, se la tua query chiede `?x :worksIn :tor_vergata`, stai dicendo al motore: _"Trovami tutti i nodi del grafo (che chiameremo `?x`) che sono collegati al nodo `tor_vergata` tramite la freccia (proprietà) `worksIn`"_. Ogni volta che il motore trova un incastro perfetto, la variabile `?x` si istanzia con il valore trovato.

**Esempio**

```SPARQL
PREFIX: http://art.uniroma2.it/ontologies/st_example
SELECT: ?x
WHERE {?x:worksIn :tor_vergata.}
```
## La Sintassi

La sintassi di SPARQL si appoggia molto a **Turtle**, uno dei formati più leggibili per scrivere RDF.

I mattoni fondamentali della sintassi sono:

- **URI**: Spesso abbreviati usando i **QNames** (es: invece di scrivere `http://xmlns.com/foaf/0.1/knows`, si dichiara un prefisso e si scrive solo `foaf:knows`).
	- nello specifico la sintassi è `<prefisso>:<resourcename>`
    
- **Literals**: Valori testuali o numerici puri (es: "Mario Rossi" o 42).
- **Variabili**: Elementi dinamici della query, sempre preceduti dal simbolo `?` o `$` (es: `?nome`, `?persona`).
	- es: ?var o \$var
- **Operatori su grafi**

Per rendere le query più compatte e leggibili, SPARQL offre utilissime scorciatoie (Triple Pattern syntax):

- Le singole tuple sono separate da punti $(\cdot)$
- **Predicate-Object Lists**: Se due o più proprietà si riferiscono allo stesso soggetto, non serve ripeterlo. Si usa il **Punto e virgola (`;`)** per separare le coppie predicato-oggetto.
	- es: `?person foaf:knows :mario_rossi ; foaf:name ?name .`
- **Object Lists**: Se un soggetto e un predicato hanno più oggetti (es: Mario conosce sia Luigi che Franco), si usa la **Virgola (`,`)** per separare gli oggetti.
	- es: `?person foaf:knows :mario_rossi, :franoc_bianchi`
- La lettera **`a`** è una scorciatoia standard per indicare la proprietà `rdf:type` (che definisce la classe a cui appartiene un elemento). 
	- Es: `?x a :Person` significa "?x è di tipo Persona".

**La struttura classica di una query** prevede quattro blocchi principali:

1. `PREFIX`: Dichiara gli spazi dei nomi (namespace) per abbreviare gli URI successivi.
    
2. `SELECT`: Elenca le variabili che vogliamo visualizzare nel risultato finale (es: `SELECT ?person`).
    
3. `FROM`: Indica l'indirizzo fisico del file o del database da interrogare (da non confondere con il namespace, che è solo un "vocabolario" concettuale).
    
4. `WHERE`: Contiene il vero e proprio Graph Pattern racchiuso tra parentesi graffe `{}`. È il blocco logico che fa il lavoro sporco di ricerca.

**Esempio**

![center|500](img/Pasted%20image%2020260515165337.png)

## Esecuzione delle query e Risultati

Come si comporta il motore SPARQL quando premi "Invio"?

1. Cerca di unificare il tuo Graph Pattern con i dati RDF sorgente.
    
2. **Per ogni unificazione riuscita**, genera una "soluzione".
    
3. Una volta trovate tutte le soluzioni, applica degli **operatori di filtro e formattazione** simili a quelli di SQL: può proiettare solo alcune variabili (`PROJECT`), eliminare i duplicati (`DISTINCT`), ordinare i risultati (`ORDER BY`), o limitare il numero di output (`LIMIT/OFFSET`).
    

L'output finale dipende dall'operatore scelto:

- `SELECT` (il più comune) restituisce i risultati sotto forma di **Tabella**.
    
- `CONSTRUCT` prende i risultati e costruisce un nuovo grafo RDF.
    
- `ASK` restituisce solo un valore booleano (Vero/Falso: il pattern esiste?).
    
- `DESCRIBE` restituisce un grafo RDF che descrive una risorsa trovata.
    

Vediamo un esempio di risultato in forma tabulare (da una `SELECT`). 

Ci sono tre colonne corrispondenti a tre ipotetiche variabili (`x`, `y`, `z`).

| x                       | y                          | z         |
| ----------------------- | -------------------------- | --------- |
| "Maria Teresa Pazienza" | \<http://this_example/ml\> | Professor |
| "Armando Stellato"      | \<http://this_example/as\> |           |

Un dettaglio cruciale e tipico di RDF emerge guardando la seconda riga dei risultati: il sistema ha trovato una soluzione ("Armando Stellato"), ma il campo della colonna `z` è **vuoto**. Nel Web Semantico, che si basa sull'ipotesi del "mondo aperto" (Open World Assumption), i dati possono essere incompleti. Una query non fallisce se manca un pezzo di informazione (a meno che non sia strettamente richiesto); semplicemente, la variabile rimane vuota o non istanziata per quella specifica riga.