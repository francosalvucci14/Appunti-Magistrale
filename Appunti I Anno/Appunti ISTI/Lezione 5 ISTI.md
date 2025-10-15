# Ancora su Disuguaglianze

## Disuguaglianza di Cauchy-Schwartz

La **disuguaglianza di Cauchy-Schwartz** è così definita

>[!definition]- Disuguaglianza di Cauchy-Schwartz
>Siano $X,Y:\Omega\to\mathbb R$ allora $$\mathbb E[|XY|]\leq\sqrt{\mathbb E[X^2]\mathbb E[Y^{2}]}$$
>Oppure $$-1\leq\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}\leq1$$

Questa disuguaglianza collega il discorso delle v.a con i vettori nello spazio vettoriale

**dimostrazione**

Consideriamo la funzione quadratica (in $\theta$)
$$R(\theta)=\mathbb E[(Y-\theta X)^{2}]=\mathbb E[Y^{2}]+\theta^{2}\mathbb E[X^{2}]-2\theta\mathbb E[XY]\geq0$$

L'equazione $R(\theta)=0$ ovviamente ammette al più una radice reale di molteplicità due, quindi il discriminante deve avere valore non-positivo, in particolare $$4(\mathbb E[XY])^2-4\mathbb E[X^{2}]\mathbb E[Y^{2}]\leq0$$
da cui segue la disuguaglianza di Cauchy-Schwartz $\blacksquare$
## Disuguaglianza di Minkowski

La **disuguaglianza di Minkowski** è così definita

>[!definition]- Disuguaglianza di Minkowski
>Prendiamo due vettori $X,Y$, allora vale che $$||X+Y||\leq||X||+||Y||\space(\text{siduguaglianza triangolare})$$
>In probabilità, definiamo $||X||=\sqrt{\mathbb E[X^{2}]}$, allora otteniamo che $$\sqrt{\mathbb E[(X+Y)^{2}]}\leq\sqrt{\mathbb E[X^{2}]}+\sqrt{\mathbb E[Y^{2}]}$$


**dimostrazione**

Dobbiamo calcolare $$\mathbb E[(X+Y)^{2}]=\mathbb E[X^{2}]+\mathbb E[Y^{2}]+
2\mathbb E[XY]\overbrace{\leq}_{\text{per Cauchy-Schwartz}}||X^{2}||+||Y^{2}||+2||X||||Y||=(||X||+||Y||)^{2}$$
Prendendo la radice ambo i membri otteniamo l'enunciato. $\blacksquare$
## Disuguaglianza di Hoeffding

La **disuguaglianza di Hoeffding** è così definita:

>[!definition]- Disuguaglianza di Hoeffding
>Siano $Y_{1},\dots,Y_{n}$ v.a indipendenti limitate fra $a_{i},b_{i}\in\mathbb R$, ovvero $a_i\leq Y_{i}\leq b_{i},\forall i=1,\dots,n$, aventi media nulla, ovvero $\mathbb E[Y_{i}]=0$
>Allora vale che $$Pr\left(\sum\limits_{i=1}^{n}Y_{i}\geq\varepsilon\right)\leq e^{-t\varepsilon}\prod_{i=1}^{n}e^{t^{2}\frac{(b_{i}-a_{i})^{2}}{8}},\space\forall t\geq0$$

Non faremo dimostrazione, ma vedremo come cambia la situazione usando Chernoff e/o Hoeffding

**Confronto fra Hoeffding e Chernoff**

Consideriamo una sequenza di v.a Bernoulliane di parametro $p=\frac{1}{2}$, con $n=100$ e $\varepsilon=0.2$

Se mettiamo a confronto le due disuguaglianze otteniamo che 
$$\begin{align*}
\text{Chernoff}\space&Pr(|\overline{Y}_{n}-p|\gt0.2)\leq\frac{Var(\overline{Y}_{n})}{\varepsilon^{2}}=\frac{1}{4n\varepsilon^{2}}\simeq0.0625\\\text{Hoeffding}\space&Pr(|\overline{Y}_{n}-p|\gt0.2)\leq2e^{-2\cdot100\cdot(0.2)^{2}}\simeq0.00067
\end{align*}$$

## Disuguaglianza di Gordon-Mill

La **disuguaglianza di Gordon-Mill** è così definita:

>[!definition]- Disuguaglianza di Gordon-Mill
>Sia $Z\sim N(0,1)$, allora vale che $$\frac{1}{\sqrt{2\pi}}\frac{t}{1+t^{2}}e^{-\frac{t^{2}}{2}}\leq Pr(Z\geq t)\leq\frac{1}{\sqrt{2\pi}}\frac{1}{t}e^{-\frac{t^{2}}{2}}$$

**dimostrazione**

Dimostriamo prima il limite superiore e poi quello inferiore

*Limite Superiore* : vale che 
$$
\begin{align*}
Pr(Z\geq t)&=\int_{t}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}dx\\&\leq\int_{t}^{\infty}\frac{1}{\sqrt{2\pi}}\frac{x}{t}e^{-\frac{x^{2}}{2}}dx\\&=\frac{1}{\sqrt{2\pi}}\int_{t}^{\infty}xe^{-\frac{x^{2}}{2}}dx\\\left(z=\frac{x^2}{2}\right)&=\frac{1}{\sqrt{2\pi}}\int_{\frac{t^{2}}{2}}^{\infty}e^{-z}dz\\&=\frac{1}{\sqrt{2\pi}}\frac{1}{t}e^{-\frac{t^{2}}{2}}
\end{align*}
$$

*Limite Inferiore* : vale che

