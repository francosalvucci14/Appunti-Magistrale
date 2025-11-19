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
# Classificazione Lineare

Nei problemi di classificazione abbiamo le seguenti regole:
- il valore da predirre $t$ è preso da un dominio discreto, dove ogni valore di $t$ denota una **classe**
	- caso più comune: classi disgiunte, ogni input viene assegnato esattamente ad una classe
- lo spazio degli input è partizionato in **regioni di decisione**
- nei **modelli di classificazione lineare** i confini decisionali sono funzioni lineari dell'input $\mathbf x$ (iperpiani a $d − 1$ dimensioni nello spazio delle feature a $d$ dimensioni)
- I dataset come le classi corrispondono a regioni che possono essere separate da confini decisionali lineari e sono detti **linearmente separabili**.

Vediamo il confronto fra regressione e classificazione:
- Regressione: il valore target è un vettore di reali $\mathbf t$
- Classificazione: vari modi per rappresentare le classi (i valori delle variabili target)

Un'esempio molto importante è la *Classificazione Binaria*
Qui abbiamo un singolo valore $t\in\{0,1\}$ dove $t=0$ indica la classe $C_{0}$ e $t=1$ indica la classe $C_{1}$

Se abbiamo $\mathbf K\gt2$ classi siamo nello spettro del "1 of $\mathbf K$" coding.
Qui, $\mathbf t$ è un vettore di $\mathbf K$ bits tali che, per ogni classe $C_{j}$ tutti i bit sono impostati a $0$ ad eccezzione del $j$-esimo, che viene messo a $1$

Abbiamo sostanzialmente $3$ approcci alla classificazione, che sono:
1. **funzione discriminativa** : Trovare la funzione $f:X\to\{1,\dots,\mathbf K\}$ che mappa ogni input $\mathbf x$ in una qualche classe $C_i$, tale che $i=f(\mathbf x)$
2. **approccio discriminativo** : Determinare la probabilità condizionata $p(C_j|\mathbf x)$ (***fase di inferenza***); usare questa distribuzione per assegnare un input ad una classe (***fase di decisione***)
3. **approccio generativo** : determinare le distribuzioni condizioni della classe $p(\mathbf x|C_{j})$ e le probabilità a priori $p(C_{j})$; applicare poi la regola di Bayes per derivare le probabilità a posteriori $p(C_{j}|\mathbf x)$; usare poi queste distribuzioni per assegnare un input ad una classe

Gli approcci $1,2$ sono **discriminativi**: affrontano il problema della classificazione derivando dal training set condizioni (come i confini decisionali) che, quando applicate a un punto, discriminano ciascuna classe dalle altre.

I confini tra le regioni sono specificati da **funzioni di discriminazione**

Nella regressione lineare, un modello prevede il valore target; la previsione viene effettuata tramite una funzione lineare $h(\mathbf x;\mathbf w, b) =\mathbf w^T\mathbf x + b = \overline{w}^T \overline{x}$ (è possibile applicare funzioni di base lineari). 

Nella classificazione, un modello prevede le probabilità delle classi, ovvero valori compresi tra $[0, 1]$; la previsione viene effettuata tramite un modello lineare generalizzato $h(\mathbf x;\mathbf w, b)= f(\mathbf w^T \mathbf x+b)$, dove $f$ è una **funzione di attivazione non lineare** con codominio $[0, 1]$

I confini corrispondono alla soluzione di $h(\mathbf x;\mathbf w, b)=c$ per una certa costante $c$; ciò si traduce in $\mathbf w^T\mathbf x + b = f^{-1}(c)$, ovvero un confine lineare. 

La funzione inversa $f^{-1}$ è detta **funzione di collegamento**.

L'approccio 3 è **generativo**: funziona definendo, dal training set, un **modello** di elementi per ciascuna classe

Il modello è una distribuzione di probabilità (di feature condizionate dalla classe) e potrebbe essere utilizzato per la generazione casuale di nuovi elementi nella classe. 

Confrontando un elemento con tutti i modelli, è possibile verificare quello che meglio si adatta

## Funzioni Discriminanti

Funzioni discriminanti lineare in classificazione binaria
- confini decisionali: *iperpiano* $(d-1)$-dimensionale di tutti i punti tali per cui $h(\mathbf x;\mathbf w, b)=\mathbf w^T\mathbf x + b=0$
- Dati due punti sull'iperpiano $\overline{x}_{1},\overline{x}_2$, la condizione $h(\overline{x}_{1};\mathbf w, b)=h(\overline{x}_{2};\mathbf w, b)=0$ è pari a $$\mathbf w^T\overline{x}_{1}+b-(\mathbf w^T\overline{x}_2+b)=\mathbf w^T(\overline{x}_{1}-\overline{x}_{2})$$ovvero, il vettore $\overline{x}_{1}-\overline{x}_{2}$ e $\mathbf w$ sono ortogonali
- Per ogni $\mathbf x$, il prodotto scalare $\mathbf w\cdot\mathbf x=\mathbf w^{T}\mathbf{x}$ è la lunghezza della proiezione di $\mathbf x$ nella direzione di $\mathbf w$ (ortogonale all'iperpiano $\mathbf w^T\mathbf x + b=0$ ), nei multipli di $||\mathbf w||_{2}$
- Normalizzando rispetto a $||\mathbf w||_{2}=\sqrt{\sum\limits_{i=1}^{d}w_{i}}$ , otteniamo la lunghezza della proiezione $\mathbf x$ nella direzione ortogonale all'iperpiano, assumendo che $||\mathbf w||_2=1$
- Per ogni $\mathbf x,h(\mathbf x;\mathbf w, b) =\mathbf w^T\mathbf x + b$ è la distanza (in multipli di $||\mathbf w||$) di $\mathbf x$ dall'iperpiano $\mathbf w^T\mathbf x + b=0$
- Il segno del valore restituito discrimina in quale delle regioni separate dall'iperpiano si trova il punto

![center|400](Pasted%20image%2020251118161235.png)

Funzioni discriminanti lineari in classificazione multiclasse
- Definiamo $\mathbf K$ funzioni lineari $$h_{i}(\mathbf x;\mathbf w_{i},b_{i})=\mathbf w_{i}^{T}\mathbf x+b_i\quad 1\leq i\leq\mathbf K$$ L'elemento $\mathbf x$ è assegnato alla classe $C_{k}$ se e solo se $h_{k}(\mathbf x;\mathbf w_{k},b_{k})\gt h_{i}(\mathbf x;\mathbf w_{i},b_{i})$ per ogni $i\neq k$, ovvero $k$ è quel valore che massimizza $h$, ovvero $$k=arg\max_{j}h_{j}(\mathbf x;\mathbf w_{j},b_{j})$$
- Confine decisionale tra $C_i$ e $C_j$ : tutti i punti $\mathbf x$ t.c $h_{i}(\mathbf x;\mathbf w_{i},b_{i})=h_{j}(\mathbf x;\mathbf w_{j},b_{j})$, un iperpiano $(d-1)$-dimensionale $$(\mathbf w_{i}-\mathbf w_{j})^{T}\mathbf x+(b_i-b_{j})=0$$

Le regioni decisionali risultanti sono connesse e convesse

![center|450](Pasted%20image%2020251119114121.png)

La definizione può essere estesa per includere termini relativi ai prodotti delle coppie di valori delle feature ( **funzioni discriminanti quadratiche**)

$$h(\mathbf x;\mathbf w,b)=b+\sum\limits_{i=1}^{d}w_{i}x_{i}+\sum\limits_{i=1}^{d}\sum\limits_{j=1}^{i}w_{ij}x_{i}x_{j}$$
Abbiamo $\frac{d(d+1)}{2}$ parametri addizionali rispetto ai $d+1$ originali: le regioni di decisione possono quindi complicarsi
### Quadrati Minimi e Classificazione

Assumiamo la classificazione con $\mathbf K$ classi

Le classi vengono rappresentate secondo lo schema $1$-of-$\mathbf K$: abbiamo un insieme di variabili $z_{1},\dots,z_{k}$, la classe $C_i$ viene codificata dai valori $z_{i}=1,z_{k}=0,\forall k\neq i$

Abbiamo inoltre $\mathbf K$ funzioni discriminanti $h_i$, che sono derivate come funzioni di regressione lineare con le variabili $z_{i}$ come target

Ad ogni variabile $z_{i}$ viene associata una funzione discriminante $h_{i}(\mathbf x)=\mathbf w_{i}^{T}\mathbf x+b$: l'elemento $\mathbf x$ viene assegnato alla classe $C_{k}$ tale per cui $$k=arg\max_{i}h_i(\mathbf x)$$
A questo punto $z_{k}(\mathbf x)=1,z_{j}(\mathbf x)(j\neq k)$ se $k=arg\max_{i}h_i(\mathbf x)$

In generale, una funzione di regressione fornisce una stima del valore target dato in input $\mathbb E[t|\mathbf x]$

La funzione $h_{i}(\mathbf x)$ può essere vista come stima della media condizionata $\mathbb E[z_{i}|\mathbf x]$, di una variabile binomiale $z_i$ dato $\mathbf x$

Se assumiamo che $z_{i}$ sia distribuito in accordo ad una Bernoulliana, allora il valor medio corrisponde alla probabilità a posteriori
$$\begin{align*}
h_{i}(\mathbf x)&\simeq\mathbb E[z_i|\mathbf x]\\
&=Pr(z_{i}=1|\mathbf x)\cdot 1+Pr(z_{i}=0|\mathbf x)\cdot 0\\
&=Pr(z_i=1|\mathbf x)\\
&= Pr(C_i|\mathbf x)
\end{align*}$$
Comunque, $h_i(\mathbf x)$ non è essa stessa una probabilità (non assumeremo infatti che assuma valore solamente nell'intervallo $[0,1]$)
#### Funzioni di apprendimento $h_{i}$

Dato un training set $\mathbf X,\mathbf t$, una funzione di regressione può essere derivata usando i quadrati minimi

Un elemento del training set è una coppia $(\mathbf x_{i},\mathbf t_{i}),\mathbf x_{i}\in\mathbb R^{d},\mathbf t_{i}\in\{0,1\}^{K}$
Le predizioni corrispondenti $\mathbf h_i(\mathbf x_i)=(h_{1}(\mathbf x_{i}),\dots,h_{K}(\mathbf x_{i}))^{T}$ vengono calcolate come:
$$\mathbf y_i=\mathbf h(\mathbf x_{i})=\mathbf W\mathbf x_{i}+\mathbf b=\begin{pmatrix}w_{11}&w_{12}&\dots&w_{1d}\\w_{21}&w_{22}&\dots&w_{2d}\\\vdots\\w_{K1}&w_{K2}&\dots&w_{Kd}\end{pmatrix}\begin{pmatrix}x_{i1}\\x_{i2}\\\vdots\\x_{id}\end{pmatrix}+\begin{pmatrix}b_{1}\\b_{2}\\\vdots\\b_{K}\end{pmatrix}$$

## Percettrone

