### [Minuti 00:00 – 03:00] | Introduzione e Contesto

_(Slide 1 - Titolo | Slide 2 - Roadmap | Slide 4 - Contesto)_

**[Slide 1 - Titolo]**


Questo studio analizza da una prospettiva teorica ed empirica la sicurezza e la resilienza del livello di routing nelle reti off-chain, concentrandosi in particolare sulla più diffusa e adottata: la Lightning Network di Bitcoin.

**[Slide 2 - Roadmap]**

La presentazione odierna seguirà un percorso chiaro: partiremo dall'inquadramento del problema della scalabilità e dai presupposti architetturali della rete Lightning, per poi definire la tesi dello studio e il funzionamento dettagliato dell'attacco. Esamineremo quindi come le tre principali implementazioni software della rete affrontano il routing e reagiscono a tale minaccia. Successivamente, analizzeremo il setup sperimentale e i dati empirici raccolti sulla mainnet di Bitcoin, per poi passare all'analisi algoritmica della strategia ottima dell'attaccante, formalizzata mediante teoria della submodularità. Concluderemo esaminando le contromisure proposte dagli autori e i principali punti di forza del lavoro.

**[Slide 4 - 1. Contesto principale: Scalabilità Blockchain e Reti Off-Chain]**

Per comprendere l'origine della vulnerabilità, dobbiamo richiamare il problema fondamentale che ha motivato la nascita dei protocolli off-chain: il trilemma e i limiti di scalabilità on-chain dei registri distribuiti. Nei sistemi blockchain classici basati su consenso globale, come Bitcoin, il throughput delle transazioni è vincolato dalla frequenza e dalla dimensione dei blocchi, permettendo di processare tipicamente poche decine di transazioni al secondo. Un valore incomparabile rispetto alle decine di migliaia di operazioni al secondo gestite comunemente dai circuiti di pagamento centralizzati tradizionali, come VisaNet.

  

Le _Payment Channel Networks_ (PCN), come la Lightning Network, nascono proprio per superare questo collo di bottiglia spostando la quasi totalità delle transazioni al di fuori della catena principale. In una PCN, due partecipanti aprono un canale bidirezionale vincolando dei fondi attraverso una transazione on-chain. Da quel momento in poi, le due parti possono eseguire un numero potenzialmente illimitato di pagamenti istantanei e a commissioni trascurabili, semplicemente aggiornando il bilancio interno del canale senza coinvolgere la blockchain, a cui si fa ricorso solo all'apertura o alla chiusura del canale.

  

Tuttavia, creare un canale diretto per ogni possibile coppia di utenti risulterebbe impraticabile e insostenibile a livello di liquidità. Per questo motivo le reti off-chain supportano il _multi-hop routing_: i pagamenti tra utenti non direttamente collegati vengono instradati attraverso una catena di nodi intermedi. Per garantire che nessun nodo intermedio possa appropriarsi indebitamente del denaro durante il trasferimento, il protocollo fa leva sugli HTLC, gli _Hashed Time-Locked Contracts_. Si tratta di contratti condizionati alla rivelazione crittografica di un segreto prima di un determinato intervallo temporale espresso in blocchi.

  

Due caratteristiche architetturali risultano cruciali per la sicurezza:

  

- La prima è il **Source Routing**: nella rete Lightning non sono i nodi intermedi a instradare autonomamente i pacchetti passo dopo passo; è il nodo sorgente che sceglie l'intero percorso a priori, basandosi sulla topologia globale della rete e sui parametri economici annunciati dai nodi tramite un protocollo di gossip continuo.
    
      
    
- La seconda è il **Trade-off tra Privacy e Rilevamento degli Errori**: per tutelare l'anonimato dei flussi finanziari, la rete impiega l'onion routing. Ogni nodo intermedio conosce solo chi lo precede e chi lo segue nell'itinerario. Se da un lato questo protegge l'identità del pagatore e del destinatario, dall'altro crea una schermatura totale: in caso di fallimento o di drop del pagamento, la sorgente riceve un errore generico e non è in grado di determinare quale nodo lungo il cammino abbia effettivamente interrotto la transazione.
    
      
    

### [Minuti 03:00 – 06:00] | Tesi Principale e Trade-off Economico

_(Slide 5 - Roadmap | Slide 6 - Tesi Principale)_

  

**[Slide 6 - 2. Tesi Principale e Trade-off Economico]**

  

Arriviamo dunque al nocciolo della ricerca presentata in questo paper. La domanda centrale che si pongono Tochner, Zohar e Schmid è: un attore malevolo può sfruttare deliberatamente le regole di routing e gli incentivi economici di una rete off-chain per manipolare i flussi di pagamento a proprio favore?

  

La risposta degli autori è sconcertante per la sicurezza della rete:

  

Un attaccante esterno può, con un investimento monetario estremamente contenuto — inferiore a 16 dollari — e aprendo appena 5 canali strategici, dirottare circa il 65% delle rotte complessive dell'intera rete Lightning. Se il budget sale a 30 canali, con una spesa sotto i 100 dollari, l'attaccante riesce a catturare oltre l'80% delle rotte globali, potendo attuare un Denial-of-Service sistematico su scala di rete.

  

Questa scoperta introduce una novità sostanziale rispetto agli attacchi noti in letteratura:

  

- Negli attacchi di congestione tradizionali o di isolamento topologico (_eclipse attacks_), l'avversario deve bloccare ingenti capitali finanziari per saturare fisicamente la capacità dei canali altrui.
    
      
    
- Nell'attacco analizzato in questo paper, invece, l'attaccante non deve saturare nulla con la forza bruta: sfrutta a proprio vantaggio gli algoritmi di shortest-path eseguiti dai nodi onesti, attirando spontaneamente il traffico su di sé.
    
      
    

Questo porta alla luce quello che gli autori definiscono il _trade-off fondamentale del difensore_: in una rete decentralizzata ed economica, gli utenti sono razionali e scelgono cammini a costo minimo. Per rendersi immuni al dirottamento, i nodi dovrebbero scegliere deliberatamente percorsi alternativi più costosi, o introdurre casualità a discapito dell'efficienza economica. Tuttavia, fare ciò distruggerebbe la pressione concorrenziale che spinge al ribasso le commissioni di inoltro, degradando la convenienza della rete stessa.

  

### [Minuti 06:00 – 11:00] | Il Meccanismo dell'Attacco

_(Slide 7 - Roadmap | Slide 8 - Meccanismo Base | Slide 9 - Amplificazione col Delay)_

  

**[Slide 8 - 3.1 Il Meccanismo: Route Hijacking & Black-Hole DoS]**

  

Vediamo ora passo dopo passo come si sviluppa concretamente la dinamica dell'attacco, schematizzata nella figura della slide.

  

1. **Apertura dei canali strategici:** L'avversario identifica nodi cardine ad alta centralità topologica all'interno del grafo e apre verso di loro dei canali di pagamento. Qui emerge una prima debolezza strutturale: per impostazione predefinita, quasi tutte le implementazioni di Lightning accettano richieste di apertura di canale da chiunque, poiché dal punto di vista crittografico non c'è rischio immediato di furto di moneta. L'attaccante può quindi agganciarsi ai nodi più critici senza richiedere alcuna autorizzazione preventiva.
    
      
    
2. **Annuncio di condizioni iper-vantaggiose:** Una volta stabilito il canale, l'attaccante diffonde via gossip parametri economici imbattibili: imposta la _base fee_ a zero, la commissione proporzionale (_proportional fee_) a zero e dichiara ritardi di transito minimi.
    
      
    
3. **Dirottamento (Route Hijacking):** Quando i nodi sorgente eseguono i loro algoritmi di source routing (tipicamente varianti dell'algoritmo di Dijkstra ponderato), il canale dell'attaccante viene percepito come una scorciatoia a costo zero estremamente conveniente. Di conseguenza, il traffico tra vaste porzioni del grafo viene ricalcolato e fatto convergere deterministamente verso l'attaccante.
    
      
    
4. **Denial-of-Service (Black-Hole):** Quando il pacchetto crittografato a cipolla contenente l'HTLC arriva al nodo malevolo, questo non inoltra la richiesta all'hop successivo, ma scarta il payload, fungendo da vero e proprio "buco nero". La transazione fallisce, e a causa dell'onion routing la sorgente non ha modo di distinguere se il problema sia dipeso dall'attaccante o da un nodo legittimo lungo la catena.
    
      
    

**[Slide 9 - 3.2 Amplificazione dell'Attacco: Congelamento tramite Delay]**

  

L'attacco base comporta un Denial-of-Service istantaneo: la transazione fallisce e l'utente può tentare un nuovo instradamento. Tuttavia, gli autori dimostrano come l'attaccante possa amplificare drasticamente il danno convertendo il DoS istantaneo in un grave blocco della liquidità dei nodi della rete.

  

Il meccanismo sfrutta la regola di sicurezza dei timeout degli HTLC. Affinché un nodo intermedio non rischi di pagare il canale successivo senza essere rimborsato da quello precedente, le scadenze temporali devono essere rigidamente decrescenti lungo la rotta:

  

$$T_{in} \ge T_{out} + \Delta_{delay}$$

Questo significa che ogni nodo impone un ritardo differenziale $\Delta_{delay}$ misurato in numero di blocchi blockchain.

  

In che modo l'attaccante sfrutta questa proprietà?

  

Quando riceve l'HTLC, il nodo malevolo non invia un messaggio immediato di fallimento, bensì trattiene la transazione fingendo di elaborarla e non rilascia né errore né segreto fino all'ultimo istante prima della scadenza del timeout.

  

L'effetto è devastante: la liquidità allocata per quella transazione in tutti i nodi onesti a monte dell'attaccante rimane completamente immobilizzata e indisponibile all'interno dei canali fino allo spirare del blocco, un tempo che per configurazione standard può raggiungere i 144 blocchi, pari a circa 24 ore.

  

Qui l'attaccante si trova di fronte a un interessante trade-off interno:

  

- Se dichiara un $\Delta_{delay}$ molto elevato, rende il congelamento della liquidità delle vittime molto più severo nel tempo.
    
      
    
- Tuttavia, un ritardo alto incrementa il peso calcolato dagli algoritmi di routing dei mittenti, che cercano di evitare percorsi troppo lenti, riducendo la percentuale di coppie catturate.
    
      
    
- Ciononostante, offrendo commissioni pari a zero, l'attaccante riesce ad assorbire e compensare ampiamente la penalità di ritardo, mantenendo le sue rotte estremamente competitive.
    
      
    

### [Minuti 11:00 – 15:30] | Implementazioni a Confronto (lnd, c-lightning, Eclair)

_(Slide 10 - Roadmap | Slide 11 - lnd | Slide 12 - c-lightning | Slide 13 - Eclair)_

  

Un contributo fondamentale del paper è l'analisi di come i principali software del panorama Lightning implementano concretamente il routing. Gli standard ufficiali, le specifiche BOLT, non impongono infatti un algoritmo specifico, lasciando la scelta della funzione di costo e della policy ai singoli team di sviluppo.

  

**[Slide 11 - 4.1 Implementazione lnd (Golang)]**

  

Iniziamo con `lnd`, sviluppato in Golang, storicamente il client più diffuso sulla rete.

  

`lnd` calcola il peso di ciascun canale lungo il percorso sommando linearmente le commissioni e una penalità proporzionale al ritardo:

  

$$w[i] = ams[i+1] \cdot p[i].delay \cdot r_f + fee_i$$

dove $r_f$ è un fattore di rischio ritardo impostato di default a un valore molto piccolo, pari a $15 \times 10^{-9}$.

  

Per mitigare i fallimenti ripetuti, gli sviluppatori di `lnd` hanno introdotto un meccanismo denominato _Mission Control_. Mission Control assegna una penalità additiva al peso di un canale se questo fallisce, nella forma $\frac{100}{P(h)}$, dove la probabilità $P(h)$ decade esponenzialmente con il trascorrere delle ore dall'ultimo errore secondo la formula:

  

$$P(h) = 0.6 - \frac{0.6}{2^h}$$

Perché `lnd` è vulnerabile nonostante Mission Control?

  

- **Penalità cieca dovuta all'Onion Routing:** Il mittente non sa quale nodo abbia effettivamente causato il drop e finisce per penalizzare tutti gli archi della rotta precedente. Se l'attaccante si posiziona sull'unico link di accesso a un hub primario, la penalizzazione finisce per isolare l'hub onesto e rendere comunque l'attaccante il punto obbligato.
    
      
    
- **Dominanza delle Fee Nulle:** La penalità massima applicata da Mission Control si aggira intorno a 400 unità di peso. Ma poiché il valore di default della `baseFee` nei canali standard è pari a 1000 millisatoshi, l'impostazione a zero da parte dell'attaccante garantisce un risparmio netto che neutralizza interamente l'aggravio della penalità!
    
      
    
- **Bypass temporale:** Inoltre, se l'attaccante trattiene l'HTLC fino all'ultimo istante, ritarda il fallimento e impedisce a Mission Control di registrare l'errore tempestivamente.
    
      
    

**[Slide 12 - 4.2 Implementazione c-lightning (C)]**

  

Passiamo ora a `c-lightning`, l'implementazione in C gestita da Blockstream.

  

`c-lightning` introduce un elemento stocastico, il _Weight Fuzzing_: per evitare che tutti i pagamenti scelgano deterministicamente lo stesso cammino creando colli di bottiglia, applica un disturbo casuale moltiplicando la sola commissione per un fattore scalare derivato da un hash pseudo-casuale (SipHash-24):

  

$$scale = 1 + fuzz \cdot \left(\frac{2h}{2^{64}-1} - 1\right)$$

con un valore di $fuzz$ di default pari a $\pm 5\%$. Il peso complessivo include poi una penalità per il ritardo con fattore di rischio 10:

  

$$w[i] = (ams_{i+1} + fee_{fuzz}) \cdot (delay_i \cdot r_f) + 1$$

Qual è la criticità matematica evidente di questo approccio?

  

Il fuzzing moltiplica _esclusivamente_ la fee del canale. Quando l'attaccante annuncia una tariffa pari a zero, qualsiasi valore scalare moltiplicato per zero produce ancora zero:

  

$$fee = 0 \implies scale \cdot 0 = 0$$

L'entropia del sistema collassa. Il routing stocastico si trasforma in una scelta deterministica: il canale dell'attaccante rimane sempre e comunque la scelta migliore per Dijkstra. Gli autori hanno testato perturbazioni fino al $\pm 30\%$ senza osservare alcuna variazione significativa nella capacità di dirottamento.

  

**[Slide 13 - 4.3 Implementazione Eclair (Scala)]**

  

Infine, analizziamo `Eclair`, il client sviluppato in Scala da ACINQ.

  

Eclair adotta una formula multivariata in cui la fee moltiplica una combinazione lineare di tre parametri normalizzati: ritardo ($\hat{d}$), capacità del canale ($\hat{c}$) e anzianità del canale nel grafo ($\hat{h}$):

  

$$w[i] = fee_i \cdot (\alpha_d \hat{d} + \alpha_c \hat{c} + \alpha_h \hat{h})$$

Inoltre, per evitare la saturazione, Eclair implementa una _Top-3 Randomization_: calcola i tre percorsi migliori a peso minimo e ne seleziona uno con distribuzione uniforme.

  

Tuttavia, anche Eclair presenta due vulnerabilità critiche:

  

- **Accoppiamento moltiplicativo fee-delay:** Poiché la commissione moltiplica l'intera parentesi, se l'attaccante dimezza la fee può permettersi di raddoppiare il ritardo dichiarato mantenendo il peso del canale invariato. Questo espone gravemente Eclair all'attacco di blocco prolungato della liquidità.
    
      
    
- **Inefficacia della Top-3 Randomization:** Creando scorciatoie a fee nulle verso hub chiave, l'attaccante introduce molteplici percorsi artificiali a peso talmente basso da saturare contemporaneamente tutti e tre i migliori percorsi disponibili. Di conseguenza, la scelta casuale uniforme tra le tre alternative ricade sempre e comunque su un cammino controllato dall'avversario.
    
      
    

### [Minuti 15:30 – 18:30] | Setup Sperimentale e Topologia di Rete

_(Slide 14 - Roadmap | Slide 15 - Setup Sperimentale e Topologia)_

  

**[Slide 15 - 5. Setup Sperimentale e Topologia di Rete]**

  

Per validare queste vulnerabilità nel mondo reale, gli autori non si sono limitati a modelli teorici astratti, ma hanno eseguito misurazioni empiriche direttamente sulla mainnet di produzione di Bitcoin.

  

Attraverso un nodo `lnd` attivo collegato alla rete, hanno estratto la topologia pubblica interrogando periodicamente il database locale mediante il comando `lncli describegraph`. Il dataset di riferimento (analizzato su 5 snapshot fino a maggio 2020) comprende circa 4.300 nodi e oltre 33.600 canali, con una capacità media di 0.028 BTC per canale. Lo studio si focalizza sui canali pubblici, poiché quelli privati non vengono annunciati via gossip e vengono impiegati unicamente come primo o ultimo hop del mittente.

  

Dall'analisi dei dati di rete sono emersi pattern comportamentali sorprendenti:

  

1. **Dominio dei Default:** Circa il 60% dei canali attivi non è mai stato configurato manualmente dagli utenti e utilizza i valori predefiniti del software (1000 millisatoshis di base fee e una prop fee di 1 per mille).
    
      
    
2. **Altruismo diffuso:** La seconda configurazione più diffusa vede tariffe completamente azzerate. Nella rete non vi è evidenza empirica di operatori che cercano egoisticamente di massimizzare il profitto alzando le fee, a conferma che gran parte dell'infrastruttura è sorretta da nodi che operano a costi minimi.
    
      
    
3. **Iper-centralizzazione topologica (Rete Scale-Free):** La topologia di Lightning si rivela estremamente asimmetrica. Il 25% dei nodi ha grado 1 (sono foglie periferiche) e il 14% ha grado 2. Soprattutto, circa l'88% di tutti i canali è direttamente collegato a pochi grandissimi hub aventi grado superiore a 600. Questa struttura a invarianza di scala offre grandi prestazioni in termini di diametro ridotto del grafo, ma introduce un'intrinseca vulnerabilità: basta colpire o manipolare una manciata di super-hub per compromettere l'intero network.
    
      
    

### [Minuti 18:30 – 22:30] | Risultati Sperimentali

_(Slide 16 - Roadmap | Slide 17 - Nodi Collusi | Slide 18 - Attaccante Esterno | Slide 19 - Difese Native | Slide 20 - Validazione Storica)_

  

**[Slide 17 - 6.1 Risultati: Vulnerabilità a Nodi Collusi]**

  

I ricercatori hanno innanzitutto simulato uno scenario interno: cosa succederebbe se un ristretto gruppo di hub già esistenti e altamente centrali decidesse di colludere per orchestrare un Denial-of-Service?

  

Simulando pagamenti di 1000 satoshi tra tutte le possibili coppie di nodi, i risultati mostrano che la centralità cumulata del traffico è concentrata in modo drammatico:

  

- 5 nodi collusi sono sufficienti per intercettare e bloccare circa il 60% delle rotte globali.
    
      
    
- 10 nodi intercettano circa l'80% dei flussi di pagamento.
    
      
    
- 30 nodi controllano oltre il 95% di tutte le transazioni possibili.
    
      
    

I risultati sono praticamente indistinguibili tra `lnd`, `c-lightning` ed `Eclair`.

  

In particolare, per Eclair, confrontando la percentuale di percorsi dirottati sulla rotta migliore (65%), sulla media delle tre migliori (67%) e sul caso peggiore in cui tutte e tre le alternative contengono i nodi collusi (60%), si nota che la curva è quasi identica. Ciò prova che la randomizzazione a 3 percorsi non protegge minimamente, poiché i grandi hub costituiscono colli di bottiglia obbligati in quasi ogni cammino plausibile.

  

**[Slide 18 - 6.2 Risultati: Attaccante Esterno a Basso Costo]**

  

La parte più allarmante dello studio riguarda però l'attaccante _esterno_, privo di una posizione privilegiata pregressa. Un'entità malevola che entra da zero nella rete e apre $k$ nuovi canali strategici annunciando fee nulle.

  

I risultati empirici mostrano che:

  

- Con l'aggiunta di soli 5 canali strategici, l'attaccante dirotta circa il 65% del traffico su Eclair, il 70% su c-lightning e oltre il 75% su lnd.
    
      
    
- Con 30 canali, l'attaccante supera stabilmente l'80-85% di copertura globale.
    
      
    

Ma quanto costa tutto questo all'attaccante?

  

I calcoli economici eseguiti su dati di maggio 2020 dimostrano che stabilire un canale costava circa 3.10 dollari, importo che comprende sia la fee on-chain di mining sia la quantità minima di satoshi da vincolare nel canale:

  

- Lanciare un attacco con 5 canali e bloccare il 70% della rete ha un costo complessivo inferiore a **16 dollari**.
    
      
    
- Un attacco con 30 canali per bloccare l'85% del traffico costa **meno di 100 dollari**.
    
      
    

Inoltre, elemento fondamentale: la liquidità vincolata non viene spesa o distrutta! A fine attacco, il malintenzionato può chiudere unilateralmente i canali e recuperare interamente i propri fondi sulla blockchain principale, sostenendo di fatto solo le commissioni di transazione on-chain.

  

**[Slide 19 - 6.3 Inefficacia delle Difese Native dei Client]**

  

Come riassunto nella slide 19, i meccanismi di protezione nativi dei client falliscono miseramente:

  

- Il _Weight Fuzzing_ di `c-lightning` moltiplica per zero.
    
      
    
- Il _Mission Control_ di `lnd` penalizza percorsi interi a causa dell'onion routing e la sua penalità massima non supera il beneficio delle fee azzerate.
    
      
    
- Infine, gli autori hanno testato un'euristica completamente agnostica rispetto al client della vittima: se l'attaccante si limita a collegarsi semplicemente ai nodi con grado topologico più elevato (_degree centrality_), ottiene tassi di dirottamento pressoché identici, rendendo l'attacco universale e indipendente dalle peculiarità software dei nodi bersaglio.
    
      
    

**[Slide 20 - 6.4 Robustezza e Validazione Storica (2018-2020)]**

  

Per scongiurare il dubbio che si trattasse di una falla temporanea legata a una specifica fase di adozione della rete, gli autori hanno replicato l'analisi su cinque distinti snapshot temporali tra novembre 2018 e maggio 2020. In questo intervallo i nodi pubblici sono raddoppiati da 2.100 a oltre 4.300 e i canali sono triplicati. Ebbene, la percentuale di hijacking con 5 e 30 canali è rimasta invariata nel tempo (oscillando sempre tra il 60% e l'85%), dimostrando che si tratta di una vulnerabilità strutturale che persiste e si consolida man mano che la rete cresce.

  

### [Minuti 22:30 – 26:30] | Strategia Ottima dell'Attaccante

_(Slide 21 - Roadmap | Slide 22 - Modellazione e Complessità | Slide 23 - Submodularità e Greedy | Slide 24 - Implementazione Efficiente)_

  

**[Slide 22 - 7.1 Modellazione del Problema e Complessità]**

  

Passiamo ora a una delle sezioni tecnicamente più pregevoli del lavoro: come fa l'attaccante a scegliere in modo matematicamente ottimale i nodi a cui collegarsi per massimizzare il danno?

  

Formalizziamo la rete come un grafo $G=(V, E)$, dove $V$ sono i nodi ed $E$ i canali di pagamento.

  

Definiamo la funzione di _centralità di un insieme di archi_ $S \subseteq E$, indicata con $C(S): 2^E \rightarrow [0, 1]$, come la frazione di percorsi validi tra tutte le coppie di nodi sorgente-destinazione che transitano attraverso almeno uno degli archi contenuti in $S$.

  

È importante notare che $C(S)$ non è una funzione semplicemente additiva, perché più canali controllati dall'attaccante possono coprire la medesima rotta $(s, t)$ generando sovrapposizioni.

  

Il problema dell'attaccante consiste quindi nel determinare il sottoinsieme $S^*$ di cardinalità al più $k$ canali che massimizzi $C(S)$.

  

Questo problema è **NP-hard**: gli autori evidenziano la riduzione diretta dal problema di _Betweenness Centrality Maximization with Bounded Budget_. Una ricerca esaustiva per combinazioni $\binom{\vert{}V\vert{}}{k}$ su un grafo di oltre 4.300 nodi risulterebbe computazionalmente intrattabile.

  

**[Slide 23 - 7.2 Submodularità e Garanzie dell'Algoritmo Greedy]**

  

Qui interviene l'intuizione matematica chiave: gli autori formulano e dimostrano i Lemmi 1 e 2 del paper.

  

La funzione di centralità $C(\cdot)$ gode della proprietà di **submodularità**, oltre ad essere non-negativa e monotona.

  

In termini formali, per ogni coppia di insiemi di canali $A \subseteq B \subseteq E$ e per un arco addizionale $e$, vale che:

  

$$C(A \cup \{e\}) - C(A) \ge C(B \cup \{e\}) - C(B)$$

L'interpretazione economica e geometrica è intuitiva: il guadagno marginale ottenuto aggiungendo un nuovo canale è decrescente. Man mano che l'attaccante ha già monopolizzato ampie fette del grafo, i canali successivi cattureranno percorsi parzialmente già intercettati.

  

Questa proprietà è straordinariamente potente. In virtù del celebre teorema di Nemhauser, Wolsey e Fisher del 1978, massimizzare una funzione d'insieme submodulare e monotona con vincolo di cardinalità mediante una semplice **euristica greedy** (ossia scegliendo a ogni passo il canale che offre il massimo incremento marginale) garantisce un fattore teorico di approssimazione analitica pari a:

  

$$1 - \left(1 - \frac{1}{k}\right)^k \ge 1 - \frac{1}{e} \approx 63.2\%$$

Questo significa che l'algoritmo greedy dell'attaccante fornirà sempre, nel caso peggiore, una soluzione che raggiunge almeno il 63.2% dell'ottimo teorico assoluto. Nella realtà empirica di Lightning, l'algoritmo greedy si comporta persino meglio del lower bound, raggiungendo il 70-75% con 5 canali e oltre l'80% con 30 canali.

  

**[Slide 24 - 7.3 Implementazione Efficiente dell'Attacco]**

  

Resta un ostacolo pratico: valutare l'arco ottimo a ogni iterazione greedy calcolando tutti i percorsi su grafi reali costerebbe $O(\vert{}V\vert{}^3)$, risultando proibitivo in tempo reale.

  

Nel paper vengono presentati due algoritmi per renderlo scalabile:

  

- **Algoritmo 2 (Programmazione Dinamica):** In una fase di pre-processing, si calcola Dijkstra una sola volta per ogni sorgente, memorizzando le distanze minime ottime $dist(s, t)$ in una tabella. A questo punto, per valutare se l'introduzione di un canale verso il nodo candidato $v$ cattura la coppia $(s, t)$, non serve ricalcolare Dijkstra: basta un controllo in tempo costante $O(1)$:
    
      
    
    $$dist(s, candidate) + dist(\bar{v}, dst) \le dist(s, dst)$$
    
- **Algoritmo 3 (Euristica Scalabile):** Introduce ulteriori ottimizzazioni ingegneristiche:
    
      
    - _Short-circuiting:_ se una coppia $(s, t)$ è già stata catturata nei round precedenti, viene saltata all'istante.
        
          
        
    - _Filtraggio topologico:_ si itera solo sulle sorgenti che hanno effettivamente un cammino valido verso il candidato $v$.
        
          
        
    - _Vincoli di protocollo:_ scarta a priori i percorsi che violerebbero i limiti reali di implementazione (come il numero massimo di hop o le soglie di costo).
        
          
        

Grazie a queste tecniche, l'attaccante può calcolare l'insieme quasi-ottimo di canali in pochissimi minuti su grafi di oltre 33.000 archi.

  

### [Minuti 26:30 – 28:30] | Contromisure e la Nuova Policy di Routing

_(Slide 25 - Roadmap | Slide 26 - Nuova Policy | Slide 27 - Sintesi Efficacia)_

  

**[Slide 26 - 8.1 Contromisure: La Nuova Policy di Routing]**

  

Alla luce di queste vulnerabilità, quali soluzioni possono essere adottate?

  

Gli autori formalizzano quattro principi guida per ridefinire le funzioni di routing:

  

1. **Disaccoppiamento additivo del delay:** Il ritardo dichiarato dal canale non deve mai moltiplicare le fee, altrimenti dimezzare la tariffa azzera l'impatto del ritardo. Il delay va inserito come addendo proporzionale al valore trasferito.
    
      
    
2. **Fuzzing applicato al peso globale:** Il disturbo stocastico deve essere applicato all'intero peso dell'arco e non solo alla commissione, evitando il collasso per tariffe a zero.
    
      
    
3. **Premialità per capacità e anzianità del canale:** Privilegiare canali con elevata capacità di bilancio e con una lunga storia on-chain. Mantenere bloccati ingenti capitali per molto tempo ha un costo opportunità reale (tassi di interesse); un attaccante faticherebbe moltissimo a mantenere canali fittizi su larga scala per mesi.
    
      
    
4. **Superamento del Top-k uniforme:** Evitare la scelta casuale uniforme sulle sole 3 rotte minime, facilmente saturabili da scorciatoie malevole.
    
      
    

Partendo dalla funzione di `Eclair`, gli autori propongono una nuova formulazione matematica calibrata:

  

$$w[i] = scale \cdot \left(\alpha_d \hat{d} + \alpha_h \hat{h} - \alpha_c \hat{c} - \beta_{int} \cdot (cap \cdot height) + \frac{fee_i}{ams} \cdot \gamma_f \right)$$

con un fattore scalare gaussiano $scale \sim \mathcal{N}(1, \sigma)$ con deviazione standard $\sigma = 0.2$.

  

I test empirici (visibili nei grafici del paper) confermano che la nuova policy riduce la centralità dei 5 nodi primari dal 60% al 45% e fa crollare l'efficacia dell'attacco delay ad alti blocchi ($>144$) a valori prossimi allo zero.

  

**[Slide 27 - 8.2 Sintesi dell'Efficacia delle Contromisure]**

  

La tabella riassuntiva alla slide 27 mette a contrasto le implementazioni attuali con la soluzione proposta:

  

- Il fuzzing di `c-lightning` e la top-3 di `Eclair` offrono una resilienza base sostanzialmente nulla contro le tariffe azzerate.
    
      
    
- Il _Mission Control_ di `lnd` genera falsi positivi penalizzando nodi onesti lungo la rotta.
    
      
    
- La policy proposta dal paper, invece, garantisce elevata resilienza sia all'hijacking base sia al delay attack.
    
      
    

Ritorna però il vincolo economico: per rendere sicura la rete, la collettività deve accettare una fee media leggermente più alta, pagando il "premio assicurativo" di instradare i fondi attraverso nodi più stabili e affidabili anziché inseguire ciecamente l'illusione del costo nullo.

  

### [Minuti 28:30 – 30:00] | Punti di Forza e Conclusioni

_(Slide 28 - Roadmap | Slide 29 - Punti di Forza | Slide 30 - Fonti)_

  

**[Slide 29 - 9. Punti di Forza del Paper]**

  

Avviandoci alla conclusione, possiamo sintetizzare i quattro grandi punti di forza che rendono questo lavoro una pietra miliare nello studio della sicurezza dei protocolli off-chain:

  

1. **Rigore Matematico e Algoritmico:** Gli autori non hanno proposto una semplice analisi euristica, ma hanno inquadrato il problema nella teoria della centralità dei grafi, dimostrando formalmente la submodularità della funzione e derivando la garanzia teorica di approssimazione greedy $1 - 1/e$.
    
      
    
2. **Validazione Empirica su Mainnet Reale:** Tutti i dati provengono dalla reale topologia di Bitcoin monitorata continuativamente per oltre 13 mesi su 5 snapshot indipendenti.
    
      
    
3. **Studio Incrociato dei Client:** L'analisi dettagliata a livello di codice sorgente di `lnd`, `c-lightning` ed `Eclair` evidenzia come differenze architetturali apparentemente secondarie creino specifici vettori di attacco.
    
      
    
4. **Dimostrazione dell'Economicità Estrema:** L'aspetto più disarmante del lavoro è aver dimostrato che per paralizzare quasi l'intera rete non occorrono milioni di dollari o attacchi su scala statale: bastano meno di 16 dollari e la conoscenza degli algoritmi di instradamento.
    
      
    

**[Slide 30 - Fonti & Riferimenti]**

  

In conclusione, questo articolo evidenzia come le architetture decentralizzate debbano prestare estrema attenzione alle assunzioni economiche implicite nei loro algoritmi. La progettazione futura delle reti di canali di pagamento dovrà necessariamente esplorare modelli economici alternativi — come commissioni ricorrenti o sistemi di reputazione topologica — per disaccoppiare la selezione dei percorsi dalla mera convenienza tariffaria istantanea.

  

Vi ringrazio per l'attenzione e resto a disposizione per qualsiasi domanda o approfondimento.