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

>[!teorem]- Legge **debole** dei grandi numeri
>Sia $\{X_{i}\}_{i=1,\dots,n}\sim$ i.i.d e $X_{n}=\frac{1}{n}\sum\limits_{i=1}^{n}X_i$Ipotizziamo $\mathbb E[X_n^{2}]\lt\infty$
>Allora $$X_{n}\to_{p}\mu=\mathbb E[X_i]$$

**dimostrazione**

$$Pr(|X_{n}-\mu|\gt\varepsilon)\underbrace{\leq}_{\text{Chebychev}}\frac{Var(X_{n})}{\varepsilon^2}=\frac{Var(X_{1})}{n\varepsilon^2}\to0\quad(1)$$
Però, **non serviva l'ipotesi i.i.d**, infatti 
$$Var\left(\sum\limits_{i=1}^nX_i\right)=\sum\limits_{i=1}^nVar(X_{i})\quad(2)$$
Ma con l'ipotesi $\mathbb E[X_i]=0$ abbiamo che $$Var\left(\sum\limits_{i=1}^nX_i\right)=\mathbb E\left[\left(\sum\limits_{i=1}^nX_i\right)^{2}\right]=\sum\limits_{i_{1}}\sum\limits_{i_{2}}\mathbb E[X_{i_1}X_{i_2}]=\sum\limits_{i_{1}i_{2}}Cov(X_{i_1}X_{i_2})$$
Dove l'ultima uguaglianza vale perchè:
$$Cov(X_{i1},X_{i2})=\mathbb E[X_{i1}X_{i2}]-\mathbb E[X_{i1}]\mathbb E[X_{i2}]$$
Ma per ipotesi abbiamo detto che $\mathbb E[X_i]=0$ quindi possiamo dire che $$Cov(X_{i1},X_{i2})=\mathbb E[X_{i1}X_{i2}]$$
E quindi basta che siano **mutualmente indipendenti**

**Non serve neanche che abbiano stessa varianza**, infatti la legge vale anche se $$Var(X_i)=i^{\alpha},\alpha\lt1$$
e di conseguenza, otteniamo che 
$$Var(X_{n})=\frac{1}{n^{2}}\sum\limits_{i=1}^{n}Var(X_{i})=\frac{1}{n^{2}}\sum\limits_{i=1}^{n}i^\alpha=\frac{n^{\alpha-1}}{\alpha+1}\quad(3)$$

**Non serve neanche che le v.a siano mutualmente indipendenti, ma basta che** : $$\mathbb E\left[\left(\sum\limits_{i=1}^nX_i\right)^{2}\right]=o(n^2)\quad(4)$$
Tornando a $(1)$, in realtà abbiamo dimostrato la convergenza in media quadratica, che è più forte della convergenza in probabilità, infatti abbiamo dimostrato che $$\mathbb E[(X_{n}-\mu)^2]\to0$$
Vediamo l'altro esempio
## Esempio 2 (Legge forte dei grandi numeri)

Prima di parlare di questo, richiamiamo il **teorema di Kolmorogov**

>[!teorem]- Kolmorogov
>Siano $X_1,\dots,X_n\sim$ i.i.d con $\mathbb E[X_i]=\mu$
>Allora $$\frac{1}{n}\sum\limits_{i=1}^{n}X_i\to_{q.c}\mu$$

Vediamo ora la legge **forte** dei grandi numeri

>[!teorem]- Legge forte dei grandi numeri
>Siano $X_{i}\sim$ i.id con $\mathbb E[X_i]=\mu$ e $\mathbb E[X_{i}^4]\lt\infty$ (per semplicità della dimostrazione)
>Allora $$X_{n}=\frac{1}{n}\sum\limits_{i=1}^nX_i\to_{c.c}\mu$$

**dimostrazione**

Per prima cosa, prendiamo $\mu=0$

Dobbiamo dimostrare che $$\sum\limits_{n=1}^\infty Pr(|X_n|\gt\varepsilon)\lt\infty$$
Quindi, possiamo riscrivere
$$Pr(|X_n|\gt\varepsilon)=Pr(|X_n|^{4}\gt\varepsilon^{4})\leq\frac{\mathbb E[X_{n}^4]}{\varepsilon^2}$$
Ora quello che dobbiamo dimostrare è che quella quantità deve essere $O\left(\frac{1}{n^2}\right)$

Calcoliamo quindi $\mathbb E[X_n^{4}]$

$$\begin{align*}
\mathbb E[X_n^{4}]&=\mathbb E\left[\left(\frac{1}{n}\sum\limits_{i=1}^nX_i\right)^{4}\right]\\&=\frac{1}{n^4}\mathbb E\left[\left(\sum\limits_{i=1}^nX_i\right)^{4}\right]\\&=\frac{1}{n^4}\mathbb E\left[\sum\limits_{i_{1}=1}^n\sum\limits_{i_{2}=1}^n\sum\limits_{i_{3}=1}^n\sum\limits_{i_{4}=1}^nX_{i_{1}}X_{i_{3}}X_{i_{3}}X_{i_{4}}\right]\\&=\frac{1}{n^4}\left(\sum\limits_{i_{1}=1}^n\sum\limits_{i_{2}=1}^n\sum\limits_{i_{3}=1}^n\sum\limits_{i_{4}=1}^n\mathbb E[X_{i_{1}}X_{i_{3}}X_{i_{3}}X_{i_{4}}]\right)\\&=\frac{1}{n^{4}}(n\cdot\mathbb E[\underbrace{X_1^{4}}_{\text{perchè }X_i\sim\text{i.i.d}}]+\underbrace{3n(n-1)}_{\text{fisso una v.a, e posso accoppiarla con una delle 3 rimanenti, per n(n-1) volte}}(\mathbb E[X_{1}^2])^2)\\&=O\left(\frac{1}{n^{3}}+ \frac{3}{n^{2}}\right)=O\left(\frac{1}{n^{2}}\right)\quad\blacksquare\\
\end{align*}$$

Abbiamo quindi dimostrato che $$\mathbb E[X_{n}^{4}]\sim \frac{3}{n^{2}}$$
In generale, se moltiplichiamo per $\sqrt{n}$ otteniamo che 
$$\begin{align*}
&\mathbb E[(\sqrt{n}X_{n})^{4}]\sim 3\quad\text{senza radice sarebbe }\frac{3}{n^{2}}\\&\mathbb E[(\sqrt{n}X_{n})^{6}]\sim 15\quad\text{senza radice sarebbe }\frac{15}{n^{3}}\\&\mathbb E[(\sqrt{n}X_{n})^{8}]\sim 105\quad\text{senza radice sarebbe }\frac{105}{n^{4}}\\&\vdots\\&\mathbb E[(\sqrt{n}X_{n})^{k}]\sim ris(\mathbb E[(\sqrt{n}X_{n})^{k-2}])\cdot(k-1)\quad\text{senza radice sarebbe }\frac{ris(\mathbb E[(X_{n})^{k-2}])\cdot(k-1)}{n^{\frac{k}{2}}}
\end{align*}$$

---
# Disuguaglianza di Jensen

>[!teorem]- Disuguaglianza di Jensen
>Sia $X:\Omega\to\mathbb R$ con $\mathbb E[X]\lt\infty$ e $f$ funzione convessa.
>Allora $$\mathbb E[f(X)]\geq f(\mathbb E[X])$$

per dimostrazione vedi appunti Salvi

Vediamo ora un esempio di applicazione della **disuguaglianza di Jenses**

Vediamo il caso in cui $r_2\gt r_1$

In questo caso, abbiamo che $$X_{n}\to_{r_{2}}X\implies X_{n}\to_{r_{1}}X$$
**dimostrazione**

$$\mathbb E[X_{n}-X]^{r_{1}}\to0\iff(\mathbb E[X_{n}-X]^{r_{1}})^{\frac{r_{2}}{r_{1}}}\to0\underbrace{\leq}_{\text{per Jensen}}\mathbb E\left([X_{n}-X]^{r_{1}\frac{r_{2}}{r_{1}}}\right)\to0$$



