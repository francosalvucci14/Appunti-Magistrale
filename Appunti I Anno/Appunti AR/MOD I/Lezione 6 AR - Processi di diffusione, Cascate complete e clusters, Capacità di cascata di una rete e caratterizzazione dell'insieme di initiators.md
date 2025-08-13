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
### Cascate e Clusters

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

**dimostrazione parte $\implies$** ^953f09

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

#### Il ruolo dei weak ties

Il teorema appena dimostrato mette in luce un nuovo aspetto della dicotomia strong/weak ties:
- le innovazioni si diffondono con relativa facilità all'interno dei cluster
	- ovvero, quando viaggia lungo strong ties l'innvazione ha un impatto significativo sui nodi che raggiunge
- invece, incontrano difficoltà nell'uscire dai cluster
	- ovvero, quando viaggia su weak ties l'innovazione ha un impatto debole sui nodi che raggiunge

Possiamo quindi concludere che, mentre l'esperimento di Granovetter ha permesso di mettere in luce la forza dei weak ties (in quanto fonte di vantaggi informativi), lo studio dei processi di diffusione ne evidenzia la debolezza (in quanto ostacolo alla diffusione)

#### Cluster e Marketing virale

La domanda che ci facciamo adesso è: è possibile superare lo stallo nel quale, a causa di cluster sufficientenmente dansi, uno stato $A$ smette di diffondersi? Se sì, come facciamo?

Abbiamo due risposte banali a questo problema.
1) Possiamo scegliere gli iniziatori in posizioni tali che ciascun cluster contenga almeno un iniziatore
2) Possiamo aumentare l'appetibilità di $A$ (per esempio, abbassandone il prezzo di vendita)

La seconda opzione però, dal punto di vista di un venditore, non è una strategia molto ben vista.

Allora ci domandiamo, quanto alto può essere mantenuto il prezzo di $A$ perchè la diffusione sia ancora virale? 
O meglio, quanto alta può essere tenuta la soglia di adozione perchè si generi una cascata completa?
##### Capacità di Cascata

Quindi, quanto alta può essere tenuta la soglia di adozione $q$ per far sì che si generi una cascata completa? Naturalmente, $q=\frac{b}{a+b}\leq1$

Innanzi tutto, per rispondere alla domanda di prima, il tutto dipende dalla struttura della rete: alcune strutture ostacolano maggiormente di altre la generazione di cascate complete

Vale quindi il seguente problema:

>[!definition]- Problema
>Dato un grafo $G=(V,E)$, qual'è la soglia di adozione *massima* $q_{\max}$ in $G$ affinchè un "piccolo" insieme $V_0$ di iniziatori di un nuovo stato $A$ generi una cascata completa?

Il valore $q_{\max}$ prende il nome di **capacità di cascata di $G$**

Nel descriverlo però siamo stati un po imprecisi, infatti la domanda sorge spontanea: quanto "piccolo" deve essere questo insieme $V_0$? e sopratutto, cosa significa "piccolo"?

**oss** : se prendiamo $V_0=V$ allora la soglia $q=1$ genera una cascata completa, tutti i nodi sono forzati nello stato $A$ (ma questo non ha molto senso)

Richiedendo che $V_0$ sia "piccolo", vogliamo che $$|V_{0}|\lt\lt|V|$$

Ipotesi di lavoro: 
- $G$ è un grafo infinito, ovvero con **infiniti nodi**
	- noi ci concentraremo su grafi *regolari* [^3]
- l'insieme $V_0$ degli iniziatori può essere un qualisasi insieme **finito**

Il problema ora diventa: 
Dato un grafo (regolare) infinito, qual'è la soglia di adozione *massima* $q_{\max}$ in $G$ affinchè **esista un insieme finito $V_0$ di iniziatori** di un nuovo stato $A$, che generi una cascata completa?

**Esempio 1 (catena)**

Se $|V_0|=1$ allora occorre $q=\frac{1}{2}$ per generare una cascata completa

![[Pasted image 20250812152510.png|center]]

Ma la domanda è, scegliendo un insieme più grande (come quello in figura sotto), è possibile generare una cascata con $q\lt \frac{1}{2}$?

![[Pasted image 20250812152744.png|center]]

La risposta è no, perchè i nodi "al confine" con $V_0$ (ovvero i nodi $x,y$ in figura), hanno comunque bisogno di $q=\frac{1}{2}$ per passare ad $A$

Allora, in una **catena infinita** abbiamo che $$q_{\max}=\frac{1}{2}$$
**Esempio 2 (griglia)**

Se $|V_0|=1$ allora occorre $q=\frac{1}{8}$ per generare una cascata completa

![[Pasted image 20250812153017.png|center|300]]

Se $|V_0|=2$ allora, scegliendo i due nodi in $V_{0}$ come nodi adiacenti, con $q=\frac{1}{4}$ si riescono ad influenzare i nodi $u,v,x,y$, per poi generare una cascata completa (come si evince in figura)

![[Pasted image 20250812153100.png|center|300]]

Se $|V_0|=3$ allora, scegliendo i tre nodi in $V_{0}$ come nodi adiacenti, con $q=\frac{3}{8}$ si riescono ad influenzare i nodi $v,y$ , poi i nodi $u,w,x,z$ e così via fino a generare una cascata completa 

![[Pasted image 20250812153238.png|center|300]]

Aumentando $|V_0|$ non si riesce ad aumentare la soglia di adozione: una volta influenzati tutti i nodi nel rettagnolo (giallo) che contiene gli iniziatori, occorre uscre da esso, e per farlo è necessario $q=\frac{3}{8}$

![[Pasted image 20250812153454.png|center|300]]

Quindi, in una **griglia infinita** si ha che $$q_\max=\frac{3}{8}$$
Da questi due esempi possiamo concludere quanto segue:
- la soglia di adozione massima è più bassa nella griglia (che ha una topologia più ricca) che non nella catena (che ha una topologia più povera)
- in entrambi i casi, essa non supera il valore $\frac{1}{2}$, e quindi, per generare una cascata completa, $A$ deve essere appetibile almeno quanto $B$

Essendo che **la soglia di adozione massima è una caratteristica della rete**, ovvero della sua topologia, la domanda sorge spontanea: esistono topologie nelle quali la soglia di adozione massima è maggiore di $\frac{1}{2}$?

Quindi, esistono topologie di rete nelle quale innovazioni di qualità mediocre soppiantino uno status quo di qualità maggiore?

Essendo che la soglia di adozione max abbiamo detto essere una caratteristica di rete, indichiamo con $q_{G}$ **la soglia di adozione massima di un grafo $G$**

Vale quindi il seguente teorema:

>[!teorem]- Teorema
>Per ogni grafo infinito $G=(V,E)$ i cui nodi hanno grado finito, vale che $$q_{G}\leq \frac{1}{2}$$

**dimostrazione**

Supponiamo per assurdo che esista un insieme finito di iniziatori $V_0$ che, con soglia di adozione $q\gt \frac{1}{2}$ generi una cascata completa (nel grafo $G$)

Come al solito, indichiamo con $V_t$ l'insieme dei nodi che adottano $A$ nel passo $t$, e sia per ogni $t\geq0,S_t=\bigcup_{0\leq i\leq t}V_i$ l'insieme dei nodi che, al passo $t$, sono nello stato $A$

Definiamo l'**interfaccia di passo $t$**, ovvero l'insieme $I_t$ degli archi che, al tempo $t$ hanno un estremo in $S_{t}$ e l'altro in $V\setminus S_{t}$, formalmente si ha che:
$$I_{t}=\{(u,v)\in E:u\in S_t\land v\in (V\setminus S_{t})\}$$
e dimostriamo che, $$\forall t\geq0,|I_{t}|\gt|I_{t+1}|\lor I_t=I_{t+1}$$
Per dimostrare ciò dobbiamo mostrare che se $$I_t\neq I_{t+1}\implies|I_t|\gt|I_{t+1}|$$
Se $I_{t}\neq I_{t+1}$ allora esiste un nodo $v$ che adotta $A$ al passo $t+1$, e quindi $V_{t+1}\neq\emptyset$
- e per far si che un nodo $v$ appartenga a $V_{t+1}$ deve esistere $u\in N(v):u\in S_{t}$

E quindi, per ogni $v\in V_{t+1}$ esiste (almeno) un arco $(u,v)\in I_{t}$ tale che $u\in S_t$

Di conseguenza, per ogni nodo $v\in V_{t+1}$ abbiamo che:
- gli archi incidenti su $v$ il cui altro estremo è in $S_t$ sono $I_{t}$ e non $I_{t+1}$
- gli archi incidenti su $v$ il cui altro estremo non è in $S_{t+1}$ sono $I_{t+1}$ e non $I_{t}$

E quindi vale che: 
$$I_{t+1}=I_{t}\setminus\left[\bigcup_{v\in V_{t+1}}\{(u,v)\in E:u\in S_{t}\}\right]\cup\left[\bigcup_{v\in V_{t+1}}\{(z,v)\in E:z\in (V\setminus S_{t+1})\}\right]$$

![[Pasted image 20250812160807.png|center|350]]

Ora, se $v\neq z$ con $v,z\in S_t$ allora vale che $$\{(u,v)\in E:u\in S_{t}\}\cap\{(u,z)\in E:u\in S_{t}\}=\emptyset$$
e se $v\neq z$, con $v,z\in V_{t+1}$ allora vale che $$\{(u,v)\in E:u\in (V\setminus S_{t+1})\}\cap\{(u,z)\in E:u\in (V\setminus S_{t+1})\}=\emptyset$$
Allora, vale che 
$$
\begin{align*}
&\left|\bigcup_{v\in V_{t+1}}\{(u,v)\in E:u\in S_{t}\}\right|=\sum\limits_{v\in V_{t+1}}\left|\{(u,v)\in E:u\in S_{t}\}\right|\\&\left|\bigcup_{v\in V_{t+1}}\{(u,v)\in E:u\in (V\setminus S_{t+1})\}\right|=\sum\limits_{v\in V_{t+1}}\left|\{(u,v)\in E:u\in V\setminus S_{t+1}\}\right|\\
\end{align*}
$$
E quindi, vale che $$|I_{t+1}|=|I_t|-\sum\limits_{v\in V_{t+1}}\left|\{(u,v)\in E:u\in S_{t}\}\right|+\sum\limits_{v\in V_{t+1}}\left|\{(u,v)\in E:u\in V\setminus S_{t+1}\}\right|$$
Però vale che $$\begin{align*}
&\left|\{(u,v)\in E:u\in S_{t}\}\right|=|N(v)\cap S_t|\\&\left|\{(u,v)\in E:u\in V\setminus S_{t+1}\}\right|=|N(v)\setminus S_{t+1}|
\end{align*}$$[^4]

E quindi, rimodifichiamo ancora (dio porco un'altra dimostrazione infinita)
$$|I_{t+1}|=|I_t|-\sum\limits_{v\in V_{t+1}}\left|N(v)\cap S_{t}\right|+\sum\limits_{v\in V_{t+1}}\left|N(v)\setminus S_{t+1}\right|$$

Per ogni $v\in V_{t+1}$ deve valere che $$\begin{align*}
\frac{|N(v)\cap S_{t}|}{|N(v)|}&\geq q\gt \frac{1}{2}\\&\Downarrow\\|N(v)\cap S_{t}|&\gt|N(v)\setminus S_t|\\&\Downarrow\\|N(v)\setminus S_t|&\gt|N(v)\setminus S_{t+1}|\space(S_t\subset S_{t+1})\\&\Downarrow\\|N(v)\cap S_{t}|&\gt|N(v)\setminus S_{t+1}|
\end{align*}$$
Allora vale che: 
$$|I_{t+1}|=|I_t|-\sum\limits_{v\in V_{t+1}}\left(\left|N(v)\cap S_{t}\right|-\left|N(v) \setminus S_{t+1}\right|\right)\underbrace{\lt}_{\text{questo perchè }V_{t+1}\neq\emptyset\land S_t\subset S_{t+1}}|I_{t}|$$

Essendo che $V_{0}$ è un insieme finito e i nodi di $G$ hanno grado finito, allora l'interfaccia iniziale ha dimensione finita, e quindi $|I_0|=k$ per qualche $k\in\mathbb N$

Di conseguenza, l'eventualità $I_{t}\neq I_{t+1}$ non può verificarsi per più di $k$ passi [^5], e allora $$\exists T:\forall t\geq T\to I_{t}=I_{t+1}$$
- ovvero, al passo $T$ la diffusione termina

Ma in un grafo infinito una cascata completa può verificarsi solo in seguito a un processo di diffusione finito, allora $V_0$ non genera nessuna cascata completa, come volevasi dimostrare $\blacksquare$

### Nodi eterogenei

Il modello di diffusione considerato fino ad ora è un modello uniforme, ovvero tutti i nodi associano lo stesso beneficio reciproco nell'adottare $A$ o $B$, che è rispettivamente $a,b$

Tuttavia questo modello è poco realistico: ciascun individuo nella rete ha un proprio beneficio nell'adottare $A$ o $B$

Allora, per ogni nodo $u$ nella rete, $a_{u},b_u$ sono il beneficio che $u$ ottiene nel relazionarsi, rispettivamente, con un nodo che adotta $A$ o con un nodo che adotta $B$

Assumiamo che il beneficio sia quello illustrato in tabella

| $u/v$ | A           | B           |
| ----- | ----------- | ----------- |
| $A$   | $a_{u},a_v$ | $0,0$       |
| $B$   | $0,0$       | $b_{u},b_v$ |
Seguendo quindi la tabella, vale che un nodo $v\in V$ nello stato $B$ passa allo stato $A$ sulla base del valore $$q_{v}=\frac{b_v}{a_{v}+b_v}$$
Come vediamo in figura, accanto ad ogni nodo $v$ viene riportata la sua soglia di adesione $q_{v}$

![[Pasted image 20250813095703.png|center|300]]

**Oss**: Notiamo che, anche se il nodo $1$ è in posizione centrale, non riuscirebbe a portare nessun in $A$ a meno che $q_v=0.1$

Allora, **non è sufficiente scegliere gli iniziatori in base alla loro centralità nella rete**, ma occorre considerare anche la **loro possibilità di avere accesso a nodi facilmente influenzabili**

Quindi, come nel caso lineare precedente, definiamo la struttura che impedisce la generazione di una cascata completa

>[!definition]- Blocking Cluster
>$V\subseteq V'$ è detto **blocking cluster** se, per ogni $v\in V'$ vale che $$\frac{|N(v)\cap V'|}{|N(v)|}\geq1-q$$

Vale quindi il seguente teorema, di cui non daremo dimostrazione (o meglio, la dimostrazione è pressochè simile a questa [[Lezione 6 AR - Processi di diffusione, Cascate complete e clusters, Capacità di cascata di una rete e caratterizzazione dell'insieme di initiators#^953f09|dimostrazione]], e viene quindi lasciata come esercizio):

>[!teorem]- Teorema
>Sia $G=(V,E)$ un grafo.
>Nel modello a nodi eterogenei, l'insieme di iniziatori $V_{0}\subseteq V$ non genera una cascata completa se e solo se $G\setminus V_0$ contiene un blocking cluster

## Azione collettiva

Vogliamo ora mostrare come modellare, mediante processi di diffusione, situazioni nelle quali è richiesto che un'azione abbia luogo *collettivamente*

Supponiamo che si voglia organizzare una protesta contro un regime dittatoriale.

Ciascun individuo, ragionevolmente, decide di aderire alla protesta solo se sa con certezza che un numero sufficientemente elevato i individui aderirà alla protesta.

Poichè l'ambientazione è quella di una dittatura, possiamo ben pensare che la libertà di stampa sia ostacolata, e che in generale le comunicazioni siano rese difficoltose

La domanda è: perchè i regimi totalitari sono, generalmente, così interessati ad ostacolare le comunicazioni?

Analizziamo quindi il modello:

Ogni nodo $v$ sceglie una "soglia di confidenza" $k_v$ : aderirà alla protesta solo se almeno $k_{v}$ individui aderiranno alla protesta
- ovvero, se oltre a lui, aderiranno altri $k_v-1$ individui

Essendo che le comunicazioni circolano con difficoltà nella rete, le uniche informazioni che $v$ può ottenere sono circa l'adesione o meno alla protesta da parte degli individui con i quali ha una relazione personale, ovvero i suoi vicini nel grafo e, da ciascun nodo $u\in N(v),v$ può sapere quale sia la soglia di adesione di $u$ (assumendo che i collegamenti siano strong ties)

$v$ però non può sapere se $u$ ha o meno dei vicini che non siano anche suoi vicini, e non può neanche sapere se $u$ aderirà alla protesta

In base alle informazioni che $v$ possiede, può solamente provare a dedurre cosa faranno i suoi vicini

Vediamo qualche esempio

**Esempio 1**

![[Pasted image 20250813101448.png|center|250]]

- Il nodo $x$ non aderisce, non ha abbastanza vicini
- Il nodo $v$ ha bisogno di due vicini che aderiscono: ma vede che $x$ vuole almeno $3$ vicini aderiscano per aderire a sua volta, e poichè $v$ vede di $x$ i soli vicini che hanno in comune, non può sapere se $x$ aderirà o meno, e quindi non aderirà neanche lui
- Il nodo $u$ sarebbe sufficiente che uno solo dei suoi vicini aderisse. Per lo stesso ragionamento fatto da $v,u$ non può sapere se $x$ aderirà o meno. Inoltre, $u$ sa che $v$ ha bisogno di almeno due vicini che aderiscano per aderire, ma non può sapere se $v$ dispone di informazioni supplementari circa l'adesione di $x$: perciò non può dedurre che $v$ parteciperà. Di conseguenza, neanche $u$ aderisce 

**Esempio 2**

![[Pasted image 20250813102243.png|center|250]]

Questo caso è leggeremente più complicato.

Il nodo $u$ vede che $k_v=k_x=3$ e capisce che loro tre $(u,v,x)$ potrebbero aderire, ma $u$ non vede $y$, non sa se $v$ ha o meno altri vicini oltre a se stesso, e quindi non sa se $v$ può dedurre che almeno due dei suoi vicini aderiranno, e poichè $u$ ha bisogno di certezze, $u$ non aderisce

Essendo che il grafo è perfettamente simmetrico, nesuno aderisce alla protesta anche se, qualora avessero avuto accesso a informazioni complete, la protesta avrebbe avuto luogo

**Esempio 3**


![[Pasted image 20250813102718.png|center|250]]

I nodi $u,v,x$ si vedono l'un l'altro, così $u$ sa che $v,x$, per partecipare, hanno bisogno che altri due partecipino
Ma $u$ sa che anche $v,x$ sanno le stesse cose che sa lui, siamo quindi in una situazione "io so che tu sai che io so" (dio porco)

Essendo che si fidano l'un l'altro (strong ties) allora partecipano tutti e tre alla protesta, senza aver bisogno di conoscere altro della rete (sono quindi indipendenti da $y$)

Possiamo trarre le nostre conclusioni.

In assenza di comunicazioni adeguate che abbiano luogo nella rete, l'azione collettiva si verifica difficilmente:
- ecco perchè i regimi dittatoriali tendono a favorire l' ***ignorranza pluralistica***, che permette di concludere erroneamente che pochi individui abbiano una certa opinione, come nell'esempio blu

Invece, l'esempio rosso permette di osservare l'importanza di disporre di *una base di conoscenza comune*

## Diffusione in presenza di compatibilità

FIn'ora abbiamo considerato i due stati $A$ e $B$ mutualmente escusivi, ciascun nodo infatti o si trova in $A$ o in $B$. 

Tuttavia, nella realtà, non è infrequente che due stati possano coesistere.

D'ora in avanti, studieremo i processi di diffusione in presenza di compatibilità, ovvero quando un nodo può trovarsi in $A,B,AB$

In questo modello, chiamato modello a "nodi omogenei", i benefici del trovarsi in un certo stato dipendono soltanto dallo stato, e sono gli stessi per tutti i nodi

Naturalmente, un nodo adotta lo stato misto ($AB$) ogni qualvolta ne trae beneficio, ma allora la domanda sorge spontanea: perchè non adottare sempre lo stato misto?

La risposta è semplice e banale, adottare sempre lo stato misto ha un costo, ovvero il costo di adottare sia $A$ che $B$

In ogni caso, mentre i benefici che otteniamo dall'adottare lo stato $AB$ sono proporzionali al numero di vicini con i quali possiamo comunicare, il costo lo paghiamo una volta sola.

Sia $(u,v)$ un arco della rete: assumiamo che il beneficio reciproco di adottare $A,B,AB$ sia quello illustrato in tabella: 

| $u/v$ | A     | B     | AB                        |
| ----- | ----- | ----- | ------------------------- |
| $A$   | $a,a$ | $0,0$ | $a,a$                     |
| $B$   | $0,0$ | $b,b$ | $b,b$                     |
| $AB$  | $a,a$ | $b,b$ | $\max\{a,b\},\max\{a,b\}$ |

Invece, per il nodo $u$, il costo di $u$ di essere nello stato $AB$ è $c$

In definitiva, se $V_{A},V_{B},V_{AB}$ sono gli insiemi dei nodi che sono, rispettivamente, negli stati $A,B,AB$, con $V_{A}\cup V_{B}\cup V_{AB}=V$, allora il beneficio per un nodo $u$ di essere nello stato $AB$ è $$\sum\limits_{v\in V_{A}\cap N(u)}a+\sum\limits_{v\in V_{B}\cap N(u)}b+\sum\limits_{v\in V_{AB}\cap N(u)}\max\{a,b\}-c$$
E quindi, i benefici di stare in $A$ e $B$ sono rispettivamente $$\sum\limits_{v\in (V_{A}\cup V_{AB})\cap N(u)}a\land\sum\limits_{v\in (V_{A}\cup V_{AB})\cap N(u)}b$$
Assodato questo, ci proponiamo di studiare la capacità di cascata di una rete in presenza di compatibilità, e lo faremo solo:
- analizzando l'esempio particolare in cui $G$ è una catena infinita
- descrivendo i risultati di uno studio qualitativo nel caso bidimensionale ($G$ griglia)
- dimostrando che, nel caso unidimensionale l'andamento del processo di diffusione conferma quanto osservato dall'analisi qualitativa
- indicheremo con $p_{A}(u),p_{B}(u),p_{AB}(u)$ il beneficio del nodo $u$ nell'adottare, rispettivamente, $A,B,AB$

Vediamo quindi questa catena: $a=5,b=3,c=1$

Per simmetria, è sufficiente considerare una catena infinita solo a destra (sempre a DESTRA!!!), il cui primo nodo è nello stato $A$ (giallo) e tutti gli altri sono nello stato $B$ (blu)

![[Pasted image 20250813111920.png|center]]

Al primo passo, $u$ adotta $AB$ (verde): infatti $p_{A}(u)=5,p_{B}(u)=3,p_{AB}(u)=5+3-1=7$

![[Pasted image 20250813112103.png|center]]

Al secondo passo, $v$ adotta $AB$ (verde): infatti $p_{A}(v)=5,p_{B}(v)=3+3=6,p_{AB}(v)=5+3-1=7$

![[Pasted image 20250813112118.png|center]]

Al terzo passo, $z$ adotta $AB$ (verde) per le stesse motivazioni di $v$, ma ora ad $u$ conviene abbandonare $AB$ e tornare ad $A$ perchè: $p_{A}(u)=10,p_{B}(u)=0,p_{AB}(u)=5+5-1=9$

![[Pasted image 20250813112132.png|center]]

A questo punto, il fenomeno si ripete

![[Pasted image 20250813112145.png|center]]

E quindi, dopo un periodo transitorio durante il quale un nodo adotta lo stato misto, esso passerà ad adottare definitivamente il nuovo stato, e quindi si genera una cascata completa nella quale il vecchio stato viene completamente soppiantanto dal nuovo

Ricordiamo che, nel caso di esclusività fra $A$ e $B$, la soglia di adozione $q$ era definita come $q=\frac{b}{a+b}$
- esso rappresenta la frazione minima dei vicini di un nodo che deve essere nello stato $A$ per convincere quel nodo a passare allo stato $A$
- dalla definizione possiamo dividere numeratore e denominatore per $b$ ed ottenere che $$q=\frac{1}{\frac{a}{b}+1}$$

Sempre nel caso di esclusività, avevamo dimostrato che **non si può generare una cascata completa (in un grafo infinito) se $q\gt \frac{1}{2}$**

Cosa possiamo dire nel caso di compatibilità fra $A$ e $B$?

Intanto, osserviamo che l'operazione di dividere per $b$ che abbiamo poc'anzi effettuato ha permesso di risursi a studiare i processi di diffusione in funzione del solo parametro $\frac{a}{b}$ invece che dei due parametri $a,b$, e questo è equivalente a fissare $b=1$ e studiare i processi in funzione di $a$

Analogamente, nel caso della compatibilità fra $A$ e $B$, possiamo fissare $b=1$ e studiare i processi in funzione di $a,c$

Uno studio qualitativo `[Kleinberg et al. 2007]` ha evidenziato uno "strano" comportamento:
- lo stato $A$ si impone quando $a\gt\gt c$ - ed è ovvio
- lo stato $A$ fa fatica ad imporsi quando $c\gt\gt a$ - e anche questo è ragionevole
- lo stato $A$ **fa fatica ad imporsi anche quando** $c$ non è né troppo grande né troppo piccolo rispetto ad $a$ - e questo è strano

Torniamo a considerare la catena

![[Pasted image 20250813121331.png|center]]

Se $x$ è nello stato $A$ (giallo) e $v$ nello stato $B$ (blu), al nodo $u$ quale stato converrà adottare?
Dato che $$p_{A}(u)=a,p_{B}(u)=1,p_{AB}(u)=a+1-c$$
possono accadere $3$ situazioni:
- se $p_{A}(u)\geq p_{B}(u)$ e $p_{A}(u)\geq p_{AB}(u)$ allora $u$ adotterà $A$
	- questo accade quando $a\geq1$ e $a\geq a+1-c$
		- quindi quando $a\geq1\land c\geq1$
- se $p_{B}(u)\gt p_{A}(u)$ e $p_{B}(u)\gt p_{AB}(u)$ allora $u$ rimarrà in $B$
	- questo accade quando $1\gt a$ e $1\gt a+1-c$
		- quindi quando $a\lt1\land a\lt c$
- se $p_{AB}(u)\gt p_{A}(u)$ e $p_{AB}(u)\gt p_{B}(u)$ allora $u$ adotterà $AB$
	- questo accade quando $a+1-c\gt a$ e $a+1-c\geq 1$
		- quindi quando $c\lt1\land a\geq c$

Riassumiamo tutto ciò in un grafico nel piano $ac$







[^1]: talvolta modificandone il comportamento, come visto nell'esperimento di Ganovetter

[^2]: non c'è coalizione di gruppi di nodi per prendere collettivamente la stessa decisione

[^3]: grafo regolare: un grafo in cui ogni nodo ha lo stesso numero di vicini di ogni altro nodo. Es: $3$-regolare $\to$ tutti i nodi hanno grado $3$

[^4]: questo perchè $\forall v\in V_{t+1},(u,v)\in I_{t}\iff u\in N(v)\cap S_t$, e $(u,v)\in I_{t+1}\iff u\in N(v)\setminus S_t$

[^5]: perchè ogni volta che $I_{t}\neq I_{t+1}$ è anche $|I_{t}|\gt|I_{t+1}|$, e la dimensione dell'interfaccia non può essere $lt0$