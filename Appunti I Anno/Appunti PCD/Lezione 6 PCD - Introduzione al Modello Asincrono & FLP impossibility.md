# Modello Asincrono

Fin'ora abbiamo assunto di essere nel cosidetto modello **sincrono**, dove i ritardi tra lo scambio di messaggi è costante.

In questo modello abbiamo visto il problema Byzantine Broadcast, e i vari protocolli che lo risolvono (sia con PKI sia senza PKI)

Spostiamoci ora nel modello **asincrono**

In questo modello : 
- Ci sono $n$ nodi
- Non abbiamo un clock globale ($\not\exists$ concetto di ROUND)
- I messaggi "prima o poi" arrivano (non abbiamo il controllo sui ritardi)
- I protocolli sono detti "event driven" : un nodo fa qualcosa in risposta a un messaggio

Iniziamo a dare qualche definizione

>[!definition]- Stato del sistema (configurazione)
>Lo stato del sistema (anche detto **configurazione**) è $$\mathbb C=(S,M)$$
>Dove : 
>1. $S$ è l'insieme degli stati dei nodi
>2. $M$ è l'insieme dei messaggi non ancora arrivati a destinazione

>[!definition]- Stato di un nodo
>Lo **stato** di un nodo è l'insieme dei valori delle sue variabili locali (e l'insieme dei messaggi arrivati al nodo fino a quel momento)

>[!definition]- Messaggio
>Un **messaggio** è la coppia $$m=(p,x)$$
>Dove : 
>1. $p$ è il destinatario del messaggio
>2. $x$ è il contenuto del messaggio

A questo punto la domanda è : cosa deve fare un protocollo nel modello asincrono?

Un **protocollo** deve specificare, data una configurazione $\mathbb C=(S,M)$ e un messaggio $m\in M$, in quale configurazione $\mathbb C'$ si arriva se il messaggio $m$ viene consegnato. Chiamiamo tale configurazione $$\begin{align}&\mathbb C'=m(\mathbb C)\\&\mathbb C'=(S',M')\end{align}$$
Dove $$\begin{align}&M'=M\setminus\{m\}\cup M^{(p)},\quad\text{p destinatario di m}\\&S'=S\text{ eccetto per lo stato del nodo p}\end{align}$$
**Oss** : con $\mathbb C'=m(\mathbb C)$ intendiamo la configurazione che otteniamo se, partendo dalla configurazione $\mathbb C$ il messaggio $m$ viene consegnato

**Oss 2**

Sia $\mathbb C=(S,M)$ e siano $m_1=(p_1,x_1)$ e $m_2=(p_2,x_2)$ messaggi $\in M$

Cosa succede alla configurazione $\mathbb C$ se consegno prima $m_1$ e poi $m_2$? 
- Succede che dalla configurazione $\mathbb C$ andiamo in una configurazione $\mathbb C'=m_1(\mathbb C)$, e poi in una configurazione $\mathbb C''=m_2(m_1(\mathbb C))$ 
Viceversa : 
- Succede che dalla configurazione $\mathbb C$ andiamo in una configurazione $\mathbb C'=m_2(\mathbb C)$, e poi in una configurazione $\mathbb C''=m_1(m_2(\mathbb C))$ 

In generale vale che, se $$p_1\neq p_2\implies m_2(m_1(\mathbb C))=m_1(m_2(\mathbb 
C))$$
Questo perchè. se $p_1=p_2=p$ allora il nodo $p$ potrebbe fare cose diverse a seconda dell'ordine di ricezione

Questo fatto può essere iterato all'infinito, e per fare ciò diamo la definizione di **schedule** di messaggi

>[!definition]- Schedule dei messaggi
>Uno **schedule** di messaggi, denominato $\sigma$, è una sequenza ordinata di messaggi. 
>Esempio : $$\sigma=[m_1=(p_1,x_1),\dots,m_k=(p_k,x_k)]$$
>Dato un protocollo $\Pi$, una configurazione $\mathbb C$ e uno schedule $\sigma$, indichiamo con $\sigma(\mathbb C)$ la configurazione che si ottiene partendo da $\mathbb C$ in base al protocollo $\Pi$ dopo la consegna di tutti i messaggi in $\sigma$ (nell'ordine stabilito dalla sequenza)

# Problema Byzantine Agreement

Dopo questa panoramica sul modello asincrono, siamo pronti per definire l'equivalente del problema Byzantine Broadcast nel modello asincrono.

Tale problema prende il nome di **Byzantine Agreement**

- In questo problema abbiamo $n$ nodi, di cui $f$ corrotti.
- Ad ogni nodo $i$ viene affidato in input un messaggio $b_i\in\{0,1\}$

Vogliamo progettare un protocollo per BA, che **termini in un tempo finito**, in cui ogni nodo onesto $i$ dia in output un valore $y_i\in\{0,1\}$ , in modo da rispettare :
1. **Consistency** : Se $i,j$ sono nodi onesti, allora $y_i=y_j$
2. **Validity** : Se tutti i nodi onesti hanno in input lo stesso bit $b$, allora $y_i=b$ per ogni nodo onesto $i$ (notare l'assenza di sorgente unica)

A questo punto, diamo l'enunciato del Teorema (il più importante del calcolo distribuito)

## FLP Impossibility

>[!teorem]- Teorema FLP (Fischer,Lynch,Paterson)
>Nel modello asincrono nessun protocollo **deterministico** per BA, che termina in un tempo finito, può soddisfare *consistency* e *validity* se c'è almeno **un nodo corrotto**

Per dimostrare questo teorema (la seconda parte della dimostrazione starà in lezione 7) dobbiamo dare una definizione molto importante

>[!definition]- 0-valente, 1-valente, bivalente
>Data una configurazione $\mathbb C=(S,M)$ e un protocollo deterministico per BA, chiamato $\mathbb P_{BA}$, diciamo che $\mathbb C$ è : 
>1. **0-valente** : Se, qualunque cosa fa l'avversario, al termine del protocollo tutti i nodi onesti danno in output $0$
>2. **1-valente** : Se, qualunque cosa fa l'avversario, al termine del protocollo tutti i nodi onesti danno in output $1$
>3. **bivalente** : Altrimenti

A questo punto, siamo pronti per dare l'idea della dimostrazione :

Dato un qualunque protocollo $\mathbb P_{BA}$, allora : 
1. $\exists$ un'assegnazione degli input tale che la configurazione iniziale $\mathbb C_0$ è bivalente
2. Se $\mathbb C$ è una configurazione bivalente, allora $\exists$ uno schedule $\sigma$ applicabile tale che $\sigma(\mathbb C)$ è anche lei bivalente

>[!teorem]- Lemma 1
>Se $\mathbb P_{ba}$ è un protocollo deterministico per Byzantine Agreement che termina e soddisfa *validity* e *consistency* allora esiste un’assegnazione degli input ai nodi tale che la configurazione iniziale è bivalente.

**Dimostriamo** il punto 1 (Lemma 1)

Sia $X_i$= assegnazione degli input in cui tutti i nodi $\leq i$ hanno in input $0$ e tutti i nodi $\gt i$ hanno in input 1
Esempio : $$\begin{align}X_0&=[\underbracket{1}_1|\underbracket{1}_2|\dots|\underbracket{1}_n]\to\text{0-valente}\\ X_1&=[0|1|\dots|1]\\&\vdots\\ X_{n-1}&=[0|0|0|\dots|1]\\X_n&=[0|0|0|\dots|0]\to\text{1-valente}\end{align}$$
Sia ora $i$ il più piccolo indice tale che $X_i$ ***non è 1-valente***
$$\begin{align}X_i&=[1|1|\dots|\underbrace{1}_i|0|\dots|0]\\ X_{i-1}&=[1|1|\dots|\underbrace{0}_i|0|\dots|0]\end{align}$$
La configurazione $X_i$ deve essere per forza **bivalente**, e non può essere **0-valente** : Questo perchè, essendo che $X_i,X_{i-1}$ differiscono di un solo bit, se quel bit fosse un nodo corrotto allora potrebbe far dare in output a tutti gli altri nodi il valore $0$, e questo non rispetterebbe la condizione di *validity*

### Dimostrazione Lemma 1 (Prof)

Per $i = 0, 1, \dots , n$, sia $X_i$ la configurazione iniziale in cui gli input dei nodi minori o uguali a $i$ sono $1$ e gli input dei nodi maggiori di $i$ sono $0$. 
Siccome per ipotesi $\mathbb P_{ba}$ soddisfa validity la configurazione $X_0$ (in cui tutti gli input sono 0) deve essere $0$-valente e la configurazione $X_n$ (in cui tutti gli input sono 1) deve essere $1$-valente.

Sia $i$ il più piccolo indice tale che $X_{i−1}$ è $0$-valente e $X_i$ non è $0$-valente.
Mostriamo che $X_i$ non può essere $1$-valente, e quindi deve essere bivalente.

Siccome per ipotesi $\mathbb P_{ba}$ **termina anche in presenza di un nodo corrotto**, deve esistere uno schedule $\sigma$ applicabile a $X_{i−1}$ tale che $\sigma$ ***non contiene messaggi*** per il nodo $i$ e $\sigma(X_{i−1})$ è una
configurazione in cui tutti i nodi diversi da $i$ che seguono il protocollo hanno deciso il loro output.

Infatti, se un tale schedule non ci fosse, nel caso in cui $i$ è un nodo corrotto che non fa nulla ogni volta che riceve un messaggio non ci sarebbe nessuno schedule che consenta agli altri $n − 1$ nodi di terminare.

Siccome $X_{i−1}$ è una configurazione $0$-valente, nella configurazione $\sigma(X_{i−1})$ tutti i nodi diversi
da $i$ devono dare in output $0$. Siccome le configurazioni $X_{i−1}$ e $X_i$ differiscono solo per l’input del nodo $i$ e lo schedule $\sigma$ non contiene messaggi per il nodo $i$, anche nella configurazione $\sigma(X_i)$ tutti i nodi diversi da i devono aver deciso che il loro output è 0. 

Quindi la configurazione iniziale $X_i$ non può essere $1$-valente e siccome non è neanche $0$-valente per costruzione, deve essere bivalente. $\blacksquare$ 