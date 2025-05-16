# Convergenza di grafi regolari

Abbiamo visto nella lezione precedente che il sistema converge a una configurazione $$\hat{x}^{(t)}\to\alpha_1\hat{u}_1=M$$
Le domande che ora ci poniamo sono : 
- Chi è $\alpha_1$?
- Chi è $\hat{u}_1$?

Per la definizione di autovettore dell'autovalore $\lambda_1=1$ dobbiamo avere che :
$$\hat{u}_1=P\cdot\hat{u}_1=\begin{bmatrix}\frac{1}{d_1}&0&\dots&\frac{1}{d_1}&0&\dots&\frac{1}{d_1}\\0&\frac{1}{d_2}&\dots&\frac{1}{d_2}&0&\dots&0\\0&0&\dots&\frac{1}{d_i}&\dots&\frac{1}{d_i}&0\\0&0&\dots&\frac{1}{d_n}&\dots&0&\frac{1}{d_n}\end{bmatrix}\cdot\begin{bmatrix}u_1(1)\\u_1(2)\\\dots\\u_1(i)\\\dots\\u_1(n)\end{bmatrix}$$
Consideriamo la convergenza norma 2. Così facendo, se abbiamo un generico $1-$autovettore $\hat{v}_1$, abbiamo bisogno di normalizzarlo per ottenere : $$\hat{u}_1=\frac{1}{||\hat{v}_1||_2}\cdot\hat{v}_1\quad(5)$$
In generale quindi, abbiamo che $$\hat{x}^{(t)}\to\alpha_{1}\hat{u}_{1}=\langle x,\hat{u}_1\rangle\hat{u}_1=\frac{1}{||\hat{v}_1||_2}\cdot\hat{v}_1\cdot\left(\sum\limits_jx(j)u_1(j)\right)\quad(7)$$Possiamo quindi derivare l'autovalore $\hat{v}_1$ mostrando la seguente affermazione

**Lemma 2.6** : 
Il vettore $\hat{y}=\left\langle\frac{d_1}{2m},\dots,\frac{d_n}{2m}\right\rangle$ è un $1-$autovettore destro della matrice $P^T=(D^{-1}A)^T=AD^{-1}$, ovvero $$P^T\hat{y}=\hat{y}$$
**dim**
Dato che $G$ è $d-$regolare, sappiamo che $\forall v\in V\to|N(v)|=d$

Calcoliamo quindi $$v^{(1)}(1)=Pv^{(1)}=\frac{1}{d}\sum\limits_{j\in N(i)}\frac{d}{2m}=\frac{1}{d}d\left(\frac{d}{2m}\right)=\frac{d^2}{d2m}=\frac{d}{2m}$$
Questa situazione vale per ogni entrata del vettore $\hat{v}$, e di conseguenza $$\hat{v}=\left\langle\frac{d_1}{2m},\dots,\frac{d_n}{2m}\right\rangle\quad\blacksquare$$
**Claim 2.7**
Un autovettore per $\lambda_1=1$ è il seguente $$\hat{v}^T=\left\langle\frac{d}{2m},\dots,\frac{d}{2m}\right\rangle$$
Dall'equazione $(7)$ otteniamo quindi : 
$$x^{(t)}\to\alpha_{1}u_{1}(i)=\frac{1}{\frac{nd^2}{4m^2}}\left(\sum\limits_{i}x(i)\frac{d}{2m}\right)\frac{d}{2m}=\frac{d^2/4m^2}{nd^2/4m^2}\sum\limits_jx(j)=\frac{\sum_jx(j)}{n}=\text{MEDIA}\quad(9)$$
Dove : 
- $\alpha_1=\langle x,\hat{u}_1\rangle$ 
- $\hat{u}_1(i)=\frac{1}{\frac{nd^2}{4m^2}}\frac{d}{2m}$

Quindi vale il seguente teorema

>[!teorem]- Teorema 2.8
>Se il grafo $G$ è connesso, non-bipartito e $d-$regolare, allora il protocollo **AVG-PROTOCOL** converge (in norma 2) a una configurazione stabile in cui ogni nodo ottiene, come suo valore, la media $\frac{\sum_jx(j)}{n}$ del vettore iniziale $\hat{x}$

# Tempo di convergenza del protocollo
