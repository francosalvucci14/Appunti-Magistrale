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

![center|500](img/Pasted%20image%2020251116160017.png)

Osserviamo infine che, invece di introdurre funzioni di base che alla fine danno luogo a un kernel equivalente, possiamo seguire lo stesso approccio di previsione mediante una combinazione lineare di valori target, con pesi calcolati da un **kernel localizzato adeguato**, definito su una coppia di elementi (cioè su $\mathbb R^d \times \mathbb R^d$) e che restituisce un valore reale
# Kernel Regression

Nei metodi di regressione kernel, il valore target corrispondente a qualsiasi elemento $\overline{x}$ viene predetto facendo riferimento agli elementi nel training set, e in particolare agli elementi più vicini a $\overline{x}$.

Ciò viene controllato facendo riferimento a una funzione kernel predefinita $\mathbf k_h(\overline{x})$, che restituisce valori non trascurabili solo in un intervallo intorno a 0.

Un kernel possibile e comune è il *kernel gaussiano* (o *RBF*), rappresentato graficamente di seguito nel caso $d = 1$ per diversi valori dell'iperparametro $h$.
$$g(\overline{x})=e^{-\frac{||\overline{x}||^{2}}{2h^{2}}}$$
![center|500](img/Pasted%20image%2020251116160417.png)

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

È possibile ottenere risultati identici ai precedenti in modo alternativo ed equivalente considerando l'inferenza direttamente nello spazio delle funzioni $f : \mathbb R^d\to\mathbb R$. 

Utilizziamo un **processo gaussiano** (***GP***) per descrivere una distribuzione sulle funzioni. [^2]

Più formalmente:
- Un **processo stocastico** $f(\overline{x})$ è un insieme di variabili casuali (possibilmente infinite), $\{f(\overline{x}) : \overline{x}\in\chi\}$, ovvero i valori assunti dalla funzione $f$ sul dominio di $\chi$. Si osservi che $f$ è completamente descritto da tali valori.
- Un processo stocastico è un **processo gaussiano** se per ogni sottoinsieme finito $\mathbf X = (\overline{x}_1,\dots ,\overline{x}_n)$ di $\chi$, i valori della funzione $f(\overline{x}_1), \dots , f(\overline{x}_n)$ hanno una distribuzione gaussiana multivariata congiunta.

Nel caso più generale, $\chi = \mathbb R^d$, ma si possono considerare casi più semplici, ad esempio con $|\chi|$ finito. 

Si noti che in questo caso, se $|\chi| = d$, ciò corrisponde ad affermare che la distribuzione multivariata congiunta $\{f(\overline{x}_i) : i = 1, \dots , d\}$ è una gaussiana, da cui, per le proprietà della distribuzione gaussiana, deriva che la distribuzione di qualsiasi sottoinsieme di punti $\{f(\overline{x}_i) : i \in\mathbf I \subset \{1,\dots, d\}\}$ è essa stessa una gaussiana.

I processi gaussiani sono quindi una generalizzazione delle gaussiane multivariate congiunte $d$-dimensionali che le estendono all'infinito $d$

Per specificare il processo gaussiano nel caso generale di $\chi$ infinito, dobbiamo introdurre due regole che, per qualsiasi insieme di punti $\mathbf X = (\overline{x}_1,\dots ,\overline{x}_n)$, definiscono la distribuzione $p(f(\overline{x}_1), \dots , f(\overline{x}_n))$ dei valori corrispondenti

- Sappiamo già che, per ipotesi, la distribuzione $p(f(\overline{x}_1), \dots , f(\overline{x}_n))$ è una distribuzione normale multivariata $m$-dimensionale, caratterizzata quindi da un **vettore delle medie** $\mu_X$ e da una **matrice di covarianza** $\Sigma_X$ .
- Per quanto riguarda la media, definiamo una funzione $m(\overline{x})$ che per ogni punto $\overline{x}_i$ restituisce l'aspettativa della distribuzione di $f(\overline{x}_i)$, che è gaussiana poiché qualsiasi marginale di una distribuzione gaussiana come $p(f(\overline{x}_1), \dots , f(\overline{x}_n))$ è essa stessa gaussiana. Di conseguenza, $\mu_X = (m(\overline{x}_1),\dots , m(\overline{x}_m))$. Un possibile valore per $\mu_X$ potrebbe essere semplicemente l' insieme dei valori target $t_1,\dots , t_m$, ovvero $m(\overline{x}_i) = t_i$, supponendo che il valore osservato per $f(\overline{x}_i)$ (o la sua approssimazione) fornito da $t_i$ corrisponda all'aspettativa di $p(f(\overline{x}_i))$. Tuttavia, vedremo in seguito che ipotizzare $\mu_X = \mathbf 0$ non limita le capacità di previsione dell'approccio, poiché l'effetto delle medie diverse da zero può essere preso in considerazione in un secondo momento, come fase finale.
- La matrice di covarianza deriva dall'applicazione di una **funzione di covarianza** predefinita $\mathbf k : \chi\times\chi\to\mathbb R$ che associa un valore reale a qualsiasi coppia di punti in $\chi$ e, in particolare, a qualsiasi coppia in $X$, quindi a tutti gli elementi di $\Sigma_X$

La funzione di covarianza è assunta essere un **kernel definito positivo** : questo significa che per insieme di punti distinti $\overline{x}_{1},\dots,\overline{x}_{n}$ deve valere che 
$$\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}c_{i}c_{j}\mathbf k(\overline{x}_{i},\overline{x}_{j})\gt0$$
per ogni scelta delle costanti $c_1,\dots,c_{n}$ tali che non tutte le $c_{i}$ siano uguali a $0$

In modo del tutto equivalente, anche la matrice quadrata di **Gram** $G_{X}$, definita come 
$$G_{X}=\begin{pmatrix}\mathbf k(\overline{x}_{1},\overline{x}_{1})&\mathbf k(\overline{x}_{1},\overline{x}_{2})&\dots&\mathbf k(\overline{x}_{1},\overline{x}_{n})\\\mathbf k(\overline{x}_{2},\overline{x}_{1})&\mathbf k(\overline{x}_{2},\overline{x}_{2})&\dots&\mathbf k(\overline{x}_{2},\overline{x}_{n})\\\vdots\\\mathbf k(\overline{x}_{n},\overline{x}_{1})&\mathbf k(\overline{x}_{n},\overline{x}_{2})&\dots&\mathbf k(\overline{x}_{n},\overline{x}_{n})\end{pmatrix}$$
deve avere autovalori positivi

Una collezione di kernel definiti positivi è nota in letteratura e può essere costruita applicando regole adeguate.

Pertanto, un processo gaussiano può essere interpretato come una distribuzione su funzioni la cui forma (uniformità, ...) è definita da $\mathbf k$.

Se i punti $\overline{x}_i$ e $\overline{x}_j$ sono considerati simili (cioè $\mathbf k(\overline{x}_{i},\overline{x}_{j})$ è piccolo) ci si può aspettare che anche i valori della funzione in questi punti, $f(\overline{x}_i)$ e $f(\overline{x}_j)$, siano simili
## Kernels

Chiaramente, diversi kernel generano diversi processi: uno dei più applicati è il kernel RBF
$$\mathbf k_{h}(\overline{x}_1,\overline{x}_{2})=\sigma^2e^{-\frac{||\overline{x}_{1}-\overline{x}_{2}||^{2}}{2\tau^{2}}}$$
questa tipologia di kernel tende ad assegnare un'altra covarianza fra $f(\overline{x}_1)$ e $f(\overline{x}_{2})$ se $\overline{x}_{1},\overline{x}_2$ sono punti vicini

Le funzioni ricavate da un processo gaussiano con kernel RBF tendono ad essere uniformi, poiché i valori calcolati per punti vicini tendono ad essere simili. 

La uniformità è maggiore per $\tau$ più grande.

Di seguito sono riportati due esempi di campioni di funzioni su $\mathbb R$ (effettivamente approssimate su una griglia di valori): si ipotizza un kernel RBF, con $\tau$ più grande nella prima immagine e $\tau$ più piccolo nella seconda.

![center|500](img/Pasted%20image%2020251117103144.png)

## Distribuzione a posteriori

Il processo gaussiano $GP\left(m(\overline{x}),\mathbf k\left(\overline{x},\overline{x}^{'}\right)\right)$ può essere visto come una distribuzione $p(f)$ di funzioni, che sono indipendenti dai punti attuali del dataset

In termini bayesiani, si tratta di un prior rispetto all'osservazione dei valori effettivi $(\overline{x}_i, t_i)$, dove $t_i$ è per ipotesi il valore che si presume sia effettivamente assunto da qualsiasi funzione campionata da $p(f )$.

Ciò è vero in particolare per l'insieme $X$ di $m$ punti nel dataset. 

Si noti che qui non stiamo prendendo in considerazione i valori target $\mathbf t$. 

Abbiamo quindi una distribuzione gaussiana di vettori $m$-dimensionali, che possono essere interpretati come funzioni che vanno da $X$ a $\mathbb R$
$$p(f)=\mathcal N(f;\mu_{X},\Sigma_{X})$$

Nella figura sottostante, il grafico rosso rappresenta la funzione sconosciuta $f (x)$ da approssimare, mentre quelli blu più sottili sono funzioni campionate da $p(f )$ ($X$ è una griglia di punti sull'asse $x$).

![center|500](img/Pasted%20image%2020251117104042.png)

Supponiamo ora che ciascun valore target corrisponda esattamente al valore associato al punto $\overline{x}_i$ restituito dalla definizione della funzione sconosciuta $f$ da approssimare, ovvero $t_i = f (\overline{x}_i)$.

In altri termini, supponiamo che non vi sia alcun rumore nelle nostre osservazioni della funzione sconosciuta $f$. 

Si noti che nel modello probabilistico di regressione ciò non è vero, poiché si ipotizza un errore (gaussiano).

Per definizione di processo gaussiano, se ora consideriamo un insieme aggiuntivo di punti $\mathbf Z = (\mathbf z_1,\dots , \mathbf z_r)^T$ , la distribuzione congiunta di $f (\overline{x}_1),\dots , f (\overline{x}_m), f (\mathbf z_1),\dots , f (\mathbf z_r)$ è una gaussiana multivariata $(m + r)$-dimensionale con media $\mu_{(X,\mathbf Z)} = (\mu_X, \mu_{\mathbf Z} )$ e matrice di covarianza
$$\Sigma_{(X,\mathbf Z)}=\begin{pmatrix}G_X&G_{\mathbf Z,X}\\G_{\mathbf Z,X}^{T}&G_{\mathbf Z}\end{pmatrix}$$
dove
$$G_{\mathbf Z,X}=\begin{pmatrix}\mathbf k(\mathbf z_{1},\overline{x}_{1})&\mathbf k(\mathbf z_{1},\overline{x}_{2})&\dots&\mathbf k(\mathbf z_{1},\overline{x}_{m})\\\mathbf k(\mathbf z_{2},\overline{x}_{1})&\mathbf k(\mathbf z_{2},\overline{x}_{2})&\dots&\mathbf k(\mathbf z_{2},\overline{x}_{m})\\\vdots\\\mathbf k(\mathbf z_{r},\overline{x}_{1})&\mathbf k(\mathbf z_{r},\overline{x}_{2})&\dots&\mathbf k(\mathbf z_{r},\overline{x}_{m})\end{pmatrix}$$

Desideriamo ricavare la distribuzione predittiva di $f (\mathbf z_1),\dots , f (\mathbf z_r)$ dati $\mathbf z_1,\dots , \mathbf z_r, \overline{x}_1, \dots , \overline{x}_m$ e $t_1, \dots , t_m$, che, in base all'ipotesi di assenza di rumore, è uguale a $f (\overline{x}_1),\dots , f (\overline{x}_m)$. 

Cioè, desideriamo ricavare la distribuzione condizionata $$p(f (\mathbf Z)|\mathbf Z, X, f (X))$$
Per farlo, ricordiamo innanzitutto alcune proprietà utili delle distribuzioni gaussiane multivariate, che possiamo trovare [qui - pag.8](https://tvml.github.io/ml2526/note/6-nonparam-regr-notes.pdf)

Da queste proprietà, impostando $\overline{x}_{A}=f(X)$ e $\overline{x}_{B}=f(\mathbf Z)$, otteniamo che 
$$p(f(\mathbf Z)|\mathbf Z,X,f(X))=p(f(\mathbf z_{i}),\dots,f(\mathbf z_{r})|\mathbf z_{1},\dots,\mathbf z_{r},\overline{x}_{1},\dots,\overline{x}_{m},f(\overline{x}_{1}),\dots,f(\overline{x}_{m}))$$
risulta essere una distribuzione gaussiana $r$-dimensionale con media e covarianza definite come:
$$\begin{align*}
&\mu_{pr}=\mu_{\mathbf Z}+G_{\mathbf Z,X}G_{X}^{-1}(\mathbf t-\mu_{X})\\
&\Sigma_{pr}=G_{\mathbf Z}-G_{\mathbf Z,X}G_{X}^{-1}G_{\mathbf Z,X}^{T}
\end{align*}$$

Si osservi che anche nell'ipotesi semplificativa che $(\mu_X, \mu_{\mathbf Z} ) = \mathbf 0$, ovvero che $m(\overline{x})$ sia pari a $0$ per tutti gli $\overline{x}$ (e $\mathbf z$), la media della distribuzione predittiva può risultare diversa da zero. 

Infatti, in tal caso, sarebbe
$$\mu_{pr}=G_{\mathbf Z,X}G_{X}^{-1}\mathbf t$$

Tuttavia, dalla prima equazione sopra riportata, anche nel caso generale di qualsiasi definizione di $m(\overline{x})$, possiamo supporre che $m(\overline{x}) = 0$, ottenendo $\mu_{pr}=G_{\mathbf Z,X}G_{X}^{-1}\mathbf t$, e successivamente modificare tale valore come
$$\mu_{pr}=\mu_{pr}+\mu_{\mathbf Z}-G_{\mathbf Z,X}G_{X}^{-1}\mu_{X}$$
per tenere conto delle aspettative presunte diverse da zero. 

Ciò dimostra che avremmo potuto effettivamente considerare il caso $m(\overline{x}) = 0$ nelle considerazioni precedenti senza perdita di generalità.

Il campionamento di diverse funzioni da tale distribuzione predittiva porta alla seguente situazione: ancora una volta, il grafico rosso è la funzione sconosciuta $f$ i cui valori in 5 punti sono ora noti, mentre il grafico blu sono campioni dalla distribuzione posteriore $\mathcal N (x|\mu_{pr}, \Sigma_{pr})$. 

Si osservi che tutte queste funzioni hanno gli stessi valori di $f$ nei 5 punti

![center|500](img/Pasted%20image%2020251117113053.png)

Le stesse considerazioni valgono, in particolare, per la previsione di un singolo punto di test $\mathbf z$ dato il training set $X, \mathbf t$. 

Secondo quanto mostrato sopra, la distribuzione predittiva di $f (\overline{x})$ è una distribuzione gaussiana con media e varianza
$$\begin{align*}
&\mu_{pr}=G_{\mathbf z,X}G_{X}^{-1}(\mathbf t-\mu_{X})\\
&\sigma_{pr}^{2}=\mathbf k(\mathbf z,\mathbf z)-G_{\mathbf z,X}G_{X}^{-1}G_{\mathbf z,X}^{T}
\end{align*}$$
Nella figura sottostante, il valore medio della distribuzione predittiva di $f (x)$ per ciascun punto $x$, dati i 5 punti indicati sul grafico rosso, è mostrato come un grafico blu, con la varianza corrispondente riportata dall'intervallo giallo intorno a tale grafico.

![center|500](img/Pasted%20image%2020251117113547.png)

Come già osservato, in questo caso è stata eseguita un'**interpolazione** dei valori dati, ovvero $f (\overline{x}_i) = t_i$ per tutte le funzioni possibili, campionate da $p(f |X, \mathbf t))$.

Ne risulta, infatti, per tutti gli $x_i \in X$
$$\begin{align*}
\mu(f(\overline{x}_{i})|X,\mathbf t)=t_{i}\\
\sigma^{2}=0
\end{align*}$$

## Gaussian process regression : gaussian noise

Se formuliamo l'ipotesi più realistica che ogni valore target $t_i$ fornisca solo un'osservazione rumorosa di $f (\overline{x}_i)$, potremmo comportarci come nella definizione del modello probabilistico per la regressione lineare: in particolare, potremmo formulare l' ipotesi di un rumore gaussiano, quindi che $p(t_i|f, \overline{x}_i) = \mathcal N (f (\overline{x}_i), \sigma^2_{f} )$, mentre in precedenza avevamo ipotizzato $t_i = f (\overline{x}_i)$.

Allora il valore ti osservato per la variabile xi differisce da quello ottenuto come $f (\overline{x}_i)$ da un rumore gaussiano e indipendente
$$t_i=f(\overline{x}_{i})+\varepsilon\quad p(\varepsilon)=\mathcal N(\varepsilon;0,\sigma^{2}_{f})$$
In base a queste ipotesi, per la distribuzione a priori sulle osservazioni rumorose abbiamo che la varianza di $f (\overline{x}_i)$ è aumentata, rispetto al caso precedente, dell'incertezza derivata dal rumore, che ha varianza $\sigma^2_f$.

Di conseguenza, abbiamo che
$$\begin{align*}
&\Sigma_{X}[i,j]=\mathbf k(\overline{x}_{i},\overline{x}_{j})\quad i\neq j\\
&\Sigma_{X}[i,i]=\mathbf k(\overline{x}_{i},\overline{x}_{j})+\sigma^{2}_{f}
\end{align*}$$
Come conseguenza, la matrice di covarianza $\Sigma_{X}$ risulta essere:
$$\Sigma_{X}=G_{X}+\sigma_{f}^{2}$$

![center|500](img/Pasted%20image%2020251117122735.png)



[^1]: vedi qua -> [La funzione di costo: cross-entropy](Gradient%20Descent.md#La%20funzione%20di%20costo%20cross-entropy)

[^2]: Per semplicità di notazione, ci riferiamo qui ai punti originali del training set $\overline{x}_1,\dots , \overline{x}_n$ invece di utilizzare la notazione più generale $\phi{\overline{x}_1},\dots ,\phi( \overline{x}_n)$ con punti ottenuti applicando un insieme di funzioni di base. Tutte le considerazioni riportate di seguito si applicano chiaramente se $\phi(\overline{x})$ viene sostituito a $\overline{x}$
