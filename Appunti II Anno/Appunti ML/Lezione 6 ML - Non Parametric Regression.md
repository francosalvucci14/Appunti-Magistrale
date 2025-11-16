```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# Recap su Regressione F.Bayesiana

Ricordiamo che, nella regressione completamente bayesiana, non vengono identificati parametri specifici del modello $\overline{w}^{\star}$ da applicare nella predizione come
$$h(\overline{x},\overline{w}^{\star})=\overline{x}^{T}\overline{w}^{\star}$$
Invece, la distribuzione $p(t|\overline{x})$ è derivata, nell'ipotesi di gaussianità, con
$$p(t|\overline{x},X,\mathbf t,;\alpha,\beta)=\mathcal N(t;m(\overline{x}),\sigma^{2}(\overline{x}))$$
con:
- media $m(\overline{x})=\beta\overline{x}^{T}S\overline{X}^{T}\mathbf t$
- varianza $\sigma^{2}(\overline{x})=\frac{1}{\beta}+\overline{x}^{T}S\overline{x}$
- $S=(\alpha\mathbf I+\beta\overline{X}^{T}\overline{X})^{-1}\in\mathbb R^{(d+1)\times(d+1)}$

La predizione $h(\overline{x})$ può essere ritornata come aspettazione della distribuzione predittiva, ovvero 
$$h(\overline{x})=m(\overline{x})=\beta\overline{x}^{T}S\overline{X}^{T}\mathbf t$$
Dato che possiamo scrivere $\overline{X}^{T}\mathbf t$ come 
$$\overline{X}^{T}\mathbf t=\begin{pmatrix}1&\dots&1\\x_{11}&\dots&x_{n1}\\\vdots\\x_{1d}&\dots&x_{nd}\end{pmatrix}\cdot\begin{pmatrix}t_{1}\\t_{2}\\\vdots\\t_{n}\end{pmatrix}=\sum\limits_{i=1}^{n}\begin{pmatrix}1\\x_{i1}\\\vdots\\x_{id}\end{pmatrix}t_{i}=\sum\limits_{i=1}^{n}\overline{x}_it_{i}$$
allora possiamo scrivere anche che 
$$h(\overline{x})=\beta\overline{x}^{T}S\sum\limits_{i=1}^{n}\overline{x}_it_{i}=\sum\limits_{i=1}^{n}\beta\overline{x}^{T}S\overline{x}_it_{i}$$
Si noti che la previsione non viene calcolata facendo riferimento a un insieme di parametri derivati dall'ottimizzazione di una funzione di loss. 

Può invece essere vista come una combinazione lineare dei valori target $t_i$ di tutti gli elementi nel training set, con pesi dipendenti dai valori degli elementi $\overline{x}_i$ (e da $\overline{x}$).

Indichiamo con $\mathbf k(\overline{x}_1, \overline{x}_2) = \beta\overline{x}_{1}^{T}S\overline{x}_{2}$ la funzione che fornisce il peso associato al valore target $t_i$, quando i suoi argomenti sono $\overline{x}_i$ e $\overline{x}$. 

Quindi, in generale abbiamo che
$$h(\overline{x})=\sum\limits_{i=1}^{n}\mathbf k(\overline{x},\overline{x}_i)t_i$$
La funzione appena descritta prende il nome di **kernel equivalente**

Si noti che, in un certo senso, fornisce una misura di quanto i valori dei target associati a $\overline{x}_1$ e $\overline{x}_2$ dipendono l'uno dall'altro. 

Applicando un insieme $\phi$ di funzioni di base, la definizione di kernel equivalente può essere modificata in
$$\mathbf k(\overline{x}_1, \overline{x}_2)=\beta\phi(\overline{x}_1)^{T}S\phi(\overline{x}_2)$$
Nel nostro quadro $\mathbf k(\overline{x},x_{i})$ è quindi una misura di quanto il valore del target associato a $\overline{x}$, che deve essere approssimato, sia correlato al target di $\overline{x}_i$, che è noto.

Nella figura sottostante, a destra è mostrato un grafico sul piano $(\overline{x}, \overline{x}_i)$ di un kernel equivalente campione per il caso in cui è data una sola caratteristica, nel caso in cui $\phi$ è un insieme di funzioni di base gaussiane.

A sinistra, un grafico dei valori di $\mathbf k(\overline{x},\overline{x}_i)$ come funzioni di $\overline{x}$, per tre diversi valori di $\overline{x}_i$

![center|500](Pasted%20image%2020251116160017.png)

Osserviamo infine che, invece di introdurre funzioni di base che alla fine danno luogo a un kernel equivalente, possiamo seguire lo stesso approccio di previsione mediante una combinazione lineare di valori target, con pesi calcolati da un **kernel localizzato adeguato**, definito su una coppia di elementi (cioè su $\mathbb R^d \times \mathbb R^d$) e che restituisce un valore reale
# Kernel Regression

Nei metodi di regressione kernel, il valore target corrispondente a qualsiasi elemento $\overline{x}$ viene predetto facendo riferimento agli elementi nel training set, e in particolare agli elementi più vicini a $\overline{x}$.

Ciò viene controllato facendo riferimento a una funzione kernel predefinita $\mathbf k_h(\overline{x})$, che restituisce valori non trascurabili solo in un intervallo intorno a 0.

Un kernel possibile e comune è il *kernel gaussiano* (o *RBF*), rappresentato graficamente di seguito nel caso $d = 1$ per diversi valori dell'iperparametro $h$.
$$g(\overline{x})=e^{-\frac{||\overline{x}||^{2}}{2h^{2}}}$$
![center|500](Pasted%20image%2020251116160417.png)

Per ricavare la funzione di previsione $h$, ricordiamo che nella regressione il nostro obiettivo è approssimare l'aspettativa condizionata
$$\mathbb E[t|\overline{x}]=\int t\space p(t|\overline{x})dt=\int t\frac{p(\overline{x},t)}{p(\overline{x})}ft=\frac{\int t\space p(\overline{x},t)dt}{p(\overline{x})}=\frac{\int t\space p(\overline{x},t)dt}{\int p(\overline{x},t)dt}$$
Assumiamo ora che la distribuzione congiunta $p(\overline{x},t)$ sia approssimata mediante una funzione kernel come
$$p(\overline{x},t)\approx \frac{1}{n}\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})\mathbf k_{h}(t-t_{i})$$
Questo si traduce in
$$h(\overline{x})=\frac{\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})\int t\space\mathbf k_{h}(t-t_{i})dt}{\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})\int \space\mathbf k_{h}(t-t_{i})dt}$$
Se ipotizziamo che il kernel $\mathbf k(x)$ sia sempre non negativo, abbia media $\int t\space\mathbf k_h(x)dx = 0$ e area sotto la curva $\int\mathbf k_h(x)dx = 1$ (il che implica che si tratta di una distribuzione di densità di probabilità), abbiamo che $\int\mathbf k_h(t − t_i)dt = 1$ e $\int t\space\mathbf k_h(t − t_i)dt = t_i$, e infine otteniamo
$$h(\overline{x})=\frac{\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})t_{i}}{\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})}$$
Impostando 
$$w_{i}(\overline{x})=\frac{\mathbf k_{h}(\overline{x}-\overline{x}_{i})}{\sum\limits_{j=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{j})}$$
possiamo riscrivere che 
$$h(\overline{x})=\sum\limits_{i=1}^{n}w_i(\overline{x})t_{i}$$
ovvero, il valore previsto viene calcolato come una combinazione lineare normalizzata di tutti i valori target, ponderata applicando il kernel scelto (**modello di Nadaraya-Watson**).

Chiaramente, se applichiamo le funzioni base, otteniamo le seguenti modifiche:
$$\begin{align*}
&h(\overline{x})=\sum\limits_{i=1}^{n}w_i(\phi(\overline{x}))t_{i}\\\\
&w_{i}(\overline{x})=\frac{\mathbf k_{h}(\phi(\overline{x})-\phi(\overline{x}_{i}))}{\sum\limits_{j=1}^{n}\mathbf k_{h}(\phi(\overline{x})-\phi(\overline{x}_{j}))}
\end{align*}$$
## Locally Weighted Regression

Nel modello Nadaraya-Watson, la previsione viene eseguita mediante una combinazione ponderata normalizzata di valori costanti (valori target nel training set).

La **regressione ponderata localmente** (***LOESS***) migliora tale approccio facendo riferimento a una versione ponderata della somma della funzione di perdita delle differenze al quadrato utilizzata nella regressione.

Se un valore $t$ deve essere previsto per un elemento $\overline{x}$, viene considerata una versione “locale” della funzione di loss, con peso $\psi_i(\overline{x})$. 

Ipotizzando nuovamente l'utilizzo delle funzioni di base $\phi$, otteniamo che 
$$L(\overline{x})=\sum\limits_{i=1}^{n}\psi_{i}(\overline{x})(\overline{w}^{T}\overline{x}_{i}-t_{i})^2=\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})(\overline{w}^{T}\overline{x}_{i}-t_i)^{2}$$
I pesi $\psi_i(\overline{x})$ dipendono dalla “distanza” tra $\overline{x}$ e $\overline{x}_i$, misurata dalla funzione kernel
$$\psi_{i}(\overline{x})=\mathbf k_{h}(\overline{x}-\overline{x}_{i})$$
La minimizzazione di questa funzione di loss
$$\overline{w}^{\star}(\overline{x})=arg\min_{\overline{w}}\sum\limits_{i=1}^{n}\psi_{i}(\overline{x})(\overline{w}^{T}\overline{x}_{i}-t_{i})^2$$
ha soluzione 
$$\overline{w}^{\star}(\overline{x})=\left(\overline{X}^{T}\Psi(\overline{x})\overline{X}\right)^{-1}\overline{X}^{T}\Psi(\overline{x})\mathbf t$$
dove $\Psi(\overline{x})$ è la matrice diagonale $n\times n$ con $\Psi(\overline{x})_{ii}=\psi_{i}(\overline{x})$

La predizione è quindi performata come al solito, ovvero come 
$$h(\overline{x})=\overline{w}^{\star}(\overline{x})^{T}\overline{x}$$
## Local Logistic Regression

Lo stesso approccio applicato nel caso della regressione locale può essere applicato alla classificazione, definendo una funzione di perdita ponderata da minimizzare, con pesi dipendenti dall'elemento il cui target deve essere previsto.

In questo caso, viene considerata una versione ponderata della funzione di **entropia incrociata** (***cross entropy***) [^1], che deve essere massimizzata.

$$L(\overline{x})=\sum\limits_{i=1}^{n}\mathbf k_{h}(\overline{x}-\overline{x}_{i})(t_{i}\log p_{i}-(1-t_{i})\log(1-p_{i})),\quad p_{i}=\sigma(\overline{w}^{T}\overline{x}_{i})$$
# Processi Gaussiani
## Kernels
## Distribuzione a posteriori
## Gaussian process regression : gaussian noise

[^1]: vedi qua -> [La funzione di costo: cross-entropy](Gradient%20Descent.md#La%20funzione%20di%20costo%20cross-entropy)
