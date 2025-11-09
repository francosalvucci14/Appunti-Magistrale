# Consistenza del metodo di massima verosimiglianza

Dimostriamo in questa lezione il secondo dei $4$ criteri di un buon stimatore, per lo stimatore di massima verosimiglianza

**oss**
Partiamo già dal secondo criterio perchè, per natura, lo stimatore di massima verosimiglianza non può essere non distorto (è non distorto per costruzione)

Per poter dimostrare effettivamente la consistenza dello stimatore ML dobbiamo introdurre la seguente nozione

>[!definition]- Distanza di Kullback-Leibler
>Siano $f,g$ funzioni di densità o di probabilità.
>La distanza di Kullback-Leibler tra $f$ e $g$ è definta come (nel caso continuo):
>$$D(f,g)=\int\log\left[\frac{f(x;\theta)}{g(x;\theta)}\right]f(x;\theta)dx$$
>Nel caso in cui $f$ non sia *assolutamente continua* rispetto a $g$ , la distanza fra le due viene posta a $+\infty$
>Nel caso discreto invece, la distanza è definita come:
>$$D(p,q)=\sum\limits_{x_{i}}\log\left[\frac{p(x_{i};\theta)}{q(x_{i};\theta)}\right]p(x_i;\theta)$$

Valgono le seguenti proprietà:
1. $D(f,g)\neq D(g,f)$, ovvero $D(\cdot,\cdot)$ non identifica una **metrica** [^1] 
2. Se $f=g\implies D(f,g)=0$
3. Se $f\neq g\implies D(f,g)\gt0$

Dimostriamo il terzo punto:
$$D(f,g)\overbrace{=}^{\text{per def. di val, atteso su densità}}\mathbb E\left[\log\left(\frac{f(X)}{g(X)}\right)\right]=\mathbb E\left[-\log\left(\frac{g(X)}{f(X)}\right)\right]$$
Applicando Jensen ora ottengo che 
$$\begin{align*}\mathbb E\left[-\log\left(\frac{g(X)}{f(X)}\right)\right]&\geq-\log\left(\mathbb E\left[\frac{g(X)}{f(X)}\right]\right)\\&=-\log\left(\int\frac{g(X)}{f(X)}f(X)dx\right)\\&=-\log\left(\underbrace{\int g(X)dx}_{=1}\right)=-\log(1)=0\end{align*}$$

E di conseguenza, otteniamo che $$D(f,g)=\mathbb E\left[\log\left(\frac{f(X)}{g(X)}\right)\right]\geq0\quad\blacksquare$$
**oss**
$\int g(X)dx=1$ perchè $g(X)$ è una densità, e l'integrale di una densità è sempre $=1$

Quale relazione lega quindi la funzione di verosimiglianza con la distanza di Kullback-Leibler?

Focalizziamoci come al solito sulla log-verosimiglianza; considerando che lo stimatore è **invariante** se la funzione è trasformata linearmente con coefficienti che non dipendono dal parametro, possiamo passare da $$\log L=\sum\limits_{i=1}^{n}\log(f(X_{i};\theta))$$
a
$$M_{n}(\theta):=\frac{1}{n}\sum\limits_{i=1}^{n}\log(f(X_{i};\theta))-\frac{1}{n}\sum\limits_{i=1}^{n}\log(f(X_{i};\theta_0))=\frac{1}{n}\sum\limits_{i=1}^{n}\log\left(\frac{f(X_{i};\theta)}{f(X_{i};\theta_{0})}\right)$$
dove $\theta_{0}$ è il "vero" valore del parametro.

**piccola oss** 
Perchè abbiamo potuto effettuare questa operazione per $M_{n}(\theta)$?
La risposta è molto semplice:
- Le $X_{i}$ sono pescate da un certo modello probabilistico, in cui si trova $\theta_{0}$ che è il vero $\theta$, di conseguenza possiamo affermare che $\theta_{0}$ e $\theta$ differiscono
- Dato che i due valori differiscono fra loro, possiamo prendere la log-verosimiglianza e sottrargli se stessa calcolata in $\theta_0$ (senza incorrere in risultati nulli o cose del genere)

Sotto alcune delle condizioni di regolarità viste in precedenza, affinchè valga la legge dei grandi numeri abbiamo che, per un valore di $\theta$ fissato vale:
$$\begin{align*}M_{n}(\theta)=\frac{1}{n}\sum\limits_{i=1}^{n}\log\left(\frac{f(X_{i};\theta)}{f(X_{i};\theta_{0})}\right)&\to_{p}\mathbb E\left[\log\left(\frac{f(X_{1};\theta)}{f(X_{1};\theta_{0})}\right)\right]\\&=\int\log\left(\frac{f(x;\theta)}{f(x;\theta_{0})}\right)f(x;\theta_0)dx\\&=-D(f_{\theta_{0}},f_{\theta})\end{align*}$$

Siamo quindi pronti a definire e dimostrare il teorema sulla consistenza dello stimatore ML.

Diamo prima uno "sketch euristico" della dimostrazione.

Quello che dobbiamo fare sostanzialmente è:
1. Definiamo $M_{n}(\theta)$
2. Dobbiamo dimostrare che $$M_{n}(\theta)\to_p -D(\theta_{0},\theta)$$
3. Infine, dobbiamo dimostrare che $$Pr(|\hat{\theta}_{ML}-\theta_0|\gt\delta)\to0\implies\hat{\theta}_{ML}=\theta_{0}$$

Diamo ora l'enunciato del teorema:

>[!teorem]- Consistenza MLE
>Sia $M_{n}(\theta)$ definito come sopra
>Sia $M(\theta)=-D(\theta_{0},\theta)$
>Assumiamo che valgano le seguenti ipotesi:
>1. (Legge dei grandi numeri uniforme) $$\sup|M_{n}(\theta)-M(\theta)|=o_{p}(1),n\to\infty\quad(\text{oppure sup}\to_p0\text{, stessa cosa})$$
>2. (Convessità) Per ogni $\varepsilon\gt0\exists\eta_{\varepsilon}\gt0$ tale per cui: $$|\theta-\theta_{0}|\gt\varepsilon\implies|M(\theta)-M(\theta_0)|\gt\eta_{\varepsilon}$$
>
>Allora $$\hat{\theta}_{ML}\to_p\theta_{0}$$

**dimostrazione**

Ricordiamo un fatto generale, ovvero che se $$A\implies B\text{ allora }Pr(A)\leq Pr(B)$$
L'idea della dimostrazione è che per ogni $\varepsilon\gt0$ fissato si ha che $$Pr(|M(\theta)-M(\theta_0)|\gt\eta_{\varepsilon})\to0$$
Grazie alla condizione di convessità abbiamo che $$Pr(|\theta-\theta_{0}|\gt\varepsilon)\leq Pr(|M(\theta)-M(\theta_0)|\gt\eta_{\varepsilon})$$
A questo proposito notiamo che, per definizione di stimatore ML abbiamo che $$M(\theta_{0})-M(\hat{\theta}_{ML})\gt0$$
e quindi $$\begin{align*}M(\theta_{0})-M(\hat{\theta}_{ML})&=M(\theta_{0})-M_{n}(\theta_{0})+M_n(\theta_{0})-M(\hat{\theta}_{ML})\\&\leq M(\theta_{0})-M_{n}(\theta_{0})+M_{n}(\hat{\theta}_{ML})-M(\hat{\theta}_{ML})\\\hat{\theta}_{ML}\text{ massimizza }M_{n}(\theta)\to&\leq\underbrace{|M(\theta_{0})-M_{n}(\theta_{0})|}_{(A)}+\underbrace{|M_{n}(\hat{\theta}_{ML})-M(\hat{\theta}_{ML})|}_{(B)}\end{align*}$$
Ora, sia $(A)$ che $(B)\to_p0$ per la prima ipotesi, infatti abbiamo che $$Pr(|M(\theta)-M(\theta_0)|\gt\eta_{\varepsilon})\leq Pr\left((A)\gt\frac{\eta_{\varepsilon}}{2}\right)+Pr\left((B)\gt\frac{\eta_{\varepsilon}}{2}\right)$$ed entrambe le probabilità $\to0$ per $n\to\infty$, usando per la prima la legge dei grandi numeri standard, e per la seconda quella uniforme (che implica la standard) $\blacksquare$

**osservazione sulle ipotesi del teorema**
1. L'ipotesi 1.) è più forte delle leggi dei grandi numeri viste da noi in precedenza, perchè richiede che la convergenza sia uniforme in $\theta$, il che non è garantito anche se la convergenza avviene puntualmente per ogni valore fisso di $\theta$
2. L'ipotesi 2.) è essenzialmente una condizione di identificabilità: se esistesse un pool di valori diversi di $\theta$ a distanza di Kullback-Leibler $0$ da $\theta_0$ il problema della consistenza sarebbe evidentemente irrisolvibile ( e lo stimatore potrebbe non essere nemmeno ben definito)




[^1]: ad esempio, perchè non è simmetrica negli argomenti (e non vale la disuguaglianza triangolare)
