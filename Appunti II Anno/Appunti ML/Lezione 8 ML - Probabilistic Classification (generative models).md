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
## Gaussian Discriminant Analysis
### Funzioni discriminative
### Classi Multiple
### Matrici di covarianza generali - caso binario
### GDA e ML
