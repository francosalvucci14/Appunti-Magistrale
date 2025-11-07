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
# Network Formation Games

I vari NFG modellano modi distinti in cui agenti egoisti possono creare e valutare reti.

Vedremo due modelli:
- Gioco di connessione globale (Global connection game)
- Gioco di connessione locale (Local connection game)

Entrambi i modelli mirano a cogliere due questioni contrastanti: i giocatori vogliono
- minimizzare i costi sostenuti nella costruzione della rete
- garantire che la rete fornisca loro un servizio di alta qualità

I NFG possono essere usati per modellare:
- formazione di social network (gli archi rappresentano le relazioni sociali)
- come le sottoreti si connettono nelle reti informatiche
- formazione di reti che connettono gli utenti tra loro per il download di file (reti P2P)

Dovremmo rispondere alle seguenti domande

Che cos'è una rete stabile?
- Utilizziamo un NE come concetto di soluzione.
- Consideriamo *stabili* le reti corrispondenti agli equilibri di Nash.

Come valutare la qualità complessiva di una rete?
- Consideriamo il costo sociale: la *somma* dei costi dei giocatori.

**Il nostro obiettivo**: limitare la perdita di efficienza derivante dalla stabilità.
## Global Connection Game

Definiamo formalmente il modello del Global Connection Game

>[!definition]- Modello GCG
>Abbiamo le seguenti strutture:
>- Grafo diretto $G(V,E)$
>- $c_{e}$ = costo non negativo dell'arco $e\in E$
>- $k$ giocatori
>- ogni giocatore $i$ ha un nodo sorgente $s_{i}$ e un nodo pozzo $t_i$
>- l'obiettivo del giocatore $i$-esimo è: creare una rete dove sia possibile arrivare a $t_i$ partendo da $s_{i}$, pagando il meno possibile
>- la strategia di ogni giocatore $i$: un percorso $P_{i}$ che va da $s_i\to t_i$

Vediamo inoltre che:
- Dato un vettore di strategie $S$, la **rete costruita** sarà $N(S)=\bigcup\limits_{i=1,\dots, k}P_{i}$
- Il **costo della rete** costruita sarà ripartito tra tutti i soggetti coinvolti come segue: $$cost_{i}(S)=\sum\limits_{e\in P_{i}}\frac{c_{e}}{k_{e}(S)}\quad k_{e}(S)=\text{num. giocatori il cui percorso contiene l'arco }e$$
Alcune volte scriveremo $k_e$ invece che $k_{e}(S)$ quando $S$ sarà chiaro dal contesto 

Questo schema di cost-sharing viene chiamato **meccanismo cost-sharing fair** oppure **di Shapley**

Abbiamo detto che usiamo un NE come concept della soluzione.
Un vettore di strategie $S$ è un NE se a nessun giocatore conviene cambiare la propria strategia
Dato quindi $S,N(S)$ si dice *stabile* se $S$ è un NE
Per valutare la qualità generale di una rete, consideriamo i **costi sociali**, ad esempio, la somma dei costi di tutti i giocatori:
$$cost=\sum\limits_{i}cost_{i}(S)$$
Diremo che una rete è **ottimale** oppure **socialmente ottimale** se minimizza il costo sociale

**oss** : notiamo che $cost(S)=\sum\limits_{e\in N(S)}c_{e}$

Vediamo un esempio

![center|400](Pasted%20image%2020251105153705.png)

Qual'è la rete socialmente ottima? Il costo dell'ottimo sociale è $13$

Se prendiamo come $N(S)$ il percorso rosso nella figura sottostante

![center|400](Pasted%20image%2020251105153828.png)

otteniamo che:
- $cost_{1}=7$ ottenuto con la formula $\sum\limits_{e\in P_{i}}\frac{c_{e}}{k_{e}(S)}=\frac{6}{2}+ \frac{4}{2}+ \frac{2}{1}=3+2+2=7$
- $cost_{2}=11$ sempre ottenuto con la formula precedente $\frac{6}{2}+ \frac{4}{2}+ \frac{1}{1}=3+2+1=6$
- il **costo sociale** della rete è $13$, ovvero $cost_{1}+cost_{2}=7+6=13$
- ma è stabile? la risposta è *no*

Cambiamo $N(S)$ come segue

![center|400](Pasted%20image%2020251105155355.png)

qui abbiamo che:
- $cost_{1}=6$
- $cost_{2}=11$
- **costo sociale** della rete $17$
- stabile? anche qui *no*

Cambiamo ulteriormente

![center|400](Pasted%20image%2020251105155456.png)

qui invece abbiamo:
- $cost_1=6$
- $cost_{2}=10$
- **costo sociale** $16$
- stabile? in questo caso ***si***, perchè è il minimo possibile $\implies$ NE

Questioni affrontate
- Esiste sempre una rete stabile?
- È possibile limitare il prezzo dell'anarchia (PoA)?
- È possibile limitare il prezzo della stabilità (PoS)?
- La versione ripetuta del gioco converge sempre verso una rete stabile?

Analizziamo sia PoA che PoS, e poi ne daremo un bound

Data una rete $G$, definiamo come:
- PoA di un gioco in $G$ come $$\max_{S\space t.c\space S\text{ è un }NE}\frac{cost(S)}{cost(S^{\star}_{G})}$$dove $S^{\star}_{G}$ è l'ottimo sociale per $G$
- PoS di un gioco in $G$ come $$\min_{S\space t.c\space S\text{ è un }NE}\frac{cost(S)}{cost(S^{\star}_{G})}$$
![center|300](Pasted%20image%2020251105160217.png)

Ovviamente quello che vogliamo fare è limitare PoA e PoS nel **worst-case** come:
- PoA del gioco = $\max_{G}$ PoA in $G$
- PoS del gioco = $\min_{G}$ PoS in $G$

Prima di definire correttamente questi bound diamo qualche notazione:
- $x=(x_{1},x_{2},\dots,x_{k});\space x_{-i}=(x_{1},\dots,x_{i-1},x_{i+1},\dots,x_{k});\space x=(x_{-i},x_{i})$
- $G$ : rete diretta e pesata
- costo o lunghezza di un percorso $\pi$ in $G$ partendo da un nodo $u\to v$: $\sum\limits_{e\in\pi}c_{e}$
- $d_{G}(u,v)$ : distanza fra $u$ e $v$ in $G$ : lunghezza di qualunque shortest path in $G$ da $u\to v$
### PoA : lower bound

Prendiamo il seguente esempio

![center|400](Pasted%20image%2020251105160833.png)

La rete ottimale ha costo $1$

Il miglior NE : tutti i giocatori usano l'arco basso (quello con costo $1$) $\to$ PoS in $G$ è $1\space\checkmark$
Il peggior NE : tutti i giocatori usano l'arco alto (quello con costo $k$) $\to$ PoA in $G$ è $1\space\times$

Quindi, il PoA del gioco è $\geq k$

Vediamo un risultato più generale, dato dal seguente teorema

>[!teorem]- Teorema 
>Il PoA nel GCG con $k$ giocatori è **al più** $k$ ($\leq$ k)

**dimostrazione**

Sia $S$ un NE, e sia $S^\star$ un profilo strategico che minimizza il costo sociale per ogni giocatore $i$

Sia inoltre $\pi_i$ lo shortest path in $G$ che va da $s_{i}\to t_{i}$

Allora, otteniamo che 
$$cost_{i}(S)\leq cost_{i}(S_{-i},\pi_{i})\leq d_{G}(s_{i},t_{i})\leq cost(S^\star)$$
![200](Pasted%20image%2020251105161705.png)

Prendiamo ora $\pi$ come un qualunque percorso in $N(S^{\star})$ che va da $s_i\to t_{i}$
Allora possiamo dire che $$d_{G}(s_{i},t_{i})\leq \text{costo di }\pi\leq cost(S^{\star})$$
Allora, alla fine ottengo che 
$$cost(S)=\sum\limits_{i}cost_{i}(S)\leq k\cdot cost(S^\star)\quad\blacksquare$$
### PoS & Potential Function Method : lower bound

Prendiamo, come fatto prima, il seguente esempio di rete

![center|500](Pasted%20image%2020251105162111.png)

dove $\varepsilon\gt0$ piccolo a piacere

Ora, la soluzioen **ottima** ha un costo di $1+\varepsilon$, ma se prendiamo $N(S)$ come sotto risulta essere stabile?

![center|500](Pasted%20image%2020251105162204.png)

La risposta è no, perchè il giocatore $k$-esimo può decrementare il suo costo

Vediamo allora se nel seguente modo risulta stabile

![center|500](Pasted%20image%2020251105162303.png)

Anche qui la risposta è no, dato che il giocatore $(k-1)$-esimo può anch'esso decrementare il suo costo, e così via per ogni altro giocatore

Risulta allora che **l'unica** rete stabile è la seguente:

![center|500](Pasted%20image%2020251105162411.png)

Così facendo, risulta quindi che il costo sociale è pari a 
$$\sum\limits_{j=1}^{k} \frac{1}{j}=H_{k}\leq\ln(k)+1$$
ovvero il $k$-esimo **numero armonico**

Avevamo detto che la soluzione ottima ha costo $1+\varepsilon$, ma questo porta a dire che il PoS del gioco ha costo $\leq H_{k}$

Come prima, vediamo dei risultati più generali dati dai seguenti teoremi

>[!teorem]- Teorema 1
>Qualsiasi istanza del GCG ha un equilibrio di Nash puro e la miglior dinamica di risposta converge sempre

>[!teorem]- Teorema 2
>Il PoS nel GCG con $k$ giocatori è al più $H_{k}$, il $k$-esimo numero armonico

Per dimostrare entrambi i teoremi useremo il **Potential Function Method**

Prima di tutto diamo la seguente definizione:

>[!definition]- Exact Potential Function
>Per ogni gioco finito, una **funzione potenziale esatta** $\phi$ è una funzione che mappa ogni vettore di strategie $S$ in un qualche valore e che soddisfa la seguente condizione:
>$\forall S=(S_{1},\dots,S_{k}),S^{'}_{i}\neq S_{i},\text{ sia }S^{'}=(S_{-i},S^{'}_{i})$ allora vale che $$\phi(S)-\phi(S^{'})=cost_{i}(S)-cost_{i}(S')$$

Un gioco che possiedeuna funzione potenziale esatta viene chiamato **gioco potenziale**

Vale quindi il seguente teorema:

>[!teorem]- Teorema 3
>Ogni gioco potenziale ha almeno un NE puro, ovvero il vettore di strategie $S$ minimizza $\phi(S)$

**dimostrazione**

Consideriamo una qualunque mossa del giocatore $i$ che porta a un nuovo vettore di strategie $S'$

Dal teorema abbiamo quindi che 
$$\underbrace{\phi(S)-\phi(S^{'})}_{\leq0}=cost_{i}(S)-cost_{i}(S^{'})\implies cost_{i}(S)\leq cost_{i}(S^{'})$$
e di conseguenza, il giocatore $i$ non può decrementare il suo costo, e quindi $S$ risulta essere un NE $\blacksquare$

Vale anche il teorema successivo:

>[!teorem]- Teorema 4
>In qualsiasi gioco potenziale finito, le migliori dinamiche di risposta convergono sempre verso un equilibrio di Nash

**dimostrazione**

La dinamica di risposta migliore simula una ricerca locale su $\phi$:
- ogni mossa decrementa (in senso stretto) $\phi$
- il numero di soluzioni è finito
$\blacksquare$

**oss** nel nostro gioco, una risposta migliore può essere calcolata in tempo polinomiale

Vediamo ora quest' ultimo teorema

>[!teorem]- Teorema 5
>Supponiamo di avere un gioco potenziale con una funzione potenziale $\phi$, e assumiamo che per ogni output $S$ abbiamo che $$\frac{cost(S)}{A}\leq\phi(S)\leq B\cdot cost(S)$$
>per qualche $A,B\gt0$
>Allora, il PoS è al più $AB$

**dimostrazione**

Sia $S^{'}$ il vettore di strategie che minimizza $\phi$
Sia $S^{\star}$ il vettore di strategie che minimizza il costo sociale

Abbiamo quindi che 
$$\frac{cost(S^{'})}{A}\leq\phi(S^{'})\leq\phi(S^{\star})\leq B\cdot cost(S)\quad\blacksquare$$

Ritorniamo ora al GCG

Sia $\phi$ la seguente funzione che mappa ogni vettore di strategie $S$ in un valore reale: 
$$\phi(S)=\sum\limits_{e\in E}\phi_{e}(S)$$
dove 
$$\phi_{e}(S)=c_{e}H_{k_{e}(S)}$$
ricordiamo che $$H_{k}=\sum\limits_{j=1}^{k} \frac{1}{j},\quad H_{0}=0$$
Valgono quindi i seguenti lemmi

>[!teorem]- Lemma 1
>Sia $S=(P_{1},\dots,P_{k})$, sia $P_{i}^{'}$ un percorso alternativo per un qualche giocatore $i$, e definiamo un nuovo vettore di strategie $S^{'}=(S_{-i},P_{i}^{'})$
>Allora:
>$$\phi(S)-\phi(S^{'})=cost_{i}(S)-cost_{i}(S^{'})$$

>[!teorem]- Lemma 2
>Per ogni vettore di strategie $S$, vale che $$cost(S)\leq\phi(S)\leq H_{k}cost(S)$$

Da questi due lemmi otteniamo che il PoS del gioco è $\leq H_{k}$

Dimostriamo questi due lemmi

**dimostrazione lemma 1**

![center|500](Pasted%20image%2020251106165529.png)

per ogni $e\in P_{i}\cap P_{i}^{'}$ abbiamo che 
- il termine $e$ del $cost_{i}()$ e il potenziale $\phi_{e}$ rimangono gli stessi

![center|500](Pasted%20image%2020251106165822.png)

per ogni $e\in P_{i}^{'}\setminus P_{i}$ abbiamo che 
- il termine $e$ di $cost_{i}()$ viene incrementato di un fattore $\frac{c_{e}}{(k_{e}(S)+1)}$
- il potenziale $\phi_{e}$ incrementa e passa da $c_{e}(1+\frac{1}{2}+\dots+\frac{1}{k_{e}(S)})$ a $c_{e}(1+\frac{1}{2}+\dots+\frac{1}{k_{e}(S)}+\frac{1}{k_{e}(S)+1})$
- otteniamo quindi che $$\Delta\phi_{e}=\frac{c_{e}}{(k_{e}(S)+1)}$$

![center|500](Pasted%20image%2020251106172938.png)

per ogni $e\in P_{i}\setminus P_{i}^{'}$ abbiamo che
-  il termine $e$ di $cost_{i}()$ viene decrementato di un fattore $\frac{c_{e}}{k_{e}(S)}$
- il potenziale $\phi_{e}$ decrementa e passa da $c_{e}(1+\frac{1}{2}+\dots+\frac{1}{k_{e}(S)-1}+\frac{1}{k_{e}(S)})$ a $c_{e}(1+\frac{1}{2}+\dots+\frac{1}{k_{e}(S)-1})$
- e quindi otteniamo che $$\Delta\phi_{e}=-\frac{c_{e}}{k_{e}(S)}$$

$\blacksquare$

**dimostrazione lemma 2**

Vale che 
$$cost(S)\leq\phi(S)=\sum\limits_{e\in E}c_{e}H_{k_{e}(S)}=\sum\limits_{e\in N(S)}c_{e}H_{k_{e}(S)}\leq\sum\limits_{e\in N(S)}c_{e}H_{k}=H_{k}cost(S)$$
dove la prima uguaglianza vale per definizione stessa di $\phi(S)$,e l'ultima disuguaglianza vale perchè $$1\leq k_{e}(S)\leq k$$
$\blacksquare$

Vediamo ora il seguente teorema

>[!teorem]- Teorema
>Data un istanza di un GCG e un valore $C$, determinare se il gioco ha un NE di costo al più $C$ è un problema **NPC**

**dimostrazione (tramite riduzione polinomale)**

la dimostrazione del teorema avviene tramite riduzione polinomale dal problema $3D$-matching

