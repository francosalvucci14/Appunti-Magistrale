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
\theta^{(i)}_{j}:&=\theta^{(i-1)}_{j}-\eta\nabla\overline{\mathcal R}_\mathcal T(\theta)|_{\theta^{(i-1)}}\\&=\theta^{(i-1)}_{j}-\frac{\eta}{|\mathcal T|}\sum\limits_{(x,t)\in\mathcal T}\nabla L(h_{\theta}(\overline{x}),t)|_{\theta^{(i-1)}}
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

![[Pasted image 20251018093538.png|center|300]]

Una funzione $f (x)$ è convessa se e solo se l'insieme dei punti che giacciono sopra la funzione è convesso, cioè, per ogni $x_{1},x_{2}\in S$ e $\lambda\in(0,1)$ vale che:
$$f(\lambda x_1+(1-\lambda)x_{2})\leq\lambda f(x_{1})+(1-\lambda)f(x_{2})$$
è strettamente convessa se vale che 
$$f(\lambda x_1+(1-\lambda)x_{2})\lt\lambda f(x_{1})+(1-\lambda)f(x_{2})$$
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


