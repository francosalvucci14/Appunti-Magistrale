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

SPARQL è progettato per funzionare "on top" (al di sopra) dei protocolli web esistenti, principalmente **HTTP**. Questo significa che puoi interrogare un "Triple Store" (un database progettato per RDF) semplicemente inviando una richiesta web. 
Vediamo un esempio di URL dove la query stessa viene passata come parametro (`?query=PREFIX...`), rendendo i database semantici facilmente interrogabili via web tramite semplici API REST.

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
### Dettagli sui Dati: Lingue e Tipi

Nel Web Semantico, un testo non è mai "solo" un testo. I _literals_ (i valori costanti come stringhe o numeri) possono avere attributi specifici che dobbiamo poter interrogare con precisione.

- **Language Tags (Etichette di lingua):** Se nel nostro grafo abbiamo stringhe localizzate, possiamo cercare esattamente la traduzione che ci serve usando il simbolo `@`. Ad esempio, `?v ?p "cat"@en` cercherà esplicitamente la parola "cat" marcata come lingua inglese.
	- esempio completo: `SELECT ?v WHERE { ?v ?p "cat“@en }`
- **Datatype (Tipi di dato):** Se un valore ha una tipizzazione specifica (es. un formato di data custom), dobbiamo indicarlo nella query unendo il valore e l'URI del tipo tramite il simbolo `^^`.
	- esempio completo `SELECT ?v WHERE { ?v ?p "abc"^^<http://example.org/datatype#specialDatatype> }`
- **Numeri (Boxing automatico):** Per i numeri semplici (interi o decimali), SPARQL ci semplifica la vita. Se scrivi semplicemente `42` nel tuo pattern, il motore fa un'operazione chiamata _boxing_: lo converte automaticamente nel formato esteso formale `"42"^^<http://www.w3.org/2001/XMLSchema#integer>`, risparmiandoti di doverlo scrivere per esteso ogni volta.
	- es: `SELECT ?v WHERE { ?v ?p 42 }` diventa `SELECT ?v WHERE { ?v ?p "42"^^<http://www.w3.org/2001/XMLSchema#integer> }`

### Gestire l'Anonimato: I Blank Nodes

A volte, nei grafi RDF, esistono dei nodi che raggruppano informazioni ma non possiedono un URI globale e univoco: sono chiamati **Blank Nodes** (nodi anonimi o bnodes).

- **Sintassi standard:** Nei risultati o nelle query, si rappresentano con il prefisso `_:` seguito da un'etichetta (es. `_:a` o `_:b57`).
	- esempio ```@prefix foaf: <http://xmlns.com/foaf/0.1/> .
_:a foaf:name "Alice" .
_:b foaf:name "Bob" .```
- **Il limite di validità (Scope):** C'è una regola d'oro: l'etichetta di un blank node ha senso _solo all'interno di quella specifica esecuzione della query_. Se ottieni il nodo `_:b57` oggi, e domani rifacendo la query ottieni di nuovo `_:b57`, non c'è alcuna garanzia che si tratti della stessa identica risorsa.
    
- **Sintassi alternativa:** SPARQL offre una comoda scorciatoia usando le parentesi quadre `[ ]`. Scrivere `[ :p "v" ]` equivale a inventare al volo un blank node e assegnargli una proprietà. Questo permette di annidare i pattern in modo molto compatto, come mostrato nell'ultimo esempio.
	- ![center|500](img/Pasted%20image%2020260516144515.png)
### Filtrare i Risultati: I Vincoli

Fino ad ora abbiamo visto come _cercare_ pattern, ma spesso vogliamo _scartare_ ciò che non ci serve. Qui entra in gioco la clausola **`FILTER`**.

Puoi usare `FILTER` per imporre restrizioni matematiche (es. `FILTER ?x < 3`) o per fare ricerche testuali complesse tramite le espressioni regolari (es. `FILTER regex(?name, "Smith")`).

Mostriamo quanto sia ricco il vocabolario a nostra disposizione (basato in gran parte sugli standard XPath e XQuery):

- **Operatori di confronto e logici:** I classici `<`, `>`, `=`, `&&` (AND), `||` (OR). Attenzione all'uguaglianza (`=`): per funzionare correttamente su tipi di dato inventati da te (custom), potrebbe richiedere estensioni specifiche del motore SPARQL, altrimenti conviene usare la funzione `sameTerm`.
    
- **Funzioni booleane:** Molto potenti per capire lo "stato" di una variabile. `isURI`, `isBlank` o `isLiteral` ti dicono che tipo di nodo hai di fronte.
    
- **La funzione BOUND:** È fondamentale. Restituisce _true_ se una variabile ha effettivamente ricevuto un valore durante il matching, e _false_ se è rimasta vuota. Affiancata al NOT (`!BOUND`), è la tecnica standard per implementare la _negation-as-failure_ (es. "trovami tutte le persone, filtrando via quelle per cui è _bound_ un'email", ovvero "trovami chi NON ha un'email").
- **Funzioni di estrazione:** `LANG` (estrae la lingua), `DATATYPE` (estrae il tipo), `STR` (converte in stringa semplice).

### Il Casting dei Dati

Lavorando con dati eterogenei, a volte devi forzare un tipo a diventare un altro (es. trasformare la stringa "123" in un numero intero per farci dei calcoli). SPARQL permette il **casting implicito**.

La tabella a doppia entrata mostra cosa si può trasformare in cosa:

- **Y (Yes):** Il casting è sempre permesso e sicuro (es. da un numero intero a una stringa).
    
- **N (No):** Il casting è impossibile o non ha senso logico (es. da una data `dT` a un valore booleano).
    
- **M (Maybe):** È la casistica più interessante. Il casting dipende dal valore specifico che si sta valutando in quel momento. Convertire una `str` (stringa) in un `int` (intero) funziona se la stringa contiene `"42"`, ma genera un errore se contiene `"Ciao"`.

![center|500](img/Pasted%20image%2020260516144835.png)

### Flessibilità Estrema: OPTIONAL e UNION

Questi due operatori sono la vera risposta di SPARQL alla natura frammentaria e destrutturata del Web.

**OPTIONAL (L'informazione aggiuntiva, se c'è):**

In un database SQL, se fai una `JOIN` rigida e manca un dato secondario, perdi l'intera riga. Nel Web Semantico i dati sono spesso incompleti. L'operatore `OPTIONAL` dice al motore: _"Cerca il Graph Pattern principale. Poi, se trovi anche questo pezzo di informazione opzionale, aggiungilo al risultato; se non lo trovi, non preoccuparti, dammi comunque i dati principali"_.

È **left-associativo**, il che significa che se metti in sequenza più blocchi `OPTIONAL`, vengono valutati in ordine da sinistra verso destra, appoggiandosi ai risultati del blocco precedente.

Infatti, la query 

```SPARQL
pattern OPTIONAL { pattern } OPTIONAL { pattern }
```

è equivalente a

```SPARQL
{ pattern OPTIONAL { pattern } } OPTIONAL { pattern }
```

***Esempio query con OPTIONAL***

```SPARQL
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name ?mbox
WHERE { ?x foaf:name ?name .
		OPTIONAL { ?x foaf:mbox ?mbox }
	}
```

Restituirà tutti quelli che hanno un foaf:name nel grafo e – se la hanno – ne riporterà la foaf:mbox.

**UNION (Gestire sinonimi e alternative):**

A volte le informazioni che cerchi sono espresse usando vocabolari (ontologie) differenti. Ad esempio, un database potrebbe definire una persona come `foaf:Person`, mentre un altro database unito al primo potrebbe chiamarla `stx:Person`.

L'operatore `UNION` agisce come un grande "OPPURE" logico (OR) a livello di pattern strutturali. Crea dei bivi: il motore cerca il pattern di sinistra, cerca il pattern di destra, e restituisce i risultati che unificano con **almeno uno** dei due scenari proposti.

***Esempio query con UNION***

```SPARQL
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX stx: <http://art.uniroma2.it/ontologies/st_example#>
SELECT ?guy
WHERE { { ?guy a foaf:Person } UNION { ?guy a stx:Person } }
```

In questo caso verranno restituite tutte le risorse definite come appartenenti alla classe stx:Person o anche alla classe foaf:Person
## L'Anatomia di un Dataset RDF 

In SPARQL, quando invii una query, non stai interrogando l'intero universo web, ma un recinto specifico che tu definisci, chiamato **Dataset RDF**.

Un Dataset RDF non è un blocco monolitico, ma ha un'architettura interna molto precisa. È composto da:

- **Un Grafo di Default (Default Graph o Background Graph):** È il "tavolo da lavoro" principale. Ce n'è sempre uno e uno solo. Non ha un nome esplicito (un URI) che lo identifica dall'esterno.
    
- **Zero o più Named Graphs (Grafi Nominati):** Sono grafi aggiuntivi, ciascuno chiaramente identificato da un proprio URI. Immaginali come delle cartelline etichettate che metti sul tavolo da lavoro.

Si possono popolare in questo modo

- Usando **`FROM <uri>`**, prendi il contenuto di quell'URI e lo svuoti nel Grafo di Default. Se usi più `FROM`, i contenuti vengono fusi insieme (_merge_).
    
- Usando **`FROM NAMED <uri>`**, prendi quel grafo e lo metti sul tavolo mantenendo la sua etichetta intatta. Diventa un _Named Graph_ a disposizione della query.

```SPARQL
FROM <http://art.uniroma2.it/ontologies/st_example>
FROM NAMED <http://xmlns.com/foaf/0.1/>
FROM NAMED <http://purl.org/dc/elements/1.1/>
```

### Sbrogliare la Confusione: Il Default Graph

 Affrontiamo uno dei punti più insidiosi delle specifiche SPARQL, che spesso confonde i neofiti. Cos'è esattamente questo _Default Graph_? La risposta dipende da cosa stai facendo.

**In fase di Lettura (SPARQL QUERY):**

Il Default Graph è l'ambiente dove la tua query `WHERE { ... }` cerca di unificare i pattern di base.

Come si forma?

1. Se **NON** usi nessuna clausola `FROM` o `FROM NAMED`, il database (Triple Store) usa il suo Default Graph interno (una fusione di tutto ciò che contiene, tipicamente).
    
2. Se usi **uno o più `FROM`**, il motore prende quei grafi, li fonde dinamicamente (_RDF Merge_) e **crea un nuovo Default Graph temporaneo** solo per la durata della tua query.
    

**In fase di Scrittura (SPARQL UPDATE - che qui viene solo accennato):**

Nelle operazioni di aggiornamento, il concetto cambia. Esiste un vero e proprio "Unnamed Graph" fisico nel database. Se scrivi nuovi dati senza specificare dove, andranno a finire lì.

**Regole d'Oro di Annullamento Reciproco:**

Si sottolinea un comportamento fondamentale (spesso sfuggito a chi legge velocemente le specifiche):

- Se metti **almeno un `FROM NAMED`** ma ti dimentichi di mettere dei `FROM`, il tuo Grafo di Default sarà **completamente vuoto**. La query base nel blocco `WHERE` non troverà nulla (a meno che non usi esplicitamente la keyword `GRAPH`).
    
- Viceversa, se metti **solo dei `FROM`**, avrai un Grafo di Default ricco, ma **nessun Named Graph** a disposizione.

### La Keyword GRAPH

Abbiamo visto come portare i Named Graphs nel nostro Dataset usando `FROM NAMED`. Ma come diciamo al motore: _"Ehi, per questa specifica parte della ricerca, non guardare nel mucchio principale (Default Graph), ma vai ad aprire quella specifica cartellina etichettata"_?

Qui entra in scena la potentissima keyword **`GRAPH`**.

**Uso Esplicito:**

Nel blocco `WHERE`, scrivi `GRAPH <uri> { ... }`.

Nell'esempio la query cerca le email delle persone che l'utente conosce. Ma lo fa inserendo una direttiva rigida: `GRAPH as:myfoaf.rdf`. Questo dice al motore: _"Smetti di cercare ovunque; per queste triple, guarda ESCLUSIVAMENTE all'interno del grafo `myfoaf.rdf`"_. Se l'informazione è altrove, verrà ignorata.

La query è 

```SPARQL
SELECT ?mail
WHERE GRAPH as:myfoaf.rdf {
?x          foaf:mbox <mailto:stellato@info.uniroma2.it> ;
            foaf:knows ?friend .
?friend     foaf:mbox ?mail
}
```

**Uso con Variabili:**

La vera magia si ottiene usando una variabile dopo `GRAPH`: `GRAPH ?variabile { ... }`.

In questo caso, stai dicendo: _"Trovami qualsiasi Named Graph (e memorizza il suo URI in `?graph`) in cui sia vero che il creatore si chiama 'Armando'"_. È una meta-interrogazione formidabile: non stai solo estraendo dati, ma stai anche chiedendo al sistema _in quale contenitore_ si trovano quei dati.

La query è

```SPARQL
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
SELECT ?graph, ?creator
WHERE GRAPH ?graph {
	?graph dc:creator ?creator .
	?creator foaf:name “Armando“.
}
```

**Intersessione tra Grafi**

Mettiamo insieme tutti i pezzi del puzzle in una query complessa e molto intelligente. È il manifesto di perché il Web Semantico si chiama così.

**L'obiettivo:** Trovare le email (`?mbox`) e i soprannomi (`?nick`) delle persone conosciute da Alice.

**I Dati a disposizione (`FROM NAMED`):**

Abbiamo importato due Named Graphs: il file profilo di Alice (`aliceFoaf`) e il file profilo di Bob (`bobFoaf`).

**La Logica del blocco WHERE:**

La query si divide in due blocchi, diretti verso grafi diversi:

1. **Primo blocco (`GRAPH data:aliceFoaf`):** Il motore entra nel file di Alice. Trova l'URI di Alice tramite la sua email. Poi cerca chi lei conosce (`?whom`).
    
    Ora la parte geniale: Alice potrebbe aver scritto nel suo file i soprannomi dei suoi amici, ma la query sceglie di ignorarli. Invece, estrae l'email degli amici e cerca un link (tramite la proprietà `rdfs:seeAlso`) che punta al _Personal Profile Document_ (PPD) di questi amici. L'URI di questo documento viene salvato nella variabile `?ppd`.
    
2. **Secondo blocco (`GRAPH ?ppd`):**
    
    Il motore usa l'URI appena trovato (`?ppd`) come bersaglio per il comando `GRAPH`. Praticamente dice: _"Ora apri il file profilo dell'amico che ho appena scoperto"_. Una volta dentro, cerca l'email (`?mbox` per assicurarsi di parlare della stessa persona) e preleva il soprannome (`?nick`) direttamente dalla fonte originale (il documento dell'amico, non quello di Alice).

![center|500](img/Pasted%20image%2020260516151213.png)

**La morale dell'esempio:** Questa query sfrutta il concetto di **Linked Data**. Non si fida della copia locale delle informazioni (ciò che Alice dice dei suoi amici), ma segue i link (gli URI dei documenti) per saltare dinamicamente da un grafo all'altro e recuperare l'informazione alla sorgente autorevole.

## I Modificatori di Sequenza

Quando il blocco `WHERE` finisce il suo lavoro, produce un insieme di soluzioni "grezzo" e **non ordinato**. È come se avesse buttato tutte le risposte trovate in un grande cesto.

Per trasformare questo cesto in una lista pulita e navigabile, SPARQL applica i modificatori di sequenza, comportandosi in modo molto simile a SQL. L'ordine di applicazione teorico è quello elencato: si ordina, si proietta (si scelgono le colonne), si rimuovono i duplicati, e infine si taglia la lista (con offset e limit).
### Mettere in ordine: ORDER BY

L'operatore `ORDER BY` serve a dare un senso logico alla lista, ordinando i risultati in base a una o più variabili.

- Puoi scegliere l'ordine ascendente (il default, oppure esplicitato con `ASC()`) o discendente (`DESC()`).
    
- Nell'esempio della slide, i risultati vengono ordinati per nome in ordine alfabetico, e a parità di nome, per ID impiegato in ordine decrescente (`ORDER BY ?name DESC(?emp)`).

```SPARQL
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name
WHERE { ?x foaf:name ?name ; :empId ?emp }
ORDER BY ?name DESC(?emp)
```

**Una particolarità di SPARQL:** In SQL ordini stringhe o numeri. Nel Web Semantico devi ordinare entità astratte (URI, Blank Nodes, ecc.). Come si fa? La slide ci fornisce la gerarchia rigorosa stabilita dal W3C quando i tipi non sono direttamente comparabili:

1. **Nessun valore:** Le variabili vuote ("unbound") finiscono in cima alla lista.
    
2. **Blank nodes:** Vengono prima degli URI.
    
3. **IRIs (o URIs):** Gli indirizzi web delle risorse.
    
4. **RDF literals:** I valori testuali puri (che a loro volta vengono comparati come stringhe semplici se non hanno un tipo di dato specifico).
### Pulire la lista: DISTINCT e REDUCED

Spesso, interrogando grafi complessi, otterrai risultati doppi. Per pulire la lista hai due armi:

- **DISTINCT:** È l'operatore drastico e garantito. Controlla l'intera lista finale e garantisce che ogni riga sia assolutamente unica. Se trova dei duplicati perfetti, li elimina.
    
- **REDUCED:** È una peculiarità di SPARQL. Funziona come una "raccomandazione" al motore di ricerca. Permette (ma non obbliga) il sistema di eliminare _alcuni_ duplicati.
    
    - _Perché usarlo?_ Il `DISTINCT` costringe il database a confrontare ogni risultato con tutti gli altri, il che richiede un'enorme quantità di memoria e potenza di calcolo su database giganteschi. Il `REDUCED` permette al database di fare un lavoro di pulizia "leggero" (ad esempio eliminando solo i duplicati consecutivi) per risparmiare risorse, offrendo prestazioni migliori quando l'unicità assoluta non è strettamente necessaria per la tua applicazione.

![center|500](img/Pasted%20image%2020260516152022.png)
### La Paginazione: LIMIT e OFFSET

Questi due modificatori sono i migliori amici di chi sviluppa interfacce web, perché agiscono esclusivamente sulla **posizione** dei risultati e non sul loro contenuto.

- **LIMIT:** Taglia la lista dal basso. `LIMIT 20` significa "fermati dopo avermi dato i primi 20 risultati".
    
- **OFFSET:** Taglia la lista dall'alto. `OFFSET 10` significa "ignora i primi 10 risultati e inizia a restituirmi i dati dall'undicesimo in poi".

![center|500](img/Pasted%20image%2020260516152145.png)

_Nota pratica fondamentale:_ Hanno senso logico **solo se usati in combinazione con `ORDER BY`**. Se non imponi un ordine, il cesto dei risultati è casuale. Chiedere di saltare i primi 10 risultati (`OFFSET 10`) da una lista non ordinata significa rischiare di saltare dati diversi ad ogni esecuzione della query!

## L'Output Finale: Le Query Forms

Ora che la sequenza è perfetta, in che formato vogliamo riceverla? SPARQL offre quattro "forme" di output (Query Forms). Finora avevamo visto solo la prima.

**1. SELECT: La Tabella**

È la forma classica. Restituisce un _Result Set_ tabulare. Tu definisci quali variabili (colonne) vuoi proiettare. Se usi `SELECT *`, ti restituirà tutte le variabili che hai usato nel blocco `WHERE`.

**2. CONSTRUCT: Il Traduttore di Grafi**

Questa è una delle funzioni più brillanti di SPARQL. Invece di restituire una tabella, restituisce un **nuovo Grafo RDF**.

Come funziona? Tu gli fornisci un "Template" (uno stampino) fatto di triple che contengono variabili. Il motore prende le soluzioni trovate dal `WHERE` e le inietta nello stampino, generando triple nuove di zecca.

- _A cosa serve?_ È perfetto per l'integrazione dei dati. Nell'esempio della slide 6, il sistema cerca tutte le risorse definite come `stx:Person` nel database sorgente, e in output "costruisce" un nuovo grafo in cui le stesse identiche persone sono taggate usando il vocabolario `foaf:Person`. In pratica, hai tradotto un database da una lingua (ontologia) all'altra in un solo colpo!
    
- _Sicurezza:_ Se una variabile risulta vuota e crea una tripla grammaticalmente scorretta in RDF, SPARQL la scarta silenziosamente senza farti crashare la query.

```SPARQL
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX stx: <http://art.uniroma2.it/ontologies/st_example#>
CONSTRUCT { ?p a foaf:Person }
WHERE { ?p a stx:Person}
```

**3. ASK: La Domanda Chiusa**

Restituisce semplicemente un valore booleano: **True** o **False**.

_"Esiste almeno un impiegato che si chiama Mario Rossi e lavora a Tor Vergata?"_ Se il `WHERE` unifica almeno una volta, restituisce True, altrimenti False. È velocissimo perché non deve trasferire i dati, deve solo verificare l'esistenza del pattern.

**4. DESCRIBE: L'Esploratore**

Anche questo restituisce un Grafo RDF, ma a differenza della `CONSTRUCT`, non devi fornirgli uno stampino. Gli passi semplicemente l'URI di una risorsa (o una variabile) e gli dici: _"Raccontami tutto quello che sai su questo oggetto"_.

- Nell'esempio della slide 7, si chiede il `DESCRIBE` dell'impiegato con ID "1234". Il risultato non è una tabella, ma un vero e proprio documento RDF strutturato che elenca tutte le proprietà di quell'impiegato (nome, cognome, mailbox, ecc.).
    
- _Attenzione:_ Come specifica la nota a piè di pagina nella slide, cosa significhi "tutto quello che sai" dipende da chi ha programmato il database. Di solito, un Triple Store restituirà tutte le triple in cui l'impiegato 1234 compare come _Soggetto_, e talvolta anche quelle in cui compare come _Oggetto_, offrendoti una fotografia completa a 360 gradi del nodo richiesto.

![center|500](img/Pasted%20image%2020260516152331.png)

---
# SPARQL 1.1

Questo è un passaggio fondamentale! Con l'introduzione di **SPARQL 1.1**, il linguaggio ha fatto un salto di qualità enorme, colmando molte delle lacune che lo separavano dai classici database SQL e diventando uno strumento maturo e incredibilmente potente.

## Aggregazione: Calcolare e Raggruppare

In SPARQL 1.0 potevi estrarre i dati, ma non potevi farci dei calcoli sopra (ad esempio, contare quanti amici ha una persona o calcolare l'età media). SPARQL 1.1 risolve questo problema introducendo l'**Aggregazione**.

Il meccanismo si basa su due pilastri presi in prestito da SQL:

- **`GROUP BY`**: Permette di raggruppare i risultati in base a una o più variabili. Se hai una lista di 100 impiegati divisi in 3 dipartimenti, raggruppando per dipartimento otterrai 3 grandi "cesti".
    
- **Operatori di Aggregazione**: Una volta creati i cesti, puoi applicarci delle funzioni matematiche o statistiche:
    
    - `COUNT`: Conta quanti elementi ci sono nel cesto.
        
    - `SUM`, `AVG`, `MIN`, `MAX`: Somma, Media, Minimo e Massimo.
        
    - `GROUP_CONCAT`: Prende tutte le stringhe del cesto e le unisce in un'unica lunga stringa (utilissimo!).
        
    - `SAMPLE`: Pesca un valore a caso dal cesto.
        

**L'esempio pratico:**

Snippet di codice

```SPARQL
SELECT ?x (AVG(?size) AS ?asize)
WHERE { ?x :size ?size }
GROUP BY ?x
HAVING(AVG(?size) > 10)
```

Qui si estraggono degli elementi (`?x`) e le loro dimensioni (`?size`). Il motore raggruppa tutto per `?x` e ne calcola la media (`AVG`).

La novità aggiuntiva è **`HAVING`**: funziona esattamente come un `FILTER`, ma agisce _dopo_ che i gruppi sono stati creati. In questo caso, dice: _"Restituiscimi i risultati solo se la media che hai appena calcolato è maggiore di 10"_. Da notare anche l'uso di **`AS`**, che permette di "ribattezzare" il risultato del calcolo assegnandolo a una nuova variabile (`?asize`) per poterla visualizzare nei risultati.
## Subquery: Le Matrioske di SPARQL

A volte, per rispondere a una domanda complessa, devi prima rispondere a una domanda più piccola e usare quel risultato come base di partenza. Le **Subquery** (query annidate) permettono esattamente questo.

- **Come funzionano:** Si inserisce una normale query `SELECT` all'interno del blocco `WHERE` di un'altra query.
    
- **L'ordine di esecuzione:** Il motore SPARQL risolve _sempre_ prima la query più interna, e poi passa i risultati a quella esterna. Questo è vitale per forzare il sistema a eseguire le operazioni nell'ordine che vogliamo noi.
    

**L'esempio pratico:**

Il database contiene Alice, Bob e Carol. Bob e Carol hanno diversi nomi/soprannomi registrati ("Bob", "B. Bar", ecc.). Vogliamo sapere chi conosce Alice e, per ciascuna di queste persone, vogliamo estrarre _solo_ il nome che viene prima in ordine alfabetico.

- **Query Interna:** Raggruppa tutte le persone (`GROUP BY ?y`) e, usando la funzione `MIN(?name)`, calcola qual è il nome alfabeticamente "più piccolo" per ciascuno, salvandolo come `?minName`.
    
- **Query Esterna:** Chiede semplicemente: _"Chi conosce Alice? (`:alice :knows ?y`)"_. A questo punto incrocia questa informazione con la tabellina generata dalla query interna.
    
    Risultato: Bob viene associato a "B. Bar" e Carol a "C. Baz". Senza le subquery, fare questa operazione in un colpo solo sarebbe stato quasi impossibile!

```SPARQL
PREFIX : <http://people.example/>
PREFIX : <http://people.example/>
SELECT ?y ?minName
WHERE {
:alice :knows ?y .
{
	SELECT ?y (MIN(?name) AS ?minName)
	WHERE {
		?y :name ?name .
		} GROUP BY ?y
	}
}
```
## Negazione

Questa è forse una delle aggiunte più amate dagli sviluppatori. Nelle slide precedenti avevamo visto che per fare una negazione in SPARQL 1.0 (es. "Trovami chi NON ha un'email") si doveva usare un trucco macchinoso: `OPTIONAL` accoppiato a un `FILTER(!BOUND)`.

In SPARQL 1.1, la negazione diventa nativa e si sdoppia in due costrutti simili ma con sfumature diverse:

**A. `NOT EXISTS`**

Si usa all'interno di un `FILTER`. Il motore valuta il pattern principale e, per ogni risultato trovato, va a sbirciare dentro il blocco `NOT EXISTS`. Se il pattern interno unifica (cioè esiste), il risultato viene scartato.

- _Esempio:_ Trova tutte le entità di tipo Persona, ma scarta quelle che possiedono la proprietà `foaf:name`. Nel database, Alice ha un nome, Bob no. Il risultato sarà solo Bob.

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?person
WHERE {
	?person rdf:type foaf:Person .
	FILTER NOT EXISTS { ?person foaf:name ?name }
}
```

**B. `MINUS`**

Questo è un operatore di pura **sottrazione di insiemi**. Il motore calcola _tutti_ i risultati del blocco principale. Poi calcola _tutti_ i risultati del blocco `MINUS`. Infine, sottrae la seconda tabella dalla prima.

- _Esempio:_ Trova tutti i soggetti (`?s`) nel grafo. Ora, usando `MINUS`, togli da questa lista tutti i soggetti che hanno come nome di battesimo "Bob". Il risultato includerà Carol e Alice, ma l'intero record di Bob verrà spazzato via.

```SPARQL
PREFIX : <http://example/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT DISTINCT ?s
WHERE {
	?s ?p ?o .
	MINUS {
		?s foaf:givenName "Bob" .
	}
}
```

_(Nota tecnica: Sebbene spesso diano lo stesso risultato, `NOT EXISTS` si basa sull'esistenza di un pattern nel grafo contestuale, mentre `MINUS` fa una vera e propria sottrazione tra due insiemi di risultati già calcolati. Nella pratica quotidiana, `NOT EXISTS` è quello più sicuro e utilizzato nella maggior parte dei casi)._

Eccoci arrivati a due delle funzionalità di SPARQL 1.1 che ti cambieranno letteralmente la vita quando scriverai query complesse: i **Property Path** (percorsi tra le proprietà) e l'**Assegnazione** (la capacità di creare o forzare dati "al volo").

Queste due novità rendono il codice infinitamente più pulito, compatto e potente. Vediamo perché.
## Property Path

In SPARQL 1.0, se volevi trovare "il nome della persona conosciuta dalla persona conosciuta da Alice" (un amico di un amico), dovevi creare una catena di triple usando un sacco di variabili temporanee (es. `?a1`, `?a2`) che non ti interessavano minimamente, solo per fare da "ponte".

I **Property Path** risolvono questo problema, permettendoti di usare una sintassi molto simile alle espressioni regolari per concatenare i predicati (le frecce del grafo).

![center|500](img/Pasted%20image%2020260516162918.png)

Ecco i superpoteri che ti mettono a disposizione:

- **La Sequenza (`/`):** Invece di scrivere tre triple separate, puoi usare lo slash (`/`) per dire al motore di seguire un percorso dritto. `foaf:knows/foaf:knows/foaf:name` significa _"segui la prima freccia 'knows', poi da lì segui un'altra freccia 'knows', e infine segui la freccia 'name'"_. Tutto in una riga, senza variabili inutili!
	- ![center|500](img/Pasted%20image%2020260516162955.png)
- **Il Percorso Inverso (`^`):** In RDF, le frecce hanno una direzione fissa (da Soggetto a Oggetto). Ma cosa succede se vuoi risalire la corrente? Usi il simbolo dell'accento circonflesso (`^`). Nella Slide 3 c'è un esempio geniale: `?x foaf:knows/^foaf:knows ?y`. Questo significa _"Trovami un `?x` che conosce qualcuno, e partendo da questo 'qualcuno', vai all'indietro per trovare un `?y` che lo conosce"_. In pratica, stai trovando due persone (`?x` e `?y`) che hanno una conoscenza in comune!
	- ![center|500](img/Pasted%20image%2020260516163026.png)
- **L'Alternativa (`|`):** Permette di creare dei bivi. Ad esempio, `foaf:name | rdfs:label` dice al motore _"cerca la proprietà nome, ma se non la trovi, mi va bene anche la proprietà label"_.
- **La Transitività, il vero Santo Graal (`*` e `+`):** Questa è la funzione più potente in assoluto. Se vuoi trovare _tutti_ gli amici di Alice, e gli amici degli amici, e così via per tutta la rete, quante volte devi ripetere `foaf:knows`? Non puoi saperlo a priori.
    
    - Usando il **Più (`+`)**, es. `foaf:knows+`, dici _"segui questa freccia da 1 a infinite volte"_.
        
    - Usando l'**Asterisco (`*`)**, dici _"segui questa freccia da 0 a infinite volte"_. È usatissimo nelle ontologie (es. `rdfs:subClassOf*`) per trovare tutte le super-classi di un oggetto esplorando l'intero albero gerarchico fino alla radice.
    - ![center|500](img/Pasted%20image%2020260516163326.png)
## L'Assegnazione

Fino a SPARQL 1.0, potevi solo estrarre i dati così com'erano scritti nel database. Se avevi il Prezzo Lordo e lo Sconto, e volevi il Prezzo Netto, dovevi estrarli entrambi e fare il calcolo nel tuo programma (in Java, Python, ecc.).

Con SPARQL 1.1 puoi fare in modo che sia il motore del database a fare il lavoro per te.

**La Regola d'Oro:**

Quando crei una nuova variabile tramite assegnazione, questa **deve essere vergine**, ovvero non deve essere mai stata usata prima in quel punto della query.

Ci sono due strumenti principali per l'assegnazione:

**A. Il costrutto BIND: Il Calcolatore**

`BIND` prende un'espressione, la calcola per ogni singola soluzione trovata, e "lega" (bind) il risultato a una nuova variabile.

- _Calcoli Matematici:_ Nel primo esempio, il database ha `?p` (il prezzo) e `?discount`. Con `BIND (?p*(1-?discount) AS ?price)` diciamo al motore di calcolare lo sconto riga per riga e di salvare il risultato finale nella nuova variabile `?price`, che ora possiamo usare tranquillamente nei filtri successivi (es. `FILTER(?price < 20)`).
	- ![center|500](img/Pasted%20image%2020260516163447.png)
- _Manipolazione di Stringhe:_ Nel secondo esempio, usiamo `BIND` insieme alla funzione `CONCAT`. Prendiamo il nome (`?G`) e il cognome (`?S`) che nel database sono separati, ci mettiamo uno spazio in mezzo, e creiamo al volo la variabile `?name` con il nome completo bello e formattato.
	- ![center|500](img/Pasted%20image%2020260516163505.png)

**B. Il costrutto VALUES: L'Iniettore**

Mentre `BIND` calcola valori nuovi partendo da variabili esistenti, `VALUES` fa l'opposto: "inietta" valori specifici e predeterminati dentro una variabile all'inizio della query.

- Nell'esempio: `VALUES ?book { :book1 :book3 }`.
	- ![center|500](img/Pasted%20image%2020260516163655.png)
- A cosa serve? Immagina di avere un database con milioni di libri, ma a te interessano i dati _solo ed esclusivamente_ di `book1` e `book3` (magari perché l'utente li ha selezionati da una spunta sul sito web). Usando `VALUES`, costringi la variabile `?book` ad assumere solo quei due specifici URI. Il motore ignorerà tutto il resto del database e cercherà il titolo e il prezzo solo per quei due libri specifici, rendendo la query incredibilmente veloce e mirata.

## Update dei dati RDF
### Dati Statici vs. Pattern Dinamici

Prima di scendere nei dettagli, mettiamo in chiaro una distinzione fondamentale nella sintassi di aggiornamento di SPARQL. Per inserire o cancellare dati, hai due "modalità":

- **La modalità `DATA` (`INSERT DATA` / `DELETE DATA`):** La usi quando sai _esattamente_ cosa vuoi aggiungere o togliere. In questa modalità **non puoi usare variabili** (`?x`). Devi scrivere le triple per esteso, inserendo gli URI e i valori esatti.
    
- **La modalità dinamica (`INSERT` / `DELETE`):** La usi quando vuoi modificare i dati basandoti su una ricerca. Questa modalità lavora obbligatoriamente in coppia con una clausola **`WHERE`**. Il motore prima cerca i dati usando il Graph Pattern (le variabili), e poi usa i risultati trovati per decidere cosa inserire o cancellare.

### Aggiungere informazioni: INSERT e INSERT DATA

Qui mostriamo visivamente questa differenza.

- **Esempio (`INSERT DATA`):** È l'operazione più semplice. Stiamo letteralmente prendendo un nuovo libro (`<http://example/book1>`), gli diamo un titolo e un autore, e lo "appoggiamo" nel nostro database. Essendo dati espliciti e costanti, usiamo `INSERT DATA`.
	- ![center|500](img/Pasted%20image%2020260516164050.png)
- **Esempio (`INSERT` con `WHERE`):** Qui la faccenda è più sofisticata. Vogliamo copiare tutti i libri pubblicati dopo il 1970 dal nostro archivio principale e inserirli in un nuovo grafo dedicato chiamato `bookStore2`.
    
    - Prima, il blocco `WHERE` cerca nel grafo originale (`bookStore`) tutti i libri e filtra le date.
        
    - Poi, il blocco `INSERT` prende le variabili valorizzate (`?book`, `?p`, `?v`) e inietta queste triple nel nuovo grafo. È una sorta di "Copia-Incolla intelligente".
    - ![center|500](img/Pasted%20image%2020260516164115.png)

### Rimuovere informazioni: DELETE e DELETE DATA 

La logica della cancellazione è perfettamente speculare a quella dell'inserimento.

- **Esempio (`DELETE DATA`):** Hai fatto un errore di inserimento e vuoi eliminare esattamente la tripla che dice che "David Copperfield" è stato scritto da "Edmund Wells". Scrivi l'URI esatto del libro, il titolo esatto, e il motore rimuove chirurgicamente quella specifica informazione dal grafo.
	- ![center|500](img/Pasted%20image%2020260516164215.png)
- **Esempio (`DELETE` con `WHERE`):** Questo è potente (e pericoloso!). Supponiamo tu voglia fare pulizia nel database. Il blocco `WHERE` individua tutti i libri precedenti al 1970. Il blocco `DELETE` prende queste variabili e distrugge tutte le triple ad esse associate. È l'equivalente di una cancellazione massiva (bulk delete).
	- ![center|500](img/Pasted%20image%2020260516164159.png)

### L'arte del "Rinomina": DELETE + INSERT (Slide 4)

Questa è una slide cruciale per capire la filosofia del Web Semantico. Se in SQL vuoi cambiare il nome di una persona da "Bill" a "William", usi il comando `UPDATE`.

In RDF (e quindi in SPARQL), **il comando `UPDATE` per modificare un singolo valore non esiste**. Poiché tutto è basato su "triple" immutabili (Soggetto-Predicato-Oggetto), per cambiare un'informazione devi _distruggere la vecchia tripla e crearne una nuova_.

Ecco perché SPARQL ti permette di combinare `DELETE` e `INSERT` in un'unica query atomica:

1. Si usa la clausola **`WITH`** per dire al motore: _"Tutte le operazioni che seguono, falle all'interno di questo specifico grafo (addresses)"_. (In alternativa potevi usare le keyword `GRAPH` dentro le parentesi graffe).
    
2. Il blocco `WHERE` individua la persona il cui nome attuale è "Bill".
    
3. Il blocco `DELETE` rimuove la tripla con il nome vecchio.
    
4. Il blocco `INSERT` crea la tripla con il nome nuovo ("William").
    
![center|500](img/Pasted%20image%2020260516164309.png)

Tutto questo avviene in un colpo solo. Se salta la corrente a metà operazione, il database non rimane in uno stato inconsistente (senza nome o con due nomi).

### LOAD e CLEAR

Infine, ci sono due comandi pensati per la gestione macroscopica del database, per spostare "scatoloni" interi di dati invece che singole triple.

- **`LOAD`:** È il muletto del Triple Store. Gli dai l'URL di un file RDF (es. un'ontologia trovata su internet o un file locale) e lui scarica tutto il contenuto e lo inietta nel tuo database. Puoi specificare il grafo di destinazione con `INTO GRAPH`. L'opzione facoltativa `SILENT` è molto comoda: dice al motore _"Se il file non esiste o il link è rotto, non mandare in crash l'intero sistema con un errore, fai finta di niente e vai avanti"_.
	- ![center|500](img/Pasted%20image%2020260516164354.png)
- **`CLEAR`:** È il bulldozer. `CLEAR GRAPH <uri>` rade al suolo un intero grafo nominato, svuotandolo completamente in un istante. Come mostra il riquadro in basso nella slide, è semplicemente una scorciatoia (molto più veloce e ottimizzata dal punto di vista computazionale) per scrivere una noiosissima query che dice: _"Trova ogni singolo Soggetto, Predicato e Oggetto in questo grafo, e cancellali tutti"_.
	- ![center|500](img/Pasted%20image%2020260516164412.png)

