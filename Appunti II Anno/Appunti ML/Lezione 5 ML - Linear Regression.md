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
# Modelli Lineari

I modelli lineari sono basati su combinazione lineare delle feature in inputs:
$$h(\overline{x};w_{1},\dots,w_{d},b)=w_{1}x_{1}+\dots+w_{d}x_{d}+b$$
dove $b$ è chiamato **bias**

In maniera più compatta possiamo scrivere che 
$$h(\overline{x};\overline{w},b)=\overline{w}^{T}\overline{x}+b=(w_{1},w_{2},\dots,w_{d})\cdot\begin{pmatrix}x_{1}\\x_{2}\\\vdots\\x_{d}\end{pmatrix}+b$$
Osserviamo che tali modelli sono lineari **sia rispetto alle feature** che, cosa ancora più importante, anche **rispetto ai parametri**. 

Ciò è rilevante poiché, durante la fase di apprendimento dei modelli, i parametri sono trattati come variabili.

In generale, l'insieme delle caratteristiche può essere modificato (in particolare, esteso) mediante un insieme di funzioni di base predefinite $\phi_1, \dots , \phi_m$ definite come $\phi_i : \mathbb R^{d}\to\mathbb R$.

Cioè, ogni vettore $\overline{x} \in\mathbb R^d$ viene mappato su un nuovo vettore in $R^m, \phi(\overline{x}) = (\phi_1(\overline{x}),\dots , \phi_m(\overline{x}))$.

Il task di predizione viene mappato da uno spazio $d$-dimensionale a uno spazio $m$-dimensionale (di solito con $m \gt d$). 

Si tratta di un'azione che riguarda il **feature engineering**, che riguarda la ricerca di una rappresentazione efficace degli elementi di dati da cui devono essere effettuate le previsioni.

Chiaramente, l'applicazione delle funzioni di base non modifica la linearità di un modello lineare, che ha quindi la struttura
$$h(\overline{x};\overline{w},b)=\sum\limits_{j=1}^{m}w_{j}\phi_{j}(\overline{x})+b$$
Le funzioni base più famose sono:
- Polinomiale (funzioni globali) $$\phi_{j}(x)=x^{j}$$
- Gaussiana (locale) $$\phi_{j}(x)=e^{-\frac{(x-\mu_{j})^{2}}{2s^{2}}}$$
- Sigmoide (locale) $$\phi_{j}(x)=\sigma\left(\frac{x-\mu_{j}}{s}\right)=\frac{1}{1+e^{-\frac{x-\mu_{j}}{s}}}$$
- Tangente iperbolica (locale) $$\phi_{j}(x)=\tanh(x)=2\sigma(x)-1=\frac{1-e^{-\frac{x-\mu_{j}}{s}}}{1+e^{-\frac{x-\mu_{j}}{s}}}$$
Osserviamo che l'insieme degli elementi $$\overline{X}=\begin{pmatrix}\overline{x}_{1}\\\vdots\\\overline{x}_{n}\end{pmatrix}=\begin{pmatrix}x_{11}&x_{12}&\dots&x_{1d}\\x_{21}&x_{22}&\dots&x_{2d}\\\vdots\\x_{1n}&x_{2n}&\dots&x_{nd}\end{pmatrix}$$
viene trasformato, dall'insieme di funzioni base $\phi$ nella matrice:
$$\Phi=\begin{pmatrix}\phi_{1}(\overline{x}_{1})&\phi_{2}(\overline{x}_{1})&\dots&\phi_{m}(\overline{x}_{1})\\\phi_{1}(\overline{x}_{2})&\phi_{2}(\overline{x}_{2})&\dots&\phi_{m}(\overline{x}_{2})\\\vdots\\\phi_{1}(\overline{x}_{n})&\phi_{2}(\overline{x}_{n})&\dots&\phi_{m}(\overline{x}_{n})\end{pmatrix}$$

Di seguito, per semplicità, faremo riferimento al training set originale $(\overline{X}, t)$. 

È previsto che tutte le considerazioni possano essere applicate se vengono applicate funzioni di base, trattando quindi il dataset trasformato $\Phi$.

Vedere esempio su $t=\sin(2\pi x)$
## Regression Loss

Quando applichiamo le funzioni base, otteniamo che $h(\overline{x};\overline{w},b)$ diventa una funzione non lineare di $\overline{x}$, ma rimane comunque una funzione lineare di $\overline{w},b$

I valori assegnati ai coefficienti dovrebbero minimizzare il rischio empirico calcolato rispetto ad una **funzione di errore** (nota anche come **funzione di costo**), quando applicati ai dati nel training set (quindi, a $\overline{x}, t$ e $\overline{w}, b$).

Una funzione di errore ampiamente adottata è la **perdita quadratica** $(h(x_i; \overline{w}, b) − t_i)^2$, che si traduce nell'approccio dei **minimi quadrati**, ovvero minimizzare la somma, per tutti gli elementi nel training set, della differenza (al quadrato) tra il valore restituito dal modello e il valore target.

![center|400](Pasted%20image%2020251111111102.png)

Risulta quindi che 
$$
E(\overline{w},b)= \frac{1}{2}\sum\limits_{i=1}^{n}r_{i}(\overline{w},b)^{2}
$$
dove:
- $E(\overline{w},b)$ è l'errore dello scarto quadratico
- $r_{i}(\overline{w},b)=h(x_{i};\overline{w},b)-t_{i}=\sum\limits_{j=1}^{d}w_{j}x_{ij}+b-t_{i}$ è il **residuo** per l'elemento $(x_{i},t_{i})$ se $\overline{w},b$ sono i valori dei parametri applicati

Scrivendo $\overline{w}^{\star}=(b,w_{1},\dots,w_{d})^{T}$ possiamo riscrivere, in maniera più compatta
$$E(\overline{w}^{\star})= \frac{1}{2}\sum\limits_{i=1}^{n}r_{i}(\overline{w}^{\star})^{2}$$
con $r_i(\overline{w}^\star)=r_{i}(\overline{w},b)$

Tutto questo è chiaramente equivalente a minimizzare il rischio empirico $\overline{\mathcal R}(\overline{w}^{\star})$, dato che 
$$E(\overline{w}^{\star})=\frac{|\mathcal T|}{2}\overline{\mathcal R}(\overline{w}^{\star})$$

Per minimizzare $E(\overline{w}^{\star})$, impostiamo le sue derivate rispetto ai valori $w_{1},\dots,w_{d},b$ a $\overline{0}$ [^1]

Dato che la quadratic loss è una funzione convessa, è definito un singolo minimo (globale)

L'errore $E(\overline{w}^{\star})=\frac{1}{2}\sum\limits_{i=1}^{n}(h(x_{i};\overline{w}^{\star})-t_{i})^{2}$ è la somma di $n$ *funzioni convesse* $(h(x_{i};\overline{w}^{\star})-t_{i})^{2}$, che implica che è definito un singolo minimo (globale)

In particolare, $E(\overline{w}, b)$quadratico implica che la sua derivata è lineare, quindi che è zero in un punto $\overline{w}^{\star}$: il predittore risultante è quindi $$h(\overline{x};\overline{w}^{\star})=\sum\limits_{i=1}^{d}w_{i}^\star x_{i}+b^{\star}$$
Il gradiente in rispetto a $\overline{w}^\star$ è quindi una collezione di derivate
Otteniamo quindi un sistema lineare composto da
$$\begin{align*}&\frac{\partial E(\overline{w}^{\star})}{\partial w_{k}}=2\sum\limits_{i=1}^{n}r_{i}(\overline{w}^{\star})\frac{\partial}{\partial w_{k}}r_{i}(\overline{w}^{\star})=2\sum\limits_{i=1}^{n}r_{i}(\overline{w}^{\star})x_{ik}=2\sum\limits_{i=1}^{n}\left(\sum\limits_{j=1}^{d}w_{j}x_{ij}+b-t_{i}\right)x_{ik},\forall k=1,\dots,d\\&\frac{\partial E(\overline{w}^{\star})}{\partial b}=2\sum\limits_{i=1}^{n}r_{i}(\overline{w}^{\star})\frac{\partial}{\partial b}r_{i}(\overline{w}^{\star})=2\sum\limits_{i=1}^{n}r_{i}(\overline{w}^{\star})=2\sum\limits_{i=1}^{n}\left(\sum\limits_{j=1}^{d}w_{j}x_{ij}+b-t_{i}\right)\end{align*}$$
dato che $$\frac{\partial}{\partial w_{k}}r_{i}(\overline{w}^{\star})=\frac{\partial}{\partial w_{k}}h(x_{i})$$
Ognuna delle $d+1$ equazioni è lineare rispetto ad ogni coefficiente in $\overline{w}^{\star}$

Il sistema lineare risultante è quindi formato da $d+1$ equazioni e $d+1$ variabili sconosciute $w_{1},\dots,w_{d},b$, e lo scriviamo così
$$\overline{X}\overline{w}^\star=t$$
dove 
$$\overline{X}=\begin{pmatrix}\overline{x}_{1}\\\overline{x}_{2}\\\vdots\\\overline{x}_{n}\end{pmatrix}=\begin{pmatrix}1&x_{11}&\dots&x_{1d}\\1&x_{21}&\dots&x_{2d}\\\vdots\\1&x_{n1}&\dots&x_{nd}\end{pmatrix}$$
In generale, ad eccezione dei casi degenerati (dovuti a punti collineari nel dataset), questo sistema ha precisamente una sola soluzione, che può essere espressa in forma chiusa dalle **equazioni normali per i minimi quadrati**, ovvero:
$$\boxed{\overline{w}^\star=\left(\overline{X}^{T}\overline{X}\right)^{-1}\overline{X}^{T}t}$$
Il minimo di $E(\overline{w})$ può essere calcolato numericamente, usando i metodi di **discesa del gradiente** aventi la seguente struttura:
1. Assegnazione iniziale $\overline{w}^{(0)}=\left(b^{(0)},w_1^{(0)},\dots,w_{d}^{(0)}\right)$ con errore corrispondente $$E\left(\overline{w}^{(0)}\right)= \frac{1}{2}\sum\limits_{i=1}^{n}r_{i}\left(\overline{w}^{(0)}\right)^2$$
2. 
## Come limitare la complessità del modello? - Regolarizzazione
# Modello Probabilistico per Regressione
## Fully Bayesian
### FUlly Bayesian e marginalizzazione dell'iperparametro

[^1]: questo è il vettore nullo, composto da tutti zeri, $\overline{0}=(0,\dots,0)^{T}$
