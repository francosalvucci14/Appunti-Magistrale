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
# Azioni e relazioni

La presenza di una rete influenza il comportamento degli individui che la compongono, dato che gli individui, proprio in virtù della rete, interagiscono fra loro [^1]

Molte delle nostre interazioni avvengono a livello locale piuttosto che globale, perciò gli individui che **possono influenzare il nostro comportamento** sono quelli con i quali siamo in relazione

Entriamo ora nel merito della natura di questa "influenza di rete"

# Omofilia

Abbiamo già incontrato il fenomeno della chiusura triadica, ovvero la tendenza che si stabiliscano relazioni fra gli individui che hanno una relazione forte con uno stesso individuo

Questo fenomeno è strettamente connesso al concetto di omofilia che si esplica in due direzioni:
- in un senso, **è la tendenza a connetterci con gli individui che ci assomigliano**
	- ad esempio, un individuo tende a non stabilire connessioni con chi ha idee politiche diverse dalle proprie
	- ma anche: se amo il mare, diventerò amico con la gente che incontro al mare
	- e questo per numerose ragioni, tra cui:
		- **selezione**: tendo ad essere amico a chi mi somiglia
		- **opportunità**: se amo il mare, difficilmente nelle mie vacanze incontrerò gli amanti della montagna
- nell'altro senso, **è la tendenza a diventare simili agli individui con i quali siamo in relazione**
	- ad assumere i loro stessi gusti
	- ad adeguarci ai loro comportamenti
	- a diventare amici dei loro amici
	- etc..
	- La motivazione soggiacente a questa tendenza è l'esigenza di ridurre la tensione sociale, ma ce anche una motivazione assolutamente razionale, ad esempio:
		- se tutti i miei amici comprano un nuovo S.O, io che li stimo (dio porco che esempi di merda), assumo che sia una buona idea e lo acquisto a mia volta
			- inoltre, se mi tenessi il mio vecchio S.O, magari non potrei più scambiare file con loro...

# Processi di diffusione

Vogliamo modellare il processo di diffusione in una rete e, per farlo dobbiamo stabilire le regole in base alle quali un nodo decide di cambiare (comportamento, opinione, prodotto)

Intanto, definiamo un modello di decisioni **individuali** [^2], nel quale le scelte dei nodi sono guidate da ***motivazioni di pure interesse personale***
- la spinta a cambiare è tanto maggiore quanto maggiore è il vantaggio che si prevede che deriverà dal cambiamento

Assumiamo che nella rete sia stabilizzato un certo stato delle cose $B$, e che, ad un certo istante di tempo, alcuni individui cambino il loro stato in $A$

In quali casi un individuo sceglie di cambiare il proprio stato da $B$ ad $A$? 
- assumendo che dallo stato $A$ non si torni mai in $B$

Modelliamo quindi un processo di diffusione mediante un **Network Coordination Game**.

SIa $(u,v)$ un arco della rete, assumiamo che il beneficio reciproco di adottare $A$ o $B$ sia quello illustrato in tabella:

| $u/v$ | A     | B     |
| ----- | ----- | ----- |
| $A$   | $a,a$ | $0,0$ |
| $B$   | $0,0$ | $b,b$ |

Vale quindi che:
- Se $u,v$ adottano entrambi $A$ allora entrambi hanno un beneficio pari ad $a$
- Se $u,v$ adottano entrambi $B$ allora entrambi hanno un beneficio pari ad $b$
- Altrimenti nessuno dei due ha alcun beneficio (dalla reciproca relazione)

Ma un nodo nella rete ha, in generale, più vicini

Cosa accade quando qualcuno dei vicini di un nodo $u$ è nello stato $A$ e qualcun'altro nello stato $B$? (modello lineare)

Semplicemente, detti $n_{A}$ il numero di vicini di $u$ nello stato $A$ e $n_{b}$ il numero di vicini di $u$ nello stato $B$, se $u$ rimane in $B$ ha un beneficio pari a $bn_{b}$, se $u$ passa ad $A$ ha un beneficio pari a $an_{a}$:
- $u$ rimane in $B$ se $bn_{b}\gt an_{a}$
- $u$ passa ad $A$ se $an_{a}\geq bn_{b}$
- osserviamo che a parità di beneficio, $u$ passerà ad $A$ (l'innovazione è preferibile al vecchio stato)

Quindi, dato che $n_{b}=|N(u)|\setminus n_{a}$, $u$ passerà ad $A$ solo se $$an_{a}\geq b(|N(u)|\setminus n_{a})$$
Quindi, solo se $\frac{n_{a}}{|N(u)|}a\geq\frac{|N(u)|\setminus n_{a}}{|N(u)|}b$, ovvero detto $p_{a}=\frac{n_{a}}{|N(u)|}$, se $p_{a}a\geq(1-p_{a})b$
Quindi, il nodo $u$ passerà nello stato $A$ solo se, detta $p_{a}$ la frazione dei vicini di $u$ che stanno in $A$, vale che $$p_{a}\geq\frac{b}{a+b}$$
Chiamiamo $q=\frac{b}{a+b}$ la **soglia di adozione** di $A$

Si distinguono $3$ casistiche:
1) quando $q$ è molto piccolo, occorrono pochi vicini nello stato $A$ per indurre un nodo a cambiare stato
	1) e $q$ è molto piccolo quando $a$ è molto più grande di $b$, ovvero quando lo stato $A$ è molto migliore dello stato $B$
2) quando $a=b$ occorrono almeno la metà dei vicini nello stato $A$ per indurre un nodo a cambiare stato
	1) questo accade quando lo stato $A$ è confrontabile con lo stato $B$
3) quando $a$ è molto più piccolo di $b$, occorrono molti vicini nello stato $A$ per indurre un nodo a cambiare stato
	1) questo accade quando lo stato $A$ è peggiore dello stato $B$
	2) è quindi costoso/rischioso/faticoso adottare lo stato $A$

## Game e configurazioni di equilibrio

Cerchiamo ora di capire se e quali **configurazioni di equilibrio** ha il network coordination game che abbiamo appena introdotto.
- configurazioni in cui nessun nodo cambia stato da $B\to A$

Osserviamo che esistono sempre $2$ configurazioni di equilibrio banali, ovvero:
1) la configurazione che si ottiene quando $A$ non viene introdotto nella rete, e quindi tutti i nodi hanno stato $B$
2) la configurazione che si ottiene quando $A$ viene inserito nella rete, e tutti i nodi assumono stato $A$

La seconda sopratutto può accadere perchè, una volta inserito nella rete, lo stato $A$ inizierà a diffondersi

Le domande però a cui dobbiamo dare una risposta sono:
- Quando termina il processo di diffusione?
- Riesce sempre a toccare tutti i nodi? Oppure talvolta la diffusione si blocca prima di raggiungere tutti i nodi, andando a finire quindi in configurazioni intermedie?
	- In questo caso, *perchè* si blocca?

Capiamo, innanzi tutto, con un esempio

![[Pasted image 20250812110103.png|center|450]]

In questo esempio, vediamo come lo stato $A$ viene forzato all'inizio sui noid $v,w$
In questo esempio, vale che $a=3,b=2$ quindi $A$ migliore di $B$, e di conseguenza, usando la formula della soglia, otteniamo che $q=\frac{2}{3+2}=\frac{2}{5}$

Quindi, per adottare $A$, un nodo deve avere i $\frac{2}{5}$ dei vicini nello stato $A$.

Come si vede alla fine, un nodo dopo l'altro, tutti adotteranno $A$

Altro esempio

![[Pasted image 20250812110533.png|center|350]]

Caso $1)$: $a=3,b=2,q=\frac{2}{5}$
- caso illustrato in figura, $A$ non riesce a raggiungere i nodi fuori l'esagono, quindi non tutti i nodi adottano $A$

![[Pasted image 20250812110643.png|center|350]]

Caso $2)$: $a=4,b=2,q=\frac{2}{6}=\frac{1}{3}$
- caso illustrato in figura, dopo aver raggiunto tutti i nodi dell'esagono, $A$ viene adottato da $2,11,14$, poi da $1,3,12,13,17$ e infine da $15,16$
- Tutti i nodi hanno adottato $A$
## Diffusione e cascate complete

Dai due esempi possiamo trarre una serie di conclusioni:
- intanto, non sempre i nodi si adeguano all'innovazione
- poi, se questo accade, possiamo aumentare il beneficio derivante dall'adozione di $A$ per indurre tutti i nodi ad adottarli, ad esempio abbasandone il costo di acquisizione

Ma dovrebbe essere chiaro anche che l'eventualità che tutti i nodi arriveranno ad adottare $A$ dipende dai nodi che scegliamo per forzare lo stato $A$ all'inizio del processo, dal loro numero,ma anche dalla loro posizione all'interno della rete

Ad esempio, mantenendo $a=3$ e fornando $A$ su $4$ nodi (invece che su $2$), otteniamo che:
- se forziamo $A$ sui nodi $7,8,2,12$ tutti i nodi adotteranno $A$
- se forziamo $A$ sui nodi $7,8,2,14$, o peggio ancora, $7,8,4,5$, non tutti i nodi adotteranno $A$
- perchè questa cosa?

Prima di procedere, abbiamo bisogno di qualche definizione e di qualche notazione.

Inizialmente, lo stato $A$ viene forzato su un certo insieme $V_0$ di nodi che chiameremo **iniziatori**

Come abbiamo visto, una volta che $A$ viene introdotto nella rete, esso inizia a diffondersi. 

Ha quindi inizio un processo di diffusione che procede ***in una sequenza di passi discreti***: 
- al passo $1$, un insieme $V_1$ di vicini dei nodi in $V_{0}$ adotta $A$
- al passo $2$, un insieme $V_2$ di vicini dei nodi in $V_{0}\cup V_{1}$ adotta $A$
- $\dots$
- al passo $t$, un insieme $V_t$ di vicini dei nodi in $V_{0}\cup V_{1}\cup\dots\cup V_{t-1}$ adotta $A$

Indichiamo quindi con $V_i$ l'insieme dei nodi che adottano $A$ al passo $i$

Viene generata una ***cascata completa*** se ad un certo passo $t$, tutti i nodi hanno adottato $A$, ovvero se: $$\exists t\geq0:\bigcup_{0\leq i\leq t}V_i=V$$
#### Cascate e Clusters

Se ripensiamo all'esempio, sembra che l'innovazione abbia difficoltà a uscire dall'"esagono centrale, che appare come un gruppo coeso di nodi

Diamo un'importante definizione, che ci servirà più avanti.

>[!definition]- Cluster di densità $p$
>Un **cluster di densità $p$** è un sottoinsieme di nodi $V'\subseteq V$ tale che la frazione di vicini che ogni suo nodo ha in $V'$ è almeno $p$, ovvero $$\forall u\in V'\left[\frac{|N(u)\cap V'|}{|N(u)|}\geq p\right]$$

Es: il sottinsieme $\{4,5,6,7,8,9,10\}$ dell'esempio è un cluster di densità $p=\frac{2}{3}$

Adesso, cosa ci facciamo con la definizione di cluster a densità $p$? 
Dimostremo un teorema importate che lega la definizione di cluster a densità $p$ con la cascata completa del processo di diffusione.

**Notazione** : Sia $G=(V,E)$ un grafo e sia $V'\subseteq V$: indichiamo con $G\setminus V'$ il grafo ottenuto rimuovendo da $G$ tutti i nodi in $V'$ e tutti gli archi incidenti ai nodi in $V'$

Vale quindi il seguente teorema

>[!teorem]- Teorema 1
>Sia $G=(V,E)$ un grafo e siano $V_0\subseteq V$ l'insieme degli iniziatori e $q$ la soglia di adozione di $A$: $V_0$ **non genera** una cascata completa $\iff G\setminus V_{0}$ contiene un cluster di densità maggiore di $1-q$

**dimostrazione parte $\implies$**

Se $V_0$ non genera una cascata completa, allora esistono nodi che non adottano $A$
Abbiamo detto che con $V_i$ indichiamo i nodi che adottano $A$ al passo $i$, sia quindi $t$ il passo tale che $V_t\neq\emptyset$ e $V_{t+1}=\emptyset$ (quindi $t+1$ è il primo passo in cui $A$ non si diffonde)

Poniamo $V_{A}=\bigcup_{0\leq i\leq t}V_{i}$: $V_A$ contiene tutti e soli i nodi che adottano $A$

Dato che, per ipotesti, esistono nodi che **non** adottano $A$, allora $V\setminus V_A\neq\emptyset$, e quindi vale che $$\forall v\in V\setminus V_A:\frac{|N(v)\cap V_{A}|}{|N(v)|}\lt q$$
e quindi, dato che $$\frac{|N(v)\cap V_{A}|}{|N(v)|}+\frac{|N(v)\cap (V\setminus V_{A})|}{|N(v)|}=1$$
vale che $$\frac{|N(v)\cap (V\setminus V_{A})|}{|N(v)|}\gt1-q$$
E quindi, $V\setminus V_A$ è un cluster di densità maggiore di $1-q$, e $(V\setminus V_{A})\subset G\setminus V_0$

**dimostrazione parte $\Leftarrow$**

Se $G\setminus V_0$ contiene un cluster di densità maggiore di $1-q$, significa che $$\exists C\subseteq V\setminus V_{0}:\forall v\in C,\frac{|N(v)\cap C|}{|N(v)|}\gt1-q$$
Supponiamo per assurdo che si generi una cascata completa, allora i nodi in $C$, prima o poi, adotteranno $A$

Sia $t$ il primo passo tale che $V_t\cap C\neq\emptyset$, ovvero, per $$i\lt t,V_i\cap C=\emptyset\land\exists u\in V_{t}\cap C$$
Poniamo $V'=\bigcup_{0\leq i\leq t-1}V_{i}:V'$ sono tutti i nodi che al passo $t-1$ sono nello stato $A$ (e $V'$ non contiene nodi di $C$)

Allora:
1) poichè $C$ è un cluster di densità $\gt1-q$ e $u\in C$, allora $\frac{|N(u)\cap C|}{|N(u)|}\gt1-q$
2) poichè $u\in V_t$, allora $\frac{|N(u)\cap V'|}{|N(u)|}\geq q$

E quindi, dato che $V'\cap C=\emptyset$, allora abbiamo che: 
$$1=\frac{|N(u)|}{|N(u)|}\geq\frac{|N(u)\cap (C\cup V')|}{|N(u)|}=\frac{|N(u)\cap C|}{|N(u)|}+\frac{|N(u)\cap V'|}{|N(u)|}\gt1$$Assurdo $\blacksquare$




[^1]: talvolta modificandone il comportamento, come visto nell'esperimento di Ganovetter

[^2]: non c'è coalizione di gruppi di nodi per prendere collettivamente la stessa decisione