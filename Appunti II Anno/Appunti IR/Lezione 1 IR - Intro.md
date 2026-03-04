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


[^1]: si riferisce alla valutazione finanziaria delle aziende all'interno del settore IR o alla dimensione del mercato IR stesso
