# Modello Radio Networks

Passiamo dal modello LOCAL al modello RADIO

>[!definition]- Definizione
>Una **Radio Network** è un insieme di **stazioni** (nodi) posizionati su uno spazio Euclideo

Ad ogni nodo $v$ viene assegnato un range di trasmissione $R(v)\gt0$

Un nodo $w$ può ricevere un *messaggio* $M$ da $v$ $\iff d(v,w)\leq R(v)$

![center|300](img/Pasted%20image%2020250516115208.png)

Quando un nodo $v$ invia un messaggio $M$, il messaggio viene inviato su **tutti** gli archi uscenti da $v$ (**Trasmissione Broadcast**) in un singolo ***Time Slot***

![center|300](img/Pasted%20image%2020250516115342.png)

Le Radio Networks sono **Sistemi Sincroni**, infatti tutti i nodi condividono lo stesso *clock globale*.
Di conseguenza, i nodi lavorano con Slot di Tempo, e la trasmissione dei messaggi viene completata in un singolo **time slot**

L'assegnamento dei Range determina univocamente un **Grafo Diretto di Comunicazione** $G(V,E)$

![center|250](img/Pasted%20image%2020250516115744.png)

Tutti i vicini entranti di $s$ (nodo arancione) ricevono il messaggio in $1$ salto, a meno che...
## Collisione dei messaggi (interferenza)

Se, durante un time slot, **due** o **più vicini entranti** inviano un messaggio a $v$ allora $v$ ***non riceve nulla***

![center|350](img/Pasted%20image%2020250516115941.png)

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
### Protocollo FLOOD

Vediamo inizialmente il protocollo FLOOD studiato qualche tempo fa per la risoluzione del Broadcast sul modello LOCAL

È facile vedere subito che il FLOOD non funziona, infatti basta prendere un grafo fatto in questo modo

![center|400](img/Pasted%20image%2020250516153008.png)

Dove il nodo arancione è la sorgente $s$

All'istante $t=t_0$ la sorgente $s$ invia il messaggio ai suoi $3$ vicini, siano essi per semplicità $u,v,w$. Subito dopo, i rispettivi nodi inviano il messaggio al loro unico vicino, sia esso $x$
Risulta però che nello stesso istante di tempo $t=t_1$ il nodo $x$ riceve $3$ messaggi, provenienti rispettivamente da $u,v,w$, e di conseguenza avviene la collisione, causando così la perdita del messaggio per $x$ ($x$ non riceve nulla).

Con questo semplice controesempio abbiamo visto che il protocollo FLOOD non soddisfa le condizioni necessarie per evitare collisioni, e di conseguenza dobbiamo pensare a un protocollo diverso.
### Protocollo Round-Robin=

Il protocollo che vedremo ora sfrutta l'idea generale del famoso algoritmo di scheduling **Round-Robin**

Prima di vedere il protocollo è necessario definire le assunzioni che stiamo ponendo : 
- I nodi conoscono una buona approssimazione di $|V|=n$
- I nodi sono indicizzati partendo da $0,1,2,\dots$

A questo punto il protocollo lavora nel modo seguente, a **fasi**

- Una **fase** di RR è composta da $n$ time slot
- A tempo $T=0,1,2,\dots$
	- Se il nodo $i=T$, se **INFORMATO**, trasmette il messaggio $M$ ai suoi vicini
	- Tutti gli altri nodi non inviano nulla

Osserviamo che per come è fatto questo protocollo, esso non terminerà mai (problema che verrà affrontato poco più avanti)

**Q.** Cosa possiamo dire dopo una singola fase di RR?
**A** Dopo la prima fase di RR ($n$ time slot) **TUTTI** i vicini-uscenti di $s$ (sorgente) saranno informati

Eseguiamo il protocollo per $L$ volte consegutive

Vale quindi il seguente teorema : 

>[!teorem]- Teorema
>Dopo la fase $k$, tutti i nodi a distanza di salto (hop-distance) $k$ dalla sorgente $s$ saranno nello stato INFORMED

La dimostrazione è per induzione sulla fase $k$
**dim**

*Caso base* : nella prima fase, il primo nodo a trasmettere sarà la sorgente $s$ nel rime slot $T=s$, inoltre in quel time slot $s$ è l'unico nodo a trasmettere (in quanto è l'unico nodo a possedere il messaggio ed essere nello stato INFORMED). 
Allora, per costruzione del grafo di comunicazione, tutti i nodi a distanza $1$ da $s$ entro la fine della prima fase saranno nello stato INFORMED

*Caso induttivo*: ipotizziamo che la tesi sia vera per i nodi dell'insieme $L(k-1)$, ovvero tutti i nodi a distanza $(k-1)$ da $s$.
Sia $w\in L(k)$, per definizione stessa di $L(k)$ deve esistere almeno un nodo, sia esso $j$, che appartiene a $L(k-1)$, quindi $j\in L(k-1)$, tale per cui esiste l'arco diretto $(j,w)$
Per ipotesi induttiva, al time slot $j\space(\text{mod n})$ (ovvero la fine della fase $k-1$) il nodo $j$ trasmetterà il messaggio al nodo $w$, e per definizione del protocollo RR il nodo $j$ sarà l'unico a trasmettere in quell'istante di tempo, quindi il nodo $w$ riceverà correttamente il messaggio senza subire interferenze, entro la fine della fase $k$

![center|300](img/Pasted%20image%2020250517094556.png)

Questa assunzione vale $\forall j\in L(k-1)$, quindi tutti i nodi $w\in L(k)$ verranno informati entro la fine della fase $k$ $\quad\blacksquare$

>[!teorem]- Corollario (Tempo di Completamento)
>Sia $D$ l'**eccentricità** (sconosciuta) della sorgente $s$. Allora, $D$ fasi di RR sono *sufficienti* per INFORMARE tutti i nodi

Cosa possiamo dire della terminazione?
- Purtroppo dipende dalla conoscenza dei nodi

Se loro conoscono $n$ allora posso decidere quando fermarsi.
L'eccentricità della sorgente è al più $n-1$ quindi, dato che ogni nodo ha un clock globale, i nodi possono decidere di **fermare** la loro esecuzione dopo la $(n-1)-$esima fase di RR

Infatti vale : 

>[!teorem]- Tempi per protocollo RR
>Il protocollo **completa** il task in tempo $\Theta(Dn)$
>Il protocollo **termina** (e si parla di terminazione globale) in tempo $O(n^2)$

