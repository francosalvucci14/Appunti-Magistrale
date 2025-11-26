# Ancora su Statistiche Sufficienti

A metà del ventesimo secolo Halmos e Savage hanno dato una caratterizzazione della sufficenza leggermente più generale, come segue.

>[!teorem]- Criterio di Fattorizzazione di Halmos-Savage
>Una statistica è sufficiente se e solo se la funzione di probabilità (o densità) di $X_1,\dots,X_{n}$ si fattorizza come:
>$$p(X_{1},\dots,X_{n};\theta)=q(T(X_{1},\dots,X_{n};\theta))h(X_{1},\dots,X_{n})$$
>dove $h(\cdot)$ non dipende da $\theta$

**dimostrazione**

L’implicazione sufficienza $\implies$ fattorizzazione è ovvia: basta prendere per $g(T ;\theta ) = q(T ;\theta )$ (la legge di q) e h la legge delle $X_i$ condizionata a $T$, che sappiamo essere indipendente da $\theta$

L’interesse del Teorema è quindi nella seconda parte, cioè nel caso in cui la fattorizzazione non corrisponda necessariamente alla coppia legge di $T$ / legge di $X_1,\dots,X_n$ condizionata a T

Come sempre in questa sezione ci limitiamo il caso discreto, e partizioniamo il dominio
di $X_1,\dots,X_n$ in classi di equivalenza corrispondenti ai valori della statistica sufficiente; definiamo cioè i sottoinsiemi di $\mathbb R^{n}$ come:
$$A_{T(X_1,\dots,X_n)}\subseteq\mathbb R^{n}:=\{Y=Y_{1},\dots,Y_{n}:T(Y)=T(X)\}$$
Prendiamo ora il seguente rapporto:
$$\frac{p(X_1,\dots,X_n;\theta)}{f_{T}(T(X_1,\dots,X_n);\theta)}$$
E dobbiamo dimostrare che il rapporto non dipende da $\theta$

$$\begin{align*}
\frac{p(X_1,\dots,X_n;\theta)}{f_{T}(T(X_1,\dots,X_n);\theta)}&=\frac{h(X_{1},\dots,X_{n})\cancel{q(T;\theta)}}{\sum\limits_{Y\in A_{T(X)}}h(Y_{1},\dots,Y_{n})\cancel{q(T(Y_{1},\dots,Y_{n});\theta)}}\\
&=\frac{h(X_{1},\dots,X_{n})}{\sum\limits_{Y\in A_{T(X)}}h(Y_{1},\dots,Y_{n})}
\end{align*}$$
che non dipende da $\theta\quad\blacksquare$

**Esempio**

Prendiamo $X_1,\dots,X_{n}\sim N(\mu,1)$
Una statistica sufficiente potrebbe essere la media arimetica, però dobbiamo dimostrarlo (grazie al cazzo)

La legge congiunta è:
$$f(X_{1},\dots,X_n;\theta)=\frac{1}{(2\pi)^{\frac{n}{2}}}e^{-\frac{1}{2}\sum\limits_{i=1}^{n}(X_i-\mu)^{2}}$$
Possiamo espandere il quadrato, ottentendo:
$$\sum\limits_{i=1}^{n}(X_{i}-\mu)^{2}=\sum\limits_{i=1}^{n}(X_{i}-X_{n}+X_{n}-\mu)=\sum\limits_{i=1}^{n}(X_{i}-X_{n})^{2}+n(X_{n}-\mu)$$
Otteniamo quindi che:
$$\begin{align*}
f(X_{1},\dots,X_n;\theta)&=\frac{1}{(2\pi)^{\frac{n}{2}}}e^{-\frac{1}{2}\sum\limits_{i=1}^{n}(X_i-\mu)^{2}}\\
&=\frac{1}{(2\pi)^{\frac{n}{2}}}\left[\underbrace{e^{-\frac{1}{2}\sum\limits_{i=1}^{n}(X_i-X_{n})^{2}}}_{h}\overbrace{e^{-\frac{1}{2}n(X_n-\mu)^{2}}}^{q}\right]
\end{align*}$$
Prendendo quindi $X_n=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}\sim N(\mu,\frac{1}{n})$, vediamo che la sua legge è proprio $q(X_{n};\mu)=q$ nell'equazione di cui sopra.

Di conseguenza, $X_n$ risulta essere la statistica sufficiente per il campione scelto

Perchè lo è? Perchè basta vedere che il rapporto fra la legge del campione e la legge della statistica non dipende da $\theta$, infatti:
$$\frac{p(X_{1},\dots,X_{n};\mu)}{q(X_{n};\mu)}=\frac{1}{(2\pi)^{\frac{n}{2}}}\times e^{-\frac{1}{2}\sum\limits_{i=1}^{n}(X_i-X_{n})^{2}}$$
## Il Teorema di Rao-Blackwell

L’idea intutiva dietro le statistiche su¢ cienti è quella di condensare l’informazione del campione aleatorio conservando quello che è utile per risalire al valore "vero" del parametro. Sembra quindi inuitivo che gli stimatori efficienti debbano essere costruiti solo a partire da statistiche sufficienti.

Questa idea è resa rigorosa dal teorema di Rao-Blackwell; prima di enunciarlo, dobbiamo ricordare alcune nozioni sul valor medio condizionato.

Abbiamo $2$ v.a $X,Y$ con distribuzione congiunta $f(X,Y)$, allora 
$$\begin{align*}
&\mathbb E[X]=\int x\cdot f_{X}(x)dx\\
&\mathbb E[Y]=\int y\cdot f_{Y}(y)dy
\end{align*}$$
dove $f_{X}(x)=\int f(x,y)dy$ 

La densità congiuta è quindi 
$$f_{X|Y}(x|Y=x)=\frac{f_{X,Y}(x,y)}{f_{Y}(y)}$$
Di conseguenza
$$\mathbb E[X|y]=\int x\cdot f_{X,Y}(x|y)dx\quad(\text{ricordiamo che così risulta un numero})$$
Se cambio $y$ con $Y$ (qua ora il risultato diventa una v.a) otteniamo 
$$\mathbb E[X|Y]=\mathbb E[X|Y_{(\omega)}]=\int x\cdot f_{X|Y}(x|Y_{(\omega)})dx=\psi(Y)$$
Vediamo ora questo lemma

>[!teorem]- Lemma
>Siano $X,Y$ v.a. di quadrato integrabile definite sullo stesso spazio di probabilità.
>Allora:
>$$Var(X)=\mathbb E[Var(X|Y)]+Var(\mathbb E[X|Y])$$

**dimostrazione**

$$\begin{align*}
Var(X)&=\mathbb E[(X-\mathbb E[X])^{2}]=\mathbb E[(X-\mathbb E[X|Y]+\mathbb E[X|Y]-\mathbb E[X])^{2}]\\
&=\mathbb E_{Y}[\mathbb E[(X-\mathbb E[X|Y]+\mathbb E[X|Y]-\mathbb E[X])^{2}]|Y]\\
&=\mathbb E_{Y}[\mathbb E[(X-\mathbb E[X|Y])^{2}]|Y]+\mathbb E_{Y}[(\mathbb E[X|Y]-\mathbb E[X])^{2}|Y]\\
&=\mathbb E[Var(X|Y)]+Var(\mathbb E[X|Y])\quad\blacksquare
\end{align*}$$

Possiamo finalmente arrivare al risultato principale, che ci garantisce che condizionando uno stimatore non distorto su una statistica sufficiente se ne ottiene un altro ancora non distorto e con varianza non maggiore.

>[!teorem]- Teorema di Rao-Blackwell
>Sia $W=W(X_{1},\dots,X_{n})$ uno stimatore con le seguenti caratteristiche:
>1. $\mathbb E[W]=\theta_0$
>2. $\mathbb E[W^{2}]\lt\infty$
>
>Presa $T$ la statistica sufficiente, allora possiamo creare un nuovo stimatore $W^{'}$ nel seguente modo:
>$$W^{'}=\mathbb E[W|T](=\psi(T))$$
>Questo nuovo stimatore ha le seguenti caratteristiche:
>1. $\mathbb E[W^{'}]=\theta_{0}$
>2. $Var(W^{'})\leq Var(W)$

**dimostrazione teorema**

La dimostrazione è una applicazione diretta del teorema della torre [^1] e del lemma descritto prima
Infatti vale che

$$\begin{align*}
&1. \mathbb E[W^{'}]=\mathbb E_{T}[\mathbb E[W|T]]=\mathbb E[W]=\theta_{0}\space\checkmark\\\\
&2.Var(W)=Var(W^{'})+Var(\mathbb E[W|T])+\mathbb E[Var(W|T)]\implies Var(W^{'})\leq Var(W)\space\checkmark
\end{align*}$$

**oss**

Dove abbiamo usato nella dimostrazione precedente la sufficienza?

Apparentemente non gioca alcun ruolo, ma in realtà ci garantisce che il valor medio condizionato non dipenda dal parametro, e quindi che $\psi(T )$ sia effettivamente uno stimatore. 

Ad esempio consideriamo un campione di sole due osservazioni $X_1, X_2$ Gaussiane indipendenti con valor medio $\mu$ e varianza $1$, e consideriamo lo stimatore $\overline{X}_2 = \frac{1}{2}(X_1 + X_2 )$ 

Consideriamo poi $$\psi(X_1):=\mathbb E[\overline{X}_{2}|X_{1}]=\frac{X_1+\mu}{2}$$
Questa variabile aleatoria ha valor medio $\mu$ e varianza $\frac{1}{4}\lt Var(\overline{X}_2)= \frac{1}{2}$; non si tratta però di uno stimatore, perchè il suo valore non può essere determinato senza conoscere il valore del parametro $\mu$

[^1]: https://it.wikipedia.org/wiki/Legge_delle_aspettative_iterate
