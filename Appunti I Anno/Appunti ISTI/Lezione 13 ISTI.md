# Dimostrazione Asintotica Gaussianità per MLE

Per dimostrare che per gli stimatori MLE valga l'asintotica Gaussianità, dobbiamo introdurre due concetti fondamentali, che sono le **condizioni di regolarità** e la **funzione punteggio**

>[!definition]- Condizioni di regolarità
>Le condizioni di regolarità sono le seguenti
>1. Le condizioni di consistenza
>2. Le osservazioni $X_{1},\dots,X_{n}$ sono i.i.d
>3. La log-verosimiglianza ammette due derivate continue, quindi $\frac{\partial^{2}\log L_{n}}{\partial\theta^2}\in C^{2}$
>4. La derivata seconda ha momento secondo finito, ovvero $\mathbb E\left[\left(\frac{\partial^{2}\log L_{n}}{\partial\theta^2}\right)^{2}\right]\lt\infty$
>5. Il vero valore del parametro $\theta_{0}$ appartiene all'interno dell'insieme dei valori ammissibili, ovvero $\theta_{0}\in Int(\Theta)$
>6. È possibile scambiare due volte la derivata con l'integrale nel valor medio della log-verosimiglianza

Definiamo ora la funzione punteggio

>[!definition]- Funzione Punteggio
>La funzione punteggio è definita da $$s_{n}(\theta;X_{i},\dots,X_{n})=\frac{\partial}{\partial\theta}\log L(\theta;X_{1},\dots,X_{n})$$
>Assumiamo ovviamente che la derivata esista.
>In generale, la funzione punteggio è una funzione che va da $\mathbb R^{p}$ in $\mathbb R^{p}$, ovvero $$s_{n}:\mathbb R^{p}\to\mathbb R^{p}$$

Una volta definite le precedenti quantità, possiamo andare avanti

Vale quindi il seguente lemma

>[!teorem]- Lemma 1
>Sotto le condizioni di regolarità, vale che $$\mathbb E_{\theta_{0}}[s_{n}(\theta;X_{i},\dots,X_{n})]=0$$
>Dove con $\mathbb E_{\theta_{0}}$ indichiamo $\mathbb E[\cdot]\big|_{\theta=\theta_{0}}$

**dim** ($p=1$)
$$\begin{align*}
0&=\frac{\partial}{\partial\theta}1=\frac{\partial}{\partial\theta}\int_{\mathbb R}f(x;\theta)dx\underbrace{=}_{\text{swap der. e int.}}\int_{\mathbb R}\frac{\partial}{\partial\theta}f(x;\theta)dx=\int\overbrace{\frac{\frac{\partial}{\partial\theta}f(x;\theta)}{f(x;\theta)}}^{=\frac{\partial}{\partial\theta}\log(f(x;\theta))}f(x;\theta)dx\\&=\mathbb E\left[{\frac{\partial}{\partial\theta}\log(f(x;\theta))}\right]=\mathbb E[s_{n}(\theta)]\quad\blacksquare
\end{align*}
$$

**Esempio**

Sia $X\sim N(\mu,1)$, la sua funzione di densità è $\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}(X-\mu)^{2}}$

La log-verosimiglianza è $\log L=-\frac{1}{2}\ln(2\pi)-\frac{1}{2}(X-\mu)^{2}$

La derivata rispetto a $\mu$ risulta essere 
$$\sum\limits_{i=1}^{n}(X_{i}-\mu)=s_{n}$$
Applicando il valor medio, e calcolandolo nel punto $\mu=\mu_{0}$ otteniamo quanto detto dal lemma
$$\mathbb E[s_{n}]=n(\mu-\mu_{0})|_{\mu=\mu_0}=0$$

Vale anche il seguente lemma 

>[!teorem]- Lemma 2
>Sotto le condizioni di regolarità, vale che (sempre con $p=1$) $$\mathbb E\left[\left(\frac{\partial\log L}{\partial\theta}\right)^{2}\right]=-\mathbb E\left[\frac{\partial^{2}\log L}{\partial\theta^{2}}\right]$$
>Se $p\gt1$ otteniamo che 
>$$\mathbb E[(\nabla\log L)(\nabla\log L)^{-1}]=-\mathbb E[\mathcal H\log L]$$
>dove $\mathcal H$ è definita essere la **matrice Hessiana** [^1]
>In qualunque caso, ovvero sia $p=1$ che $p\gt1$, sia la derivata secoda che l'Hessiana sono dette **matrice di informazione**

**dim**
$$\frac{\partial}{\partial\theta}0=0=\frac{\partial}{\partial\theta}\int\frac{\partial\log L}{\partial\theta}f(x;\theta)dx=\int\frac{\partial^2\log L}{\partial\theta^{2}}f(x;\theta)dx+\int\frac{\partial\log L}{\partial\theta}\frac{\partial}{\partial\theta}f(x;\theta)dx$$
Ora, moltiplicando e dividendo a dx e sx per $f(x;\theta)$ il secondo integrale concludiamo la dimostrazione $\blacksquare$

**oss**

Osserviamo quanto segue, in $\theta=\theta_{0}$ abbiamo che $$\int\frac{\partial^2\log L}{\partial\theta^{2}}f(x;\theta_{0})dx=\mathbb E[(s_{n}(\theta_{0}))^2]=Var(s_{n}(\theta_{0}))$$
La varianza della funzione punteggio calcolata nel vero valore del parametro è pertanto uguale al reciproco della derivata seconda della log-verosimiglianza nello stesso punto.

Diamo anche quest'altra mini-definizione

>[!definition]- Informazione di Fisher
>La varianza della funzione punteggio è nota come **informazione di Fisher** e si indica con $I_{n}(\theta_{0})$
>In generale, è una matrice di dimensione $p\times p$

Vediamo ora il teorema che ci garantisce l'asintotica Gaussianità degli stimatori MLE

>[!teorem]- Teorema
>Sotto le condizioni di regolarità, vale che 
>$$\sqrt{n}(\hat{\theta}_{ML}-\theta_{0})\to_{d} N(0,I_{1}^{-1}(\theta_{0}))$$

**dimostrazione** (caso $p=1$)

Per il **teorema del valor medio di Lagrange** [^2] , esiste $\overline{\theta}_{ML}$ intermedio fra $\hat{\theta}_{ML}$ e $\theta_{0}$ tale per cui vale l'uguaglianza: 
$$0=\log^{'}L(\hat{\theta}_{ML})=\log L^{'}(\theta_{0})+\log L^{''}(\overline{\theta}_{ML})(\hat{\theta}_{ML}-\theta_{0})$$
da cui otteniamo che 
$$\sqrt{n}(\hat{\theta}_{ML}-\theta_{0})=-\frac{\log L^{'}(\theta_0)/\sqrt{n}}{\log L^{''}(\overline{\theta}_{ML})/n}$$
Vediamo ora come si comportano numeratore e denominatore

**numeratore**

Per il numeratore abbiamo una somma di variabii aleatorie i.i.d con valor medio nullo e varianza finita; siamo quindi nel dominio di applicabilità del teorema del limite centrale ed otteniamo

$$\log L^{'}(\theta_0)/\sqrt{n}=\frac{1}{\sqrt{n}}\sum\limits_{i=1}^{n}\frac{\partial\log f(X_{i};\theta)}{\partial\theta}\Big|_{\theta=\theta_{0}}\to_{d}N(0,I_{1}(\theta_0))$$

**denominatore**

Per il denominatore abbiamo una somma di variabili aleatorie i.i.d con valor medio finito, quindi per la legge dei grandi numeri su variabili uniformemente integrabili ed il teorema di Slutzky otteniamo

$$\log L^{''}(\theta_0)/n=\frac{1}{n}\sum\limits_{i=1}^{n}\frac{\partial^{2}\log f(X_{i};\theta)}{\partial\theta^2}\Big|_{\theta=\theta_{0}}\to_{d}I_{1}(\theta_0))$$

Combinando i due risultati ed usando di nuovo Slutzky si arriva all'enunciato del teorema $\blacksquare$

Vediamo ora l'*unico* controesempio al teorema

**Contro-Esempio**

Siano $X_{1},\dots, X_{n}\sim U[0,\theta]$

La verosimiglianza è quindi $$L(\theta;X_{1},\dots,X_n)=\prod_{i=1}^{n}\frac{1}{\theta}\mathbb 1_{[0,\theta]}(X_{i})=\frac{1}{\theta^{n}}\mathbb 1_{[0,\theta]}\left(X_{(n)}\right)$$
dove $X_{(n)}$ indica il valore più grande fra tutte le $X_i$

A questo punto, vediamo che $$\hat{\theta}_{ML}=X_{(n)}$$
questo perchè se $\theta\lt X_{(n)}$ allora la funzione di verosimiglianza $L\to0$

A questo punto vediamo che 
$$Pr(n(\theta_0-X_{(n)})\gt\varepsilon)=Pr\left(\theta_{0}-X_{(n)}\gt\frac{\varepsilon}{n}\right)=\left(1-\frac{\varepsilon}{\theta n}\right)^{n}\to e^{-\frac{\varepsilon}{\theta}}$$
La distribuzione limite risulta quindi esponenziale invece che Gaussiana, non vale quindi il teorema.

[^1]: https://it.wikipedia.org/wiki/Matrice_hessiana

[^2]: https://it.wikipedia.org/wiki/Teorema_di_Lagrange
