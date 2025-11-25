# Efficienza degli stimatori ML

Per parlare di efficienza degli stimatori ML, osserviamo che la matrice di informazione è strettamente legata all'efficienza

introduciamo il concetto di **stimatori B.U.E**

>[!definition]- Stimatori B.U.E (Best Unbiased Estimator)
>Uno stimatore si dice B.U.E se vale la non distorsione (ovvero $\mathbb E[T_{n}]=\theta_{0}$) e per ogni altro stimatore $T_{n}^{'}:\mathbb E[T_{n}^{'}]=\theta_{0}$ allora vale che $$Var(T_{n})\leq Var(T_{n}^{'})$$

Vediamo subito il seguente lemma

>[!teorem]- Lemma 1
>Se esiste lo stimatore B.U.E, allora lui è unico.
>In altre parole, non esistono due stimatori B.U.E in contemporanea

**dimostrazione lemma 1**

Assumiamo che esistano altri due stimatori B.U.E oltre a $T_n$, ovvero $T_{n}^{'},T_{n}^{''}$
Riscriviamo quindi $T_{n}^{''}=\alpha T_{n}+(1-\alpha)T_{n}^{'}$ (se $\alpha\in[0,1]$ allora è non distorto)
Dove sta l'assurdo? L'assurdo sta nel fatto che, come vedremo, la varianza di $T_{n}^{''}$ potrebbe essere più piccola di quella di $T_{n}^{'},T_{n}$

Calcoliamo la varianza di $T_{n}^{''}$:
$$\begin{align*}
Var(T_{n}^{''})&=\alpha^{2}Var(T_{n})+(1-\alpha)^{2}Var(T_n^{'})+2\alpha Cov(T_{n},T_{n}^{'})\\
(Var(T_{n})=Var(T_{n}^{'})=\sigma^{2})&=\sigma^{2}(\alpha^{2}+(1-\alpha)^{2})+2\alpha(1-\alpha)^{2}Cov(T_{n},T_{n}^{'})\\
\text{Per Cauchy-Schwartz}&=\sigma^{2}\left(\overbrace{\alpha^{2}+(1-\alpha)^{2}+2\alpha(1-\alpha)}^{=1}\underbrace{\frac{Cov(T_{n},T_{n}^{'})}{\sqrt{Var(T_{n})Var(T_{n}^{'})}}}_{\star}\right) 
\end{align*}$$
Ora, se $(\star)$ fosse $\lt1$, allora tutto il calcolo verrebbe $\lt1$, e di conseguenza risulterebbe che $T_n^{''}$ migliore sia di $T_n$ che $T_{n}^{'}$, ma questo è **assurdo** perchè per ipotesi $T_n$ è B.U.E
## Limite inferiore di Cramer-Rao



---
# Statistiche Sufficienti
