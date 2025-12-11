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
# Decision Tree

Un **albero di decisione** è un classificatore espresso come partizione ricorsiva dello spazio istanziato.

La sua struttura è la seguente:
- Consiste in nodi che formano un'albero radicato
- Ogni nodo interno divide lo spazio instanziato in due o più sottospazi, seguendo una data funzione discreta dei valori degli attributi
- Di solito, ogni nodo è associato ad una partizione rispetto a un singolo attributo
- Ogni foglia è associata ad un sottospazio e:
	- a una classe, che rappresenta la previsione più appropriata per tutti i punti nel sottospazio
	- oppure a un vettore di probabilità delle classi

**esempio**

![center|500](img/Pasted%20image%2020251210173914.png)

## Decision Tree: Classification
## Decision Tree: Construction
## Decision Tree: Partitioning at each node

## Impurity measure
## Goodness of split
### Entropy and infomation gain
### Gini index
### Other goodness of split measures
## Decision Tree: Leaves
### Pruning