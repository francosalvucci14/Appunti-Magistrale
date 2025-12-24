# Continuo algebra degli S.O

Recap sull'algebra degli S.O

Vale il seguente lemma:

>[!teorem]- Lemma
>Sia $X_{n}:\Omega\to\mathbb R$ allora
>$$X_n=O_p\left(\mathbb E[X_n^{r}]^{\frac{1}{r}}\right),\quad\forall r\gt0$$

**Dim**

Usiamo Markov [^1]

Calcoliamo quindi 

$$Pr\left(\frac{X_n}{\mathbb E\left[X_n^r\right]^{\frac{1}{r}}}\geq c\right)\leq \frac{\mathbb E[X_n^r]}{(\mathbb E[X_n^r])^{\frac{1}{r}\cdot r}}\cdot\frac{1}{c^r}\leq \frac{1}{c^{r}}$$
Questa $c$ è arbitraria, quindi la posso prendere piccola quanto voglio per far sì che $\frac{1}{c^{r}}\leq\varepsilon\quad\blacksquare$  

Vediamo ora una carrellata di esempi riguardanti gli $O_p(\cdot)$

**esempio/lemma**

Sia $X_n$ con $\mathbb E[X_n]=0$ allora è sempre vero che $$X_{n}=O_p\left(\sqrt{Var(X_n)}\right)$$
## Esempio 1

Prendiamo $$Z_n=\begin{cases}1& \frac{1}{2}\\-1& \frac{1}{2}\end{cases},\quad X_n=\sum\limits_{i=1}^{n}Z_i$$
Osserviamo che le $Z_i$ sono i.i.d, di conseguenza vale che $$Var(X_n)=\sum\limits_{i=1}^nVar(Z_i)$$
Osservando che le $Z_i\sim Rad(\frac{1}{2})\implies\mathbb E[Z_i]=0,Var(Z_i)=1$ ($Z_i$ sono delle **Rademarcher**)

Usando quindi l'esempio precedente otteniamo che $$X_{n}=O_{p}(\sqrt{n})\quad(1)$$
Se invece prendiamo $$\overline{X_n}=\frac{1}{n}\sum\limits_{i=1}^{n}Z_{i}$$
Allora otteniamo che:
$$\overline{X_n}=O_p\left(\frac{1}{\sqrt{n}}\right)\quad(2)$$
(Questo perchè la $Var(\overline{X_n})=\frac{1}{n}$)

Se invece prendiamo $$\tilde{X_n}=\frac{1}{\sqrt{n}}\sum\limits_{i=1}^nZ_i\implies\tilde{X_n}\to_dN(0,1)(\text{Normale, Gaussiana})\quad(3)$$
Prendiamo la somma di v.a
- Se lasciate da sole esplodono, quindi otteniamo il caso $(1)$
- Se moltiplichiamo per $\frac{1}{n}$ otteniamo la **legge dei grandi numeri**, quindi il caso $(2)$
- Se moltiplichiamo per $\frac{1}{\sqrt{n}}$ otteniamo il **teorema del limite centrale**, quindi il caso $(3)$

Vediamo un'altro esempio
## Esempio 2

Prendiamo $\mathcal E_{i}\sim N[0,1]$ i.i.d e prendiamo $$X_{n}=\sum\limits_{i=1}^ni^{\alpha}\mathcal E_{i}\quad\alpha\in\mathbb R$$
Quello che dobbiamo calcolare ora è la varianza di $X_{n}$, infatti:
$$Var(X_n)=\sum\limits_{i=1}^{n}i^{2\alpha}\sim\frac{n^{2\alpha+1}}{2\alpha+1}$$
Ora, consideriamo $\beta=2\alpha$, e otteniamo che:
- per $\beta=1\implies\frac{n(n+1)}{2}\sim\frac{n^2}{2}$
- per $\beta=2\implies\frac{n(n+1)(2n+1)}{6}\sim\frac{n^3}{3}$
- per $\beta=3\implies(\frac{n(n+1)}{2})^2\sim\frac{n^4}{4}$

In generale, per ogni $\alpha\lt -\frac{1}{2}$ otteniamo
$$\sum\limits_{i=1}^n \frac{1}{i}\sim\log(n)$$
Vale quindi il seguente lemma

>[!teorem]- Lemma 
>Per ogni $\alpha\gt -\frac{1}{2}$ otteniamo che $$\sum\limits_{i=1}^{n}i^{2\alpha}\sim\frac{n^{2\alpha+1}}{2\alpha+1}$$

Quindi, possiamo dire che:
$$\begin{align*}
X_n=\sum\limits_{i=1}^ni^{\alpha}\mathcal E_i&\to O_{p}\left(n^{\alpha+ \frac{1}{2}}\right)\space\forall\alpha\gt- \frac{1}{2}\\&\to O_p(1)\space\forall\alpha\lt- \frac{1}{2}\\&\to O_p\left(\sqrt{\log(n)}\right)\space\alpha=-\frac{1}{2}
\end{align*}$$
---
# Seconda Parte : Teorema di Prohorov

Ricordiamo prima di tutto l'enunciato del **teorema di Prohorov**

>[!teorem]- Th. Prohorov
>Prendiamo $X_n$ come sempre, allora $$X_n=O_{p}(1)\implies\exists X_{nk}\to_{d}X$$

La domanda che ci poniamo è la seguente:

Se $X_n\to X$ in qualche senso (es. convergenza in prob, in distribuzione, etc..) allora **è vero che** $F(X_{n})\to F(X)$ nello stesso senso.

Per alcune convergenze questa cosa vale, ma per altre no, un esempio di queste è la **convergenza in media r-esima**

Per dirlo, prendiamo $$X_n=\begin{cases}0&1- \frac{1}{n^{2}}\\n& \frac{1}{n^{2}}\end{cases}$$
Così facendo, vale che $$\begin{align*}&X_n\to_p0\\&X_{n}\to_{c.c}0\end{align*}$$
In media $r$-esima non vale, e lo vediamo con il seguente esempio di $X_{n}^{3}$

$$X_{n}^{3}=\begin{cases}0&1- \frac{1}{n^{2}}\\ n^3& \frac{1}{n^{2}}\end{cases}\implies\mathbb E[(X_{n}-0)^{3}]=n\space\text{e quindi esplode}$$

Vale quindi il seguente lemma:

>[!teorem]- Lemma
>1) $X_{n}\to_pX$ e $g$ continua allora $g(X_n)\to_pg(X)$ (**Lemma di Slutzky**)
>2) $X_{n}\to_dX$ e $g$ continua allora $g(X_n)\to_dg(X)$ (**Continuos Mapping Theorem**)




[^1]: $X\geq0,Pr(X\geq c)\leq\frac{\mathbb E[X]}{c}$
