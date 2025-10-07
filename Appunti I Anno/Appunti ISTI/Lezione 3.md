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

## Esempio 1

Sia $X_n$ con $\mathbb E[X_n]=0$ allora è sempre vero che $$X_{n}=O_p\left(\sqrt{Var(X_n)}\right)$$
## Esempio 2

Prendiamo $$Z_n=\begin{cases}1& \frac{1}{2}\\-1& \frac{1}{2}\end{cases},\quad X_n=\sum\limits_{i=1}^{n}Z_i$$
Osserviamo che le $Z_i$ sono i.i.d, di conseguenza vale che $$Var(X_n)=\sum\limits_{i=1}^nVar(Z_i)$$
Osservando che le $Z_i\sim Rad(\frac{1}{2})\implies\mathbb E[Z_i]=0,Var(Z_i)=1$ ($Z_i$ sono delle **Rademarcher**)

Usando quindi precedente otteniamo che $$X_{n}=O_{p}(\sqrt{n})\quad(1)$$
Se invece prendiamo $$\overline{X_n}=\frac{1}{n}\sum\limits_{i=1}^{n}Z_{i}$$
Allora otteniamo che:
$$\overline{X_n}=O_p\left(\frac{1}{\sqrt{n}}\right)\quad(2)$$
(Questo perchè la $Var(\overline{X_n})=\frac{1}{n}$)

Se invece prendiamo $$\tilde{X_n}=\frac{1}{\sqrt{n}}\sum\limits_{i=1}^nZ_i\implies\tilde{X_n}\to_dN(0,1)(\text{Normale, Gaussiana})\quad(3)$$
Prendiamo la somma di v.a
- Se lasciate da sole esplodono, quindi otteniamo il caso $(1)$
- Se moltiplichiamo per $\frac{1}{n}$ otteniamo la **legge dei grandi numeri**, quindi il caso $(2)$
- Se moltiplichiamo per $\frac{1}{\sqrt{n}}$ otteniamo il **teorema del limite centrale**, quindi il caso $(3)$




[^1]: $X\geq0,Pr(X\geq c)\leq\frac{\mathbb E[X]}{c}$
