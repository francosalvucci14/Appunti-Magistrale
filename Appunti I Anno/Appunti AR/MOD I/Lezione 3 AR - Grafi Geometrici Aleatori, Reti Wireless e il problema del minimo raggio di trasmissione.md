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
>Una **rete wireless ad-hoc** è una rete costituita da nodi che dispongono di ricetrasmettitori wireless, mediante i quali realizzano comunicazioni **peer-to-peer** (P2P)

In una rete wireless ad-hoc tipicamente avvengono comunicazioni **multi-hop**, ovvero, due nodi i cui trasmettitori non sono in grado di connettersi l'uno con l'altro (causa elevata distanza, ostacoli, etc..) **possono comunicare** mediante una serie di **nodi intermedi** che si inoltrano l'uno all'altro il messaggio da comunicare finchè esso non raggiunge il nodo destinazione.

Si osservi che, affinchè le comunicazioni possano circolare **ovunque** nella rete e raggiungere anche i nodi più remoti, è necessario che la rete sia **connessa**, infatti deve valere che: $$\forall (a,b)\space\exists P=\langle u_{1},u_{2},\dots,u_{k}\rangle:a\to u_{1},u_{1}\to u_{2},\dots,u_{k-1}\to u_{k},u_{k}\to b$$
**oss**: con la notazione $x\to y$ indichiamo la possibilità di $x$ di **poter trasmettere direttamente (quindi in un hop, salto)** a $y$

La domanda fondamentale che ci porremo d'ora in avanti è: **quali sono le condizioni necessaria al fine di garantire che una rete sia connessa?**

Per rispondere a questa domanda, prima di tutto assumeremo che gli $n$ nodi siano distribuiti u.a.r in una regione limitata che, w.l.o.g, considereremo essere il quadrato unitario $Q=[0,1]^2$.

Assumeremo inoltre che tutti i nodi trasmettano con la stessa potenza e che pertanto, esiste un valore $r$, detto **raggio di trasmissione**, tale che due nodi possono comunicare direttamente solo le la loro distanza è $\leq r$

Inoltre, ad ogni nodo viene assegnata una *batteria di capacità limitata.*

Così facendo avremo che la nostra rete sarà modellata da un **grafo geometrico aleatorio**, che è un grafo **non** orientato

In queste ipotesi, ci porremo come obiettivo quello di determinare il valore minimo di $r$, che genera grafi di comunicazione che sono connessi con alta probabilità, ovvero studieremo il problema : **dati $n$ punti distribuiti u.a.r nel quadrato unitario $Q$, calcolare il valore minimo di $r$ affinchè il grafo $G(n,r)$ sia connesso**

Tale problema prende il nome di **Minimo Raggio di Trasmissione (MTR)**

Piccola osservazione, perchè vogliamo il raggio di trasmissione *minimo*?
A noi basta che il grafo di comunicazione sia **fortemente connesso**, e per fare ciò basta che ad ogni nodo assegniamo un raggio di trasmissione abbastanza grande, ovvero detto $V$ l'insieme dei nodi e indicata con $d(u,v)$ la distanza fra i due nodi $u,v,\forall u\in V$ poniamo $$r_u=\max\{d(u,v):v\in V\setminus\{u\}\}$$
Così facendo, il grafo risulterà fortemente connesso.

C'è un problema però, le batterie illimitate.

Infatti così facendo, l'energia che serve ad un nodo per trasmettere risulterà essere tanto maggiore quanto più è grande il raggio di trasmissione, e di conseguenza il dispendio di energia sarà molto elevato.

Analizziamo quindi quale sarà il valore del raggio di trasmissione minimo necessario.
### Analisi probabilistica del problema MTR

Consideriamo il fatto che ogni nodo abbia lo ***stesso*** raggio di trasmissione, e indichiamolo con $r=r(n)$ (ovvero $r$ in funzione del num. di nodi)

Dimostreremo la seguente affermazione, sfruttando due teoremi fondamentali:
$$\begin{align}&\text{detto }r^{\star}(n)\text{ il min. valore per }r(n)\text{ che garantisce, con prob. ragionevole, che G(n,r(n)) è connesso}\\&\implies r^{\star}(n)\in\Theta\left(\sqrt{\frac{\ln(n)}{n}}\right)\end{align}$$
Valgono quindi i seguenti teoremi, di cui daremo le dimostrazioni

>[!teorem]- Teorema 1 (Delimitazione superiore al minimo raggio di connessione)
>Esiste una costante $\gamma_1\gt0$ tale che se $r(n)\geq\gamma_1\left(\sqrt{\frac{\ln(n)}{n}}\right)$ allora $G(n,r(n))$ è connesso ***con alta probabilità***

>[!teorem]- Teorema 2 (Delimitazione inferiore al minimo raggio di connessione)
>Per ogni costante $c\gt0$ se $r(n)\leq\left(\sqrt{\frac{\ln(n)+c}{n}}\right)$ allora la probabilità che $G(n,r(n))$ sia non connesso è $\gt0$, ovvero $$\lim_{n\to\infty}Pr(\text{G(n,r(n)) è non connesso})\gt0$$

#### Delimitazione Superiore

Dimostriamo quindi il primo teorema.

Sia $k(n)\gt0$ un intero, dipendente da $n$. 

Partizioniamo quindi $Q=[0,1]^2$ in $k^2(n)$ celle, ciascuna di lato $\frac{1}{k(n)}$, poniamo poi $r(n)$ pari alla lunghezza della diagonale di una coppia di celle adiacenti
- due celle si dicono **adiacenti** se hanno un lato in comune

Vale quindi che $$r(n)=\sqrt{\left(\frac{2}{k(n)}\right)^{2}+\left(\frac{1}{k(n)}\right)^{2}}=\frac{\sqrt{5}}{k(n)},\quad k(n)=\frac{\sqrt{5}}{r(n)}$$
![[Pasted image 20250806170606.png|center|250]]

![[Pasted image 20250806171342.png|center|250]]

Ponendo $r(n)$ in questo modo, ciascun nodo in una qualsiasi cella è collegato da un arco a tutti i nodi (eventualmente) contenuti in tutte le celle adiacenti.

Perciò, se *riuscissimo* a dimostrare che, con alta prob., ciascuna cella contiene **almeno** un nodo allora avremmo dimostrato che $G(n,r(n))$ è connesso con alta prob.

Dimostriamo adesso che è **possibile** scegliere $k(n)$ in modo tale che, con alta prob., **nessuna cella sarà vuota**

Invece di calcolare direttamente la prob. di tale evento, calcoleremo la prob. dell'evento complementare, ovvero **esiste almeno una cella vuota**

Sia $C$ una di queste suddette celle, il primo passo sarà trovare una delimitazione superiore a $$Pr(C=\emptyset)$$
Per fare ciò, esprimiamo l'evento $\{C=\emptyset\}$ come intersezioni di eventi, nel seguente modo:
$$\{C=\emptyset\}=\{1\not\in C\land 2\not\in C\land\dots\land n\not\in C\}$$
che possiamo riscrivere come: 
$$\{C=\emptyset\}=\left[\bigcap_{1\leq i\leq n}(i\not\in C)\right]$$
Quindi, abbiamo che: 
$$Pr(C=\emptyset)=Pr\left(\bigcap_{1\leq i\leq n}(i\not\in C)\right)$$
Dato che ogni nodo in $Q$ è posizionato in maniera *indipendente* rispetto agli altri, abbiamo che:
$$Pr\left(\bigcap_{1\leq i\leq n}(i\not\in C)\right)=\prod_{1\leq i\leq n}Pr(i\not\in C)$$
Sia ora $i$ un nodo, la prob. che il nodo $i$ sia scelto all'interno della cella $C$ è pari al rapporto fra l'area di $C$ e l'area del quadrato $Q$ (la cui area è ovviamente $1$). 

Abbiamo allora che:
$$Pr(i\in C)=\frac{\text{Area di C}}{\text{Area di Q}}=\frac{1}{k^{2}(n)}\implies Pr(i\not\in C)=1-\frac{1}{k^{2}(n)}$$
Di conseguenza si ha che:
$$\begin{align}Pr(C=\emptyset)&=Pr\left(\bigcap_{1\leq i\leq n}(i\not\in C)\right)\\&=\prod_{1\leq i\leq n}Pr(i\not\in C)\\&=\left(1-\frac{1}{k^{2}(n)}\right)^{n}\end{align}$$
Vediamo ora quanto vale la prob. che esista almeno una cella vuota, e per fare ciò useremo il principio dello **Union Bound**

Vale quindi che:
$$Pr(\exists C:C=\emptyset)=Pr\left(\bigcup_{C\in Q}(C=\emptyset)\right)\leq\sum_{C\in Q}Pr(C=\emptyset)\implies Pr(\exists C:C=\emptyset)\leq k^{2}(n)\left(1-\frac{1}{k^{2}(n)}\right)^{n}$$
Ora, sostituendo $k(n)=\frac{\sqrt{5}}{r(n)}$ otteniamo che 
$$Pr(\exists C:C=\emptyset)\leq\frac{5}{r^{2}(n)}\left(1-\frac{r^{2}(n)}{5}\right)^{n}$$
Infine, ponendo $r(n)=\gamma_1\left(\sqrt{\frac{\ln(n)}{n}}\right)$ (come da ipotesi del th) otteniamo che:
$$Pr(\exists C:C=\emptyset)\leq\frac{5n}{\gamma_{1}^{2}\ln(n)}\left(1-\frac{\gamma_{1}^{2}\ln(n)}{5n}\right)^{n}$$
A questo punto ci serve un risultato tecnico, dato dal seguente lemma:

>[!teorem]- Lemma
>Per ogni $x\in\mathbb R:1-x\leq e^{-x}$.
>Inoltre, se $x\neq0\implies 1-x\lt e^{-x}$

**dim lemma**:
1) Definiamo la funzione $G(x)=1-x-e^{-x}$
2) Calcoliamo la derivata prima di $G(x):G'(x)=e^{-x}-1$
3) Studiamo il segno di $G'(x):e^{-x}-1\geq0\to e^{-x}\geq e^{0}\to x\leq0$
4) $G'(x)\geq0$ per $x\leq0$: allora $G(x)$ ha un massimo relativo in $x=0$
	1) Inoltre, essendo l'unico punto in cui la derivata si annulla, $x=0$ è anche massimo assoluto
5) Poichè $G(0)=1-0-e^{-0}=0$ questo implica che:
	1) $G(x)\leq G(0)=0$ per ogni $x\in\mathbb R$, ossia $1-x\leq e^{-x}\space\forall x\in\mathbb R$
	2) $G(x)\lt G(0)$

In virtù del lemma appena dimostrato, poichè $\frac{\gamma_{1}^{2}\ln(n)}{5n}\neq0\space\forall n\in\mathbb N$ allora vale che $$\left(1-\frac{\gamma_{1}^{2}\ln(n)}{5n}\right)^{n}\lt e^{-\frac{\gamma_{1}^{2}\ln(n)}{5n}}$$
Quindi:
$$\begin{align}Pr(\exists C:C=\emptyset)&\lt\frac{5n}{\gamma_{1}^{2}\ln(n)}e^{-n\frac{\gamma_{1}^{2}\ln(n)}{5n}}=\frac{5n}{\gamma_{1}^{2}\ln(n)}e^{-\frac{\gamma_{1}^{2}\ln(n)}{5}}\\&\lt\frac{5n}{\gamma_{1}^{2}}e^{-\frac{\gamma_{1}^{2}\ln(n)}{5}}=\frac{5n}{\gamma_{1}^{2}}n^{-\frac{\gamma_{1}^{2}}{5}}\\&=\frac{5}{\gamma_{1}^{2}}n^{1-\frac{\gamma_{1}^{2}}{5}}\end{align}$$
Infine, essendo che $1-\frac{\gamma_{1}^{2}}{5}\lt0$ per $\gamma_1\gt\sqrt{5}$, se poniamo $b=\frac{5}{\gamma_1^2}$ e $c=\frac{\gamma_1^2}{5}-1$ otteniamo che: $$Pr(\exists C:C=\emptyset)\lt\frac{b}{n^c},c\gt0$$
Quindi, nelle ipotesi del teorema, la prob. che $G(n,r(n))$ sia connesso sarà:
$$Pr(\text{G(n,r(n)) è connesso})\geq Pr(\not\exists C=\emptyset)=1-Pr(\exists C:C=\emptyset)\gt1-\frac{b}{n^c}$$
E quindi, $G(n,r(n))$ è connesso con alta probabilità. $\blacksquare$

#### Delimitazione Inferiore

