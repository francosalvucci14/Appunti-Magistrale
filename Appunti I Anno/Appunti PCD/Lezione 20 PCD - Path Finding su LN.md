
La **Lightning Network (LN)** è un protocollo di pagamento di secondo livello costruito sopra la blockchain di Bitcoin, progettato per consentire pagamenti istantanei, economici e scalabili. Una delle sue caratteristiche fondamentali è che i pagamenti vengono instradati **fuori dalla blockchain**, attraverso una rete di canali bidirezionali tra nodi.

Perché un pagamento vada a buon fine, deve essere trasportato da un nodo all’altro attraverso uno o più canali: questo è il ruolo del **path finding**.
# Cos'è il Path Finding?

Il _path finding_ (o "ricerca del percorso") è il processo mediante il quale un nodo mittente determina il **percorso ottimale** attraverso la rete Lightning per inviare un pagamento verso un nodo destinatario.

Questa ricerca avviene localmente nel nodo mittente, senza richiedere l'interazione degli altri nodi se non al momento dell'invio effettivo del pagamento.

> A differenza di altri protocolli (es. IP su Internet), dove ogni router decide localmente il prossimo salto (hop), in LN il percorso viene **completamente determinato dal mittente**, che incapsula le istruzioni in un messaggio onion (Onion Routing).

# Obiettivi del path finding

Il path finding non deve semplicemente trovare un _qualunque_ percorso valido, ma deve **ottimizzare** rispetto a più criteri, tra cui:

1. **Liquidità disponibile** nei canali attraversati
2. **Fee totali di instradamento**
3. **Tempo di blocco dei fondi (timelock)**
4. **Probabilità di successo**
5. **Privacy**

Questi obiettivi spesso sono in **conflitto tra loro**: un percorso con fee basse può avere poca liquidità, o un percorso molto breve potrebbe essere più costoso.

# Le informazioni disponibili

Ogni nodo mantiene una **vista locale** della rete, ottenuta tramite il meccanismo di gossip definito nelle specifiche BOLT. Tuttavia, queste informazioni sono **parziali**.

## Informazioni pubbliche:

- Capacità del canale (es: 1 000 000 satoshi)    
- Fee base e fee rate
- CLTV delta (ritardo minimo richiesto in blocchi)
- ID dei nodi e canali

## Informazioni private (non note):

- **Bilanciamento attuale** del canale (quanto è lato A e quanto lato B)
- **Liquidità effettiva disponibile per il routing**
- Eventuali HTLC pendenti

Questo è un punto cruciale: **la LN non rivela il bilanciamento dei canali**, quindi il mittente non sa se un canale è in grado di instradare l’importo desiderato.

# Come stimare la liquidità

Dato che la liquidità è nascosta, il mittente deve ragionare in termini di **intervalli**:

- `liquidity_min` = riserva minima (es: 1%)
- `liquidity_max` = capacità – riserva

Con queste stime, il mittente può costruire un grafo in cui ogni canale ha un “peso” e una “probabilità di successo”.

# HTLC Probing

Una strategia pratica è usare pagamenti “di prova” (HTLC che si annullano prima della consegna) per testare la liquidità effettiva. Se un canale fallisce un pagamento, il mittente può **aggiornare la stima** verso il basso.

Questi tentativi possono essere:

- Binari (es: provo 100 000, poi 50 000…)
- Adattivi (con algoritmi tipo ricerca binaria o bayesiana)

# Algoritmi di ricerca del percorso

La rete Lightning può essere vista come un **grafo orientato e pesato**:

- Nodi = peer LN    
- Archi = canali bidirezionali
- Pesi = combinazione di fee, time-lock, lunghezza, probabilità di successo

## Algoritmi principali:

Nel path finding vengono usati vari algoritmi, a seconda della situazione attuale della LN
Ad es :

1. **BFS (Breadth-First Search)**:    
    - Solo se i pesi sono uniformi
    - Trova semplicemente il minor numero di hop
2. **Dijkstra**:
    - Trova il percorso a costo minimo in base alle fee
    - Funziona bene con fee statiche
3. **A\***:
    - Come Dijkstra, ma più efficiente grazie a euristiche (es: distanza stimata in hop)
4. **Algoritmi probabilistici**:
    - Usati per stimare la **probabilità di successo** di un percorso
    - Si basano su dati storici e feedback (es: Eclair, LND con mission control)
# Multipart Payments (MPP)

La LN supporta i pagamenti multipath (MPP), in cui l'importo viene **suddiviso in più parti**, instradate su percorsi diversi.

Il path finding, in questo caso, deve trovare:

- Diversi percorsi **con liquidità sufficiente per ogni parte**
- Una combinazione che arrivi a coprire l’intero importo
- Tutti i percorsi devono **arrivare entro una certa scadenza (timeout)**

MPP aumenta la complessità del path finding, ma **aumenta le probabilità di successo**, soprattutto per pagamenti grandi.
# Privacy e Onion Routing

Ogni pagamento è incapsulato in un **pacchetto onion**:
- Ogni nodo può vedere solo:
    - Il nodo precedente (che gli ha passato l’HTLC)
    - Il nodo successivo (a cui deve inoltrarlo)
- Non conosce il percorso completo né l’identità del mittente o del destinatario

Questo garantisce una buona **privacy**, ma implica che **i nodi intermedi non possano contribuire al path finding**. L’intero percorso deve essere determinato _ex ante_ dal mittente.
# Inquadramento nello stack Lightning

Il path finding si colloca **nello strato applicativo superiore** della LN:

- Sta sopra il protocollo di rete, HTLC, onion routing    
- È completamente implementato nei **wallet e client LN**
- Non fa parte delle specifiche BOLT, ma è cruciale per l’esperienza utente

Ogni wallet (es. Phoenix, Breez, Zeus, BlueWallet) implementa strategie diverse: alcuni usano path finding off-chain (tramite server), altri si basano su nodi embedded e probing locale.
# Conclusione

Il path finding è uno degli elementi più sofisticati della Lightning Network, e determina direttamente:

- La **velocità** con cui i pagamenti avvengono
- Il **costo effettivo** per l’utente 
- La **probabilità di successo** di ogni transazione
- La **scalabilità** della rete a lungo termine

Poiché la rete è **dinamica, privata e incerta**, non esiste un algoritmo perfetto. Le implementazioni moderne combinano:

- Algoritmi di grafi classici
- Stime di liquidità
- Feedback iterativi da pagamenti falliti
- Ottimizzazione multi-obiettivo
