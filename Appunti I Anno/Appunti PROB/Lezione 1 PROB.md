# Cap 1 : Eventi e Probabilità

>[!definition]- Spazio di Probabilità
>Tripla $(\Omega,\mathbb F,\mathbb P)$ dove : 
>- $\Omega$ : Spazio degli eventi
>- Famiglia $\mathbb F$ di sottoinsiemi di $\Omega$ (detti **eventi**)
>- $\mathbb P$ : misura di probabilità

**oss** : in questo corso $\Omega$ sarà sempre discreto e $\mathbb F$ l'insieme delle parti di $\Omega$

>[!definition]- Misura di probabilità
>Funzione $\mathbb P:\mathbb F\to\mathbb R$ è detta misura di probabilità se : 
>- $\forall E\in \mathbb F : 0\leq\mathbb P(E)\leq 1$
>- $\mathbb P(\Omega)=1$
>- $\forall$ sequenza (finita o infinita) di eventi $E_1,E_2,\dots$ ***a due a due disgiunti*** ($E_i\cap E_j=\emptyset,\forall i\neq j$) si ha che $$\mathbb P\left(\bigcup_{i=1,2,3,\dots} E_i\right)=\sum\limits_{i=1,2,3,\dots}\mathbb P(E_i)$$

> Notazione

Se $E\in\mathbb F$, definiamo $E^c=\Omega\setminus E$ l'evento **complementare**

