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

Ricordiamo che $\hat{\sigma}^{2}_{ML}=\frac{\hat\varepsilon^{T}\hat\varepsilon}{n}=\frac{(Y-X\hat\beta)^{T}(Y-X\hat\beta)}{n}$

Osserviamo prima di tutto che $\hat\varepsilon^{T}\hat\varepsilon=\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}\sim\sigma^{2}\chi_{n}^{2}$
Vediamo inoltre che $$\hat\varepsilon=Y-X\hat\beta=(I-X(X^{T}X)^{-1}X^{T})Y$$
Inolre, vale che 
$$\mathbb E[\hat\varepsilon]=\mathbb E[Y-X\hat\beta]=\overbrace{\mathbb E[Y]}^{=X\hat\beta}-\mathbb E[X\hat\beta]=0$$

Sostituendo $Y=X\hat\beta+\varepsilon$ otteniamo che
$$\hat\varepsilon=Y-X\hat\beta=(I-\underbrace{X(X^{T}X)^{-1}X^{T}}_{P_{X}})\varepsilon$$
Vale quindi il seguente lemma

>[!teorem]- Lemma su $\hat\varepsilon$
>$\hat\varepsilon\sim N(0,\sigma^{2}_{\varepsilon}(I-P_{X}))$ e $\mathbb E[(I-P_X)\varepsilon(I-P_{X})^{T}\varepsilon^{T}]=(I-P_{X})\sigma^{2}_{\varepsilon}$

Dimostriamo poi il seguente lemma, che ci dirà come si distribuisce lo stimatore della varianza $\hat\sigma^{2}_{ML}$

>[!teorem]- Distribuzione dello stimatore $\hat\sigma^{2}_{ML}$
>Lo stimatore $\hat{\sigma}^{2}_{ML}=\hat\varepsilon^{T}\hat\varepsilon=(Y-X\hat\beta)^{T}(Y-X\hat\beta)$ si distribuisce come $\sigma^{2}_{\varepsilon}\chi_{n-k}^{2}$
>Ovvero $$\hat\sigma^{2}_{ML}\sim\sigma^{2}_{\varepsilon}\chi_{n-k}^{2}$$
>
>Per semplicità eliminiamo la $n$ che dovrebbe stare al denominatore dello stimatore

**dimostrazione**

Prima di tutto, vediamo che possiamo scrivere $$(I-P_{X})=M_{X}\quad\text{vedi lezione scorsa}$$
E quindi otteniamo che 
$$\hat\varepsilon=(I-P_{X})^{T}\varepsilon^{T}\varepsilon(I-P_{X})=M_{X}^{T}\varepsilon^{T}\varepsilon M_{X}=M_{X}^{T}M_{X}\varepsilon^{T}\varepsilon=\varepsilon^{T}M_{X}\varepsilon$$
(Dove l'ultima uguaglianza è verificata perchè $M_{X}$ è simmetrica ed idempotente)

Ricordando poi la diagonalizzazione $M_{X}=Q\tilde{\Lambda}Q$, dove $\tilde{\Lambda}$ ha $n-k$ elementi pari ad "1" sulla diagonale principale e tutti gli altri pari a $0$, otteniamo che:
$$\begin{align*}
\varepsilon^{T}M_{X}\varepsilon&=\varepsilon^{T}Q\tilde{\Lambda}Q\varepsilon\\
(u\sim N(0,\sigma^{2}_{\varepsilon}I_{n}))&=u^{T}\tilde{\Lambda}u\\
&=\sum\limits_{i=1}^{n-k}u_{i}^{2}=\chi_{n-k}^{2}\quad\blacksquare
\end{align*}$$
Perchè queste uguaglianze sono verificate?
Perchè succede la seguente cosa:
$$X\sim N(\mu,\Sigma)\overbrace{\to}^{\text{molt. X per A(matrice o vett.)}} AX\sim N(A\mu,A\Sigma A^{T})$$
Nel nostro caso quindi otteniamo che 
$$\varepsilon\sim N(0,I)\to Q\varepsilon\sim N(0,QIQ^{T}=I)$$
Quindi, **se ho un vettore Gaussiano standard e lo ruoto, non succede nulla. Riottengo un'altra Gaussiana identica alla precedente**
Dato che vale questa cosa, posso riscrivere tranquillamente che $$Q^{T}\varepsilon=u,\varepsilon^{T}Q=u^{T}$$
# Stimatore GLS (Generalized Least Square)

Possiamo ora generalizzare il modello che abbiamo studiato sinora, immaginando che i residui $\varepsilon$ abbiano una struttura di dipendenza molto più complessa di variabili indipendenti

In particolare, ipotizziamo che $\mathbb E[\varepsilon\varepsilon^{T}]=\Omega$ con matrice positiva definita di rango (pieno) $n$

La funzione di verosimiglianza prende quindi la forma 
$$L(\beta;Y,X)=\frac{1}{(2\pi)^{n}}\frac{1}{\sqrt{det(\Omega)}}e^{-\frac{1}{2}\left[(Y-X\beta)^{T}\Omega^{-\frac{1}{2}}(Y-X\beta)^{T}\right]}$$
Potremmo procedere come il caso ordinario, ma c'è una strategia più semplice

La matrice $\Omega$ si può diagonalizzare come $\Omega=Q\Lambda_{\Omega}Q^{T}$, per qualche matrice ortonormale $Q$ che non corrisponde a quelle che abbiamo introdotto prima

Possiamo definire quindi $\Omega^{-\frac{1}{2}}=Q\Lambda_{\Omega}^{-\frac{1}{2}}Q^{T}$, con la proprietà che:
$$\begin{align*}
\Omega^{-\frac{1}{2}}\Omega\Omega^{-\frac{1}{2}}&=Q\Lambda_{\Omega}^{-\frac{1}{2}}Q^{T}Q\Lambda_{\Omega}Q^{T}Q\Lambda_{\Omega}^{-\frac{1}{2}}Q^{T}\\
&=Q\Lambda_{\Omega}^{-\frac{1}{2}}\Lambda_{\Omega}\Lambda_{\Omega}^{-\frac{1}{2}}Q^{T}\\
&=QQ^{T}\\
&=I_{n}
\end{align*}$$
Possiamo quindi definire il vettore $\tilde\varepsilon=\Omega^{- \frac{1}{2}}\varepsilon$, che ha matrice di varianza/covarianza pari all'identità
Quindi, possiamo riscrivere che
$$Y=X\beta+\varepsilon\to\Omega^{- \frac{1}{2}}Y=\Omega^{- \frac{1}{2}}X\beta+\Omega^{- \frac{1}{2}}\varepsilon\to\tilde{Y}=\tilde{X}\beta+\tilde{\varepsilon}$$
con 
- $\tilde{Y}=\Omega^{- \frac{1}{2}}Y$
- $\tilde{X}=\Omega^{- \frac{1}{2}}X$
- $\tilde\varepsilon=\Omega^{- \frac{1}{2}}\varepsilon$

Lo stimatore diventa quindi 
$$\tilde\beta_{GLS}=(\tilde{X}^{T}\tilde{X})^{-1}\tilde{X}\tilde{Y}=(X^{T}\Omega^{-1}X)^{-1}X\Omega^{-1}Y$$
che è uno stimatore **non distorto** con legge Gaussiana e matrice di varianza e covarianza pari a 
$$\mathbb E[(\tilde\beta_{GLS}-\beta)(\tilde\beta_{GLS}-\beta)^{T}]=\Omega^{-1}$$

**osservazione** (non serve per l'esame)

Lo stimatore GLS può essere visto come i coefficienti di proiezione su un sottospazioni generato dalle colonne di X quando la proiezione viene effettuata con una metrica *Riemanniana* [^1] indotta dalla matrice positiva definita $\Omega^{-1}$

[^1]: https://it.wikipedia.org/wiki/Variet%C3%A0_riemanniana
