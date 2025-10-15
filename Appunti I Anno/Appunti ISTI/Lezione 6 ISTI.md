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
