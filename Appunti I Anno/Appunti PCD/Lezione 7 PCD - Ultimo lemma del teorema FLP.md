Continuo della dimostrazione del teorema di impossibilità FLP.

Ricordiamo che :

Dato un qualunque protocollo $\mathbb P_{BA}$, allora : 
1. $\exists$ un'assegnazione degli input tale che la configurazione iniziale $\mathbb C_0$ è bivalente
2. Se $\mathbb C$ è una configurazione bivalente, allora $\exists$ uno schedule $\sigma$ applicabile tale che $\sigma(\mathbb C)$ è anche lei bivalente

Nella lezione 6 abbiamo dimostrato il primo punto (lemma 1), ora invece dimostriamo il punto 2 (lemma 2)

>[!teorem]- Lemma 2
>Se $\mathbb P_{ba}$ è un protocollo deterministico per Byzantine Agreement che termina e soddisfa *validity* e *consistency*, $C = (S, M )$ è una configurazione bivalente per $\mathbb P_{ba}$ e $m = (p, x)$ è un messaggio in $M$ , allora esiste uno schedule $\sigma = (m_1 = (p_1, x_1), \dots , m_k = (p_k, x_k))$ applicabile a $C$ tale che : 
>1. $m_k=m$
>2. $p_i\neq p,\forall i=1,2,\dots,k-1$
>3. $\sigma(C)$ è una configurazione bivalente per $\mathbb P_{ba}$

**Dimostrazione**

Se $m(C)$ è bivalente, il lemma è dimostrato. Altrimenti $m(C)$ è $0$-valente o $1$-valente. 
Consideriamo il caso in cui $m(C)$ è $0$-valente; il caso in cui è $1$-valente è speculare.

Data una configurazione bivalente $\hat{C}$ per $\mathbb P_ba$, diciamo che $\hat{C}$ è di tipo $0^\star$ per il nostro messaggio $m$ se $m(\hat{C})$ è $0$-valente. Analogamente diciamo che $\hat{C}$ è di tipo $1^\star$ o $bi^\star$, se $m(\hat{C})$ è $1$-valente o bivalente, rispettivamente.

Siccome ci siamo posti, senza perdita di generalità, nel caso in cui $m(C)$ è $0$-valente, con
la terminologia appena definita possiamo dire che $C$ è una configurazione bivalente di tipo $0^\star$

Consideriamo tutte le configurazioni raggiungibili applicando a $C$ degli schedule che non contengono il nostro messaggio $m = (p, x)$. Osserviamo che fra queste configurazioni ce ne deve essere qualcuna che non è di tipo $0^\star$, perchè se fossero tutte di tipo $0^\star$ allora la configurazione $C$ non potrebbe che essere $0$-valente, invece è bivalente per ipotesi.

Indichiamo con $Y$ la prima configurazione non $0^\star$ raggiungibile applicando a $C$ uno schedule che non contiene il messaggio $m$, indichiamo con $X$ la configurazione di tipo $0^\star$ che la precede e con $m' = (p', x')$ il messaggio dello schedule che secondo il protocollo porta dalla configurazione $X$ alla configurazione $Y$

![[Pasted image 20250414104527.png|center|500]]

l nostro messaggio $m = (p, x)$ è applicabile alla configurazione $Y$, perchè stava nella message pool della configurazione $C$ e non è mai stato consegnato, quindi sta anche nella message pool di $Y$. 
Sia allora $Z = m(Y )$ la configurazione che si ottiene applicando $m$ a $Y$. Mostriamo che $Z$ è la configurazione bivalente che stiamo cercando, concludendo così la dimostrazione del lemma.

La configurazione $Z$ non può essere $0$-valente, altrimenti $Y$ sarebbe di tipo $0^\star$. 
Ora mostriamo che $Z$ non può essere neanche $1$-valente esibendo uno schedule applicabile a $Z$ che conduce a una configurazione in cui tutti i nodi onesti danno in output $0$.

Prima di tutto osserviamo che se $Z$ non è $0$-valente allora deve essere $p = p'$. 
Infatti, se fosse $p \neq p'$, la configurazione $Z$, che si ottiene da $X$ consegnando prima $(p', x')$ e poi $(p, x)$, sarebbe la stessa configurazione che si ottiene da $X$ consegnando prima $(p, x)$ e poi $(p', x')$ (vedi lezioni scorse), ma quest’ultima configurazione è sicuramente $0$-valente, perchè $X$ è di tipo $0^\star$.

Siccome $p = p'$ e siccome per ipotesi $\mathbb P_{ba}$ **termina anche in presenza di un nodo corrotto**, deve esistere uno schedule $\sigma$ applicabile a $X$ tale che $\sigma$ non contiene messaggi per il nodo $p$ e $X' := \sigma(X)$ è una configurazione in cui tutti i nodi diversi da $p$ che seguono il protocollo hanno deciso il loro output. 
Infatti, se un tale schedule non ci fosse, nel caso in cui p è un nodo corrotto che non fa
nulla ogni volta che riceve un messaggio, **nessuno schedule consentirebbe** agli altri $n − 1$ nodi di terminare.

Lo schedule $\sigma$ non contiene messaggi per il nodo $p$ quindi è applicabile anche alla configurazione $m(X)$ e, siccome $p' = p$, anche alla configurazione $Z$:

1. Siccome $\sigma(X)$ è una configurazione in cui tutti i nodi diversi da $p$ devono aver deciso il loro output, anche $m(\sigma(X))$ lo è. Ma quindi l’output deciso dai nodi deve essere $0$, perchè $m(\sigma(X)) = \sigma(m(X))$ e $m(X)$ è una configurazione $0$-valente dato che $X$ è di tipo $0^\star$
2. La configurazione $\sigma(Z) = \sigma(m(m'(X))) = m(m'(\sigma(X)))$ e siccome σ(X) è una configurazione in cui tutti i nodi diversi da $p$ hanno deciso che il loro output è $0$, anche $\sigma(Z)$ lo è.

Quindi abbiamo trovato uno schedule $\sigma$ applicabile a $Z$ tale che i nodi danno in output $0$.
Quindi $Z$ non può essere neanche $1$-valente e pertanto deve essere bivalente.

![[Pasted image 20250414105813.png|center|500]]

Usando ora i due Lemmi, possiamo dare la dimostrazione del teorema di impossibilità FLP

**Dimostrazione teorema FLP**

Supponiamo per assurdo che esista un protocollo deterministico $\mathbb P_{ba}$ che termina e soddisfa *validity* e *consistency* nel modello asincrono anche in presenza di un nodo corrotto. 
Per il Lemma 1 deve esistere una configurazione iniziale bivalente $C_0 = (S_0, M_0)$ per $\mathbb P_{ba}$. 

Per ogni $i \geq 1$, sia mi il messaggio "più vecchio" presente in $M_{i−1}$ (rompendo la simmeria arbitrariamente in caso di più messaggi), sia $\sigma_i$ lo schedule che termina con mi la cui esistenza è garanita dal Lemma 2 e sia $C_i = \sigma_i(C_{i−1})$ la configurazione bivalente risultante.

Lo schedule ($\sigma_1, \sigma_2, \sigma_3, \dots$) è quindi uno ***schedule infinito*** che garantisce che ogni messaggio
inserito nella **message pool** viene prima o poi consegnato e fa in modo che il protocollo rimanga sempre in configurazioni bivalente. $\blacksquare$

Il Teorema FLP afferma che nel modello asincrono non può esistere nessun protocollo deterministico per Byzantine Agreement in presenza di qualche nodo corrotto. Questo non esclude la possibilità che sia possibile progettare protocolli probabilistici.

