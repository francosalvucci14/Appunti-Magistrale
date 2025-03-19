# Ancora Cap 2

>[!definition]- Disuguaglianza di Jensen
>Consideriamo la varianza di una v.a., ovvero $$Var(X)\coloneqq\mathbb E[(X-\mathbb E[X])^2]\geq0$$
>Allora $$\begin{align}0\leq Var(X)&=\mathbb E[X^{2}-2\mathbb E[X]+\mathbb E[X]^{2}]\\\text{(per linearità)}&=\mathbb E[X^{2}]-\mathbb E[2\mathbb E[X]]+\mathbb E[\mathbb E[X]^{2}]\\&=\mathbb E[X^{2}]-2\mathbb E[X]\mathbb E[X]+\mathbb E[X]^{2}\\&=\mathbb E[X^{2}]-\mathbb E[X]^2\end{align}$$
>Quindi $$\mathbb E[X^{2}]\geq\mathbb E[X]^2$$

Estendiamo questa relazione a funzioni più generali : 

>[!definition]- Funzioni convesse
>$f:\mathbb R\to\mathbb R$ si dice **convessa** se $\forall x_1,x_2\in\mathbb R$ si ha che : $$\forall\lambda\in(0,1)\implies f(\lambda x_1+(1-\lambda)x_2)\leq \lambda f(x_1)+(1-\lambda)f(x_2)$$

**Oss** : Se $f$ ammette derivata seconda, $f$ è convessa $\iff f^{''}(x)\geq0,\forall x$

