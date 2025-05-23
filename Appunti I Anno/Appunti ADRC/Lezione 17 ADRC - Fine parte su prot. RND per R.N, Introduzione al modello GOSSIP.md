# Continuo prot. RND per R.N

## Estendere BGI a grafi generali

Possiamo estendere il protocollo BGI a **grafi generali** per completare il Broadcast in temp $O(D\log^2(n))$ w.h.p

Per fare ciò dobbiamo metterci nella restrizione che i nodi conoscano $n$

Modifichiamo il protocollo BGI in questo modo, aggiungendo un ulteriore ciclo for : 

For $L=1,\dots,\lceil\log(n)\rceil$
- Nodo trasmette con probabilità $\frac{1}{2^L}$

Il protocollo modificato sarà quindi : 

For $K=1,\dots$ (stages)
- For $L=1,\dots,\lceil\log(n)\rceil$
	- For $j=1,2,\dots,c\log(n)$
		- Se nodo $x$ è stato informato in stage $k-1$, $x$ trasmette con probabilità $\frac{1}{2^L}$

Vediamo che : 
- Il ciclo for interno costa $O(\log(n))$
- Il secondo ciclo for costa anch'esso $O(\log(n))$
- Il ciclo for più esterno costa $O(D)=\text{diam(G)}$

In totale abbiamo che $$Time(BGI-Mod)=O(D\log^2(n))$$
Se i nodi non conoscono $n$, possono "indovinarne" il valore usando la ricerca **binaria**
- Così facendo però i nodi non possono terminare
- Il tempo di completamento diventa $O(D\log^3(n))$ w.h.p

---
# Modelli GOSSIP

Abbandoniamo il modello RADIO per introddure una nuova classe di modelli, ovvero i modelli **GOSSIP**. (nello specifico **GOSSIP PUSH e PULL**)

Per un grafo non diretto $G=(V,E)$, con $|V|=n$ e $|E|=m$, denotiamo il vicinato di un nodo $v\in V$ come $N(v)$ e $d(v)=|N(v)|$

>[!definition]- Definizione (Il modello GOSSIP PUSH (PULL))
>Dato un (non diretto) grafo $G(V,E)$, il modello di comunicazione **uniforme** PUSH (PULL) lavora in modo sincrono, con roud discreti. 
>Ad ogni round $t=0,1,\dots$ ogni nodo $v\in V$ **sceglie** u.a.r uno dei suoi vicini $u\in_uN(v)$ ed esegue l'operazione di **push (pull)** per prendere (inviare) un qualunque messaggio $M$ da (a) $u$
>Alla fine di ogni round $t$, il nodo $u$ (nodo $v$) avrà il messaggio $M$

## Proprietà dei modelli GOSSIP

Ad ogni round, il numero totale di comunicazioni (es. trasmissioni dei messaggi) è $n$ in entrambi i modelli.

In particolare, queste comunicazioni generano un grafo diretto delle comunicazioni al round $t$ chiamato $G_t(V_t,E_t)$, dove $E_t$ rappresenta l'insieme di **archi attivi** ad ogni round $t$.
Il grafo $G_t$ è sempre un **grafo sparso**.

Valgono quindi le seguenti proprietà
1. Nel modello **PUSH**, ad ogni round, il numero atteso di operazioni *push* **ricevute** da ogni nodo è $1$, e in totale è $O(\log(n))$ w.h.p
2. Nel modello **PULL**, ad ogni round, il numero atteso di operazioni *pull* **ricevute** da ogni nodo è $1$, e in totale è $O(\log(n))$ w.h.p

## Protocollo PULL su Clicque

Analizziamo il seguente PULL Broadcast Protocolo (***BP***) sul grafo completo $K(V,E)$

Sia $M$ l'informazione che ogni nodo deve possedere per completare il task del Broadcast.
Assumiamo che ogni entità $x\in V$ abbiamo un registro privato $c_x$ tale che : $$c_x=\begin{cases}\text{informed}&\text{x ha ricevuto M}\\\text{not-informed}&\text{x non ha ricevuto M}\end{cases}$$
In modo formale, il problema è descritto dalla tripla $\langle P_{init},P_{final},G_{pull}\rangle$, dove : 
- $P_{init}=\exists!x\in V:c_x=\text{informed}\land\forall y\neq x,c_y=\text{not-informed}$
- $P_{final} = \forall x\in V : c_x=\text{informed}$
- $G_{pull}=$ Restrizioni del modello GOSSIP $\cup$ KT
	- $KT=$Knowledge Topology

Vediamo ora il protocollo effettivo

Tutti i nodi, durante l'esecuzione del protocollo possono trovarsi nei due stati possibili, ovvero $\{\text{informed,not-informed}\}$ 

BP su $K_n,s\in V$: 
- Inizialmente la sorgente $s$ è l'unica nello stato $\text{informed}$, in quanto è l'unica a possedere il messaggio $M$. Tutti gli altri nodi si trovano nello stato $\text{not-informed}$
- Ad ogni round $t\geq1$ ogni nodo $v$ che si trova nello stato $\text{not-informed}$ esegue una operazione di **pull** su un'altro nodo $u\in_uN(v)$ : 
	- Se $u$ è un nodo nello stato $\text{informed}$, allora $v$ si fa inviare una copia di $M$ e passa allo stato $\text{informed}$
- Il protocollo termina globalmente quando tutti i nodi si trovano nello stato $\text{informed}$

Vale quindi il seguente teorema

>[!teorem]- Teorema 3.3
>Il tempo di completamento di BP su input $(K(V,E),s\in V)$ è $\Theta(\log(n))$ w.h.p

### Dimostrazione

Fissiamo un qualunque $t\geq1$, e per ogni $v\in V$ consideriamo la v.a. binaria $$Y_v=\begin{cases}1&\iff\text{v sarà informato al round }t+1\\0&\text{altrimenti}\end{cases}$$
Definiamo inoltre $$I_{t}=\{u\in V|\text{u è informato al round } t\};\quad I_0=\{s\}$$
Dato che, in ogni roud, ogni nodo effettua una operazione di **pull** da un'altro nodo della rete scelto u.a.r, e i nodi informati al round $t$ sono in totale $|I_t|=m_t$, vale che per ogni $v\in V\setminus I_t$ $$\mathbb E[Y_v]=Pr[T_v=1]=\frac{m_t}{n}$$
A questo punto, la dimostrazione si divide in due parti : 
1. **Prima Fase** : Dimostreremo con alta probabilità che il numero di nodi informati al round $t$ cresce **esponenzialmente** fino a raggiungere $|I_t|=\frac{n}{2}$
2. **Seconda Fase** : Dimostreremo con alta probabilità che il numero di nodi restanti non informati decresce **esponenzialmente** fino a raggiungere lo zero.

#### Prima Fase : $m_t\leq\frac{n}{2}$

Fintanto che $m_t\leq\frac{n}{2}$ abbiamo che $$\mathbb E[m_{t+1}|I_{t}=m_{t}]=m_{t}+\sum\limits_{u\in V\setminus I_{t}}\frac{m_{t}}{n}\geq m_{t}+(n-m_{t})\frac{m_{t}}{n}\geq\frac{3}{2}m_t$$
Questa disuguaglianza ci dice che, ad ogni round, il numero di nodi informati cresce almeno di un **fattore costante** in media.

In particolare, srotolando l'espressione si ottiene che $$m_{t}\geq\frac{3}{2}m_{t-1}\geq\left(\frac{3}{2}\right)^2m_{t-2}\geq\dots\geq\left(\frac{3}{2}\right)^t$$
Se $\tau=\min\{t\geq1:m_t\gt\frac{n}{2}\}$ è il primo round in cui il numero di nodi informati supera la metà del numero di nodi totali, secondo la relazione di ricorrenza si ottiene che $$\tau\simeq\log_{\frac{3}{2}}\left(\frac{n}{2}\right)\in\Theta(\log(n))$$
Ovvero in un numero logaritmico di round, almeno la metà dei nodi viene informato, **in media**

Notiamo però che l'analisi che abbiamo appena fatto indica che tutti cioò accade in media. 
Abbiamo bisogno quindi di prendere i risultati di **concentrazione** ad ogni round usando i bound di **Chernoff**, e poi applicare l'UnionBound su una finestra temporale di lunghezza logartmica.

Dobbiamo quindi dividere la Fase Uno in due sottofasi 

##### SottoFase 1.1 $1\leq m_t\leq\alpha\log(n)$

In questa prima fase, chiamata *Bootstrap*, facciamo riferimento al range $1\leq m_t\leq\alpha\log(n)$ per una certa costante $\alpha\gt0$.

Qui il nostro goal è quello di dimostrare il seguente Claim

>[!teorem]- Claim 3.4
 Per ogni $\alpha\gt0,\exists\gamma=\gamma(\alpha)$ t.c dopo i primi $\tau_1=\gamma\log(n)$ round vale che $m_{\tau_1}\geq\alpha\log(n)$ w.h.p

**dim**
Per ogni $u\in V\setminus\{s\}$, consideriamo la v.a $$Y_u^{(\tau_1)}=1\iff\text{u è informato al round }\tau_1+1$$
Essendo che ogni operazioen di pull, fatta da ogni nodo al round $t$, è **indipendente** rispetto all'operazione di pull fatta al round $t+1$, vale che  : $$\begin{align}Pr\left(Y_u^{(\tau_1)}=0\right)&=Pr\left(\bigcap_{t=1}^{\tau_{1}}\text{u sceglie nodo senza info. al round }t\right)\\&=\prod_{t=1}^{\tau_1}\left(1-\frac{m_t}{n}\right)\\&\leq\left(1-\frac{1}{n}\right)^{t}\leq e^{-\frac{\gamma\log(n)}{n}}\end{align}$$
dato che almeno la sorgente è informata dall'inizio. 

Ora, sia $$Y^{(\tau_1)}=\sum\limits_{u\in V}Y^{(\tau_1)}_u$$
Vale quindi la seguente disuguaglianza : $$\mathbb E[Y^{(\tau_1)}]=\mathbb E\left[\sum\limits_{u\in V}Y^{(\tau_1)}_u\right]\geq\sum\limits_{u}\left(1-e^{-\frac{\gamma\log(n)}{n}}\right)\geq n\frac{\gamma\log(n)}{2n}$$
Inoltre, dato che le v.a $Y_u^{(\tau_1)}$ sono **mutualmente indipendenti**, possiamo applicare il **Chernoff bound moltiplicativo** per una costante $\gamma=\gamma(\alpha)\gt0$ suff. grande, in modo da ottenere che, dopo $\tau_1=\gamma\log(n)$ round vale che $m_{\tau_1}\geq\alpha\log(n)$ w.h.p $\blacksquare$

##### SottoFase 1.2 : $\alpha\log(n)\leq m_t\leq\frac{n}{2}$
