# Modello Radio Networks

Passiamo dal modello LOCAL al modello RADIO

>[!definition]- Definizione
>Una **Radio Network** è un insieme di **stazioni** (nodi) posizionati su uno spazio Euclideo

Ad ogni nodo $v$ viene assegnato un range di trasmissione $R(v)\gt0$

Un nodo $w$ può ricevere un *messaggio* $M$ da $v$ $\iff d(v,w)\leq R(v)$

![[Pasted image 20250516115208.png|center|300]]

Quando un nodo $v$ invia un messaggio $M$, il messaggio viene inviato su **tutti** gli archi uscenti da $v$ (**Trasmissione Broadcast**) in un singolo ***Time Slot***

![[Pasted image 20250516115342.png|center|300]]

Le Radio Networks sono **Sistemi Sincroni**, infatti tutti i nodi condividono lo stesso *clock globale*.
Di conseguenza, i nodi lavorano con Slot di Tempo, e la trasmissione dei messaggi viene completata in un singolo **time slot**

L'assegnamento dei Range determina univocamente un **Grafo Diretto di Comunicazione** $G(V,E)$

![[Pasted image 20250516115744.png|center|250]]

Tutti i vicini entranti di $s$ (nodo arancione) ricevono il messaggio in $1$ salto, a meno che...
## Collisione dei messaggi (interferenza)

Se, durante un time slot, **due** o **più vicini entranti** inviano un messaggio a $v$ allora $v$ ***non riceve nulla***

![[Pasted image 20250516115941.png|center|350]]

Quindi : 
Un nodo $v$ riceve un messaggio durante lo slot $T\iff$c'è **esattamente** un vicino-entrante di $v$ che invia il messaggio $M$ durante lo slot $T$
## Broadcast su Radio Network

Uno dei task più comuni nel mondo Radio è quello di fare broadcast su tutta la rete.

Vogliamo quindi progettare un protocollo che porti a termine correttamente il broadcast, senza causare collisioni di messaggi.

Il problema lo modelliamo in questo modo : 
- Configurazione iniziale ($t=t_0$): un solo nodo $s\in V$ si trova nello stato INFORMED, mentre tutti gli altri nodi $w\in V-\{s\}$ sono nello stato NON INFORMED
- Configurazione finale : Tutti in nodi $v\in V$ si trovano nello stato INFORMED

Ricordiamo che per il problema del Broadcast abbiamo : 
- **Correttezza** : Un protocollo ***completa*** il Broadcast dalla sorgente $s$ a tutto il grafo $G$ se **c'è un time slot** tale che ogni nodo si trova nello stato INFORMED
- **Terminazione** : Un protocollo ***termina*** se c'è un time slot $t$ tale che **ogni** nodo **interrompe** ogni sua azione ENTRO il time slot $t$


### Protocollo Round-Robin
