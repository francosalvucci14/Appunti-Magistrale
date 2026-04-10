# Distributed Indexing

Quando si vuole indicizzare l'intero Web, bisogna per forza usare un cluster di calcolo distribuito. 

I grandi motori di ricerca come Google, Bing e Baidu non usano supercomputer fantascientifici, ma immensi data center sparsi per il mondo pieni di "commodity machines", ovvero computer standard ed economici. 
Già nel 2007, si stimava che Google avesse circa 1 milione di server e 3 milioni di processori.

Ma c'è un problema enorme: **le singole macchine si guastano di continuo o rallentano in modo imprevedibile**.

Si può dare anche una dimostrazione matematica a ciò:

- Se hai un sistema con 1000 nodi e ogni nodo è affidabile al $99,9\%\dots$
- il tempo in cui _tutto_ il sistema funziona perfettamente è appena il $37\%$.
- Questo significa che per il **$63\%$ del tempo c'è almeno un server guasto**. Immagina cosa succede con un milione di server: i guasti avvengono al minuto!

Come si gestisce questo livello di fallimento hardware? Con una rigida divisione dei ruoli per sfruttare questo "pool" di macchine:

- **Il Master (Il Direttore dei Lavori):** C'è una macchina principale, considerata "sicura", che non fa il lavoro sporco ma si limita a dirigere le operazioni di indicizzazione.
- **Le Task Parallele:** Il lavoro enorme viene spezzettato in compiti paralleli, e il Master li assegna alle macchine che in quel momento sono inattive.
- **Gli "Operai" (Parsers e Inverters):** I compiti si dividono in due squadre specializzate, i Parsers e gli Inverters.
- **Gli Splits:** La gigantesca collezione di documenti in ingresso non viene elaborata tutta insieme, ma spezzettata in sottoinsiemi di documenti chiamati "splits" (che sono concettualmente identici ai blocchi che abbiamo visto negli algoritmi BSBI e SPIMI)
## Data Flow

Vediamo ed analizziamo quindi il **data flow** di questo processo di Indexing Distribuito

![center|500](img/Pasted%20image%2020260407142600.png)

Leggiamo il diagramma da sinistra verso destra:

1. **Gli Splits in ingresso:** A sinistra abbiamo i blocchi di documenti grezzi.    
2. **Fase Map (I Parsers):** Il Master prende uno split e lo assegna a un **Parser**. Il Parser legge i documenti ed estrae le parole chiave.
3. **I Segment Files (Lo smistamento):** Invece di fare un unico minestrone, il Parser divide le parole estratte in secchielli alfabetici (le "partitions"). Come si vede nel diagramma, le parole dalla A alla F vanno in un secchiello, dalla G alla P in un altro, e dalla Q alla Z in un altro ancora.
4. **Fase Reduce (Gli Inverters):** Ora entrano in gioco gli **Inverters**. Il Master assegna un secchiello alfabetico a un Inverter specifico. Ad esempio, il primo Inverter in alto si prende _tutti_ i pezzettini "a-f" generati da tutti i Parser precedenti.
5. **Il Risultato Finale (Postings):** L'Inverter ordina queste parole, fonde i dati e scrive su disco l'indice invertito definitivo (Postings) per la sua fetta di alfabeto.

Il vero colpo di genio di questo schema è che se un Parser o un Inverter si rompe a metà del lavoro, il Master se ne accorge, prende quello stesso pezzo di lavoro e lo riassegna semplicemente a un'altra macchina inattiva, senza dover ricominciare tutto da capo.
### Parser (Fase MAP)

Il Parser è l'operaio specializzato nella prima fase del lavoro.

- Il Master individua una macchina inattiva (idle) e le assegna uno "split", ovvero un blocco di documenti grezzi da elaborare.
- Il compito del Parser è leggere un documento alla volta ed estrarre le singole parole, emettendo delle coppie composte dal termine e dall'ID del documento `(term, doc)`. 
- **Lo smistamento intelligente:** Il Parser non butta queste coppie in un unico grande calderone, ma le scrive separandole in $j$ partizioni distinte.
- Un classico esempio di questo smistamento è la divisione in base alla prima lettera del termine: ad esempio, una partizione per le parole da _a_ a _f_, una per quelle da _g_ a _p_, e una da _q_ a _z_ (in questo caso $j=3$).
### Invertes

Una volta che i Parser hanno finito di estrarre e smistare le parole, entrano in gioco gli Inverter per completare l'inversione dell'indice.

- Un Inverter raccoglie tutte le coppie `(term, doc)` appartenenti a una **singola partizione di termini**. Ad esempio, un Inverter specifico si occuperà _solo_ di tutte le parole che iniziano con le lettere dalla A alla F, raccogliendole da tutti i Parser del sistema.
- Il suo compito finale è prendere questa immensa mole di coppie grezze, ordinarle alfabeticamente e scriverle nelle liste di invio definitive (postings lists) su disco.

Vediamo un'esempio pratico

- **Fase Map (Parser):** Immagina due documenti. Il documento `d1` dice "C came, C c' ed" (Caesar came, Caesar conquered) e il `d2` dice "C died" (Caesar died). Il Parser legge e sputa fuori coppie grezze: `<C, d1>`, `<came, d1>`, un altro `<C, d1>`, e così via.    
- **Fase Reduce (Inverter):** L'Inverter riceve queste coppie disordinate, raggruppa tutti i documenti in cui compare una parola creando una lista come `<C, (d1, d1, d2)>`, e infine calcola le frequenze esatte per ottimizzare l'indice, trasformandola in `<C, (d1:2, d2:1)>` (ovvero: la parola "C" compare 2 volte in d1 e 1 volta in d2).

L'algoritm che abbiamo appena visto crea quello che si chiama un **indice partizionato per termini (term-partitioned index)**.

- In un indice _term-partitioned_, una singola macchina gestisce un sottoinsieme specifico del vocabolario (es. tutte le parole dalla A alla F per tutto il web).
- Tuttavia, per i motori di ricerca, la costruzione dell'indice è solo una fase. C'è un'ulteriore fase di trasformazione necessaria per convertire questo indice in un **indice partizionato per documenti (document-partitioned index)**.
- In un indice _document-partitioned_, una macchina gestisce l'intero vocabolario, ma solo per un sottoinsieme specifico di documenti.    
- La maggior parte dei motori di ricerca usa quest'ultimo approccio perché garantisce un bilanciamento del carico (load balancing) di gran lunga superiore quando milioni di utenti fanno ricerche contemporaneamente.
# MapReduce

L'intero algoritmo di costruzione dell'indice distribuito che abbiamo appena definitio (con i master, i parser e gli inverter) non è altro che un'istanza classica di **MapReduce**.

- **Cos'è:** MapReduce (introdotto in una celebre pubblicazione da Dean e Ghemawat nel 2004) è un framework per il calcolo distribuito robusto e concettualmente molto semplice.
- **Il vero "Superpotere":** Il punto chiave assoluto è: MapReduce permette di fare tutto questo _senza dover scrivere il codice per la parte di distribuzione_. In pratica, un programmatore deve solo scrivere due funzioni (la "Map" e la "Reduce"); il framework di Google pensa automaticamente ad assegnare i compiti ai server inattivi, gestire i guasti di rete, riavviare le macchine bloccate e trasferire i dati da un nodo all'altro!
- **La Storia:** Google ha descritto il proprio sistema di indicizzazione web (risalente a circa il 2002) come un processo diviso in diverse fasi, e ciascuna di queste fasi era implementata proprio usando MapReduce.
## Schema per la costruzione dell'indice in MapReduce

Qui si fa il salto dalla teoria alla pratica informatica, mostrando lo "scheletro" logico del framework e come si adatta al nostro specifico problema dell'Information Retrieval.

**Lo Schema Astratto Generale:** In MapReduce, tutto il mondo si divide in due sole operazioni che manipolano "Chiavi" ($k$) e "Valori" ($v$):

- **La funzione Map:** Prende un input qualsiasi e lo trasforma in una lista di coppie chiave-valore, ovvero `input -> list(k, v)`.
- **La funzione Reduce:** Raccoglie una specifica chiave ($k$) associata a una lista di tutti i suoi valori `list(v)` e li "riduce" in un output finale, ovvero `(k,list(v)) -> output`.

**L'Istanziazione per l'Indice (Come lo applichiamo noi):** Ora applichiamo questo schema astratto al lavoro dei nostri Parser e Inverter per costruire un motore di ricerca:

- **Fase Map (Il lavoro del Parser):** L'input di partenza è l'intera collezione di documenti. La funzione Map estrae le parole e genera una lunghissima lista di coppie dove la chiave è il termine e il valore è il documento: `list(termID, docID)`.
- **Fase Reduce (Il lavoro dell'Inverter):** Il framework raggruppa automaticamente tutti i `docID` che hanno lo stesso `termID` (es. raggruppa tutti i documenti in cui compare la parola "Caesar"). La funzione Reduce riceve in ingresso queste liste raggruppate, come `<termID1, list(docID)>, <termID2, list(docID)>`, ecc.. Il suo compito finale è comprimerle e formattarle per sputare fuori il risultato definitivo: le liste di invio dell'indice invertito `(postings list1, postings list2, ...)`.

---
# Dynamic Indexing

Dopo aver costruito il nostro enorme indice distribuito, ci scontriamo con un problema reale: il Web non è una biblioteca polverosa, ma un ecosistema vivo e in continua espansione. Qui affrontiamo la necessità di passare da un'indicizzazione statica a un'**indicizzazione dinamica (Dynamic Indexing)**.
## Problema dell'Indicizzazione Dinamica

Fino a questo punto, avevamo lavorato sotto l'assunto di avere una collezione di documenti statica. Tuttavia, nella realtà questo avviene raramente:

- I documenti arrivano nel tempo e devono essere inseriti costantemente nel sistema.
- I documenti esistenti possono essere modificati oppure eliminati (deletions).

Di conseguenza, sia il dizionario in memoria che le liste di postings sul disco non possono rimanere immutabili, ma devono essere aggiornati. Ciò comporta due tipi di operazioni:

1. **Aggiornamento dei postings:** Aggiungere nuovi ID di documento alle liste di termini già presenti nel dizionario.
2. **Aggiunta di nuovi termini:** Inserire nel dizionario parole mai viste prima e creare le relative nuove liste di postings.
## L'approccio "ingenuo"

Vediamo il metodo più semplice e basilare per gestire questi aggiornamenti continui, senza dover ricostruire l'intero indice da zero a ogni nuova pagina web scoperta.

- **Architettura a due livelli:** Si mantiene il grande indice principale ("big" main index) sul disco e si crea un indice ausiliario più piccolo ("small" auxiliary index), solitamente tenuto in memoria RAM.
- **Inserimenti:** Tutti i nuovi documenti in arrivo vengono elaborati e inseriti _solo_ nell'indice ausiliario.
- **Interrogazione (Querying):** Quando un utente fa una ricerca, il sistema deve interrogare simultaneamente sia l'indice principale che quello ausiliario, per poi fondere (merge) i risultati prima di mostrarli.
- **Gestione delle eliminazioni:** Le cancellazioni sono gestite tramite un "vettore di bit di invalidazione" (invalidation bit-vector). In pratica, è una lista in cui ogni documento ha un flag (0 o 1) che indica se è stato cancellato. Prima di restituire i risultati all'utente, il sistema filtra l'output nascondendo i documenti marcati come eliminati nel vettore.
- **Ricostruzione:** Periodicamente, quando l'indice ausiliario diventa troppo grande, il sistema si ferma e re-indicizza tutto fondendolo in un unico, nuovo indice principale.
### Limiti dell'approccio ingenuo

Questo approccio però presenta gravi limiti prestazionali su larga scala.

- **Il problema delle fusioni (Merges):** Il difetto principale risiede nella necessità di fusioni frequenti tra l'indice ausiliario e quello principale. Questo comporta dover leggere e riscrivere sul disco enormi moli di dati, causando un crollo drastico delle prestazioni (poor performance) durante l'operazione di merge.
- **Il paradosso dell'efficienza:** _In teoria_, fondere i due indici sarebbe un'operazione banalissima (un semplice "append", un'aggiunta in coda) se mantenessimo un singolo file separato sul disco per ogni singola parola del dizionario (per ogni postings list).
- **Il collo di bottiglia del Sistema Operativo:** _In pratica_, un vocabolario di milioni di termini richiederebbe milioni di file aperti contemporaneamente. Questa frammentazione estrema è inaccettabile e profondamente inefficiente per i file system dei sistemi operativi.
- **Il compromesso reale:** Per scopi didattici, si assume che l'indice sia memorizzato in un unico grande file. Nella realtà ingegneristica, i motori di ricerca adottano soluzioni ibride: ad esempio, spezzano su più file solo le liste di postings eccezionalmente lunghe (come quelle della parola "il"), o raggruppano in un unico file decine di liste molto corte (parole rare che compaiono in un solo documento).
## Un'idea migliore: Il Merge Logaritmico

Dopo aver visto che l'approccio "ingenuo" (unire continuamente un piccolo indice a uno gigantesco) fa crollare le prestazioni del disco, entriamo nel territorio delle soluzioni ingegneristiche avanzate.

Il **Merge Logaritmico (Logarithmic Merge)** è una soluzione elegante e matematicamente molto più efficiente.
### Funzionamento
 
L'idea alla base è la seguente:

Invece di avere solo due indici (uno principale e uno ausiliario), il sistema mantiene una **serie di indici**, dove ciascuno è grande esattamente il doppio del precedente.

- In qualsiasi momento, solo alcune di queste potenze di $2$ esistono fisicamente (sono istanziate) sul disco.
- L'indice più piccolo della catena si chiama $Z_0​$ e viene mantenuto direttamente in memoria RAM.
- Gli indici via via più grandi ($I_0​,I_1​,I_2​,\dots$) vengono salvati sul disco.

L'inserimento dei dati procede come un contagiri.

- Quando l'indice in memoria $Z_0$​ diventa troppo grande (supera una soglia $n$), viene scritto sul disco e prende il nome di $I_0$​.
- Se sul disco esiste già un indice $I_0​$, i due vengono fusi (merge) per formare un nuovo indice temporaneo $Z_1$​.
- A questo punto, se non c'è nessun $I_1​, Z_1$​ viene salvato come $I_1$​. Altrimenti, si fonde a sua volta con $I_1$​ per formare $Z_2$​, e così via in una reazione a catena.

![center|500](img/Pasted%20image%2020260407144646.png)

**osservazione** : attenzione, nello schema qui sopra il ruolo degli indici $Z_{i},I_i$ è stato invertito dal professore; il ruolo corretto è comunque quello scritto sopra nella spiegazione
### Analisi della complessità

Qui giustifichiamo matematicamente perché si usa questo sistema apparentemente contorto. 

È un classico compromesso tra velocità di scrittura e velocità di lettura:

- **Il vecchio metodo (Main + Auxiliary):** Se abbiamo $T$ postings totali e un indice ausiliario di grandezza $n$, saremo costretti a fare $\frac{T}{n}$ fusioni totali. Nel caso peggiore, ogni singolo dato viene toccato e riscritto $\frac{T}{n}$ volte, portando il tempo di costruzione dell'indice a una disastrosa complessità quadratica di $O(\frac{T^{2}}{n})$.
- **La velocità del Logarithmic Merge (Costruzione):** Con il sistema a cascata, ogni singolo posting viene fuso al massimo $O\left(\log\left(\frac{T}{n}\right)\right)$ volte. La complessità crolla drasticamente a $O\left(T\log\left(\frac{T}{n}\right)\right)$, rendendo la costruzione dell'indice enormemente più efficiente.
- **Il prezzo da pagare (Interrogazione):** Poiché l'indice è ora frammentato, elaborare una query (query processing) è più lento. Il motore di ricerca deve cercare la parola interrogando $O\left(\log\left(\frac{T}{n}\right)\right)$ indici separati e unire i risultati al volo, mentre nel vecchio sistema l'operazione era di complessità $O(1)$ (doveva guardare solo in due file).

Lo pseudocodice dell'algoritmo è quindi il seguente

```pseudo
\begin{algorithm}
    \caption{Logarithmic Merge Add Token Procedure}
    \begin{algorithmic}
      \Procedure{LMergeAddToken}{indexes,$Z_{0}$,token}
        \State $Z_{0} \gets$ Merge($Z_0$,{token})
          \If{$|Z_0|=n$}
	          \For{$i \gets 0$ to $\infty$}
		          \If{$I_{i}\in$ indexes}
			          \State $Z_{i+1}\gets$ Merge($I_{i},Z_{i}$)
			          \Comment{$Z_{i+1}$ è un indice temp. su disco}
			          \State indexes $\gets$ indexes - $\{I_i\}$
				    \Else
				    \State $I_i\gets Z_{i}$
				    \Comment{$Z_i$ diventa l'indice permanente $I_{i}$}
				    \State indexes $\gets$ indexes $\cup\{I_i\}$
				    \Break
                  \EndIf     
	          \EndFor
	          \State $Z_{0}\gets \emptyset$
          \EndIf
        \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

```pseudo
\begin{algorithm}
    \caption{Logarithmic Merge}
    \begin{algorithmic}
      \Procedure{LogarithmicMerge}{}
        \State $Z_{0} \gets\emptyset$
        \Comment{$Z_{0}$ è l'indice in-memory}
          \State indexes $\gets\emptyset$
	    \While{TRUE}
	    \State\Call{LMergeAddToken}{indexes,$Z_{0}$,getNextToken()}
        \EndWhile
        \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```
### I problemi "nascosti"

Oltre alla lentezza delle query, avere molteplici indici crea grattacapi statistici.

- Mantenere statistiche valide per l'intera collezione di documenti diventa molto difficile.
- **L'esempio della correzione ortografica:** Se l'utente digita una parola sbagliata, il motore di ricerca usa algoritmi di spell-correction per suggerire un'alternativa. Per decidere _quale_ alternativa suggerire, si sceglie di solito la parola che ha più "hit" (occorrenze) nei documenti.
- Calcolare accuratamente la parola più frequente spulciando tra molteplici sotto-indici e vettori di invalidazione (i documenti cancellati) è un incubo computazionale.
- **La scorciatoia:** Una soluzione pratica adottata dai sistemi è semplicemente ignorare i piccoli indici frammentati e calcolare queste statistiche basandosi _solo_ sull'indice principale più grande.

