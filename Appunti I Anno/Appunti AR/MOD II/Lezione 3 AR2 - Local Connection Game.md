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
# Local Connection Game

Definiamo informalmente cos'è un LCG 
- Un LCG è un gioco che modella la **creazione di reti**
- ci sono 2 problemi principali: i giocatori vogliono
	- ridurre al minimo i costi sostenuti per la realizzazione della rete
	- garantire che la rete offra loro un'elevata qualità del servizio
- i giocatori sono nodi che:
	- pagano per i links
	- beneficiano degli short paths
## Il modello

Definiamo ora, formalmente, il modello LCG:

**input**:
- $n$ giocatori: nodi del grafo da costruire
- **Strategia** per il giocatore $u$: insieme di archi **non diretti** che $u$ costruirà (tutti ***incidenti*** ad $u$)
- Dato un vettore di strategie $S$, la **rete costruità** verrà denominata con $G(S)$
	- in questa rete $\exists$ arco non diretto $(u,v)$ se viene acquistato da $u$, da $v$ oppure da entrambi

**Goal del giocatore** $u$:
- rendere la distanza fra lui e gli altri giocatori **piccola**
- pagare il meno possibile

Vediamo inoltre che ogni arco costa $\alpha$

La distanza tra $u$ e $v$, denominata con $dist_{G(S)}(u,v)$ è pari alla lunghezza (in termini di numero di archi usati) dello **shortest path** fra i due nodi

Quello che il player $u$ vuole fare è minimizzare il suo costo, espresso con la formula:
$$\boxed{cost_u(S)=\underbrace{\alpha\cdot n_u}_{\text{costo di costruzione}}+\underbrace{\sum\limits_{v\in V}dist_{G(S)}(u,v)}_{\text{costo di utilizzo}}}$$
dove $n_{u}$ è definito come il **numero di archi in possesso** del nodo $U$

Come abbiamo fatto per i NFG, ricordiamo che:
- Useremo l'equilibrio di Nash (NE) come concept della soluzione
- Per valutare la qualità generale della rete, consideriamo il **costo sociale**, come ad esempio la somma dei costi di tutti i giocatori (indicato con $SC(S)$)
- Diremo che una rete si dice **ottimale** o **socialmente efficiente** se minimizza il costo sociale
- Diremo inoltre che un grafo $G=(V,E)$ si dice **stabile** (per un valore $\alpha$) se esiste un vettore di strategie $S$ tale per cui:
	- $S$ è un NE
	- $S$ crea $G$

**Esempio**

Consideriamo il seguente grafo diretto, con nodo $u$ quello segnato in giallo

![center|400](img/Pasted%20image%2020260327105911.png)

Vediamo subito che, se la strategia del nodo $u$ prevede l'utilizzo solamente dell'arco a lui subito sotto, allora il nodo $u$ dovrò pagare
$$cost_u(S)=\alpha\cdot 1+\sum\limits_{v\in V\setminus u}dist_{G(S)}(u,v)\equiv\alpha+13$$

![center|400](img/Pasted%20image%2020260327160657.png)

Se invece il nodo $u$ decide di **costruire** un'altro arco (quello con $\alpha$ in rosso), allora:
- si riaggiornano le distanze, adesso il nodo $u$ arriva al nodo $4$ usando un solo arco, quindi la distanza da $u$ a quel nodo non sarà più $4$ ma diventerà $1$
	- stessa cosa per l'altro nodo con $-1$
- si riaggiorna il $cost_u(S)$ considerando l'utilizzo dell'altro arco ($\alpha$ rosso)

Il costo per il nodo $u$ diventa quindi:
$$cost_u(S)=2\alpha+9$$

![center|400](img/Pasted%20image%2020260327160941.png)

Possiamo quindi dare alcune semplici osservazioni
1. In $SC(S)$ ogni termine $dist_G(S)(u,v)$ contribuisce **due volte** alla qualità generale
2. In una rete stabile ogni arco $(u,v)$ viene acquistato da al massimo **un giocatore**
3. Qualsiasi rete stabile deve essere connessa
	1. questo è ovvio se pensiamo al fatto che, in caso contrario, la distanza fra un nodo $u$ e un nodo $v$ potrebbe essere $\infty$

Da queste 3 osservazioni possiamo quindi dedurre che:

>il **costo sociale** di una rete *stabile* $G(S)=(V,E)$ può essere definito come:
>$$SC(S)=\alpha|E|+\sum\limits_{(u,v)}dist_{G(S)}(u,v)$$

A questo punto possiamo definire qual'è il nostro goal.

Il nostro goal è quindi quello di **limitare** la perdità di efficienza derivata dalla stabilità; in particolare, vogliamo stimare quanto valgono il PoS e il PoA
## Come appare una rete ottimale?

Prima di dare dei bound alle due metriche PoS e PoA, quello che dobbiamo cercare di capire è: **come deve essere fatta una rete stabile?**

Prima di rispondere alla domanda facciamo un piccolo recap di alcune topologie di grafi

**Grafo Completo** : Si indica con $K_n$ e rappresenta un grafo dove ogni nodo $i$ è connesso ad ogni altro nodo $j$ con $j\neq i$

![center|200](img/Pasted%20image%2020260327162710.png)

**Grafo a Stella** : Albero (ergo grafo connesso e aciclico) la cui altezza è al più $1$

![center|200](img/Pasted%20image%2020260327162818.png)

Perfetto, a questo punto possiamo dare l'enunciato e la dimostrazione del seguente lemma, che ci servirà per rispondere alla domanda iniziale (insieme ad un'altro lemma)

>[!teorem]- Lemma 1
>Se $\alpha\leq2$ allora il grafo completo è la soluzione ottimale, mentre se $\alpha\geq2$ allora una *qualunque* stella è soluzione ottimale

**dimostrazione lemma 1**

Prendiamo $G=(V,E)$ un grafo con $|E|=m$ archi

Allora possiamo scrivere il costo sociale relativo a questo grafo come:
$$\boxed{SC(G)\geq \alpha\cdot m+2m+2(n(n-1)-2m)=\underbrace{(\alpha-2)m+2n(n-1)}_{LB(m)}}$$

Osserviamo che : 
$$LB(m)=\begin{cases}SC(K_n)&m=\frac{n(n-1)}{2} \\
SC(\text{any star)}&m=n-1\end{cases}$$

Okay, a questo punto allora possiamo affermare che:
$$\boxed{OPT\geq \min_{m}LB(m)\geq\begin{cases}LB(n-1)=SC(\text{any star)}&\alpha\geq2\\LB\left(\frac{n(n-1)}{2}\right)=SC(K_{n})&\alpha\leq2\end{cases}}$$

Possiamo inoltre affermare che, nella formula di cui sopra, quando abbiamo $\alpha\geq2$ il problema diventa un problema di ***minimizzazione del fattore*** $m$, quando invece $\alpha\leq2$ diventa ***massimizzazione del fattore*** $m$ $\blacksquare$

A questo punto, ci sorge spontanea un' altra domanda: ma il grafo completo e la stella sono stabili?

Per rispondere a questa domanda introduciamo e dimostriamo il seguente lemma

>[!teorem]- Lemma 2
>Se $\alpha\leq1$ il grafo completo è stabile, se $\alpha\geq1$ allora una qualunque stella è stabile

**dimostrazione lemma 2**

***caso*** $\alpha\leq1$

Prendiamo ad esempio il seguente grafo completo

![center|200](img/Pasted%20image%2020260327165159.png)

**Perché nessuno vuole deviare?** Immagina che un nodo $v$ decida di risparmiare sui costi di costruzione eliminando $k$ archi che aveva comprato.

- **Quanto risparmia in costruzione?** Risparmia esattamente $\alpha k$.
- **Quanto ci perde in distanza?** Per i $k$ nodi a cui si è disconnesso, la distanza non è più 1. Nel migliore dei casi possibili (assumendo che il grafo resti connesso tramite altri nodi), la nuova distanza verso questi $k$ nodi sarà _almeno_ 2. Quindi il costo di distanza aumenta di almeno $(2-1)=1$ per ciascuno di questi $k$ nodi. L'aumento totale del costo di routing è $\geq k$.

Il bilancio totale per il nodo $v$ (variazione di costo) è: $-\alpha k+k=k(1-\alpha)$. Poiché siamo nell'ipotesi $\alpha\leq1$, la quantità ($1-\alpha$) è $\geq0$. Quindi la variazione di costo è sempre positiva o nulla (il costo aumenta o resta uguale, non diminuisce mai). Nessun nodo può migliorare la propria situazione rimuovendo archi. **Il grafo completo è stabile.**

***caso*** $\alpha\geq1$

Prendiamo ad esempio il seguente grafo a stella, dove $c$ è il centro e $v$ le foglie (che comprano archi verso il centro)

![center|200](img/Pasted%20image%2020260327165510.png)

Le foglie comprano un solo arco verso il centro. La distanza foglia-centro è $1$, la distanza foglia-foglia è $2$ (passando per il centro).

Dobbiamo dimostrare che né il centro né le foglie vogliono cambiare strategia.

**1. Il nodo centrale $c$ non ha interesse a deviare:** Il centro è già a distanza $1$ da tutti gli altri nodi. Non compra nessun arco (sono le foglie che puntano a lui). Non potendo rimuovere archi (ne compra 0) e non potendo migliorare le sue distanze (sono già al minimo possibile), la sua strategia è già ottima.

**2. I nodi periferici $v$ non hanno interesse a deviare:** Cosa succede se una foglia $v$ decide di comprare $k$ nuovi archi diretti verso altre foglie? (le frecce rosse).

- **Quanto paga in più?** Paga il costo di costruzione per i nuovi archi: $\alpha k$.
- **Quanto risparmia in distanza?** Prima, per raggiungere quelle $k$ foglie, ci metteva 2 passi (passando per il centro). Ora ci mette 1 passo (diretto). Il risparmio sulla distanza è esattamente di 1 passo per ogni nodo, quindi risparmia un totale di $k$.

Il bilancio totale per il nodo $v$ è: $\alpha k-k=k(\alpha -1)$. Poiché siamo nell'ipotesi $\alpha\geq1$, la quantità ($\alpha-1$) è $\geq0$. Anche in questo caso, la variazione del costo totale è positiva o nulla. Comprare nuovi archi non porta a un risparmio netto. Allo stesso modo, rimuovere l'unico arco verso il centro lo disconnetterebbe dalla rete (costo di distanza infinito). Nessuna foglia vuole deviare. **La stella è stabile** $\blacksquare$
### PoS: Upper Bound

Possiamo quindi calcolare quanto vale il PoS, grazie al seguente teorema

>[!teorem]- Teorema PoS
>Quando $\alpha\leq1$ e $\alpha\geq2$ il PoS è $1$.
>Quando $1\lt\alpha\lt2$ il PoS è al più $\frac{4}{3}$
>

**dimostrazione teorema**

La dimostrazione la dividiamo in 2 casistiche

**I casi "Trivial"** ($\alpha\leq1$ e $\alpha\geq2$)

Perché sono banali? Perché in questi scenari **l'Ottimo Sociale coincide con un Equilibrio di Nash**. Se l'assetto migliore in assoluto è anche stabile, nessuno ha incentivo a deviare dal massimo bene comune. Quindi la frazione $\frac{SC(Miglior_{NE})}{SC(OPT)}$ è esattamente **1**.

- **Per** $\alpha\leq1$: Gli archi costano pochissimo. L'Ottimo Sociale è il Grafo Completo ($K_n$​), perché conviene a tutti essere connessi a tutti. Come abbiamo visto nel lemma precedente, se $\alpha\leq1$ il grafo completo è stabile (è un NE). Quindi ***PoS = 1***.
- **Per** $\alpha\geq2$: Gli archi costano tantissimo. Creare un arco costa $\alpha\geq2$, ma fa risparmiare solo 2 di distanza globale (1 per l'andata, 1 per il ritorno tra i due estremi). Quindi l'Ottimo Sociale è costruire il numero minimo assoluto di archi per tenere il grafo connesso minimizzando le distanze: ovvero una Stella ($T$). Sappiamo già che per $\alpha\geq1$ la stella è stabile. Quindi ***PoS = 1***.

**Il caso intermedio** ($1\lt\alpha\lt2$)

Qui le cose si fanno interessanti.

- **L'Ottimo Sociale (OPT) è ancora il Grafo Completo** $(K_{n})$ Perché? Perché il costo di un arco è $\alpha\lt2$. Aggiungere un arco costa meno di 2, ma risparmia 2 in termini di distanze sociali. Quindi per la "società" conviene sempre aggiungerlo.
- **L'Equilibrio di Nash.** Sappiamo però che per $\alpha\gt1$ i giocatori egoisti _non_ formeranno un grafo completo (costa troppo individualmente), ma formeranno reti a Stella ($T$), che abbiamo dimostrato essere stabili.

Quindi per calcolare un limite superiore al PoS, possiamo valutare il rapporto tra il Costo Sociale di una stella $SC(T)$ e il Costo Sociale del grafo completo $SC(K_{n}​)$.

Vale quindi la seguente formula:

$$\boxed{\begin{align*}
PoS&\leq\frac{SC(T)}{SC(K_{n})}=\underbrace{\frac{(\alpha-2)(n-1)+2n(n-1)}{\alpha\left(\frac{n(n-1)}{2}\right)+n(n-1)}}_{\text{max. con }\alpha=1}\leq\frac{-1(n-1)+2n(n-1)}{\frac{n(n-1)}{2}+n(n-1)}\\
&=\frac{2n-1}{\frac{3n}{2}}=\frac{4n-2}{3n}\lt \frac{4}{3}\quad\blacksquare
\end{align*}}$$
### PoA : Upper Bound

Dopo aver calcolato il bound per il PoS, passiamo a calcolare quello per il PoA.

>Prima di tutto notiamo che, quando $\alpha\lt1$ allora l'unica rete stabile è il grafo completo, e di conseguenza il PoA è $1$ ([dimostrazione formale](#^c0ae07))

Andiamo avanti con il calcolo del PoA, richiamando alcuni concetti di Algoritmi e Strutture Dati

Prima di tutto ricordiamo la definizione di **diametro**:

>[!definition]- Diametro
>Il **diametro** di un grafo $G$ è definito come la massima distanza tra una qualunque coppia di nodi

Alcuni esempi:
![center|400](img/Pasted%20image%2020260328111714.png)

Ricordiamo anche la definizione di **arco di taglio (cut-edge)**

>[!definition]- Cut-Edge
>Un arco $e$ viene definito **cut-edge** di un grafo $G$ se il grafo $G-e=(V,E\setminus{e})$ risulta sconnesso
>(sostanzialmente, se togliamo l'arco $e$ in question eil grafo risultante non è più connesso)

**Semplice proprietà** : in un grafo $G$ ci sono al puù $n-1$ archi di taglio

Dopo aver fatto questi richiami, possiamo definire il teorema principale per il bound del PoA

>[!teorem]- Teorema PoA
>Il PoA è al più $O(\sqrt{\alpha})$

**dimostrazione teorema**

La dimostrazione del teorema seguendalla dimostrazione dei seuguenti lemmi

>[!teorem]- Lemma 1
>Il diametro di una qualunque rete stabile è al più $2\sqrt{\alpha}+1$

>[!teorem]- Lemma 2
>Il SC di una qualunque rete stabile con diametro $d$ è al più $O(d)$ volte il SC ottimale

**dimostrazione lemma 1**

Prendiamo $G$ una rete stabile, e consideriamo lo shortest path fra due nodi $(u,v)$
Per semplicità di trattazione, assumiamo inoltre che
$$2k\leq dist_{G}(u,v)\leq 2k+1\quad\text{per qualche }k$$

![center|500](img/Pasted%20image%2020260328113553.png)

Cosa succederebbe se il nodo $u$ decidesse di deviare dalla sua strategia attuale e **comprasse un arco diretto** verso $v$ (la freccia rossa in alto)?

- **Il Costo:** Pagherebbe il prezzo di un nuovo arco, ovvero $\alpha$.
- **Il Beneficio:** Risparmierebbe un sacco di distanza non solo per raggiungere $v$, ma per raggiungere _tutti i nodi vicini a $v$_ su quel cammino.

![center|500](img/Pasted%20image%2020260328113327.png)

Concentriamoci sugli **ultimi $k$ nodi** di questo cammino. 
Guardiamo quanto risparmia $u$ per raggiungerli usando la scorciatoia diretta per $v$ e poi tornando indietro lungo il cammino

- **Per arrivare a v:** Prima la distanza era $\geq2k$. Col nuovo arco, la distanza è 1.
    - _Risparmio:_ $\geq(2k-1)$
- **Per arrivare al nodo subito prima di $v$:** Prima la distanza era $\geq2k-1$. Col nuovo arco, $u$ salta a $v$ (1 passo) e poi fa un passo indietro verso quel nodo (1 passo), per un totale di distanza 2.
    - _Risparmio:_ $\geq(2k-1)-2=2k-3$
- ...questo ragionamento continua a scendere...
- **Per arrivare al $k$-esimo nodo (partendo dal fondo):** Prima la distanza era $\geq k+1$. Con la scorciatoia, $u$ salta a $v$ e fa ($k-1$) passi indietro, per un totale di distanza $k$.
    - _Risparmio:_ $\geq(k+1)-k=1$

Il risparmio totale garantito per $u$ (guardando _solo_ questi ultimi $k$ nodi) è la somma di tutti i dispari decrescenti:
$$(2k-1)+(2k-3)+\dots+3-1$$

Per sommarli tutti usiamo una nota proprietà matematica: la somma dei primi $k$ numeri dispari è esattamente $k^2$.
$$\sum\limits_{i=0}^{k-1}(2i+1)=k^{2}$$

![center|500](img/Pasted%20image%2020260328113631.png)

A questo punto sfruttiamo il fatto che la rete sia stabile

In un Equilibrio di Nash, il nodo $u$ _non deve avere alcun incentivo_ a comprare quell'arco. Se non lo compra, significa che il costo dell'arco ($\alpha$) deve essere per forza maggiore o uguale al risparmio che ne trarrebbe (altrimenti sarebbe stupido a non comprarlo!). Di conseguenza, otteniamo la disequazione
$$\alpha\geq k^2\implies k\leq\sqrt{\alpha}$$

A questo punto, riprendendo l'assunzione iniziale sulla lunghezza del cammino fra $(u,v)$ e sostituendo il valore di $k$ appena trovato otteniamo
$$dist_{G}(u,v)\leq2k+1\implies dist_{G}\leq2\sqrt{\alpha}+1\quad\blacksquare$$

A questo punto procediamo con la dimostrazione ( o meglio con lo scheletro della dimostrazione) per il lemma 2

**dimostrazione lemma 2**

La dimostrazione è divisa in due grandi fasi: prima si trova un limite inferiore per l'Ottimo (quanto costa come minimo la rete perfetta?), e poi si analizzano le singole componenti del Costo Sociale della nostra rete stabile $G$.

**Il limite inferiore per l'Ottimo (OPT)**

La prima parte stabilisce quanto deve costare, _come minimo assoluto_, l'Ottimo Sociale.

- **Costo degli archi:** Qualsiasi rete connessa con $n$ nodi deve avere almeno $n-1$ archi (un albero di copertura). Quindi, spenderà almeno $\alpha(n-1)$ per la costruzione.
- **Costo delle distanze:** Ci sono $n(n-1)$ coppie ordinate di nodi. La distanza minima possibile tra due nodi distinti è 1. Quindi, la somma minima di tutte le distanze è $n(n-1)$, che è nell'ordine di grandezza di $n^2$.

Di conseguenza, il costo minimo assoluto dell'ottimo sociale sarà
$$OPT\geq\alpha(n-1)+n(n-1)$$

Di conseguenza, evidenziamo due fatti cruciali: 

1. $OPT\geq\alpha(n-1)$
2. $OPT=\Omega(n^2)$ _(cioè, il valore di OPT cresce almeno tanto velocemente quanto $n^2$)_.

**Scomposizione del Costo Sociale di $G$ ($SC(G)$)**

Ora prendiamo la nostra rete stabile $G$. Il suo Costo Sociale è la somma delle distanze più il costo degli archi:
$$SC(G)=\sum\limits_{u,v}dist_{G}(u,v)+\alpha|E|$$

Per analizzare gli archi $|E|$, dividiamo in due insiemi:

- $E_{cut}$: Sono gli archi che formano l'albero di copertura della rete (il "cuore" vitale per mantenerla connessa). Essendo un albero, sono esattamente $n-1$.
- $E_{non-cut}$​: Sono tutti gli _altri_ archi, quelli extra che creano cicli e servono solo come "scorciatoie".

A questo punto possiamo riscrivere $SC(G)$ come 
$$SC(G)=\underbrace{\sum\limits_{u,v}dist_{G}(u,v)}_{(A)}+\underbrace{\alpha|E_{cut}|}_{(B)}+\underbrace{\alpha|E_{non-cut}|}_{(C)}$$

Analizziamo ora quanto valgono i tre blocchi

**Blocco** $(A)$

Sappiamo che la distanza massima (il diametro) è $d$.
Ci sono circa $n^2$ coppie di nodi.
Quindi, nel caso peggiore, la somma di _tutte_ le distanze è al massimo $d\cdot n^2$, ovvero $O(dn^2)$.

Ma noi sappiamo che $n^2$ è proporzionale a OPT (poiché $OPT=\Omega(n^2)$). Quindi, possiamo riscrivere $O(dn^2)$ come $$O(d)\cdot OPT$$

**Blocco** $(B)$

Questi archi sono al massimo $n-1$. Il loro costo totale è $\leq\alpha(n-1)$.
Guardando di nuovo il punto 1, sappiamo che $\alpha(n-1)\leq OPT$.

Quindi, il costo di questa parte è $\leq OPT$ (che è ovviamente assorbito in un $O(d)\cdot OPT$).

**Blocco** $(C)$

Il _numero_ di archi extra ($|E_{non-cut}​|$) è limitato da $O\left(\frac{n^{2}d}{\alpha}\right)$. ("***tricky bound, vedi giù per dimostrazione***; nel dettaglio [prop1](#^eb940c)+[prop2](#^17521e) ")
Per sapere il loro _costo_, dobbiamo moltiplicare questo numero per $\alpha$:
$$\alpha\cdot O\left(\frac{n^{2}d}{\alpha}\right)=O(n^2d)$$

Ancora una volta, poiché $\Omega(n^2)$ è contenuto in OPT, possiamo sostituire $n^2$ ottenendo di nuovo $O(d)\cdot OPT$.

Se sommiamo i risultati dei tre blocchi:
$$SC(G)\leq O(d)\cdot OPT+OPT+O(d)\cdot OPT=O(d)\cdot OPT\quad\blacksquare$$

Il Costo Sociale della nostra rete stabile non sarà mai superiore all'Ottimo moltiplicato per l'ordine di grandezza del suo diametro.

Questa però non era la dimostrazione ufficiale per il Lemma 2; prima di dimostrare formalmente il Lemma 2 introduciamo (e dimostriamo) due proposizioni (sono quelle che ci serviranno per definire il "tricky bound" correttamente)

>[!teorem]- Proposizione 1
>Sia $G$ una rete con diametro $d$, e sia $e=(u,v)$ l'arco non-cut. 
>Allora in $G-e$, ogni nodo $w$ aumenta la sua distanza da $u$ al più di un fattore $2d$

^eb940c

**dimostrazione prop. 1**

L'idea è: se io tolgo un arco che _non_ è vitale per la connessione (un arco non-cut), di quanto peggiorano le distanze nella rete rimanente?

La dimostrazione si basa sulla costruzione di un **BFS tree** (Breadth-First Search tree, ovvero un albero dei cammini minimi) a partire dal nodo $u$.

Vediamo quindi la dimostrazione passo passo

**step 1: setup**

Abbiamo un grafo. Il nodo in alto è $u$. L'albero disegnato con le linee continue è il BFS tree radicato in $u$. Questo albero contiene i cammini minimi da $u$ a tutti gli altri nodi.

Le linee tratteggiate sono gli archi "extra" del grafo, quelli che non fanno parte dell'albero BFS.

Consideriamo un arco specifico $e=(u,v)$ che fa parte del BFS tree. Se questo arco viene rimosso, l'albero si spezza in due componenti.

$w$ è un nodo qualsiasi che si trova nel sottoalbero radicato in $v$ (cioè, il cammino minimo da $u$ a $w$ passava per $e$).

![center|400](img/Pasted%20image%2020260328145026.png)

**step 2: Il Taglio e l'Arco Alternativo**

Rimuoviamo l'arco $e$ (indicato dalle due sbarrette rosse). Questo crea un "taglio" (cut) nel grafo, separando la componente di $u$ (a destra) dalla componente di $v$ (a sinistra).

Poiché sappiamo per ipotesi che e è un "arco non-cut" del grafo _originale_ $G$ (cioè la sua rimozione non disconnette l'intero grafo), **deve esistere per forza almeno un altro arco** che collega la componente di destra con quella di sinistra.

Questo arco alternativo è l'arco $(x,y)$ (la linea tratteggiata rossa), dove $x$ è nella componente di $u$ e $y$ è nella componente di $v$.

![center|500](img/Pasted%20image%2020260328145218.png)

**step 3: Il Nuovo Cammino Minimo (La Dimostrazione)**

Ora dobbiamo valutare la nuova distanza tra $u$ e $w$ nel grafo senza l'arco $e$, ovvero $dist_{G-e}​(u,w)$. Visto che l'arco $(u,v)$ non c'è più, per andare da $u$ a $w$ dobbiamo usare il "ponte" alternativo $(x,y)$. Il nuovo cammino (evidenziato in rosso) sarà:

1. Da $u$ a $x$.
2. Da $x$ a $y$ (attraverso l'arco).
3. Da $y$ a $v$.
4. Da $v$ a $w$.

La formula in basso calcola la lunghezza massima di questo nuovo cammino:

$$dist_{G-e}​(u,w)\leq dist_G​(u,x)+1+dist_G​(y,v)+dist_G​(v,w)$$

Analizziamo i singoli pezzi rispetto alla distanza originale $dist_G​(u,w)$:

- $dist_G​(u,x)\leq d$: La distanza originale tra $u$ e $x$ non può superare il diametro della rete $d$.
- $1$: È il costo di attraversare l'arco $(x,y)$.
- $dist_G​(y,v)\leq d$: La distanza originale tra $y$ e $v$ non può superare il diametro della rete $d$.
- $dist_G​(v,w)=dist_G​(u,w)-1$: Poiché $w$ è nel sottoalbero di $v$, il cammino originale da $u$ a $w$ era semplicemente l'arco $(u,v)$ (lungo 1) più il cammino da $v$ a $w$. Quindi, la distanza da $v$ a $w$ è esattamente la distanza da $u$ a $w$ meno 1.

Sostituendo queste maggiorazioni nella formula, otteniamo:

$$dist_{G-e}​(u,w)\leq d+1+d+(dist_G​(u,w)-1)$$

I due $+1$ e $-1$ si annullano, e ci rimane:

$dist_{G-e}​(u,w)\leq dist_G​(u,w)+2d$

Abbiamo dimostrato che se togliamo un arco "inutile" per la connettività globale ($e$), la distanza da $u$ a qualsiasi nodo $w$ che prima usava quell'arco aumenterà al massimo di un addendo pari a $2d$. $\blacksquare$

Passiamo ora alla seconda proposizione

>[!teorem]- Proposizione 2
>Sia $G$ una rete stabile, e sia $F$ l'insieme degli archi di tipo non-cut pagati da un nodo $u$
>Allora, vale che $$|F|\leq\frac{2d(n-1)}{\alpha}$$

^17521e

**dimostrazione prop. 2**

Questo lemma serve a calcolare **quanti "archi extra" (non-cut) un singolo giocatore $u$ è disposto a pagare** in una rete che si trova in un Equilibrio di Nash. L'intuizione è che, siccome gli archi costano $\alpha$, un giocatore ne comprerà tanti solo se servono a raggiungere velocemente un gran numero di nodi.

Analizziamo la dimostrazione passo dopo passo:

**step1 : Setup**

Guardiamo la rete dal punto di vista del nodo $u$.

- Chiamiamo $F$ l'insieme degli archi _non-cut_ che il nodo $u$ ha deciso di comprare. Il numero di questi archi è $k=|F|$.
- Nella figura di cui sotto, questi archi vanno da $u$ ai nodi $v_1​,\dots,v_i​,\dots,v_k​$.
- Se guardiamo l'albero dei cammini minimi (BFS tree) radicato in $u$, ogni nodo $v_i$​ è la radice di un "sottoalbero". Chiamiamo $n_i$​ il numero totale di nodi contenuti nel sottoalbero di $v_i$​. Questo significa che, per raggiungere quegli $n_i​$ nodi, il cammino più breve per $u$ passa proprio per l'arco $(u,v_i​)$.

![center|500](img/Pasted%20image%2020260328150910.png)

**step 2: La Deviazione: Cosa succede se $u$ taglia un arco?**

Immaginiamo la solita dinamica da Game Theory: il giocatore egoista $u$ valuta se gli conviene smettere di pagare per un certo arco $(u,v_i​)$.

- **Quanto risparmia?** Risparmia esattamente il costo di costruzione: $\alpha$.
- **Quanto ci perde in distanze?** Qui usiamo la **Proposizione 1**. Sappiamo che rimuovendo un arco non-cut, la distanza verso un qualsiasi nodo penalizzato aumenta al massimo di $2d$. Poiché i nodi penalizzati rimuovendo $(u,v_i​$) sono gli $n_i$​ nodi del suo sottoalbero, l'aumento totale del costo di routing per $u$ sarà al massimo $2d\cdot n_i​$.

**step 3: La Condizione di Stabilità**

Poiché sappiamo per ipotesi che la rete $G$ è stabile (Equilibrio di Nash), la deviazione _non deve_ convenire a $u$. Il risparmio deve essere minore o uguale al danno subito. Si genera così la disequazione per un singolo arco $i$:
$$\alpha\leq2d\cdot n_i​$$

Questa regola vale per _tutti_ i $k$ archi non-cut pagati da $u$. Se sommiamo le disequazioni di tutti i $k$ sottoalberi, otteniamo:

$$k\cdot\alpha\leq2d\sum\limits_{i=1}^{k}n_{i}​$$
>[!warning]- Attenzione
>Ora, riflettiamo su quel termine $\sum\limits_{i=1}^{k}n_{i}​$​. Rappresenta la somma dei nodi di tutti i sottoalberi. Poiché questi sottoalberi sono rami separati dell'albero BFS originato da $u$, la somma dei loro nodi non può fisicamente superare il numero totale di _tutti gli altri nodi_ della rete (escluso $u$). Quindi, sappiamo con certezza che $\sum\limits_{i=1}^{k}n_{i}​\leq n-1$.

Sostituendo questo limite massimo nella disequazione otteniamo:

$$k\cdot\alpha\leq2d(n-1)\implies k\leq(n-1)\frac{2d}{\alpha}\quad\blacksquare$$

Abbiamo appena dimostrato che un _singolo_ nodo compra al massimo $\approx\frac{2dn}{\alpha}$​ archi extra. Se moltiplichiamo questo valore per tutti gli $n$ nodi della rete, il numero totale di archi extra nell'intera rete ($|E_{non-cut​}|$) sarà limitato da $O\left(\frac{n^{2}d}{\alpha}​\right)$, che è proprio il "tricky" bound visto prima.

A questo punto, siamo pronti a finire la dimostrazione **formale** del lemma $2$

**dimostrazione formale lemma 2**

Prima di tutto ricordiamo quanto deve valere l'ottimo
$$OPT\geq\alpha(n-1)+n(n-1)$$

Guardiamo la prima parte della formula del Costo Sociale di G: $\sum\limits_{u,v}​dist_G​(u,v)$

- Sappiamo che la distanza massima tra due nodi qualsiasi in $G$ è il diametro $d$.
- Ci sono $n(n−1)$ coppie di nodi (considerando i percorsi in entrambe le direzioni).
- Quindi, la somma massima di tutte le distanze è $d\cdot n(n-1)$.
- Poiché sappiamo che il termine $n(n-1)$ fa parte dell'OPT, possiamo limitare tutto questo dicendo che il costo delle distanze è $\leq d\cdot OPT$.

Ora analizziamo il costo totale degli archi costruiti: $\alpha|E|$. Dividiamo gli archi in quelli dell'albero base ($E_{cut}$​) e quelli extra ($E_{non-cut}​$):

- **Costo​** $E_{cut}$: Sono al massimo $n-1$, quindi costano al massimo $\alpha(n-1)$.
- **Costo** $E_{non-cut}​$: Qui usiamo la Prop. 2 che abbiamo appena dimostrato. Sappiamo che un _singolo_ nodo compra al massimo $\frac{(n-1)2d}{\alpha}$ archi extra. Moltiplicando per tutti gli $n$ nodi della rete, il numero totale di archi extra è $\leq \frac{n(n-1)2d}{\alpha}$. Moltiplicando per il costo unitario $\alpha$, la formula si semplifica e il costo totale degli archi extra è $n(n-1)2d$.

Se sommiamo questi due costi ($\alpha(n-1)+n(n-1)2d$), vediamo che assomigliano tantissimo alla formula dell'OPT. Raccogliendo $2d$, è facile dimostrare che questa somma è abbondantemente $\leq2d\cdot OPT$.

$$\alpha|E|=\alpha|E_{cut}|+\alpha|E_{non-cut}|\leq\alpha(n-1)+n(n-1)2d\leq2d\cdot OPT$$

Adesso uniamo i risultati ottenuti:

$$\begin{align}SC(G)&=\text{Costo Distanze}+\text{Costo Archi}\\ SC(G)&\leq(d\cdot OPT)+(2d\cdot OPT)=3d\cdot OPT\end{align}$$

Poiché $3d$ appartiene alla classe di complessità $O(d)$, abbiamo appena dimostrato formalmente il teorema: **il Price of Anarchy è limitato da $O(d)$**, e siccome $d\leq 2\sqrt{\alpha}+1$ (da Prop. 1) otteniamo che 
$$PoA=O(\sqrt{\alpha})$$
# Teorema sulle strategie degli agenti

Vale il seguente teorema:

>[!teorem]- Teorema
>Date le strategie di tutti gli altri agenti, determinare la **miglior strategia** di un dato giocatore risulta essere **NP-Hard**

**dimostrazione**

La dimostrazione segue da una riduzione dal problema **Dominating Set (DS)**

Prima di tutto quindi ricordiamo il formalismo del problema:

- **input**
	- un grafo $G=(V,E)$
- **soluzione**
	- un sottoinsieme $U\subseteq V$ tale per cui $\forall v\in V\setminus U$ esiste un $u\in U$ tale che $(u,v)\in E$
- **misura**
	- cardinalità di $U$

![center|300](img/Pasted%20image%2020260331124844.png)
## Riduzione: Dominating Set

La riduzione è la seguente:
- partendo dal grafo $G$ originale, si costruisce un grafo $G'=G(S_{-i})$; ovvero il grafo $G'$ è lo stesso di quello originale meno il nodo relativo al giocatore $i$-esimo
- si considerano inoltre valori di $\alpha$ tale che $1\lt\alpha\lt2$

![center|400](img/Pasted%20image%2020260331125404.png)

La riduzione quindi si basa sul dimostrare questa doppia implicazione (se e solo se):

> Il giocatore $i$ ha una strategia con un costo $\leq\alpha k+2n-k$ **se e solo se** nel grafo degli altri giocatori $G$ esiste un Dominating Set di dimensione $\leq k$.

### La direzione "Facile" ($\leftarrow$)

**Ipotesi:** Supponiamo che nel grafo $G$ esista un Dominating Set (chiamiamolo $U$) composto da $k$ nodi (i nodi rossi). 

![center|400](img/Pasted%20image%2020260331125838.png)

**Tesi:** Il giocatore i può ottenere un costo $\leq\alpha k+2n-k$.

**Dimostrazione:** Il giocatore $i$ decide semplicemente di "comprare" gli archi diretti verso tutti i $k$ nodi che formano il Dominating Set $U$. Calcoliamo il suo costo totale:

- **Costo degli archi:** Ha comprato $k$ archi, quindi spende αk.
- **Costo delle distanze verso $U$:** I $k$ nodi di $U$ sono a distanza 1 dal nodo del giocatore $i$. Il costo è $1\cdot k=k$.
- **Costo delle distanze verso il resto del grafo:** Poiché $U$ è un Dominating Set, tutti gli altri $n-k$ nodi del grafo sono collegati direttamente a un nodo di $U$. Quindi, per raggiungere questi $n-k$ nodi, il giocatore $i$ fa 2 passi (va in un nodo di $U$ e poi scende). Il costo per questi nodi è $2\cdot(n-k)=2n-2k.$

Sommando i costi delle distanze otteniamo: $$k+2n-2k=2n-k$$
Il costo totale è quindi: $$\alpha k+2n-k$$Questa direzione è provata.

### La direzione "Impegnativa" ($\implies$)

**Ipotesi:** Supponiamo che il giocatore $i$ abbia trovato una strategia $S_i$​ che gli garantisce un costo $\leq\alpha k+2n-k$. 
**Tesi:** Nel grafo $G$ deve esistere per forza un Dominating Set di dimensione $\leq k$.

**Dimostrazione:** Questa fase procede per passi successivi.

**Passo A: Eliminare le distanze lunghe (L'ottimizzazione)** Prendiamo la strategia $S_i​$.

Supponiamo che ci sia un nodo $v$ nel grafo che si trova a distanza 3 o superiore dal giocatore $i$. Cosa succede se il giocatore $i$ modifica la sua strategia e decide di comprare un arco diretto verso $v$?

- Paga il costo del nuovo arco: $+\alpha$.
- La distanza verso $v$ passa da $\geq3$ a $1$. Il suo risparmio sulle distanze è _almeno_ $2$.
- La variazione netta del suo costo è $\leq\alpha-2$. Poiché siamo nell'ipotesi $\alpha\lt2$, la quantità ($\alpha-2$) è un numero negativo. Significa che comprare questo arco **diminuisce strettamente il costo totale**.

Di conseguenza, una strategia ottima o comunque con un costo basso non avrà _mai_ nodi a distanza $3$ o superiore.

Se ci sono, possiamo comprare archi per abbassare ulteriormente il costo della strategia $S_i$​, fino a quando tutti i nodi saranno a distanza $1$ o $2$ dal giocatore $i$.

![center|400](img/Pasted%20image%2020260331131704.png)


**Passo B: Individuare il Dominating Set** 

Dopo aver applicato l'ottimizzazione del Passo A, chiamiamo $U$ l'insieme dei nodi che il giocatore $i$ ha deciso di connettere direttamente (i nodi a distanza $1$, colorati in rosso). 

Tutti gli altri nodi del grafo si trovano a distanza $2$. Come fanno a essere a distanza $2$? Devono necessariamente essere collegati ad almeno uno dei nodi in $U$. Questo significa che l'insieme **$U$ è un Dominating Set** del grafo $G$.

![center|400](img/Pasted%20image%2020260331131910.png)

**Passo C: Dimostrare la dimensione di $U$** 

Sappiamo che questa strategia modificata usa il Dominating Set $U$. 

Il suo costo (applicando la formula vista nella prima parte) sarà esattamente $\alpha|U|+2n-|U|$. 

Poiché le modifiche fatte nel Passo A hanno solo _diminuito o mantenuto uguale_ il costo iniziale, questo nuovo costo deve essere minore o uguale al costo della strategia di partenza:
$$\alpha|U|+2n-|U|\leq Costo(S_i​)\leq\alpha k+2n-k$$

Semplifichiamo la disequazione e otteniamo:

$$\begin{align*}
\alpha|U|-|U|+2n&\leq\alpha k-k+2n\\
\alpha|U|-|U|&\leq\alpha k-k\\
|U|(\alpha-1)&\leq k(\alpha-1)
\end{align*}
$$
Poiché $\alpha\gt1$, la quantità ($\alpha-1$) è un numero strettamente positivo. 

Possiamo dividere entrambi i lati per ($\alpha-1$) senza cambiare il verso della disequazione, ottenendo: $$|U|\leq k$$

Abbiamo dimostrato che esiste un Dominating Set di dimensione al massimo $k$

Trovare quindi la mossa migliore per il giocatore (che minimizza il costo in funzione di $k$) equivale matematicamente a trovare il Dominating Set minimo del grafo. 

Poiché trovare il Dominating Set minimo è un problema intrattabile (***NP-Hard***), anche calcolare la Best Response nei Local Connection Games (per $1\lt\alpha\lt2$) è ***NP-Hard***

---

Dimostrazione formale PoA=1 con $\alpha\lt1$ ^c0ae07