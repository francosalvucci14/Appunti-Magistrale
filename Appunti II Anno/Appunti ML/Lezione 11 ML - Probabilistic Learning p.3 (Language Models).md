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
# Language Models

Un **modello linguistico** è una distribuzione di probabilità (categoriale) su un vocabolario di termini (possibilmente tutte le parole che compiono in una vasta raccolta di documenti).

Un modello linguistico può essere applicato per prevedere il termine successivo che compairà in un testo. 

La probabilità di comparsa di un termine è correlata al suo contenuto informativo ed è alla base di numerose tecniche di recupero delle informazioni.

Si presume che la probabilità di occorrenza di un termine sia indipendente dai termini precedenti in un testo (modello **bag of words**).

Dato un modello linguistico, è possibile campionare dalla distribuzione per generare documenti casuali statisticamente equivalenti ai documenti della raccolta utilizzata per derivare il modello.

Sia $D = \{t_1,\dots , t_n\}$ il dizionario, ovvero l'insieme dei termini presenti in una data raccolta $C$ di documenti, dopo la **rimozione delle parole vuote** (termini comuni e non informativi) e lo **stemming** (riduzione delle parole alla loro forma base).

Per ogni $i = 1,\dots , n$ sia $m_i$ la ***molteplicità*** (numero di occorrenze) del termine $t_i$ in $C$

Un modello linguistico può essere derivato come una distribuzione categoriale associata a un vettore $\hat{\pmb{\phi}} = (\hat\phi_{1},\dots , \hat\phi_n)^{T}$ di probabilità: ovvero,
$$0\leq \hat\phi_{i}\leq1,i=1,\dots,n\quad\sum\limits_{i=1}^{n}\hat\phi_{i}=1$$
dove $\hat\phi_{j}=p(t_{j}|C)$
## Learning a language model by ML

Applicando la massima verosimiglianza per ricavare le probabilità dei termini nel modello linguistico si ottiene l'impostazione
$$\hat\phi_{j}=p(t_{j}|C)=\frac{m_{j}}{\sum\limits_{k=1}^{n}m_{k}}=\frac{m_{j}}{N}$$
dove $N=\sum\limits_{k=1}^{n}m_{k}$ è il numero complessivo di occorrenze in C dopo la rimozione delle parole vuote

Secondo questa stima, un termine $t$ che non si è mai verificato in $C$ ha una probabilità pari a zero di essere osservato (*paradosso del cigno nero*), a causa dell'eccessivo adattamento del modello ai dati osservati, tipico della stima ML.

Soluzione: assegnare una probabilità piccola, diversa da zero, agli eventi (termini) non osservati fino ad ora. Questo si chiama **livellamento** (smoothing).
## Bayesian learning of a language model

Possiamo applicare il modello multinomiale di Dirichlet.
- Questo implica definire un prior Dirichlet chiamato $Dir(\hat{\pmb{\phi}}|\pmb\alpha)$, con $\pmb\alpha=(\alpha_{1},\alpha_{2},\dots,\alpha_{n})$, definito come $$p(\phi_{1},\dots,\phi_{n}|\pmb\alpha)=\frac{1}{\Delta(\alpha_{1},\alpha_{2},\dots,\alpha_{n})}\prod_{i=1}^{n}\phi_{i}^{\alpha_i-1}$$
- la distribuzione posteriore di $\phi$ dopo che $C$ è stato osservato è quindi $Dir(\mathbf\phi|\overline\alpha)$, dove $$\pmb{\overline{\alpha}}=(\alpha_{1}+m_{1},\alpha_{2}+m_{2},\dots,\alpha_{n}+m_{n})$$cioè $$p(\phi_{1},\dots,\phi_{n}|\pmb{\overline{\alpha}})=\frac{1}{\Delta(\alpha_{1}+m_{1},\dots,\alpha_{n}+m_{n})}\prod_{i=1}^{n}\phi_{i}^{\alpha_i+m_i-1}$$

Il modello di linguaggio $\overline{\hat\phi}$ corrisponde alla distribuzione a posteriori predittiva
$$\hat{\phi_{j}}=p(t_{j}|C,\pmb\alpha)=\int p(t_{j}|\hat{\pmb{\phi}})p(\hat{\pmb{\phi}}|C,\alpha)d\hat{\pmb{\phi}}=\int\phi_{j}Dir(\hat{\pmb{\phi}}|\overline{\alpha})d\hat{\pmb{\phi}}=\mathbb E_{\hat{\pmb{\phi}}\sim Dir(\cdot|\overline{\alpha})}[\phi_{j}]$$
ovvero l'aspettativa di $\phi_j$ rispetto alla distribuzione $Dir(\hat{\pmb{\phi}}|\overline{\alpha})$. 
Quindi
$$\hat\phi_j=\frac{\overline{\pmb\alpha}_{j}}{\sum\limits_{k=1}^{n}\overline{\pmb\alpha}_{k}}=\frac{\alpha_{j}+m_{j}}{\sum\limits_{k=1}^{n}(\alpha_{k}+m_{k})}=\frac{\alpha_{j}+m_{j}}{\alpha_{0}+N}$$

Il termine $\alpha_j$ rende impossibile ottenere probabilità pari a zero (**livellamento di Dirichlet**).

Il prior non informativo in questo caso è $\alpha_i = \alpha$ per tutti gli $i$, il che porta a
$$p(t_{j}|C,\pmb\alpha)=\frac{m_{j}+\alpha}{\alpha|D|+N}$$
dove $|D|$ è la dimensione del vocabolario
## Naive bayes classifiers

Un modello linguistico generativo può essere applicato per ricavare classificatori di documenti in due o più classi, come descritto sopra:
- date due classi $C_1, C_2$, supponiamo che, per qualsiasi documento $d$, le probabilità $p(C_1|d)$ e $p(C_2|d)$ siano note: allora, $d$ può essere assegnato (ad esempio) alla classe con probabilità più alta
- come derivare $p(C_k|d)$ per qualsiasi documento, data una raccolta $\pmb C_1$ di documenti noti per appartenere a $C_1$ e una raccolta simile $\pmb C_2$ per $C_2$? Applichiamo la regola di Bayes: $$p(C_{k}|d)\propto p(d|C_{k})p(C_{k})$$l'evidenza $p(d)$ è la stessa per ambo le classi, e quindi può essere ignorata
- Abbiamo ancora il problema del calcolare $p(C_{k})$ e $p(d|C_{k})$ dalla collezione $\pmb C_{1}$ e $\pmb C_{2}$

Le probabilità a priori $p(C_k) (k = 1, 2)$ possono essere facilmente stimate da $\pmb C_1, \pmb C_2$: ad esempio, applicando ML, otteniamo che
$$p(C_{k})=\frac{|C_{1}|}{|C_{1}|+|C_{2}|}$$

Per quanto riguarda le probabilità $p(d|C_k) (k = 1, 2)$, osserviamo che $d$ può essere visto, secondo l'ipotesi del bag of words, come un multiset di $n_d$ termini
$$d=\{\overline{t}_{1},\overline{t}_{2},\dots,\overline{t}_{n_{d}}\}$$
Applicando la regola del prodotto, otteniamo che:
$$p(d|C_{k})=p(\overline{t}_{1},\overline{t}_{2},\dots,\overline{t}_{n_{d}}|C_{k})=p(\overline{t}_1|C_{k})p(\overline{t}_{2}|\overline{t}_{1},C_{k})\dots p(\overline{t}_{n_{d}}|\overline{t}_{1},\dots,\overline{t}_{n_{d}-1},C_{k})$$

## Naive Bayes assumption

Il calcolo di $p(d|C_k)$ è molto più semplice se assumiamo che i termini siano a due a due condizionalmente indipendenti, data la classe $C_k$, ovvero, per $i, j = 1 \dots, n_d$ e $k = 1, 2$:

$$p(\bar{t}_i, \bar{t}_j|C_k) = p(\bar{t}_i|C_k)p(\bar{t}_2|C_k)$$

Di conseguenza:

$$p(d|C_k) = \prod_{j=1}^{n_d} p(\bar{t}_j|C_k)$$

Le probabilità $p(\bar{t}_j|C_k)$ sono disponibili per tutti i termini se i modelli linguistici sono stati derivati per $C_1$ e $C_2$, rispettivamente dai documenti in $\mathcal{C}_1$ e $\mathcal{C}_2$.

Applicando queste considerazioni, otteniamo un **classificatore Naive Bayes** che opera come segue per classificare un documento $d$:

1. Siano $\bar{t}_1, \dots, \bar{t}_m$ la rappresentazione _bag of words_ di $d$, dove $m = |\mathcal{D}|$.
2. Per ogni $i = 1, \dots, m$ e $k = 0, 1$, calcolare $p(\bar{t}_i|C_k)$.
3. Per $k = 0, 1$, calcolare $p(d|C_k)$ applicando l'assunzione di Naive Bayes.
4. Assegnare $d$ alla classe $\mathcal{C}_r$ dove $r = \underset{k \in \{0,1\}}{\text{argmax }} p(d|C_k)p(C_k)$.

Si noti che lo stesso approccio può essere applicato alla classificazione di elementi $\mathbf{x} = (x_0, \dots, x_d)$. In questo caso, l'assunzione di Naive Bayes è che le caratteristiche (_features_) siano condizionalmente indipendenti data la classe, quindi:

$$p(\mathbf{x}|C_k) = \prod_{i=0}^{d} p(x_i|C_k)$$
