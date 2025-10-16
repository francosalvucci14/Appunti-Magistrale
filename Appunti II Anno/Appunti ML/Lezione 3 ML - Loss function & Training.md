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
# Loss Function

In generale, la funzione di loss $L:\mathcal Y\times\mathcal Y\to\mathbb R$ misura il **costo** di riferirsi a $y$ invece che al target $t$ per ogni azione successiva, dove $y$ e $t$ sono elementi dello spazio target.

Nel supervised learning, questo offre una misura della qualità della predizione ritornata dalla funzione di predizione $h$:
$$\mathcal R(\overline{x},y)=L(h(\overline{x}),y)$$
È una componente fondamentale del rischio empirico, che è il valore medio della funzione loss applicata a tutte le coppie valore-target presenti nel training set $\mathcal T$
$$\overline{\mathcal R}_{\mathcal T}(h)=\frac{1}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}L(h(x),t)$$
Questo offre una misura della qualità della predizione fatta da $h$, almeno per quanto riguarda i dati disponibili (ovvero il training set)

Durante la fase di training, il rischio empirico viene minimizzato rispetto alla funzione di predizione $h$, in particolare per quanto riguarda l'insieme di parametri $\theta$ che definiscono la funzione parametrica $h = h_{\theta}$

Ciò corrisponde alla minimizzazione della **loss complessiva**, indicata con $\mathcal L$:
$$\mathcal L(\theta,\mathcal T)=\sum\limits_{i=1}^{n}L_{i}(\theta)$$
che è la somma delle funzioni di loss $L_{i}=L(\theta,x_{i},t_{i})$ per ogni data point $(x_{i},t_{i})$
## Approcci alla minimizzazione della funzione loss

Come possiamo affrontare il problema della minimizzazione della funzione di loss? 
Idealmente, il nostro obiettivo è trovare un **minimo globale** della funzione di loss, che rappresenterebbe il miglior insieme possibile di parametri per il modello.

Un approccio comune si basa sul calcolo, in particolare sull'impostazione a zero di tutte le derivate della funzione di loss rispetto ai parametri:
$$\nabla\mathcal L(\theta,\mathcal T)=0$$
dove $\nabla$ è l'operatore del ***gradiente*** che, data una funzione multivariata $f(x_{1},\dots,x_{m})$ ritorna il vettore delle derivate parziali $$\nabla f=\begin{bmatrix}\frac{\partial f}{\partial x_{1}}\\\vdots\\\frac{\partial f}{\partial x_{m}}\end{bmatrix}$$
