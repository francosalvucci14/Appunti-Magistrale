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

## Come limitare la complessità del modello? - Regolarizzazione
# Modello Probabilistico per Regressione
## Fully Bayesian
### FUlly Bayesian e marginalizzazione dell'iperparametro
