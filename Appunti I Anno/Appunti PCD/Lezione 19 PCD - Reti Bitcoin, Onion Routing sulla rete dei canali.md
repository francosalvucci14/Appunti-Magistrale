# La rete P2P di Bitcoin

La rete P2P di Bitcoin è sconosciuta *by design*: i nodi *raggiungibili* della rete sono noti, ma se fra due nodi $u$ e $v$ esiste o meno un arco è noto solo ai nodi $u$ e $v$. 

Cercare di capire se sia possibile progettare delle tecniche che rivelino la topologia della rete P2P di Bitcoin è un’area di ricerca attualmente attiva.

Al contrario della rete P2P di Bitcoin, la rete dei canali Lightning è **nota**. 
Ogni nodo è identificato da una chiave pubblica; i canali (gli archi) devono essere noti affinchè un nodo $u$, che debba effettuare un pagamento a un nodo $v$, possa cercare un cammino da $u$ a $v$ lungo il quale instradare il pagamento. 

Si osservi che la rete dei canali Lightning è in realtà un multigrafo, perchè fra due nodi $u$ e $v$ potrebbe esserci più di un arco.

Per un maggiore approfondimento sul discorso *Onion Routing* vedere [BOLT 4](https://github.com/lightning/bolts/blob/master/04-onion-routing.md)

---

# La Rete Peer-to-Peer di Bitcoin e l'Evoluzione con Lightning Network

Il cuore pulsante di Bitcoin è la sua **rete peer-to-peer (P2P)**. A differenza dei sistemi finanziari tradizionali centralizzati, Bitcoin opera su una rete distribuita dove ogni partecipante (nodo) può connettersi direttamente con altri nodi, scambiando informazioni su transazioni e blocchi senza la necessità di intermediari. Questa architettura P2P garantisce la robustezza, la resistenza alla censura e la decentralizzazione del protocollo Bitcoin.

Ogni nodo Bitcoin mantiene una copia (o una parte) della blockchain, valida le transazioni e i blocchi, e li propaga agli altri nodi. Questa comunicazione avviene tramite protocolli di rete standard, con messaggi che annunciano nuove transazioni o blocchi, contribuendo a mantenere un consenso globale sullo stato della blockchain. La forza di questa rete risiede nella sua natura senza permessi: chiunque può partecipare semplicemente eseguendo un nodo Bitcoin.
## Lightning Network: La Rete P2P e la Rete dei Canali

Mentre la rete P2P di Bitcoin gestisce le transazioni on-chain (direttamente sulla blockchain), la **Lightning Network** è una soluzione di scalabilità di **layer-2** che si sovrappone a Bitcoin, permettendo transazioni istantanee ed economiche off-chain. Anche Lightning Network è una **rete P2P**, ma con una struttura e una finalità specifiche, incentrate sui **canali di pagamento**.

In Lightning, i nodi si connettono direttamente tra loro stabilendo **canali di pagamento bilaterali**. Ogni canale è essenzialmente un contratto Bitcoin multisig (multi-firma) sulla blockchain, che permette a due partecipanti di scambiarsi un numero illimitato di transazioni tra loro, aggiornando un saldo interno, senza registrare ogni singola transazione sulla blockchain principale. Solo l'apertura e la chiusura finale del canale (o in caso di controversia) richiedono una transazione on-chain.

La vera magia della Lightning Network risiede nella sua capacità di far sì che i pagamenti attraversino più canali, creando una **rete di canali**. Se Alice ha un canale con Bob, e Bob ha un canale con Carol, Alice può inviare un pagamento a Carol tramite Bob. Questo meccanismo di instradamento è ciò che trasforma una collezione di canali bilaterali in una rete globale capace di connettere quasi tutti gli utenti.

**L'infrastruttura di rete di Lightning**, dettagliata in Capitoli come il 10 e 11 di "Mastering the Lightning Network", si basa su un complesso insieme di regole e protocolli che permettono ai nodi di comunicare, gestire i canali e instradare i pagamenti.

- **Identificatori dei Nodi e dei Canali:** Ogni nodo Lightning ha un identificatore univoco (la sua chiave pubblica), e ogni canale è identificato da un `short_channel_id` che lo lega a una transazione specifica sulla blockchain Bitcoin.
- **Protocollo di Gossip:** I nodi scambiano informazioni sui canali pubblici e sui nodi attraverso un "protocollo di gossip". Questo permette a ogni nodo di costruire una mappa (un "grafo") parziale o completa della rete dei canali pubblici, inclusi dettagli come la capacità dei canali e le commissioni di instradamento.
- **Messaggistica P2P (BOLT 4):** L'interoperabilità tra le diverse implementazioni di Lightning (come LND, c-lightning, Eclair) è garantita dalle specifiche **BOLT (Basis of Lightning Technology)**. In questo contesto, **BOLT 4 ("Peer Protocol")** è di fondamentale importanza. Definisce il protocollo di comunicazione a basso livello tra i nodi peer-to-peer. Questo include:
    - L'**handshake crittografico** per stabilire connessioni sicure e autenticate.
    - La negoziazione delle **capacità** dei nodi (`init` messages).
    - I meccanismi per **mantenere vive le connessioni** (`ping`/`pong`).
    - Il formato generale per lo scambio di tutti i messaggi del protocollo Lightning. In sostanza, BOLT 4 è il linguaggio comune che i nodi Lightning "parlano" per connettersi e comunicare in modo affidabile, ponendo le basi per tutte le operazioni di livello superiore, inclusa la gestione dei canali e l'instradamento dei pagamenti.
## Onion Routing sulla Rete dei Canali: Privacy e Instradamento

Il processo di instradamento dei pagamenti su Lightning Network è una delle sue caratteristiche più innovative e complesse, e si basa sul principio dell'**Onion Routing (Instradamento a Cipolla)**. Questo meccanismo è cruciale per la privacy e per il funzionamento stesso dei pagamenti multi-hop.

Quando un utente (mittente) vuole inviare un pagamento a un altro utente (destinatario) attraverso la Lightning Network, il pagamento non è semplicemente inviato direttamente. Invece, il mittente deve costruire un percorso attraverso una serie di nodi intermedi che hanno canali aperti tra loro. Il mittente conosce il percorso completo (o almeno una parte significativa di esso) grazie al grafo dei canali.

L'Onion Routing funziona incapsulando il pagamento e le istruzioni di instradamento in "strati", proprio come gli strati di una cipolla. Ogni nodo intermedio nel percorso può "sbucciare" solo il suo strato esterno, rivelando le istruzioni per il salto successivo e l'importo da inoltrare, ma senza conoscere l'origine del pagamento o la sua destinazione finale.

**Ecco come si svolge il processo:**

1. **Costruzione del Percorso:** Il mittente seleziona un percorso di nodi e canali che ritiene possano instradare il pagamento.
2. **Preparazione del Pagamento (HTLCs):** Il pagamento viene suddiviso in una serie di **Hash Time-Locked Contracts (HTLCs)**, uno per ogni salto del percorso. Ogni HTLC è condizionato dalla rivelazione di una "pre-immagine" segreta da parte del destinatario entro una certa scadenza.
3. **Onion Payload:** Il mittente crea un "payload a cipolla" cifrato per ogni nodo nel percorso. Questo payload contiene:
    - L'identificatore del nodo successivo.
    - L'importo esatto da inoltrare (con le commissioni incluse).
    - La scadenza (timeout) per l'HTLC.
    - Istruzioni aggiuntive per l'instradamento. Questi payload sono cifrati sequenzialmente, in modo che solo il nodo destinato a uno specifico strato possa decifrarlo.
4. **Inoltro (Forwarding):**
    - Il mittente invia il pacchetto onion al primo nodo del percorso.
    - Il primo nodo decifra il suo strato, apprende che deve inoltrare il pagamento a un certo nodo con un certo importo, e poi invia il pacchetto onion rimanente (che contiene lo strato successivo cifrato) a quel nodo.
    - Questo processo si ripete ad ogni nodo intermedio: decifra, inoltra. Nessun nodo intermedio conosce più di quanto sia strettamente necessario (l'identità del nodo precedente e del nodo successivo).
5. **Rivelazione della Pre-immagine:** Una volta che il pagamento raggiunge il destinatario finale, questo conosce la pre-immagine segreta. Il destinatario la rivela al nodo precedente, sbloccando il suo HTLC. La pre-immagine si propaga all'indietro lungo il percorso, sbloccando sequenzialmente tutti gli HTLC fino al mittente originale. Questo garantisce l'**atomicità**: o tutti i fondi arrivano a destinazione, o nessuno perde nulla.

**Benefici dell'Onion Routing:**

- **Privacy:** Nessun nodo intermedio conosce l'origine o la destinazione finale del pagamento, né l'intera catena di nodi. Questo migliora significativamente la privacy delle transazioni.
- **Sicurezza:** Ogni nodo può verificare solo la validità delle istruzioni a lui destinate, senza compromettere l'integrità dell'intero percorso.
- **Efficienza:** Il mittente ha il controllo sull'instradamento, potendo scegliere percorsi ottimali basati su commissioni e capacità.

**Sfide dell'Instradamento:**

- **Grafo Incompleto:** Il mittente ha spesso una visione incompleta della rete, poiché i canali privati non vengono annunciati.
- **Liquidità Incerta:** La liquidità effettiva all'interno di un canale può variare rapidamente e non è pubblicizzata, rendendo difficile garantire il successo del percorso al primo tentativo.
- **Costo:** Ogni nodo intermedio può addebitare una commissione, aumentando il costo totale del pagamento.

Per mitigare queste sfide, Lightning impiega strategie come i **pagamenti multi-percorso atomici (AMP - Atomic Multi-Path Payments)**, che dividono un pagamento in più parti su percorsi diversi, migliorando la resilienza e la capacità di gestire pagamenti di dimensioni maggiori.

In conclusione, la Lightning Network rappresenta un'evoluzione fondamentale della rete P2P di Bitcoin, introducendo un layer di canali di pagamento che, grazie all'instradamento intelligente basato sull'Onion Routing e ai protocolli ben definiti (come BOLT 4 per la comunicazione P2P), permette transazioni veloci, private ed efficienti, superando le limitazioni di scalabilità della blockchain principale.