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
# Derivare un Predittore Funzionale p.2
## Ensemble Learning Approach

Il terzo approccio prevede la **creazione di un'intera serie di predittori** e l'esecuzione di previsioni componendo l'insieme delle loro previsioni, il che spesso può portare a un miglioramento delle prestazioni e della robustezza. 

Questo metodo può essere meglio specificato come segue:

1) **Costruzione dell'insieme**: Derivare dal training set $\mathcal T$ un insieme di $s$ algoritmi $\mathcal A_{\mathcal T}^{(1)},\mathcal A_{\mathcal T}^{(2)},\dots,\mathcal A_{\mathcal T}^{(s)}$, ognuno che calcola una funzione diversa $h_{\mathcal T}^{(i)}:\mathcal X\to\mathcal Y$ nella classe data $\mathcal H$. Ogni algoritmo $\mathcal A^{(i)}$ è quindi un predittore per $y$ partendo da $\overline{x}$ derivato dallo stesso insieme $\mathcal T$ di esempi.
2) **Assegnamento dei pesi**: Assegnare un insieme di pesi corrispondenti $\omega^{(1)},\omega^{(2)},\dots,\omega^{(s)}$ ad ogni predittore. Essenzialmente, ogni peso $\omega^{(i)}$ è direttamente correlato alla qualità stimata delle predizioni fornite da $\mathcal A^{(i)}$ per quanto riguarda gli elementi di $\mathcal T$
3) **Combinazione delle Predizione**: per ogni $\overline{x}$ calcoliamo il ***valore predetto finale*** combinando i valori $$y^{(1)}=h_{\mathcal T}^{(1)}(\overline{x}),\dots,y^{(s)}=h_{\mathcal T}^{(s)}(\overline{x})$$ predetti dagli algoritmi individuali, pesati secondo i rispettivi pesi $$\omega^{(1)},\dots,\omega^{(s)}$$
>[!help]- Definizione Formale
>Il valore target predetto per l'elemento $\overline{x}$ è la **combinazione lineare** dei valori $y^{(1)},y^{(2)},\dots,y^{(s)}$, predetti dai predittori $\mathcal A^{(1)},\mathcal A^{(2)},\dots,\mathcal A^{(s)}$, ognuno pesato in base al corrispettivo peso $\omega^{(1)},\dots,\omega^{(s)}$
>Ogni $\mathcal A^{(i)}$ è un semplice predittore derivato da $\mathcal T$
>

Lo schema è il seguente:

![[Pasted image 20251014102318.png|center|500]]


Una variante importante di questo approccio è chiamata **Predizione Bayesiana Completa**, dove l'insieme dei diversi predittori è un' insieme continuo, ciascuno corrispondente a un valore diverso dell'insieme dei parametri $(w_{1},w_{2},\dots,w_{d})\in\mathbb R^{d}$ .
In questo caso, chiaramente, la somma è sostituita da un'**integrale** (solitamente multidimensionale)

Un'esempio del terzo approccio è il seguente: per i task di regressione, i predittori possono essere visti come **regressori lineari**, e calcolare la predizione finale per l'elemento $\overline{x}$ come la combinazione lineare dei valori $y^{(1)},\dots,y^{(s)}$, predetti dai predittori $\mathcal A^{(1)},\dots,\mathcal A^{(s)}$, ognuno pesato usando i corrispettivi pesi $\omega^{(1)},\dots,\omega^{(s)}$.

Quindi, $h(\overline{x})$ è calcolato come segue:
$$h(\overline{x})=\sum\limits_{i=1}^{s}\omega^{(i)}h^{(i)}(\overline{x})$$
dove:
- $\sum\limits_{i=1}^{s}\omega^{(i)}=1$ 
- $\omega^{(i)}\geq0,\forall i$ 

Stesso esempio per i task di classificazione: qui possiamo usare l'approccio basato sul voto, in cui viene restituita la classe prevista dal maggior numero di predittori.

La situazione è quindi cosi espressa:
$$h(\overline{x})=\max_{y\in\mathcal Y}\sum\limits_{i=1}^{s}\omega^{(i)}\mathbb 1[h^{i}(\overline{x})=y]$$
dove $\mathbb 1[\cdot]$ è la **funzione indicatrice**, che vale $1$ se il predicato nelle parentesi quadre è Vero, $0$ altrimenti.

I tre approcci che abbiamo visto quindi si differenziano su vari aspetti, ovvero:
1) Nel primo approccio, un algoritmo predefinito viene applicato ai dati di input comprendenti sia l'elemento $\overline{x}$ che l'intero training set $\mathcal T$
2) Nel secondo approccio, l'algoritmo da applicare ad ogni elemento $\overline{x}$ viene derivato in base al training set $\mathcal T$
3) Nel terzo approccio, nessun singolo algoritmo viene applicato all'elemento $\overline{x}$; la predizione viene invece calcolata partendo dalle predizioni ritornate dall'insieme dei predittori.

--- 
# Framework Probabilistici per il ML



## Rischio Empirico e Rischio Atteso
### Problemi con il Bias Induttivo