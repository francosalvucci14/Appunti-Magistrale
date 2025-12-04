# Ancora su Modello Lineare Multivariato

Nella lezione 19 eravamo rimasti con due domande:
1. Come si distribuisce $\hat{\beta}_{ML}$
2. Come si distribuisce $\hat{\sigma}^{2}_{ML}$

Rispondiamo ad entrambe le domande:

**distribuzione di $\hat\beta_{ML}$** 

Ricordiamo che $Y=X\beta+\varepsilon$
Sostituiamo $Y$ nella formula di $\hat\beta$ ottenendo:
$$\hat\beta_{ML}=(X^{T}X)^{-1}X^{T}(X-\beta+\varepsilon)=\beta+(X^{T}X)^{-1}X^{T}\varepsilon$$
Da qui si deduce che $\hat\beta_{ML}$ è un vettore Gaussiano, perchè è trasformazione lineare di Gaussiane
Di conseguenza, otteniamo che 
$$\begin{align*}
\mathbb E[\hat\beta_{ML}]&=\beta\\
Var(\hat\beta_{ML})&=\mathbb E[(\hat\beta_{ML}-\beta)(\hat\beta_{ML}-\beta)^{T}]\\
&=\mathbb E[(X^{T}X)^{-1}X^{T}\varepsilon\cdot(X^{T}X)^{-1}X\varepsilon^{T}]=(X^{T}X)^{-1}\overbrace{\mathbb E[\varepsilon\varepsilon^{T}]}^{=\sigma^{2}I_{n}}(X^{T}X)^{-1}\\
&=\sigma^{2}(X^{T}X)^{-1}
\end{align*}$$

Vale quindi il seguente lemma

>[!teorem]- Lemma su $\hat\beta_{ML}$
>Vale che $\hat\beta_{ML}\sim N(\beta,\sigma^{2}(X^{T}X)^{-1})$

Vediamo ora per lo stimatore $\hat{\sigma}^{2}_{ML}$

**distribuzione di $\hat{\sigma}^{2}_{ML}$**

Ricordiamo che $\hat{\sigma}^{2}_{ML}=\frac{\hat\varepsilon^{T}\varepsilon}{n}=\frac{(Y-X\hat\beta)^{T}(Y-X\hat\beta)}{n}$

Osserviamo prima di tutto che $\hat\varepsilon^{T}\varepsilon=\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}\sim\sigma^{2}\chi_{n}^{2}$
Vediamo inoltre che $$\hat\varepsilon=Y-X\hat\beta=(I-X(X^{T}X)^{-1}X^{T}Y)$$
Inolre, vale che 
$$\mathbb E[\hat\varepsilon]=\mathbb E[Y-X\hat\beta]=\overbrace{\mathbb E[Y]}^{=X\hat\beta}-\mathbb E[X\hat\beta]=0$$


# Stimatore GLS (Generalized Least Square)