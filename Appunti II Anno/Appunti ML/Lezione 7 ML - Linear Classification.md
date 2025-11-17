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
1. **funzioni discriminative**
2. **approccio discriminativo**
3. **approccio generativo**


## Funzioni Discriminanti
### Quadrati Minimi e Classificazione
#### Funzioni di apprendimento $h_{i}$
## Percettrone

