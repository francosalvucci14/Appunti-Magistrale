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
# Introduzione

Qui studieremo in che modo, e con quali esiti, possiamo sintetizzare le informazioni in possesso dei singoli individui in una rete al fine di derivare una singola informazione comulativa, che permetterà di prendere una decisione fra una serie di alternative, fra le quali scegliere la "migliore"

Iniziamo studiando cosa accade quando un insieme di individui deve prendere una decisione di gruppo:
- dando ad ogni individuo un segnale privato
- e prendendo decisioni individuali
# Un nuovo modello di decision making

Definiamo un modello di decision making individuale

1) Ogni individuo deve prencedere una decisione fra due alternative: $X,Y$
	- una delle due è "giusta", l'altra "sbagliata", e si esprime con il simbolo "$\gt$: ad es., scriviamo $X\gt Y$ se $X$ è la scelta giusta
	- le due alternative sono, a priori, equiprobabili: $Pr(X\gt Y)=Pr(Y\gt X)= \frac{1}{2}$
2) Ogni individuo riceve un segnale privato: $x,y$
	- $Pr(x|X\gt Y)=Pr(y|Y\gt X)=q\gt \frac{1}{2}$
3) Ogni individuo sceglie in accordo al proprio segnale privato
4) CIascun individuo opera la propria scelta fra $X$ e $Y$, la scrive su una scheda che poi introduce in un'urna
5) Infine, viene presa una decisione collettiva fra $X$ e $Y$ sulla base delle scelte dei singoli individui

