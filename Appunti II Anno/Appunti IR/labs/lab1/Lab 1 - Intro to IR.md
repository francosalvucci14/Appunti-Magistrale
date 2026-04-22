# 🧠 Laboratorio 1.1 – Introduction to Information Retrieval

**Corso:** Information Retrieval – Laurea Magistrale in Informatica  
**Università:** Roma “Tor Vergata”  
**Docente:** Danilo Croce

---

## 🎯 Obiettivo del laboratorio

In questo notebook costruiremo passo dopo passo una versione semplificata di un sistema di **Information Retrieval (IR)**, cioè un sistema capace di trovare documenti rilevanti rispetto a un bisogno informativo espresso da un utente.

L’idea del laboratorio è alternare:
- brevi spiegazioni teoriche
- esempi concreti
- codice Python eseguibile
- piccoli esercizi di osservazione

L’obiettivo non è costruire subito un motore di ricerca realistico, ma comprendere con chiarezza le **strutture dati** e i **meccanismi di base** che rendono possibile la ricerca documentale.

---

## 📖 Che cos’è l’Information Retrieval?

L’**Information Retrieval** si occupa di trovare materiale rilevante, di solito documenti testuali non strutturati, all’interno di una collezione di grandi dimensioni.

Oggi il primo esempio che viene in mente è spesso il **web search**, ma i casi d’uso sono molto più ampi. Alcuni esempi tipici sono:
- motori di ricerca sul Web
- ricerca nelle email
- ricerca nei file del proprio computer
- ricerca in archivi aziendali
- ricerca in basi documentali giuridiche o tecniche

L’Information Retrieval è quindi lo studio di come rappresentare, indicizzare e recuperare documenti in modo efficace rispetto a una richiesta dell’utente.

---

## 🧩 Concetti chiave

Nel laboratorio useremo alcuni concetti fondamentali:

- **Collection**: insieme dei documenti su cui effettuiamo la ricerca
- **Document**: una singola unità testuale della collezione
- **Information need**: ciò che l’utente vuole davvero sapere
- **Query**: la formulazione testuale con cui l’utente esprime il proprio bisogno informativo
- **Relevance**: quanto un documento è utile rispetto al bisogno informativo dell’utente

Questi concetti sono centrali perché un sistema di IR non lavora direttamente sul “vero intento” dell’utente, ma solo sulla **query** che l’utente riesce a formulare.

---

## 💡 Esempio: information need vs query

Un utente potrebbe avere questo bisogno informativo:

> “Voglio trovare un modo per catturare un topo senza ucciderlo.”

Ma potrebbe formulare la query come:

> `how to trap a mouse alive`

Notiamo subito che **information need** e **query** non coincidono sempre perfettamente.

La query è solo una rappresentazione parziale, spesso incompleta o imperfetta, del bisogno informativo reale.  
Questa differenza è uno dei motivi per cui l’Information Retrieval è un problema interessante: il sistema deve cercare documenti utili partendo da una formulazione linguistica che può essere ambigua, incompleta o poco precisa.

---

## 🧪 Obiettivo pratico

Per rendere il laboratorio concreto, lavoreremo su una piccola collezione di documenti e costruiremo progressivamente:

1. una rappresentazione dei documenti
2. una **term-document incidence matrix**
3. un **inverted index**
4. semplici operazioni di **query processing**
5. una prima gestione delle **phrase query** tramite **positional index**

Questo approccio ci permetterà di capire bene la logica dei sistemi di retrieval prima di passare, nei laboratori successivi, a collezioni più grandi e realistiche.

---

## 🎓 Risultati di apprendimento attesi

Al termine del laboratorio lo studente dovrebbe essere in grado di:

- descrivere il problema affrontato dall’Information Retrieval
- distinguere tra **information need** e **query**
- rappresentare una collezione testuale tramite termini e documenti
- comprendere il funzionamento di una **term-document incidence matrix**
- costruire un semplice **inverted index**
- eseguire query booleane di base
- capire perché le phrase query richiedono un **positional index**

---

## ▶️ Struttura del notebook

Il laboratorio segue un percorso progressivo:

1. introduzione ai concetti di base dell’Information Retrieval  
2. costruzione di una piccola collezione di documenti  
3. tokenizzazione e costruzione del vocabolario  
4. term-document incidence matrix  
5. inverted index  
6. query processing con merge di postings lists  
7. phrase query e positional index  
8. esercizi finali

---
# Mini-collezione di documenti su cui lavoreremo nel laboratorio

```python
documents = {
    1: "Brutus killed Caesar",
    2: "Caesar was killed by Brutus",
    3: "Rome was a powerful republic",
    4: "Brutus and Cassius planned against Caesar",
    5: "Cleopatra met Caesar in Egypt"
}

print("Collection of documents:\n")

for doc_id, text in documents.items():
    print(f"Doc {doc_id}: {text}")
```
## Osservazione
In un sistema reale, la collezione può contenere milioni di documenti.  
Nel nostro caso useremo una collezione molto piccola, utile per capire bene i meccanismi interni dei sistemi di Information Retrieval.

Ogni documento è identificato da un **docID**, cioè un identificatore numerico univoco.  
Questa scelta sarà utile più avanti quando costruiremo l'**inverted index**.
## Dal testo ai termini: tokenizzazione

I documenti, così come sono scritti in linguaggio naturale, non sono ancora nella forma più comoda per essere elaborati da un sistema di Information Retrieval.

Un primo passo consiste nella **tokenizzazione**, cioè nella suddivisione del testo in unità elementari chiamate **token**.  
In molti casi, i token corrispondono semplicemente alle parole.

Per semplicità, in questo laboratorio useremo una tokenizzazione molto basilare:
- convertiamo tutto in minuscolo
- separiamo il testo in parole usando gli spazi

In sistemi reali, questo passaggio è più complesso e può includere:
- rimozione della punteggiatura
- gestione di apostrofi e forme contratte
- normalizzazione
- stemming o lemmatizzazione
- rimozione delle stopwords

## Obiettivo di questa sezione
Trasformare ogni documento in una lista di termini e costruire il **vocabolario** dell'intera collezione.

Il **vocabolario** è l'insieme di tutti i termini distinti presenti nei documenti.

```python
# Tokenizzazione molto semplice: lowercase + split su spazi

tokenized_documents = {}

for doc_id, text in documents.items():
    tokens = text.lower().split()
    tokenized_documents[doc_id] = tokens

print("Tokenized documents:\n")

for doc_id, tokens in tokenized_documents.items():
    print(f"Doc {doc_id}: {tokens}")
```
## Osservazione

Dopo la tokenizzazione, ogni documento viene rappresentato come una sequenza di termini.

Ad esempio, il documento:

`Brutus killed Caesar`

diventa:

`['brutus', 'killed', 'caesar']`

Questa rappresentazione è già più adatta alla costruzione di strutture dati per la ricerca.

Il passo successivo consiste nel costruire il **vocabolario globale** della collezione, cioè la lista ordinata di tutti i termini distinti.

```python
# Costruzione del vocabolario: insieme di tutti i termini distinti

vocabulary = sorted(set(
    token
    for tokens in tokenized_documents.values()
    for token in tokens
))

print("Vocabulary:\n")
print(vocabulary)
print(f"\nNumber of distinct terms: {len(vocabulary)}")
```
## Perché il vocabolario è importante?

Il vocabolario è una componente centrale nei sistemi di Information Retrieval perché permette di:

- sapere quali termini compaiono nella collezione
- costruire una **term-document incidence matrix**
- costruire un **inverted index**
- analizzare la frequenza dei termini

Nei sistemi reali, il vocabolario può contenere da migliaia a milioni di termini distinti.
Nel nostro esempio, invece, la dimensione è volutamente piccola per rendere i passaggi trasparenti.

```python
print("Vocabulary with index:\n")

for i, term in enumerate(vocabulary):
    print(f"{i:2d} -> {term}")
```
## Term-document incidence matrix

Una volta costruito il vocabolario, possiamo rappresentare la collezione tramite una **term-document incidence matrix**.

### Idea
- ogni **riga** corrisponde a un termine del vocabolario
- ogni **colonna** corrisponde a un documento
- l'elemento in posizione `(termine, documento)` vale:
  - **1** se il termine compare nel documento
  - **0** altrimenti

Questa rappresentazione è utile per capire il modello booleano di retrieval:
una query come

`brutus AND caesar`

può essere vista come un'operazione logica tra vettori binari.

### Limite importante
La term-document matrix è molto utile dal punto di vista concettuale, ma non è adatta a collezioni grandi:
nella pratica, quasi tutte le celle sono 0, quindi la matrice è molto **sparsa**.

Per questo motivo, nei sistemi reali si preferisce una struttura molto più efficiente: l'**inverted index**.

```python
# Costruzione della term-document incidence matrix come dizionario di liste

incidence_matrix = {}

for term in vocabulary:
    row = []
    for doc_id in documents:
        row.append(1 if term in tokenized_documents[doc_id] else 0)
    incidence_matrix[term] = row

print("Term-document incidence matrix:\n")

header = "term".ljust(15) + "".join([f"D{doc_id}".rjust(5) for doc_id in documents])
print(header)
print("-" * len(header))

for term, row in incidence_matrix.items():
    row_str = "".join([str(value).rjust(5) for value in row])
    print(term.ljust(15) + row_str)
```
## Come leggere la matrice

Se una riga contiene i valori:

`[1, 1, 0, 1, 0]`

significa che il termine compare nei documenti:
- 1
- 2
- 4

e non compare nei documenti:
- 3
- 5

In altre parole, ogni riga può essere interpretata come un **vettore di incidenza** del termine nella collezione.

```python
# Mostriamo esplicitamente alcuni incidence vectors utili per il retrieval booleano

terms_to_inspect = ["brutus", "caesar", "cleopatra"]

for term in terms_to_inspect:
    print(f"{term:10s} -> {incidence_matrix[term]}")
```
## Dalla matrice alle query booleane

Nel modello booleano, una query viene interpretata come un'espressione logica.

Per esempio:

`brutus AND caesar`

significa: restituisci i documenti che contengono **entrambi** i termini.

Dal punto di vista della matrice, questo equivale a fare un **AND bit a bit** tra i due vettori di incidenza.

Allo stesso modo:
- `OR` corrisponde a una disgiunzione bit a bit
- `NOT` corrisponde a una negazione bit a bit

Nella prossima cella vedremo un primo esempio concreto.

```python
# Esempio di query booleana con AND tra incidence vectors

brutus_vector = incidence_matrix["brutus"]
caesar_vector = incidence_matrix["caesar"]

and_result = [b & c for b, c in zip(brutus_vector, caesar_vector)]

print("brutus  ->", brutus_vector)
print("caesar  ->", caesar_vector)
print("AND     ->", and_result)

matching_docs = [doc_id for doc_id, value in zip(documents.keys(), and_result) if value == 1]

print("\nDocuments matching 'brutus AND caesar':", matching_docs)
```
## Osservazione didattica

Questo esempio rende molto chiara l'idea del **Boolean Retrieval Model**:
ogni documento o soddisfa la query oppure no.

Non c'è ancora nessun concetto di ranking:
- i documenti non vengono ordinati per importanza
- non esiste una nozione di "più rilevante" o "meno rilevante"
- il match è semplicemente **esatto**

Questo approccio è semplice e molto utile per capire le basi dell'Information Retrieval, ma ha anche limiti evidenti:
- può essere troppo rigido
- non gestisce bene query vaghe o incomplete
- non ordina i risultati per utilità

```python
# Piccolo esempio con AND, OR e NOT

brutus_vector = incidence_matrix["brutus"]
caesar_vector = incidence_matrix["caesar"]
cleopatra_vector = incidence_matrix["cleopatra"]

not_cleopatra_vector = [1 - x for x in cleopatra_vector]

query_result = [b & c & nc for b, c, nc in zip(brutus_vector, caesar_vector, not_cleopatra_vector)]

print("brutus          ->", brutus_vector)
print("caesar          ->", caesar_vector)
print("NOT cleopatra   ->", not_cleopatra_vector)
print("final result    ->", query_result)

matching_docs = [doc_id for doc_id, value in zip(documents.keys(), query_result) if value == 1]

print("\nDocuments matching 'brutus AND caesar AND NOT cleopatra':", matching_docs)
```
## Mini esercizio

Prova a scrivere una nuova query booleana usando i termini presenti nel vocabolario.

Ad esempio:
- `caesar OR cleopatra`
- `brutus AND NOT cassius`
- `egypt OR republic`

### Domanda
Quali documenti vengono restituiti?  
Il risultato coincide con la tua intuizione leggendo i testi originali?
## Perché la term-document matrix non scala?

La term-document incidence matrix è molto utile per capire i concetti di base, ma presenta un grosso limite pratico.

In una collezione reale:
- il numero di documenti può essere molto grande
- il numero di termini distinti può essere enorme
- la maggior parte dei termini compare solo in una piccola parte dei documenti

Di conseguenza, la matrice contiene soprattutto **zeri**.  
Si dice quindi che la matrice è **sparsa** (*sparse matrix*).

### Problema
Memorizzare esplicitamente tutti gli 0 e gli 1 è inefficiente.

### Idea chiave
Invece di memorizzare tutta la matrice, conviene registrare solo le posizioni in cui compare il valore **1**.

Questa idea porta alla struttura dati fondamentale dell'Information Retrieval moderno:

# Inverted index

Per ogni termine, memorizziamo la lista dei documenti in cui compare.

Ad esempio:

- `brutus -> [1, 2, 4]`
- `cleopatra -> [5]`

Queste liste si chiamano **postings lists**.

```python
# Costruiamo una sequenza di coppie (term, docID)

term_doc_pairs = []

for doc_id, tokens in tokenized_documents.items():
    for token in tokens:
        term_doc_pairs.append((token, doc_id))

print("Term-doc pairs:\n")
print(term_doc_pairs)
# Ordiniamo prima per termine, poi per docID

term_doc_pairs = sorted(set(term_doc_pairs))

print("Sorted unique term-doc pairs:\n")
print(term_doc_pairs)
# Raggruppiamo le coppie per costruire l'inverted index

inverted_index = {}

for term, doc_id in term_doc_pairs:
    if term not in inverted_index:
        inverted_index[term] = []
    inverted_index[term].append(doc_id)

print("Inverted index:\n")

for term, postings in inverted_index.items():
    print(f"{term:15s} -> {postings}")
```
## Come leggere un inverted index

L'inverted index associa a ogni termine una posting list, cioè la lista dei documenti che contengono quel termine.

Per esempio, se leggiamo:

`caesar -> [1, 2, 4, 5]`

significa che il termine `caesar` compare nei documenti 1, 2, 4 e 5.

### Vantaggio
Questa struttura è molto più compatta della matrice completa, perché memorizza solo le informazioni utili.

### Osservazione importante
Nei sistemi reali, le postings lists sono mantenute **ordinate per docID**.  
Questa scelta è cruciale perché permette di eseguire in modo efficiente operazioni come l'intersezione tra liste.

```python
# Confronto concettuale: incidence vector vs postings list

term = "caesar"

print(f"Incidence vector for '{term}': {incidence_matrix[term]}")
print(f"Postings list for '{term}':   {inverted_index[term]}")
```
## Dalla matrice all'inverted index

Possiamo vedere l'inverted index come una rappresentazione compatta della term-document incidence matrix.

### Esempio
Supponiamo che il vettore di incidenza di `brutus` sia:

`[1, 1, 0, 1, 0]`

Questo equivale a dire che `brutus` compare nei documenti:

`[1, 2, 4]`

cioè esattamente la sua posting list.

In pratica:
- la **matrice** è utile per capire il modello
- l'**inverted index** è utile per implementare il sistema

```python
# Aggiungiamo anche la document frequency (df):
# il numero di documenti in cui compare un termine

document_frequency = {}

for term, postings in inverted_index.items():
    document_frequency[term] = len(postings)

print("Document frequency:\n")

for term, df in document_frequency.items():
    print(f"{term:15s} -> df = {df}")
```
## Document frequency

La **document frequency** di un termine è il numero di documenti in cui il termine compare.

Ad esempio:
- se `cleopatra` compare in un solo documento, allora `df(cleopatra) = 1`
- se `caesar` compare in quattro documenti, allora `df(caesar) = 4`

### Perché è utile?
La document frequency è importante perché:
- descrive quanto un termine è diffuso nella collezione
- aiuta nell'ottimizzazione delle query booleane
- sarà fondamentale anche in modelli di ranking più avanzati

```python
# Stampiamo i termini ordinati per document frequency crescente

sorted_by_df = sorted(document_frequency.items(), key=lambda x: x[1])

print("Terms ordered by increasing document frequency:\n")

for term, df in sorted_by_df:
    print(f"{term:15s} -> df = {df}")
```
## Osservazione didattica

I termini con document frequency più bassa sono spesso più selettivi.

Per esempio, un termine che compare in un solo documento restringe molto il numero di candidati.

Questo suggerisce una strategia importante nel query processing booleano:
quando dobbiamo fare molte intersezioni, conviene iniziare dalle postings lists più piccole.

```python
# Visualizziamo alcune postings lists di interesse

terms_to_inspect = ["brutus", "caesar", "cleopatra", "republic"]

for term in terms_to_inspect:
    print(f"{term:15s} -> postings = {inverted_index[term]}, df = {document_frequency[term]}")
```
## Mini esercizio

Osserva l'inverted index e prova a rispondere senza eseguire nuovo codice:

1. In quali documenti compare `brutus`?
2. Quale termine tra `cleopatra` e `caesar` è più selettivo?
3. Quale posting list ti aspetti più utile da elaborare per prima in una query con AND?

Nella prossima sezione useremo direttamente le postings lists per eseguire query come:

`brutus AND caesar`

tramite una procedura di **merge** tra liste ordinate.
## Query processing con l'inverted index

Ora che abbiamo costruito l'inverted index, possiamo usarlo per rispondere a query booleane in modo più efficiente.

Consideriamo la query:

`brutus AND caesar`

Con la term-document matrix potevamo fare un AND bit a bit tra vettori binari.  
Con l'inverted index, invece, lavoriamo direttamente sulle **postings lists**:

- `brutus -> [1, 2, 4]`
- `caesar -> [1, 2, 4, 5]`

La risposta alla query è l'**intersezione** tra queste due liste.

## Idea del merge

Poiché le postings lists sono ordinate per `docID`, possiamo scorrerle simultaneamente con due puntatori:

- se i due docID coincidono, abbiamo trovato un match
- se un docID è più piccolo dell'altro, avanziamo nella lista con il docID più piccolo
- continuiamo finché una delle due liste termina

Questa procedura si chiama spesso **merge** o **intersection of postings lists**.

## Vantaggio
Se una lista ha lunghezza `x` e l'altra ha lunghezza `y`, il merge richiede tempo proporzionale a:

`O(x + y)`

Questo è uno dei motivi per cui l'inverted index è così efficace.

```python
def intersect(postings1, postings2):
    """
    Restituisce l'intersezione tra due postings lists ordinate.
    """
    answer = []
    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):
        if postings1[i] == postings2[j]:
            answer.append(postings1[i])
            i += 1
            j += 1
        elif postings1[i] < postings2[j]:
            i += 1
        else:
            j += 1

    return answer
```
## Prima implementazione dell'intersezione

La funzione `intersect` implementa esattamente l'algoritmo di merge tra due postings lists ordinate.

### Osservazione
Questo algoritmo funziona bene perché:
- le liste sono già ordinate
- non dobbiamo confrontare ogni elemento con tutti gli altri
- possiamo avanzare in modo intelligente

Vediamolo ora in azione su una query semplice.

```python
postings_brutus = inverted_index["brutus"]
postings_caesar = inverted_index["caesar"]

result = intersect(postings_brutus, postings_caesar)

print("brutus ->", postings_brutus)
print("caesar ->", postings_caesar)
print("\nResult of 'brutus AND caesar' ->", result)
```
## Interpretazione del risultato

Se il risultato è:

`[1, 2, 4]`

significa che i documenti 1, 2 e 4 contengono sia `brutus` sia `caesar`.

Possiamo anche recuperare direttamente il testo dei documenti corrispondenti.

```python
matching_docs = intersect(inverted_index["brutus"], inverted_index["caesar"])

print("Documents matching 'brutus AND caesar':\n")

for doc_id in matching_docs:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## Traccia passo passo del merge

Per capire bene l'algoritmo, può essere utile osservare come si muovono i due puntatori durante l'intersezione.

Nella prossima cella useremo una versione "verbose" della funzione, che stampa ogni confronto effettuato.

```python
def intersect_verbose(postings1, postings2):
    answer = []
    i = 0
    j = 0

    print(f"Initial lists: {postings1} AND {postings2}\n")

    while i < len(postings1) and j < len(postings2):
        print(f"Compare {postings1[i]} and {postings2[j]}")

        if postings1[i] == postings2[j]:
            print(f"  Match found: {postings1[i]}")
            answer.append(postings1[i])
            i += 1
            j += 1
        elif postings1[i] < postings2[j]:
            print(f"  {postings1[i]} is smaller -> advance first pointer")
            i += 1
        else:
            print(f"  {postings2[j]} is smaller -> advance second pointer")
            j += 1

    print("\nFinal result:", answer)
    return answer

intersect_verbose(inverted_index["brutus"], inverted_index["caesar"])
```
## Perché l'ordine delle postings è cruciale?

Se le postings lists non fossero ordinate, il merge lineare non funzionerebbe.

Dovremmo allora usare strategie molto meno efficienti, ad esempio:
- controllare per ogni elemento della prima lista se compare nella seconda
- oppure ordinare le liste prima di eseguire l'intersezione

Per questo, nei sistemi di Information Retrieval, le postings lists vengono mantenute ordinate per `docID`.

```python
# Esempio con una query AND diversa

query_result = intersect(inverted_index["caesar"], inverted_index["cleopatra"])

print("caesar AND cleopatra ->", query_result)

for doc_id in query_result:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## AND tra più di due termini

Se una query contiene più termini in AND, ad esempio:

`brutus AND caesar AND cassius`

possiamo procedere iterativamente:
1. intersechiamo le prime due postings lists
2. intersechiamo il risultato con la terza
3. continuiamo fino a esaurire i termini

Tuttavia, l'ordine in cui facciamo queste intersezioni è importante.

```python
# Esempio di AND tra più termini

query_terms = ["brutus", "caesar", "cassius"]

current_result = inverted_index[query_terms[0]]

for term in query_terms[1:]:
    current_result = intersect(current_result, inverted_index[term])

print(f"Result of {' AND '.join(query_terms)} -> {current_result}")

for doc_id in current_result:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## Query optimization: in quale ordine conviene fare le intersezioni?

Consideriamo una query come:

`term1 AND term2 AND term3`

Non tutti i termini sono ugualmente frequenti nella collezione.

### Idea chiave
Conviene iniziare dalle postings lists più piccole, cioè dai termini con **document frequency** più bassa.

### Perché?
Perché l'intersezione di due liste piccole tende a produrre un risultato piccolo, che sarà più veloce da intersecare con le liste successive.

In altre parole:
- iniziare dai termini più selettivi riduce il numero di candidati il prima possibile
- questo migliora l'efficienza del query processing

```python
def and_query(query_terms, inverted_index, document_frequency):
    """
    Esegue una query AND ordinando prima i termini
    per document frequency crescente.
    """
    sorted_terms = sorted(query_terms, key=lambda term: document_frequency[term])

    print("Processing order:", sorted_terms)

    current_result = inverted_index[sorted_terms[0]]

    for term in sorted_terms[1:]:
        current_result = intersect(current_result, inverted_index[term])

    return current_result
query_terms = ["caesar", "brutus", "cassius"]

result = and_query(query_terms, inverted_index, document_frequency)

print(f"\nFinal result for {' AND '.join(query_terms)} -> {result}")

for doc_id in result:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## Cosa è successo?

La funzione ha riordinato automaticamente i termini in base alla loro document frequency.

Questo è un esempio molto semplice di **query optimization**.

Nei sistemi reali, l'ottimizzazione può essere più sofisticata, ma l'idea di base resta la stessa:
ridurre il costo delle operazioni iniziando dai termini o dai sotto-problemi più selettivi.

```python
# Mostriamo chiaramente df e ordine di esecuzione

query_terms = ["caesar", "brutus", "cassius"]

print("Document frequencies:")
for term in query_terms:
    print(f"{term:10s} -> {document_frequency[term]}")

ordered_terms = sorted(query_terms, key=lambda term: document_frequency[term])

print("\nRecommended processing order:")
print(ordered_terms)
```
## Mini esercizio

Prova a cambiare la query nella cella precedente e osserva:
- quali termini vengono processati per primi
- come cambia il risultato finale
- se il termine più raro viene effettivamente messo all'inizio

Puoi provare, ad esempio, con:
- `["caesar", "cleopatra"]`
- `["brutus", "caesar", "egypt"]`
- `["republic", "rome"]`

## Nota importante
Finora abbiamo gestito solo query booleane semplici basate sulla presenza o assenza di termini nei documenti.

Ma cosa succede se vogliamo cercare una **frase esatta**, per esempio:

`"killed caesar"`

L'inverted index costruito fin qui non basta più, perché ci dice solo **in quali documenti** compare un termine, non **in quale posizione** compare.

Per risolvere questo problema serve una nuova struttura: il **positional index**.
## Phrase query: perché l'inverted index semplice non basta?

Fino a questo punto abbiamo rappresentato ogni termine tramite la lista dei documenti in cui compare.

Per esempio:

- `killed -> [1, 2]`
- `caesar -> [1, 2, 4, 5]`

Se eseguiamo la query booleana:

`killed AND caesar`

otteniamo i documenti che contengono entrambi i termini.

### Ma attenzione
Questo non garantisce che i due termini compaiano come **frase esatta**.

Per esempio, un documento potrebbe contenere entrambe le parole ma in posizioni lontane, o in ordine inverso.

Per gestire query come:

- `"killed caesar"`
- `"brutus killed"`
- `"caesar in egypt"`

non basta sapere **se** un termine compare in un documento: dobbiamo sapere anche **dove** compare.

Per questo introduciamo il **positional index**.

```python
# Mostriamo il limite dell'inverted index semplice con una phrase query

print("Postings for 'killed':", inverted_index.get("killed", []))
print("Postings for 'caesar':", inverted_index.get("caesar", []))

candidate_docs = intersect(inverted_index.get("killed", []), inverted_index.get("caesar", []))
print("\nCandidate documents for 'killed AND caesar':", candidate_docs)

for doc_id in candidate_docs:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## Positional index

Nel **positional index**, per ogni termine non memorizziamo solo i documenti in cui compare, ma anche le **posizioni** in cui compare all'interno di ciascun documento.

### Forma generale
Per ogni termine memorizziamo una struttura del tipo:

`term -> {docID: [posizioni]}`

Ad esempio:

`caesar -> {1: [2], 2: [1], 4: [5], 5: [2]}`

Questo significa che:
- in `Doc 1`, `caesar` compare in posizione 2
- in `Doc 2`, compare in posizione 1
- e così via

### Vantaggio
Con questa informazione possiamo verificare se due termini compaiono:
- in posizioni consecutive, per una **phrase query**
- entro una certa distanza, per una **proximity query**
# Costruzione del positional index

```python
# Per ogni termine salviamo, per ogni documento, tutte le posizioni in cui compare

positional_index = {}

for doc_id, tokens in tokenized_documents.items():
    for position, token in enumerate(tokens):
        if token not in positional_index:
            positional_index[token] = {}
        if doc_id not in positional_index[token]:
            positional_index[token][doc_id] = []
        positional_index[token][doc_id].append(position)

print("Example positional postings:\n")

for term in ["brutus", "killed", "caesar", "cleopatra"]:
    if term in positional_index:
        print(f"{term:12s} -> {positional_index[term]}")
```
## Come leggere il positional index

Supponiamo di avere:

`killed -> {1: [1], 2: [2]}`

Questo significa che:
- nel documento 1 il termine `killed` compare in posizione 1
- nel documento 2 compare in posizione 2

Se in uno stesso documento troviamo:

- `killed` in posizione 1
- `caesar` in posizione 2

allora possiamo concludere che nel documento compare la frase:

`"killed caesar"`

perché i due termini sono consecutivi e nell'ordine corretto.

```python
# Ispezioniamo i token con posizione per ogni documento

for doc_id, tokens in tokenized_documents.items():
    indexed_tokens = list(enumerate(tokens))
    print(f"Doc {doc_id}: {indexed_tokens}")
```
## Verifica di una phrase query a due termini

Per rispondere a una query come:

`"killed caesar"`

possiamo procedere così:

1. troviamo i documenti che contengono entrambi i termini
2. per ciascun documento comune, confrontiamo le posizioni
3. controlliamo se esiste una posizione `p` del primo termine tale che il secondo compaia in `p + 1`

Se sì, il documento contiene la frase esatta.

```python
def phrase_query_two_terms(term1, term2, positional_index):
    """
    Restituisce i docID che contengono la frase esatta 'term1 term2'.
    """
    result = []

    postings1 = positional_index.get(term1, {})
    postings2 = positional_index.get(term2, {})

    common_docs = sorted(set(postings1.keys()) & set(postings2.keys()))

    for doc_id in common_docs:
        positions1 = postings1[doc_id]
        positions2 = postings2[doc_id]

        positions2_set = set(positions2)

        for pos in positions1:
            if pos + 1 in positions2_set:
                result.append(doc_id)
                break

    return result
phrase = ("killed", "caesar")
result = phrase_query_two_terms(phrase[0], phrase[1], positional_index)

print(f'Documents matching the phrase "{phrase[0]} {phrase[1]}":', result)

for doc_id in result:
    print(f"Doc {doc_id}: {documents[doc_id]}")
```
## Osservazione importante

La phrase query è più restrittiva della semplice query booleana.

Infatti:

- `killed AND caesar` restituisce i documenti che contengono entrambi i termini
- `"killed caesar"` restituisce solo i documenti in cui i due termini compaiono in sequenza

Questo mostra bene perché i positional indexes sono più potenti dei semplici inverted indexes non posizionali.

```python
# Proviamo alcune phrase query

test_phrases = [
    ("brutus", "killed"),
    ("killed", "caesar"),
    ("caesar", "was"),
    ("in", "egypt")
]

for term1, term2 in test_phrases:
    result = phrase_query_two_terms(term1, term2, positional_index)
    print(f'"{term1} {term2}" -> {result}')
```
## Estensione concettuale: proximity query

Una phrase query richiede che due termini siano consecutivi.

Una **proximity query**, invece, richiede che due termini compaiano entro una certa distanza.

Per esempio:

`brutus` entro 3 parole da `caesar`

In questo caso, invece di controllare se il secondo termine compare in `p + 1`, controlliamo se compare in una posizione abbastanza vicina a `p`.

Non implementeremo qui una proximity query completa, ma il positional index è esattamente la struttura necessaria per farlo.

```python
def proximity_query_two_terms(term1, term2, k, positional_index):
    """
    Restituisce i docID in cui term1 e term2 compaiono entro distanza k.
    Implementazione semplice e leggibile, non ancora ottimizzata.
    """
    result = []

    postings1 = positional_index.get(term1, {})
    postings2 = positional_index.get(term2, {})

    common_docs = sorted(set(postings1.keys()) & set(postings2.keys()))

    for doc_id in common_docs:
        positions1 = postings1[doc_id]
        positions2 = postings2[doc_id]

        found = False
        for p1 in positions1:
            for p2 in positions2:
                if abs(p1 - p2) <= k:
                    found = True
                    break
            if found:
                result.append(doc_id)
                break

    return result
print("Proximity query examples:\n")

examples = [
    ("brutus", "caesar", 1),
    ("brutus", "caesar", 2),
    ("caesar", "egypt", 2)
]

for term1, term2, k in examples:
    result = proximity_query_two_terms(term1, term2, k, positional_index)
    print(f'{term1} within {k} words of {term2} -> {result}')
```
## Riassunto del laboratorio

In questo laboratorio abbiamo costruito passo dopo passo una versione semplificata di un sistema di Information Retrieval.

### Abbiamo introdotto
- il concetto di **collection**
- la distinzione tra **information need** e **query**
- il ruolo della **relevance**

### Abbiamo costruito
- una **tokenized collection**
- un **vocabolario**
- una **term-document incidence matrix**
- un **inverted index**
- un **positional index**

### Abbiamo implementato
- query booleane tramite vettori di incidenza
- intersezione di postings lists con algoritmo di **merge**
- una semplice strategia di **query optimization**
- phrase query con il **positional index**

## Messaggio chiave
La term-document matrix è utile per capire i concetti, ma l'**inverted index** è la struttura realmente usata per rendere efficiente la ricerca.

Quando vogliamo gestire frasi o vicinanza tra termini, dobbiamo arricchire l'indice con l'informazione sulle **posizioni**.
## Esercizi finali

### Esercizio 1
Aggiungi nuovi documenti alla collezione e osserva come cambiano:
- il vocabolario
- la document frequency
- le postings lists

### Esercizio 2
Implementa una funzione per eseguire query del tipo:

`term1 AND term2 AND term3`

accettando direttamente una stringa di input.

### Esercizio 3
Estendi la funzione per le phrase query a una frase di lunghezza maggiore di 2 termini, ad esempio:

`"brutus killed caesar"`

### Esercizio 4
Rendi più efficiente la proximity query evitando il doppio ciclo completo su tutte le posizioni.

### Esercizio 5
Confronta, su alcuni esempi, il risultato di:
- query booleana
- phrase query
- proximity query

e commenta le differenze.
## Conclusione

Questo notebook ha mostrato i meccanismi fondamentali dell'Information Retrieval su una piccola collezione controllata.

Nel prossimo laboratorio passeremo da un esempio "toy" a una collezione reale, affrontando problemi più vicini ai sistemi veri:
- preprocessing più ricco
- indexing di molti documenti
- gestione di query più complesse
- valutazione dei limiti dell'implementazione