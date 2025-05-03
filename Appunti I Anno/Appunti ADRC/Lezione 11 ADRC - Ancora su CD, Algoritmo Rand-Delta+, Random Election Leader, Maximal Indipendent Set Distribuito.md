# Un'altro algoritmo randomizzato per CD

Nella lezione scorsa avevamo introdotto un primo algoritmo randomizzato per il problema del Coloring Distribuito, ottenendo un $(2\Delta)$-coloramento.

Ora vediamo il secondo algoritmo distribuito, che da $2\Delta$ ci farà raggiungere il $(\Delta+1)$-coloramento.
## Procedura Rand-Delta+

In questa procedura facciamo due **cambiamenti chiave**

In ogni fase : 
1. Ogni nodo sopravvisuto $v$ prima sceglie u.a.r un bit $c(v)\in\{0,1\}$
	1. Se $c(v)=0$ allora $v$ viene ***sconfitto*** e salta alla prossima fase
	2. Altrimenti, il nodo $v$ sceglie un colore $C(v)$ u.a.r dalla palette $[\Delta+1]\setminus F_v$

A questo punto, il protocollo procede come Rand-$2\Delta$

![[Pasted image 20250418160753.png|center]]

**Fatto 3** : Se *tutti* i nodi terminano (es. $V=0$) , allora il protocollo Rand-$\Delta^+$ calcola un (legale) $(\Delta+1)$-coloramento per il grafo $G$

**dim** : identica a quella per il protocollo Rand-$2\Delta$

### Rand-Delta+ : Analisi

**Fatto 4** : **Dopo** $O(\log(n))$ fasi, con alta probabilità, *tutti* i nodi terminano

**dim** : 

Fissiamo $v$ e una fase $t$

Per un $u\in N(v)$ fissato, abbiamo che $$Pr[c(u)=c(v)]\leq\frac{1}{2(\Delta+1\setminus|F_v|)}\quad (1)$$
Usando lo Union Bound su ***tutti i vicini sopravvisuti*** $u\in N(v)$ ***che hanno scelto*** $b=1$, dall'equazione $(1)$ si ha che $$Pr[\mathcal E_{v}=\exists u\in N(v):c(u)=c(v)]\leq\frac{\overbracket{(\Delta+1\setminus|F_v|)}^{\text{num. vicini attivi di v}}}{2(\Delta+1\setminus|F_v|)}\leq\frac{1}{2}\quad (2)$$
Quindi, si ha che $$Pr[c(v)\gt0\land\lnot\mathcal E_v]\geq\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}$$
Da qui in poi, si prosegue come la dimostrazione del Fatto 2

---

# Random Leader Election

Spostiamoci dal problema del Coloring Distribuito, e torniamo per un secondo al vecchio problema della Leader Election.

Ricordando che nella Leader Election avevamo mostrato che, senza l'assuzione di Unique Identifier, era impossibile risolvere problema in modo ***deterministico***

Qui studiamo un'approccio probabilistico che risolve il problema della Leader Election, nella situazione in cui tutti i nodi sono **anonimi**

## RLE in Grafi non etichettati

---
# Maximal Indipendent Set Distribuito

- **Sytem Model e Restrizioni**
	- Grafo etichettato $G(V,E),ID$, con $|V|=n$ nodi e $|E|=m$ archi
	- Restrizioni Standard, Modello *Local* e Attivazioni Parallele *Sincrone* $t=1,2,\dots$

**Def (MIS)**
- *Configurazione Iniziale* : un'etichettamento (iniziale) $I:V\to\{0,1\}$ tale che $I(v)=0,\forall v\in V$
- *Configurazione Finale* : un'etichettamento $I:V\to\{0,1\}$ tale che l'insieme $M=\{v\in V:I(v)=1\}$ forma un Indipendent Set ***Massimale***

Remark Massimale : $I$ indipendent set massimale significa che $\forall z\in V\setminus I\implies I\cup\{z\}$ non è più IS

## Procedura Base per MIS

Qualche notazione : 
- $N(v)^+$ = $N(v)\cup\{v\}$
- $N^{+}(S)$ = $S\cup\left(\bigcup_{s\in S}N(s)\right)$

**MIS Task** su grafo $G$ : 
- Imposta $M=\emptyset$
- While $V\neq\emptyset$
	- i. Calcola un indipendent set $S\subseteq V$ per $G$ (**Step (a)**)
	- ii. $M=M\cup S$
	- iii. $V=V\setminus N^{+}(S)$; $E=E\setminus E(N^+(S))$ dove $E(N^+(S))=\{(u,v):v\in N^+(S)\}$
- Per ogni nodo $v\in V$, imposta $I(v)=1\iff v\in M$

>[!teorem]- Teorema
>Sotto le ipotesi definite in precedenza, la procedura MIS-P ritorna sempre un MIS per il grafo $G$

**dim**
- (a) ogni coppia di nodi in $M$ non può essere collegata da un'arco, a causa dello step iii definito dall'algoritmo
- (b) solo i nodi (e gli archi) che sono in $N^+(S)$ sono rimossi ad ogni round. I nodi che stanno in $N^+(S)\setminus S$ sono esattamente quelli che ***NON*** possono essere inseriti in $M$ nei prossimi rounds, e quindi $M$ è **massimale**

### MIS-P : Analisi e Problemi

**Problema 1** : Nello step (a) dobbiamo calcolare un Indipendent Set $S$ per $G$, ma la domanda è
- come possiamo eseguire questo task nel mondo distribuito? I nodi devono sincronizzare le loro scelte

Primo tentativo (inefficiente) : ***Facciamo Leader Election sui Vicinati***
- Ogni nodo $v$ tira una "moneta" (sceglie un random bit $b(v)$)
	- Ogni nodo $v$ che (i) ottiene $1$ mentre (ii) ***tutti*** i suoi vicini ottengono $0$ (in questo caso diremo che $v$ ha "vinto la lotteria") sarà inserito in $S$
	- Questo evento può essere controllato localmente con una comunicazione one-round
	- **Problema Tecnico Fondamentale** : Qual'è la probabilità che per un nodo fissato $v\in N^+(v)$ vinca la lotteria? Purtroppo molto piccola, infatti la probabilità è $$\frac{1}{2}\cdot\frac{1}{2^{|N^+(v)|}}\simeq\frac{1}{2^{|N^+(v)|}}$$Questo implica un tempo atteso ***esponenziale***

Vediamo ora la procedura per migliorare questa situazione

## Il Protocollo di Luby (LP)

Il protocollo è il seguente, e sfrutta l'idea che ogni nodo scelge u.a.r un valore di priorità

**MIS Task** su $G$ ; Parametro $N\in\mathbb N$ (verrà definito dopo)
- Imposta $M=\emptyset$
- While $V\neq\emptyset$
	- Ogni nodo $v$ sceglie u.a.r un valore $r(v)\in[N]$
	- Sia $S=\{v\in V:r(v)=\max\{r(w):w\in N(v)\}\}$
	- Sia $M=M\cup S$
	- $V=V\setminus N^{+}(S)$; $E=E\setminus E(N^+(S))$ dove $E(N^+(S))=\{(u,v):v\in N^+(S)\}$
- Per ogni nodo $v\in V$, imposta $I(v)=1\iff v\in M$

### LP : Analisi

Impostiamo il parametro di LP come $N=\Theta(n^3)$

Perchè lo impostiamo a questo valore? La risposta ce la da il seguente lemma : 

**Lemma** : Ad ogni roud $t\geq1$ abbiamo che le priorità $r(v)$ sono **tutte mutualmente indipendenti** (e stocasticamente indipendenti), e quindi con alta probabilità vale che non esiste nessuna coppia di nodi che ha lo stesso valore di priorità

**dim**

La probabilità che due nodi vicini abbiano lo stesso valore di priorità è 
$$Pr[\exists(u,v)\in E:r(u)=r(v)]=Pr\left(\bigcup_{(u,v)\in E}r(v)=r(u)\right)\leq\sum\limits_{(u,v)\in E}Pr[r(v)=r(u)]=\frac{|E|}{R}$$
Ora, nel caso peggiore $|E|=m=n^2$. Di conseguenza, se scegliamo $R=n^c=n^{3+\varepsilon}$ otteniamo che la prob. descritta sopra è $\simeq\frac{1}{n^c}$, e quindi abbiamo ottenuto che con alta probabilità il Lemma 1 vale.

Ora, per proseguire consideriamo che il Lemma 1 vale con probabilità 1.

Vogliamo ora vedere quati archi vengono rimossi ad ogni round del protocollo.

Consideriamo il seguente esempio : 

![[Pasted image 20250503153214.png|center|500]]

**Goal** : Calcolare il numero (atteso) $e(t)$ di archi che sono ***rimossi*** da $E$ ad ogni round di LP. Per fare ciò, introduciamo l'**azione** : "nodo $u$ ***salva** $w$" 

Per ogni inserimento $v\to S$, sappiamo che $r(v)$ è la priorità *maggiore* in $N^+(v)$. Quindi, come possiamo vedere dalla figura sopra : 
Se $u,v\to S$, allora $r(v)$ è la *maggiore* priorità in $N(u)$ e $r(u)$ è la *maggiore* priorità in $N(v)$

Diamo ora una definizione : 

>[!definition]- Definizione
>Sia il nodo $u$ tale che $$r(u)=\max\{r(v):v\in N(w)\}\space(1)$$
>Allora diciamo che l'arco $(w,w')$ viene *rimosso* perchè **il nodo u salva w**

A questo punto : 
**Claim I** : Dall'equazione $(1)$ otteniamo che $r(u)=\max\{r(v):v\in N^+(u)\cup N^+(w)\}$ -> Evento $B$

A questo punto possiamo affermare il seguente lemma

**Lemma 1** : Ad ogni round del protocollo LP, per ogni nodo $u\to S$, si ha che : $$Pr[B]\geq\frac{1}{d(u)+d(v)}\quad(2)$$
**Dim** : Conseguenza diretta dell'equazione $(1)$ e del fatto che tutte le priorità sono mutualmente indipendenti

***Oss*** : Nell'equazione $(2)$ abbiamo un uguaglianza quando $N(u)\cap N(w)=\emptyset$

Ora, definiamo una v.a $X$ in questo modo : 

>[!definition]- Variabile Aleatoria X Binaria
>Per un $u\to S$, per $w\in N(u)$, definiamo la v.a binaria $$X(u\to w)=\begin{cases}1&\text{u salva w}\\0&\text{altrimenti}\end{cases}$$

Ora, dall'equazione $(2)$ otteniamo che $$Pr[X(u\to w)=1]\geq\frac{1}{d(u)+d(w)}\quad(3)$$
Ora siamo pronti a determinare il valore atteso di archi rimossi ad ogni round $t$

**Lemma 2** : Ad ogni round $t$, il numero $Y$ di archi **rimossi** soddisfa l'equazione : $$\begin{align}\mathbb E(Y)&\geq\frac{1}{2}\cdot\sum\limits_{{u,w}\in E}Pr[X(u\to w)=1]\cdot d(w)\space(\text{dato che se }u\to w\text{ allora u salva tutto }N(w))\\&=\frac{1}{2}\left[\sum\limits_{{u,w}\in E}Pr[X(u\to w)=1]\cdot d(w)+\sum\limits_{{u,w}\in E}Pr[X(w\to u)=1]\cdot d(u)\right]\\&\geq\frac{1}{2}\cdot\sum\limits_{{u,w}\in E}\left[\frac{d(w)}{d(u)+d(w)}+\frac{d(w)}{d(u)+d(w)}\right]\\&=\frac{|E|}{2}\end{align}$$
**Oss** : Perchè abbiamo il fattore $\frac{1}{2}$? Perchè, come possiamo vedere dalla figura precedente, ci **possono essere al più** 2 leader $u$ e $u'$ che possono *salvare* lo ***stesso*** arco $(w,w')$. Quindi ogni "salvataggio" dei leader deve essere ridotto di un fattore $50\%$
### LP : Tempo di convergenza

>[!teorem]- Teorema 1 \[Tempo di convergenza atteso del protocollo LP\]
>Sotto le restrizioni standard, il protocollo LP con input il grafo $G$ ha come tempo atteso di **convergenza** pari a $O(\log(n))$

**Dimostrazione** 

Definiamo $$m(t)=|\overbrace{E(t)}^{\text{num. archi a tempo t}}|$$Allora il Lemma 2 implica che, per ogni $t\geq0:\mathbb E[m(t+1)]\leq\frac{m(t)}{2}$

Usando l'***equazione di Markov***, otteniamo che $$Pr\left[m(t+1)\geq\frac{3}{2}\frac{m(t)}{2}\right]\leq\frac{\left(\frac{m(t)}{2}\right)}{\frac{3}{2}\frac{m(t)}{2}}=\frac{2}{3}\quad(5)$$
Definiamo ora la v.a binaria $Z(t)=\begin{cases}1&m(t)\leq\frac{3}{4}m(t-1)\\0&\text{altrimenti}\end{cases}$ e sia $Z(T)=\sum\limits_{t=1}^TZ(t)$

Dall'equazione $(5)$ otteniamo che $$\mathbb E[Z(T)]=\sum\limits_{t=1}^T\mathbb E[Z(t)]\geq\frac{2}{3}T$$
Quindi, per $T=c\cdot\log(|E(0)|)$, otteniamo che $E(T)=\emptyset$, per una costante $c$ sufficientemente grande. (oss. $E(0)$ è il num. di archi a tempo $0$, quindi è pari a $m\approx n$)

Di conseguenza, quando $E(T)=\emptyset$ il protocollo termina globalmente, ritornando in output il **MIS**. $\blacksquare$


