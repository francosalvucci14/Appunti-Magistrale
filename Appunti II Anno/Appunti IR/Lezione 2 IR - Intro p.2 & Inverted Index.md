# Classic Search Model

Riprendiamo le assunzioni basi fatte nella prima lezione
- **Collezione** : prima di tutto assumiamo che per "collezione" si intenda un ***insieme di documenti*** (per ora assumiamo anche che sia una collezione statica)
- **Goal**: Il goal dell'IR è recuperare documenti con informazioni che sono *rilevanti* al bisogno informativo dell'utente, e che aiuti lo stesso a completare un *task*

Man mano che andremo avanti andremo a rilassare queste assunzioni.

Sulla base di queste, vediamo il **classico search model** usato

![600](img/Pasted%20image%2020260307110857.png)

Come possiamo vedere, il modello funziona nel seguente modo:
- **User Task** : Prende l'input dell'utente - deve capire cosa vuole fare l'utente
- **Info Need** : Il bisogno informativo dell'utente - deve capire che tipo di informazioni servono
- **Query** : La query di ricerca da madare al Search Engine
- **Search Engine** : Colui che si occupa di effettuare la ricerca, prendendo in input la collezione di documenti, e dando in output il risultato
- **Query Refinement**: Se i risultati non vanno ancora bene, si può rifinire la query e rimandarla al Search Engine

Una nota fondamentale è che il Search Engine deve essere più **generale** possibile

Come possiamo vedere dallo schema però, ci possono essere formulazioni errate in vari livelli di questo modello

Ci servono però delle metriche per capire quanto buono sia il modello di IR

Le due metriche che useremo riprendono molto dal Machine Learning, e sono:
- **Precision** : Frazione di documenti recuperati che sono rilevanti al **bisogno informativo** dell'utente
- **Recall** : Frazione di documenti rilevanti nella collezione che sono stati recuperati

Vediamo ora un esempio (credo il primo modello di IR)
## Matrice Termini-Documenti

Ipotizziamo di volere un modello di IR che risponda a questa query:
- Quali opere di Shakespeare contiene le parole **Brutus** AND **Caesar** ma NON **Calpurnia**

Una prima soluzione potrebbe essere quella di *raggruppare* tutte le opere di Shakespeare per Brutus e Caesar, e poi eliminare le line contenenti Calpurnia

Sembra corretto vero? perccato che non lo è, per molti punti:
- È un'operazione troppo lenta (per grandi collezzioni) - non scala in termini di tempo e complessità
- NOT Calpurnia è non-trivial
- Altre operazioni non sono ammissibili
- C'è anche un problema con il Ranked Retrieval (migliori documenti da ritornare) - prossime lezioni

Una soluzione migliore è quella di usare la **Matrice Termini-Documenti**.

>[!definition]- Matrice Termini-Documenti
>È una matrice composta dalle righe che sono i **Termini**, e le colonne sono i **Documenti**
>Inoltre, la matrice è una matrice binaria, costruita in questo modo
>$$M[\text{parola},\text{opera}]=\begin{cases}1&\text{opera contiene parola}\\0&\text{altrimenti}\end{cases}$$

Un esempio è il seguente:

![600](img/Pasted%20image%2020260307112537.png)

Ora, per rispondere alla query precedente, la soluzione è:
- prendi le righe (i vettori) per le 3 parole Brutus, Caesar e Calpurnia (*invertita*)
- poi si fa l'AND bit-a-bit fra le righe

Con questo esempio quindi otteniamo una cosa del tipo:
$$
\begin{align*}
\text{Brutus}:110100&\\
\text{Caesar}:110111&\\
\text{(inv.) Calpurnia}:101111&\\
\text{Risultato}: 100100 &
\end{align*}
$$

Bella questa soluzione, ma c'è un grosso problema

Ipotizziamo che ci siano $N=1$ milione di documenti, ognuno di circa $1000$ parole
Se consideriamo una media di circa $6$ bytes/parola, includendo spazi e punteggiatura ottieniamo circa $6$GB di dati nei documenti
Ipotizziamo anche che ci siano $M=500$K termini **distinti** fra questi

Dove si trova il problema della matrice? La ***dimensione***

In questo caso, dovremmo creare una matrice di dimensione $500$k$\times1$M, contenente circa a mezzo trilione di zeri e uni, ma non più di un bilione di uni -> la matrice è ***estremamente sparsa***

---

Qui dobbiamo fare una piccola digressione sul concetto di sparso e denso

Quando trattiamo questi concetti troviamo due problemi fondamentali:
1) la natura intriseca del problema
2) la rappresentazione

Un'oggetto potrebbe essere sparso per natura, ma la rappresentazione che noi usiamo è densa, o viceversa ovviamente

Per questo, bisogna prestare parecchia attenzione quando si parla di sparso/denso

---

Una migliore **rappresentazione** del problema in questione? Ci salviamo solamente le posizioni delgi uni

## Inverted Index

>[!definition]- Struttura dati Inverted Index
> Per ogni termine $t$, salviamo una lista di documenti che contengono $t$
> Ogni documento viene identificato tramite un **docID** - numero seriale del documento

Domanda fondamentale, possiamo usare array di dimensione fissata per fare questo?

Prendiamo il seguente esempio:

![500](img/Pasted%20image%2020260307114553.png)

Con la dimensione fissata, cosa succede se la parola Caesar viene aggiunta nel documento 14?
Ogni volta che avviene un nuovo inserimento dentro ad un qualunque documento, dovremmo ri-scansionare la lista relativa a quel termine, e inserire il valore (es. 14) nella posizione corretta (nel peggiore dei caso la complessità risulterà essere **lineare** nel numero di documenti)

Quello che dobbiamo usare è un'array di **postings** a dimensione variabile
- Su disco, una serie di postings continua è normale e ottimale
- Nella memoria, è possibile usare linked list o array di dimensione variabile

La situazione diventa quindi la seguente:

![600](Pasted%20image%2020260307115737.png)

Come vediamo quindi la struttura è un **dizionario** le cui chiavi sono i termini, e i valori di ogni chiave è una lista a dimensione variabile contenente il docID 

Inoltre, le liste di postings sono ordinate secondo i docID (vedremo poi perchè)

La costruzione dell'Inverted Index avviene nel modo seguente:

![500](img/Pasted%20image%2020260307120718.png)

Abbiamo quindi che i documenti che vanno indicizzati verranno passati al **Tokenizer**
Dopo aver ottenuto il token stream si passa ai **Moduli Linguistici**, ottenendo dei toker modificati.
Infine, i token modificati vengono presi e passati all'**Indicizzatore**

Le fasi sono quindi scomposti nel modo seguente:

***Tokenizzazione***
- Tagliare la sequenza di caratteri in token di parole
	- Gestire “John's”, una soluzione all'avanguardia (?)

***Normalizzazione***
- Mappare il testo e il termine di ricerca nella stessa forma
	- Si desidera che U.S.A. e USA corrispondano

***Stemming***
- Si potrebbero desiderare diverse forme di una radice da abbinare
	- es. autorizzare, autorizzazione

**Stop Words**
- È possibile omettere le parole molto comuni (o meno)
	- es. the, a, to, of

