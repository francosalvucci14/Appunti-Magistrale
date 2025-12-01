# Stimatori Bayesiani

Prima di parlare di **Stimatori Bayesiani**, ricordiamo la *formula di Bayes*

>[!definition]- Formula di Bayes
>Siano $H_{1},\dots,H_{m}$ eventi disgiunti ed esaustivi. cioè tali per cui $H_i\cap H_{j}=\emptyset$ per ogni $i\neq j$, e $\bigcup_{i=1}^{m}H_{i}=\Omega$
>Sia inoltre $E\in \mathcal F$ un evento con probabilità strettamente positiva; allora:
>$$Pr(H_{i}|E)=\frac{Pr(E|H_{i})Pr(H_{i})}{\sum\limits_{j=1}^{m}Pr(E|H_{j})Pr(H_{j})}$$
>

La derivazione della formula di Bayes è matematicamente banale (si riduce essenzialmente a ricordare che $Pr(E) = \sum\limits_{j=1}^{m} Pr(E|H_j ) Pr(H_j )$; 
l’interpretazione però è molto importante, perché permette di combinare in modo matematicamente la probabilità a priori di $m$ cause disgiunte $H_j$ e l’evidenza empirica sul
fatto che $E$ si sia verificato.

L’approccio Bayesiano all’inferenza statistica è profondamente diverso da quello che abbiamo seguito finora. 

L’idea di fondo è che non esista un "vero" parametro da stimare $\theta=\theta_0$ ; ma che il parametro sia esso stesso una variabile (o un vettore) aleatorio la cui distribuzione, che rappresenta il nostro stato di conoscenza, viene aggiornata tramite la formula di Bayes alla luce delle osservazioni. 

In altre parole, oltre alla legge delle osservazioni $f(X_1,\dots, X_n|\theta)$ dobbiamo supporre di conoscere la legge $\pi(\theta)$ del parametro prima di aver effettuato osservazioni. 
Si noti come abbiamo scritto $f(X_1,\dots, X_n|\theta)$ invece di $f(X_1\dots X_n;\theta)$; perché ora ha senso parlare della legge di $X_1,\dots,X_n$ condizionatamente al valore del parametro.
L’oggetto centrale dell’inferenza diviene quindi la legge a posteriori, che attraverso la formula di Bayes è data da
$$\pi(\theta|X_{1},\dots,X_{n})=\frac{f(X_1\dots X_n|\theta)\pi(\theta)}{\int_{\Theta}f(X_1\dots X_n|\theta)\pi(\theta)d\theta}$$

**Esempio**:

Consideriamo $X_1,\dots,X_{n}$ v.a Bernoulliane di parametro $p$; per quest'ultimo, assumiamo che abbia una distribuzione a priori di tipo Beta con parametri $\alpha,\beta$, cioè:
$$\pi(p)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{\alpha-1}(1-p)^{\beta-1},p\in[0,1]$$
Ricordiamo inanzitutto i valori di valor medio e varianza:
$$\mathbb E[p]=\frac{\alpha}{\alpha+\beta},Var(p)=\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$$
*vedere calcoli su dispensa*

Inoltre, scrivendo $y=\sum\limits_{i=1}^{n}X_{i}$ otteniamo che 
$$
\begin{align*}
f(y|p)\pi(p)&=\overbrace{{n\choose y}p^{y}(1-p)^{n-y}}^{f(X_{1},\dots,X_{n}|p)}\overbrace{\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{\alpha-1}(1-p)^{\beta-1}}^{\pi(p)}\\
&={n\choose y}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{y+\alpha-1}(1-p)^{n-y+\beta-1}
\end{align*}
$$
La **marginale a denominatore** è data da:
$$
\begin{align*}
f(y)&=\int_{0}^{1}{n\choose y}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{y+\alpha-1}(1-p)^{n-y+\beta-1}dp\\
&={n\choose y}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\frac{\Gamma(y+\alpha)\Gamma(n-y+\beta)}{\Gamma(n+\alpha+\beta)}
\end{align*}
$$
La **distribuzione a posteriori** è quindi:
$$
\begin{align*}
\pi(y|p)&=\frac{{n\choose y}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{y+\alpha-1}(1-p)^{n-y+\beta-1}}{{n\choose y}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\frac{\Gamma(y+\alpha)\Gamma(n-y+\beta)}{\Gamma(n+\alpha+\beta)}}\\
&=\frac{\Gamma(n+\alpha+\beta)}{\Gamma(y+\alpha)\Gamma(n-y+\beta)}p^{y+\alpha-1}(1-p)^{n-y+\beta-1}
\end{align*}
$$
cioè ancora una Beta, con parametri aggiornati.

Quando la distribuzione a posteriori assume la stessa forma di quella a priori, si parla di **leggi coniugate**

**Osservazione Importante**

Una interpretazione rigorosa dell’approccio Bayesiano dovrebbe concludersi con la derivazione della distribuzione a posteriori: il calcolo di uno stimatore "puntuale" non ha strettamente senso, visto che il paramrto non ha un singolo valore.

In pratica però il calcolo degli stimatori Bayesiani si conclude molto spesso con la derivazione di un singolo valore di sintesi, come ad esempio il valore che massimizza la distribuzione a posteriori o ancora più spesso il valore medio a posteriori.

Nel caso della binomiale con a priori beta otteniamo
$$
\begin{align*}
\hat{p}_{Bayes}&=\int_{0}^{1}p\cdot\frac{\Gamma(n+\alpha+\beta)}{\Gamma(y+\alpha)\Gamma(n-y+\beta)}p^{y+\alpha-1}(1-p)^{n-y+\beta-1}dp\\
&=\frac{y+\alpha}{n+\alpha+\beta}=\frac{y}{n}\frac{n}{n+\alpha+\beta}+\frac{\alpha}{\alpha+\beta}\frac{\alpha+\beta}{n+\alpha+\beta}
\end{align*}
$$

L’ultima espressione è illuminante, perchè rappresenta lo "stimatore Bayesiano" come una media ponderata di due elementi: lo stimatore classico di massima verosimiglianza (in questo caso, la semplice media aritmetica) ed il valore atteso a priori:
$$\hat{p}_{MLE}=\frac{y}{n}=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}=\overline{X}_{n},\frac{\alpha}{\alpha+\beta}=\mathbb E[\pi(p)]$$

Il peso dello stimatore di massima verosimiglianza converge ad 1 quando la dimensione del campione n diverge all’infinito; intuitvamente, le nostre opinioni a priori sono schiacciate dalla forza dell’evidenza empirica.