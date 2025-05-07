# Concetti base di algebra lineare

Norma finita standard di un vettore $\hat{x}=\langle x(1),\dots,x(n)=\rangle\in\mathbb R^n$ : 
$$\text{per ogni fissato }p\in\mathcal N:||\hat{x}||_{p}=\left(\sum\limits_{j}|x(j)|^{p}\right)^\frac{1}{p}$$
e $$||\hat{x}||_\infty=\max\{|x(j)|:j\in[n]\}$$
**Fatto 1.1** : Per ogni vettore $\hat{x}=\langle x(1),\dots,x(n)=\rangle\in\mathbb R^n$ vale che : $$||\hat{x}||_\infty\leq||\hat{x}||_2\leq||\hat{x}||_1\leq\sqrt{n}\cdot||\hat{x}||_2\leq n\cdot||\hat{x}||_\infty$$
# Il protocollo di Averaging

Consideriamo il seguente protocollo, chiamato *AVG-PROTOCOL* : 
- **Input** : Ogni nodo $i$ ha un valore iniziale, chiamato stato, $x(i)\in\mathbb R^{+}$
	- Sia $\hat{x}=\langle x(1),\dots,x(n)=\rangle^T$
- **Ad ogni round** $t\geq1$ ogni nodo $i$ **fa**:
	- **Pull** : il valore corrente $x(j)$ da ogni vicino $j\in N(i)$
	- **Update** : del proprio valore come $x^{'}(i)=\frac{1}{d_i}\sum\limits_{j\in N(i)}x(j)$

## Analisi del protocollo per Grafi Connessi $d$-regolari

Si può verificare immediatamente che vale il seguente Claim

**Claim 2.1** : La message complexity per round del protocollo è $\Theta(m)$

Ora, le domande principali che ci dobbiamo porre sono : 
1. I valori $x(i)$ convergono a un qualche valore $M$?
2. Se si, cos'è $M$? È la media globale di tutti i valori iniziali?
3. Quanto tempo ci vuole affichè il processo sia "vicino" a una configurazione stabile?

**oss** : la convergenza non viene riconosciuta dai nodi, mentre la terminazione viene riconosciuta da ogni nodo

Per il momento, non consideriamo la terminazione del processo, ma ci concentriamo solo sulla convergenza della sequenza temporale $\hat{x}^{(0)},\hat{x}^{(1)},\dots,\hat{x}^{(t)},\dots$ dove $\hat{x}^{(t)}=\langle x^{(t)}(1),\dots,x^{(t)}(n)\rangle^{T}\in\mathcal (R^+)^n$ è il vettore colonna rappresentante la configurazione del sistema al tempo $t$

Ora, sia $A\in Mat_{(n\times n)}$ la matrice di adiacenza di $G$ e sia $D^{-1}\in Mat_{(n\times n)}$ la matrice diagonale, con $$\begin{align}&A(i,j)=1\iff(i,j)\in E\\&D^{-1}(i,i)=\frac{1}{d_i}\space\forall i\in V\end{align}$$
Allora vale il seguente Claim

**Claim 2.2** : Per ogni round $t\geq1$, la configurazione del sistema al round $t$ soddisfa la seguente equazione : $$\hat{x}^{(0)}=\hat{x},\quad\hat{x}^{(t+1)}=(D^{-1}A)\hat{x}^{(t)}=D^{-1}\cdot(A\cdot\hat{x}^{(t)})\quad(1)$$
Inoltre, sia $P=D^{-1}A$ la matrice di transizione dle grafo $G$ (es. **Markov Chain**), allora : $$\hat{x}^{(0)}=\hat{x},\quad\hat{x}^{(t+1)}=P\hat{x}^{(t)}=P^t\hat{x}\quad(2)$$
**dim** : Per ogni $v\in V$, possiamo scrivere l'$i-$esima componente dell'equazione $1$ come : 
$$x^{(t+1)}(i)=\frac{1}{d_i}\cdot\sum\limits_{j=1}^{n}A(i,j)\cdot x^{(t)}(j)=\frac{\sum\limits_{j\in N(i)}x^{(t)}(j)}{d_i}\quad(3)$$
**Claim 2.3** : Assumiamo $G$ connesso e non-bipartito. Allora, l'insieme di **autovalori** di $P$ sono tutti reali e, scrivendoli in ordine decrescente, vale che : 
$$\langle\lambda_{1}=1,\lambda_{2}\lt1,\dots,\lambda_{n}\rangle\space|\lambda_{i}|\leq1,\forall i=1,\dots,n$$
L'algebra lineare ci permette di scrivere il vettore iniziale $\hat{x}$ come combinazione linare di basi *ortonormali* $\langle\hat{u_1},\hat{u_2},\dots,\hat{u_n}\rangle$ di autovalori di $P$, come segue : 
$$\hat{x}=\alpha_1\hat{u_1}+\alpha_2\hat{u_2}+\dots+\alpha_n\hat{u_n}$$
Con, $G$ è $d-$regolare,$P$ simmetrica e i vettori $\hat{u_i}$ sono mutualmente ortogonali e hanno norma $2$ pari a $||\hat{u_i}||_2=1$. Allora, applichiamo l'equazione $(2)$, ottenendo il seguente lemma

**Lemma 2.4** :
$$\begin{align}\hat{x}^{(t+1)}&=P^t\hat{x}^=\alpha_1\lambda_1\hat{u_1}+\alpha_2\lambda_2^t\hat{u_2}+\dots+\alpha_n\lambda_n^t\hat{u_n}\\\text{dato che }\lambda_1=1&=\alpha_1\hat{u_1}+\alpha_2\lambda_2^t\hat{u_2}+\dots+\alpha_n\lambda_n^t\hat{u_n}\end{align}\quad(4)$$
dove $\alpha_i=\langle \hat{x},\hat{u_i}\rangle$ sono le proiezioni dei vettori $\hat{x}$ originali lungo i vettori della base ortonormale. Vale anche che $|\alpha_i|=|\langle \hat{x},\hat{u_i}\rangle|\leq M=\sum\limits_jx(j)$


