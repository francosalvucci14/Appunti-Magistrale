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
1. **funzione discriminativa** : Trovare la funzione $f:X\to\{1,\dots,\mathbf K\}$ che mappa ogni input $\mathbf x$ in una qualche classe $C_i$, tale che $i=f(\mathbf x)$
2. **approccio discriminativo** : Determinare la probabilità condizionata $p(C_j|\mathbf x)$ (***fase di inferenza***); usare questa distribuzione per assegnare un input ad una classe (***fase di decisione***)
3. **approccio generativo** : determinare le distribuzioni condizioni della classe $p(\mathbf x|C_{j})$ e le probabilità a priori $p(C_{j})$; applicare poi la regola di Bayes per derivare le probabilità a posteriori $p(C_{j}|\mathbf x)$; usare poi queste distribuzioni per assegnare un input ad una classe

Gli approcci $1,2$ sono **discriminativi**: affrontano il problema della classificazione derivando dal training set condizioni (come i confini decisionali) che, quando applicate a un punto, discriminano ciascuna classe dalle altre.

I confini tra le regioni sono specificati da **funzioni di discriminazione**

Nella regressione lineare, un modello prevede il valore target; la previsione viene effettuata tramite una funzione lineare $h(\mathbf x;\mathbf w, b) =\mathbf w^T\mathbf x + b = \overline{w}^T \overline{x}$ (è possibile applicare funzioni di base lineari). 

Nella classificazione, un modello prevede le probabilità delle classi, ovvero valori compresi tra $[0, 1]$; la previsione viene effettuata tramite un modello lineare generalizzato $h(\mathbf x;\mathbf w, b)= f(\mathbf w^T \mathbf x+b)$, dove $f$ è una **funzione di attivazione non lineare** con codominio $[0, 1]$

I confini corrispondono alla soluzione di $h(\mathbf x;\mathbf w, b)=c$ per una certa costante $c$; ciò si traduce in $\mathbf w^T\mathbf x + b = f^{-1}(c)$, ovvero un confine lineare. 

La funzione inversa $f^{-1}$ è detta **funzione di collegamento**.

L'approccio 3 è **generativo**: funziona definendo, dal training set, un **modello** di elementi per ciascuna classe

Il modello è una distribuzione di probabilità (di feature condizionate dalla classe) e potrebbe essere utilizzato per la generazione casuale di nuovi elementi nella classe. 

Confrontando un elemento con tutti i modelli, è possibile verificare quello che meglio si adatta

## Funzioni Discriminanti

Funzioni discriminanti lineare in classificazione binaria
- confini decisionali: *iperpiano* $(d-1)$-dimensionale di tutti i punti tali per cui $h(\mathbf x;\mathbf w, b)=\mathbf w^T\mathbf x + b=0$
- Dati due punti sull'iperpiano $\overline{x}_{1},\overline{x}_2$, la condizione $h(\overline{x}_{1};\mathbf w, b)=h(\overline{x}_{2};\mathbf w, b)=0$ è pari a $$\mathbf w^T\overline{x}_{1}+b-(\mathbf w^T\overline{x}_2+b)=\mathbf w^T(\overline{x}_{1}-\overline{x}_{2})$$ovvero, il vettore $\overline{x}_{1}-\overline{x}_{2}$ e $\mathbf w$ sono ortogonali
- Per ogni $\mathbf x$, il prodotto $\mathbf w\cdot\mathbf x=\mathbf w^{T}\mathbf{x}$ è la lunghezza della proiezione di $\mathbf x$ nella direzione di $\mathbf w$ (ortogonale all'iperpiano $\mathbf w^T\mathbf x + b=0$ ), nei multipli di $||\mathbf w||_{2}$
- Normalizzando rispetto a $||\mathbf w||_{2}=\sqrt{\sum\limits_{i=1}^{d}w_{i}}$ , otteniamo la lunghezza della proiezione $\mathbf x$ nella direzione ortogonale
### Quadrati Minimi e Classificazione
#### Funzioni di apprendimento $h_{i}$
## Percettrone

