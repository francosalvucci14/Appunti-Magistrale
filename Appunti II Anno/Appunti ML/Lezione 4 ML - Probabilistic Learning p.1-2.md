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
# Approssimare $p_{C}(\overline{x},t)$

Ci poniamo nel caso in cui la distribuzione di probabilità $p_{C}(t|\overline{x})$ sia sconosciuta (nel caso in cui sia conosciuta, ci sono tecniche spiegate sempre in questo pacco di note, che ancora non abbiamo affrontato)

Siccome $p_{C}(t|\overline{x})$ non è conosciuta, dobbiamo dedurre per $\mathcal T$ una distribuzione di probabilità $p(t|\overline{x})$ che bene approssima $p_{C}$

Ci sono due approcci che possono essere applicati:
1. **Modelli generativi probabilistici**: Inferenza delle probabilità condizionate $p(\overline{x}|C_k)$ per tutte le classi. Inferenza delle **probabilità a priori** $p(C_k)$. Uso della regola di Bayes $$p(C_{k}|\overline{x})=\frac{p(\overline{x}|C_{k})p(C_k)}{p(\overline{x})}\approx p(\overline{x}|C_{k})p(C_k)$$per derivare (a meno di una costante moltiplicativa) la **probabilità a posteriori** $p(C_{k}|\overline{x})$
2. **Modelli discriminativi probabilistici**: Inferenza delle probabilità di classe $p(C_{k}|\overline{x})$ direttamente da $\mathcal T$

**Caso 1**
![[Pasted image 20251021164418.png|center|500]]

**Caso 2**
![[Pasted image 20251021164451.png|center|500]]

A tal fine,

1. possiamo considerare una classe di possibili distribuzioni condizionate $\mathcal P$ e
2. selezionare (dedurre) la distribuzione condizionata "migliore" $p^{\star}\in\mathcal P$ dalle conoscenze disponibili (ovvero il dataset), in base a una qualche misura $q$
3. dato un nuovo elemento $\overline{x}$, applicare $p^{\star}(t|\overline{x})$ per assegnare probabilità a ciascun valore possibile del target corrispondente

![[Pasted image 20251021164759.png|center|500]]

Come definire la classe delle possibili distribuzioni condizionate $p(t|\overline{x})$?

Risposta: solitamente, si usa un'approccio parametrico: distribuzioni definite da una struttura comune (arbitraria) e da un insieme di parametri

**Esempio**: regressione logistica per classificazioni binarie

La probabilità $p(t|\overline{x})$, con $t\in\{0,1\}$, è assunta essere una distribuzione **Bernoulliana**
$$p(t|\overline{x})=\pi(\overline{x})^{t}(1-\pi(\overline{x}))^{1-t}$$con 
$$\pi(\overline{x})=p(t=1|\overline{x})=\frac{1}{1+e^{-\sum\limits_{i=1}^{d}w_{i}x_{i}+w_0}}$$
>[!help]- Info
>La funzione $\frac{1}{1+e^{-z}}$, con $z=\theta_{0}+\theta_{1}x_{1}+\theta_{2}x_{2}+\dots+\theta_{m}x_{d}$ è detta **funzione sigmoide** (o sigmoidea) [^1]
>In questo caso, $z$ è stato preso come combinazione lineare delle feature $x_{1},\dots,x_{d}$ e dei parametri $\theta_{0},\dots,\theta_{m}$
## Dedurre la distribuzione migliore - Approccio $1$

Qual è una misura $q(p,\mathcal T)$ della qualità della distribuzione (dato il dataset $T=(X,t)$)?

- Questa misura è collegata al modo in cui un dataset generato campionando casualmente da $D_1$​ (solitamente una distribuzione uniforme) e da $p(t|\overline{x})$ (al posto della distribuzione ignota $D_2$​) può risultare simile al dataset osservato $\mathcal T$.
- In particolare, ci chiediamo: qual è la probabilità che il dataset $T=(X,t)$ sia stato ottenuto sotto le seguenti ipotesi?  
	- Le $n=|t|$ coppie $(x_i, t_i)$ sono campionate in modo indipendente tra loro.  
	- Ogni $x_i$ è campionato da $D_1$​ (che assumiamo essere uniforme).  
	- Ogni $t_i$ è campionato da $p(t|x_i)$.
- Possiamo quindi usare tale probabilità come misura di qualità $q(p,T)$, e cercare la distribuzione $p^{\star}(t|\overline{x})$ che massimizza $p(X,t)$, assumendo che $D_1$ sia la distribuzione uniforme e che $D_2 = p^\star(t|\overline{x})$.

Cioè, consideriamo la probabilità
$$p(X,t)=\prod_{i=1}^{n}p(\overline{x}_{i},t_{i})=\prod_{i=1}^{n}p(t_{i}|\overline{x}_{i})p(\overline{x}_{i})\propto\prod_{i=1}^{n}p(t_{i}|\overline{x}_{i})=q(p,\mathcal T)$$
e cerchiamo (all'interno di una certa classe di distribuzioni) la probabilità condizionata $p^{\star}(t|\overline{x})$ che rende $p(X, t)$ massimo

Si osservi che l'apprendimento della distribuzione $p^\star(t|\overline{x})$ che massimizza $q(p, \mathcal T )$ corrisponde, nel caso del predittore probabilistico, all'apprendimento della funzione $h^\star$ che minimizza il rischio empirico $\overline{R}_{\mathcal T} (h)$ nel caso del predittore funzionale.

In entrambi i casi, l'apprendimento viene eseguito tramite ottimizzazione.

Le stesse considerazioni fatte riguardo al bias induttivo nel caso di un predittore funzionale, e relative all'overfitting e all'underfitting, possono essere riformulate qui riguardo alla classe delle possibili distribuzioni condizionate.
## Approccio $2$

Invece che trovare la migliore distribuzione $p^{\star}\in\mathcal P$, e usarla per predirre le probabilità del target $p^{\star}(t|\overline{x})$, per ogni elemento $\overline{x}$, potremmo:
1. considerare ogni possibile distribuzione condizionale $p\in\mathcal P$ e la sua misura di qualità $q(p,\mathcal T)$
2. comporre tutte le distribuzioni condizionali $p(y|\overline{x})$, ognuna pesata secondo la sua misura $q(p,\mathcal T)$ (comporre ad esempio mediante la media ponderata)
3. applicare la distribuzione risultante

Assumiamo che $q$ prenda la forma di una distribuzione di probabilità (*di una distribuzione di probabilità*)
1. Il primo approccio: prende il valore modale (la distribuzione della qualità massima) e lo usa per performare predizioni
2. Il secondo approccio: calcola il valor medio delle distribuzioni, in rispetto alla distribuzione di probabilità $q$
### Inferenza della distribuzione predittiva

Supponiamo che gli elementi nel dataset $\mathcal T$ corrispondano a un insieme di $n$ campioni, estratti in modo indipendente dalla stessa distribuzione di probabilità (ovvero, sono **indipendenti e identicamente distribuiti**, i.i.d): possono essere visti come $n$ realizzazioni di una singola variabile casuale.

Siamo interessati ad apprendere, a partire da $\mathcal T$ , una **distribuzione predittiva** $p(\overline{x}|X)$ (o $p(\overline{x}, t|X, t)$) per qualsiasi nuovo elemento (o coppia elemento-target). 

Possiamo interpretare questo come la probabilità che, in un campionamento casuale, l'elemento effettivamente restituito sia effettivamente $\overline{x}$ (o $(\overline{x}, t)$).

- (**Unsupervised**) nel caso in cui $\mathcal T = X = \{x_1, \dots , x_n\}$, siamo interessati a derivare la distribuzione di probabilità $p(\overline{x}|X)$ di un nuovo elemento, data la conoscenza dell'insieme $X$
- (**Supervised**) nel caso in cui $\mathcal T = (X, t) = \{(x_1, t_1),\dots , (x_n, t_n)\}$, siamo interessati a ricavare la distribuzione di probabilità congiunta $p(\overline{x}, t|X, t)$ o, supponendo che $p(\overline{x}|X, t)$ sia uniforme e quindi anche indipendente da $(X, t)$, la distribuzione condizionata $p( t|\overline{x},X, t)$, data la conoscenza dell'insieme di coppie $(X, t)$
# Modelli Probabilistici

Definiamo il concetto di modello probabilistico

>[!definition]- Modello Probabilistico
>Un **modello probabilistico** è una collezzione di distribuzioni di probabilità con la stessa struttura, definite su un dominio dei dati.
>Le distribuzioni di probabilità sono istanze del modello probabilistico e sono caratterizzate dai valori assunti da un insieme di parametri

Un modello probabilistico può essere di due tipi:
- **parametrico**: se l'insieme dei parametri viene dato,è finito e indipendente dai dati
- **non parametrico**: se l'insieme dei parametri non viene dato in anticipo, ma viene derivato dai dati

Dato un dataset $\mathcal T$ e una distribuzione di probabilità $p$ con parametri $\theta$, definiti sullo stesso dominio dei dati, abbiamo che:
- la **verosomiglianza** (***likelihood***) di $\theta$ in rispetto a $\mathcal T$ è definita come $$L(\theta|\mathcal T)=p(\mathcal T|\theta)$$la probabilità del dataset sotto la distribuzione $p$ con parametri $\theta$, cioè la probabilità che il dataset venga generato campionando, indipendentemente, punti ottenuti da $p(\overline{x},t;\theta)$
- mentre la probabilità $p(\mathcal T|\theta)$ è considerata una funzione di $p(\mathcal T|\theta)$ con $\theta$ fissato, la verosomiglianza $L(\theta|\mathcal T)$ è una funzione di $\theta$ con $\mathcal T$ fissato
- i paramentri $\theta$ sono considerati essere (indipendenti) variabili (e questo è il così detto **approccio frequentista** della probabilità)
- assumendo che tutti gli elementi in $\mathcal T$ siano i.i.d, otteniamo che $$\begin{align*}L(\theta|\mathcal T)&=p(X|\theta)=\prod_{i=1}^{n}p(x_{i}|\theta)\quad\text{primo caso,vedi sopra T=X}\\ L(\theta|\mathcal T)&=p(X,t|\theta)=\prod_{i=1}^np(x_{i},t_i|\theta)=\prod_{i=1}^np(t_{i}|x_i\theta)p(x_{i}|\theta)=p(\overline{x}|\theta)\prod_{i=1}^np(t_{i}|x_i\theta)\\&=p(\overline{x})\prod_{i=1}^np(t_{i}|x_i\theta)\propto\prod_{i=1}^np(t_{i}|x_i\theta)\quad\text{secondo caso T=(X,t),assumendo }p(\overline{x}|\theta)\text{ unif.}\end{align*}$$
## Maximum likelihood estimate


## Maximum a posteriori estimate



[^1]: https://it.wikipedia.org/wiki/Funzione_sigmoidea ; funzione che trasforma $z$ in un valore compreso fra $0$ e $1$

