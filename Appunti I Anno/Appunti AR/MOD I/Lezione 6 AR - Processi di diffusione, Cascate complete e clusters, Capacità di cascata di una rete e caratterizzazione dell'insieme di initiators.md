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





[^1]: talvolta modificandone il comportamento, come visto nell'esperimento di Ganovetter

[^2]: non c'è coalizione di gruppi di nodi per prendere collettivamente la stessa decisione