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
# Loss Function

In generale, la funzione di loss $L:\mathcal Y\times\mathcal Y\to\mathbb R$ misura il **costo** di riferirsi a $y$ invece che al target $t$ per ogni azione successiva, dove $y$ e $t$ sono elementi dello spazio target.

Nel supervised learning, questo offre una misura della qualità della predizione ritornata dalla funzione di predizione $h$:
$$\mathcal R(\overline{x},y)=L(h(\overline{x}),y)$$
È una componente fondamentale del rischio empirico, che è il valore medio della funzione loss applicata a tutte le coppie valore-target presenti nel training set $\mathcal T$
$$\overline{\mathcal R}_{\mathcal T}(h)=\frac{1}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}L(h(x),t)$$
Questo offre una misura della qualità della predizione fatta da $h$, almeno per quanto riguarda i dati disponibili (ovvero il training set)

Durante la fase di training, il rischio empirico viene minimizzato rispetto alla funzione di predizione $h$, in particolare per quanto riguarda l'insieme di parametri $\theta$ che definiscono la funzione parametrica $h = h_{\theta}$

Ciò corrisponde alla minimizzazione della **loss complessiva**, indicata con $\mathcal L$:
$$\mathcal L(\theta,\mathcal T)=\sum\limits_{i=1}^{n}L_{i}(\theta)$$
che è la somma delle funzioni di loss $L_{i}=L(\theta,x_{i},t_{i})$ per ogni data point $(x_{i},t_{i})$
## Approcci alla minimizzazione della funzione loss

Come possiamo affrontare il problema della minimizzazione della funzione di loss? 
Idealmente, il nostro obiettivo è trovare un **minimo globale** della funzione di loss, che rappresenterebbe il miglior insieme possibile di parametri per il modello.

Un approccio comune si basa sul calcolo, in particolare sull'impostazione a zero di tutte le derivate della funzione di loss rispetto ai parametri:
$$\nabla\mathcal L(\theta,\mathcal T)=0$$
dove $\nabla$ è l'operatore del ***gradiente*** che, data una funzione multivariata $f(x_{1},\dots,x_{m})$ ritorna il vettore delle derivate parziali $$\nabla f=\begin{bmatrix}\frac{\partial f}{\partial x_{1}}\\\vdots\\\frac{\partial f}{\partial x_{m}}\end{bmatrix}$$
osservarviamo che il gradiente in un dato punto $x_1, \dots , x_m$ nello spazio del dominio di $f$ è un **vettore** che punta nella direzione di salita più ripida da quel punto.

Impostare il gradiente a $0$ significa risolvere il sistema di equazioni:
$$\frac{\partial}{\partial\theta_{i}}\mathcal L(\theta,\mathcal T)=0\quad\forall i$$
dove ogni derivata parziale è impostata a zero, identificando così i potenziali punti in cui la perdita potrebbe essere minima.

Tuttavia, questo metodo presenta diverse difficoltà: innanzitutto, questo sistema di equazioni ha spesso più soluzioni, tra cui minimi locali, massimi e punti di sella, rendendo difficile identificare un minimo globale.

Inoltre, in molti casi, ***risolvere queste equazioni analiticamente è estremamente difficile o addirittura impossibile***.
## Discesa del gradiente

Un minimo locale della funzione di rischio empirico $\overline{\mathcal R}_{\mathcal T}(\theta)$ può essere calcolato numericamente mediante metodi iterativi, come la **discesa del gradiente**. 

Il processo inizia tipicamente inizializzando i parametri in un punto di partenza, $\theta^{(0)}=\left(\theta^{(0)}_{0},\theta^{(0)}_{1},\dots,\theta^{(0)}_{d}\right)$, con un valore di errore iniziale dato da:
$$\overline{\mathcal R}_{\mathcal T}\left(\theta^{(0)}\right)$$
La procedura iterativa funziona quindi modificando i valori attuali dei parametri $\theta^{(i-1)}$ nella direzione della ***discesa più ripida*** della funzione di rischio empirico $\overline{\mathcal R}_{\mathcal T}(\theta)$. 

Nello specifico, ciò significa muoversi nella direzione opposta al gradiente relativo al rischio empirico valutato in $\theta^{(i−1)}$.

Ad ogni iterazione $i$, il parametro $\theta^{(i−1)}_j$ viene aggiornato secondo la seguente regola:
$$\begin{align*}
\theta^{(i)}_{j}:&=\theta^{(i-1)}_{j}-\eta\frac{\partial}{\partial\theta_{j}}\overline{\mathcal R}_\mathcal T(\theta)|_{\theta^{(i-1)}}\\&=\theta^{(i-1)}_{j}-\frac{\eta}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}\frac{\partial}{\partial\theta_{j}}L(h_{\theta}(\overline{x}),t)|_{\theta^{(i-1)}}
\end{align*}$$
dove $\eta$ rappresenta il ***rate di apprendimento***, che controlla la dimensione del passo ad ogni aggiornamento (iterazione)

In forma matriciale, questo può essere riscritto come:
$$\begin{align*}
\theta^{(i)}:&=\theta^{(i-1)}-\eta\nabla\overline{\mathcal R}_\mathcal T(\theta)|_{\theta^{(i-1)}}\\&=\theta^{(i-1)}-\frac{\eta}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}\nabla L(h_{\theta}(\overline{x}),t)|_{\theta^{(i-1)}}
\end{align*}$$
Mentre questo metodo ci permette di approssimare a un minimo locale, il risultato dipende *pesantemente* dai parametri iniziali scelti.

Alcuni problemi chiave da considerare sono:
- Noi siamo interessati a trovare un minimo globale, ma questa tecnica (discesa del gradiente) può rimanere bloccata al minimo locale, come facciamo?
- Come gestiamo i punti di sella, che non sono ne massimi ne minimi?
- Quanto velocemente questo metodo iterativo converge? e quali fattori influiscono la sua velocità di convergenza?

Queste sfide rendono il processo di minimizzazione complesso, ma questa tecnica rimane una delle più usate nella pratica per l'ottimizzazione dei parametri
### Appendice sulla convessità della funzione loss

Un insieme di punti $S\subset\mathbb R^{d}$ si dice **convesso** se e solo se per ogni $x_{1},x_{2}\in S$ e $\lambda\in(0,1)$ vale che $$\lambda x_{1}+(1-\lambda)x_{2}\in S$$
cioè, se tutti i punti del segmento che connette $x_{1}$ e $x_2$ appartengono a $S$

![center|300](img/Pasted%20image%2020251018093538.png)

Una funzione $f (x)$ è convessa se e solo se l'insieme dei punti che giacciono sopra la funzione è convesso, cioè, per ogni $x_{1},x_{2}\in S$ e $\lambda\in(0,1)$ vale che:
$$f(\lambda x_1+(1-\lambda)x_{2})\leq\lambda f(x_{1})+(1-\lambda)f(x_{2})$$
è strettamente convessa se vale che 
$$f(\lambda x_1+(1-\lambda)x_{2})\lt\lambda f(x_{1})+(1-\lambda)f(x_{2})$$

![center|400](img/Pasted%20image%2020251018101118.png)

Supporre che la funzione di loss complessiva $\mathcal L(\theta; \mathcal T )$ sia convessa è una semplificazione rilevante: se $f (x)$ è una funzione convessa, allora qualsiasi minimo locale di $f$ è anche un minimo globale.
Inoltre, se $f$ è una funzione strettamente convessa, esiste un solo minimo locale per $f$ (ed è globale).

Cioè, risolvere
$$\nabla\mathcal L(\theta,\mathcal T)=0$$
permette di ottenere esattamente il minimo globale

Un caso semplice ma rilevante è quello in cui $f (x)$ è quadratica. 

Questo è il caso di una serie di modelli ML semplici, ma purtroppo non vale per modelli più complessi come le reti neurali.

Ricordiamo che:
1) la somma di funzioni (strettamente) convesse è (strettamente) convessa
2) il prodotto di una funzione (strettamente) convessa e una costante è (strettamente) convesso

Dato che $$\overline{\mathcal R}_{\mathcal T}(h)=\frac{1}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}L(h(x),t)\propto\sum\limits_{(x,t)\in\mathcal T}L(\theta,x,t)$$
questo implica che:
1. se $L(\theta,x,t)$ è (strettamente) convessa allora il costo complessivo è anch'esso (strettamente) convesso
2. se $L(\theta,x,t)$ è convessa allora ogni minimo locale del rischio empirico è anche minimo globale
3. se $L(\theta,x,t)$ è strettamente convessa allora esiste un solo minimo relativo al rischio empirico

## Alcune Loss famose

### Loss per regressione

Consideriamo il caso della **regressione**
- sia $y$ che $h(\overline{x})$ sono valori reali
- la loss è legata a qualche tipo di misura di distanza fra punti
#### Quadratic Loss

La funzione loss più comune per la regressione è la **quadratic loss**
$$L(y,t)=(y-t)^{2}$$
![center|500](img/Pasted%20image%2020251110103356.png)

Applicare la loss quadratica ci fa ottenere il seguente rischio empirico
$$\overline{\mathcal R}_\mathcal T=\frac{1}{|\mathcal T|}\sum\limits_{(\overline{x},t)\in\mathcal T}(h(\overline{x})-t)^{2}$$
Nel caso comune della regressione lineare, la previsione viene eseguita mediante una funzione lineare $h(\overline{x})=\overline{w}^{T}\overline{x} + b$: ciò si traduce in una loss complessiva da minimizzare
$$\mathcal L(\overline{w},b;\mathcal T)=\sum\limits_{(\overline{x},t)\in\mathcal T}(\overline{w}^{T}\overline{x}+b-t)^{2}$$
Dato che la funzione quadratica è strettamenre convessa, la loss generale avrà un solo minimo locale (che sarà anche il globale)

Il gradiente è lineare, infatti:
$$\frac{\partial}{\partial w_{i}}\mathcal L(\overline{w},b;\mathcal T)=\sum\limits_{(\overline{x},t)\in\mathcal T}(\overline{w}^{T}\overline{x}+b-t)w_{i}\quad\frac{\partial}{\partial b}\mathcal L(\overline{w},b;\mathcal T)=\sum\limits_{(\overline{x},t)\in\mathcal T}(\overline{w}^{T}\overline{x}+b-t)$$
#### Absolute Loss

La perdita quadratica è facile da gestire matematicamente, ma non è robusta nei confronti dei valori anomali, ovvero presta troppa attenzione ai valori anomali

Una funzione loss differente per la regressione è la **absolute loss**
$$L(t,y)=|t-y|$$
![center|500](img/Pasted%20image%2020251110104228.png)

Il gradiente ora è costante a tratti
#### Huber Loss

Un'altra loss differente per la regressione è la **Huber Loss**, che risulta quadratica per valori piccoli e lineare dopo una certa soglia data, ovvero:
$$L(t,y)=\begin{cases} \frac{1}{2}(t-y)^{2}&|t-y|\leq\delta\\\delta(|t-y|)-\frac{\delta}{2}&|t-y|\gt\delta\end{cases}$$
![center|500](img/Pasted%20image%2020251110104449.png)
### Loss per classificazione

Per quanto riguarda le loss per classificazione abbimao due approcci, che dipendono da cosa ci aspettiamo dalla predizione:
1. se la predizione ritorna una classe specifica (funzione di predizione)
2. se la predizione ritorna una distribuzione di probabilità su un'insieme di classi (distribuzione delle predizioni)

Questo implica diverse definizioni di errore:
1. primo caso: coincidenza tra classi previste e classi reali
2. secondo caso: differenza cumulativa tra probabilità prevista e 0/1 per tutte le classi

Consideriamo il caso binario, con due classi identificate dai valori target $-1$ e $1$.

Supponiamo che venga restituito un valore reale come previsione.
#### 0/1 Loss

La loss più "naturale" nella classificazione è la $0/1$ **loss**
$$L(t,y)=\begin{cases}1&sgn(t)\neq y\\0&sgn(t)=y\end{cases}$$
dove $$sgn(x)=\begin{cases}1&x\gt0\\0&\text{altrimenti}\end{cases}$$
questo può essere riscritto come $\mathbb 1[ty\lt0]$ 

Usare la funzione $0/1$ è problematico, dato che:
1. non è convessa
2. non è regolare (derivata prima indefinita in alcuni punti o non continua)
3. il suo gradiente è 0 quasi ovunque (indefinito a 0): non è possibile applicare la discesa del gradiente (vedi dopo)

![center|500](img/Pasted%20image%2020251110105338.png)

se assumiamo una funzione di predizione lineare otteniamo il seguente rischio empirico
$$\overline{\mathcal R}_{\mathcal T}(h)=\frac{1}{|\mathcal T|}\sum\limits_{(\overline{x},t)\in\mathcal T}\mathbb 1[(\overline{w}^{T}\overline{x}+b)y\lt0]$$
il problema è trovare i valori di $\overline{w},b$ che minimizzano il numero generale di errori: questo è un problema NP-Hard

(tranne la **cross-entropy**, vedi [qui](Code-labs/lab2/Gradient%20Descent.md#La%20funzione%20di%20costo%20cross-entropy))
## Tecniche di gradient descent

Il gradient descent esegue la minimizzazione di una funzione $J(\theta)$ attraverso aggiornamenti iterativi del valore corrente di $\theta$, partendo da un valore iniziale $\theta^{(0)}$, nella direzione opposta a quella specificata dal valore corrente del gradiente, ovvero $\nabla J|_{\theta^{(k)}}$
$$\theta^{(k+1)}=\theta^{(k)}-\eta\nabla J|_{\theta^{(k)}}$$
cioè, per ogni parametro $\theta_{i}$ otteniamo
$$\theta_{i}^{(k+1)}=\theta_i^{(k)}-\eta\frac{\partial J(\theta)}{\partial\theta_{i}}\big|_{\theta^{(k)}}$$
$\eta$ è il parametro di **tuning**, che controlla il numero di aggiornamenti ad ogni step

Esistono sostanzialmente tre tecniche principali per il gradient descent, che sono:
- **Batch gradient descent** [vedi qui](Code-labs/lab2/Gradient%20Descent.md#Batch%20Gradient%20Descent%20(BGD))
- **Stochastic gradient descent** [vedi qui](Code-labs/lab2/Gradient%20Descent.md#Stochastic%20Gradient%20Descent%20(SGD))
- **Mini-batch gradient descent** [vedi qui](Code-labs/lab2/Gradient%20Descent.md#Mini-Batch%20Gradient%20Descent)

#### Ottimizzatori avanzati

Abbiamo visto come il *gradient descent* — nelle sue varianti *batch*, *stochastic* e *mini-batch* — permetta di minimizzare il rischio empirico aggiornando iterativamente i parametri del modello nella direzione opposta al gradiente della funzione di costo.

Tuttavia, questi metodi di base presentano alcune **limitazioni pratiche**:
- convergenza lenta in presenza di superfici di costo irregolari o “vallate strette”;
- forte dipendenza dalla scelta del **learning rate**, ovvero $\eta$;
- difficoltà nel gestire funzioni di costo **non convesse**, tipiche delle reti neurali.

Di seguito verranno quindi reportate alcune tecniche di ottimizzazione avanzate, che permetto di superare queste limitazioni

Come sopra, non andrò nel dettaglio perchè il tutto è reperibile qui -> [Tecniche di ottimizzazione del Gradient Descent](Code-labs/lab3/Tecniche%20di%20ottimizzazione%20del%20Gradient%20Descent.md)

Le varie tecniche sono:

1. **Metodo del Momento**  
   Introduce un termine di “inerzia” che tiene conto dei gradienti precedenti, riducendo le oscillazioni e accelerando la discesa.
2. **Accelerazione di Nesterov**  
   Variante del momento che anticipa la direzione di discesa, migliorando la stabilità e la convergenza.
3. **Adagrad**  
   Adatta il learning rate in modo automatico per ogni parametro, in base alla storia dei gradienti.
4. **RMSProp**  
   Smorza l’effetto di Adagrad mantenendo un tasso di apprendimento più stabile nel tempo.
5. **Adadelta**  
   Elimina la necessità di un learning rate fisso, rendendo l’adattamento completamente dinamico.
6. **Adam**  
   Combina momentum e adattività: è oggi l’ottimizzatore più utilizzato nel Deep Learning.
7. **Metodi del Secondo Ordine (Newton-Raphson)**  
   Utilizzano anche la matrice Hessiana per stimare curvature e direzioni di discesa più precise.