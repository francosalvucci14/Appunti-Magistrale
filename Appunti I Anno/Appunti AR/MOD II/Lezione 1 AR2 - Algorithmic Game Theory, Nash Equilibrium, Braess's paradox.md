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

![center|500](img/Pasted%20image%2020251103123127.png)

La decisione del Player $1$ è la seguente:
- Se il player $2$ sceglie "Don't Implicate" allora per il player $1$ è meglio scegliere "Implicate"
- Se il player $2$ sceglie "Implicate" allora per il player $1$ è meglio scegliere "Implicate"
- È sempre meglio scegliere "Implicate" per il player $1$, indipendentemente da cosa sceglie il player $2$: ci troviamo quindi davanti a una ***Strategia Dominante***

![center|500](img/Pasted%20image%2020251103123614.png)


La decisione del Player $2$ è la seguente:
- Se il player $1$ sceglie "Don't Implicate" allora per il player $2$ è meglio scegliere "Implicate"
- Se il player $1$ sceglie "Implicate" allora per il player $2$ è meglio scegliere "Implicate"
- È sempre meglio scegliere "Implicate" per il player $2$, indipendentemente da cosa sceglie il player $1$: ci troviamo quindi davanti a una ***Strategia Dominanteuindi

![center|500](img/Pasted%20image%2020251103123735.png)

Quindi, abbiamo che:
- Per entrambi è meglio scegliere di Implicare **indipendetemente** dalla scelta dell'altro player
- "Implicate" è quindi la Strategia Dominante per entrambi
- (Implicate_verde, Implicate_blu) diventa quindi il **Dominating Strategy Equilibrium** (DSE)

Nota: se potrebbero colludere, allora è vantaggioso per entrambi **non implicarsi**, ma non si tratta di un equilibrio poiché entrambi hanno un incentivo a deviare.

![center|500](img/Pasted%20image%2020251103123808.png)
### Un gioco in rete

Vediamo quest'altro esempio famoso di "gioco"

Il gioco è costruito in questo modo:
- abbiamo due Internet Service Providers (ISP): ISP1 e ISP2
- ISP1 vuole mandare il traffico di rete da $s_{1}$ a $t_{1}$
- ISP2 vuole mandare il traffico di rete da $s_{2}$ a $t_{2}$
- Gli archi del grafo hanno tutti peso $1$
- Ogni ISP può usare due percorsi: uno che passa per $C$ e uno che passa per $S$

![center|300](img/Pasted%20image%2020251103124501.png)

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

Vediamo un'esempio di NE, tramite il coordination game chiamato "La battaglia dei Sessi"

La situazione è quella descritta in figura

![center](Pasted%20image%2020251104121125.png)

Notiamo che:
- La coppia (Stadium_v, Stadium_b) è un NE: miglior risposta per ognugno
- La coppia (Cinema_v, Cinema_b) è un NE: miglior risposta per ognugno

Il problema è le loro non sono DSE, siamo veramente sicuri che alla fine usciranno insieme?

Vedi anche esempio sulla congestione

Possiamo quindi trarre alcune conclusioni, ovvero 

- In un NE nessun agente può deviare unilateralmente dalla propria strategia, dato che le strategie degli altri sono fisse.
- L'agente deve riflettere sulle strategie degli altri agenti.
- DSE $\implies$ NE (ma non vale il contrario).
- Se il gioco viene **ripetuto** più volte e i giocatori convergono verso una soluzione, allora deve trattarsi di un NE.

### Un grande problema nella GT : l'esistenza di un NE

Sfortunatamente, per giochi **puramente strategici** (come visti fin'ora), è facile vedere che non possiamo avere un risultato generale di esistenza

In altre parole, possono esserci ***nessun***, ***uno***, ***molti*** NE, a seconda del gioco

Vediamo un'esempio, tramite il gioco conflittuale. Matching Pennies

La situazione è la seguente:

![center|600](Pasted%20image%2020251104123152.png)

In ogni configurazione, uno dei giocatori preferisce cambiare la sua strategia, e quindi **no NE**

Tuttavia, quando un giocatore può selezionare la propria strategia **in modo casuale** utilizzando una **distribuzione di probabilità** sul proprio insieme di strategie possibili (***strategia mista***), allora vale il seguente risultato generale:

>[!teorem]- Teorema (Nash, 1951)
>Qualsiasi gioco con un insieme finito di giocatori e un insieme finito di strategie ha un NE di strategie miste (cioè, il guadagno atteso non può essere migliorato modificando unilateralmente la distribuzione di probabilità selezionata ).

Ritornando al gioco matching pennis: se ogni giocatore imposta $Pr(Testa)=Pr(Croce)=\frac{1}{2}$, allora il guadagno atteso di ogni giocatore è $0$, e questo è un NE, poiché nessun giocatore può migliorare questo risultato scegliendo una distribuzione di probabilità diversa!

Quando parliamo di **analisi di un gioco** emergono alcune problematiche, che sono:
- Stabilire se un gioco ha SEMPRE un NE
- Una volta appurato che esiste, trovare un NE
- In un gioco ripetuto, stabilire *se* e *in quanti* passi il sistema finirà per **convergere** verso un NE
- Stabilire la **qualità** del NE

### Sulla qualità del NE

Le domande che ci poniamo qui sono:

1. Quanto è inefficiente un NE rispetto a una situazione ideale in cui i giocatori si sforzerebbero di collaborare con l'obiettivo comune di scegliere il risultato migliore?
2. Il risultato migliore rispetto a cosa?

Abbiamo bisogno di una **funzione di scelta sociale** $C$ che mappi i profili strategici in numeri reali.
- $C$ misura la qualità complessiva di un risultato $s$.
- Ad esempio, $C(s)$: somma dei costi/utilità di tutti i giocatori.

#### Una prospettiva worst-case: Price of Anarchy (PoA)

Definiamo la **PoA**, nel seguente modo:

>[!definition]- PoA (Koutsopias & Papadimitriou, 1999)
>Dato un gioco $G$ e una funzione di scelta sociale $C$, sia $S$ l'insieme di tutti i NE.
>Se il payoff rappresenta un **costo** (rispettivamente un'**utilità**) per un player, sia $OPT$ il risultato del gioco $G$ che ***minimizza*** (rispettivamente ***massimizza***) $C$.
>Allora, il **Price of Anarchy (PoA)** di $G$ in rispetto a $C$ è $$PoA_{G}(C)=\sup_{s\in S}\frac{C(s)}{C(OPT)}\quad\left(\text{rispettivamente }\inf_{s\in S}\frac{C(s)}{C(OPT)}\right)$$

#### Un'altra prospettiva: Price of Stability (PoS)

Definiamo ora la **PoS**, nel seguente modo:

>[!definition]- PoA (Schulz & Moses, 2003)
>Dato un gioco $G$ e una funzione di scelta sociale $C$, sia $S$ l'insieme di tutti i NE.
>Se il payoff rappresenta un **costo** (rispettivamente un'**utilità**) per un player, sia $OPT$ il risultato del gioco $G$ che ***minimizza*** (rispettivamente ***massimizza***) $C$.
>Allora, il **Price of Stability (PoS)** di $G$ in rispetto a $C$ è $$PoS_{G}(C)=\inf_{s\in S}\frac{C(s)}{C(OPT)}\quad\left(\text{rispettivamente }\sup_{s\in S}\frac{C(s)}{C(OPT)}\right)$$

