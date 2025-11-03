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
# Algorithmic Game Theory

La **Teoria dei Giochi Algoritmica** (***AGT***) si occupa di risolvere problematiche algoritmiche relative a sistemi ditribuiti non-cooperativi

Ci sono $2$ strade di ricerca, che sono:
- Teoria degli Algoritmi: si occupa di **problemi computazionali**, risponde alle seguenti domande
	- Cosa può essere facilmente computato?
	- Quanto tempo impiego a calcolare una soluzione?
	- Qual'è la qualità della soluzione calcolata?
- Teoria dei Giochi: si occupa di **interazioni tra individui egoisti**, risponde alle seguenti domande
	- Qual'è il risultato dell'interazione?
	- Quali obiettivi sociali sono compatibili con l'egoismo?

Ci sono delle assunzioni differenti fra le $2$ strade di ricerca appena evidenziate, che sono:
- Teoria degli Algoritmi (in sistemi distribuiti): 
	- Processori sono **obbedienti, difettosi o avversariali**
	- *Grandi* sistemi, risorse computazionali *limitate*
- Teoria dei Giochi:
	- I giocatori sono **strategici** (egoisti)
	- *Piccoli* sistemi, risorse computazionali *illimitate*

Il mondo dei Networks moderni è composto da **agenti** che spesso sono autonomi (anche chiamati utenti), che hanno i propri goals individuali, e le componenti di rete sono tenute dai providers

Delle volte il mondo moderno involve reti di **enormi** dimensioni, che contengono sistemi massivi, però presentano il problema delle risorse **computazionali/comunicative** limitate

Questo comprende sia problemi ***computazionali che strategici***

Se volessimo dare una definizione effettiva all' AGT potremmo dire che $$\text{AGT=TA+GT}$$
dove:
- $TA$ sta per Teoria degli Algoritmi
- $GT$ sta per Teoria dei Giochi

La teoria dei giochi offre un'insieme di strumenti utili per indirizzare **problemi computazionali** in scenari non-cooperativi, come ad esempio le reti usate da utenti "egoisti"

La teoria degli algoritmi fa luce sui risultati della teoria dei giochi
- per diversi risultati sull'esistenza di equilibri/meccanismi abbiamo che tale equilibrio/meccanismo non può essere trovato/implementato in modo efficiente

## Basi della Teoria dei Giochi: Giochi ed equilibri

Partiamo intanto dal definire cosa intendiamo con "gioco"

>[!definition]- Gioco
>Un **gioco** consiste in:
>1. Un insieme di **giocatori** (player)
>2. Un insieme di **regole**: *Chi* deve agire *quando*, e *quali* sono le possibili azioni (**strategie**)
>3. Una specifica dei **guadagni** (payoffs) per ciascuna combinazione di strategie

La teoria dei giochi cerca quindi di *predirre* il **risultato** del gioco (ovvero la **soluzione**), tenendo conto del comportamento di ogni giocatore

Cerca quindi di trovare il così detto ***equilibrio***
### Un famoso gioco one-shot: il Dilemma del Prigioniero

Il gioco inizia così 

![[Pasted image 20251103123127.png|center|700]]

La decisione del Player $1$ è la seguente:
- Se il player $2$ sceglie "Don't Implicate" allora per il player $1$ è meglio scegliere "Implicate"
- Se il player $2$ sceglie "Implicate" allora per il player $1$ è meglio scegliere "Implicate"
- È sempre meglio scegliere "Implicate" per il player $1$, indipendentemente da cosa sceglie il player $2$: ci troviamo quindi davanti a una ***Strategia Dominante***

![[Pasted image 20251103123614.png|center|700]]


La decisione del Player $2$ è la seguente:
- Se il player $1$ sceglie "Don't Implicate" allora per il player $2$ è meglio scegliere "Implicate"
- Se il player $1$ sceglie "Implicate" allora per il player $2$ è meglio scegliere "Implicate"
- È sempre meglio scegliere "Implicate" per il player $2$, indipendentemente da cosa sceglie il player $1$: ci troviamo quindi davanti a una ***Strategia Dominanteuindi

![[Pasted image 20251103123735.png|center|700]]

Quindi, abbiamo che:
- Per entrambi è meglio scegliere di Implicare **indipendetemente** dalla scelta dell'altro player
- "Implicate" è quindi la Strategia Dominante per entrambi
- (Implicate_verde, Implicate_blu) diventa quindi il **Dominating Strategy Equilibrium** (DSE)

Nota: se potrebbero colludere, allora è vantaggioso per entrambi **non implicarsi**, ma non si tratta di un equilibrio poiché entrambi hanno un incentivo a deviare.

![[Pasted image 20251103123808.png|center|700]]
### Un gioco in rete

Vediamo quest'altro esempio famoso di "gioco"

Il gioco è costruito in questo modo:
- abbiamo due Internet Service Providers (ISP): ISP1 e ISP2
- ISP1 vuole mandare il traffico di rete da $s_{1}$ a $t_{1}$
- ISP2 vuole mandare il traffico di rete da $s_{2}$ a $t_{2}$
- Gli archi del grafo hanno tutti peso $1$
- Ogni ISP può usare due percorsi: uno che passa per $C$ e uno che passa per $S$

![[Pasted image 20251103124501.png|center|300]]

Analizziamo quindi la *Matrice dei Costi*

| ISP1/ISP2    | attraverso S | attraverso C |
| ------------ | ------------ | ------------ |
| attraverso S | $2,2$        | $5,1$        |
| attraverso C | $1,5$        | $4,4$        |
Vediamo ora come rappresentare formalmente un gioco, usando la **Forma Normale**
- $N$ players **razionali**
- $S_i$ = Insieme di strategie per il player $i$
- La combinazione delle strategie $(s_{1},s_{2},\dots,s_{N})$ assegna le vincite $(p_{1},\dots,p_{N})$ agli $N$ players, generando così la matrice delle vincite $$S_{1}\times S_{2}\times\dots\times S_{N}$$
## Dominant Strategy Equilibrium

Definiamo il concetto di DSE

>[!definition]- Dominatic Strategy Equilibrium (DSE)
>È una **combinazione di strategie** $s^{\star}=(s^{\star}_{1},s^{\star}_{2},\dots,s^{\star}_{N})$ tale che $s_{i}^{\star}$ è la **strategia dominante** per ogni $i$, ovvero, *per ogni possibile profilo strategico alternativo* $s=(s_{1},s_{2},\dots,s_i,\dots,s_{N})$ vale che:
>1. se $p_{i}$ è un'**utilità** allora $p_{i}(s_{1},s_{2},\dots, s^{\star}_i,\dots,s_{N})\geq p_{i}(s_{1},s_{2},\dots,s_i,\dots,s_{N})$
>2. se $p_{i}$ è un **costo** allora $p_{i}(s_{1},s_{2},\dots,s^{\star}_i,\dots,s_{N})\leq p_{i}(s_{1},s_{2},\dots,s_i,\dots,s_{N})$

La Dominant Strategy è quindi la **miglior risposta** ad *ogni* strategia di ogni altro player
Se un gioco ha il DSE, allora i giocatoru convergeranno immediatamente ad esso

Ovviamente, non tutti i giochi hanno un DSE (infatti, solo pochi di essi lo contengono in pratica)

## Nash Equilibrium

Una soluzione più flessibile al DSE è il così detto **Equilibrio di Nash** (NE)

NE è definito come segue:

>[!definition]- Nash Equilibrium (NE)
>È una **combinazione di strategie** $s^{\star}=(s^{\star}_{1},s^{\star}_{2},\dots,s^{\star}_{N})$ tale che per ogni $i,s^{\star}_i$ è la **miglior risposta** a $(s^{\star}_{1},s^{\star}_{2},\dots s_{i-1}^{\star},s_{i+1}^{\star},\dots,s^{\star}_{N})$, ovvero, *per ogni possibile strategia alternativa* $s_i$ del giocatore $i$ vale che:
>1. se $p_{i}$ è un'**utilità** allora $p_{i}(s_{1}^{\star},s_{2}^{\star},\dots, s^{\star}_i,\dots,s_{N}^{\star})\geq p_{i}(s_{1}^{\star},s_{2}^{\star},\dots,s_i,\dots,s_{N}^{\star})$
>2. se $p_{i}$ è un **costo** allora $p_{i}(s_{1}^{\star},s_{2}^{\star},\dots,s^{\star}_i,\dots,s_{N}^{\star})\leq p_{i}(s_{1}^{\star},s_{2}^{\star},\dots,s_i,\dots,s_{N}^{\star})$

