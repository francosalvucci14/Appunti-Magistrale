# Metodo di Massima Verosimiglianza

Supponiamo di avere di fronte a noi due urne, una con $90$ palline bianche e $10$ nere, e l’altra con $10$ nere e $90$ bianche; identifichiamo le urne con la proporzione di palline bianche che contengono (denotata con $p$), in modo tale che la prima urna corrisponda a $p = .9$ e la seconda a $p = .1$

Viene estratta una singola pallina e non sappiamo da quale urna venga; osserviamo però che la pallina è bianca. 

Dovendo cercare di risalire all’urna di provenienza, sembra naturale scegliere quella che rende più probabile osservare quello che abbiamo effettivamente osservato, cioè l’urna che contiene la maggiore proporzione di palline bianche; in altre parole, dall’osservazione "è stata estratta una pallina bianca" sembra naturale far discendere lo stimatore $\hat{p} = 0.9$

Supponiamo ora che invece di una sola pallina ne siano estratte $5$, e che risultino essere $3$ bianche e $2$ nere; immaginiamo altresì che l’alternativa non sia solo tra due urne, ma tra un continuo di urne con tutte le possibili proporzioni di palline bianche tra $0$ ed $1$, identificate sempre con $p$. 

In questo caso, la probabilità di osservare $3$ bianche e $2$ nere è data da una legge binomiale:
$$Pr(3b,2n)=\binom{5}{3}p^{3}(1-p)^{2}$$
ed è facilmente verificabile che questa probabilità è massimizzata prendendo $\hat{p}=\frac{3}{5}$

Questo esempio molto semplice dovrebbe aiutare a capire l’idea che è alla base degli stimatori di massima verosimiglianza - si tratta di costruire la funzione di probabilità (o di densità, nel caso continuo) relativa ad un certo campione aletaorio, e vederla quindi non più come funzione del campione, ma come funzione (aleatoria) dei parametri, prendendo come date le osservazioni. 

In altre parole, si ha la seguente definizione:

>[!definition]- Funzione di Verosimiglianza
>Sia $X_{1},\dots,X_{n}$ un campione aleatorio con legge (=funzione di prob. o densità, a seconda del caso discreto o continuo) $f_{\theta},\theta\in\mathbb R^{p}$
>La **funzione di verosimiglianza** $L:\mathbb R^{p}\to\mathbb R$ è quindi definita come $$L(\theta;X_{1},\dots,X_{n}):=\prod_{i=1}^{n}f(X_{i};\theta)=f(X_{1},\dots,X_{n};\theta)$$

**oss**

Vediamo che la definizione di funzione di verosimiglianza in qualche modo "assomiglia" alla densità congiunta.
Quello che cambia è che la verosimiglianza è funzione del parametro prendendo i valori di $X_{1},\dots,X_{n}$ come dati, mentre la densità congiunta prende il parametro $\theta$ come dato ed è funzione dei possibili valori delle osservazioni $x_{1},\dots,x_{n}$

Definiamo poi il concetto di **stimatore di massima verosimiglianza (ML)**

>[!definition]- Stimatore di massima verosimiglianza (ML)
>Data $L$ la funzione di verosimiglianza appena definita, indichiamo con $\hat{\theta}$ lo **stimatore di massima verosimiglianza**, in questo modo: $$\hat{\theta}:=\underset{\theta}{\arg\max}\space L(\theta;X_{1},\dots,X_{n})$$
>Ovvero quel valore di $\theta$ che **massimizza** il risultato della funzione $L$

Vediamo ora una carrellata di esempi

**Esempio 1**

Prendiamo un campione aleatorio di variabili Bernoulliane $X_{1},\dots,X_n\sim Ber(\theta)$, dove $$X_{i}=\begin{cases}
1&\theta\space(p)\\0&1-\theta\space(1-p)
\end{cases}$$ 
La funzione di verosimiglianza sarà quindi:
$$L(\theta;X_1,\dots,X_{n})=\theta^{\sum\limits_{i=1}^{n}X_{i}}(1-\theta)^{n-\sum\limits_{i=1}^{n}X_{i}}$$
Sfruttiamo la $\log$-verosimiglianza, in modo tale da eliminare produttorie varie e rimanere con solamente le sommatorie

La $\log L$ sarà quindi $$\log L=\left(\sum\limits_{i=1}^{n}X_{i}\right)\log(\theta)+\left(n-\sum\limits_{i=1}^{n}X_{i}\right)\log(1-\theta)$$
Dobbiamo ora massimizzare la $\log L$, facendone la derivata e ponendola uguale a $0$; così facendo otteniamo che 
$$\begin{align*}
\frac{d\log L}{d\theta}&=\frac{\sum\limits_{i=1}^{n}X_{i}}{\theta}-\frac{n-\sum\limits_{i=1}^{n}X_{i}}{1-\theta}\\&=\frac{\sum\limits_{i=1}^{n}X_{i}-n\theta}{\theta(1-\theta)}
\end{align*}$$
Ponendo questo uguale a $0$ otteniamo che 
$$\hat{\theta}_{ML}=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}$$
Piccola osservazione, avremmo potuto scrivere la verosimiglianza come 
$$L(\theta;X_1,\dots,X_{n})=\dbinom{n}{\sum\limits_{i=1}^nX_{i}}\theta^{\sum\limits_{i=1}^{n}X_{i}}(1-\theta)^{n-\sum\limits_{i=1}^{n}X_{i}}$$
La cosa che cambia fra la prima equazione e la seconda è puramente "filosofica", ovvero scritta nel secondo modo noi stiamo prendendo una *qualsiasi sequenza di successi*, mentre nel primo caso stiamo prendendo *una sequenza esatta di successi*.
Entrambe le versioni sono equivalenti

**Esempio 2**

