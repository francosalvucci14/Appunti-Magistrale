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
![center|400](Pasted%20image%2020260328111714.png)

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

![center|500](Pasted%20image%2020260328113553.png)

Cosa succederebbe se il nodo $u$ decidesse di deviare dalla sua strategia attuale e **comprasse un arco diretto** verso $v$ (la freccia rossa in alto)?

- **Il Costo:** Pagherebbe il prezzo di un nuovo arco, ovvero $\alpha$.
- **Il Beneficio:** Risparmierebbe un sacco di distanza non solo per raggiungere $v$, ma per raggiungere _tutti i nodi vicini a $v$_ su quel cammino.

![center|500](Pasted%20image%2020260328113327.png)

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

![center|500](Pasted%20image%2020260328113631.png)

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

Il _numero_ di archi extra ($|E_{non-cut}​|$) è limitato da $O\left(\frac{n^{2}d}{\alpha}\right)$. ("tricky bound, vedi giù per dimostrazione")
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



---

Dimostrazione formale PoA=1 con $\alpha\lt1$ ^c0ae07