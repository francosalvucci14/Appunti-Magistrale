# Index Construction

Le domande che ci poniamo in questa sezione sono:
- Come costruiamo un indice?
- Che strategie possiamo usare avendo memoria limitata?

Ricordiamo le basi di costruzione gettate qualche lezione fa
1) Vengono estratte le parole dai documenti, e salvate in un dizionario con entrate *<Term;DocID>*
2) Quando tutti i documenti sono stati elaborati, il dizionario viene ordinato in base ai termini

Prendiamo anche come base il dataset RCV1: lo useremo per un pò

Guardando un po le statistiche di RCV1 notiamo la seguente situazione

![center|400](img/Pasted%20image%2020260324121706.png)

Vediamo subito due valolri molto strani, ovvero : 4.5 bytes per word token vs. 7.5 bytes per word type

Perchè questa distinzione?

Per capire la differenza tra 4.5 e 7.5, dobbiamo prima chiarire bene la differenza tra **Token** e **Type** (o Termine):

- **Token (Occorrenza):** È ogni singola parola così come appare nel testo. Se la parola "il" compare 10.000 volte nei documenti, conterai 10.000 token.
- **Type / Term (Vocabolo univoco):** È la parola inserita nel "dizionario" dell'indice. Se la parola "il" compare 10.000 volte, nel dizionario verrà inserita **una sola volta**. È un _type_.

Ecco perché le medie sono così diverse
1. La media sui Token (4.5 bytes)
	1. In quasi tutte le lingue naturali (inglese incluso, che è la lingua del dataset RCV1), **le parole usate più di frequente sono molto corte**. Pensa ad articoli, preposizioni e congiunzioni come _the_, _a_, _of_, _to_, _in_, _and_. Quando calcoli la lunghezza media dei _token_, stai contando queste paroline di 1, 2 o 3 lettere milioni di volte. Questa valanga di parole cortissime "tira giù" inesorabilmente la media matematica, portandola a circa 4.5 caratteri (in questo contesto, 1 byte = 1 carattere standard ASCII).
2. La media sui Type / Term (7.5 bytes)
	1. Quando calcoli la media sui _type_, stai guardando la lista del vocabolario (i 400.000 termini unici indicati nella slide). In questa lista, la parolina "the" (3 lettere) vale esattamente quanto la parola "information" (11 lettere) o "unconstitutional" (16 lettere): ciascuna conta per uno. Poiché in qualsiasi lingua esistono molte più parole lunghe (termini tecnici, nomi, aggettivi complessi) rispetto alle poche decine di particelle grammaticali corte, la media della lunghezza si alza notevolmente, arrivando a 7.5 caratteri.

**In sintesi:** Leggiamo in continuazione parole corte (ecco perché i token sono di 4.5 bytes in media), ma il nostro vocabolario è composto per la stragrande maggioranza da parole lunghe che usiamo raramente (ecco perché i type sono di 7.5 bytes in media).

Il processo logico per creare un indice è semplice: si analizzano i documenti, si estraggono le parole e si associano all'ID del documento in cui si trovano. Il passaggio cruciale, tuttavia, è **l'ordinamento**.

- Dopo aver estratto tutte le coppie (termine, ID documento), bisogna riordinare l'intero file in base al termine.
- Se usiamo come esempio la collezione Reuters RCV1 (800.000 documenti), otteniamo circa 100 milioni di queste coppie (postings).
- A 8 byte per coppia, l'indice richiede molto spazio. Anche se 100 milioni di record oggi possono stare in RAM, per collezioni reali molto più grandi (come il web o gli archivi del New York Times) la memoria interna non basta. Siamo costretti a salvare i risultati intermedi sul disco rigido.

Per capire le soluzioni, bisogna prima capire come funziona l'hardware:

- L'accesso ai dati in memoria (RAM) è enormemente più veloce rispetto all'accesso ai dati sul disco.
- Sul disco rigido ci sono i tempi di "seek" (posizionamento della testina), durante i quali non viene trasferito alcun dato.
- Di conseguenza, leggere e scrivere sul disco è efficiente solo se lo si fa a "blocchi" di grandi dimensioni, invece che trasferire continuamente piccoli pezzettini di dati.
- **Conclusione:** Non possiamo semplicemente applicare un normale algoritmo di ordinamento sul disco, perché richiederebbe troppi salti della testina, risultando lentissimo. Ci serve un algoritmo di "external sorting" (ordinamento esterno)
# External Memory Indexing
## Primo Algoritmo: BSBI (Blocked Sort-based Indexing)

il BSBI è il primo metodo proposto per risolvere il problema riducendo gli accessi al disco.

- **Come funziona:** Accumula le coppie (termID, docID) in memoria fino a riempire un "blocco" (es. 10 milioni di record). Poi ordina questo blocco in memoria e lo scrive sul disco. Ripete l'operazione fino alla fine dei documenti, creando vari blocchi ordinati.
- **La fusione (Merge):** Alla fine, tutti questi blocchi parziali vengono fusi in un unico grande indice. Per farlo velocemente, si esegue un "multi-way merge": si aprono tutti i file contemporaneamente, si legge un pezzo di ciascun blocco in memoria e si scrivono i dati fusi sul disco in grandi blocchi, evitando colli di bottiglia hardware.
- **Il limite del BSBI:** Questo algoritmo presuppone che si possa mantenere in RAM un grande dizionario globale che mappa ogni termine di testo al suo identificativo numerico (termID). Se la collezione è immensa, anche solo questo dizionario potrebbe saturare la memoria.

Lo pseudocodice di questo algoritmo è quindi il seguente:

```pseudo
\begin{algorithm}
    \caption{BSBI}
    \begin{algorithmic}
      \Procedure{BSBIndexCostruction}{}
        \State $n \gets 0$
          \While{all doc. have not been processed}
          \State $n \gets n+1$
		          \State block $\gets$ \Call{ParseNextBlock}{}
		          \State \Call{BSBI-Invert}{block}
		          \State \Call{WriteBlockToDisk}{block,$f_n$}
          \EndWhile
          \State \Call{MergeBlocks}{$f_{1},\dots,f_{n};f_{\text{merged}}$}
        \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```
Vediamo ora nel dettaglio le fasi dell'algoritmo
### Fase 1: Ordinamento interno dei blocchi

Abbiamo stabilito che non possiamo ordinare tutti i 100 milioni di record in una volta sola nella RAM.

- **Cosa succede:** L'algoritmo riempie la memoria con un "blocco" di dati alla volta (in questo esempio, 10 milioni di record). Una volta che il blocco è in memoria, lo ordina internamente utilizzando un algoritmo classico come il Quicksort, che richiede un tempo stimato di $O(N\ln N)$.
- **Il risultato:** Questo processo viene ripetuto 10 volte, generando sul disco 10 file separati chiamati **"runs"** (sequenze), ognuno contenente 10 milioni di record perfettamente ordinati.
### Fase 2.1: Unione dei blocchi (approccio base)

Adesso abbiamo 10 file separati e ordinati sul disco, ma a noi serve un unico grande indice invertito. Dobbiamo fonderli (_merge_).

- **Fusione Binaria:** Un approccio è fare fusioni a due a due (binary merges). Come si vede nel diagramma, prendiamo il file 1 e il file 2, li portiamo in memoria, incrociamo i dati e scriviamo un nuovo file fuso sul disco.
- **Il diagramma in azione:** Guarda il termine "brutus". Nel primo blocco appare nei documenti `d1, d3`. Nel secondo blocco appare nei documenti `d6, d7`. L'operazione di merge combina semplicemente queste liste in modo ordinato creando la lista finale `d1, d3, d6, d7`.
- **Il problema:** Questo metodo crea un "albero" di fusioni di $\log_2​ 10=4$ livelli. Costringe il sistema a leggere e riscrivere gli stessi dati sul disco più e più volte, sprecando tempo prezioso.

![center|500](img/Pasted%20image%2020260325113935.png)
### Fase 2.2: Unione dei blocchi (approccio efficiente)

Per evitare le inefficienze della fusione binaria, il BSBI utilizza una tecnica molto più intelligente: la **fusione multi-via (multi-way merge)**. È qui che aggiriamo i limiti hardware del disco fisso (i tempi di seek).

- **Come funziona:** Invece di fonderli a due a due, l'algoritmo **apre tutti i 10 blocchi contemporaneamente**.
- **Uso dei Buffer:** Assegna a ciascun blocco un "read buffer" (un piccolo spazio in RAM dove carica un pezzetto del file dal disco) e usa un "write buffer" per il file finale in uscita.
- **La Coda di Priorità:** L'algoritmo guarda i primissimi elementi di tutti i 10 buffer, sceglie il termine più piccolo in ordine alfabetico (usando una struttura dati chiamata _priority queue_), unisce tutte le sue liste di documenti e lo sposta nel buffer di scrittura.
- **Il trucco Hardware:** Poiché si leggono e scrivono dal disco blocchi di dati ("chunks") di dimensioni consistenti solo quando i buffer si riempiono o si svuotano, si minimizzano i salti della testina del disco, rendendo l'operazione estremamente veloce
### Fase 3: Il "Tallone di Achille" del BSBI

Questa è la parte cruciale che fa da ponte verso l'algoritmo successivo (lo SPIMI). Spiega perché il BSBI, per quanto ottimizzato con la fusione multi-via, fallisce su scale immense (come l'indicizzazione del Web).

- **L'assunto fatale:** Il BSBI per funzionare velocemente non usa le parole intere (es. "brutus"), ma le converte in numeri (`termID`). Per fare questa conversione parola → numero, **deve mantenere in RAM un dizionario globale** che cresce dinamicamente man mano che scopre nuove parole nei testi.
- **Il limite:** Se la collezione di documenti è gigantesca, il vocabolario diventerà così grande che **il solo dizionario esaurirà tutta la memoria RAM disponibile** prima ancora di poter elaborare i blocchi.
## Secondo Algoritmo: SPIMI (Single-pass In-memory Indexing)

Lo SPIMI risolve i problemi del BSBI con un approccio molto più intelligente ed efficiente. Si basa su due idee chiave:

- **Idea Chiave 1 - Dizionari separati:** Invece di avere un dizionario globale in RAM, lo SPIMI genera un dizionario indipendente per ogni singolo blocco.   
- **Idea Chiave 2 - Niente ordinamento iniziale:** Invece di accumulare singole coppie e poi ordinarle, lo SPIMI costruisce le liste direttamente. Man mano che legge le parole, le aggiunge al dizionario (se non ci sono già) e accoda l'ID del documento direttamente alla lista di quel termine.
- **Chiusura del blocco:** Quando la memoria RAM si riempie, l'algoritmo semplicemente ordina alfabeticamente il dizionario locale e scrive l'intero blocco sul disco.

**Perché SPIMI è superiore?** Consuma molta meno memoria rispetto al BSBI e fa risparmiare tantissimo tempo di calcolo, dato che non deve ordinare milioni di coppie individuali, ma ordina solo i vocaboli del dizionario prima di scriverli su disco.

Lo pseudocodice dell'algoritmo SPIMI è il seguente

```pseudo
\begin{algorithm}
    \caption{SPIMI}
    \begin{algorithmic}
      \Procedure{SPIMI-Invert}{token\_stream}
        \State out\_file $\gets$ \Call{NewFile}{}
        \State dict $\gets$ \Call{NewHash}{}
          \While{free memory available}
          \State token $\gets$ next(toker\_stream)
          \If{term(token)$\not\in$ dict}
          \State postings\_list $\gets$ \Call{AddToDict}{dict,term(token)}
          \Else
          \State postings\_list $\gets$ \Call{GetPostingsList}{dict,term(token)}
          \EndIf
          \If{full(postings\_list)}
          \State postings\_list $\gets$ \Call{DoublePostingsList}{dict,term(token)}
          \EndIf
          \State \Call{AddToPostingsList}{postings\_lists,docID(token)}
          \EndWhile
          \State sorted\_terms $\gets$ \Call{SortTerms}{dict}
          \Call{WriteBlockToDisk}{sorted\_term,dict,out\_file}
          \Return out\_file
        \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```
### SPIMI in azione

Qui vediamo cosa succede nella memoria RAM passo dopo passo:

- **Fase 1: Input token (Il flusso in ingresso)** L'algoritmo legge le parole dai documenti una per volta. Come vedi nella prima colonna, arrivano coppie grezze come `Caesar d1` (la parola Caesar trovata nel documento 1) o `with d1`.
- **Fase 2: Dictionary (Costruzione delle liste "al volo")** Nel BSBI avremmo salvato ogni singola riga per ordinarla dopo. Lo SPIMI invece, usa una struttura a dizionario dinamica. Quando legge `Caesar d1`, crea la voce "caesar" e ci attacca `d1`. Quando più avanti legge `Caesar d2`, non crea una nuova riga, ma va semplicemente ad allungare la lista esistente, facendola diventare `d1 d2 d4`. _Nota bene:_ In questa fase centrale, l'ordine delle parole nel dizionario è casuale (`brutus`, `with`, `noble`, `caesar`) perché l'obiettivo è solo accumulare i dati il più velocemente possibile.
- **Fase 3: Sorted dictionary (Ordinamento finale del blocco)** Quando la memoria RAM si riempie, lo SPIMI fa l'unica operazione di ordinamento necessaria: **ordina alfabeticamente solo i termini del vocabolario** (trasformando l'ordine in `brutus, caesar, noble, with`). Le liste dei documenti ad essi collegate lo seguono passivamente. A questo punto, il blocco è pronto e viene scritto sul disco.

**Il collegamento col BSBI:** Questa slide dimostra come lo SPIMI eviti il catastrofico costo hardware di dover ordinare 100 milioni di singole coppie (il tallone d'Achille del BSBI). Ordina solo le poche migliaia di vocaboli univoci presenti in quel blocco!
### SPIMI: Compressione

Poiché lo SPIMI fa tutto in RAM, **la sua efficienza dipende interamente da quanti dati riusciamo a far stare in memoria** prima di doverci fermare e scrivere il blocco sul disco.

Per far stare più dati possibile nello stesso spazio RAM, la compressione rende lo SPIMI ancora più efficiente:

- **Compressione dei termini (Compression of terms)**: Invece di salvare le parole chiave nel dizionario usando tanto spazio (ricordi i 7.5 bytes per type di cui parlavamo prima?), si usano trucchi per comprimere il testo del vocabolario.
- **Compressione dei postings (Compression of postings)**: Invece di salvare gli ID dei documenti per intero (es. `d1000, d1005, d1008`), si salvano solo le distanze tra un documento e l'altro (es. `d1000, +5, +3`). Questo riduce drasticamente lo spazio occupato dalle lunghissime liste di numeri.


