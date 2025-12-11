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

In GDA, tutte le probabilità condizionate delle classi $p(\textbf{x}|C_{k})$ sono assunte essere Gaussiane.
Questo implica che le distribuzioni a posteriori corrispondenti $p(C_{k}|\textbf{x})$ possono essere facilmente derivabili

**ipotesi** : Tutte le distribuzioni $p(\textbf{x}|C_{k})$ hanno stessa matrice di covarianza $\Sigma$, di dimensione $d\times d$
Allora:
$$p(\textbf{x}|C_{k})=\frac{1}{(2\pi)^{\frac{d}{2}}|\Sigma|^{\frac{1}{2}}}e^{- \frac{1}{2}[(\textbf{x}-\mu_{k})^{T}\Sigma^{-1}(\textbf{x}-\mu_{k})]}$$
Se $K=2$, otteniamo che 
$$p(C_1|\textbf{x})=\sigma(a(\textbf{x}))$$
dove 
$$\begin{align*}
a(\textbf{x})&=\log\left(\frac{p(\textbf{x}|C_{1})p(C_{1})}{p(\textbf{x}|C_{2})p(C_{2})}\right)\\
&= \frac{1}{2}\left(\mu_{2}^{T}\Sigma^{-1}\mu_{2}-\textbf{x}^{T}\Sigma^{-1}\mu_{2}-\mu_{2}^{T}\Sigma^{-1}\textbf{x}\right)-\frac{1}{2}\left(\mu_{1}^{T}\Sigma^{-1}\mu_{1}-\textbf{x}^{T}\Sigma^{-1}\mu_{1}-\mu_{1}^{T}\Sigma^{-1}\textbf{x}\right)\\
&+\log\left(\frac{p(C_{1})}{p(C_{2})}\right)
\end{align*}$$
Si osservi che i risultati di tutti i prodotti che coinvolgono $\Sigma^{-1}$ sono scalari, quindi, in particolare otteniamo che:
$$
\begin{align*}
&\textbf{x}^{T}\Sigma^{-1}\mu_1=\mu_{1}^{T}\Sigma^{-1}\textbf{x}\\
&\textbf{x}^{T}\Sigma^{-1}\mu_{2}=\mu_{2}^{T}\Sigma^{-1}\textbf{x}\\
\end{align*}
$$
E quindi, possiamo riscrivere $a(\textbf{x})$ come:
$$a(\textbf{x})=\frac{1}{2}\left(\mu_{2}^{T}\Sigma^{-1}\mu_{2}-\mu_{1}^{T}\Sigma^{-1}\mu_{1}\right)+\phi(\textbf{x})\left(\mu_{1}^{T}\Sigma^{-1}-\mu_{2}^{T}\Sigma^{-1}\right)+\log\left(\frac{p(C_{1})}{p(C_{2})}\right)=\textbf{w}^{T}\textbf{x}+b$$
con:
- $\textbf{w}=\Sigma^{-1}(\mu_{1}-\mu_{2})$
- $b=\frac{1}{2}\left(\mu_{2}^{T}\Sigma^{-1}\mu_{2}-\mu_{1}^{T}\Sigma^{-1}\mu_{1}\right)+\log\left(\frac{p(C_{1})}{p(C_{2})}\right)$

Otteniamo quindi che $p(C_{1}|\textbf{x})=\sigma(\textbf{w}^{T}\textbf{x}+b)$ è calcolata applicando una funzione non-lineare a una combinazione lineare delle feature (**modello lineare generalizzato**)
### Funzioni discriminative

La funzione discrimante può essere ottenuta dalla condizione $p(C_{1}|\textbf{x})=p(C_{2}|\textbf{x})$, ovvero da $\sigma(a(\textbf{x}))=\sigma(-a(\textbf{x}))$ [^1]

Questo è equivalente a dire che $a(\textbf{x})=-a(\textbf{x})$ e $a(\textbf{x})=0$
Come conseguenza, si ottiene che:
$$\textbf{w}^{T}\textbf{x}+b=0$$
oppure che 
$$\Sigma^{-1}(\mu_{1}-\mu_{2})\textbf{x}+\frac{1}{2}\left(\mu_{2}^{T}\Sigma^{-1}\mu_{2}-\mu_{1}^{T}\Sigma^{-1}\mu_{1}\right)+\log\left(\frac{p(C_{1})}{p(C_{2})}\right)=0$$
Vediamo ora un caso semplice, ovvero quando $\Sigma=\lambda\textbf{I}$ (ovvero, $\sigma_{ii}=\lambda,\forall i=1,\dots,d$)
In questo caso, la funzione discriminante risulta essere:
$$2(\mu_{2}-\mu_{1})\textbf{x}+||\mu_{1}||^{2}-||\mu_{2}||^{2}+2\lambda\log\left(\frac{p(C_{1})}{p(C_{2})}\right)=0$$
### Classi Multiple

In questo caso ci riferiamo alla funzione softmax
$$p(C_{k}|\textbf{x})=s(a_k(\textbf{x}))$$
dove $a_{k}(\textbf{x})=\log(p(\textbf{x}|C_{k})p(C_{k}))$ 

Prendendo le considerazioni fatte in precedenza, è facile vedere che:
$$a_{k}(\textbf{x})=\frac{1}{2}(\mu_{k}^{T}\Sigma^{-1}\textbf{x}-\mu_{k}^{T}\Sigma^{-1}\mu_{k})+\log(p(C_{k}))-\frac{d}{2}\log(2\pi)-\frac{1}{2}\log|\Sigma|=\textbf{w}_{k}^{T}\textbf{x}+b_{k}$$
Nuovamente, abbiamo che $p(C_{k}|\textbf{x})=s(\textbf{w}_{k}^{T}\textbf{x}+b_{k})$ viene calcolata applicando una funzione non lineare ad una combinazione lineare di feature (anche qui **modello lineare generalizzato**)

I *confini decisionali* corrispondono al caso in cui vi siano due classi $C_j , C_k$ tali che le corrispondenti probabilità a posteriori siano uguali e maggiori della probabilità di qualsiasi altra classe. 

Ovvero
$$p(C_{k}|\textbf{x})=p(C_{j}|\textbf{x})\quad p(C_{i}|\textbf{x})\lt p(C_{k}|\textbf{x})\space i\neq j,k$$
quindi
$$e^{a_{k}(\textbf{x})}=e^{a_{j}(\textbf{x})}\quad e^{a_{i}(\textbf{x})}\lt e^{a_{k}(\textbf{x})}\space i\neq j,k$$
ovvero
$$a_{k}(\textbf{x})=a_{j}(\textbf{x})\quad a_i(\textbf{x})\lt a_{k}(\textbf{x})\space i\neq j,k$$
Come mostrato, questo implica che i confini sonoo **lineari**
### Matrici di covarianza generali - caso binario

Mettiamoci nel caso in cui le distribuzioni condizionali delle classi $p(C_{k}|\textbf{x})$ siano Gaussiane con diverse matrici di covarianza
Per semplificare i conti mettiamo anche nel caso binario, il caso con $K\gt2$ è del tutto analogo

$$\begin{align*}
a(\textbf{x})&=\log\left(\frac{p(\textbf{x}|C_{1})p(C_{1})}{p(\textbf{x}|C_{2})p(C_{2})}\right)\\
&= \frac{1}{2}\left((\textbf{x}-\mu_{2})^{T}\Sigma^{-1}_2(\textbf{x}-\mu_{2})-(\textbf{x}-\mu_{1})^{T}\Sigma^{-1}_{1}(\textbf{x}-\mu_{1})\right)\\
&+\frac{1}{2}\log\frac{|\Sigma_{2}|}{|\Sigma_{1}|}+\log\left(\frac{p(C_{1})}{p(C_{2})}\right)
\end{align*}$$

Applicando le stesse considerazioni fatte in precedenza, otteniamo che i confini decisionali risultano essere:
$$\left((\textbf{x}-\mu_{2})^{T}\Sigma^{-1}_2(\textbf{x}-\mu_{2})-(\textbf{x}-\mu_{1})^{T}\Sigma^{-1}_{1}(\textbf{x}-\mu_{1})\right)\\
+\log\frac{|\Sigma_{2}|}{|\Sigma_{1}|}+2\log\left(\frac{p(C_{1})}{p(C_{2})}\right)=0$$

Le classi sono quindi separate da al più una superficie quadratica
Può essere dimostrato che le superfici decisionali sono al più quadratiche

**esempio**

A sx: $3$ classi, modellate da Gaussiane con matrici di covarianza differenti
A dx: distribuzione a posteriori delle classi, con superfici decisionali

![center|500](img/Pasted%20image%2020251203143443.png)

### GDA e ML

Le distribuzioni condizionali delle classi $p(\textbf{x}|C_{k})$ possono essere derivate partendo dal training set usando la stima di massima verosimiglianza

Per semplicità, assumiamo $K=2$ e stessa matrice $\Sigma$ per le classi
Dobbiamo quindi stimare $\mu_{1},\mu_{2},\Sigma,\pi=p(C_{1})(p(C_{2})=1-\pi)$

Prendiamo ora un training set $\mathcal T$: esso include $n$ elementi $(\textbf{x}_{i},t_{i})$ con 
$$t_{i}=\begin{cases}0&\textbf{x}_{i}\in C_{2} \\
1&\textbf{x}_{i}\in C_{1}\end{cases}$$
Se $\textbf{x}\in C_{1}$ allora $$p(\textbf{x},C_{1})=p(\textbf{x}|C_{1})p(C_{1})=\pi\cdot\mathcal N(\textbf{x}|\mu_{1},\Sigma)$$
In maniera del tutto analoga, se $\textbf{x}\in C_{2}$ allora $$p(\textbf{x},C_{2})=p(\textbf{x}|C_{2})p(C_{2})=(1-\pi)\cdot\mathcal N(\textbf{x}|\mu_{2},\Sigma)$$

La verosimiglianza del training set $\mathcal T$ è:
$$L(\pi,\mu_{1},\mu_{2},\Sigma|\mathcal T)=\prod_{i=1}^{n}(\pi\cdot\mathcal N(\textbf{x}_{i}|\mu_{1},\Sigma))^{t_{i}}(1-\pi)\cdot\mathcal N(\textbf{x}_{i}|\mu_{2},\Sigma)^{1-t_{i}}$$

La log-verosimiglianza corrisponderte è:
$$\begin{align*}
l(\pi,\mu_{1},\mu_{2},\Sigma|\mathcal T)&=\sum\limits_{i=1}^n(t_{i}\log\pi+t_i\log(\mathcal N(\textbf{x}|\mu_{1},\Sigma)))\\
&+\sum\limits_{i=1}^n((1-t_{i})\log(1-\pi)+(1-t_i)\log(\mathcal N(\textbf{x}|\mu_{2},\Sigma)))
\end{align*}$$
Derivando rispetto al parametro $\pi$ otteniamo che
$$\frac{\partial l}{\partial\pi}=\frac{\partial}{\partial\pi}\sum\limits_{i=1}^{n}(t_{i}\log\pi+(1-t_{i})\log(1-\pi))=\sum\limits_{i=1}^{n}\left(\frac{t_{i}}{\pi}-\frac{(1-t_{i})}{1-\pi}\right)=\frac{n_{1}}{\pi}-\frac{n_{2}}{1-\pi}$$
che è uguale a $0$ quando $$\pi=\frac{n_{1}}{n}$$
Il massimo rispetto ai parametri $\mu_1(\mu_{2})$ è ottenuto calcolando il gradiente
$$\nabla_{\mu_{1}}l=\nabla_{\mu_{1}}\sum\limits_{i=1}^{n}t_{i}\log(\mathcal N(\textbf{x}_{1}|\mu_{1},\Sigma))=\Sigma^{-1}\sum\limits_{i=1}^{n}t_{i}(\textbf{x}_{i}-\mu_{1})$$
di conseguenza, otteniamo $\nabla_{\mu_{1}}l=\textbf{0}$ quando 
$$\sum\limits_{i=1}^{n}t_{i}\textbf{x}_i=\sum\limits_{i=1}^{n}t_{i}\mu_{1}$$
quindi, otteniamo che 
$$\begin{align*}
&\mu_{1}=\frac{1}{n_{1}}\sum\limits_{\textbf{x}_{i}\in C_{1}}\textbf{x}_{i}\\
&\mu_{2}=\frac{1}{n_{2}}\sum\limits_{\textbf{x}_{i}\in C_{2}}\textbf{x}_{i}
\end{align*}$$
Massimizzare la log-verosimiglianza rispetto al parametro $\Sigma$ ci fa ottenere:
$$\Sigma=\frac{n_1}{n}\textbf{S}_1+\frac{n_2}{n}\textbf{S}_2$$
Dove:
- $\textbf{S}_1=\frac{1}{n_1}\sum\limits_{\textbf{x}_{i}\in C_{1}}(\textbf{x}_i-\mu_{1})(\textbf{x}_i-\mu_{1})^{T}$
- $\textbf{S}_2=\frac{1}{n_2}\sum\limits_{\textbf{x}_{i}\in C_{2}}(\textbf{x}_i-\mu_{2})(\textbf{x}_i-\mu_{2})^{T}$


[^1]: notiamo che la condizione di uguaglianza delle due probabilità risulta essere la **condizione di massima incertezza del modello**
