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

Notiamo innanzitutto che la funzione di verosimiglianza prende la forma 
$$
\begin{align*}
L(\beta,\sigma^2;\overline{Y},\overline{X})&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}}\\
&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}\langle\overline{Y}-\overline{X}\beta,\overline{Y}-\overline{X}\beta\rangle}\\
&=\frac{1}{(2\pi\sigma^{2})^{\frac{n}{2}}}e^{-\frac{1}{2\sigma^{2}}(\overline{Y}-\overline{X}\beta)^{T}(\overline{Y}-\overline{X}\beta)}
\end{align*}
$$

Le ultime uguaglianze valgono perchè $\sum\limits_{i=1}^{n}\varepsilon_{i}^{2}$ in termini geometrici lo possiamo rappresentare come $\langle\varepsilon,\varepsilon\rangle=||\varepsilon||^{2}\text{ oppure }\varepsilon^{T}\varepsilon,\varepsilon=\overline{Y}-\overline{X}\beta$   
## Il rapporto con i teoremi di proiezione
