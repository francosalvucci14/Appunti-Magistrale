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
# Modelli Generativi

Le classi sono modellate da distribuzioni condizionali adeguate $p(\mathbf x|C_k)$ (modelli linguistici nel caso precedente): è possibile campionare da tali distribuzioni per generare documenti casuali statisticamente equivalenti ai documenti nella raccolta utilizzata per derivare il modello.

La regola di Bayes consente di derivare $p(C_k|\mathbf x)$ dati tali modelli (e le distribuzioni a priori $p(C_k)$ delle classi)

È possibile derivare i parametri di $p(\mathbf x|C_k)$ e $p(C_k)$ dal dataset, ad esempio attraverso la stima della massima verosimiglianza

La classificazione viene eseguita confrontando $p(C_k|\mathbf x)$ per tutte le classi
## Derivare le probabilità a posteriori

Consideriamo il caso della classificazione binaria e osserviamo che:
$$p(C_{1}|\textbf{x})=\frac{p(\textbf{x}|C_{1})p(C_{1})}{p(\textbf{x}|C_{1})p(C_{1})+p(\textbf{x}|C_{2})p(C_{2})}=\frac{1}{1+\frac{p(\textbf{x}|C_{2})p(C_{2})}{p(\textbf{x}|C_{1})p(C_{1})}}$$
Definiamo inoltre:
$$a(\textbf{x})=\log\left(\frac{p(\textbf{x}|C_{1})p(C_{1})}{p(\textbf{x}|C_{2})p(C_{2})}\right)=\log\left(\frac{p(C_{1}|\textbf{x})}{p(C_{2}|\textbf{x})}\right)$$
$a$ è quindi il logaritmo della frazione fra le probabilità a posteriori (**logs odds**)

Otteniamo quindi:
$$p(C_{1}|\textbf{x})=\frac{1}{1+e^{-a(\textbf{x})}}=\sigma(a(\textbf{x}))\quad p(C_{2}|\textbf{x})=1-P(C_{1}|\textbf{x})=\frac{1}{1+e^{a(\textbf{x})}}$$
$\sigma(x)$ è la **funzione logistica** (detta anche **sigmoide**)

![center|500](Pasted%20image%2020251202141800.png)

Di seguito alcune proprietà utili della funzione sigmoide:
1. $\sigma(-x)=1-\sigma(x)$
2. $\frac{d\sigma(x)}{dx}=\sigma(x)(1-\sigma(x))$

Nel caso della classificazione con $K\gt2$ classi, vale la seguente formula generale
$$p(C_{k}|\textbf{x})=\frac{p(\textbf{x}|C_{k})p(C_{k})}{\sum\limits_{j}p(\textbf{x}|C_{j})p(C_{j})}$$
Definiamo inoltre, per ogni $k=1,\dots,K$ la seguente funzione:
$$a_{k}(\textbf{x})=\log(p(\textbf{x}|C_{k})p(C_{k}))=\log p(\textbf{x}|C_{k})+\log p(C_{k})$$

Allora, possiamo scrivere:
$$p(C_k|\textbf{x})=\frac{e^{a_{k}}}{\sum\limits_{j}e^{a_{j}}}=s(x_{k})$$
dove $s(\textbf{x})$ è la funzione **softmax** (anche detta **esponenziale normalizzata**), e può essere vista come una estensione della sigmoide al caso $K\gt2$
## Gaussian Discriminant Analysis


### Funzioni discriminative
### Classi Multiple
### Matrici di covarianza generali - caso binario
### GDA e ML
