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

Prima di entrare nel dettaglio dell'analisi, dobbiamo chiarire quale nozione di convergenza per il processo di averaging e quale nozione di output locale dobbiamo considerare. 

Come si può osservare, nel codice di **AVG-PROTOCOL** non c'è nessuna regola di stop, nessun valore di output ritornato, e nessun criterio di stop.

Ricordiamo che stiamo assumendo che i nodi del sistema distribuito possono eseguire computazioni algebriche con precisione infinita.
Questo ovviamente non è realistico

Per ovviare a questo problema, aggiungiamo un nuovo paramentro di confidenza in input e un criterio di stop che ci permette di avere un piccolo errore nei valori calcolati-

Il nuovo protocollo è quindi : 
**AVG-PROTOCOL1**
- **Input** : Ogni nodo $i$ ha un valore iniziale, chiamato stato, $x(i)\in\mathbb R^{+}$ (Sia $\hat{x}=\langle x(1),\dots,x(n)=\rangle^T$) e un parametro di confidenza $\varepsilon\gt0$
- **Ad ogni round** $t\geq1$ ogni nodo $i$ **fa**:
	- **Pull** : il valore corrente $x(j)$ da ogni vicino $j\in N(i)$
	- **Update** : del proprio valore come $x^{'}(i)=\frac{1}{d_i}\sum\limits_{j\in N(i)}x(j)$
	- **Se** $x'(i)-x(i)\leq\varepsilon$ allora **return** $x'(i)$ e si **ferma**

Iniziamo ad analizzare il protocollo in un qualunque nodo fissato del sistema come segue.

Osserviamo che, dato che stiamo guardando al valore *locale* mantenuto da ogni nodo, dovremmo considerare la norma $||\cdot||_\infty$ che limita il valore **massimale** tra tutti i nodi

Per ogni istante di tempo $t\geq1$ vale che : 
$$\begin{align}\hat{x}^{(t+1)}-\hat{x}^{(t)}&=P^{t+1}\hat{x}-P^t\hat{x}\\&=\alpha_1\hat{u}_1-\alpha_1\hat{u}_1+(1+\lambda_2)\lambda_2^t\alpha_2\hat{u}_2+\dots+(1+\lambda_n)\lambda_n^t\alpha_n\hat{u}_n\\&=(1+\lambda_2)\lambda_2^t\alpha_2\hat{u}_2+\dots+(1+\lambda_n)\lambda_n^t\alpha_n\hat{u}_n\end{align}\quad(10)$$
Definiamo quindi $$\lambda=\max\{|\lambda_j|:j\geq2\},\lambda_\min=\{|\lambda_j|:j\geq2\}$$
e ricordiamo che dato che $G$ è connesso e non-bipartito allora vale che $$0\lt\lambda_\min\leq\lambda\lt1$$
Quindi, l'eq (10) implica che 
$$\begin{align}||\hat{x}^{(t+1)}-\hat{x}^{(t)}||_\infty&=||P^{t+1}\hat{x}-P^{t}\hat{x}||_\infty\\&\leq n(1-\lambda_\min)\lambda^{t}\alpha_n||\hat{u}_n||_\infty=n(1-\lambda_\min)\lambda^tM\end{align}\quad(11)$$
con $M=\sum\limits_jx(j)$ e osserviamo che, per ogni $i\in[n],\alpha_i\leq M$ 
Quindi ora possiamo vedere quanto grande deve essere $t$ in modo da ottenere l'ultimo "incremento" sufficientemente piccolo del valore di ogni nodo, ovvero : 
$$||\hat{x}^{(t+1)}-\hat{x}^{(t)}||_\infty\leq\varepsilon\quad(12)$$
Dall'eq. (11) sappiamo che il processo indotto dal protocollo **AVG-PROTOCOL1** fermerà ogni nodo entro $T$ rounds, tale che $T$ soddisfa : 
$$n(1-\lambda_\min)\lambda^TM\leq\varepsilon$$
e quindi $$\lambda^T\leq\frac{\varepsilon}{nM(1-\lambda_\min)}$$
Dato che $|\lambda|\lt1$, possiamo riscrivere l'equazione come : $$T\geq\log\left(\frac{nM(1-\lambda_\min)}{\varepsilon}\right)/\log\left(\frac{1}{\lambda}\right)$$
e dato che $|\lambda_\min|\lt1$, abbiamo che per ogni $$T\geq\log\left(\frac{nM}{\varepsilon}\right)/\log\left(\frac{1}{\lambda}\right)$$
vale l'eq. (12)

Abbiamo quindi dimostrato il seguente lemma

**Lemma 2.9** : 
Il processo indotto dal protocollo **AVG-PROTOCOL1** termina dopo $$T=\log\left(\frac{nM}{\varepsilon}\right)/\log\left(\frac{1}{\lambda}\right)$$
e quindi, il valore $x'(i)$ al round $T$ di ogni nodo $i$ sarà $\varepsilon-$vicina al valore $x(i)$ del round precedente.

>[!teorem]- Teorema 2.10
>Con input un grafo connesso,non-bipartito e $d-$regolare e un parametro di confidenza $\varepsilon\gt0$, il protocollo **AVG-PROTOCOL1** termina dopo $T=\log\left(\frac{nM}{\varepsilon}\right)/\log\left(\frac{1}{\lambda}\right)$ round. Inoltre, ogni nodo $i\in[n]$ ritorna un valore $x^{(T)}$ tale che $$\left|x^{(T)}(i)-\frac{\sum_jx(j)}{n}\right|\leq\varepsilon$$

**dim**
Dall'equazione $(11)$ sappiamo che $$\begin{align}||\hat{x}^{(t+1)}-\hat{x}^{(t)}||_\infty&=||P^{t+1}\hat{x}-P^{t}\hat{x}||_\infty\\&\leq n(1-\lambda_\min)\lambda^{t}\alpha_n||\hat{u}_n||_\infty\\&\leq n(1-\lambda_\min)\lambda^tM\\&\leq n\lambda^tM\end{align}\quad(13)$$
D'altra parte $$\begin{align}||\hat{x}^{(t)}-\alpha_1\hat{u}_1||_\infty&=||P^{t}\hat{x}-\alpha_1\hat{u}_1||_\infty\\&= \lambda_2^t\alpha_2\hat{u}_2+\dots+\lambda_n^t\alpha_n\hat{u}_n\\&\leq n\lambda^tM||\hat{u}_n||_\infty=n\lambda^tM\end{align}\quad(14)$$
Grazie al Lemma 2.9, e comparando le equazioni (13) e (14) possiamo affermare che quando il nodo $i$ ferma la sua computazione, dopo $T$ round, ottiene un valore tale che $$\left|x^{(T)}(i)-\alpha_{1}\hat{u}_{1}\right|=\left|x^{(t)}(i)-M/n\right|\leq n\lambda^tM\leq\varepsilon\quad\blacksquare$$
