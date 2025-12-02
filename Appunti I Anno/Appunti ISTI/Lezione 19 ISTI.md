# Regressione / Modello lineare multivariato

Nella pratica, è estremamente comune la situazione in cui si cerchi di stimare la relazione esistente tra una particolare variabile (che chiameremo genericamente $Y$) ed un gruppo di altre (che chiameremo genericamente $X_1,\dots,X_k$ ), dove queste ultime sono considerate esplicative del comportamento della Y: Si tratta di un caso particolare di un ambito di ricerca al momento estremamente attivo, e che viene spesso indicato come **Supervise Learning**; in generale, lo studio di relazioni come $Y = f (X)$ va anche sotto il nome di Machine Learning o Statistical Learning. 

In questo corso, ci limiteremo a trattare il caso più comune, che è anche il più semplice; quello in cui assumiamo che $f (\cdot)$ abbia una forma lineare in un vettore di parametri $\beta$: In particolare, supponiamo che valga la seguente relazione, per $i = 1, 2,\dots, n :$
$$y_{i}=x_{1i}\beta_{1}+x_{2i}\beta_{2}+\dots+x_{ki}\beta_{k}+\varepsilon_{i}$$
dove le variabilin $\varepsilon_{i}$ sono considerate dei "residui" o "errori" e catturano tutto quello che non è spiegato dalla relazione lineare fra $y,x$.

In forma matriciale, possiamo scrivere: 
$$\overline{Y}=\overline{X}\beta+\overline{\varepsilon}$$
dove:
- $\overline{Y}$ è un vettore $n\times1$ della forma $\overline{Y}=(y_{1},\dots,y_{n})^{T}$
- $\overline{X}$ è una matrice $n\times k$ le cui colonne sono costituite da $(x_{j1},\dots,x_{jn})^{T}$
- $\overline{\varepsilon}$ è un vettore di residui

Iniziamo supponendo che si tratti di residui Gaussiani, ovvero con valore medio nullo e matrice di varianza/covarianza $\mathbb E\left[\overline{\varepsilon}\overline{\varepsilon}^{T}\right]=\Omega$; ovvero $$\overline{\varepsilon}\sim N(\overline{0},\sigma^{2}I_{n})$$
Comunemente la prima colonna di $\overline{X}$ viene scelta come il vettore di costanti $(1,\dots,1)$; così. ad esempio per $k=2$ otteniamo:
$$y_{i}=\beta_{1}+\beta_{2}x_{i}+\varepsilon_{i}$$

Prima di procedere però, dobbiamo imporre due condizioni per la matrice $\overline{X}$:
- **cond 1**: Le variabili $\overline{X}$ sono deterministiche ($k\lt n$ credo)
- **cond 2**: Il rango della matrice è esattamente $k$ ($Rg(X)=k$)

Ambedue le condizioni possono essere rimosse ed e¤ettivamente lo sono nella ricerca più recente; si tratta però di ipotesi semplificatrici che costituiscono un punto di partenza naturale. 
Si noti che questa condizione implica immediatamente $k\leq n$; questa ipotesi in particolare viene abbandonata negli studi più recenti (high-dimensional statistics/big data).

Vediamo ora quanto vale lo stimatore di massima verosimiglianza in questo modello.

>[!teorem]- Stimatore di ML nel modello 
>Lo stimatore ML in questo modello assume la seguente forma:
>$$\begin{align*}&\hat{\beta}_{MLE}=(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}\\&\hat{\sigma}^{2}_{MLE}=\frac{1}{n}(\hat{\varepsilon}^{T}\hat{\varepsilon})\end{align*}$$
>
>Dove $\hat{\varepsilon}=\overline{Y}-\hat{Y}=\overline{Y}-\overline{X}\hat{\beta}$

Si ha inoltre che:
$$\begin{align*}
&\hat{\beta}_{MLE}=^{d}N(\beta,\sigma^{2}(\overline{X}^{T}\overline{X})^{-1})\\
& n\times\frac{\hat{\sigma}^{2}_{MLE}}{\hat{\sigma}^{2}}=^{d}\chi_{n-k}^{2}
\end{align*}$$
**dimostrazione risultato**

>ricordiamo che vogliamo stimare $\\beta$, che è un vettore di dimensione $k\times 1$

Notiamo innanzitutto che la funzione di verosimiglianza prende la forma 
$$
\begin{align*}
L(\beta,\sigma^2;\overline{Y},\overline{X})&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}}\\
&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}\langle\overline{Y}-\overline{X}\beta,\overline{Y}-\overline{X}\beta\rangle}\\
&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)}
\end{align*}
$$

Le ultime uguaglianze valgono perchè $\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}$ in termini geometrici lo possiamo rappresentare come $\langle\varepsilon,\varepsilon\rangle=||\varepsilon||^{2}\text{ oppure }\varepsilon^{T}\varepsilon,\varepsilon=\overline{Y}-\overline{X}\beta$ 

Passando alla $\log L$ otteniamo:
$$\begin{align*}
\log L(\beta,\sigma^{2};\overline{Y},\overline{X})=- \frac{n}{2}\log(2\pi)- \frac{n}{2}\log(\sigma^{2})- \frac{1}{2\sigma^{2}}(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)
\end{align*}$$
A questom punto, notiamo che $(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)$ lo possiamo riscrivere come:
$$
\begin{align*}
(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)&=\overline{Y}^{T}\overline{Y}-\underbrace{\overline{Y}^{T}\overline{X}\beta-\beta^{T}\overline{X}^{T}\overline{Y}}_{\text{uguali, uno è la trasposta dell'altro}}+\beta^{T}\overline{X}^{T}\overline{X}\beta\\
&=\overline{Y}^{T}\overline{Y}-2\overline{Y}^{T}\overline{X}\beta+\beta^{T}\overline{X}^{T}\overline{X}\beta
\end{align*}
$$
A questo punto, il calcolo del gradiente (per il parametro $\beta$ con $\nabla$, per $\sigma^{2}$ con der. parziale) ci da come risultato:
$$\begin{align*}
\nabla_{\beta}\log L(\beta,\sigma^2;\overline{Y},\overline{X})&=\nabla_{\beta}\overline{Y}^{T}\overline{Y}-2\overline{Y}^{T}\overline{X}\beta+\beta^{T}\overline{X}^{T}\overline{X}\beta\\
&=\overline{0}-2\overline{X}^{T}\overline{Y}+2\overline{X}^{T}\overline{X}\beta\\
\left(\frac{\partial\log L}{\partial \sigma^{2}}\right)&=- \frac{n}{2\sigma^{2}}+ \frac{1}{2\sigma^{4}}(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)
\end{align*}$$
Impostando poi queste quantità uguali a 0, otteniamo
$$\begin{align*}
&\hat{\beta}_{MLE}=(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}\\
&\hat{\sigma^{2}}_{MLE}=\frac{1}{n}(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)=\frac{1}{n}(\hat\varepsilon^{T}\hat\varepsilon)
\end{align*}$$
Che è proprio quello detto in precedenza $\blacksquare$

**osservazione**:

Lo stimatore $\hat\beta_{MLE}$ è anche noto come **stimatore OLS** (Ordinary Least Squares)
## Il rapporto con i teoremi di proiezione

Lo stimatore di massima verosimiglianza nel modello lineare multivariato si presta ad una importante interpretazione usando gli strumenti dell’algebra lineare. 

In particolare, notiamo che il valor medio di $\overline{Y}$ dato $\overline{X}$ è dato da $E[\overline{Y}] =\overline{X}\beta$ ; il valore di è ignoto, ma è naturale definire il valore $\hat{Y} := \overline{X}\hat{\beta}$ come il valore "previsto" per il vettore $\overline{Y}$ sulla base delle stime $\hat{\beta}$ e del valore dei regressori $\overline{X}$.

Analogamente, il vettore degli "errori" $\varepsilon=\overline{Y}-\overline{X}\beta$ si può stimare come $\hat\varepsilon=\overline{Y}-\overline{X}\hat\beta$ 
Notiamo ora che
$$\begin{align*}
\hat{Y}&:=\overline{X}\hat\beta=X(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}=P_{\overline{X}}\overline{Y}\\
P_{\overline{X}}&:=\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}
\end{align*}$$
È immediato verificare che $P_{\overline{X}}$ è una **matrice di proiezione**, cioè simmetrica ed idempotente; infatti:
$$P_{\overline{X}}^{2}=\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}=\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{Y}$$
In particolare, l'azione della matrice $P_{\overline{X}}$ (che ha dimensione $n\times n$) corrisponde a proiettare il vettore $\overline{Y}$ sullo spazio vettoriale (**span**) di dimensione $k$ generato dalle colonne di $\overline{X}$ (ricordiamo che queste colonne sono linearmente indipendenti per ipotesi)

Analogamente, abbiamo che :
$$\begin{align*}
\hat\varepsilon&=\overline{Y}-\overline{X}\hat\beta=M_{\overline{X}}\overline{Y}\\
M_{\overline{X}}&=\overline{I}-P_{\overline{X}}=\overline{I}-\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}
\end{align*}$$
Anche $M_{\overline{X}}$ è simmetrica ed idempotente:
$$M_{\overline{X}}=(\overline{I}-P_{\overline{X}})^{2}=\overline{I}-2P_{\overline{X}}+P_{\overline{X}}^{2}=\overline{I}-2P_{\overline{X}}+P_{\overline{X}}=M_{\overline{X}}
$$

In particolare, l'azione di $M_{\overline{X}}$ consiste nel proiettare $\overline{Y}$ nello spazio ortogonale a quello generato dalle colonne di $\overline{X}$
Questo ha alcune conseguenze importanti;si ha infatti che 
$$M_{\overline{X}}P_{\overline{X}}=P_{\overline{X}}M_{\overline{X}}=\textbf{0}$$
dove con $\textbf{0}$ intendiamo la matrice $n\times n$ costituita da tutti zeri.
Come ulteriore conseguenza notiamo che 
$$\overline{X}^{T}\hat\varepsilon=0$$
ed in particolare, il vettore dei residui stimati è ortogonale a qualsiasi vettore che giacca nello spazio generato dalle colonne di $\overline{X}$

Possiamo ora enunciare le seguenti ulteriori proprietà delle matrici $M_{\overline{X}},P_{\overline{X}}$

>[!teorem]- Lemma
>Le matrici $P_{\overline{X}},M_{\overline{X}}$ hanno tutti autovalori pari a zero o uno e rango $k,n-k$ rispettivamente

**dimostrazione**

Poichè le matrici sono reali e simmetriche, possiamo diagonalizzarle come:
$$\begin{align*}
&P_\overline{X}=Q\Lambda Q^{T},\quad QQ^{T}=Q^{T}Q=I_{n}\\
&\Lambda=\begin{pmatrix}\lambda_{1}&0&\dots&0\\0&\lambda_{2}&\dots&0\\\dots&0&\dots&0\\0&\dots&0&\lambda_{n}\end{pmatrix}
\end{align*}$$
Si ha allora che 
$$P_\overline{X}^{2}=Q\Lambda Q^{T}Q\Lambda Q^{T}=Q\Lambda^{2}Q^{T}=Q\Lambda Q^{T}$$
da cui segue necessariamente $\lambda_{i}=0,1$ per $i=1,2,\dots,n$; ragionamento identico si applica al $M_{\overline{X}}$

Per quello che riguarda il rango, notiamo che esso eguaglia il numero di autovalori diversi da zero (con molteplicità), quindi nel caso di matrici di proiezioni la traccia  (cioè la somma di autovalori, uguale al numero di quelli che valgono $1$)
Ricordando che $Tr(AB)=Tr(BA)$, possiamo scrivere
$$Tr(P_\overline{X})=Tr\left(\overline{X}(\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\right)=Tr\left((\overline{X}^{T}\overline{X})^{-1}\overline{X}^{T}\overline{X}\right)=Tr(I_{k})=k=Rg(P_\overline{X})$$
La dimostrazione per $M_{\overline{X}}$ è identica $\blacksquare$

