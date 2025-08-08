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
In questo caso, quando $r=1$, il grafo prende il nome di **Unit Disk Graph**, che noi non tratteremo, ci concentreremo quindi solo sul caso **non normalizzato** ^8b5ecc

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
Così facendo, il grafo ne risulterà fortemente connesso, ma questa soluzione presenta un problema non da poco, ovvero la ***limitatezza delle batterie***

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
>Per ogni costante $c\gt0$ se $r(n)=\left(\sqrt{\frac{\ln(n)+c}{\pi n}}\right)$ allora si ha che $$\lim_{n\to\infty}Pr(\text{G(n,r(n)) è non connesso})\gt0$$

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

Dimostriamo il secondo teorema

Introduciamo i seguenti eventi: 
- $\mathcal E_{\geq1}=G$ contiene almeno un nodo isolato
- $\mathcal E_{i_1,i_2,\dots,i_h}=$ tutti i nodi $i_1,i_2,\dots,i_h$ sono isolati in $G$ con $i_1,i_2,\dots,i_h\in[n]$
- $\mathcal E_{i!}=i$ è l'unico nodo isolato in $G$, con $i\in[n]$

Esprimiamo in loro funzione la probabilità che $G$ sia non connesso, nel seguente modo:
- Ovviamente, se $G$ contiene almeno un nodo isolato allora $G$ è non connesso, dunque vale che $$Pr(\text{G è non connesso})\geq Pr(\mathcal E_{\geq1})$$
- Poi, se accade che $1$ è l'unico nodo isolato, oppure $2$ è l'unico isolato, oppure $\dots\space n$ è l'unico isolato allora accade anche che $G$ contiene almeno un nodo isolato (ovviamente). Dunque vale che $$Pr(\mathcal E_{\geq1})\geq Pr\left(\bigcup_{i\in[n]}\mathcal E_{i!}\right)$$
- Infine, dato che gli eventi $\mathcal E_{1!},\mathcal E_{2!},\dots,\mathcal E_{n!}$ sono eventi **disgiunti** allora vale che $$Pr(\text{G è non connesso})\geq\sum\limits_{i\in[n]}Pr(\mathcal E_{i!})$$

Calcolare direttamente $Pr(\mathcal E_{i!})$ non è semplice, lavoriamo allora per *minorarla* con espressioni che sappaimo calcolare.

A questo scopo, osserviamo quanto segue:
- $i$ è l'unico isolato in $G\iff i$ è isolato e inoltre, comunque scegliamo un altro nodo $j$, si ha che $i,j$ non sono entrambi isolati in $G$, dunque $$\mathcal E_{i!}=\mathcal E_{i}\bigcap_{j\in[n]-\{i\}}\mathcal E_{ij}^{C}=\mathcal E_{i}-\bigcup_{j\in[n]-\{i\}}\mathcal E_{ij}$$
- Da cui si ottiene che: $$Pr(\mathcal E_{ij})=Pr\left(\mathcal E_{i}-\bigcup_{j\in[n]-\{i\}}\mathcal E_{ij}\right)\geq Pr(\mathcal E_{i})-Pr\left(\bigcup_{j\in[n]-\{i\}}\mathcal E_{ij}\right)\geq Pr(\mathcal E_{i})-\sum\limits_{j\in[n]-\{i\}}Pr(\mathcal E_{ij})$$
- **oss**: l'evento $\mathcal E_{ij}^C=i,j$ non sono entrambi isolati

Non ci resta che trovare una **minorazione per $Pr(\mathcal E_{i})$** e una **maggiorazione per $Pr(\mathcal E_{ij})$**

Prima di procedere, indichiamo: 
- per un punto $t\in Q,C_r(t)$ come il cerchi di raggio $r$ e centro $t$
- per $i\in[n],t_i\in Q$ come il punto del quadrato nel quale è posizionato il nodo $i$

##### Minoriamo $Pr(\mathcal E_{i})$

L'evento $\mathcal E_{i}$ si verifica $\iff$ una volta fissato $t_i$, nessun nodo $j\neq i$ è posizioanto in $C_r(t_i)$
- fissato quindi $t_i$ e fissato $j\neq i$ si ha che $$Pr(t_{j}\not\in C_{r}(t_i))=\frac{\text{area di }(Q-C_r(t_i))}{\text{area di Q}}\geq 1-\pi r^2$$
	- Il tutto maggiore o uguale perchè $C_r(t_i)$ potrebbe non essere completamente contenuto in $Q$
- Di conseguenza, fissato $t_i$ vale che $$Pr(\forall j\neq i:t_j\not\in C_r(t_i))\geq(1-\pi r^2)^{n-1}$$
Il punto $t_i$, nel quale posizionare $i$, è scelto u.a.r in $Q$:
- che è un insieme continuo
- e la funzione di densità corrispondente alla scelta u.a.r di un punto in $Q$ è $f(t)=\frac{1}{\text{area di Q}}=1$

Di conseguenza, vale che: 
$$Pr(\mathcal E_{i})\geq\int_{t_i\in Q}f(t_{i})(1-\pi r^{2})^{n-1}dt_{i}=\int_{t_i\in Q}(1-\pi r^{2})^{n-1}dt_{i}=(1-\pi r^{2})^{n-1}$$

##### Maggioriamo $Pr(\mathcal E_{ij})$

Si verifica l'evento $\mathcal E_{ij}\iff$, una volta fissato $t_i,j$ è posizionato in un nodo $t_j\not\in C_r(t_i)$ e nessun nodo $h\in[n]-\{i,j\}$ è posizionato in $C_r(t_i)\cup C_r(t_j)$

Possiamo quindi esprimere questo evento come unione di due eventi mutulamente esclusivi, nel seguente modo: 
- $\mathcal E_{ij}^{1}=t_{j}\not\in C_{2r}(t_{i})\land\space\forall h\in[n]-\{i,j\}[t_h\not\in C_r(t_i)\cup C_r(t_j)]$. Ovvero, $t_j$ si trova nella regione gialla della figura
- $\mathcal E_{ij}^{2}=t_{j}\in C_{2r}(t_{i})-C_{r}(t_{i})\land\space\forall h\in[n]-\{i,j\}[t_h\not\in C_r(t_i)\cup C_r(t_j)]$. Ovvero, $t_j$ si trova nella regione azzurra della figura
- Allora possiamo riscrivere $$Pr(\mathcal E_{ij})=Pr(\mathcal E_{ij}^1\cup\mathcal E_{ij}^2)=Pr(\mathcal E_{ij}^1 )+Pr(\mathcal E_{ij}^2)$$

![[Pasted image 20250807110301.png|center|250]]

**Calcoliamo** quindi $Pr(\mathcal E_{ij}^1)$: 

Fissiamo $t_i$, fissiamo $t_j$ nella zona gialla e fissiamo $h\in[n]-\{i,j\}$.
Allora, la probabilità di scegliere un $t_h$ nella regione rimanente (gialla+azzurra) è pari al rapporto dell'area della regione con l'area del quadrato, che è equivalente a $1-2\pi r^2$
- questa quantità è $\geq (1-2\pi r^2)$ se $t_i,t_j$ non sono troppo vicino al bordo del quadrato

![[Pasted image 20250807112303.png|center|500]]

Fissati invece solamente $t_i$ e $t_j$ nella zona gialla, abbiamo che la probabilità che $\forall h\in[n]-\{i,j\}[t_h\not\in C_r(t_i)\cup C_r(t_j)]$ è in questo caso (con $t_j$ cselto nella zona gialla) pari a $(1-2\pi r^2)^{n-2}$
- anche qui questa quantità è $\geq (1-2\pi r^2)^{n-2}$ se $t_i,t_j$ non sono troppo vicino al bordo del quadrato
- in realtà, complicando leggermente la prova è possibile giungere agli stessi risultati considerando anche gli **effetti ai bordi**, cosa che non non faremo

FIssato solamente $t_i$, la probabilità che, **scegliendo $t_j$ nella zona gialla**, $\forall h\in[n]-\{i,j\}[t_h\not\in C_r(t_i)\cup C_r(t_j)]$ è  $$\int_{t_j\in Q-C_{2r}(t_i)}f(t_j)(1-2\pi r^2)^{n-2}dt_j$$
Mettendo tutto insieme quindi, otteniamo che:

$$\begin{align}Pr(\mathcal E_{ij}^1)&=\int_{t_i\in Q}f(t_i)\int_{t_j\in Q-C_{2r}(t_i)}f(t_j)(1-2\pi r^2)^{n-2}dt_j\space dt_i\\&=\int_{t_i\in Q}f(t_i)\int_{t_j\in Q-C_{2r}(t_i)}(1-2\pi r^2)^{n-2}dt_j\space dt_i\\&=\int_{t_i\in Q}(1-4\pi r^2)(1-2\pi r^2)^{n-2}dt_i\\&=(1-4\pi r^2)(1-2\pi r^2)^{n-2}\end{align}$$

**Maggioriamo** ora $Pr(\mathcal E_{ij}^2)$:

Fissiamo $t_i$, fissiamo $t_j$ nella zona azzurra e fissiamo $h\in[n]-\{i,j\}$.
Allora, la probabilità di scegliere un $t_h$ nella regione rimanente (gialla+azzurra) è pari al rapporto dell'area della regione con l'area del quadrato, e questa volta dipende dalla posizione di $t_j$ nella zona azzurra

![[Pasted image 20250807115313.png|center|500]]

La probabilità di scegliere $t_h$ nella regione rimanente è **massima** quando è massima l'intersezione di $C_r(t_i)$ con $C_r(t_j)$, ossia quando $t_j$ si trova sulla circonferenza che delimita $C_r(t_i)$

Così facendo, l'area di $C_r(t_i)\cup C_r(t_j)=2\pi r^2-\text{area}(C_r(t_i)\cap C_r(t_j))$

![[Pasted image 20250807121023.png|center|250]]

Calcoliamo quanto vale $\text{area}(C_r(t_i)\cap C_r(t_j))$, fissando $t_i$, $t_j$ su $C_r(t_i)$ e $h\in[n]-\{i,j\}$

Vale che
$$\text{area}(C_r(t_i)\cap C_r(t_j))=2\cdot\text{area col. viola}=2\cdot[\text{area col. (rosa e viola)-area }t_jAB]$$

Abbiamo che $t_jAt_i$ è un triangolo equilatero di lato $r$, allora la sua area è $\frac{1}{2}r\frac{r\sqrt{3}}{2}=\frac{r^2\sqrt{3}}{4}$ 

Calcoliamo le altre aree:
- area triangolo $t_jAB$= area triangolo $t_jAt_i=\frac{r^2\sqrt{3}}{4}$ 
- la regione rosa e viola è un settore circolare di $C_r(t_j)$, e il suo angolo al centro $At_jB$ è il doppio di $At_jt_i$ che misura $\frac{\pi}{3}$
	- allora, l'area della regione rosa e viola è $\frac{1}{2}r^2\frac{2\pi}{3}=r^2\frac{\pi}{3}$ 
	- l'area della regione viola è $r^2\frac{\pi}{3}-\frac{r^2\sqrt{3}}{4}$
	- allora, mettendo tutto insieme vale che: $$\text{area}(C_r(t_i)\cap C_r(t_j))=2r^2\left(\frac{\pi}{3}-\frac{\sqrt{3}}{4}\right)$$

![[Pasted image 20250807122915.png|center|250]]

Infine, calcoliamo $\text{area}(C_r(t_i)\cup C_r(t_j))$

Vale che 
$$\begin{align}\text{area}(C_r(t_i)\cup C_r(t_j))&=2\pi r^2-\text{area}(C_r(t_i)\cap C_r(t_j))\\&=2\pi r^2-2r^2\left(\frac{\pi}{3}-\frac{\sqrt{3}}{4}\right)\\&=\frac{4\pi}{3}r^2+\frac{\sqrt{3}\pi}{2\pi}r^2\\&=\pi r^2\left(\frac{4}{3}+\frac{\sqrt{3}}{2\pi}\right)\\&\gt\frac{8}{5}\pi r^2\end{align}$$
Quindi, la probabilità di scegliere $t_h$ nella regione gialla+azzurra è:
$$1-\text{area}(C_r(t_i)\cup C_r(t_j))\lt1-\frac{8}{5}\pi r^2$$
E quindi la probabilità di scegliere tutti gli $n-2$ punti $t_h$ nella regione gialla+azzurra è $\lt\left(1-\frac{8}{5}\pi r^2\right)^{n-2}$
- sempre trascurando gli effetti di bordo

![[Pasted image 20250807121023.png|center|250]]

Quindi, alla fine, fissato $t_i$ otteniamo che la probabilità, scegliendo $t_j$ nella zona azzura, per ogni $h\in[n]-\{i,j\}[t_h\not\in C_r(t_i)\cup C_r(t_j)]$ è $$\int_{t_j\in C_{2r}(t_i)-C_{r}(t_i)}f(t_j)\left(1-\frac{8}{5}\pi r^2\right)^{n-2}dt_j$$
Di conseguenza, abbiamo che:

$$\begin{align}Pr(\mathcal E_{ij}^2)&\lt\int_{t_i\in Q}\int_{t_j\in C_{2r}(t_i)-C_{r}(t_i)}f(t_i)f(t_j)\left(1-\frac{8}{5}\pi r^2\right)^{n-2}dt_j\space dt_i\\&=\int_{t_i\in Q}\int_{t_j\in C_{2r}(t_i)-C_{r}(t_i)}\left(1-\frac{8}{5}\pi r^2\right)^{n-2}dt_j\space dt_i\\&=\int_{t_i\in Q}(4\pi r^2-\pi r^2)\left(1-\frac{8}{5}\pi r^2\right)^{n-2}dt_i\\&=3\pi r^2\left(1-\frac{8}{5}\pi r^2\right)^{n-2}\end{align}$$

Sostituiamo ora $r=\sqrt{\frac{\ln(n)+c}{n\pi}}$, ottenendo che:
$$\begin{align}Pr(\mathcal E_{ij}^2)&\lt\left(1-2\frac{\ln(n)+c}{n}\right)^{n-2}+3\frac{\ln(n)+c}{n}\left(1-\frac{8}{5}\frac{\ln(n)+c}{n}\right)^{n-2}\\&\lt e^{-2\frac{\ln(n)+c}{n}(n-2)}+3\frac{\ln(n)+c}{n}e^{-\frac{8}{5}\frac{\ln(n)+c}{n}(n-2)}\\&= e^{-2\frac{\ln(n)+c}{n}(n-2)}+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}n^{\frac{-2}{5}}e^{-\frac{8}{5}\frac{\ln(n)+c}{n}(n-2)}\\&= e^{-2\frac{n-2}{n}\ln(n)}e^{-2\frac{c(n-2)}{n}}+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}n^{\frac{-2}{5}}e^{-\frac{8}{5}\frac{n-2}{n}\ln(n)}e^{-\frac{8}{5}\frac{c(n-2)}{n}}\\&=e^{-2\frac{n-2}{n}\ln(n)}e^{-2\frac{c(n-2)}{n}}+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{-\frac{2}{5}\ln(n)}e^{-\frac{8}{5}\frac{n-2}{n}\ln(n)}e^{-\frac{8}{5}\frac{c(n-2)}{n}}\\&\lt e^{-2\frac{n-2}{n}\ln(n)}e^{-2\frac{c(n-2)}{n}}+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{-\frac{2}{5}\frac{n-2}{n}\ln(n)}e^{-\frac{8}{5}\frac{n-2}{n}\ln(n)}e^{-\frac{8}{5}\frac{c(n-2)}{n}}\\&=n^{-2\frac{n-2}{n}}e^{-2\frac{c(n-2)}{n}}\left[1+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}\right]\end{align}$$

**Riassumiamo quanto detto fin'ora**: 

Abbiamo detto che 
$$Pr(\text{G non connesso})\geq\sum\limits_{i\in[n]}Pr(\mathcal E_{i!})\geq\sum\limits_{i\in[n]}\left[Pr(\mathcal E_{i})-\sum\limits_{j\in[n]-\{i\}}Pr(\mathcal E_{ij})\right]$$
E abbiamo detto che:
- $Pr(\mathcal E_i)\geq(1-\pi r^2)^{n-1}$
- $Pr(\mathcal E_{ij})\lt n^{-2\frac{n-2}{n}}e^{-2\frac{c(n-2)}{n}}\left[1+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}\right]$

Quindi, abbiamo che: 
$$Pr(\text{G non connesso})\gt n(1-\pi r^2)^{n-1}-n(n-1)n^{-2\frac{n-2}{n}}e^{-2\frac{c(n-2)}{n}}\left[1+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}\right]$$

Passiamo ora al limite, notiamo che $$\lim_{n\to\infty}n(n-1)n^{-2\frac{n-2}{n}}e^{-2\frac{c(n-2)}{n}}\left[1+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}\right]=e^{-2c}\quad(1)$$
Questo perchè (informalmente): 
- $\lim_{n\to\infty}n(n-1)n^{-2\frac{n-2}{n}}=1$
- $\lim_{n\to\infty}e^{-2\frac{c(n-2)}{n}}=e^{-2c}$
- $\lim_{n\to\infty}3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}=0$ 

Quindi, dato che il limite in $(1)$ vale $e^{-2c}$, allora significa che $\forall\varepsilon\gt0\exists n_\varepsilon\gt0:\forall n\geq n_\varepsilon$ vale che $$n(n-1)n^{-2\frac{n-2}{n}}e^{-2\frac{c(n-2)}{n}}\left[1+3\frac{\ln(n)+c}{n^{\frac{3}{5}}}e^{\frac{2}{5}\frac{c(n-2)}{n}}\right]\lt(1+\varepsilon)e^{-2c}$$
Che possiamo riscrivere come: 
$$Pr(\text{G non connesso})\gt n(1-\pi r^2)^{n-1}-(1+\varepsilon)e^{-2c}$$

Allora, per dimostrare il th del limite inferiore, ovvero dimostrare che $\lim_{n\to\infty}Pr(\text{G non connesso})\gt0$ è sufficiente dimostrare che, da *un certo $n$ in poi*, vale che $$n(1-\pi r^2)^{n-1}-(1+\varepsilon)e^{-2c}\gt0$$
Dobbiamo quindi calcolare $$n(1-\pi r^2)^{n-1}\gt (1+\varepsilon)e^{-2c}$$
Calcoliamo il logaritmo della parte sinistra dell'equazione
$$\begin{align}\ln(n(1-\pi r^2)^{n-1})&=\ln(n)+(n-1)\ln(1-\pi r^2)\\(x\lt1\to\ln(n)=-\sum\limits_{k=1}^\infty\frac{(\pi r^2)^k}{k})&=\ln(n)-(n-1)\sum\limits_{k=1}^\infty\frac{(\pi r^2)^k}{k}\\\left(r=\sqrt{\frac{\ln(n)+c}{n}}\to\pi r^2=\frac{\ln(n)+c}{n}\right)&=\ln(n)-(n-1)\sum\limits_{k=1}^\infty\frac{(\ln(n)+c)^k}{kn^k}\end{align}$$

A questo punto, poniamo $\delta(n)=\sum\limits_{k=3}^\infty\frac{(\ln(n)+c)^k}{kn^k}$ così da avere: 
$$\begin{align}\ln(n(1-\pi r^2)^{n-1})&=\ln(n)-(n-1)\left[\sum\limits_{k=1}^2\frac{(\ln(n)+c)^k}{kn^k}+\delta(n)\right]\\&=\ln(n)-(n-1)\left[\frac{(\ln(n)+c)}{n}+\frac{(\ln(n)+c)^2}{2n^2}+\delta(n)\right]\end{align}$$

A questo punto, non resta che maggiorare $\delta(n)$

Vale che:
$$
\begin{align*}
\delta(n)&=\sum\limits_{k=3}^\infty\frac{(\ln(n)+c)^k}{kn^k}\leq \frac{1}{3}\sum\limits_{k=3}^\infty\frac{(\ln(n)+c)^k}{n^k}\leq \frac{1}{3}\int_{2}^\infty\left(\frac{(\ln(n)+c)}{n}\right)^xdx\\&=\lim_{n\to\infty}\frac{1}{3}\int_{2}^h\left(\frac{(\ln(n)+c)}{n}\right)^xdx=\lim_{n\to\infty}\frac{1}{3}\int_{2}^he^{x\ln\left(\frac{(\ln(n)+c)}{n}\right)}dx\\&=\lim_{n\to\infty}\left[\frac{1}{3}\frac{1}{\ln\left(\frac{\ln(n)+c}{n}\right)}\left(\frac{\ln(n)+c}{n}\right)^x\right]^h_2\\&=-\frac{1}{3}\frac{1}{\ln\left(\frac{\ln(n)+c}{n}\right)}\frac{(\ln(n)+c)^2}{n^2}=\frac{1}{3}\frac{1}{\ln\left(\frac{n}{\ln(n)+c}\right)}\frac{(\ln(n)+c)^2}{n^2}
\end{align*}
$$

E, poichè $\lim_{n\to\infty}\frac{1}{\ln\left(\frac{n}{\ln(n)+c}\right)}=0$ allora n$\frac{1}{\ln\left(\frac{n}{\ln(n)+c}\right)}\lt1$ **per $n$ sufficientemente grande** 

Concludendo, otteniamo che $\delta(n)\lt\frac{1}{3}\frac{(\ln(n)+c)^2}{n^2}$ 

Siamo in conclusione di questa dimostrazione interminabile infinta dio cristo sparatemi fanculo

**Ricapitolando**: 
- Abbiamo $Pr(\text{G non connesso})\gt n(1-\pi r^2)^{n-1}-(1+\varepsilon)e^{-2c}$
- Inoltre $\ln(n(1-\pi r^2)^{n-1})=\ln(n)-(n-1)\left[\frac{(\ln(n)+c)}{n}+\frac{(\ln(n)+c)^2}{2n^2}+\delta(n)\right]$
- E infine $\delta(n)\lt\frac{1}{3}\frac{(\ln(n)+c)^2}{n^2}$ 

Allora, vale che: 

$$
\begin{align*}
\ln(n(1-\pi r^2)^{n-1})&\gt\ln(n)-(n-1)\left[\frac{(\ln(n)+c)}{n}+\frac{(\ln(n)+c)^2}{2n^2}+\frac{1}{3}\frac{(\ln(n)+c)^2}{n^2}\right]\\&=\ln(n)-(n-1)\left[\frac{(\ln(n)+c)}{n}+\frac{(\ln(n)+c)^2}{2n^2}+\frac{5(\ln(n)+c)^2}{6n^2}\right]\\&=\ln(n)-\frac{n-1}{n}(\ln(n)+c)-\frac{5(n-1)(\ln(n)+c)^2}{6n^2}\\&\gt\ln(n)-(\ln(n)+c)-\frac{5(n-1)(\ln(n)+c)^2}{6n^2}\\&=-c-\frac{5(n-1)(\ln(n)+c)^2}{6n^2}
\end{align*}
$$

Prendendo il limite all'ultimo membro notiamo che $$\lim_{n\to\infty}\frac{5(n-1)(\ln(n)+c)^2}{6n^2}=0$$
Allora $$\forall\omega\gt0\space\exists\space n_\omega\geq n_\varepsilon:\forall n\geq n_\omega:\frac{5(n-1)(\ln(n)+c)^2}{6n^2}\lt\omega$$
E quindi, per $n$ suff. grande possiamo affermare che $$\begin{align}\ln(n(1-\pi r^2)^{n-1})&\gt-c-\omega\\&\downarrow\\n(1-\pi r^2)^{n-1}&\gt e^{-c-\omega}\end{align}$$
Scegliendo quindi $\omega\lt c-\ln(1+\varepsilon)$ otteniamo che

$$n(1-\pi r^2)^{n-1}\gt e^{-c-c+\ln(1+\varepsilon)}=e^{-2c}e^{\ln(1+\varepsilon)}=(1+\varepsilon)e^{-2c}$$

E quindi (DIO PORCO FINALMENTE CRISTO DIO SIGNORE DEL CIELO DEL PORCO DIO DEI GRAFI GEOMETRICI) otteniamo che:

$$Pr(\text{G è non connesso})\gt n(1-\pi r^2)^{n-1}-(1+\varepsilon)e^{-2c}\gt(1+\varepsilon)e^{-2c}-(1+\varepsilon)e^{-2c}=0$$
**come volevasi dimostrare**
