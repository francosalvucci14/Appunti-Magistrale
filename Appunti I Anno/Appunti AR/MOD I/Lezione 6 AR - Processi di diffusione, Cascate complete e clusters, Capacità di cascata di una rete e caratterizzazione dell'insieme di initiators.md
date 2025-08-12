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



[^1]: talvolta modificandone il comportamento, come visto nell'esperimento di Ganovetter

[^2]: non c'è coalizione di gruppi di nodi per prendere collettivamente la stessa decisione