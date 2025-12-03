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
![center|500](img/Pasted%20image%2020251021164418.png)

**Caso 2**
![center|500](img/Pasted%20image%2020251021164451.png)

A tal fine,

1. possiamo considerare una classe di possibili distribuzioni condizionate $\mathcal P$ e
2. selezionare (dedurre) la distribuzione condizionata "migliore" $p^{\star}\in\mathcal P$ dalle conoscenze disponibili (ovvero il dataset), in base a una qualche misura $q$
3. dato un nuovo elemento $\overline{x}$, applicare $p^{\star}(t|\overline{x})$ per assegnare probabilità a ciascun valore possibile del target corrispondente

![center|500](img/Pasted%20image%2020251021164759.png)

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

Punto di vista **frequentista**: i parametri sono variabili deterministiche, il cui valore è sconosciuto e deve essere stimato.

Quello che dobbiamo fare è determinare il valore del parametro che massimizza la verosimiglianza, in questo modo:
$$\theta^{\star}=\underset{\theta}{\arg\max}\space L(\theta|\mathcal T)=\underset{\theta}{\arg\max}\space p(X|\theta)=\underset{\theta}{\arg\max}\prod_{i=1}^{n}p(x_{i}|\theta)$$
oppure 
$$\theta^{\star}=\underset{\theta}{\arg\max}\space L(\theta|\mathcal T)=\underset{\theta}{\arg\max}\space p(X,t|\theta)=\underset{\theta}{\arg\max}\space p(\overline{x})\prod_{i=1}^{n}p(t_{i}|x_{i},\theta)=\underset{\theta}{\arg\max}\prod_{i=1}^{n}p(t_{i}|x_{i},\theta)$$
La log-verosomiglianza (log-likelihood) $$l(\theta|\mathcal T)=\ln L(\theta|\mathcal T)$$è preferibile, dato che i prodotti vengono trasformati in somme, mentre $\theta^{\star}$ rimane la stessa (dato che la funzione $\ln$ è monotona)
Otteniamo quindi $$\underset{\theta}{\arg\max}\space l(\theta|\mathcal T)=\underset{\theta}{\arg\max}\space L(\theta|\mathcal T)$$
Il problema di ottimizzazione risultante è quindi $$\theta_{ML}^{\star}=\underset{\theta}{\arg\max}\space p(X|\theta)=\underset{\theta}{\arg\max}\sum\limits_{i=1}^{n}\ln p(x_i|\theta)$$
oppure 
$$\theta_{ML}^{\star}=\underset{\theta}{\arg\max}\space p(X,t|\theta)=\underset{\theta}{\arg\max}\sum\limits_{i=1}^{n}\ln p(t_i|x_i,\theta)$$
La soluzione viene calcolata risolvendo il set di equazioni $$\frac{\partial l(\theta|\mathcal T)}{\partial\theta_{i}}=0,\forall i=1,\dots,d$$
Più precisamente, impostando il gradiente a $0$
$$\nabla l(\theta|\mathcal T)=0$$

Si noti che la condizione di gradiente nullo è ***solo una condizione necessaria*** per la massimizzazione della funzione ML considerata, poiché in questo caso possiamo solo dire che il punto corrispondente è un punto stazionario (cioè un massimo, un minimo o un punto di sella). Anche nel caso in cui il punto sia un massimo (che potrebbe essere verificato stimando la derivata seconda o, in generale, l'Hessiano), potremmo concludere che si tratta di un massimo **locale**, mentre noi siamo interessati al massimo globale.

Questi problemi vengono tipicamente affrontati considerando casi in cui, ad esempio, esiste solo un punto stazionario e tale punto è un massimo (quindi quello globale), oppure applicando strategie di ricerca del massimo più complesse.

Una volta calcolato il valore ottimale $\theta^{\star}_{ML}$, è possibile effettuare previsioni stimando, per ogni nuova osservazione $\overline{x}$, la sua probabilità:

$$p(\overline{x}|X)=\int_{\theta}p(x|\theta)p(\theta|X)d\theta\approx\int_{\theta}p(\overline{x}|\theta^{\star}_{ML})p(\theta|X)d\theta=p(\overline{x}|\theta^{\star}_{ML})\int_{\theta}p(\theta|X)d\theta=p(\overline{x}|\theta^{\star}_{ML})$$
e la distribuzione condizionata $t|\overline{x}$ del valore target associato

$$\begin{align*}
p(\hat{t}|\overline{x},X,t)&=\int_{\theta}p(\hat{t}|x,\theta)p(\theta|X,t)d\theta\\
&\approx\int_{\theta}p(\hat{t}|\overline{x},\theta^{\star}_{ML})p(\theta|X)d\theta=p(\overline{x}|\theta^{\star}_{ML})\int_{\theta}p(\theta|X,t)d\theta=p(\hat{t}|\overline{x},\theta^{\star}_{ML})
\end{align*}$$
Vediamo alcuni esempi

**Esempio 1**

Prendiamo una collezione $X$ di $n$ eventi binari, modellati tramite una distribuzione Bernoulliana con parametro sconosciuto $\phi$ 
$$p(x|\phi)=\phi^{x}(1-\phi)^{1-x}$$
Allora vale che:
- likelihood: $L(\phi|X)=\prod_{i=1}^{n}\phi^{x_{i}}(1-\phi)^{1-x_{i}}$
- log-likelihood: $l(\phi|X)=\sum\limits_{i=1}^{n}(x_{i}\ln(\phi)+(1-x_{i})\ln(1-\phi))=n_{1}\ln(\phi)+n_{0}\ln(1-\phi)$ dove $n_{0}(n_{1})$ è il numero di eventi $x\in X$ uguali a $0(1)$
- massimizziamo la likelihood, risolvendo il sistema delle equazioni "derivate parziali=0", ottenendo $$\frac{\partial l(\phi|X)}{\partial\phi}=\frac{n_{1}}{\phi}-\frac{n_{0}}{1-\phi}=0\implies\phi^{\star}_{ML}=\frac{n_1}{n_0+n_{1}}=\frac{n_1}{n}$$
Altro esempio, regressione lineare (vedi slides)

Massimizzare la verosimiglianza del dataset osservati tende a produrre una stima troppo sensibile ai valori del dataset, causando quindi un **overfitting**. 

Le stime ottenute sono adatte a modellare i dati osservati, ma potrebbero essere troppo specializzate per essere utilizzate per modellare set di dati diversi.

È possibile introdurre una funzione aggiuntiva $P (\theta)$ con l'obiettivo di limitare l'overfitting e la complessità complessiva del modello. 

Ciò porta alla seguente funzione da massimizzare
$$C(\theta|X)=l(\theta|X)-P(\theta)$$
come caso comune, vale che $P(\theta)=\frac{\gamma}{2}||\theta||^{2}$, dove $\gamma$ è chiamato parametro di **tuning**

## Maximum a posteriori estimate

L'inferenza tramite il massimo a posteriori (MAP) è simile al ML, ma $\theta$ è ora considerato come una variabile casuale (seguendo un approccio bayesiano), la cui distribuzione deve essere derivata dalle osservazioni, tenendo conto anche delle conoscenze precedenti (distribuzione a priori). 

Il valore del parametro che massimizza la funzione $$p(\theta|\mathcal T)=\frac{p(\mathcal T|\theta)p(\theta)}{p(\mathcal T)}$$viene quindi calcolato come:
$$\begin{align*}
\theta^{\star}_{MAP}=\underset{\theta}{\arg\max}\space p(\theta|\mathcal T)&=\underset{\theta}{\arg\max}\space p(\mathcal T|\theta)p(\theta)\\
&=\underset{\theta}{\arg\max}\space L(\theta|\mathcal T)p(\theta)\\
&=\underset{\theta}{\arg\max}\space (l(\theta|\mathcal T)+\ln p(\theta))
\end{align*}$$
che risulta in $$\theta^{\star}_{MAP}=\underset{\theta}{\arg\max}\left(\sum\limits_{i=1}^{n}\ln p(x_{i}|\theta)+\ln p(\theta)\right)$$
oppure 
$$\theta^{\star}_{MAP}=\underset{\theta}{\arg\max}\left(\sum\limits_{i=1}^{n}\ln p(t_i|x_{i},\theta)+\ln p(\theta)\right)$$

[^1]: https://it.wikipedia.org/wiki/Funzione_sigmoidea ; funzione che trasforma $z$ in un valore compreso fra $0$ e $1$

## MAP e Prior Gaussiano

Assumiamo che $\overline{\theta}$ sia distribuito intorno all'origine come una v.a Gaussiana Multivariata con varianza uniforme e covarianza nulla, ovvero:
$$Pr(\overline{\theta})\sim\mathcal N(\overline{\theta}|\overline{0},\sigma^{2})=\frac{1}{(2\pi)^{\frac{d}{2}}\sigma^{d}}e^{-\frac{||\overline{\theta}||^{2}}{2\sigma^{2}}}\propto e^{-\frac{||\overline{\theta}||^{2}}{2\sigma^{2}}}$$
Partendo dalle ipotesi, otteniamo che: 
$$\begin{align*}
\overline{\theta}^{\star}_{MAP}&=arg\max_{\overline{\theta}}Pr(\overline{\theta}|\mathcal T)arg\max_{\overline{\theta}}(l(\overline{\theta}|\mathcal T)+\ln Pr(\overline{\theta}))\\&arg\max_{\overline{\theta}}\left(l(\overline{\theta}|\mathcal T)+\ln e^{-\frac{||\overline{\theta}||^{2}}{2\sigma^{2}}}\right)=arg\max_{\overline{\theta}}\left(l(\overline{\theta}|\mathcal T)-\frac{||\overline{\theta}||^{2}}{2\sigma^{2}}\right)
\end{align*}$$
