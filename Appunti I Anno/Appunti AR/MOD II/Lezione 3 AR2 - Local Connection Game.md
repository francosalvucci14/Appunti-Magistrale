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

![center|400](Pasted%20image%2020260327160657.png)

Se invece il nodo $u$ decide di **costruire** un'altro arco (quello con $\alpha$ in rosso), allora:
- si riaggiornano le distanze, adesso il nodo $u$ arriva al nodo $4$ usando un solo arco, quindi la distanza da $u$ a quel nodo non sarà più $4$ ma diventerà $1$
	- stessa cosa per l'altro nodo con $-1$
- si riaggiorna il $cost_u(S)$ considerando l'utilizzo dell'altro arco ($\alpha$ rosso)

Il costo per il nodo $u$ diventa quindi:
$$cost_u(S)=2\alpha+9$$

![center|400](Pasted%20image%2020260327160941.png)

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

![center|200](Pasted%20image%2020260327162710.png)

**Grafo a Stella** : Albero (ergo grafo connesso e aciclico) la cui altezza è al più $1$

![center|200](Pasted%20image%2020260327162818.png)

Perfetto, a questo punto possiamo dare l'enunciato e la dimostrazione del seguente lemma, che ci servirà per rispondere alla domanda iniziale (insieme ad un'altro lemma)

>[!teorem]- Lemma 1
>Se $\alpha\leq2$ allora il grafo completo è la soluzione ottimale, mentre se $\alpha\geq2$ allora una *qualunque* stella è soluzione ottimale

**dimostrazione lemma 1**

Prendiamo $G=(V,E)$ un grafo con $|E|=m$ archi

Allora possiamo scrivere il costo sociale relativo a questo grafo come:
$$\boxed{SC(G)\geq \alpha\cdot m+2m+2(n(n-1)-2m)=\underbrace{(\alpha-2)m-2n(n-1)}_{LB(m)}}$$

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

![center|200](Pasted%20image%2020260327165159.png)

**Perché nessuno vuole deviare?** Immagina che un nodo $v$ decida di risparmiare sui costi di costruzione eliminando $k$ archi che aveva comprato.

- **Quanto risparmia in costruzione?** Risparmia esattamente $\alpha k$.
- **Quanto ci perde in distanza?** Per i $k$ nodi a cui si è disconnesso, la distanza non è più 1. Nel migliore dei casi possibili (assumendo che il grafo resti connesso tramite altri nodi), la nuova distanza verso questi $k$ nodi sarà _almeno_ 2. Quindi il costo di distanza aumenta di almeno $(2-1)=1$ per ciascuno di questi $k$ nodi. L'aumento totale del costo di routing è $\geq k$.

Il bilancio totale per il nodo $v$ (variazione di costo) è: $-\alpha k+k=k(1-\alpha)$. Poiché siamo nell'ipotesi $\alpha\leq1$, la quantità ($1-\alpha$) è $\geq0$. Quindi la variazione di costo è sempre positiva o nulla (il costo aumenta o resta uguale, non diminuisce mai). Nessun nodo può migliorare la propria situazione rimuovendo archi. **Il grafo completo è stabile.**

***caso*** $\alpha\geq1$

Prendiamo ad esempio il seguente grafo a stella, dove $c$ è il centro e $v$ le foglie (che comprano archi verso il centro)

![center|200](Pasted%20image%2020260327165510.png)

Le foglie comprano un solo arco verso il centro. La distanza foglia-centro è $1$, la distanza foglia-foglia è $2$ (passando per il centro).

Dobbiamo dimostrare che né il centro né le foglie vogliono cambiare strategia.

**1. Il nodo centrale $c$ non ha interesse a deviare:** Il centro è già a distanza $1$ da tutti gli altri nodi. Non compra nessun arco (sono le foglie che puntano a lui). Non potendo rimuovere archi (ne compra 0) e non potendo migliorare le sue distanze (sono già al minimo possibile), la sua strategia è già ottima.

**2. I nodi periferici $v$ non hanno interesse a deviare:** Cosa succede se una foglia $v$ decide di comprare $k$ nuovi archi diretti verso altre foglie? (le frecce rosse).

- **Quanto paga in più?** Paga il costo di costruzione per i nuovi archi: $\alpha k$.
- **Quanto risparmia in distanza?** Prima, per raggiungere quelle $k$ foglie, ci metteva 2 passi (passando per il centro). Ora ci mette 1 passo (diretto). Il risparmio sulla distanza è esattamente di 1 passo per ogni nodo, quindi risparmia un totale di $k$.

Il bilancio totale per il nodo $v$ è: $\alpha k-k=k(\alpha -1)$. Poiché siamo nell'ipotesi $\alpha\geq1$, la quantità ($\alpha-1$) è $\geq0$. Anche in questo caso, la variazione del costo totale è positiva o nulla. Comprare nuovi archi non porta a un risparmio netto. Allo stesso modo, rimuovere l'unico arco verso il centro lo disconnetterebbe dalla rete (costo di distanza infinito). Nessuna foglia vuole deviare. **La stella è stabile** $\blacksquare$




