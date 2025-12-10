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

Nell'approcio discriminativo siamo interessati nel modellare $p(C_k|\mathbf x)$ 
In particolare, possiamo supporre che tale probabilità sia un GLM e, di conseguenza, ricavarne i coefficienti (ad esempio attraverso la stima ML)

Confronto rispetto all'approccio generativo:
- Meno informazioni derivate (non conosciamo $p(\mathbf x|C_k)$, quindi non siamo in grado di generare nuovi dati)
- Metodo più semplice, solitamente con un insieme più ridotto di parametri da derivare
- Previsioni migliori, se le ipotesi formulate rispetto a $p(\mathbf x|C_k)$ sono errate

## Logistic Regression

La **regressione logistica** è un GLM derivante dall'ipotesi di una distribuzione di Bernoulli di $t$, che porta a

$$p(C_{1}|\mathbf x)=\sigma(\overline{w}^{T}\overline{x})=\frac{1}{1+e^{-\overline{w}^{T}\overline{x}}}$$
dove, come al solito, possiamo applicare funzioni base

Il modello è equivalente, per il caso della classificazione binaria, alla regressione lineare per il caso di regressione
### Degrees of freedom

- La regressione logisitica richiede $d+1$ coefficienti $b,w_{1},\dots,w_{d}$ da derivare a partire dal training set
- Un'approccio generativo con distribuzioni Gaussiane richiede:
	- $2d$ coefficienti per le medie $\mathbf{\mu}_{1},\mathbf{\mu}_{2}$
	- per ogni matrice di covarianza servono $$\sum\limits_{i=1}^{d}i=\frac{d(d+1)}{2}\text{ coefficienti}$$
	- una probabilità a priori $p(C_{1})$
	- in totale, risultano quindi $d(d+1)+2d+1=d(d+3)+1$ coefficienti (se si assuma matrice di covarianza unica, allora il numero di coefficienti risulterà essere $\frac{d(d+1)}{2}+2d+1=\frac{d(d+5)}{2}+1$ coefficienti)

### Maximum Likelihood Estimation

Come indicato sopra, ipotizziamo che i target degli elementi del training set possano essere modellati in modo condizionale (rispetto ai coefficienti del modello) attraverso una distribuzione di Bernoulli. 

Cioè, ipotizziamo che
$$p(t_i|\mathbf x_{i};\mathbf{w})=p_{i}^{t_{i}}(1-p_{i})^{1-t_{i}}$$
dove:
- $p_{i}=p(C_{1}|\mathbf{x}_i)=\sigma(a_i)$
- $a_{i}=\overline{w}^{T}\overline{x}_{i}$

Allora, la verosimiglianza dei target $\mathbf{t}$ del training set, dato $\mathbf{X}$ è:
$$p(\mathbf{t}|\mathbf X;\overline{w})=L(\overline{w}|\mathbf X,\mathbf t)=\prod_{i=1}^{n}p(t_{i}|\mathbf x_i;\overline{w})=\prod_{i=1}^{n}p_{i}^{t_{i}}(1-p_{i})^{1-t_{i}}$$
e la log-verosimiglianza è:
$$l(\overline{w}|\mathbf X,\mathbf t)=\log L(\overline{w}|\mathbf X,\mathbf t)=\sum\limits_{i=1}^{n}(t_{i}\log p_i+(1-t_{i})\log(1-p_{i}))$$
Facendo le derivate parziali per $\overline{w}$ e $b$ si ottiene che:

$$\begin{align*}
\frac{\partial}{\partial w_{j}}l(\overline{w}|\mathbf X,\mathbf t)&=\sum\limits_{i=1}^{n}\frac{t_{i}-p_{i}}{p_{i}(1-p_i)}p_{i}(1-p_{i})x_{ij}\\
&=\sum\limits_{i=1}^{n}(t_{i}-p_{i})x_{ij}=\sum\limits_{i=1}^{n}(t_{i}-\sigma(\overline{w}^{T}\overline{x}_i))x_{ij}
\end{align*}$$
e
$$\frac{\partial}{\partial b}l(\overline{w}|\mathbf X,\mathbf t)=\sum\limits_{i=1}^{n}(t_{i}-\sigma(\overline{w}^{T}\overline{x}_{i}))$$

In notazione vettoriale otteniamo che

$$\nabla_{\overline{w}}l(\overline{w}|\mathbf X,\mathbf t)=\sum\limits_{i=1}^{n}(t_{i}-\sigma(\overline{w}^{T}\overline{x}_i))\overline{x}_{i}$$
Per massimizzare la verosimiglianza, applichiamo un algoritmo di discesa del gradiente, dove ad ogni iterazione viene performata la seguente operazione di aggiornamento della stima di $\mathbf w$

$$\begin{align*}
\overline{w}^{(j+1)}&=\overline{w}^{(j)}+\alpha\nabla_{\overline{w}}l(\overline{w}|\mathbf X,\mathbf t)\big|_{\overline{w}^{(j)}}\\
&=\overline{w}^{(j)}+\alpha\sum\limits_{i=1}^{n}(t_{i}-\sigma((\overline{w}^{(j)})^{T}\overline{x}_i))\overline{x}_{i}\\
&=\overline{w}^{(j)}+\alpha\sum\limits_{i=1}^{n}(t_{i}-h^{(j)}(\overline{x}_i))\overline{x}_{i}\\
\end{align*}$$
### Logistic Regression and GDA

Osserviamo che assumendo che sia $p(\mathbf x|C_1)$ che $p(\mathbf x|C_2)$ come distribuzioni normali multivariate con la stessa matrice di covarianza $\Sigma$ si ottiene una $p(C_1|\mathbf x)$ logistica.

Il contrario, tuttavia, non è vero in generale: infatti, la GDA si basa su ipotesi più forti rispetto alla regressione logistica.

Più viene verificata l'ipotesi di normalità delle distribuzioni condizionate di classe con la stessa covarianza, più la GDA tenderà a fornire i modelli migliori per $p(C_1|\mathbf x)$

La regressione logistica si basa su ipotesi più deboli rispetto alla GDA: è quindi meno sensibile alla correttezza limitata di tali ipotesi, risultando così una tecnica più robusta

Poiché $p(C_i|\mathbf x)$ è logistica in un ampio insieme di ipotesi su $p(\mathbf x|C_{i})$, fornirà solitamente soluzioni migliori (modelli) in tutti questi casi, mentre la GDA fornirà modelli meno efficaci nella misura in cui le ipotesi di normalità sono meno verificate

### Softmax Regression

Per estendere l'approccio della regressione logistica al caso $K \gt 2$, consideriamo la matrice $\overline{W} = (\mathbf w_0, \mathbf w_1,\dots ,\mathbf w_K )$ dei coefficienti del modello, di dimensione $(d + 1)\times K$, dove $\mathbf w_j$ è il vettore $(d + 1)$-dimensionale dei coefficienti per la classe $C_j$ . 

In questo caso, la verosimiglianza è definita come
$$p(\mathbf T|\mathbf X,\overline{W})=\prod_{i=1}^{n}\prod_{k=1}^{K}y_{ik}^{t_{ik}}$$
dove
$$y_{ik}^{t_{ik}}=p(C_{k}|x_{i})=\frac{e^{\overline{w}_{k}^{T}\overline{x}_{i}}}{\sum\limits_{r=1}^{K}e^{\overline{w}_{r}^{T}\overline{x}_{i}}}$$
e $\mathbf T$ è la matrice di dimensione $n\times K$, dove la riga $i$-esima contiene la rappresentazione "1-to-$K$" di $t_{i}$

Cioè, se $x_{i}\in C_{k}$ allora $t_{ik}=1$ e $t_{ir}=0$ per ogni $r\neq k$
#### ML and Softmax Regression

La log-verosimiglianza è definita come:
$$l=\sum\limits_{i=1}^{n}\sum\limits_{k=1}^{K}t_{ik}\log y_{ik}$$
E il gradiente è definito come:
$$\nabla_{\overline{w}}l=(\nabla_{\overline{w}_{1}}l,\dots,\nabla_{\overline{w}_{K}}l)$$
dove 
$$\nabla_{\overline{w}_K}l=\sum\limits_{i=1}^{n}(t_{ik}-y_{ik})\overline{x}_{i}$$
Osserviamo che il gradiente ha la stessa struttura che aveva nel caso della regressione lineare e della regressione logistica


[^1]: it.wikipedia.org/wiki/Isosuperficie
