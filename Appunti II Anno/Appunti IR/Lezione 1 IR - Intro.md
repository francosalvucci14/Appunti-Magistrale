# Introduzione al corso

Partiamo dagli obiettivi di questo corso

Il corso si propone di introdurre gli scopi, le principali problematiche e i principali modelli di Information Retrieval

Gli argomenti trattati saranno:
- Introduzione al problema dell'Information Retrieval
- Definizione della nozione di Inverted Indices
- Costruzione di Indici per l'Information Retrieval
- Algoritmi per la codifica e compressione dell'Informazione
- Funzione di Ranking documentale
- Introduzione al Vector Space Model
- Modelli Probabilistici per l'Information Retrieval
- Valutazione dei Sistemi di IR
- Sviluppo efficiente e su larga scala di sistemi di IR
- Crawling e Detection di risorse duplicate
- Introduzione a IR Engines
- Introduzione a Map Reduce

Il corso si dividerà in lezione teoriche e Laboratori, dove vedremo l'implementazione di alcuni dei paradigmi di IR che si vedranno a lezione

Ci saranno anche degli esercizi da svolgere

L'esame si compone di una prova scritta, contenente un Test a risposte multiple e una Domanda aperta (potranno essere divisi in due test in itinere oppure un'unica prova finale) e di una prova orale

C'è anche la possibilità di effettuare un progetto, che completerà il voto finale

---
# Introduzione al problema dell'Information Retrieval

Prima di tutto definiamo correttamente e formalmente cosa si intende per **Information Retrieval**

>[!definition]- Information Retrieval
>L'Information Retrieval (IR) si occupa di **trovare materiale** (di solito documenti) di natura **non strutturata** (di solito testi), che soddisfi un **bisogno informativo** all'interno di **grandi collezioni di dati** (di solito collezioni di dati salvati sui computer)

La prima cosa a cui uno potrebbe pensare allora è il **web search**, ma ci sono moltri altri casi, tra cui:
- E-mail search
- Searching laptop
- Corporate knwoledge bases
- Legal information retrieval

La situazione dati non strutturati (testo) vs. dati strutturati (database) è evoluta molto nel corso degli anni

La situazione nella seconda metà degli anni 90 era circa la seguente:

![center|500](img/Pasted%20image%2020260304122532.png)

Come possiamo vedere, il volume dei dati era molto sbilanciato verso i dati non strutturati, il che significa che c'erano molti più dati **non strutturati** che **strutturati**; mentre il **market cap** [^1] tendeva ad essere molto più elevato per i dati **strutturati** che per quelli **non strutturati**

Ad oggi invece la situazione è parecchio cambiata

![center|500](img/Pasted%20image%2020260304122922.png)

Come possiamo vedere,sia il volume dei dati non strutturati che il loro market cap sono **parecchio aumentati** rispetto agli anni 90

Come possiamo intendere, ad oggi servono quindi più sistemi di IR per poter recuperare informazioni da questi dati non strutturati

Vediamo però quali sono le assunzioni base dell'IR

- **Collezione** : prima di tutto assumiamo che per "collezione" si intenda un ***insieme di documenti*** (per ora assumiamo anche che sia una collezione statica)
- **Goal**: Il goal dell'IR è recuperare documenti con informazioni che sono *rilevanti* al bisogno informativo dell'utente, e che aiuti lo stesso a completare un *task*

## Information Retrieval VS Databases

Tradizionalmente, l'IR è un campo di ricerca separato da quello dei Database

Anche i prodotti sono tradizionalmente separati

Sembrano quindi due "bestie" differenti, cosa che possiamo affermare guardando la seguente tabella


| IR                                                        | DBMS                                       |
| --------------------------------------------------------- | ------------------------------------------ |
| Semantica Imprecisa                                       | Semantica Precisa                          |
| Ricerca per keyword                                       | SQL                                        |
| Formati non strutturati per i dati                        | Formati strutturati                        |
| Per lo più lettura. Aggiunta di documenti occasionalmente | Si aspetta un numero ragionevole di update |
| i **primi** $k$ risultati                                 | Genera tutte le risposte                   |

Entrambi i modelli però supportano query su dataset enormi, sfruttando la tecnica di *indexing*

Queste differenze portano a dover scegliere, nella pratica, uno dei due modelli

## Modello di IR "Bag of Words"

Analizziamo questo modello di IR (che è anche un **tipico** data modell IR)

- Ogni documento è un semplice insieme (multiset) di parole ("termini")
- Il **modello Bag** rappresenta un documento proprio come il modello BBox rappresenta un oggetto spaziale

Alcuni dettagli particolari di questo modello

- **Dettaglio 1** : le "Stop Words"
	- Certe parole sono considerate irrilevanti e non vengono posizionate nel Bag
- **Dettaglio 2** : "Stemming" (Derivazione) e altre analisi dei contenuti
	- Si usano regole specifiche della lingua per convertire le parole nella loro forma base, es: "surfed" -> "surf"

## Boolean Search in SQL

Nei modelli di IR Boolean Search, si usa una sola query SQL, che contiene:
- **Selects** single-table
- **UNION**
- **INTERSECT**
- **EXCEPT**

La **relevance** è la "salsa segreta" dei search engines (è il "cuore" dei search engines)
- È una combo di statistica, linguestica e teoria dei grafi (es. calcolare la reputazione delle pagine, hubs e authority sui topics, etc...)
- Sfortunatamente, non è facile calcolare questa quantità in maniera **efficiente** usando le tipiche implementazioni DBMS
### Calcolo della relevance

Il calcolo della **relevance** involve quante volte i termini di ricerca appaiono nel documento, e quante volte appaiono nella collezione
- Più termini di ricerca compaiono nel documento, più esso è rilevante ai fini della ricerca 
- Viene attribuita maggiore importanza alla ricerca di termini *rari*

Fare questo negli engine SQL non è facile
- La "rilevanza di un documento rispetto a un termine di ricerca" è una funzione che viene richiamata una volta per ogni documenti in cui compare il termine usato
- Per un calcolo efficiente bisogna memorizzare, per ogni termine, il numero di volte in cui il termine compare in ogni documento, nonchè il numero di documenti in cui compare
- È inoltre necessario ordinare i documenti recuperati in base al loro valore di rilevanza
- Inoltre occorre considerare anche gli operatori booleani (se la ricerca contiene più termini) e capire il modo in cui influenzano il calcolo della rilevanza

## Architetture: DBMS vs Search Engine

Vediamo allora le differenze fra le due architetture 

![661](img/Pasted%20image%2020260307105603.png)

***Garanzie semantiche***
- Il DBMS garantisce la semantica transazionale.
	- Se si inseriscono commit Xact, una query successiva *vedrà* l'aggiornamento.
	- Gestisce correttamente più aggiornamenti simultanei.
- I sistemi IR non lo fanno, ma nessuno se ne accorge!
	- Rimanda gli inserimenti fino al momento opportuno
	- Nessun modello di concorrenza corretta

***Modellazione dei dati e complessità delle query***
- Il DBMS supporta qualsiasi schema e query
	- Richiede la definizione dello schema
	- Linguaggio di query complesso e difficile da imparare
- L'IR supporta solo uno schema e una query
	- Non è richiesta la progettazione dello schema (testo non strutturato)
	- Linguaggio di query facile da imparare

**Obiettivi prestazionali**
- Il DBMS supporta SELECT generici e query arbitrariamente complesse.
	- Inoltre, supporta una combinazione di INSERT, UPDATE e DELETE.
	- Il motore generico deve sempre funzionare “bene”.
- I sistemi IR prevedono solo un SELECT stilizzato.
	- Inoltre, INSERT ritardati, DELETE insoliti, nessun UPDATE.
	- Scopo speciale, deve funzionare in modo estremamente veloce su “The Query”.
	- Gli utenti raramente guardano la risposta completa nella ricerca booleana.


[^1]: si riferisce alla valutazione finanziaria delle aziende all'interno del settore IR o alla dimensione del mercato IR stesso
