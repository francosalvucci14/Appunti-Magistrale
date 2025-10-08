# Disuguaglianze

Recap sulla **disuguaglianza di Markov**

>[!teorem]- Markov
>Sia $X\geq0$ allora $$Pr(X\geq c)\leq\frac{\mathbb E[X]}{c}$$

**dimostrazione**

$$Pr(X\geq c)\equiv\mathbb E[\mathbb 1_{[c,\infty)}(X)]\leq\mathbb E\left[\frac{X}{c}\mathbb 1_{[c,\infty)}(X)\right]\leq\frac{\mathbb E[X]}{c}\quad\blacksquare$$

Recap su **Chebychev**

>[!teorem]- Chebychev
>$X\geq0$ allora $$Pr(|X-\mathbb E[X]|\geq c)\leq\frac{Var(X)}{c^2}$$

**dimostrazione**

$$Pr(|X-\mathbb E[X]|\geq c)=Pr(|X-\mathbb E[X]|^{2}\geq c^{2})\underbrace{\leq}_{\text{Markov}}\frac{\mathbb E[|X-\mathbb E[X]|^2]}{c^2}=\frac{Var(X)}{c^{2}}\quad\blacksquare$$
Possiamo sfruttare queste disuguaglianze per dimostrare varie cose, vediamo alcuni esempi

## Esempio 1 (Legge debole dei grandi numeri)
