# More on I.I

Stiamo ancora parlando dell' **Inverted Index**

Nella scorsa lezione avevamo introdotto questa struttura dati di IR, e avevo visto gli stage iniziali del text processing, che sono:
- Tokenizzazione
- Normalizzazione
- Stemming
- Stop words

Vediamo ora la parte dell'**Indexer** step by step
## Indexer Steps: Token sequence

In questa fase, il documento viene scomposto (**tokenizzato**), e si crea un dizionario di coppie (token,docID)

Ad esempio, possiamo avere una situazione del genere

![500](img/Pasted%20image%2020260312141447.png)

Come possiamo vedere, la parola *did* compare solo nel documento $1$, quindi nella tabella a sinistra vediamo che al termine **Term: did** è associato il docID $1$

La parola *Caesar* invece compare in entrambi i documenti, quindi nella tabella a sinistra il termine *Caesar* è associato sia a docID $1$ che a docID $2$ . Vediamo quindi che c'è una ripetizione nella tabella
## Indexer Steps: Sort

La tabella generata dalla fase $1$ viene poi **ordinata** per i Termini e , almeno concettualmente, per docID

>Questo è un step **cruciale** della fase di indexing

Vediamo che per l'esempio precedente otteniamo quindi la seguente situazione

![308](img/Pasted%20image%2020260312142231.png)
## Indexer Steps: Dictionary & Postings

A questo punto si passa alla fase finale dell'Indexer, ovvero la fase dove la tabella creata e modificata nelle prime 2 fasi viene trasformata in un dizionario che punta ai postings.

Nel dettaglio, avvengono le seguenti cose:
- Tutti i termini doppi che appartengono allo stesso documento vengono mergiati
	- es. "was->1", "was->2" vengono mergiati in "was->2"
	- es. "killed->1", "killed->1" vengono mergiati in un'unica entrata "killed->1"
- La lista viene divisa in due componenti interconnesse (la struttura sulla destra):
	- **Dictionary (Dizionario):** È l'elenco dei termini unici (il vocabolario). Ogni parola, da "ambitious" a "with", compare una sola volta.
    - **Postings Lists (Liste di Posting):** A ogni parola del dizionario è agganciata una "lista di posting", ovvero l'elenco dei documenti (`docID`) in cui quella parola è presente. Ad esempio, il termine "brutus" punta alla lista `1 -> 2`, indicando che si trova in entrambi i documenti
- Nel dizionario si aggiunge poi un'informazione fondamentale: ovvero la **frequenza nei documenti**

La situazione è quindi la seguente:

![500](img/Pasted%20image%2020260312142809.png)

Il **doc. frequency** non serve per trovare i documenti, ma sarà cruciale nella fase di **ranking** (es. calcolo del TF-IDF) per capire quanto una parola sia "rara" o "comune" nell'intera collezione di testi e, di conseguenza, quanto sia importante per una determinata query

La domanda che ci poniamo però è cruciale: "*quanto spazio richiede memorizzare l'I.I?*"

Quando si progetta un sistema di Information Retrieval (IR) reale, le dimensioni contano.

I tre "colli di bottiglia" principali dove il sistema consuma memoria (RAM) o spazio su disco sono:
1. Terms and counts (Termini e conteggi)
	- **Cosa memorizza:** È il dizionario (Dictionary). Contiene le stringhe di testo (le parole vere e proprie, come "ambitious", "brutus") e un numero intero per la frequenza nel documento (`doc. freq.`).
    - **Il costo:** Ogni carattere di ogni parola occupa spazio. In collezioni di testi molto grandi, il vocabolario può raggiungere milioni di termini unici.
2. Pointers (Puntatori)
	- **Cosa memorizza:** Il collegamento tra il dizionario e le liste. Il computer deve sapere fisicamente _dove_ andare a leggere gli ID dei documenti per una specifica parola.
	- **Il costo:** Le freccie al centro rappresentano dei puntatori in memoria (indirizzi fisici). Ogni termine nel dizionario deve avere un puntatore verso l'inizio della sua lista di posting. Anche questi puntatori occupano byte preziosi (solitamente 4 o 8 byte ciascuno).
 3. Lists of docIDs (Liste di Posting)
	- **Cosa memorizza:** L'elenco vero e proprio dei documenti in cui compare una parola.
	- **Il costo:** **Questa è solitamente la parte più pesante dell'intero indice.** Sebbene per parole rare (es. "ambitious") la lista sia corta, per parole molto comuni la lista di `docID` diventa chilometrica. Se un termine compare in un milione di documenti, la sua lista dovrà memorizzare un milione di numeri interi.

Si pongono quindi due domande fondamentali:
- Come indicizziamo in modo efficiente?
- Di quanto spazio abbiamo *davvero* bisogno?

![500](img/Pasted%20image%2020260312143812.png)

---
# Query Processing with I.I

La domanda che sorge spontanea, dopo aver visto come si crea un Inverted Index è:

> Come processiamo una query? e più avanti, che *tipo* di query possiamo processare?

## Query Processing: AND

Consideriamo la query: Brutus ***AND*** Caesar

Come rispondiamo sfruttando l'I.I?

Un'approccio possibile è:
1) Trovare il termine **Brutus** nel dizionario
	1) Recuperare la sua lista di posting
2) Trovare il termine **Caesar** nel dizionario
	1) Recuperare la sua lista di posting
3) "Mergiare" le due liste di postings (equivalente a fare l'intersezione degli insiemi di documenti)

Il risultato delle prime due operazioni è il seguente:

![600](img/Pasted%20image%2020260312144616.png)

Come facciamo l'operazione di Merge di queste due liste?

Scorriamo entrambe le liste **contemporaneamente**, in tempo lineare nel numero totale di entrate possiamo effettuare il merge
Di conseguenza, se le due liste hanno lunghezze $P_1=x,P_2=y$, allora l'operazione di **merge** avrà costo $$O(x+y)$$
Il fattore cruciale di tutto questo è stato l'aver ordinato i posting secondo il docID

L'algoritmo di merge è quindi

```pseudo
```
```pseudo
\begin{algorithm}
    \caption{Intersect}
    \begin{algorithmic}
      \Procedure{Intersec}{$p_{1}, p_{2}$}
        \State $\text{answer} \gets \emptyset$
          \While{$p_{1}\neq$ NULL and $p_{2}\neq$ NULL}
	          \If{$docID(p_{1})=docID(p_{2})$}
		          \State \Call{Add}{answer,docID($p_1$)}
		          \State $p_1\gets\text{next}(p_1)$
		          \State $p_2\gets\text{next}(p_2)$
		        \Elif{$docID(p_{1})\lt docID(p_{2})$}
			        \State $p_1\gets\text{next}(p_1)$
			        \State $p_2\gets\text{next}(p_2)$
              \EndIf
          \EndWhile
          \Return answer
        \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

---
# Boolean Retrieval Model & Extendend Boolean Models

Passiamo ora a vedere un particolare modello di IR, il **boolean retrieval model**

Questo modello è capace di rispondere a query di tipo Boolean, ovvero query che usano gli operatori AND, OR e NOT per concatenare i termini della query
- si vedono ogni documento come un *insieme* di parole
- si vede se il documento **combacia** con la condizione oppure no

Per circa $3$ decenni è stato il tool di retrieval commerciale più usato, e molti sistemi attuali ancora lo usano

Un'esempio di questo sistema è Westlaw[^1]

ALcuni esempi di query:
1) Qual è il termine di prescrizione nei casi che coinvolgono la legge federale sui risarcimenti per danni?
	- **query** -> LIMIT! /3 STATUTE ACTION /S FEDERAL /2 TORT /3 CLAIM
		- /3 = entro 3 parole, /S = nella stessa frase
2) Requisiti affinché le persone con disabilità possano accedere a un luogo di lavoro
	- **query** -> disabl! /p access! /s work-site work-place (employment /3 place)

**Esercizio 1** : adattare il merge per le query
- Brutus AND NOT Caesar
- Brutus OR NOT Caesar
Possiamo ancora eseguire il merge in tempo $O(x+y)$

**Esercizio 2** : Cosa possiamo dire di una formula Booleana arbitraria, del tipo:
- (Brutus OR Caesar) AND NOT (Antony OR Cleopatra)
Possiamo ancora eseguire il merge in tempo lineare? Possiamo fare di meglio?
## Query optimization

Un problema fondamentale quando si processano query è: Qual è il miglior ordine per processare una query?

Prendiamo ad esempio una query fatta dell' AND fra $n$ termini, es.
- Brutus AND Calpurnia AND Caesar

Una soluzione possibile è la seguente -> per ogni termine, prendiamo la sua lista di postings e poi si fa l'AND fra loro

![500](img/Pasted%20image%2020260313110557.png)

Questa soluzione però non è troppo buona.

La soluzione migliore è processare in base alla ***frequenza crescente***
- si inizia con gli insiemi più piccoli, e poi si continua a tagliare ulteriormente

Questo è esattamente il motivo per cui abbiamo lasciato la document frequency nel dizionario dell' Inverted Index

Una volta fatto questo, si esegue la query precedente come:
- (Calpurnia AND Brutus) AND Caesar

**Esercizio 3** : Scrivere un ordine di processo per la seguente query, considerando il dizionario in foto (vedi giù):
- (tangerine OR trees) AND (marmalade OR skies) AND (kaleidoscope OR eyes)

![300](img/Pasted%20image%2020260313111203.png)

Possiamo quindi definire una **ottimizzazione** generale
- es. (madding OR crowd) AND (ignoble OR strife)
- 1. Si prendono le document freq. di tutti i termini
- 2. Si calcola la dimensione di ogni OR considerando la somma delle document freq.
- 3. Si elabora la query in ordine crescente di OR



[^1]: http://www.westlaw.com/
