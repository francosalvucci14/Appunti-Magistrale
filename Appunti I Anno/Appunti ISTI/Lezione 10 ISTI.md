# Metodo dei momenti

Vogliamo ora introdurre uno dei tanti metodi esistenti per costruire degli buoni stimatori $T_{n}$

Avevamo detto la scorsa volta che ci sono degli stimatori noti, ad esempio:
- per stimare $\mu=\mathbb E[X_i]$ abbiamo usato $\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}$
- per stimare $\sigma^2=\mathbb E[(X-\mu)^{2}]$ abbiamo usato $\frac{1}{n}\sum\limits_{i=1}^{n}(X_{i}-X_{n})^{2}$

Vediamo quindi come generalizzare questa idea, sfruttando il **metodo dei momenti**

L'idea è la seguente:
- Supponiamo di avere un campione aleatorio $X_{1},\dots,X_{n}$ estratto da una legge di probabilità $P_{\theta}$, con $\theta=(\theta_{1},\dots,\theta_{k})$
- Supponiamo anche che questa legge ammetta $k$ momenti finiti, cioè $\mu_{j}=\mathbb E[X_{1}^{j}]$ ben definito per $j=1,\dots,k$
- Chiamiamo inoltre con $\hat\mu_{j,n}$ i momenti empirici definiti come $\hat\mu_{k,n}= \frac{1}{n}\sum\limits_{i=1}^{n}X_{i}^{j},\forall j=1,\dots,k$
- L'idea di fondo è quindi scegliere il valore dei parametri $\theta_{1},\dots,\theta_{k}$ in modo che valgano le seguenti uguaglianze vettoriali: $$\begin{align*}&\hat\mu_{1,n}=\mu_{1}(\overline{\theta}_{1},\overline{\theta}_{2},\dots,\overline{\theta}_{k})\\&\hat\mu_{2,n}=\mu_{2}(\overline{\theta}_{1},\overline{\theta}_{2},\dots,\overline{\theta}_{k})\\&\vdots\\&\hat\mu_{k,n}=\mu_{k}(\overline{\theta}_{1},\overline{\theta}_{2},\dots,\overline{\theta}_{k})\end{align*}$$
>[!teorem]- Metodo dei Momenti
>Assumiamo che esista un diffeomorfismo [^1] $g:\mathbb R^{k}\to\mathbb R^{k}$ tale che $g(\mu_{1},\dots,\mu_{k})=(\theta_{1},\dots,\theta_{k})$ per ogni valore di $(\theta_{1},\dots,\theta_{k})$.
>Lo stimatore del metodo dei momenti è allora definito da $$\hat\theta_{n}=(\overline{\theta}_{1},\dots,\overline{\theta}_{k}):=g(\hat\mu_{1,n},\dots,\hat\mu_{k,n})$$

[^1]: https://it.wikipedia.org/wiki/Diffeomorfismo

Per determinare le proprietà asintotiche del nostro stimatore dobbiamo rinforzare leggermente le nostre ipotesi.

Prima di tutto dobbiamo assumere che le nostre variabili aleatorie $X_{1},\dots,X_{n}$ sono *indipendenti ed identicamente distribuite* con momenti di ordine $2k$ finiti.

Vediamo ora una guida step-by-step per determinare se il metodo dei momenti rispetta i $4$ criteri per un buon stimatore:
1) Dobbiamo cercare condizioni tali per cui $\hat\mu_{1,n}\to_{p}\mu_{1},\hat\mu_{2,n}\to_{p}\mu_{2},\dots$
2) Se $g$ continua applichiamo **Slutzky** $$g(\hat\mu_{1,n},\dots,\hat\mu_{1,n})\to_{p}g(\mu_1,\dots,\mu_{k})=\theta\quad\text{consistenza}$$
3) Dobbiamo poi dimostrare che $$(\hat\mu_{1,n},\dots,\hat\mu_{1,n})\to_{d}N\quad\text{solo dopo aver centrato e normalizzato,prossimamente}$$
4) Se $g$ è **differenziabile** allora applichiamo il Metodo Delta, così che posso usare il CLT e far valere l'ultima condizione, ovvero l'asintotica gaussianità

Vediamo ora nel dettaglio ogni punto

1) Sotto le ipotesi $X_{1},\dots,X_{n}\sim\text{i.i.d},\theta\in\mathbb R^{p},\mathbb E[X_{1}^{p}]\lt\infty$ allora $(\hat\mu_{1,n},\dots,\hat\mu_{1,n})\to_{p}(\mu_{1},\dots,\mu_{n})$
	1) Così facendo incontro problemi con la Varianza e dovrei cambiare assumendo che esistano i momenti $\mathbb E[X_{1}^{2p}]$ , per evitare ciò posso sfruttare la definizione di *Uniforme Integrabilità*, così da evitare l'uso della Varianza) (vedere dimostrazione LGN sotto UI)
2) Sotto le ipotesi $X_{1},\dots,X_{n}\sim\text{i.i.d},\theta\in\mathbb R^{p},\mathbb E[X_{1}^{p}]\lt\infty$ preso $\theta=g(\mu_{1},\dots,\mu_{p})$ allora $$\hat\theta_{n}\to_{p}\theta$$
	1) Questo vale per il **lemma di Slutzky**
3) Per il terzo punto,sotto l'ipotesi che $\exists$ i pirmi $2p$ momenti, allora possiamo sfruttare il **CLT Multivariato** e ottenere che $$\sqrt{n}\left(\begin{align*}
\hat\mu_{1,n}&-\mu_{1}\\&\vdots\\\hat\mu_{p,n}&-\mu_{p}
\end{align*}\right)\to_{d}N(0,\Omega_{p\times p})$$dove $\Omega$ è definita come la **matrice Varianza e Covarianza**
4) Per l'ultimo punto, assumendo inoltre che $g$ sia differenziabile e che $$(Dg)=\left(\begin{align*}
&\frac{\partial g_{1}}{\partial x_{1}}\cdots\frac{\partial g_{1}}{\partial x_{p}}\\&\vdots\\&\frac{\partial g_{p}}{\partial x_{1}}\cdots\frac{\partial g_{p}}{\partial x_{p}}
\end{align*}\right)$$allora $$\sqrt{n}({\hat\theta_{n}}_{_{p\times 1}}-\theta_{p\times 1})\to_{d}N(0,(Dg)_{p\times p}\Omega(Dg)^{T})$$dove $(Dg)$ è definita come la matrice Jacobiana, ovvero $$(Dg)=Jg(\mu_{1},\dots,\mu_{k})$$
**oss** 
Per i primi due punti, basta che esistano i primi $p$ momenti finiti, se vogliamo invece arrivare anche agli altri due punti, serve necessariamente la condizione che esistano anche i primi $2p$ momenti.

---
# Esempio/Esercizio 1

Supponiamo di avere un campioni di variabili IID con legge Gamma di parametri $\alpha$ e $\beta$ ; cioè con densità:
$$\begin{align*}
&f_{X}(x)=\frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-\frac{y}{\beta}}\mathbb 1_{[0,\infty)}(x)\\
&\Gamma(\alpha)=\int_{0}^{\infty}x^{\alpha-1}e^{-x}dx
\end{align*}$$
Come si può vedere dall' [Appendice di probabilità](Appendice%20di%20probabilità.md) abbiamo che:
$$\begin{align*}
&\mathbb E[X_{1}]=\alpha\beta=\mu_{!}\\
&\mathbb E[X_{1}^{2}]=(\alpha\beta)^{2}+\alpha\beta^{2}=\alpha\beta(\alpha+1)=\mu_{2}\\
&Var(X_{1})=\alpha\beta^{2}
\end{align*}$$
Pertanto possiamo proseguire nel seguente modo (stiamo esplicitando dalle formule di cui sopra sia $\alpha$ che $\beta$)
$$\begin{align*}
&\alpha=\frac{\alpha^{2}\beta^{2}}{\alpha\beta^2}=\frac{\mu_{1}^{2}}{\mu_{2}-\mu_{1}^{2}}\\
&\beta=\frac{(\alpha\beta)^{2}+\alpha\beta^{2}-(\alpha\beta)^{2}}{\alpha\beta}=\frac{\mu_{2}-\mu_{1}^{2}}{\mu_{1}}
\end{align*}$$
Pertanto, gli stimatori dei valori $\alpha,\beta$ usando il metodo dei momenti saranno:
$$\begin{pmatrix}\hat\alpha_{n}\\\hat\beta_{n}\end{pmatrix}=\begin{pmatrix}\frac{\hat\mu_{1,n}^{2}}{\hat\mu_{2,n}-\hat\mu_{1,n}^{2}}\\\frac{\hat\mu_{2,n}-\hat\mu_{1,n}^{2}}{\hat\mu_{1,n}}\end{pmatrix}$$
