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
# Generalized Linear Models

Nei casi considerati di seguito, le distribuzioni a posteriori delle classi $p(C_{k}|\textbf{x})$ sono sigmoidali o softmax con argomento dato da una combinazione lineare di $\textbf{x}$, ad esempio, sono istanze dei **modelli lineari generalizzati**

Definiamo cos'è un GLM

>[!definition]- GLM - Generalized Linear Model
>È una funzione del tipo $$h(\textbf{x})=f(\mathbf{w}^{T}\mathbf{x}+b)=f(\overline{w}^{T}\overline{x})$$
>
>dove $f$ (spesso chiamata *funzione di risposta*) è in generale una funzione ***non-lineare***

Ogni **iso-superficie** [^1] di $h(\mathbf{x})$, tale che per definizione $h(\mathbf{x})=c$ (per una qualche costante $c$) è tale che:
$$f(\overline{w}^{T}\overline{x})=c$$
e
$$\overline{w}^{T}\overline{x}=f^{-1}(t)=c^{'}$$
Quindi, le iso-superfici di un GLM sono iperpiani, e questo implica che i confini sono anch'essi iperpiani
## Exponential Families and GLM

Assumiamo di voler predirre una variabile random $t$ come una funzione di un insieme diverso di v.a $\mathbf{x}$
Per definizione, un modello di previsione per questo task è un GLM se valgono le seguenti condizioni:
1. la distribuzione condizionale $p(t|\mathbf{x})$ appartiene ad una **famiglia esponenziale**; ovvero, possiamo riscrivere la probabilità come: $$p(t|\mathbf{x})=\frac{1}{s}g(\theta(\mathbf{x}))f\left(\frac{t}{s}\right)e^{\frac{1}{s}\theta(\mathbf{x})^{T}\mathbf{u}(t)}$$per qualche $\theta,g,\mathbf{u}$, dove:
	1. $g(\theta(\mathbf{x}))$ è la funzione di attivazione (funzione di risposta)
	2. $\mathbf{u}(t)$ è la ***statistica sufficiente***
2. per ogni $\mathbf{x}$, vogliamo predirre il valore atteso di $\mathbf{u}(t)$ dato $\mathbf{x}$, ovvero $\mathbb E[\mathbf{u}(t)|\mathbf{x}]$
3. $\theta(\mathbf{x})$ (il **parametro naturale**) è combinazione lineare delle feature, ovvero $\theta(\mathbf{x})=\overline{w}^{T}\overline{x}$

Vediamo ora il rapporto fra GLM e le varie distribuzioni note
## GLM and Normal Distribution

Vediamo i tre punti
1. Assumiamo che $t\in\mathbb R$ e $p(t|\mathbf{x})=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(t-\mu(\mathbf{x}))^{2}}{2\sigma^{2}}}$ è una distribuzione Normale con media $\mu(\mathbf{x})$ e varianza costante $\sigma^{2}$: è facile verificare che $$\theta(\mathbf{x})=\begin{pmatrix}\theta_{1}(\mathbf{x})\\\theta_{2}\end{pmatrix}=\begin{pmatrix}\mu(\mathbf{x})/\sigma^{2}\\-1/2\sigma^{2}\end{pmatrix}$$e $\mathbf{u}(t)=t$
2. Vogliamo predirre il valore di $\mathbb E[\mathbf{u}(t)|\mathbf{x}]=\mathbb E[t|\mathbf{x}]=\mu(\mathbf{x})$ come $h(\mathbf{x})$, allora $$h(\mathbf{x})=\mu(\mathbf{x})=\sigma^{2}\theta_{1}(\mathbf{x})$$
3. Assumiamo che $\theta_{1}(\mathbf{x})$ è una combinazione lineare delle feature, ovvero $\theta_{1}(\mathbf{x})=\overline{w}^{T}\overline{x}$

Allora, abbiamo che
$$h(\mathbf{x})=\sigma^{2}\overline{w}^{T}\overline{x}$$
e risulta quindi una ***regressione lineare*** $h(\mathbf{x})=\overline{u}^{T}\overline{x}$ con $u_{i}=\sigma^{2}w_i,i=,\dots,d$

Per le distribuzioni Gaussiane otteniamo quindi il MSE (Mean Square Error, ovvero l'**errore quadratico medio**)
## GLM and Bernoulli Distribution

Vediamo i tre punti
1. Assumiamo che $t\in\{0,1\}$ e $p(t|\mathbf{x})=\pi(\mathbf{x})^{t}(1-\pi(\mathbf{x}))^{1-t}$ è una distribuzione di Bernoulli con parametro $\pi(\mathbf{x})$; allora il parametro naturale $\theta(\mathbf{x})$ risulterà essere $$\theta(\mathbf{x})=\log\frac{\pi(\mathbf{x})}{1-\pi(\mathbf{x})}$$e $\mathbf{u}(t)=t$
2. Vogliamo predirre il valore di $\mathbb E[\mathbf{u}(t)|\mathbf{x}]=\mathbb E[t|\mathbf{x}]=p(t=1|\mathbf{x})=\pi(\mathbf{x})$ come $h(\mathbf{x})$, allora $$h(\mathbf{x})=\frac{1}{1+e^{-\theta(\mathbf{x})}}$$
3. Assumiamo che $\theta_{1}(\mathbf{x})$ è una combinazione lineare delle feature, ovvero $\theta_{1}(\mathbf{x})=\overline{w}^{T}\overline{x}$

Allora, viene derivata una regressione logistica
$$h(\mathbf{x})=\frac{1}{1+e^{-\overline{w}^{T}\overline{x}}}$$
Abbiamo quindi cross-entropy
## GLM and Categorical Distribution

Vediamo i tre punti
1. Assumiamo $t\in\{1,\dots,K\}$ e $p(t|\mathbf{x})=\prod_{i=1}^{K}\pi_{i}(\mathbf{x})^{t_i}$ (dove $t_i=1$ se $t_{i}$, $t_{i}=0$ altrimenti) è una distrubuzione Categorica con probabilità $\pi_{1}(\mathbf{x}),\dots,\pi_K(\mathbf{x})$: il parametro naturale è quindi $\theta(\mathbf{x})=(\theta_1(\mathbf{x}),\dots,\theta_{K}(\mathbf{x}))^{T}$, con $$\theta_{i}(\mathbf{x})=\log\frac{\pi_i(\mathbf{x})}{\pi_K(\mathbf{x})}=\log\frac{\pi_i(\mathbf{x})}{1-\sum\limits_{j=1}^{K-1}\pi_j(\mathbf{x})}$$e $\mathbf{u}(t)=(t_{1},\dots,t_{K})^{T}$ è la rappresentazione $1$-of-$K$ di $t$
2. Vogliamo predirre $\mathbb E[u_{i}(t)|\mathbf{x}]=p(t=i|\mathbf{x})$ come $$h_{i}(\mathbf{x})=p(t=i|\mathbf{x})=\pi_i(\mathbf{x})=\pi_K(\mathbf{x})e^{\theta_{i}(\mathbf{x})}$$e dato che $\sum\limits_{j=1}^{K}\pi_i(\mathbf{x})=\pi_K(\mathbf{x})\sum\limits_{j=1}^{K}e^{\theta_{i}(\mathbf{x})}=1$, esce fuori che $$\pi_{K}(\mathbf{x})=\frac{1}{\sum\limits_{i=1}^{K}e^{\theta_{i}(\mathbf{x})}}\space\land\space\pi_{i}(\mathbf{x})=\frac{e^{\theta_{i}(\mathbf{x})}}{\sum\limits_{i=1}^{K}e^{\theta_{i}(\mathbf{x})}}$$
3. Assumiamo che tutti i $\theta_i(\mathbf{x})$ siano combinazioni lineari delle feature, quindi $\theta_{i}(\mathbf{x})=\overline{w}_{i}^{T}\overline{x}$

Allora, otteniamo una softmax regression
$$\begin{align*}
&h_{i}(\mathbf{x})=\frac{e^{\overline{w}_{i}^{T}\overline{x}}}{\sum\limits_{j=1}^{K}e^{\overline{w}_{j}^{T}\overline{x}}}\quad i=1,\dots,K-1\\
&h_{K}(\mathbf{x})=\frac{1}{\sum\limits_{j=1}^{K}e^{\overline{w}_{j}^{T}\overline{x}}}
\end{align*}$$
# Discriminative Approach



[^1]: it.wikipedia.org/wiki/Isosuperficie
