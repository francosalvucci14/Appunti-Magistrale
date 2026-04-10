# Compressione: Cosa e perchè

Prima di tutto rinfreschiamo la memoria su cos'è un indice invertito.

- A sinistra c'è il **Dizionario** (BRUTUS, CAESAR, CALPURNIA), ovvero il vocabolario di tutti i termini unici.
- A destra ci sono i **Postings**, ovvero le lunghissime liste di numeri (gli ID dei documenti) in cui quei termini appaiono.

![center|500](Pasted%20image%2020260407151312.png)

In questa lezione analizzeremo statisticamente quanto sono grandi queste due componenti (usando sempre il database di test RCV1) e, successivamente, come comprimere matematicamente entrambe le parti.
## Perchè comprimere?

La risposta banale è "per usare meno spazio sul disco", ma in realtà i vantaggi architettonici sono molto più profondi. La compressione si fa per tre motivi principali:

**A. Risparmio di spazio fisico (Disk Space):** Compressione significa file più piccoli. Questo fa risparmiare soldi per i server e permette di offrire più spazio di archiviazione agli utenti. Ridurre lo spazio su disco è fondamentale per le liste di postings (Postings files) che sono la parte più pesante dell'indice.

**B. "In-memory speed" (Tenere più roba in RAM):** Questa è la ragione più critica. Ricordiamo che la memoria RAM è velocissima mentre il disco fisso è lento. Se si comprimono i dati possiamo:

- lasciare l'**intero Dizionario** nella memoria principale.
- Ancora meglio: i grandi motori di ricerca riescono a mantenere una porzione significativa delle stesse _liste di postings_ direttamente in RAM. La compressione ti permette di tenere molta più roba in memoria, azzerando i tempi morti.

**C. Velocizzare il trasferimento dati:** Questo è il concetto più controintuitivo dell'informatica moderna: **leggere un file compresso dal disco e decomprimerlo al volo col processore è _più veloce_ che leggere un file non compresso dal disco**. Perché? Perché il collo di bottiglia è il trasferimento dei dati fisici dalla testina del disco alla scheda madre. Il processore è così veloce che la decompressione avviene istantaneamente, risultando in un netto guadagno di tempo. Questo riduce il tempo necessario per leggere le liste di postings dal disco.

Vediamo l'impatto delle nostre scelte di indicizzazione sulle dimensioni reali del sistema.

- ricordiamo le statistiche della collezione RCV1: 800.000 documenti, 400.000 vocaboli unici (terms), e ben 100 milioni di occorrenze totali (non-positional postings).
- tabella fondamentale (Index parameters vs. what we index) che mostra come le tecniche di pre-elaborazione del testo influenzano drasticamente le dimensioni.
	- ![center|500](img/Pasted%20image%2020260407151654.png)
## Lossy vs. Lossless Compression

Definiamo le due grandi famiglie della compressione dei dati.

- **Compressione Lossless (Senza perdita):** L'algoritmo riduce lo spazio occupato, ma garantisce che **tutta l'informazione originale sia preservata e ricostruibile al 100%**. È il tipo di compressione che si usa per i file ZIP o per i testi, e **quello che facciamo quasi sempre nell'Information Retrieval (IR)** per dizionari e postings.
- **Compressione Lossy (Con perdita):** L'algoritmo scarta attivamente alcune informazioni per ottenere file molto più piccoli. Viene usato tipicamente per immagini (JPEG) o audio (MP3).

**Il legame sorprendente con il pre-processing:** La slide ci fa notare una cosa molto interessante: i classici passaggi di pulizia del testo (pre-processing) - come il _case folding_ (tutto minuscolo), l'eliminazione delle _stop words_, o lo _stemming_- possono essere considerati a tutti gli effetti una forma di **compressione lossy**. 

Quando trasformi "Mela" in "mela", hai perso per sempre l'informazione sulla lettera maiuscola originale.

Un altro esempio di tecnica _lossy_ (trattata nel Capitolo 7 del libro di testo IIR) consiste nel **potare (pruning) le voci delle liste di postings** che hanno pochissime probabilità di apparire nei primi $k$ risultati ("top $k$ list") di una query.

Questa potatura comporta quasi nessuna perdita di qualità nei risultati finali mostrati all'utente, pur riducendo le dimensioni dell'indice.
## Vocabulary Size vs. Collection Size

Prima di comprimere il dizionario, dobbiamo chiederci: quanto è grande il vocabolario dei termini? Ovvero, quante parole distinte esistono?

Potremmo pensare che, siccome il vocabolario di una lingua è finito, esista un limite massimo (upper bound). 

Ma la slide ci dice che **non possiamo assumere un limite superiore**.

- **La matematica pura:** Se consideriamo stringhe di 20 caratteri formati da 70 simboli possibili (lettere, numeri, ecc.), le combinazioni possibili sono astronomiche: almeno $70^{20}\approx 10^{37}$ "parole" diverse.
- **La pratica:** Nel mondo reale, il vocabolario continuerà a crescere all'infinito man mano che la collezione di documenti cresce. Nuovi acronimi, nomi propri, errori di battitura e codifiche internazionali (Specialmente con l'Unicode) generano continuamente nuovi _token_ unici.
## Legge di Heaps e Legge di Zipf
### Heaps

Poiché il vocabolario cresce in modo infinito, ci serve una formula matematica per stimarne le dimensioni in base a quanti testi leggiamo. 

Questa formula empirica è nota come **Legge di Heaps (Heaps' Law)**.

La formula è:
$$M=kT^b$$

Dove:

- $M$ è la dimensione del vocabolario (il numero di vocaboli univoci o _word types_).
- $T$ è il numero totale di _token_ (tutte le parole lette nella collezione di documenti).
- $k$ e $b$ sono costanti. I valori tipici calcolati empiricamente sull'inglese sono: $30\leq k\leq 100$ e $b\approx 0.5$

**Il significato del logaritmo:** Se tracciamo questa formula su un grafico in cui entrambi gli assi usano una scala logaritmica (log-log plot), la complessa curva della Legge di Heaps si trasforma in una semplice linea retta con una pendenza di circa 1/2. È la relazione lineare più semplice possibile tra le due variabili in uno spazio log-log.

La formula linearizzata diventa:

$$\log M=\log k+b\log T$$

_Nota Bene:_ Questa non è una legge della fisica inscalfibile, ma una "legge empirica", ovvero una scoperta basata sull'osservazione statistica che si è rivelata estremamente accurata per quasi tutte le lingue umane. Ci dice che il vocabolario all'inizio cresce in fretta, ma poi rallenta, sebbene non si fermi mai completamente.

La Legge di Heaps non è solo un'ipotesi accademica, ma funziona incredibilmente bene sui dati reali della collezione Reuters RCV1.

- **Il Grafico Log-Log:** Il grafico mostra una linea tratteggiata che rappresenta la retta di "miglior adattamento ai minimi quadrati" (best least squares fit) per i dati del dataset.
- **L'equazione derivata:** L'equazione di questa linea è $\log_{10}​M=0.49\log_{10}​T+1.64$
- **I Parametri:** Trasformando questa equazione per rimuovere i logaritmi, otteniamo la classica formula di Heaps ($M=kT^b$): $M=10^{1.64}T^{0.49}$. Questo ci dice che per la lingua inglese del dataset Reuters, i parametri ottimali sono $k\approx 44$ e $b=0.49$.
- **La Precisione Straordinaria:** L'efficacia empirica di questa formula è impressionante. Se la applichiamo ai primi 1.000.020 token letti, la legge prevede matematicamente l'esistenza di 38.323 termini unici. Contandoli fisicamente, i termini unici reali sono 38.365. Il margine di errore è microscopico

![center|400](Pasted%20image%2020260407153504.png)

### Zipf

Mentre la Legge di Heaps ci aiuta a prevedere la _dimensione_ del vocabolario, la **Legge di Zipf** studia le _frequenze relative_ dei termini.

- **L'assunto di base:** Nel linguaggio naturale esistono pochissime parole usate con una frequenza altissima (come articoli e preposizioni) e moltissime parole usate molto raramente.
- **La Formula di Zipf:** L'$i$-esimo termine più frequente ha una frequenza proporzionale a $\frac{1}{i}$. In formule matematiche, $cf_{i}\propto \frac{1}{i}=\frac{K}{i}$, dove $K$ è una costante di normalizzazione e $cf_i$​ (collection frequency) rappresenta il numero totale di volte in cui il termine compare in tutta la collezione.
- **Le Conseguenze Pratiche:** Questo significa che se la parola in assoluto più frequente (ad esempio "the" in inglese) compare $cf_1$​ volte:
    - La seconda parola più frequente ("of") comparirà esattamente la metà delle volte ($\frac{cf_1​}{2}$).
    - La terza parola più frequente ("and") comparirà un terzo delle volte ($\frac{cf_1​}{3}$), e così via a scendere.
- **La Linearità Logaritmica:** Come per Heaps, se applichiamo i logaritmi otteniamo l'equazione $\log cf_i​=\log K-\log i$. Questo dimostra un'altra perfetta relazione lineare tra il logaritmo della frequenza e il logaritmo della posizione in classifica (rank), confermando che ci troviamo di fronte a un'altra "legge di potenza" (power law relationship).

Vediamo graficamente l'applicazione della Legge di Zipf sulla collezione Reuters, tracciando $\log_{10}​cf$ sull'asse verticale e log10​rank sull'asse orizzontale.
    
- La linea retta continua rappresenta la previsione teorica perfetta della legge.
- La linea spezzata rappresenta i dati reali della collezione. Come si può notare, la legge si modella molto bene sulla maggior parte del vocabolario, tendendo a divergere leggermente solo alle estremità assolute (la "coda" delle parole estremamente rare).

![center|400](img/Pasted%20image%2020260407153426.png)

## Transizione verso la compressione

Conoscendo la distribuzione statistica delle parole (sappiamo quanti vocaboli ci aspetteranno e con che frequenza si presenteranno), il sistema è finalmente pronto per la progettazione del software di compressione.

- **Il Prossimo Passo:** La lezione annuncia che si considereranno schemi per comprimere lo spazio fisico occupato sia dal dizionario che dalle liste di postings.
- **I Limiti (Scope):** Per semplificare l'apprendimento, verranno sviluppati algoritmi di compressione pensati esclusivamente per un indice booleano di base.
- Non verranno studiati nel dettaglio algoritmi per la compressione di indici posizionali, sebbene la slide specifichi che queste idee fondanti possono essere estese anche ad architetture più complesse.

---
# Compressione dei dizionari

Perchè ci preoccupiamo tanto delle dimensioni di questa specifica parte dell'indice.

- **Il punto di partenza:** Ogni singola ricerca effettuata da un utente inizia inevitabilmente consultando il dizionario. Se non trovi la parola lì, la ricerca si ferma.
- **Il Sacro Graal della RAM:** Per garantire risposte fulminee, **vogliamo tenere l'intero dizionario in memoria principale (RAM)**, evitando i lenti accessi al disco fisso.
- **La competizione:** La memoria RAM è una risorsa condivisa. L'indice del motore di ricerca compete costantemente (Memory footprint competition) con il sistema operativo e altre applicazioni in esecuzione sul server.
- **Il problema dei dispositivi piccoli:** Questo problema è ancora più acuto se pensiamo a motori di ricerca integrati su dispositivi embedded o mobili, dove la memoria disponibile è drasticamente inferiore rispetto a un server farm.
- **Velocità di avvio:** Anche ammettendo di non poter tenere tutto in RAM, avere un dizionario di dimensioni ridotte garantisce un tempo di avvio (startup time) del sistema di ricerca molto più veloce, poiché trasferire i dati dal disco alla memoria richiede meno tempo.
## Versione Naive

Come salveremmo il dizionario se non conoscessimo le tecniche di compressione? vediamo la "naïve version" (versione ingenua).

Il metodo standard nei linguaggi di programmazione (come il C) è usare un **array di voci a larghezza fissa (fixed-width entries)**. Questo significa assegnare a priori un blocco di memoria della stessa esatta dimensione per ogni singola parola.

Guardiamo la struttura della tabella per ogni termine:

1. **Terms:** Si assegnano 20 byte (caratteri) per memorizzare la stringa della parola.
2. **Freq.:** Si assegnano 4 byte per memorizzare un numero intero che rappresenta la frequenza della parola nei documenti.
3. **Postings ptr.:** Si assegnano 4 byte per il "puntatore", ovvero l'indirizzo di memoria che indica dove inizia la vera e propria lista di documenti (i postings) per quella parola.

**Il calcolo del peso:** Ogni voce (riga) della tabella occupa $20+4+4=28$ byte. Se prendiamo i $\approx400.000$ termini stimati per la collezione RCV1 e li moltiplichiamo per 28 byte, otteniamo un dizionario di **11.2 MB**. _Nota:_ 11.2 MB sembra poco oggi, ma ricordiamo che RCV1 è un set di dati minuscolo rispetto all'intero Web.

![center|500](img/Pasted%20image%2020260410103616.png)

L'approccio ingenuo ha due difetti fatali: è incredibilmente sprecone ed è anche troppo rigido.

- **Lo spreco per le parole corte:** Abbiamo bloccato 20 byte per ogni parola. Cosa succede quando dobbiamo salvare la parola "a" (o l'articolo italiano "il")? Usiamo 1 byte per la lettera e lasciamo 19 byte completamente vuoti e sprecati. La stragrande maggioranza dei byte nella colonna _Term_ viene sprecata in questo modo.
- **Il blocco per le parole lunghe:** Peggio ancora, cosa succede se incontriamo parole estremamente lunghe, come termini chimici o medici (es. _hydrochlorofluorocarbons_, 24 lettere)? L'array rigido a 20 byte semplicemente "taglierebbe" la parola, creando errori o corrompendo la memoria.

**La statistica contro l'intuizione:** Sapendo che l'inglese scritto ha in media $\approx4.5$ caratteri per parola, perché non usiamo questo numero per stimare la dimensione del dizionario?

La risposta sta nel principio visto in precedenza: le parole molto corte (i _token_, le occorrenze) dominano il conteggio nei testi perché si ripetono milioni di volte, ma **non dominano la media nel vocabolario (i _type_)**. Nel dizionario (dove ogni parola appare una sola volta, che sia "il" o "precipitevolissimevolmente"), la lunghezza media di una parola inglese si alza a $\approx$**8 caratteri**.

La vera sfida tecnica diventa quindi: come facciamo ad abbandonare i blocchi rigidi da 20 byte e allocare invece una media di $\approx8$ caratteri per termine nel nostro dizionario, risparmiando così un'enorme quantità di memoria?

Questo apre la strada alle vere tecniche di compressione, come il salvataggio del "Dictionary-as-a-string".
## Dictionary-as-a-String (DAAS)

L'idea alla base è drastica: invece di assegnare una "scatola" di dimensioni fisse a ogni parola, **memorizziamo l'intero dizionario come un'unica, gigantesca stringa continua di caratteri**.

- Tutte le parole vengono concatenate senza spazi: `...systilesyzygeticsyzygialsyzygy...`.
- Ma come facciamo a sapere dove finisce una parola e dove inizia la successiva? Semplice: il puntatore ("Term ptr.") nella tabella principale indica l'inizio della parola corrente, e **il puntatore della parola successiva ci indica la fine della parola corrente**.

![center|500](img/Pasted%20image%2020260410104307.png)

**La Matematica del Risparmio**

- **La Stringa:** Sapendo che ci sono $\approx400.000$ termini e che la lunghezza media di un termine nel dizionario è di $8$ byte, la lunghezza totale di questa mega-stringa sarà $400.000\times8 \text{ byte}=3.2 \text{ MB}$
- **I Puntatori:** Dobbiamo essere in grado di puntare a qualsiasi dei $3.2$ milioni di posizioni (byte) all'interno di questa stringa. Per indirizzare $3.2$ milioni di posizioni, ci servono $\log_2​(3.2\space M)\approx22$ bit. Poiché lavoriamo in byte, arrotondiamo a **$3$ byte per ogni puntatore**.

Se ricalcoliamo lo spazio totale per singolo termine con questo nuovo metodo:

- Frequenza: 4 byte
- Puntatore ai postings: 4 byte
- Puntatore al termine (nella stringa): **3 byte**
- Caratteri della parola (nella stringa): $\approx$**8 byte in media**
- **Totale:** $\approx19$ byte per termine in media (invece dei 28 byte del metodo ingenuo).

**Risultato DAAS:** Il dizionario passa da 11.2 MB a **7.6 MB**. Un risparmio enorme! Ma possiamo fare di meglio.
### L'Evoluzione: Blocking

Se guardiamo la tabella DAAS, notiamo che stiamo sprecando ancora spazio: stiamo salvando un puntatore da 3 byte per _ogni singola parola_! 
Per ovviare a questo "problema" si è introdotta la tecnica **Blocking** (raggruppamento in blocchi).

- **L'intuizione:** Perché salvare il puntatore per ogni parola? Raggruppiamo le parole in blocchi di dimensione $k$ e salviamo **solo il puntatore della prima parola del blocco**.
- **Il trucco delle lunghezze:** Se non abbiamo più i puntatori per le parole successive, come le dividiamo? Dobbiamo inserire all'interno della stringa stessa, subito prima della parola, un numero che ne indica la lunghezza. Questo numero costa **$1$ byte extra** per ogni parola. La stringa diventa: `...7systile9syzygetic8syzygial...`.

**Calcolo dei Guadagni Netti (Blocking Net Gains):** Facciamo l'esempio con blocchi da $k=4$ (raggruppiamo le parole a 4 a 4).

- **Senza Blocking (DAAS puro):** Per 4 parole ci servivano 4 puntatori. $4\times3 \text{ byte}=12 \text{ byte}$.
- **Con Blocking ($k=4$):** Per 4 parole usiamo 1 solo puntatore (3 byte) e dobbiamo aggiungere 4 "lunghezze" extra (4 parole $\times$ 1 byte = 4 byte). Totale: $3+4=7$ byte.
- **Risparmio:** $12-7=5$ byte salvati ogni blocco da 4 parole. In pratica, risparmiamo $1.25$ byte per termine.

Su 400.000 termini, questo ci fa risparmiare un altro mezzo Megabyte ($\approx0.5$ MB), riducendo la dimensione finale del dizionario a **7.1 MB**.

La Domanda Finale: **Perché non aumentare** $k$?

Se aumentare il parametro $k$ (es. $k=8$ o $k=16$) ci fa risparmiare sempre più memoria togliendo puntatori, perché non fare blocchi giganti?

La risposta è il classico compromesso tra spazio e tempo! Quando cerchi una parola in un blocco, il sistema non ha il puntatore diretto: deve saltare al primo termine del blocco, leggere la prima lunghezza (es. 7), leggere la prima parola, se non è quella giusta saltare avanti di 7 byte, leggere la lunghezza successiva, e così via scorrendo la stringa linearmente. **Più grande è $k$, più lenta sarà la ricerca a runtime.**
#### Ricerca nel dizionario con/senza Blocking

Per cercare una parola nel dizionario, il motore usa una struttura dati chiamata **albero binario (binary search tree)**. Vediamo la differenza di prestazioni.

- **Ricerca SENZA Blocking:** In un albero normale (dove $k=1$, cioè ogni parola ha il suo puntatore), ogni nodo punta direttamente a una parola. Se cerchiamo, ad esempio, "AID", il percorso è: `JOB -> DEN -> BOX -> AID`. Assumendo (irrealisticamente) che ogni termine sia cercato con la stessa probabilità, per calcolare il numero medio di confronti da fare in questo specifico albero a 8 nodi, si fa la media ponderata delle profondità: $\frac{(1+2\cdot 2+4\cdot 3+4)}{8}\approx2.6$ **confronti in media**.
- **Ricerca CON Blocking:** Se raggruppiamo le parole in blocchi da 4 ($k=4$), l'albero binario non punta più alle singole parole, ma _solo al primo elemento del blocco_. Il percorso diventa in due fasi:
    
    1. **Binary Search:** Naviga l'albero per trovare il blocco corretto (es. il blocco che inizia con "AID").
    2. **Linear Search:** Una volta dentro il blocco, deve scorrere le parole una a una (leggendo la lunghezza, poi la parola) finché non trova quella giusta. In questo scenario con $k=4$, la formula per la media dei confronti diventa $\frac{(1+2\cdot 2+2\cdot 3+2\cdot 4+5)}{8}=3$ **confronti in media**.

**Il Bilancio:** Raggruppare a 4 a 4 ci ha fatto risparmiare 0.5 MB di RAM, pagando il prezzo di un lievissimo rallentamento (da 2.6 a 3 confronti medi).

**Esempio Albero senza Blocking**

![center|300](img/Pasted%20image%2020260410105445.png)

**Esempio Albero con Blocking**

![center|500](img/Pasted%20image%2020260410105517.png)
## Tecnica del Front-Coding

C'è un'ultima osservazione brillante da fare. Il nostro dizionario è ordinato alfabeticamente. 
Questo significa che parole consecutive spesso condividono le stesse lettere iniziali. Perché ripetere "automat" quattro volte di fila?

La tecnica del **Front-coding** sfrutta questa ridondanza.

- **L'intuizione:** Poiché le parole ordinate hanno spesso un lungo prefisso in comune, memorizziamo il prefisso una volta sola e per le parole successive salviamo _solo le differenze_ (i suffissi).

**Come funziona (L'esempio visivo):** Prendiamo il blocco di parole consecutive: `automata, automate, automatic, automation`. Senza front-coding, la stringa sarebbe (con le lunghezze in rosso): `8automata8automate9automatic10automation`

![center|500](img/Pasted%20image%2020260410105736.png)

Con il front-coding, la stringa si trasforma magicamente in: `8automat*a1⋄e2⋄ic3⋄ion`

**Decodifica della nuova stringa:**

- `8automat*` -> Dichiara che il prefisso comune per questo blocco è lungo 8 caratteri ed è "automat". L'asterisco segna la fine del prefisso comune.
- `a` -> La prima parola è il prefisso + "a" (automata).
- `1⋄e` -> L'uno indica la lunghezza del suffisso ("e" è lungo 1). Il simbolo ⋄ (rombo) è un separatore speciale. Quindi la seconda parola è il prefisso + "e" (automate).
- `2⋄ic` -> Il suffisso è lungo 2. Parola: prefisso + "ic" (automatic).
- `3⋄ion` -> Il suffisso è lungo 3. Parola: prefisso + "ion" (automation).

Con l'aggiunta del Front-coding al nostro Dictionary-as-a-string con Blocking, la nostra tecnica inizia ad assomigliare a veri e propri algoritmi di compressione stringhe general-purpose

Per riassumere, possiamo definire la seguente tabella


| Tecnica                            | Dimensione in MB |
| ---------------------------------- | ---------------- |
| Larghezza fissata                  | 11.2             |
| DAAS con puntatore ad ogni termine | 7.6              |
| + Blocking, es. k=4                | 7.1              |
| + Blocking + Front-Coding          | 5.9              |

---
# Compressione dei postings
## Gamma Code
## Variabile Byte (VB) codes