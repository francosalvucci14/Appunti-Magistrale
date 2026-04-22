Grafi Temporali

Mix fra grafi temporali e big data

Problematica: Clustering Temporale

Idea tesi: ricerca bibliografica su questo argomento (prima parte) - partire da paper di Straziota

Studiare paper, capire contesto, problema specifico e risultati e related work

Capire se esistono altri paper che si collegano a questo, altri lavori simili

---
# Analisi Avanzata della Stabilità Strutturale e Rilevazione di Comunità in Reti Temporali

L'analisi dei dati di rete ha subito una trasformazione fondamentale con l'avvento dei grafi temporali, in cui ogni arco non è più considerato un'entità statica ma è associato a un timestamp specifico o a un intervallo di tempo. Questa evoluzione rispecchia la natura intrinsecamente dinamica dei sistemi del mondo reale, come le reti di comunicazione via email, le collaborazioni scientifiche e le interazioni sociali tra individui. La rilevazione di comunità in questi contesti non può limitarsi all'analisi della densità topologica istantanea, ma deve affrontare la sfida della stabilità temporale, distinguendo tra strutture coese persistenti e fluttuazioni transitorie nei flussi di dati.

## Evoluzione della Network Analysis: dai Grafi Statici ai Grafi Temporali

Storicamente, la ricerca sulla rilevazione di comunità si è concentrata su grafi statici, definendo le comunità come gruppi di nodi con una densità di connessione interna superiore rispetto a quella esterna. Algoritmi classici basati sull'ottimizzazione della modularità, come il metodo di Louvain, o sulla ricerca di sottografi densi (clique e quasi-clique), hanno dominato la letteratura per decenni. Tuttavia, questi modelli ignorano l'informazione temporale, fallendo nell'identificare pattern cruciali come la stabilità a lungo termine delle relazioni.

Nelle reti temporali, rappresentate formalmente come un insieme di nodi $\mathcal{V}$ e un insieme di archi temporali $\mathcal{E}$ composti da triplette $(u, v, t)$, l'obiettivo si sposta verso l'identificazione di strutture che mantengono la loro coesione strutturale attraverso il tempo. Un grafo temporale può essere visualizzato come un flusso di collegamenti (link stream) o come una sequenza di snapshot discreti $\mathcal{G}_1, \mathcal{G}_2, \dots, \mathcal{G}_T$, dove ogni snapshot cattura lo stato della rete in un determinato intervallo temporale. Questa distinzione è fondamentale per la scelta dell'approccio algoritmico: i modelli basati su snapshot permettono l'estensione di teorie statiche, mentre i modelli di link stream facilitano l'aggiornamento incrementale in tempo reale.

## Il Modello TSCAN: Clustering basato sulla Densità nelle Reti Temporali

Una delle innovazioni più significative per affrontare la stabilità temporale è il framework TSCAN (Temporal Structural Clustering Algorithm for Networks), proposto per estendere l'algoritmo SCAN ai contesti dinamici. Il cuore di questo approccio risiede nella misura della similarità strutturale tra i nodi, non più limitata a un singolo istante ma valutata sulla sua persistenza.

### Fondamenti Matematici della Stabilità Strutturale

TSCAN introduce il concetto di $\epsilon$-stable similarity, denotata come $S_{\epsilon}(u, v)$, che quantifica il numero di snapshot in cui la similarità strutturale $\sigma_i(u, v)$ tra due nodi supera una soglia $\epsilon$. La similarità strutturale nello snapshot $i$ è definita come:

$$\sigma_i(u, v) = \frac{|N_i[u] \cap N_i[v]|}{\sqrt{|N_i[u]| \times |N_i[v]|}}$$

dove $N_i[u]$ rappresenta il vicinato chiuso del nodo $u$ nello snapshot $i$. Se $S_{\epsilon}(u, v) \ge \tau$, l'arco $(u, v)$ è considerato $(\tau, \epsilon)$-connected, indicando una relazione strutturalmente significativa per almeno $\tau$ istanti temporali. Questo parametro $\tau$ agisce come un filtro di stabilità, permettendo di ignorare contatti casuali o di breve durata che non riflettono una vera appartenenza a una comunità.

### Definizione di $(\mu, \tau, \epsilon)$-Stable Core

Un nodo $u$ è definito come un $(\mu, \tau, \epsilon)$-stable core se possiede almeno $\mu$ vicini con i quali forma una struttura a stella persistente per almeno $\tau$ snapshot. Questa definizione è più rigorosa rispetto ai modelli statici poiché richiede che la similarità strutturale sia soddisfatta simultaneamente per un gruppo di vicini, catturando l'essenza di un "nucleo" stabile all'interno della rete.

La rilevazione di una comunità stabile avviene quindi attraverso la propagazione della raggiungibilità strutturale dai core stabili. Una comunità stabile soddisfa due proprietà fondamentali:

1. **Massimalità:** Se un nodo $u$ appartiene a una comunità stabile, tutti i nodi raggiungibili strutturalmente da $u$ devono essere inclusi.
    
2. **Connettività:** Qualsiasi coppia di nodi nella comunità deve essere collegata attraverso un percorso di core stabili.
    

### Simboli e Definizioni Chiave nel Clustering Temporale

|**Simbolo**|**Definizione**|**Applicazione**|
|---|---|---|
|$\mathcal{G}=(\mathcal{V}, \mathcal{E})$|Grafo temporale non orientato|Rappresentazione completa del dataset|
|$\sigma_i(u, v)$|Similarità strutturale nello snapshot $i$|Misura dell'overlap locale al tempo $t$|
|$S_{\epsilon}(u, v)$|$\epsilon$-stable similarity|Conteggio della persistenza della similarità|
|$(\mu, \tau, \epsilon)$-stable core|Nodo con $\mu$ vicini stabili per $\tau$ istanti|Backbone della comunità stabile|
|$\Delta$|Distanza temporale o finestra|Risoluzione temporale degli snapshot|
|$G = (V, E)$|Grafo de-temporalizzato statico|Vista aggregata per analisi di base|

## Categorizzazione del Related Work: Prospettive e Metodologie

L'analisi della letteratura specialistica permette di mappare le direzioni di ricerca in tre grandi categorie: probabilistiche, strutturali/topologiche e basate sulla densità. Ognuna di queste classi risponde a diverse esigenze di interpretabilità e scalabilità.

### Modelli Probabilistici e Statistici

I modelli probabilistici si basano spesso sul concetto di Stochastic Block Model (SBM), in cui i nodi sono assegnati a classi latenti e la probabilità di connessione tra due nodi dipende esclusivamente dalla loro appartenenza a tali classi. L'estensione dinamica, nota come Dynamic Stochastic Block Model (dSBM), è stata approfondita da Catherine Matias e Vincent Miele.

Il dSBM combina la struttura statica dell'SBM con catene di Markov indipendenti che governano l'evoluzione delle appartenenze dei nodi nel tempo. Questo approccio permette di modellare non solo la presenza di archi, ma anche la loro frequenza o il loro peso in reti pesate. Un aspetto critico del dSBM è il controllo del "label switching", ovvero il problema di mantenere l'identità dei cluster coerente tra snapshots successivi. L'inferenza viene solitamente effettuata tramite algoritmi di Variational Expectation-Maximization (VEM), che approssimano la distribuzione a posteriori delle variabili latenti per rendere il calcolo trattabile su reti di grandi dimensioni.

### Approcci Strutturali e Topologici

Questa categoria si focalizza sull'identificazione di sottografi che soddisfano vincoli topologici precisi, come $k$-core e $k$-truss, estendendoli alla dimensione temporale. In questo contesto, il lavoro di Huang e altri ha investigato la manutenzione di comunità $k$-truss in grafi dinamici, mentre Wu ha proposto modelli di decomposizione $k$-core temporale basati sul conteggio degli archi temporali.

Recentemente, il concetto di "comunità durevole" (durable community) è emerso come una variante del $k$-core temporale che identifica i sottografi più longevi in cui i membri rimangono invariati per un periodo continuo. Un'altra direzione rilevante riguarda la ricerca di "bursting cores", ovvero strutture dense che emergono con intensità in finestre temporali specifiche, rappresentando una forma di stabilità strutturale limitata a periodi di alta attività.

### Framework basati sulla Densità

Il framework basato sulla densità, esemplificato da SCAN e dalle sue evoluzioni (SCAN++, PSCAN), si distingue per la capacità di identificare non solo i cluster ma anche i ruoli periferici dei nodi, come hub e outlier. TSCAN appartiene a questa classe e introduce tecniche di potatura (pruning) per gestire l'elevata complessità computazionale derivante dall'analisi di molteplici snapshot.

Il vantaggio principale degli approcci basati sulla densità è la loro efficacia pratica nel separare il rumore dalle strutture reali. Mentre i modelli probabilistici possono essere influenzati da assunzioni sulla distribuzione dei dati, il clustering strutturale basato sulla densità si fonda sulla connettività locale osservata, risultando più robusto in presenza di dati eterogenei.

## Metodologie di Scomposizione Tensoriale e Non-Negative Tensor Factorization

Un approccio alternativo e potente per la rilevazione di comunità temporali è la scomposizione tensoriale, in particolare la Non-Negative Tensor Factorization (NTF). Questo metodo tratta la rete temporale come un tensore a tre vie $\mathcal{X} \in \mathbb{R}^{N \times N \times T}$, dove le dimensioni rappresentano i nodi, i vicini e il tempo.

### Il Modello di Gauvin et al.

L'approccio proposto da Gauvin e colleghi permette di identificare simultaneamente le comunità e di tracciare la loro attività nel tempo. Il tensore viene approssimato come una somma di componenti di rango uno:

$$\mathcal{X} \approx \sum_{r=1}^R a_r \circ b_r \circ c_r$$

In questa formulazione:

- I vettori $a_r$ e $b_r$ codificano l'appartenenza dei nodi alla comunità $r$.
    
- Il vettore $c_r$ descrive il profilo di attività temporale della comunità.
    

L'NTF è particolarmente utile per scoprire comunità che potrebbero essere sparse in un singolo istante ma che mostrano un'attività altamente correlata su periodi estesi. Ad esempio, nell'analisi dei contatti sociali in una scuola, questo metodo è in grado di recuperare con alta precisione la struttura delle classi e di rilevare comunità miste corrispondenti ad attività sociali negli spazi comuni. Inoltre, varianti come il modello Toffee utilizzano il prodotto tensoriale basato sulla convoluzione circolare (t-product) per catturare meglio le intercorrelazioni tra snapshots consecutivi.

### Confronto tra Metodologie Probabilistiche e Tensoriali

|**Caratteristica**|**Modelli dSBM**|**Scomposizione Tensoriale (NTF)**|
|---|---|---|
|**Natura del Modello**|Probabilistica / Generativa|Algebrica / Fattorizzazione|
|**Gestione Tempo**|Catene di Markov discrete|Dimensione tensoriale continua o discreta|
|**Output Principale**|Appartenenza alle classi latenti|Vettori di appartenenza e profili attività|
|**Punto di Forza**|Identificabilità statistica|Scoperta di pattern di attività correlati|
|**Sfida Principale**|Label switching e scalabilità|Scelta del rango $R$ e sparsità del tensore|

## Efficienza Computazionale e Tecniche di Potatura (Pruning)

La sfida tecnica principale nella rilevazione di comunità stabili è il costo computazionale. Determinare se un nodo è un $(\mu, \tau, \epsilon)$-stable core richiederebbe, ingenuamente, di eseguire algoritmi di mining di pattern frequenti su tutti gli snapshot, un compito proibitivo per grafi con milioni di nodi. Per superare questo ostacolo, sono state sviluppate tecniche di riduzione del grafo basate su core deboli e forti.

### Potatura tramite Weak Core e Strong Core

L'algoritmo TSCAN-A utilizza due livelli di filtraggio per ridurre il numero di candidati core :

1. **Weak Core Pruning:** Un nodo $u$ è un core debole se possiede almeno $\mu$ vicini $(\tau, \epsilon)$-connected nel grafo de-temporalizzato. Poiché ogni core stabile deve essere un core debole, tutti i nodi che non soddisfano questo requisito possono essere scartati immediatamente.
    
2. **Strong Core Pruning:** Un core forte è un core debole che soddisfa ulteriormente il vincolo di avere almeno $\mu$ vicini simili in almeno $\tau$ snapshot individuali, indipendentemente dalla simultaneità.
    

Questo processo di potatura è estremamente efficace. In dataset reali come DBLP, solo l'1,97% dei nodi viene identificato come core forte e solo lo 0,99% viene confermato come core stabile. Grazie a questa riduzione drastica, l'algoritmo può processare grafi di enormi dimensioni in tempi contenuti.

### Analisi delle Performance su Dataset Reali

I test condotti su quattro dataset (Chess, Lkml, Enron, DBLP) dimostrano la scalabilità degli approcci ottimizzati rispetto ai baseline.

|**Dataset**|**Nodi (n)**|**Archi Temporali (m)**|**Snapshot (T)**|**Tempo TSCAN-A (s)**|
|---|---|---|---|---|
|**Chess**|7.301|62.385|99|< 1|
|**Lkml**|26.885|328.092|96|~5|
|**Enron**|86.978|499.983|48|~10|
|**DBLP**|1.729.816|12.007.380|78|~100|

L'algoritmo TSCAN-A mantiene in memoria le similarità strutturali calcolate per evitare computazioni ridondanti, con un overhead di memoria che rimane proporzionale alla dimensione del grafo. Questo lo rende utilizzabile su macchine standard anche per reti di scala miliare.

## Evoluzioni Recenti e Nuove Frontiere (2023-2026)

La ricerca tra il 2023 e il 2026 ha introdotto concetti innovativi per affrontare l'instabilità intrinseca delle reti temporali, spesso causata dal rumore spettrale o da una campionatura non uniforme.

### Instabilità e "Hallucinations" nelle GNN Temporali

Un problema emergente riguarda le "allucinazioni" (hallucinations) nelle Graph Neural Networks (GNN) utilizzate per il clustering: queste reti possono produrre partizioni instabili o spurie a causa della sensibilità agli autovalori ad alta frequenza e al rumore. Per mitigare questo fenomeno, è stato proposto il framework F2-CommNet, che utilizza il calcolo di ordine frazionario (fractional-order calculus) per modellare effetti di "lunga memoria". Questo approccio permette di bilanciare la reattività del modello ai cambiamenti topologici rapidi con una stabilità globale, riducendo gli indici di allucinazione fino al 35% e aumentando il margine di stabilità $\rho$ di oltre tre volte.

### Higher-Order Edge Enhancement (HOEE)

Un'altra direzione critica riguarda la perdita di strutture di ordine superiore (come i motivi a triangolo chiuso) durante la segmentazione del grafo in snapshot. L'algoritmo HOEE (Higher-Order Edge Enhancement), introdotto nel 2026, mira a ricostruire queste interazioni analizzando il potenziale di attività di ordine superiore (HAP) dei nodi tra snapshots consecutivi. Esiste infatti una correlazione positiva tra la perdita di queste strutture e l'instabilità dei risultati di rilevazione di comunità: ricostruendo i triangoli mancanti, HOEE garantisce una coerenza temporale molto superiore rispetto ai metodi di smoothing tradizionali.

### Comunità Quasi-Periodiche e Durabilità

Il lavoro di Hongchao Qin e colleghi si è evoluto verso l'identificazione di comunità che mostrano una coesione non solo costante, ma ricorrente. Il modello delle "comunità quasi-periodiche" (quasi-periodic communities) rilassa i vincoli di periodicità stretta per adattarsi a ritmi reali leggermente irregolari. Parallelamente, la ricerca sulle "comunità durevoli" continua a perfezionare la capacità di trovare sottografi che resistono al turnover dei membri per tempi massimali, una proprietà fondamentale per l'analisi di team di esperti o gruppi criminali.

## Metriche di Valutazione e Casi di Studio

La valutazione dell'efficacia degli algoritmi di rilevazione di comunità temporali richiede metriche specifiche che vadano oltre la semplice modularità statica.

### Goodness Metrics per Cluster Temporali

Le metriche principali utilizzate includono:

1. **Average Separability (AS):** Cattura l'intuizione che le buone comunità dovrebbero avere pochi archi rivolti verso l'esterno rispetto a quelli interni.
    
2. **Average Density (AD):** Misura la frazione di archi temporali che appaiono tra i nodi del cluster.
    
3. **Average Cohesiveness (AC):** Basata sulla conduttanza, indica quanto sia difficile dividere la comunità in due sottogruppi.
    
4. **Average Clustering Coefficient (ACC):** Valuta la distribuzione locale degli archi basata sui vicini comuni.
    

Gli esperimenti dimostrano che all'aumentare del parametro di stabilità $\tau$, i valori di AS e ACC tendono a crescere, confermando che le comunità più stabili sono anche quelle strutturalmente più coese.

### Caso di Studio: Prof. Qiang Yang (DBLP)

Nell'analisi della rete di collaborazione DBLP, l'applicazione di TSCAN-A ha permesso di identificare la comunità stabile del Prof. Qiang Yang. Il risultato ha mostrato che i membri della comunità identificata non erano semplici co-autori occasionali, ma includevano collaboratori a lungo termine e ex studenti di dottorato che mantenevano legami stretti e persistenti. Al contrario, gli algoritmi statici aggregati non sono stati in grado di isolare questo nucleo, mescolando i collaboratori stabili con centinaia di autori legati a singoli paper pubblicati in anni diversi.

## Conclusioni e Prospettive Future

La rilevazione di comunità stabili nelle reti temporali rappresenta una frontiera critica della data science, con applicazioni che spaziano dalla sociologia alla cybersicurezza. La transizione dai modelli statici a quelli dinamici ha richiesto lo sviluppo di nuove definizioni di stabilità, come la $(\mu, \tau, \epsilon)$-stable similarity, e di algoritmi efficienti in grado di gestire dataset di scala miliare attraverso tecniche avanzate di pruning.

Mentre i modelli probabilistici come il dSBM offrono una solida base teorica per l'evoluzione delle classi latenti, i framework basati sulla densità come TSCAN eccellono nell'identificare strutture locali robuste e nel separare il rumore. La scomposizione tensoriale continua a fornire strumenti unici per l'analisi dei pattern di attività, specialmente in presenza di relazioni multi-modali.

Il futuro della disciplina sembra orientato verso l'integrazione di dinamiche di ordine superiore e l'utilizzo di strumenti di controllo per garantire la stabilità spettrale delle assegnazioni. L'emergere di tecniche come HOEE e F2-CommNet suggerisce che la prossima generazione di algoritmi non si limiterà a osservare il tempo, ma interverrà attivamente per ricostruire le informazioni perse e stabilizzare le traiettorie evolutive delle comunità. In sintesi, la comprensione della stabilità strutturale nei grafi temporali non è solo una sfida computazionale, ma una necessità interpretativa per navigare la complessità dei sistemi interconnessi moderni.

## Riferimenti Chiave e Paper Correlati

Di seguito sono riportati i contributi scientifici più significativi che definiscono lo stato dell'arte e le direzioni future nell'ambito del temporal clustering e della stabilità strutturale:

1. **Qin et al. (2022) - "Mining Stable Communities in Temporal Networks by Density-Based Clustering"**: Il lavoro fondamentale che introduce il framework TSCAN, il concetto di $(\mu, \tau, \epsilon)$-stable core e le tecniche di potatura per grafi temporali su larga scala.
    
2. **Matias & Miele (2017) - "Statistical clustering of temporal networks through a dynamic stochastic block model"**: Propone l'utilizzo del modello dSBM e algoritmi VEM per gestire l'identificabilità delle comunità e il problema del label switching nel tempo.
    
3. **Gauvin et al. (2014) - "Detecting the community structure and activity patterns of temporal networks: A non-negative tensor factorization approach"**: Introduce la scomposizione tensoriale (NTF) per catturare simultaneamente la topologia delle comunità e i loro profili di attività temporale.
    
4. **Rossetti et al. (2017) - "TILES: an online algorithm for community discovery in dynamic social networks"**: Presenta un approccio iterativo online basato su una strategia a "effetto domino" per identificare comunità sovrapposte in flussi continui di interazioni.
    
5. **Qin et al. (2022) - "Mining Bursting Core in Large Temporal Graph"**: Estende la ricerca sulla stabilità identificando i "bursting cores", strutture dense che emergono con intensità in finestre temporali specifiche.
    
6. **Yin et al. (2026) - "Community Detection with Higher-Order Edge Enhancement in Temporal Networks"**: Uno dei lavori più recenti (2026) che affronta l'instabilità dei risultati tramite la ricostruzione di motivi a triangolo basata sul potenziale HAP.