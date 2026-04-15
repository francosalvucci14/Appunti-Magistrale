Grafi Temporali

Mix fra grafi temporali e big data

Problematica: Clustering Temporale

Idea tesi: ricerca bibliografica su questo argomento (prima parte) - partire da paper di Straziota

Studiare paper, capire contesto, problema specifico e risultati e related work

Capire se esistono altri paper che si collegano a questo, altri lavori simili

---
# Analisi Avanzata della Rilevazione di Comunità Stabili in Reti Temporali tramite Clustering Basato sulla Densità Strutturale

L'evoluzione della scienza delle reti ha portato alla consapevolezza che le strutture sociali, biologiche e tecnologiche non sono entità statiche, ma sistemi dinamici le cui interazioni fluttuano nel tempo. Il problema della rilevazione di comunità, tradizionalmente affrontato su grafi statici, richiede oggi un cambio di paradigma verso i grafi temporali, dove ogni arco è marcato da un timestamp che ne definisce l'istante o l'intervallo di esistenza. Un approccio particolarmente promettente, analizzato nel dettaglio in questa sede, riguarda l'identificazione di comunità stabili, ovvero gruppi di nodi che non solo mostrano una densità di connessione elevata, ma mantengono questa coesione strutturale in modo persistente lungo la dimensione temporale.

## Inquadramento Teorico e Motivazioni della Ricerca

Le reti reali, come quelle di contatti umani, collaborazioni scientifiche o comunicazioni digitali, sono intrinsecamente temporali. In una rete di contatti, un arco $(u, v, t)$ rappresenta un'interazione tra due individui in un momento specifico; in una rete di co-autoria, denota la pubblicazione congiunta di un articolo in un dato anno. Gran parte degli algoritmi di rilevazione di comunità esistenti ignora queste informazioni temporali, aggregando i dati in un unico grafo statico. Questa semplificazione comporta la perdita di pattern critici, poiché interazioni avvenute in tempi distanti vengono trattate come simultanee, portando alla formazione di comunità "artificiali" che non riflettono la realtà operativa del sistema.

La ricerca di comunità stabili si differenzia nettamente dalla ricerca di comunità dinamiche o evolutive. Mentre queste ultime si concentrano su come i gruppi cambiano, si fondono o si dividono, la stabilità mira a isolare il nucleo invariante della rete. Ad esempio, in una rete di email universitarie, una comunità stabile può rivelare l'appartenenza allo stesso dipartimento, dove la comunicazione è costante e strutturata, distinguendola da gruppi di lavoro temporanei formati per progetti a breve termine. Allo stesso modo, nelle reti di collaborazione scientifica, identificare un team di esperti che collabora stabilmente da anni è fondamentale per assemblare gruppi di ricerca affidabili per progetti complessi.

Le tecniche tradizionali di clustering basate sulla densità, come SCAN (Structural Clustering Algorithm for Networks), hanno dimostrato grande efficacia nel gestire grafi di grandi dimensioni, grazie alla capacità di distinguere tra nodi core, hub e outlier. Tuttavia, l'estensione di SCAN al dominio temporale presenta sfide computazionali non banali. La definizione di "stabilità" richiede infatti che la somiglianza strutturale tra i nodi sia verificata non solo in modo aggregato, ma in una serie di snapshot temporali, introducendo una complessità legata al mining di pattern frequenti che cresce esponenzialmente con il numero di timestamp considerati.

## Fondamenti Matematici e Definizioni di Stabilità

Per formalizzare il problema, il grafo temporale $\mathcal{G}=(\mathcal{V},\mathcal{E})$ viene suddiviso in una sequenza di snapshot $\{G_1, G_2,..., G_T\}$, dove ogni $G_i=(V, E_i)$ rappresenta lo stato della rete nell'intervallo temporale $i$-esimo. La base del clustering strutturale risiede nella misura della similarità tra nodi adiacenti, calcolata tramite la sovrapposizione dei loro vicinati.

### Similarità Strutturale e Stabilità Temporale

In uno snapshot specifico $G_i$, la similarità strutturale $\sigma_i(u,v)$ tra due nodi $u$ e $v$ è definita dalla frazione di vicini comuni rispetto alla media geometrica delle dimensioni dei loro vicinati inclusivi :

$$\sigma_{i}(u,v) \triangleq \frac{|N_{i}[u]\cap N_{i}[v]|}{\sqrt{|N_{i}[u]|\times|N_{i}[v]|}}$$

dove $N_i[u] = N_i(u) \cup \{u\}$. Se l'arco $(u,v)$ non esiste nello snapshot $i$, la similarità è posta a zero. Partendo da questa misura puntuale, viene introdotta la $\epsilon$-stable similarity ($S_\epsilon(u,v)$), che conta il numero di snapshot in cui la somiglianza strutturale supera una soglia definita $\epsilon$ :

$$S_{\epsilon}(u,v) = \sum_{i=1}^{T} \mathcal{I}(\sigma_{i}(u,v) \ge \epsilon)$$

dove $\mathcal{I}$ è la funzione indicatrice. Un arco è considerato $(\tau, \epsilon)$-connesso se $S_\epsilon(u,v) \ge \tau$, dove $\tau$ rappresenta la soglia minima di stabilità temporale.

### Definizione del $(\mu, \tau, \epsilon)$-Stable Core

Il concetto cardine dell'algoritmo è lo stable core, che identifica i nodi "nucleo" attorno ai quali si sviluppano i cluster. Un nodo $u$ è definito $(\mu, \tau, \epsilon)$-stable core se possiede un insieme di almeno $\mu$ vicini che sono simultaneamente simili a $u$ in almeno $\tau$ snapshot. Formalmente, deve esistere un sottoinsieme $\tilde{N}(u) \subseteq N(u)$ tale che $|\tilde{N}(u)| \ge \mu$ e che esista un insieme di snapshot $\{G_{j_1},..., G_{j_l}\}$ con $l \ge \tau$ in cui, per ogni snapshot $G_{j_k}$ e per ogni $v \in \tilde{N}(u)$, si abbia $\sigma_{j_k}(u,v) \ge \epsilon$.

Questa definizione impone un vincolo di simultaneità molto forte: non è sufficiente che ogni vicino sia stabile singolarmente; è necessario che un intero gruppo di vicini sia strutturalmente simile al core negli stessi istanti temporali. Questo garantisce che la comunità identificata abbia una coesione interna che persiste come unità funzionale nel tempo.

|**Simbolo**|**Definizione**|**Significato Algoritmico**|
|---|---|---|
|$\mathcal{G}=(\mathcal{V},\mathcal{E})$|Grafo temporale|Insieme di nodi e archi associati a timestamp.|
|$G_i=(V, E_i)$|Snapshot $i$-esimo|Grafo statico derivato da un intervallo temporale.|
|$\sigma_i(u,v)$|Similarità strutturale|Grado di vicinanza locale nello snapshot $i$.|
|$S_\epsilon(u,v)$|$\epsilon$-stable similarity|Frequenza temporale della somiglianza $\ge \epsilon$.|
|$\mu$|Parametro di densità|Numero minimo di vicini simili richiesti.|
|$\tau$|Parametro di stabilità|Numero minimo di snapshot richiesti.|
|$\epsilon$|Soglia di similarità|Valore minimo di $\sigma$ per considerare due nodi simili.|

## Architettura dell'Algoritmo TSCAN-B

Il framework algoritmico di base, denominato TSCAN-B (Temporal SCAN-Basic), adatta il processo di clustering di PSCAN alle reti temporali. Il processo si suddivide in due fasi principali: l'identificazione e il raggruppamento dei nodi core, e la successiva assegnazione dei nodi non-core.

### Identificazione dei Core e Clustering

Inizialmente, l'algoritmo attraversa ogni nodo $u \in V$ per determinare se soddisfa i requisiti di stable core. Data la complessità della definizione di core, l'approccio di base prevede l'utilizzo di algoritmi di frequent pattern mining massimale, come Apriori, trattando l'insieme dei vicini $\epsilon$-simili in ogni snapshot come una transazione. Se esiste un pattern frequente con supporto $\ge \tau$ e cardinalità $\ge \mu$, il nodo è marcato come core.

Una volta identificati i core, l'algoritmo costruisce un grafo delle comunità $G_c$:

1. Se un nodo $u$ è un core, viene aggiunto a $G_c$.
    
2. Per ogni vicino $v$ di $u$ nel grafo aggregato, se l'arco $(u,v)$ è $(\tau, \epsilon)$-connesso e anche $v$ è un core, viene aggiunto un arco tra $u$ e $v$ in $G_c$.
    
3. I componenti connessi di $G_c$ formano i nuclei delle comunità stabili.
    

### Assegnazione dei Nodi Periferici

Il modello segue la filosofia SCAN nel non forzare ogni nodo all'interno di un cluster. I nodi che non sono core, ma sono $(\tau, \epsilon)$-connessi ad almeno un nodo core, vengono assegnati alla comunità di quel core. Se un nodo non-core è connesso a più comunità, esso assume il ruolo di hub; se non è connesso a nessuna, viene classificato come outlier o rumore. Questo approccio permette di identificare strutture di comunità naturali, preservando la capacità di isolare elementi marginali della rete che potrebbero distorcere l'analisi della stabilità.

## Ottimizzazioni e Tecniche di Pruning: L'Algoritmo TSCAN-A

Il limite principale di TSCAN-B risiede nel costo computazionale del mining dei pattern frequenti per ogni nodo, un'operazione che può richiedere $O(C_{\mathcal{T}}^{\tau})$ tempo. Per gestire grafi con milioni di nodi e archi, è stato sviluppato l'algoritmo TSCAN-A, che introduce tecniche di potatura (pruning) basate su modelli core rilassati: il Weak Core e il Strong Core.

### Il Modello Weak Core

Il Weak Core Pruning si basa sull'osservazione che un nodo stable core deve necessariamente avere almeno $\mu$ vicini che siano individualmente stabili. Un nodo $u$ è definito Weak Core se $|N_{(\tau,\epsilon)}(u)| \ge \mu$. Questa condizione è molto più semplice da verificare rispetto alla definizione di stable core, poiché richiede solo il calcolo delle somiglianze individuali $S_\epsilon(u,v)$ lungo il tempo.

L'algoritmo WeakCore utilizza un approccio basato su limiti (bounds) per evitare calcoli superflui. Per ogni nodo $u$, viene mantenuto un contatore $cd(u)$ dei vicini stabili confermati e un limite superiore $\overline{cd}(u)$ dei potenziali vicini stabili. Inizialmente, $\overline{cd}(u)$ è pari al grado del nodo nel grafo aggregato. Se $\overline{cd}(u) < \mu$, il nodo $u$ viene scartato immediatamente, poiché non potrà mai diventare un core. Questo permette di ridurre drasticamente il numero di nodi candidati, specialmente in grafi sparsi dove molti nodi hanno gradi ridotti o interazioni temporali scarse.

### Il Modello Strong Core

Per raffinare ulteriormente la ricerca, viene introdotto il Strong Core Pruning. Un nodo $u$ è definito Strong Core se è un Weak Core e se esistono almeno $\tau$ snapshot in cui il numero di vicini strutturalmente simili (anche se diversi in ogni snapshot) è almeno $\mu$. Il Lemma 2 della ricerca dimostra che ogni $(\mu, \tau, \epsilon)$-stable core è necessariamente un Strong Core.

L'algoritmo StrongCore verifica se $\sum_{i=1}^{\mathcal{T}} \mathcal{I}(|N_i^\epsilon(u)| \ge \mu) \ge \tau$. Anche in questo caso, vengono utilizzati bound inferiori e superiori per terminare anticipatamente il calcolo negli snapshot che non contribuiscono alla soglia $\tau$. Questa fase elimina i nodi che, pur avendo vicini stabili individualmente, non presentano una densità di vicinato sufficiente in un numero adeguato di snapshot.

| **Livello di Pruning** | **Condizione Matematica**             | **Risultato**                                            |
| ---------------------- | ------------------------------------- | -------------------------------------------------------- |
| **Filtro Grado**       | $d(u) < \mu$                          | Eliminazione immediata dei nodi a bassa connettività.    |
| **Weak Core**          | $                                     | N_{(\tau,\epsilon)}(u)                                   |
| **Strong Core**        | Snapshots densi $< \tau$              | Eliminazione di nodi senza ricorrenza di densità locale. |
| **Stable Core**        | Pattern frequente simultaneo $< \tau$ | Identificazione esatta tramite mining (Apriori).         |

## Analisi della Complessità e Scalabilità

L'efficienza di TSCAN-A deriva dalla sua capacità di ridurre il grafo a un numero limitato di Strong Cores prima di eseguire la parte più onerosa dell'algoritmo. Nel caso peggiore, la complessità del mining frequente è elevata, ma nella pratica, il numero di Strong Cores ($s$) è tipicamente inferiore al 2% della popolazione totale dei nodi in reti reali come DBLP.

La complessità temporale di TSCAN-A può essere espressa come $O(m'm + |s| C_T^\tau |s|^\tau)$, dove $m'$ è il numero di archi nel grafo aggregato e $m$ il numero di archi temporali. Il termine $m'm$ deriva dal calcolo della similarità strutturale, che viene ottimizzato tramite caching per evitare ricalcoli. Grazie alle tecniche di potatura, l'algoritmo riesce a processare il dataset DBLP (1,7 milioni di nodi) in circa 100 secondi, un tempo significativamente inferiore rispetto a TSCAN-B, che risulta spesso intrattabile su tali scale.

Dal punto di vista della memoria, TSCAN-A mantiene i punteggi di similarità calcolati, con un overhead spaziale che scala linearmente con il numero di archi del grafo aggregato. Gli esperimenti indicano che per DBLP sono necessari circa 678 MB di memoria per memorizzare questi punteggi, rendendo l'approccio applicabile su comuni server di calcolo.

## Risultati Sperimentali e Metriche di Qualità

La validazione dell'algoritmo è stata condotta su quattro dataset eterogenei: Chess, Lkml, Enron e DBLP, confrontando TSCAN-A con diverse baseline, tra cui PSCAN-W (una versione pesata di PSCAN che aggrega i timestamp come pesi degli archi) e TSCAN-S (una variante che utilizza i Strong Cores per il clustering).

### Metriche Temporali di Buona Formazione

Per valutare la qualità delle comunità stabili, sono state adattate quattro metriche classiche della scienza delle reti alla dimensione temporale :

1. **Average Separability (AS):** Misura quanto le comunità sono isolate dal resto della rete. Un valore AS elevato indica che ci sono molti più archi temporali interni rispetto a quelli verso l'esterno.
    
2. **Average Density (AD):** Quantifica la frazione di archi temporali esistenti tra i nodi della comunità rispetto al massimo teorico.
    
3. **Average Cohesiveness (AC):** Basata sulla conduttanza, indica quanto sia difficile dividere internamente una comunità mantenendo archi temporali coerenti.
    
4. **Average Clustering Coefficient (ACC):** Riflette la tendenza dei nodi all'interno della comunità a formare triangoli strutturalmente simili nel tempo.
    

### Analisi Comparativa delle Performance

I risultati mostrano che TSCAN-A supera costantemente PSCAN-W in tutte le metriche di qualità. PSCAN-W, basandosi su pesi aggregati, tende a fondere comunità che sono dense in tempi diversi ma mai simultaneamente, portando a valori di separabilità e coesione inferiori. TSCAN-A, al contrario, identifica cluster che mantengono una fedeltà strutturale elevata lungo gli snapshot.

|**Dataset**|**Metric**|**PSCAN-W**|**TSCAN-S**|**TSCAN-A**|
|---|---|---|---|---|
|**DBLP**|AS (norm)|0.22|0.81|1.00|
|**DBLP**|AD (norm)|0.45|0.92|1.00|
|**DBLP**|AC (norm)|0.61|0.88|1.00|
|**DBLP**|ACC (norm)|0.38|0.85|1.00|

L'analisi dell'efficienza evidenzia che, sebbene PSCAN-W sia più veloce (poiché opera su un grafo pesato statico), la sua incapacità di catturare la stabilità lo rende inefficace per le applicazioni target. TSCAN-A offre il miglior compromesso tra rigore teorico (identificazione degli stable core esatti) e velocità operativa grazie al pruning.

## Studio di Caso e Applicazioni Pratiche

Un'analisi qualitativa sul dataset DBLP ha permesso di esaminare la comunità stabile del ricercatore Qiang Yang. Mentre PSCAN-W restituisce una comunità "rumorosa" che include centinaia di co-autori occasionali accumulati in trent'anni, TSCAN-A isola un nucleo ristretto di collaboratori storici. Questi membri, identificati attraverso l'analisi manuale delle loro biografie, risultano essere i suoi ex studenti di dottorato e partner di ricerca a lungo termine presso Microsoft Research Asia.

Questo risultato evidenzia la capacità dell'algoritmo di operare una distinzione fondamentale tra contatti superficiali (molti, ma brevi) e legami strutturali (stabili e persistenti). In termini di algoritmi, questo si traduce nella capacità di filtrare il rumore temporale che affligge le rappresentazioni statiche delle reti.

## Discussione delle Implicazioni Algoritmiche

L'approccio basato sulla densità strutturale offre vantaggi unici rispetto ad altri modelli temporali come i "bursting cores". Mentre la ricerca di burst è focalizzata sull'identificazione di eventi improvvisi e densi (come una discussione virale su Twitter o un'emergenza in una rete di comunicazione), il mining di comunità stabili cerca la struttura "ossatura" del grafo.

### Confronto con Modelli di Bursting

Un modello di bursting (es. $(l, \delta)$-maximal bursting core) richiede che un nodo abbia un grado medio elevato in un segmento temporale di lunghezza $l$. TSCAN-A, invece, non richiede necessariamente un'intensità esplosiva, ma una persistenza strutturale. In molti scenari reali, una comunità stabile può non essere mai la più "densa" in termini assoluti in un singolo istante, ma è l'unica che sopravvive alla scomposizione per snapshot senza perdere la propria configurazione di vicinato.

### Relazione con il Problema dell'Identità

Nelle reti dinamiche, un problema classico è l'Identity Problem: determinare se il cluster $C_t$ è lo stesso di $C_{t+1}$. TSCAN-A aggira intrinsecamente questo problema definendo la comunità sulla base di un'unica de-temporalizzazione guidata da vincoli di stabilità. Non c'è bisogno di tracciare l'evoluzione perché la definizione stessa di $(\mu, \tau, \epsilon)$-stable cluster garantisce che i membri appartengano a una struttura che è rimasta valida per almeno $\tau$ istanti. Questo riduce drasticamente la complessità logica necessaria per l'analisi post-clustering.

## Considerazioni Finali e Conclusioni

La ricerca presentata nel paper di Qin et al. stabilisce un nuovo punto di riferimento per l'analisi delle reti temporali, dimostrando che il clustering basato sulla densità strutturale può essere scalato efficacemente oltre i grafi statici. La chiave del successo di TSCAN-A risiede nell'integrazione sinergica tra la teoria dei grafi e le tecniche di mining di pattern, mediata da strategie di pruning che sfruttano le proprietà matematiche dei core nodali.

L'algoritmo proposto non solo garantisce una qualità superiore delle comunità identificate, ma offre anche una robustezza eccezionale contro il rumore temporale e la marginalità dei nodi outlier, un limite noto dei metodi basati sulla modularità. Per un corso avanzato di Algoritmi, TSCAN-A rappresenta un eccellente esempio di come la scomposizione di un problema complesso in bound rilassati (Weak e Strong) possa trasformare un compito combinatorio intrattabile in un'operazione quasi-lineare in contesti di big data reali.

Le future direzioni di ricerca potrebbero includere l'estensione di questo modello a grafi orientati e pesati, nonché l'integrazione di attributi dei nodi per raffinare ulteriormente la definizione di somiglianza, passando da una stabilità puramente strutturale a una stabilità tematica o semantica. La capacità di identificare l'invariante temporale rimane, tuttavia, il contributo più significativo per la comprensione della dinamica dei sistemi complessi.