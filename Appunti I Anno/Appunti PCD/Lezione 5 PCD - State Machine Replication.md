Riassunto

Problema Byzantine Broadcast : 
- Modello sincrono
	- con PKI usiamo il protocollo Dolev-Strong
	- senza PKI:
		- $\not\exists$ protocollo se $f\geq\frac{n}{3}$
		- Protocollo probabilistico se $f\lt\frac{n}{3}$

Il problema Byzantine Broadcast è molto legato al problema **State Machine Replication** (SMR)

# Problema SMR

Consideriamo un sistema distribuito con $n$ nodi. Anche qui, $f$ sono corrotti e $n-f$ onesti.

Assumiamo di essere in un sistema *sincrono* in cui c'è un *clock globale* noto a tutti i nodi che scandisce il tempo in *round* discreti, e ogni messaggio inviato in un round $t$ arriva a destinazione prima dell'inizio del round $t+1$.

Consideriamo il problema seguente : 

Ad ogni nodo $i\in[n]$, in ogni round $r\in\mathbb N$, può essere affidata una o più "transazioni" **tx** (stringhe binarie). 
Ogni nodo $i$ mantiene un *LOG* che consiste in una concatenazione di transazioni, indicato così : $$LOG_{i}^r$$
Dove $i$ è il nodo e $r$ il round

Vogliamo progettare un protocollo che faccia in modo che l'evoluzione dei log dei nodi nel tempo soddisfi le due proprietà seguenti : 
- **Consistency** : Per ogni $i,j\in[n]$ e per ogni coppia di round $r,s\in\mathbb N$, se $i$ e $j$ sono nodi onesti allora $$LOG_{i}^{r}\preceq LOG_{j}^s$$o viceversa, dove con la notazione $LOG\preceq LOG'$ intendiamo che $LOG$ è un prefisso di $LOG'$
- **Liveness** : Esiste un ***confirmation time*** $T_{conf}\in\mathbb N$ tale che, se una transazione **tx** viene affidata a un nodo onesto in un round $r\in\mathbb N$, allora per ogni nodo onesto $i\in[n],tx\in LOG_{i}^{r+T_{conf}}$

Vediamo quindi il **protocollo** per SMR

Sia $\mathbb P_{BB}$ un protocollo per BB per messaggi arbitrari, e supponiamo che tale protocollo lavori in $R$ round.

Definiamo, $\forall i,LOG_i^0=\emptyset$ 

Per ogni $k=0,1,\dots$ 
Al ROUND $kR$:
- La "sorgente" di $\mathbb P_{BB}$ è il suo nodo $k$ mod $n$
- Eseguiamo $\mathbb P_{BB}$ con $msg_{\text{k mod n}}=\left\{tx|\text{tx è stata data in input a k (mod n) e non è ancora inserita in }LOG_{k mod n}^{kR}\right\}$
- 