# Cap 2 : Variabili Aleatorie ed Aspettazione

>[!definition]- Def 2.1 Variabile Aleatoria
>Una **variabile aleatoria** (v.a.) è una funzione $$X:\Omega\to\mathbb R$$
>Una v.a. si dice **discreta** se assume un numero finito (o numerabile) di valori

**oss** 

Se $\Omega$ è finito o numerabile si ha che : $$\forall a\in\mathbb R\quad\{X=a\}=\{\omega\in\Omega|X(\omega)=a\}$$
E quindi : 
$$\mathbb P(X=a)=\sum\limits_{\substack{\omega\in\Omega\\ X(\omega)=a}}\mathbb P(\{\omega\})$$
*esempio*

Lancio due dadi equi 
$\Omega=\{(1,1),(1,2),\dots,(6,6)\}$

Sia $X$ la somma dei due dadi. Allora : 
$$\mathbb P(X=4)=\mathbb P(\{(1,3)\})+\mathbb P(\{(2,2)\})+\mathbb P(\{(1,3)\})=\frac{3}{36}=\frac{1}{12}$$


>[!definition]- Def 2.2 V.A. indipendenti
>Due v.a. discrete $X,Y$ si dicono **indipendenti** $\iff$ $$\mathbb P(\{X=x\}\cap\{Y=y\})=\mathbb P(X=x)\mathbb P(Y=y)$$
>Questo deve valere $\forall x,y\in\mathbb R$
>Analogamente, $X_1,\dots,X_n$ sono **mutualmente indipendenti** $\iff\forall$ sottoinsieme $I\subseteq\{1,\dots,k\}$ e $\forall x_i\in\mathbb R$ si ha $$\mathbb P\left(\bigcap_{i\in I}\{X_i=x_i\}\right)=\prod_{i\in I}\mathbb P(X_i=x_i)$$

>[!definition]- Valore Atteso
>Una v.a discreta $X$ ha **valore atteso** finito se $$\sum\limits_{\underbrace{x_k}_{\text{somma su tutti i valori possibili che X può assumere}}}|x_k|\mathbb P(X=x_k)\lt\infty$$

In tal caso il valore atteso (anche detto *media* oppure *speranza matematica*) di $X$ è : $$\mathbb E[X]=\sum\limits_{x_k}x_k\mathbb P(X=x_k)$$
**oss importante** 

È possibile che $X$ sia finita ma $\mathbb E[X]=\infty$

>[!teorem]- Teorema 2.1 e Lemma 2.2 Linearità dell'aspettazione
>Siano $X_1,\dots,X_n$ v.a con aspettazione finita
>Siano $c_1,\dots,c_n\in\mathbb R$ costanti
>Allora : $$\mathbb E[\sum\limits_{i=1}^{n}c_iX_i]=\sum\limits_{i=1}^{n}c_i\mathbb E[X_i]$$

