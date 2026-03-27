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
- Per valutare la qualità generale della rete, consideriamo il **costo sociale**, come ad esempio la somma dei costi di tutti i giocatori
- Diremo che una rete si dice **ottimale** o **socialmente efficiente** se minimizza il costo sociale
- Diremo inoltre che un grafo $G=(V,E)$ si dice **stabile** (per un valore $\alpha$) se esiste un vettore di strategie $S$ tale per cui:
	- $S$ è un NE
	- $S$ crea $G$


![center|400](img/Pasted%20image%2020260327105911.png)

