# Indirizzi Bitcoin

Possiamo descrivere una **curva ellittica** come l'insieme dei punti $(x,y)$, a cordinate in un opportuno **campo**, che soddisfano l'equazione $$y^2=x^3+ax+b$$
dove $a,b$ sono parametri che definiscono la curva, con l'aggiunta di un punto che chiamiamo **punto all'infinito** $\{\infty\}$

per le applicazioni in crittografia non si considera il campo dei numeri reali $\mathbb R$, ma si considerano i ***campi finiti*** $\mathbb F_p$, dove $p$ è numero primo.

Di conseguenza l'insieme $\mathbb F_p=\{0,1,\dots,p-1\}$ con le usuali operazioni di somma e prodotto, tutte modulo $p$.

La curva ellittica che viene usata da Bitcoin si chiama **secp256k1** ed è definita dai parametri $$a=0,b=7,p=2^{256}-2^{32}-2^{9}-2^{8}-2^{7}-2^{6}-2^{4}-1$$
Su una curva ellttica $$\mathcal C=\{(x,y)\in\mathbb F_p^2:y^2=x^3+ax+b\}\cup\{\infty\}$$
si può definire un'operazione, che chiamiamo *somma*, tale che $$+:\mathbb F_p\times\mathbb F_p\to\mathbb F_p$$ovvero un'operazione che associa a due punti sulla curva $P,Q\in\mathcal C$ un terzo punto, chiamato $P+Q\in\mathcal C$, in modo tale che $(\mathcal C,+)$ diventi un **gruppo**

>[!info]- Remark sul significato di gruppo
>Un insieme $G$ è detto **gruppo** se su di lui è definita un'operazione matematica (es. la somma) tale che : 
>1. $\exists$ elemento neutro $e\in G:\forall x\in G,e+x=x+e=x$
>2. $\forall x\in G\exists y\in G:x+y=y+x=e$
>3. L'operazione è associativa, ovvero $\forall x,y\in G\to(x+y)+z=x+(y+z)$
>
>Esempio : $(\mathbb Z,+)$ è gruppo, ma $(\mathbb Z,\cdot)$ non è gruppo

È facile vede che, siccome $(\mathcal C,+)$ è un gruppo, c'è un algoritmo polinomiale per il seguente problema computazionale

INPUT: Un punto sulla curva $G\in\mathcal C$ e un intero $k\in\mathbb N$
OUTPUT : Il punto $P\in\mathcal C$ tale che $P=kG$

Dove con $kP$ intendiamo $\underbrace{P+P+\dots+P}_{\text{k volte}}$
D'altra parte, nessuno conosce un algoritmo polinomalie per il problema computazionale inverso (ovvero il problema del [Logaritmo Discreto](https://en.wikipedia.org/wiki/Discrete_logarithm))

INPUT : Due punti sulla curva $G,P\in\mathcal C$
OUTPUT : Un intero $k\in\mathbb N$ tale che $P=kG$, oppure **None** se un tale intero non esiste
- Questo problema è chiamato anche problema **ECDH** (Ellittic Curve Diffie-Hellman)

Perciò dato un *punto base* $G\in\mathcal C$, detto anche **generatore del gruppo** $\mathcal C$, si può definire una coppia di chiavi $(sk,pk)$ dove la chiave segreta $sk$ è un intero positivo minore di $p$, e la chiave pubblica $pk$ è il punto sulla curva $sk\cdot G$

