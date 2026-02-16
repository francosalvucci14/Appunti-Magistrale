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

![center|500](img/Pasted%20image%2020251014102318.png)


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

Ci sono sostanzialmente due **framework probabilistici** per il ML, che sono:
1) ***Training Object Generation Model***: Postuliamo che gli oggetti nel training set siano campionati da $\mathcal X$ secondo una **distribuzione di probabilità (marginale) sconosciuta** $p_M$. Formalmente, per qualsiasi $\overline{x} \in\mathcal X , p_M(\overline{x})$ rappresenta la probabilità che $\overline{x}$ sia il nuovo oggetto campionato nel training set
2) ***Training Target Generation Model***: Nel caso generale, si presume che le etichette associate agli elementi nel training set siano generate secondo una distribuzione di probabilità $p_C$, condizionata da $\mathcal X$ . Nello specifico, per ogni $t \in\mathcal Y, p_C(t|\overline{x})$ indica la probabilità che l'etichetta osservata dell'oggetto $\overline{x}$ nel training set sia $t$: ciò equivale a ipotizzare una **distribuzione congiunta** $p(\overline{x}, t) = p_M(\overline{x})p_C(t|\overline{x})$ per la generazione di coppie elemento-target. Per semplicità, inizialmente ipotizziamo una *relazione deterministica tra oggetti ed etichette*, rappresentata da una funzione sconosciuta $f$ tale per cui $t=f(\overline{x})$

Concentrandosi sull'approccio model-based descritto in precedenza, emergono diversi concetti chiave:

1) La qualità di un predittore $h$, come quello restituito dall'apprenditore, viene valutata in termini di ***rischio***. Per qualsiasi elemento $\overline{x}\in\mathcal X$ , l'*errore* di $h$ quando applicato a $\overline{x}$ deriva dal confronto tra la sua previsione $h(\overline{x})$ e l'etichetta target corretta $t$. Questo confronto viene quantificato utilizzando una funzione predefinita, chiamata ***loss function***, fatta in questo modo: $$L : \mathcal Y\times\mathcal Y\to\mathbb R$$
2) L'*errore* di una previsione $y = h(\overline{x})$ viene quindi definito in termini di **rischio di previsione**, dato dall'applicazione della funzione loss:$$\mathcal R_{f}(y,\overline{x})=L(y,f(\overline{x}))$$
3) Nel caso più generale, in cui si ipotizza solo una relazione probabilistica $p_C(y|\overline{x})$ (anziché una funzione $f$ ) tra un elemento e la sua etichetta corrispondente, il rischio di previsione corrisponde all'aspettativa della funzione loss rispetto a questa distribuzione, ovvero:$$\mathcal R_{p_{C}}(y,\overline{x})=\mathbb E_{t\sim p_{C}(\cdot|\overline{x})}[L(y,t)]=\int_{\mathcal Y}L(y,t)\cdot p_{C}(t|\overline{x})dt$$
4) Per i task di classificazione, questo diventa$$\mathcal R_{p_{C}}(y,\overline{x})=\mathbb E_{t\sim p_{C}(\cdot|\overline{x})}[L(y,t)]=\sum\limits_{t\in\mathcal Y}L(y,t)\cdot p_{C}(y|\overline{x})$$
Di seguito, faremo talvolta riferimento al caso più semplice di un task di classificazione binaria, dove $\mathcal Y = \{0, 1\}$, con la funzione loss $0-1$, e quindi $$L(y,t)=\mathbb 1[y\neq t]$$che ritorna $1$ se gli argomenti differiscono, $0$ altrimenti

Questo quadro probabilistico fornisce una base rigorosa per comprendere e valutare i modelli di apprendimento automatico, tenendo conto sia dell'incertezza intrinseca nella generazione dei dati sia delle prestazioni degli algoritmi predittivi.
## Rischio Empirico e Rischio Atteso

L'*errore* di un predittore $h$ è definito in termini di loss attesta su tutti gli oggetti nell'insieme $\mathcal X$, ovvero:
$$\mathcal R_{p_{M},f}(h)=\mathbb E_{x\sim p_{M}}[\mathcal R_{f}(h(\overline{x}),\overline{x})]=\mathbb E_{x\sim p_{M}}[L(h(\overline{x}),f(\overline{x}))]=\int_{\mathcal X}L(h(\overline{x}),f(\overline{x}))\cdot p_{M}(\overline{x})d\overline{x}$$
E nel caso generale, vale che $$\mathcal R_{p}(h)=\mathbb E_{(x,y)\sim p}[L(h(\overline{x}),t)]=\int_{\mathcal X}\int_{\mathcal Y}L(h(\overline{x}),t)\cdot p_{M}(\overline{x})\cdot p_{C}(t|\overline{x})d\overline{x}dt$$
Nel caso della funzione loss $0-1$, questa è solo la probabilità di una previsione errata in un elemento o coppia campionati casualmente, rispettivamente, ovvero:
$$\mathcal R_{p_{M},f}=\mathbb E_{x\sim p_{M}}[\mathbb 1[h(\overline{x})\neq f(\overline{x})]]=Pr_{x\sim p_M}[h(\overline{x})\neq f(\overline{x})]]$$
oppure
$$\mathcal R_{p}=\mathbb E_{(x,t)\sim p}[\mathbb 1[h(\overline{x})\neq t]]=Pr_{(x,t)\sim p}[h(\overline{x})\neq t]$$
Dato che $p_{M}$ e $f$ (oppure $p$) sono sconosciute, il rischio può solo essere stimato partendo dai dati disponibili (ovvero il training set $\mathcal T$)
Questo porta alla definizione di **rischio empirico** $\overline{\mathcal R}_{\mathcal T}(h)$, che prevede una stima dell'aspettazione della funzione loss, definita come la loss media sul training set, ovvero: 
$$\overline{\mathcal R}_{\mathcal T}=\frac{1}{|\mathcal T|}\sum\limits_{(x,y)\in\mathcal T}L(h(\overline{x}),t)$$
Nel caso della loss $0-1$, questa è la frazione degli elementi di $\mathcal T$ che sono mal classifcati da $h$, ovvero: 
$$\overline{\mathcal R}_{\mathcal T}=\frac{1}{|\mathcal T|}\sum\limits_{(x,y)\in\mathcal T}\mathbb 1[h(\overline{x})\neq t]=\frac{|\{(\overline{x},t)\in\mathcal T:h(\overline{x})\neq t\}|}{|\mathcal T|}$$

In questo modo, un problema di apprendimento viene ridotto a un ***problema di minimizzazione*** in uno spazio funzionale $\mathcal H$, l'insieme di tutti i possibili predittori $h$.
$$h_{\mathcal T}=\min_{h\in\mathcal H}\overline{\mathcal R}_{\mathcal T}(h)$$
Qui, $\mathcal H$ è l'insieme delle ***ipotesi*** o ***bias induttivo***

### Problemi con il Bias Induttivo

La scelta dell'insieme di ipotesi è una questione importante nel ML. In particolare, potremmo chiederci: 
- qual è l'effetto della struttura e delle dimensioni di $\mathcal H$?
- come definire H in modo tale da rendere fattibile il calcolo di $h_{\mathcal T}$? 

Per quanto riguarda la scelta della classe di ipotesi $\mathcal H$, essa può essere vista come il riflesso di alcune conoscenze preliminari che l'apprenditore ha riguardo al compito, nella convinzione che uno dei membri della classe $\mathcal H$ sia un predittore a basso errore per il compito.

Un modo banale per perseguire l'obiettivo di derivare predittori con un rischio minimo sarebbe quello di definire una classe molto ricca, cioè supponendo che molte funzioni possibili appartengano a $\mathcal H$: come limite, $\mathcal H$ potrebbe essere definito semplicemente come l'insieme di tutte le funzioni $f : \mathcal X \to\mathcal Y$.

Questo approccio, tuttavia, può facilmente causare problemi.

Supponiamo, infatti, un problema di classificazione binaria con training set $\mathcal T = (\mathcal X, t)$, con loss $0/1$, definita come segue
$$L(y,t)=\begin{cases}
0&y=t\\1&\text{altrimenti}
\end{cases}$$
Così facendo, la perdita è pari a $1$ se l'elemento è classificato erroneamente, altrimenti è pari a $0$ 
Di conseguenza, il *rischio* è il **numero atteso di errori di classificazione**, mentre il *rischio empirico* è la **frazione di elementi nel training set che sono classificati erroneamente**.

Supponiamo inoltre che $p_C(t = 1|\overline{x}) = \frac{1}{2} \forall\space\overline{x}\in\mathcal X$ , ovvero che le due classi abbiano la stessa dimensione nella popolazione.

Consideriamo la funzione di classificazione definita come:
$$h_{\mathcal T}(\overline{x})=\begin{cases}
1&\overline{x}=\overline{x}_i\in\mathcal X,t_{i}=1\\0&\text{altrimenti}
\end{cases}$$
ovvero un predittore che assegna alla classe $1$ tutti gli elementi etichettati come $1$ nel training set, mentre tutti gli altri elementi vengono classificati come $0$.

Chiaramente, il rischio empirico qui è $0$ per definizione, ma il rischio generale è $\approx \frac{1}{2}$ 

Quando viene applicato a un set di dati campionato casualmente dalla popolazione, la qualità di $h_{\mathcal T}$ è la stessa di una funzione che assegna casualmente gli elementi alle classi.

Questo fenomeno è chiamato **overfitting**: il metodo di classificazione funziona bene sul set di addestramento, ma male su altri elementi della popolazione.

Tuttavia, se $\mathcal H$ è molto piccolo, può accadere che nessun predittore di questo set sia in grado di fornire un rischio accettabilmente piccolo.

Riassumendo, si possono fare le seguenti considerazioni generali per quanto riguarda la dimensione di $\mathcal H$.
1) Se $\mathcal H$ è troppo grande (complesso), può verificarsi un **overfitting**: può essere disponibile una funzione che si comporta molto bene sul training set , ma che tuttavia ha prestazioni scadenti sui nuovi dati
2) Se $\mathcal H$ è troppo piccolo (semplice), può verificarsi un **underfitting**: in $\mathcal H$ non è disponibile alcuna funzione che si comporti in modo soddisfacente, sia sul training set che sui nuovi set di dati.

Ciò è correlato al cosiddetto **compromesso tra bias e varianza**.

