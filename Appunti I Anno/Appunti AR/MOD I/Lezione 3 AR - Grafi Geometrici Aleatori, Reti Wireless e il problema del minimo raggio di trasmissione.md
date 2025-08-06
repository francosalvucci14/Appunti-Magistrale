# Introduzione

Abbiamo introdotto due modelli di grafi aleatori - il modello Erdos-Renyi e il modello Barabasi-Alber (per fenomeno rich-get-richer)

Entrambi i modelli si prestano a generare grafi che corrispondono a reti, per così dire, virtuali, ossia reti i cui archi sono virtuali e rappresentano realzioni virtuali fra individui come:
- relazioni di amicizia nelle reti sociali
- oppure collegamenti logici, come gli hyperlink

Ma quando occorre effettivamente costruire una rete fisica, ad esempio una rete di calcolatori nella quale occorre predisporre fisicamente le connessioni fra i dispositivi, occorre tenere in considerazioni la struttura geometrica dello spazio nel quale i nodi sono inseriti, e pertanto, i modelli studiati fin'ora sono poco significativi.

Per fare ciò, introdurremo una classe specifica di grafi, chiamati **Grafi Geometrici**, di cui studieremo poi la variante **Aleatoria**
# Grafi Geometrici

>[!definition]- Grafo Geometrico
>Un **grafo geometrico** consiste in un insieme $V$ di punti in uno spazio metrico, dei quali conosciamo le coordinate, e in un parametro $r\gt0$

Per fissare le idee, assumiamo che lo spazio metrico sia il **piano cartesiano** $\mathbb R^2$, in questo caso infatti, ciascun punto $A$ è individuato da una coppia di coordinate: $A=(x_A,y_A)$

Gli arhci del grafo individuato da $V$ e $r$ sono tutte e sole le coppie di punti la cui **distanza euclidea** è $\leq r$, ovvero abbiamo che: 
$$E=\{(A,B):A\in V\land B\in V\land\sqrt{(x_A-x_B)^2-(y_A-y_B)^2}\leq r\}$$
Generalmente, si **normalizza** rispetto a $r$, ossia:
- si riportano i punti in scala $1:r$ (si pone pari ad $r$ l'unità sugli assi copordinati), in modo da avere che due punti sono adiacenti $\iff$ la loro distanza è $\leq1$
In questo caso, quando $r=1$, il grafo prende il nome di **Unit Disk Graph**, che noi non tratteremo, ci concentreremo quindi solo sul caso **non normalizzato**

Analizziamo ora la variante aleatoria di questi grafi

## Grafi Geometrici Aleatori

Fissiamo $n\in\mathbb N,r\gt0$ (vedremo poi che $r\leq\sqrt{2}$) 

Scegliamo **u.a.r** $n$ punti nel quadrato $[0,1]\times[0,1]$ e costruiamo il grafo geometrico $G(n,r)$ corrispondente:
- pocihè i punti sono scelti nel quadrato unitario, e la diagonale del quadrato misura $\sqrt{2}$ è sufficiente scegliere $r\leq\sqrt{2}$
- infatti, con $r=\sqrt{2}$ otteniamo un grafo completo ed è dunque inutile scegliere per $r$ un valore maggiore di $\sqrt{2}$

Naturalmente, l'aleatorietà del grafo $G(n,r)$ dipende dalla scelta dei punti nel quadrato unitario, infatti quando $r\in[\sqrt{2},0]$ vale che:
1) $r=\sqrt{2}$ e per ogni scelta di $n$, abbiamo che il grafo $G(n,\sqrt{2})$ è un grafo fissato (infatti, qualunque sia $n$, il grafo $G(n,\sqrt{2}$ risulterà essere un **grafo completo**)
2) $r=0$ e per ogni scelta di $n$, abbiamo che il grafo $G(n,0)$ è un grafo fissato (infatti, qualunque sia $n$, il grafo $G(n,0)$ è sempre un grafo costituito da **soli nodi isolati**)

Abbiamo quindi una sorta di analogia con il modello di Erdos-Renyi, nel quale avevamo scelto il parametro $p$ in funzione di $n$, ovvero $p=p(n)$. 

Per i grafi geometrici aleatori scegliamo quindi $r$ in funzione di $n$, ovvero $r=r(n)$, infatti scegliendo $r$ costante, otterremmo grafi sempre più densi al crescere di $n$

Il problema che vogliamo affrontare è quindi **scegliere il più piccolo** valore di $r(n)$ che permette di ottenere un grafo connesso.

Naturalmente, essendo $G(n,r)$ un evento aleatorio, vogliamo studiarne la connessione in ambito probabilistico, ci interessa quindi che $G(n,r)$ sia **connesso con alta probabilità**

Vediamo ora una applicazione famosa di questo problema, ovvero le **reti wireless ad-hoc** (sezione mutuata con la Dispensa $1$ del corso.)

## Reti Wireless ad-hoc

Prima di tutto, cos'è una *rete wireless ad-hoc*?

>[!definition]- Rete Wireless ad-hoc
>Una **rete wireless ad-hoc** è una rete costituita da nodi che dispongono di ricetramettitori wireless, mediante i quali realizzano comunicazioni **peer-to-peer** (P2P)

In una rete wireless ad-hoc tipicamente avvengono comunicazioni **multi-hop**, ovvero, due nodi i cui trasmettitori non sono in grado di connettersi l'uno con l'altro (causa elevata distanza, ostacoli, etc..) **possono comunicare** mediante una serie di **nodi intermedi** che si inoltrano l'uno all'altro il messaggio da comunicare finchè esso non raggiunge il nodo destinazione.

Si osservi che, affinchè le comunicazioni possano circolare **ovunque** nella rete e raggiungere anche i nodi più remoti, è necessario che la rete sia **connessa**, infatti deve valere che: $$\forall (a,b)\space\exists P=\langle u_{1},u_{2},\dots,u_{k}\rangle:a\to u_{1},u_{1}\to u_{2},\dots,u_{k-1}\to u_{k},u_{k}\to b$$
**oss**: con la notazione $x\to y$ indichiamo la possibilità di $x$ di **poter trasmettere direttamente (quindi in un hop, salto)** a $y$

La domanda fondamentale che ci porremo d'ora in avanti è: **quali sono le condizioni necessaria al fine di garantire che una rete sia connessa?**

Per rispondere a questa domanda, prima di tutto assumeremo che gli $n$ nodi siano distribuiti u.a.r in una regione limitata che, w.l.o.g, considereremo essere il quadrato unitario $Q=[0,1]^2$.

Assumeremo inoltre che tutti i nodi trasmettano con la stessa potenza e che pertanto, esiste un valore $r$, detto **raggio di trasmissione**, tale che due nodi possono comunicare direttamente solo le la loro distanza è $\leq r$

Così facendo avremo che la nostra rete sarà modellata da un **grafo geometrico aleatorio**, che è un grafo **non** orientato

In queste ipotesi, ci porremo come obiettivo quello di determinare il valore minimo di $r$, che genera grafi di comunicazione che sono connessi con alta probabilità, ovvero studieremo il problema : **dati $n$ punti distribuiti u.a.r nel quadrato unitario $Q$, calcolare il valore minimo di $r$ affinchè il grafo $G(n,r)$ sia connesso**

Tale problema prende il nome di **Minimo Raggio di Trasmissione (MTR)**

### Analisi probabilistica del problema MTR

