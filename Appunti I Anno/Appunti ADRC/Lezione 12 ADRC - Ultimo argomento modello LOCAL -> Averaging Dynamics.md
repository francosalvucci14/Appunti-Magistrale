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

