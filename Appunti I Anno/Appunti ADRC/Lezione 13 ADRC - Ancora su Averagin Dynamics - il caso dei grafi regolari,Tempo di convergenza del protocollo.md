# Convergenza di grafi regolari

Abbiamo visto nella lezione precedente che il sistema converge a una configurazione $$\hat{x}^{(t)}\to\alpha_1\hat{u}_1=M$$
Le domande che ora ci poniamo sono : 
- Chi è $\alpha_1$?
- Chi è $\hat{u}_1$?

Per la definizione di autovettore dell'autovalore $\lambda_1=1$ dobbiamo avere che :
$$\hat{u}_1=P\cdot\hat{u}_1=\begin{bmatrix}\frac{1}{d_1}&0&\dots&\frac{1}{d_1}&0&\dots&\frac{1}{d_1}\\0&\frac{1}{d_2}&\dots&\frac{1}{d_2}&0&\dots&0\\0&0&\dots&\frac{1}{d_i}&\dots&\frac{1}{d_i}&0\\0&0&\dots&\frac{1}{d_n}&\dots&0&\frac{1}{d_n}\end{bmatrix}\cdot\begin{bmatrix}u_1(1)\\u_1(2)\\\dots\\u_1(i)\\\dots\\u_1(n)\end{bmatrix}$$
Consideriamo la convergenza norma 2. Così facendo, se abbiamo un generico $1-$autovettore $\hat{v}_1$, abbiamo bisogno di normalizzarlo per ottenere : $$\hat{u}_1=\frac{1}{||\hat{v}_1||_2}\cdot\hat{v}_1\quad(5)$$
In generale quindi, abbiamo che $$\hat{x}^{(t)}\to\alpha_{1}\hat{u}_{1}=\langle x,\hat{u}_1\rangle\hat{u}_1=\frac{1}{||\hat{v}_1||_2}\cdot\hat{v}_1\cdot\left(\sum\limits_jx(j)u_1(j)\right)\quad(7)$$
# Tempo di convergenza del protocollo
