# Uniforme Integrabilità

Diamo subito la definzione di **Uniforme Integrabile**

>[!definition]- Uniforme Integrabile
>Sia $\{X_{i}\}_{i\in\mathbb N}$ una sequenza di $n$ v.a
>Questa sequenza è chiamata **Uniforme Integrabile** se vale che: 
>$$\lim_{M\to\infty}\sup_{i}\mathbb E\left[|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]=0$$

**Esempi**

v.a *non* UI:
$$X_{n}=\begin{cases}
0&1-\frac{1}{n^{2}}\\n^{2}&\frac{1}{n^2}
\end{cases}$$
questa v.a non è UI perchè, anche se $\mathbb E[X_{n}]=1\space\forall n$, vale comunque che $$\lim_{M\to\infty}\sup_{i}\mathbb E\left[|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]=1$$
v.a UI:
$$X_{n}=\begin{cases}
0&1-\frac{1}{n^{2}}\\n&\frac{1}{n^2}
\end{cases}$$
così facendo vale che $$\lim_{M\to\infty}\sup_{i}\mathbb E\left[|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]=0$$
Vediamo ora le **condizioni necessarie e sufficienti** per affermare che una sequenza di v.a sia UI

>[!definition]- Condizioni Sufficienti per UI
>Valgono le seguenti condizioni sufficienti:
>1) $|X_{i}|\leq k,\forall k\in\mathbb R$
>2) $\mathbb E[X_{i}]\lt\infty$ e $X_{i}\sim$ i.i.d
>3) $\exists\eta\gt0:\mathbb E[|X_{i}|^{1+\eta}]\lt k,\forall i,k\in\mathbb R$

**dimostrazione**
1) Ovvia
2) Dobbiamo calcolare $$\lim_{M\to\infty}\sup_{i}\mathbb E\left[|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]=0$$Essendo le v.a i.i.d, allora il limite diventa $$\lim_{M\to\infty}\mathbb E\left[|X_1|\mathbb 1_{[|X_{1}|\gt M]}\right]=0\space(\text{definizione stessa di valor medio})$$
3) Qui il limite diventa $$\begin{align*}\lim_{M\to\infty}\sup_{i}\mathbb E\left[|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]&\leq\lim_{M\to\infty}\sup_{i}\mathbb E\left[\frac{|X_{i}|^{\eta}}{M^{\eta}}|X_i|\mathbb 1_{[|X_{i}|\gt M]}\right]\\&=\lim_{M\to\infty}\frac{1}{M^{\eta}}\overbrace{\sup_{i}\mathbb E\left[|X_i|^{1+\eta}\mathbb 1_{[|X_{i}|\gt M]}\right]}^{k}=0\end{align*}$$
$\blacksquare$

>[!definition]- Condizione Necessaria per UI
>La condizione necessaria per far sì che $X_{n}$ sia UI è che $\sup_{i}\mathbb E[|X_{i}|]\lt k$ (valor medio uniformemente limitato)
>Quindi, vale che se $$X_{n}\sim UI\implies\mathbb E[|X_{n}|]\lt k$$

**dimostrazione**

Scegliamo $\varepsilon=1\implies\exists M=M_{\varepsilon}$ tale che $$\sup_{i}\mathbb E[|X_{i}|\mathbb 1_{[|X_{i}|\gt M]}]\leq\varepsilon$$
Quindi, possiamo riscrivere $$\mathbb E[|X_{i}|]=\underbrace{\mathbb E[|X_i|\mathbb 1_{[|X_{i}|\leq M]}]}_{\leq M_{\varepsilon}}+\underbrace{\mathbb E[|X_i|\mathbb 1_{[|X_{i}|\gt M]}]}_{\leq\varepsilon\space\text{per ipotesi}}\leq M_{\varepsilon}+\varepsilon\space\blacksquare$$
Passiamo ora a una variante della **Legge dei Grandi Numeri**

>[!teorem]- LGN senza varianza finita
>Sia $\{X_{i}\}_{i\in\mathbb N}$ una sequenza di v.a UI e indipendenti.
>Per semplicità assumiamo che $\mathbb E[X_{i}]=0$
>Allora vale la seguente:
>$$\overline{X}_{n}=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}\to_{1}0$$
>E nello specifico, $\overline{X}_{n}\to_{p}0$

**dimostrazione**

Spezziamo $X_{i}$ in due parti, ottenendo $$X_i=X_{i}^{'}+X_{i}^{''},\space X_{i}^{'}=X_{i}\mathbb 1_{[|X_{i}|\leq M]}\land X_{i}^{''}=X_{i}\mathbb 1_{[|X_{i}|\gt M]}$$
In questo modo, otteniamo che 
$$\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}=\overbrace{\frac{1}{n}\sum\limits_{i=1}^{n}(X_{i}^{'}-\mathbb E[X_{i}^{'}])}^{(A)}+\overbrace{\frac{1}{n}\sum\limits_{i=1}^{n}(X_{i}^{''}-\mathbb E[X_{i}^{''}])}^{(B)}$$
Ricordiamo che $\mathbb E[X_i]=0$, ma non è detto che $\mathbb E[X_{i}^{'}]=0$ oppure $\mathbb E[X_{i}^{''}]=0$, sappiamo solo che $\mathbb E[X_{i}^{'}]+\mathbb E[X_{i}^{''}]=0$ 

Il punto $(A)$ è semplicemente la media aritemita di variabili aleatorie con valor medio nullo e varianzia uniformemente limitata da $M^2$, quindi va a zero in media quadratica per la legge dei grandi numeri di Chebychev.

Per il punto $(B)$ possiamo riscrivere la situazione così: 
$$\begin{align*}
\mathbb E\left[\frac{1}{n}\sum\limits_{i=1}^{n}(X_{i}^{''}-\mathbb E[X_{i}^{''}])\right]\leq \frac{1}{n}\mathbb E\left[\sum\limits_{i=1}^{n}(X_{i}^{''}-\mathbb E[X_{i}^{''}])\right]\leq\frac{2}{n}\sum\limits_{i=1}^{n}\mathbb E[X_{i}^{''}]\leq\frac{2}{n}n\varepsilon=2\varepsilon
\end{align*}$$
E questo $\varepsilon$ lo possiamo rendere piccolo a piacere, così facendo otteniamo che anche $(B)\to0\quad\blacksquare$ 
La nozione di UI può essere usata anche per invertire la freccia $(3)\implies(2)$ 

Vale quindi la seguente proposizione

>[!teorem]- Proposizione
>Sia $\{X_{n}\}$ una sequenza di v.a UI con $X_{n}\to_{p}X$, allora $$X_{n}\to_{1}X$$

**dimostrazione**

Riscriviamo il tutto come:
$$\mathbb E[|X_{n}-X|]\leq \mathbb E[|X_{n}|\mathbb 1_{[|X_{n}|\leq M]}-X_{n}]+\mathbb E[|X|\mathbb 1_{[|X|\leq M]}-X]+\mathbb E[|X_{n}|\mathbb 1_{[|X_{n}|\leq M]}-X\mathbb 1_{[|X|\leq M]}]$$
Il primo elemento può essere reso piccolo a piacere, grazie alla condizione UI
Il secondo elemento anchè però qui grazie al fatto che $X$ ha necessariamente valor medio finito
Il terzo elemento anche perchè abbiamo a che fare con variabili limitate che convergono in probabilità
$\blacksquare$


