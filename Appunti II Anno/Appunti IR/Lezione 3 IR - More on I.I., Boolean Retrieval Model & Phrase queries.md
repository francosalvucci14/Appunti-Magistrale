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

## Query Processing with I.I

La domanda che sorge spontanea, dopo aver visto come si crea un Inverted Index è:

> Come processiamo una query? e più avanti, che *tipo* di query possiamo processare?

### Query Processing: AND

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

**Altri esercizi**:
- se la query è friends AND romans AND (NOT countrymen), come possiamo usare la frequenza di countrymen?
- estendere il merge ad una query Booleana arbitraria. Possiamo sempre garantire che il tempo di esecuzione sia lineare nella dimensione totale dei postings?
---
# Phrase queries & positional indexes

In questa sezione vediamo come processare query del tipo "stanford university" - ovvero query che vengono intese come *frasi*

In questo caso, la sentenza "I went to university at Stanford" non è un match valido

> Il concetto di ***ricerca per frasi*** si è dimostrato facilmente comprensibile per gli utenti; infatti è una delle idee di "ricerca avanzata" che funziona

Per fare questo, non è più sufficiente salvare in memoria solo le coppie `<term:docs>`
## Prima soluzione: Biword indexes

Un primo approccio è quello di usare i **Biword indexes**

L'idea dietro è la seguente:

> Si indicizzano le coppie **consecutive** di termini nel testo come se fossero frasi

Esempio: se il testo è "Friends, Roman, Countrymen" -> si generano le seguenti **biwords**:
- friends roman
- roman countrymen

Ogniuna delle biwords create risulta quindi essere un **dizionario di termini**

Così facendo, il query-processing di frasi a due parole risulta essere immediato

Non ci limitiamo solamente alle frasi a due parole, ma il concetto di Biword Indexes può essere esteso anche a frasi più lunghe; infatti testi più lunghi vengono semplicemente processati **scomponendo** i termini fra loro

Esempio: il testo "stanford university palo alto" può essere scomposto in query Booleane su biwords, ottenendo la seguente query: "stanford university AND university palo AND palo alto"

***Attenzione***: senza i documenti, non possiamo verificare che i documenti corrispondenti alla query Booleana sopra riportata contengano effettivamente la frase

> Di conseguenza otteniamo i cosi detti ***falsi positivi***

Un'altra problematica relativa all'uso dei Biword indexes è che la dimensione degli indici **esplode** con dizionari più grandi
- infatti questa tecnica è impraticabile per più di due parole, e comunque anche per loro è già troppo grande

Di conseguenza affermiamo che questa tecnica non è proprio la soluzione standard, MA può essere parte di una ***strategia combinata***
## Seconda soluzione: Positional indexes

Abbiamo appena visto quindi che la soluzione con i Biword indexes non è proprio la soluzione migliore al problema delle query a frasi

Il secondo approccio che vediamo prende il nome di ***positional indexes***; la logica è la seguente

> Nelle liste di postings salviamo, **per ogni termine**, la sua posizione (/posizioni) in cui compaiono i suoi token

Otteniamo quindi una struttura del genere:

 ```
 <term, #doc contenenti term;
  doc1: position1, position2,...;
  doc2: position1, position2,...;
  etc...>
 ```

**Esempio** : per il termine "be"; quale fra questi documenti contiene la frase "to be or not to be"?

```
 <be, 993427;
  1: 7,18,33,72,86,231;
  2: 3,149;
  4: 17,191,291,430,434;
  5: 363,367,...>
```

A questo punto, per le queri su frasi utilizziamo l'algoritmo di Merge in modo ricorisivo a livello di documento

Il problema però è che adesso dobbiamo gestire più della semplice uguaglianza

Processiamo ora la query di prima, ovvero "**to be or not to be**"

1. Estraiamo le entrate dell' inverted index per ogni termine distinto: **to,be,or,not**
2. Uniamo le loro liste *doc:position* per enumerare tutte le posizioni contenenti **to be or not to be**
	1. **to** -> 2 : 1,17,74,222,551 ; *4 : 8,16,190,429,433* ; 7 : 13,23,191,...
	2. **be** -> 1 : 17,19 ; *4 : 17,191,291,430,434* ; 5 : 14,19,101,...

Stesso metodo generale per le ***ricerche di prossimità***

C'è un piccolo problema però con gli indici posizionali, ovvero che la loro presenza aumenta **notevolmente** la dimensione dei postings, anche se gli indici possono venire compressi

Ciononostante, l'indice posizionale è ormai di uso comune grazie alla potenza e all'utilità delle query basate su frasi e sulla prossimità... sia che venga utilizzato in modo esplicito o implicito in un sistema di classificazione e recupero dei risultati

In un indice standard, registri solo _se_ una parola compare in un documento (es. "La parola 'cane' si trova nel Documento 4"). In un indice posizionale, bisogna registrare _ogni singola posizione_ in cui la parola compare (es. "La parola 'cane' si trova nel Documento 4 alle posizioni 12, 45 e 110").

La dimensione dell'indice dipende quindi dalla dimensione media del documento
Infatti, se un documento è molto lungo allora una stessa parola avrà più probabilità di ripetersi. Mentre l'indice standard aggiungerà sempre e solo un elemento (il documento ID), l'indice posizionale dovrà aggiungere una nuova posizione per ogni singola ripetizione.

Prendiamo ad esempio un temrine con frequenza $0.1\%$ (ovvero compare una volta ogni 1000 termini):
- In un documento di **1.000 parole**, la parola compare 1 volta. Sia l'indice standard (Postings) che quello posizionale (Positional postings) registrano 1 solo valore.
- In un documento di **100.000 parole** (es. un libro), la parola compare 100 volte. L'indice standard continua a usare **1 solo posting** (dice semplicemente "la parola è in questo libro"). L'indice posizionale, invece, ha bisogno di **100 postings** per registrare l'esatta posizione di ogni occorrenza.

Abbiamo quindi la seguente situazione:

| Doc Size | Postings | Positional Postings |
| -------- | -------- | ------------------- |
| 1000     | 1        | 1                   |
| 100.000  | 1        | 100                 |

Di conseguenza otteniamo le seguenti **regole pratiche**:
- - **2-4 volte più grande:** A causa di tutti i numeri extra necessari per memorizzare le posizioni esatte di ogni parola, un indice posizionale è generalmente dalle 2 alle 4 volte più pesante di un indice non posizionale.
- **Rispetto al testo originale:** La dimensione totale dell'indice posizionale corrisponde circa al 35% - 50% del volume del testo originale. Questo significa che se bisogna indicizzare un database di testi di 1 GB, l' indice posizionale peserà tra i 350 MB e i 500 MB.
- **L'eccezione (Caveat):** Queste stime valgono per lingue strutturate come l'inglese ("English-like"). Lingue con morfologie molto diverse, come il cinese (che non ha spazi tra le parole) o le lingue agglutinanti (come il finlandese o il turco), avranno rapporti di grandezza differenti.

**Il problema dell'indice posizionale:** Se un utente cerca la frase esatta `"Michael Jackson"`, il sistema deve prendere la lista infinita di tutte le posizioni di "Michael" e la lista di tutte le posizioni di "Jackson", per poi incrociarle e vedere dove "Jackson" compare esattamente una posizione dopo "Michael". È un'operazione pesante. Diventa un incubo per query come `"The Who"`, perché "The" e "Who" sono "stop words" comunissime presenti in quasi tutti i documenti.

**La soluzione (Schema Misto):** Invece di fare questo calcolo ogni volta, conviene indicizzare le frasi più comuni (es. "Michael Jackson") come se fossero una singola parola nel vocabolario, mantenendo l'indice posizionale per tutto il resto.

**I risultati (Williams et al., 2004):** Questo schema ibrido crea un classico compromesso (trade-off) tra spazio e tempo:
- **Vantaggio (Tempo):** Le query miste tipiche del web vengono eseguite in **1/4 del tempo** rispetto all'uso del solo indice posizionale (sono molto più veloci).
- **Svantaggio (Spazio):** Richiede il **26% di spazio in più** sul disco rispetto al semplice indice posizionale, perché devi salvare nel vocabolario anche le frasi composte oltre alle singole parole.

[^1]: http://www.westlaw.com/
