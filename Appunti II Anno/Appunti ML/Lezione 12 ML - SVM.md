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
# Support Vector Machine

Il problema della classificazione binaria viene affrontato in modo diretto, ovvero cerchiamo di trovare un piano che separi le classi nello spazio delle feature (in realtà, un piano “ottimale”, secondo una caratteristica ragionevole). 

Se ciò non è possibile, adottiamo due approcci creativi:
- Ammorbidiamo il significato di “separare” e/o
- Arricchiamo e ampliamo lo spazio delle caratteristiche in modo che la separazione sia (più) possibile

Prima di tutto, osserviamo che la maggior parte degli algoritmi di classificazione non produce solo un'etichetta di classe, ma anche un punteggio, e l' etichetta prevista viene assegnata sulla base di tale punteggio, che viene confrontato con una soglia.

Nella classificazione lineare, il punteggio viene calcolato come una combinazione lineare $\mathbf{w}^T \mathbf x + b$ delle feature.

Ad esempio, la regressione logistica restituisce la probabilità di classe
$$p(y=1|\mathbf x)=\sigma(\mathbf w^{T}\mathbf x+b)\in[0,1]$$
e potremmo seguire la strategia di prevedere la classe $1$ se la probabilità della classe è $\gt 0,5$.

Essenzialmente, il punteggio è una stima della confidenza: più è lontano dalla soglia, più siamo sicuri della previsione. 

In termini geometrici, il punteggio rappresenta anche la distanza fra il punto corrispondente all'elemento dato e il confine decisionale, che è l'iperpiano $\mathbf{w}^T \mathbf x + b=0$

![center|500](img/Pasted%20image%2020251219155957.png)

Per esempio, nel seguente caso:

![center|400](img/Pasted%20image%2020251219160421.png)

$A$ può essere assegnato a $\mathbf C_1$ con maggiore sicurezza rispetto a $B$ e con ancora maggiore sicurezza rispetto a $C$.

Queste considerazioni, se applicate alla fase di addestramento, portano a preferire confini decisionali tali che tutti gli elementi nel training set siano classificati correttamente (si trovano nella regione decisionale corretta) e fare riferimento a quel confine ci rende sicuri di tale classificazione (si trovano abbastanza lontani dal confine).

Intuitivamente, vogliamo selezionare confini che classifichino correttamente gli elementi nel training set caratterizzati da un margine di spazio intorno a essi che non contenga alcun elemento.

Più in dettaglio, consideriamo un classificatore binario che, per qualsiasi elemento $\mathbf x$, restituisce un valore $y \in \{-1, 1\}$, dove supponiamo che $\mathbf x$ sia assegnato a $C_0$ se $y = -1$ e a $C_1$ se $y = 1$.

Inoltre, consideriamo classificatori lineari come
$$h(\mathbf x)=g(\mathbf w^{T}\mathbf x+b)=g(\overline{\pmb w}^{T}\overline{\pmb x})$$
dove $$g(z)=\begin{cases}1&z\geq0\\-1&z\lt0\end{cases}$$
La previsione sulla classe di $\mathbf x$ viene quindi fornita derivando un valore in $\{-1, 1\}$ proprio come nel caso di un percettrone, ovvero senza alcuna stima delle probabilità $p(C_i|\mathbf x)$ che $\mathbf x$ appartenga a ciascuna classe.

Per qualsiasi elemento del training set $(\mathbf x_i, t_i)$, il **margine funzionale** di $(\mathbf w, b) = \overline{\mathbf w}$ rispetto a tale elemento è definito come:
$$\overline{\gamma}_{i}=t_{i}(\mathbf w^{T}\mathbf x+b)=t_{i}\overline{\mathbf w}^{T}\overline{\mathbf x}_{i}$$

Si osservi che la previsione risultante è corretta se e solo se $\overline{\gamma}_i > 0$.

Inoltre, assumiamo che valori maggiori di $\overline{\gamma}_i$ indichino una maggiore confidenza nella previsione.

Dato un training set $\mathcal{T} = \{(\mathbf{x}_1, t_1), \dots, (\mathbf{x}_n, t_n)\}$, il margine funzionale di $\overline{\mathbf{w}}$ rispetto a $\mathcal{T}$ è il margine funzionale minimo tra tutti gli elementi in $\mathcal{T}$:

$$\overline{\gamma} = \min_{i} \overline{\gamma}_i$$

Tuttavia, abbiamo un problema con questa definizione:

- Se riscaliamo i parametri $\overline{\mathbf{w}}$ per uno scalare $\alpha > 0$, otteniamo nuovi parametri $\alpha\overline{\mathbf{w}}$, ovvero $\alpha\mathbf{w}, \alpha b$.    
- L'utilizzo di $\alpha\overline{\mathbf{w}}$ non cambia la classificazione dei punti.
- Tuttavia, il margine $\alpha\overline{\mathbf{w}}^T \overline{\mathbf{x}}_i = \alpha\mathbf{w}^T \mathbf{x}_i + \alpha b$ risulta ora scalato di $\alpha$.

Non ha senso che lo stesso confine di classificazione possa avere margini diversi quando lo riscaliamo.

Al fine di superare questo inconveniente, definiamo il **margine geometrico** $\gamma_i$ rispetto a un esempio di addestramento $(\mathbf{x}_i, t_i)$ come:
$$\gamma_{i}=t_{i}\left(\frac{\mathbf w^{T}}{||\mathbf w||}\mathbf x_{i}+\frac{b}{||\mathbf w||}\right)=\frac{\overline{\gamma_{i}}}{||\mathbf w||}$$
dove, come di consueto, $\|\mathbf{w}\| = \sqrt{\sum_{i=1}^d w_i^2}$. 

Il margine geometrico $\gamma_i$ equivale alla distanza (con segno) tra $\mathbf{x}_i$ e l'iperpiano definito da $\mathbf{w}, b$, ovvero la lunghezza del segmento di retta da $\mathbf{x}_i$ alla sua proiezione sull'iperpiano di confine, espressa utilizzando $\|\mathbf{w}\|$ come unità di distanza.

![center|400](img/Pasted%20image%2020251219162249.png)

Diversamente da $\overline{\gamma}_i$, il margine geometrico $\gamma_i$ è invariante rispetto al riscalamento dei parametri. 

Infatti, sostituendo $\alpha\overline{\mathbf{w}}$ a $\overline{\mathbf{w}}$, abbiamo:

$$t_i \overline{\mathbf{w}}^T \overline{\mathbf{x}}_i = t_i (\mathbf{w}^T \mathbf{x}_i + b) = \overline{\gamma}_i$$
$$t_i (\alpha\overline{\mathbf{w}})^T \overline{\mathbf{x}}_i = t_i (\alpha\mathbf{w}^T \mathbf{x}_i + \alpha b) = \alpha t_i (\mathbf{w}^T \mathbf{x}_i + b) = \alpha (t_i \overline{\mathbf{w}}^T \overline{\mathbf{x}}_i) = \alpha \overline{\gamma}_i$$

mentre

$$t_i \frac{\overline{\mathbf{w}}^T}{\|\mathbf{w}\|} \overline{\mathbf{x}}_i = t_i \left( \frac{\mathbf{w}^T}{\|\mathbf{w}\|} \mathbf{x}_i + \frac{b}{\|\mathbf{w}\|} \right) = \gamma_i$$

$$t_i \frac{(\alpha\overline{\mathbf{w}})^T}{\|(\alpha\mathbf{w})\|} \overline{\mathbf{x}}_i = t_i \left( \frac{\alpha\mathbf{w}^T}{\alpha\|\mathbf{w}\|} \mathbf{x}_i + \frac{\alpha b}{\alpha\|\mathbf{w}\|} \right) = t_i \left( \frac{\mathbf{w}^T}{\|\mathbf{w}\|} \mathbf{x}_i + \frac{b}{\|\mathbf{w}\|} \right) = \gamma_i$$

- Il margine geometrico rispetto al training set $\mathcal{T} = \{(\mathbf{x}_1, t_1), \dots, (\mathbf{x}_n, t_n)\}$ è quindi definito come il più piccolo margine geometrico tra tutti gli elementi $(\mathbf{x}_i, t_i)$:$$\gamma = \min_{i} \gamma_i$$
- Un'interpretazione utile di $\gamma$ è come la metà dell'ampiezza della fascia più larga, centrata sull'iperpiano $\mathbf{w}^T \mathbf{x} + b = 0$, che non contiene nessuno dei punti $\mathbf{x}_1, \dots, \mathbf{x}_n$.
- Gli iperpiani sul confine di tale fascia, ciascuno a distanza $\gamma$ dall'iperpiano e passanti (almeno uno di essi) attraverso qualche punto $\mathbf{x}_i$, sono detti **iperpiani a margine massimo** (maximum margin hyperplanes).

![center|500](img/Pasted%20image%2020251219162354.png)

## Optimal margin classifiers

Dato un training set $\mathcal T$ , desideriamo trovare gli iperpiani che separano le due classi (se esistono) e hanno $\gamma$ massimo: rendendo la distanza tra gli iperpiani e l'insieme di punti corrispondenti agli elementi il più grande possibile, aumenta la confidenza nella classificazione fornita.

Supponiamo che le classi siano linearmente separabili nel training set: esiste quindi un iperpiano (anzi, un'infinità di essi) che separa gli elementi in $C_1$ dagli elementi in $C_2$. 

Per trovare quello tra questi iperpiani che massimizza $γ$, dobbiamo risolvere il seguente problema di ottimizzazione
$$\begin{align*}
&\max_{\mathbf w,b}\gamma\\
&\text{sotto il vincolo }\gamma_{i}=\frac{t_{i}}{||\mathbf w||}(\mathbf w^{T}\mathbf x_{i}+b)\geq\gamma\quad i=1,\dots,n
\end{align*}$$
che massimizza il margine più piccolo sul training set $(\mathbf{x}_1, t_1)$
Garantisce che ogni punto abbia un margine almeno pai a  $\gamma$
Ciò corrisponde a :
$$\begin{align*}
&\max_{\mathbf w,b}\gamma\\
&\text{sotto il vincolo }t_{i}(\mathbf w^{T}\mathbf x_{i}+b)\geq\gamma||\mathbf w||\quad i=1,\dots,n
\end{align*}$$
Come osservato, se tutti i parametri sono scalati da una costante $\alpha$, tutti i margini geometrici $\gamma_{i}$ tra gli elementi e l' iperpiano rimangono invariati: possiamo quindi sfruttare questa libertà per introdurre il vincolo
$$\min_{i}(\mathbf w^{T}\mathbf x_{i}+b)t_{i}=1$$
Ciò si ottiene assumendo $||\mathbf w|| = \frac{1}{\gamma}$ , che corrisponde a considerare una scala in cui il margine massimo ha larghezza $2$. 
Ciò si traduce, per ciascun elemento $\mathbf x_i, t_i$, in un vincolo
$$y_{i}=t_{i}(\mathbf w^{T}\mathbf x_{i}+b)\geq1$$
Un elemento (punto) è detto **attivo** se la disuguaglianza vale, ovvero se:
$$t_{i}(\mathbf w^{T}\mathbf x_{i}+b)=1$$
ed è detto **inattivo** se non vale.

Si osservi che, per definizione, deve esistere almeno un punto attivo.

Per ogni elemento $(\mathbf x, t)$, casi diversi corrispondono al valore della combinazione lineare con segno $t(\mathbf w^{T}\mathbf x+b)$:

1. $t(\mathbf w^{T}\mathbf x+b) \gt 1 \implies\mathbf x$ si trova nella regione corrispondente alla sua classe, al di fuori della fascia di margine
2. $t(wT x + b) = 1\implies\mathbf x$ si trova nella regione corrispondente alla sua classe, sull'iperpiano di margine massimo
3. $0 \lt t(\mathbf w^{T}\mathbf x+b) \lt 1 \implies\mathbf x$ si trova nella regione corrispondente alla sua classe, all'interno della striscia di margine
4. $\mathbf w^{T}\mathbf x+b = 0 \implies\mathbf x$ si trova sull'iperpiano di separazione
5. $-1 \lt t(\mathbf w^{T}\mathbf x+b) \lt 0\implies\mathbf x$ si trova nella regione corrispondente all'altra classe, all'interno della striscia di margine
6. $t(\mathbf w^{T}\mathbf x+b)=-1\implies\mathbf x$ si trova nella regione corrispondente all'altra classe, sull'iperpiano di margine massimo
7. $t(\mathbf w^{T}\mathbf x+b)\lt-1\implies\mathbf x$ si trova nella regione corrispondente all'altra classe, al di fuori della striscia di margine

Il problema di ottimizzazione è quindi trasformato in:
$$\begin{align*}
&\max_{\mathbf w,b}\gamma=||\mathbf w||^{-1}\\
&\text{sotto il vincolo }t_{i}(\mathbf w^{T}\mathbf x_{i}+b)\geq1\quad i=1,\dots,n
\end{align*}$$
Massimizzare $||\mathbf w||^{-1}$ è equivalente a minimizzare $||\mathbf w||^{2}$: quindi possiamo riformulare il problema come:
$$\begin{align*}
&\min_{\mathbf w,b}\frac{1}{2}||\mathbf w||^{2}\\
&\text{sotto il vincolo }t_{i}(\mathbf w^{T}\mathbf x_{i}+b)\geq1\quad i=1,\dots,n
\end{align*}$$
Si tratta di un ***problema di ottimizzazione quadratica convessa***. 

La funzione da minimizzare è infatti convessa e l'insieme dei punti che soddisfano il vincolo è un poliedro convesso (intersezione di semispazi).
## Duality

Dalla teoria dell'ottimizzazione deriva che, data la struttura del problema (vincoli lineari + convessità):
- esiste una **formulazione duale** del problema
- l'ottimale del problema duale è lo stesso del problema originale (primario)

### Lagrangian

Consideriamo il problema di ottimizzazione
$$\min_{\mathbf x\in\Omega}f(\mathbf x)$$
dove $\Omega$ è la regione ammissibile, definita dai vincoli
$$g_i(\mathbf x)\leq0\quad i=1,\dots,n$$
dove $f(\mathbf x),g_i(\mathbf x)$ sono funzioni convesse, e $\Omega$ è un insieme convesso

Il **Lagrangiano** è definito come:
$$L(\mathbf x,\lambda)=f(\mathbf x)+\sum\limits_{i=1}^{k}\lambda_ig_{i}(\mathbf x)$$

Consideriamo il massimo rispetto a un $\lambda$ non negativa del Lagrangiano:
$$\begin{align*}
&\max_{\lambda}L(\mathbf x,\lambda)=f(\mathbf x)+\max_{\lambda}\sum\limits_{i=1}^{k}\lambda_ig_{i}(\mathbf x)\\
&\lambda_{i}\geq0\quad i=1,\dots,n
\end{align*}$$
che è una funzione di $\mathbf x$
- se $\mathbf x$ è una soluzione ammissibile, $g_{i}(\mathbf x)\geq0$ per tutti gli $i$ e il massimo viene ottenuto quando $\lambda_{i}=0$: come conseguenza, otteniamo che $$\max_{\lambda:\lambda_i\geq0}L(\mathbf x,\lambda)=f(\mathbf x)$$
- se $\mathbf x$ è soluzione non-ammissibile, allora $g_{i}(\mathbf x)\gt0$ per alcuni $i$ e il massimo è illimitato, poiché $\lambda_i$ può essere arbitrariamente grande

Di conseguenza, il massimo del lagrangiano è uguale a $f(\mathbf x)$ se $\mathbf x$ è fattibile, mentre è illimitato se $\mathbf x$ non è fattibile. 

Ciò si traduce, nel caso in cui esista un minimo $\mathbf x^{\star}$, in
$$\min_{\mathbf x\in\Omega}f(\mathbf x)=\min_{\mathbf x\in\Omega}\max_{\lambda:\lambda_{i}\geq0}L(\mathbf x,\lambda)$$

In generale, vale la **proprietà di dualità debole**
$$\max_{\lambda:\lambda_{i}\geq0}\min_{\mathbf x\in\Omega}L(\mathbf x,\lambda)\leq \min_{\mathbf x\in\Omega}\max_{\lambda:\lambda_{i}\geq0}L(\mathbf x,\lambda)=\min_{\mathbf x\in\Omega}f(\mathbf x)$$

dove $\max_{\lambda:\lambda_{i}\geq0}\min_{\mathbf x\in\Omega}L(\mathbf x,\lambda)$ è il problema **duale** di $\min_{\mathbf x\in\Omega}f(\mathbf x)$

Inoltre, nel caso dell'ottimizzazione convessa (il nostro caso specifico), vale la proprietà di dualità forte
$$\max_{\lambda:\lambda_{i}\geq0}\min_{\mathbf x\in\Omega}L(\mathbf x,\lambda)= \min_{\mathbf x\in\Omega}\max_{\lambda:\lambda_{i}\geq0}L(\mathbf x,\lambda)=\min_{\mathbf x\in\Omega}f(\mathbf x)$$
### Karus-Kuhn-Tucker conditions

Le seguenti condizioni necessarie e sufficienti valgono all'ottimo $(\mathbf{x}^*, \lambda^*)$, e possono essere utilizzate per semplificare la definizione del problema duale.
$$\nabla_{\mathbf{x}} L(\mathbf{x}, \lambda) \Big|_{\mathbf{x}^*, \lambda^*} = \mathbf{0}$$$$\frac{\partial L(\mathbf{x}, \lambda)}{\partial \lambda_i} \Big|_{\mathbf{x}^*, \lambda^*} = g_i(\mathbf{x}^*) \ge 0 \quad i = 1, \dots, k$$$$\lambda_i^* \ge 0 \quad i = 1, \dots, k$$$$\lambda_i^* g_i(\mathbf{x}^*) = 0 \quad i = 1, \dots, k$$
Affinché l'ottimo sia un minimo, deve valere la condizione del secondo ordine per cui l'Hessiana $H_{\mathbf{x}}$ valutata in $\mathbf{x}^*$ deve essere definita positiva.

**Nota:** l'ultima condizione (**complementary slackness**, o complementarità dei vincoli) afferma che un moltiplicatore lagrangiano $\lambda_i^*$ può essere diverso da zero solo se $g_i(\mathbf{x}^*) = 0$, ovvero se $\mathbf{x}^*$ si trova "al limite" per il vincolo $g_i(\mathbf{x}) \le 0$. In questo caso, il vincolo è detto **attivo**.
## Application to SVM

Nel nostro caso:
- $f(\mathbf x)$ corrisponde a $\frac{1}{2}||\mathbf w||^{2}$
- $g_{i}(\mathbf x)$ corrisponde a $t_{i}(\mathbf w^{T}\mathbf x_{i}+b)-1\geq0$
- $\Omega$ è l'intersezione di un insieme di iperpiani, ovvero un poliedro, quindi convesso

Il corrispondente Lagrangiano è quindi:
$$\begin{align*}
L(\overline{\mathbf w},\lambda)&=\frac{1}{2}||\mathbf w||^{2}-\sum\limits_{i=1}^{n}\lambda_{i}((\mathbf w^{T}\mathbf x_{i}+b)t_{i}-1)\\
&=\frac{1}{2}\mathbf w^{T}\mathbf w-\sum\limits_{i=1}^{n}\lambda_i\mathbf w^{T}\mathbf x_{i}t_{i}-b\sum\limits_{i=1}^{n}\lambda_it_{i}+\sum\limits_{i=1}^{n}\lambda_{i}
\end{align*}$$
ed il problema duale (con stessa ottimizzazione) è :
$$\begin{align*}
&\max_{\lambda}\min_{\overline{\mathbf w}}L(\overline{\mathbf w},\lambda)\\
&\lambda_i\geq0\quad i=1,\dots,k
\end{align*}$$

### Applying the KKT conditions

Al fine di esprimere il problema duale come funzione di $\lambda$, deriviamo i valori dei coefficienti $\overline{\mathbf{w}}$ all'ottimo di $L(\overline{\mathbf{w}}, \lambda)$, applicando le condizioni di Karush-Kuhn-Tucker (KKT).

Per prima cosa, calcoliamo:
$$\frac{\partial L(\overline{\mathbf{w}}, \lambda)}{\partial w_k} \bigg|_{\mathbf{w}^*, b^*} = w_k^* - \sum_{i=1}^{n} \lambda_i t_i x_{ik} = 0$$$$\frac{\partial L(\overline{\mathbf{w}}, \lambda)}{\partial b} \bigg|_{\mathbf{w}^*, b^*} = \sum_{i=1}^{n} \lambda_i t_i = 0$$Ovvero:
$$\nabla_{\mathbf{w}} L(\overline{\mathbf{w}}, \lambda) \bigg|_{\mathbf{w}^*, b^*} = \mathbf{w}^* - \sum_{i=1}^{n} \lambda_i t_i \mathbf{x}_i = \mathbf{0}$$$$\frac{\partial L(\overline{\mathbf{w}}, \lambda)}{\partial b} \bigg|_{\mathbf{w}^*, b^*} = \sum_{i=1}^{n} \lambda_i t_i = 0$$
Le condizioni KKT risultanti sono
$$\mathbf{w}^* = \sum_{i=1}^{n} \lambda_i t_i \mathbf{x}_i$$$$\sum_{i=1}^{n} \lambda_i t_i = 0$$$$t_i(\mathbf{w}^{*T} \mathbf{x}_i + b^*) - 1 \ge 0 \quad \text{per } i = 1, \dots, n$$$$\lambda_i \ge 0 \quad \text{per } i = 1, \dots, n$$$$\lambda_i \left( t_i(\mathbf{w}^{*T} \mathbf{x}_i + b^*) - 1 \right) = 0 \quad \text{per } i = 1, \dots, n$$
Sostituendo i valori dei coefficienti $\mathbf{w}^*$ secondo le equazioni sopra riportate e osservando che $b^*$ è moltiplicato per zero, possiamo affermare che all'ottimo $\overline{\mathbf{w}}^*$ il problema duale richiede di massimizzare
$$\begin{align*}
L(\lambda) &= \frac{1}{2} \mathbf{w}^{*T} \mathbf{w}^* - \sum_{i=1}^n \lambda_i t_i \mathbf{w}^{*T} \mathbf{x}_i - b^* \sum_{i=1}^n \lambda_i t_i + \sum_{i=1}^n \lambda_i\\
&= \frac{1}{2} \left( \sum_{i=1}^n \lambda_i t_i \mathbf{x}_i \right)^T \sum_{j=1}^n \lambda_j t_j \mathbf{x}_j - \sum_{i=1}^n \lambda_i t_i \mathbf{x}_i^T \sum_{j=1}^n \lambda_j t_j \mathbf{x}_j + \sum_{i=1}^n \lambda_i\\
&= \frac{1}{2} \sum_{i=1}^n \lambda_i t_i \mathbf{x}_i^T \sum_{j=1}^n \lambda_j t_j \mathbf{x}_j - \sum_{i=1}^n \lambda_i t_i \mathbf{x}_i^T \sum_{j=1}^n \lambda_j t_j \mathbf{x}_j + \sum_{i=1}^n \lambda_i\\
&= \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \mathbf{x}_i^T \mathbf{x}_j - \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \mathbf{x}_i^T \mathbf{x}_j + \sum_{i=1}^n \lambda_i\\
&= \sum_{i=1}^n \lambda_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \mathbf{x}_i^T \mathbf{x}_j
\end{align*}$$
con i seguenti vincoli su $\lambda$:
$$\begin{align*}
&\sum_{i=1}^n \lambda_i t_i = 0\\
&\lambda_i \ge 0 \quad \text{per } i = 1, \dots, n
\end{align*}$$
**Nota:** Si può dimostrare che le restanti due condizioni KKT sono sempre verificate.
# Dual SVM problem

Abbiamo modificato la definizione del problema duale applicando le condizioni KKT per eliminare le occorrenze dei coefficienti $\mathbf{w}, b$ da $L(\mathbf{w}, b, \lambda)$. 

Il nuovo problema ha lo stesso ottimo del **primale originale**, dove le condizioni KKT saranno effettivamente soddisfatte, collegando i valori delle soluzioni ottime dei due problemi.

$$\begin{gathered} &\max_{\lambda} L(\lambda) = \max_{\lambda} \left( \sum_{i=1}^n \lambda_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \mathbf{x}_i^T \mathbf{x}_j \right) \\&\lambda_{i}\geq0\quad i=1,\dots,n
\\
&\text{con i vincoli: } \sum_{i=1}^n \lambda_i t_i = 0, \quad i = 1, \dots, n \end{gathered}$$

Tutte le considerazioni sopra esposte valgono chiaramente se ipotizziamo l'applicazione di un insieme di funzioni di base $\phi$, risultando così nel problema duale che apre la strada all'utilizzo dei kernel:

$$\begin{gathered} \max_{\lambda} L(\lambda) = \max_{\lambda} \left( \sum_{i=1}^n \lambda_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j) \right) \\ \text{soggetto a: } \lambda_i \ge 0, \quad \sum_{i=1}^n \lambda_i t_i = 0 \end{gathered}$$

Definendo la **funzione kernel**
$$\mathcal k(\mathbf x_{i},\mathbf x_{j})=\phi(\mathbf x_{i})\phi(\mathbf x_{j})=\phi(\mathbf x_{i})^{T}\phi(\mathbf x_{j})$$
la formulazione del problema duale può essere riscritta come:
$$\begin{gathered} \max_{\lambda} L(\lambda) = \max_{\lambda} \left( \sum_{i=1}^n \lambda_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \mathcal k(\mathbf x_{i},\mathbf x_{j}) \right) \\ \text{soggetto a: } \lambda_i \ge 0, \quad \sum_{i=1}^n \lambda_i t_i = 0 \end{gathered}$$
Passare da primale a duale porta con sè vantaggi e svantaggi:
- **vantaggio** : Il numero di variabili da considerare, che sono rilevanti per la classificazione, esce fuori essere molto più piccolo di $n$
- **svantaggio** : Il numero di variabili incrementa da $m$ a $n$ (in particolare, se $\mathbf x=\mathbf x$, da $d$ a $n$)

Risolvendo il problema duale, si ottengono i valori ottimali dei moltiplicatori di Lagrange $\lambda^*$. 
I valori ottimali dei parametri $\mathbf{w}^*$ vengono quindi derivati attraverso le relazioni:

$$w_i^* = \sum_{j=1}^n \lambda_j^* t_j \phi_i(\mathbf{x}_j) \quad i = 1, \dots, m$$

Il valore di $b^*$ può essere ottenuto osservando che, per ogni vettore di supporto $\mathbf{x}_k$ (caratterizzato dalla condizione $\lambda_k \ge 0$), deve essere:

$$\begin{aligned} 1 &= t_k \left( \mathbf{w}^{*T} \phi(\mathbf{x}_k) + b^* \right) = t_k \left( \sum_{j=1}^n \lambda_j^* t_j \phi(\mathbf{x}_j)^T \phi(\mathbf{x}_k) + b^* \right) \\ &= t_k \left( \sum_{j=1}^n \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}_k) + b^* \right) = t_k \left( \sum_{j \in \mathcal{S}} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}_k) + b^* \right) \end{aligned}$$

dove $\mathcal{S}$ è l'insieme degli indici dei vettori di supporto. Di conseguenza, poiché $t_k = \pm 1$, per avere un prodotto unitario deve essere:

$$t_k = \sum_{j \in \mathcal{S}} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}_k) + b^*$$

e:

$$b^* = t_k - \sum_{j \in \mathcal{S}} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}_k)$$

Una soluzione più precisa può essere ottenuta come il valore medio ottenuto considerando tutti i vettori di supporto:

$$b^* = \frac{1}{|\mathcal{S}|} \sum_{i \in \mathcal{S}} \left( t_i - \sum_{j \in \mathcal{S}} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}_i) \right)$$

## Classification through SVM

Un nuovo elemento $\mathbf{x}$ può essere classificato, dato un insieme di funzioni base $\phi$ o una funzione kernel $\kappa$, controllando il segno di
$$h(\mathbf{x}) = \sum_{i=1}^{m} w_i^* \phi_i(\mathbf{x}) + b^* = \sum_{j=1}^{n} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}) + b^*$$

Come osservato, se $\mathbf{x}_i$ non è un vettore di supporto, allora deve essere $\lambda_i^* = 0$. Pertanto, la somma precedente può essere scritta come

$$h(\mathbf{x}) = \sum_{j \in \mathcal{S}} \lambda_j^* t_j \kappa(\mathbf{x}_j, \mathbf{x}) + b^*$$

La classificazione eseguita attraverso la formulazione duale, utilizzando la funzione kernel, non tiene conto di tutti gli elementi del training set, ma solo dei vettori di supporto, solitamente un sottoinsieme piuttosto piccolo del training set.
### Non separability in the training set

L'approccio descritto in precedenza, quando applicato a insiemi non linearmente separabili, non fornisce soluzioni accettabili: è infatti impossibile soddisfare tutti i vincoli
$$t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) \geq 1 \quad i = 1, \dots, n$$
Questi vincoli devono quindi essere allentati per permettere loro di non valere, al costo di un certo aumento della funzione obiettivo da minimizzare   

Viene introdotta una **variabile slack** $\xi_i$ per ogni vincolo, per fornire una misura di quanto il vincolo non sia verificato

Questo può essere formalizzato come
$$\begin{align*}
&\min_{\mathbf{w},b,\boldsymbol{\xi}} \frac{1}{2} \mathbf{w}^T \mathbf{w} + C \sum_{i=1}^n \xi_i\\
&t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) \geq 1 - \xi_i \quad i = 1, \dots, n\\
&\xi_i \geq 0 \quad i = 1, \dots, n
\end{align*}$$
dove $\boldsymbol{\xi} = (\xi_1, \dots, \xi_n)$

Introducendo moltiplicatori opportuni, si può ottenere la seguente Lagrangiana
$$\begin{aligned} L(\mathbf{w},b,\boldsymbol{\xi}, \boldsymbol{\lambda}, \boldsymbol{\alpha}) &= \\ &= \frac{1}{2} \mathbf{w}^T \mathbf{w} + C \sum_{i=1}^n \xi_i - \sum_{i=1}^n \lambda_i (y_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) - 1 + \xi_i) - \sum_{i=1}^n \alpha_i \xi_i \\ &= \frac{1}{2} \sum_{i=1}^n w_i^2 + \sum_{i=1}^n (C - \alpha_i) \xi_i - \sum_{i=1}^n \lambda_i (t_i(\sum_{j=1}^m w_j \phi_j(\mathbf{x}_i)) + b) - 1 + \xi_i) \\ &= \frac{1}{2} \sum_{i=1}^n w_i^2 + \sum_{i=1}^n (C - \alpha_i - \lambda_i) \xi_i - \sum_{i=1}^n \sum_{j=1}^m \lambda_i t_i w_j \phi_j(\mathbf{x}_i) + b \sum_{i=1}^n \lambda_i t_i + \sum_{i=1}^n \lambda_i \end{aligned}$$

dove $\alpha_i \geq 0$ e $\lambda_i \geq 0$, per $i = 1, \dots, n$.

Le condizioni di Karush-Kuhn-Tucker sono ora:

|**Equazione**|**Descrizione**|
|---|---|
|$\frac{\partial}{\partial \mathbf{w}} L(\mathbf{w}, b, \boldsymbol{\xi}, \lambda, \alpha) = \mathbf{0}$|gradiente nullo|
|$\frac{\partial}{\partial b} L(\mathbf{w}, b, \boldsymbol{\xi}, \lambda, \alpha) = 0$|gradiente nullo|
|$\frac{\partial}{\partial \boldsymbol{\xi}} L(\mathbf{w}, b, \boldsymbol{\xi}, \lambda, \alpha) = \mathbf{0}$|gradiente nullo|
|$t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) - 1 + \xi_i \geq 0 \quad i = 1, \dots, n$|vincoli|
|$\xi_i \geq 0 \quad i = 1, \dots, n$|vincoli|
|$\lambda_i \geq 0 \quad i = 1, \dots, n$|moltiplicatori|
|$\alpha_i \geq 0 \quad i = 1, \dots, n$|moltiplicatori|
|$\lambda_i (t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) - 1 + \xi_i) = 0 \quad i = 1, \dots, n$|complementarità (slackness)|
|$\alpha_i \xi_i = 0 \quad i = 1, \dots, n$|complementarità (slackness)|

**Derivazione di una formulazione duale**

Dalle condizioni di gradiente nullo rispetto a $w_i, b, \xi_j$ si ricava:

$$\begin{align*}
&w_i = \sum_{j=1}^n \lambda_j t_j \phi_i(\mathbf{x}_j) \quad i = 1, \dots, m\\
&0 = \sum_{i=1}^n \lambda_i t_i\\
&\lambda_i = C - \alpha_i \leq C \quad i = 1, \dots, n
\end{align*}$$

Inserendo le relazioni sopra in $L(\mathbf{\bar{w}}, \boldsymbol{\xi}, \lambda, \alpha)$, si ottiene il problema duale:

$$\begin{align*}
&\max_{\lambda} \tilde{L}(\lambda) = \max_{\lambda} \left( \sum_{i=1}^n \lambda_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \lambda_i \lambda_j t_i t_j \kappa(\mathbf{x}_i, \mathbf{x}_j) \right)\\
&0 \leq \lambda_i \leq C \quad i = 1, \dots, n\\
&\sum_{i=1}^n \lambda_i t_i = 0
\end{align*}$$

Si osservi che l'unica differenza rispetto al caso linearmente separabile è data dai vincoli $0 \leq \lambda_i$ trasformati in $0 \leq \lambda_i \leq C$.

**Classificazione**

Dalla soluzione ottimale $\lambda^{\star}$ del problema duale, i coefficienti $\mathbf w^{\star},b^\star$ possono essere derivati come nel caso linearmente separabile

Un nuovo elemento $\mathbf x$ può essere classificato, ancora, tramite il suo segno
$$y(\mathbf x)=\sum\limits_{i=1}^{m}w_{i}^{\star}\phi_{i}(\mathbf x)+b^{\star}$$
o, in maniera equivalente
$$y(\mathbf x)=\sum\limits_{i\in S}\lambda_{j}^{\star}t_{j}\kappa(\mathbf x_{i},\mathbf x_{j})+b^{\star}$$
**Estensione**

L'approccio può essere esteso a :
- Più di 2 classi (classificazione multiclasse): risolvere il problema della classificazione binaria uno contro tutti per tutte le classi
- Risultati con valori reali (regressione vettoriale di supporto)

**Problemi computazionali**

Il tempo di addestramento dell'SVM standard è $O(n^3)$ (risoluzione QP)
- Può essere proibitivo per set di dati di grandi dimensioni

Sono state condotte numerose ricerche per velocizzare gli SVM
- Per velocizzare gli SVM vengono utilizzati molti risolutori QP approssimativi
- Discesa del gradiente più veloce e con possibilità di limitare il tempo di calcolo
# SVM and gradient descent

Richiamo della formalizzazione del problema nel caso generale

$$\begin{align*}
&\min_{\mathbf{w},b,\boldsymbol{\xi}} \frac{1}{2} \mathbf{w}^T \mathbf{w} + C \sum_{i=1}^{n} \xi_i\\
&t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) \geq 1 - \xi_i \quad i = 1, \dots, n\\
&\xi_i \geq 0 \quad i = 1, \dots, n
\end{align*}$$

Dati $\mathbf{w}, b$, la variabile slack $\xi_i$ viene minimizzata come

$$\xi_i = \begin{cases} 0 & t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) \geq 1 \\ 1 - t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b) & \text{altrimenti} \end{cases}$$

Il valore ottimale di $\xi_i$ corrisponde alla **hinge loss** dell'elemento corrispondente

$$L_H(\mathbf{w}, b, \mathbf{x}_i, t_i) = \max (0, 1 - t_i(\mathbf{w}^T \phi(\mathbf{x}_i) + b))$$

Possiamo quindi definire la funzione di costo da minimizzare come

$$\begin{align*}
&C(\mathbf{w}) = \frac{1}{2} \mathbf{w}^T \mathbf{w} + C \sum_{i=1}^n L_H(\mathbf{w}, b, \mathbf{x}_i, t_i)\\
&\propto \sum_{i=1}^n L_H(\mathbf{w}, b, \mathbf{x}_i, t_i) + \frac{1}{2C} \|\mathbf{w}\|^2
\end{align*}$$

Cioè, le SVM corrispondono alla hinge loss con regolarizzazione ridge

Poiché la perdita della cerniera non è differenziabile a $x = 1$, come discusso sopra, è possibile applicare la discesa del sottogradiente per trovare iterativamente la soluzione ottimale, con
$$\frac{\partial L_H}{\partial w_{i}}=w_{i}-\sum\limits_{\mathbf x_{k}\in L}t_{k}\phi_{i}(\mathbf x_{k})$$
dove $x_{k}\in L\iff t_{k}(\mathbf w^{T}\phi(x_{k})+b)\lt1$

L'iterazione risultate è:
$$w_{i}^{(r+1)}=w_{i}^{(r)}-\eta w_{i}^{(r)}+\eta\sum\limits_{\mathbf x_{k}\in L}t_{k}\phi_{i}(\mathbf x_{k})=(1-\eta)w_{i}^{(r)}+\alpha\sum\limits_{\mathbf x_{k}\in L}t_{k}\phi_{i}(\mathbf x_{k})$$
## SVM and SGD

Usando lo stochastic gradient descent, assumendo che ad ogni step venga aggiornato l'elemento $\mathbf x_{k}$, otteniamo che
$$\begin{align*}
&w_{i}^{(r+1)}=(1-\eta)w_{i}^{(r)}+\alpha\phi_{i}(\mathbf x_{k})\quad t_{k}(\mathbf w^{T}\phi(\mathbf x_{k})+b)\lt1\\
&w_i^{(r+1)}=w_{i}^{(r)}\quad\text{altrimenti}
\end{align*}$$

