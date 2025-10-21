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
>La funzione $\frac{1}{1+e^{-z}}$, con $z=\theta_{0}+\theta_{1}x_{1}+\theta_{2}x_{2}+\dots+\theta_{m}x_{d}$ è detta **funzione sigmoide** (o sigmoidea) [^1] [^2]
>In questo caso, $z$ è stato preso come combinazione lineare delle feature $x_{1},\dots,x_{d}$ e dei parametri $\theta_{0},\dots,\theta_{m}$
## Dedurre la distribuzione migliore

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



[^1]: https://it.wikipedia.org/wiki/Funzione_sigmoidea

[^2]: funzione che trasforma $z$ in un valore compreso fra $0$ e $1$
