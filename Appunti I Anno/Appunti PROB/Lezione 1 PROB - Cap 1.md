# Cap 1 : Eventi e Probabilità

>[!definition]- Def 1.1 Spazio di Probabilità
>Tripla $(\Omega,\mathbb F,\mathbb P)$ dove : 
>- $\Omega$ : Spazio degli eventi
>- Famiglia $\mathbb F$ di sottoinsiemi di $\Omega$ (detti **eventi**)
>- $\mathbb P$ : misura di probabilità

**oss** : in questo corso $\Omega$ sarà sempre discreto e $\mathbb F$ l'insieme delle parti di $\Omega$

>[!definition]- Def 1.2 Misura di probabilità
>Funzione $\mathbb P:\mathbb F\to\mathbb R$ è detta misura di probabilità se : 
>- $\forall E\in \mathbb F : 0\leq\mathbb P(E)\leq 1$
>- $\mathbb P(\Omega)=1$
>- $\forall$ sequenza (finita o infinita) di eventi $E_1,E_2,\dots$ ***a due a due disgiunti*** ($E_i\cap E_j=\emptyset,\forall i\neq j$) si ha che $$\mathbb P\left(\bigcup_{i=1,2,3,\dots} E_i\right)=\sum\limits_{i=1,2,3,\dots}\mathbb P(E_i)$$

> Notazione

Se $E\in\mathbb F$, definiamo $E^c=\Omega\setminus E$ l'evento **complementare**

**Conseguenze della definizione** 

1. $\emptyset\in\mathbb F$ e $\mathbb P(\emptyset)=0$
2. se $E_1\subseteq E_2\implies\mathbb P(E_1)\leq\mathbb P(E_2)$
3. $\mathbb P(E^{c})=1-\mathbb P(E),\forall E\in\mathbb F$
4. $\forall E_1,E_2\in\mathbb F\implies\mathbb P(E_1)=\mathbb P(E_1\cap E_2)+\mathbb P(E_{1}\cap E_{2}^c)$

>[!definition]- Lemma base (1.1)
>$\forall$ coppia di eventi $E_{1},E_{2}\in\mathbb F$ si ha che : 
>$$\mathbb P(E_{1}\cup E_{2})=\mathbb P(E_1)+\mathbb P(E_2)-\mathbb P(E_1\cap E_2)$$

>[!definition]- Lemma 1.2 Union-Bound
>$\forall$ sequenza di eventi $E_{1},E_{2},\dots\in\mathbb F$ si ha che : 
>$$\mathbb P\left(\bigcup_{i}E_{i}\right)\leq\sum\limits_{i}\mathbb P(E_i)$$

**oss** : $\mathbb P(E_1\cup E_2)\leq\mathbb P(E_1)+\mathbb P(E_2)$

>[!definition]- Lemma 1.3 Principio di Inclusione-Esclusione
>Sia $E_{1},\dots,E_{n}\in\mathbb F$. Allora
>$$\begin{align}\mathbb P\left(\bigcup_{i=1}^{n}E_i\right)=&\sum\limits_{i=1}^{n}\mathbb P(E_i)-\sum\limits_{\substack{i\lt j\\i,j=1}}^{n}\mathbb P(E_{i}\cap E_j)+\\&\sum\limits_{i\lt j\lt k}^{n}\mathbb P(E_{i}\cap E_{j}\cap E_k)-\dots\\& +(-1)^{l-1}\sum\limits_{i_{1}\lt i_{2}\lt\dots\lt i_{l}}^{n}\mathbb P\left(\bigcap_{r=1}^{l}E_r\right)+\dots\end{align}$$

>[!definition]- Def 1.3 Eventi Indipendenti
>Due eventi $E_1,E_2\in\mathbb F$ si dicono **indipendenti** se $$\mathbb P(E_1\cap E_2)=\mathbb P(E_1)\mathbb P(E_2)$$


In generale eventi $E_1,E_2,\dots,E_n$ si dicono **mutualmente indipendenti** se 
$$\forall I\subseteq\{1,\dots,n\}\to\mathbb P\left(\bigcap_{i\in I}E_i\right)=\prod_{i\in I}\mathbb P(E_i)$$
>[!definition]- Probabilità Condizionata
>La **probabilità condizionata** dell'evento $E_1$ sapendo che è accaduto l'evento $E_2$ è : 
>$$\mathbb P(E_1|E_2)=\frac{\mathbb P(E_{1}\cap E_2)}{\mathbb P(E_2)}\quad(*)$$
>Essa è ben definita $\iff\mathbb P(E_2)\neq0$

Diamo ora un paio di osservazioni : 

1. È come se il nuovo spazio degli eventi fosse $E_2$
2. Si può verificare che $\mathcal P(\cdot)=\mathbb P(\cdot|E_2)$ è una nuova misura di probabilità
3. Se $\mathbb P(E_2)\neq 0\implies E_1,E_2$ sono indipendenti $\iff\mathbb P(E_1|E_2)=\mathbb P(E_1)$
4. È utile a volte riscrivere $(*)$ come $$\mathbb P(E_{1}\cap E_2)=\mathbb P(E_1|E_2)\mathbb P(E_2)$$ o anche $$\mathbb P(E_1|E_2)=\frac{\mathbb P(E_{1}\cap E_{2})}{\mathbb P(E_2)}=\underbracket{\mathbb P(E_2|E_1)}_{\text{a volte più semplice da calcolare}}\cdot\frac{\mathbb P(E_1)}{\mathbb P(E_2)}$$
>[!teorem]- Teorema 1.6 Formula Probabilità Totali
>Siano $\{E_{i}\}_{i=1,\dots,n}n$ eventi disgiunti di $\mathbb F$ tale che $\bigcup_{i}E_i=\Omega$ (dicesi partizione di $\Omega$)
>Allora : 
>$\forall B\in\mathbb F$ si ha che $$\mathbb P(B)=\sum\limits_{i=1}^{n}\mathbb P(B\cap E_i)=\sum\limits_{i=1}^{n}\mathbb P(B|E_i)\mathbb P(E_i)$$

Piccola digressione prima del teorema di Bayes

Abbiamo visto che $$\mathbb P(E_1|E_2)=\mathbb P(E_2|E_1)\frac{\mathbb P(E_1)}{\mathbb P(E_2)}$$
Scrivendo $$E_{2}=(E_{2}\cap E_{1})\cup(E_{2}\cap E_{1}^c)$$
Otteniamo $$\mathbb P(E_1|E_2)=\frac{\mathbb P(E_2|E_1)\mathbb P(E_1)}{\mathbb P(E_2|E_1)\mathbb P(E_1)+\mathbb P(E_2|E_1^c)\mathbb P(E_1^c)}$$
Sia pronti per definire il teorema di Bayes

>[!teorem]- Teorema di Bayes (1.7)
>Abbiamo le stesse ipotesi del teorema precedente
>Sia $B\in\mathbb F$ con $\mathbb P(B)\neq0$
>Si ha che : 
>$$\mathbb P(E_j|B)=\frac{\mathbb P(B|E_j)\mathbb P(E_j)}{\sum\limits_{i=1}^{n}\mathbb P(B|E_i)\mathbb P(E_i)}$$
>Valida per ogni $j$ fissato

Vedi esempi + applicazione del teorema di Bayes sull'Ipad (col cazzo che li riscrivo in Latex)
