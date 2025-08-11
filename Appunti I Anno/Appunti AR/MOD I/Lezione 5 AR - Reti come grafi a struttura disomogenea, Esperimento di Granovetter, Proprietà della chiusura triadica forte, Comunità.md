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
# Introduzione

Il materiale descritto qui si può trovare anche nel capitolo $3$ del libro e nella dispensa Communities (che useremo più avanti come appoggio)

Fin'ora abbiamo studiato grafi che modellano reti a livello statistico.

Così facendo, ci siamo disinteressati delle *peculiarità dei singoli nodi*, piuttosto abbiamo studiato proprietà che valevano *mediamente* per i nodi.

Da qui in poi "cambieremo" il punto di vista, andando ad analizzare la posizione dei singoli nodi all'interno della rete, per poter studiare:
- se è possibile evidenziare particolari strutture nella rete
- se tutti i nodi si trovano, grosso modo, nella stessa situazione all'interno della rete, oppure se vi sono differenze osservabili fra nodo e nodo
- e se i nodi possono trarre vantaggio (e di quale tipo) da queste differenze
# L'esperimento di Granovetter

Negli anni $'60$ il sociologo Mark Granovetter intervistò un gruppo di individui che avevano recentemente cambiato lavoro

Granovetter fece loro una serie di domande volte a capire in che modo erano venuti a conoscenza della possibilità di ottenere l'impiego che avevano ottenuto

Il risultato di tale esperimento fu che molti degli intervistati avevano avuto le informazioni, che li avevano condotti alla loro occupazione attuale, attraverso una comunicazione da parte di qualcuno che conoscevano (una specie di passa-parola, che può essere ben prevedibile)

Il fatto abbastanza inaspettato che emerse dalle sue interviste fu che spesso, l'informazione era arrivata da qualcuno che conoscevano superficialmente, non dagli amici più stretti

Allora l'esperimento di Gravenotter sembra suggerire che:
1) non è tanto la forza del legame quella che ha aiutato a trovare lavoro
2) **quanto il tipo di informazione che una relazione è capace di veicolare**

In effetti, pensandoci bene, i nostri più cari amici frequentano, grosso modo, gli stessi posti che frequentiamo anche noi (questo perchè si presuppone che abbiamo una serie di cose che ci accomunano parecchio). 

Così facendo, noi e i nostri amici abbiamo accesso alle stesse fonti di informazione

Invece, i nostri conoscenti frequentano posti diversi da quelli che frequentiamo noi, cosicchè hanno accesso a fonti di informazione diverse, e così facendo vanno ad ampliare il nostro "**raggio d'azione**"

## Bridges e Local Bridges

Se consideriamo il grafo $G=(V,E)$ che modella la rete, gli archi che "aumentano" le nostre informazioni sono quelli che ci collegano a regioni della rete *inaccessibili* ai nostri amici

Vale quindi la seguente definizione:

>[!definition]- Bridge
>Definiamo un **bridge** come un arco la cui rimozione disconnette la rete [^1]

D'altra parte, sappiamo che una rete contiene con buona probabilità componenti giganti densamente connesse, e dunque la presenza di bridge è poco probabile, pertanto possiamo "*rilassare*" la definizione precedente:

>[!definition]- Local Bridges
>Chiamiamo un arco **local bridges** se i suoi vicini non hanno vicini in comune, ovvero $$(u,v)\in E\text{ è local bridge se }N(u)\cap N(v)=\emptyset$$

Dato che, come abbiamo visto dall'esperimento, spesso l'informazione arriva da qualcuno conosciuto solo superficialmente (e quindi no da amici stretti), possiamo riconoscere $2$ tipi di relazione, all'interno di una rete sociale
- **relazioni forti**: quelle che ci collegano agli amici stretti
- **relazioni deboli**: quelle che ci collegano a semplici conoscenti

Conseguentemente, possiamo modellare una rete del genere mediante un grafo $G$ in cui gli archi sono partizionati in due sottoinsiemi:
- **archi forti** (**strong ties**)
- **archi deboli** (**weak ties**)

Quindi, avremo che $$G=(V,S\cup W),\quad S\cap W=\emptyset$$
Come ha dimostrato Granovetter, gli archi deboli veicolano informazioni alle quali non avremmo accesso tramite gli archi forti: e questa viene chiamata **forza degli archi deboli**

Detto questo, se c'è una relazione fra i nodi $a,b$ e una relazione fra $a,c$ (quindi sia $(a,b)$ che $(a,c)$ sono **archi forti**), **allora è probabile che prima o poi si creerà anche l'arco $(b,c)$**, vale a dire, si andrà a creare la vecchia ***chiusura triadica*** (incontrata nel fenomeno Small World)

L'esistenza di chiusure triadiche ci impone che, per descrivere queste reti, abbiamo bisogno di grafi dinamici[^2]

Alla base della creazione di chiusure triadiche possiamo individuare ragioni di:
- *opportunità* di incontrarsi
- *incentivo* a stringere una nuova relazione
- *fiducia*

Lasciamo ora che la rete evolva, ovvero che si vadano a formare man mano tutti i triangoli, fino a raggiungere una configurazione stabile (ovvero una configurazione in cui la rete non cambia più nel tempo)

Cosa possiamo dire della struttura del grafo $G=(V,S\cup W)$ corrisponde a una rete in una configurazione stabile? 
La risposta è che, probabilmente, tutti i triangoli possibili si sono formati

Definiamo ora la **proprietà di chiusura triadica forte**

>[!definition]- Proprietà di Chiusura Triadica Forte (STCP)
>Sia $G=(V,S\cup W)$; un nodo $u$ soddifa **STCP** se, per ogni coppia di archi forti incidenti a $u$, i loro estremi sono collegati da un arco. 
>Formalmente vale che:
>$$u\in V\text{ soddisfa SCTP se }\forall(u,v)\in S\left[(v,z)\in S\cap W\right]$$
>$G$ soddisfa la SCTP se tutti i suoi nodi la soddisfano

### STCP e Local Bridges

Vale quindi il seguente teorema

>[!teorem]- Teorema
>Sia $G=(V,S\cup W)$; se un nodo $u$ soddisfa SCTP, e se esistono due nodi distinti $x,z:(u,x)\in S,(u,z)$ è local bridge, allora $(u,z)\in W$

**dimostrazione**

Poichè l'arco $(u,z)$ è local bridge, allora per definizione deve valere che $N(u)\cap N(z)=\emptyset$

Se $(u,z)\in S$ allora, poichè $(u,x)\in S$ e soddisfa SCTP, dovrebbe valere che $(x,z)\in S\cup W$, e quindi $x\in N(u)\cup N(z)$, ma di conseguenza $N(u)\cup N(z)\neq\emptyset$ - contraddizione $\blacksquare$

Questo teorema mostre come **una proprietà globale (essere local bridge) si riflette in una proprietà locale (essere un weak ties)** 
- essere weak ties è proprietà **locale**: un nodo sa da solo se un suo vicino è un amico o un conoscente
- essere local bridge è una proprietà **globale**: un nodo deve chiedere a tutti i suoi vicini se qualcuno di loro conosce un suo conoscente per sapere se è un local bridge

In effetti, nell'esperimento di Granovetter, i waek ties erano anche local bridge (in quanto portatori di informazione)

Con il passare del tempo, una chiusura triadica dopo l'altra, si andrà a formare nella rete **un gruppo di nodi fortemente coeso**, con un elevato grado di interconnessione fra i nodi che lo compongono.

Questo gruppo coeso prende nome di **cluster/comunità**

La domanda ora è, quand'è che possiamo dire che un gruppo di nodi è *abbastanza* coeso per poterlo definire una comunità?

# Comunità e coefficiente di clustering

Intanto, per misurare il grado di coesione di un nodo $u$ all'interno di un gruppo di nodi è stato definito il **coefficiente di clustering $c(u)$** come il rapporto fra il numero di relazioni fra vicini di $u$ rispetto a tutte le coppie possibili di vicini di $u$, ovvero: $$c(u)=\frac{|\{(x,y)\in E:x\in N(u)\land y\in N(u)\}|}{\frac{|N(u)|\left[|N(u)-1\right]}{2}}$$
Informalmente, il coefficiente di clustering misura quanto un nodo è "ben inserito" all'interno della rete costituita dai suoi vicini
- un nodo con coefficiente di clustering **basso** è "mal" inserito nel suo gruppo di amici, si trova infatti in una posizione "periferica" secondo quel gruppo di persone
- un nodo con coefficiente di clustering **alto** è "molto" inserito nel suo gruppo di amici, possiamo dire che è un elemento *centrale* di quel gruppo di amici
- per queste motivazioni, il coefficiente di clustering è anche detto **indice di centralità** di un nodo

Sia $C$ un sottoinsieme di nodi: definiamo per ogni nodo $u\in C$ il **coefficiente di clustering di $u$ relativo a $C$** come $$c_C(u)=\frac{|\{(x,y)\in E:x\in N(u)\cap C\land y\in N(u)\cap C\}|}{\frac{|N(u)\cap C|\left[|N(u)\cap C|-1\right]}{2}}$$
Se tutti i nodi contenuti in $C$ hanno coefficiente di clustering relativo a $C$ **elevato**, possiamo ben pensare che $C$ sia una comunità.

La domanda però sorge spontanea: ***quanto elevato*** deve essere il coefficiente di clustering relativo a $C$ per poter definire $C$ una comunità? 
In aggiunta a questa domanda ne sorge un'altra: le comunità non potrebbero essere definite sulla base di altri concetti oltre che al coefficiente di clustering?

Per rispondere a queste due domande dovremo introdurre di *alcuni tipi di comunità* e *determinati concetti* relativi alle comunità stesse, che sono:
- **Cut-Communities**
- **Web-Communities**
- Metodi agglomerativi e partitivi per l'individuazione di comunità
	- qui, sopratutto, descriveremo un metodo partitivo che porterà all'individuazione di comunità basate su un'altro concetto di centralità, ovvero il concetto di **betweenness di un arco**

## Cut-Communities

Iniziamo subito a definire cos'è una **cut-communities** formalmente

>[!definition]- Cut-Community
>Una **cut-community** per un grafo $G=(V,E)$ è un sottoinsieme *proprio e non vuoto* $C$ dei nodi di $G$ che minimizza gli **archi del taglio**, ossia gli archi che collegano nodi in $C$ a nodi in $V\setminus C$
>Formalmente, dato un grafo $G=(V,E),C\subset V$ è una cut-communities se $C\neq\emptyset$ e $$|\{(u,v):u\in C\land v\in V\setminus C\}|=\min_{C'\subset V:C'\neq\emptyset}\left(|\{(u,v):u\in C'\land v\in V\setminus C'\}|\right)$$

Dati un grafo $G=(V,E)$ e una coppia di nodi $s,t$, un *taglio minimo rispetto alla coppia $(s,t)$* è un sottoinsieme *proprio e non vuoto* $C\subset V$ dei nodi di $G$ che contiene $s$ e non contiene $t$, e che minimizza gli archi del taglio

Calcolare il taglio minimo rispetto ad una data coppia di nodi è facile, si può usare l'algoritmo di **Ford-Fulkerson**, ovvero dati due nodi $s,t$ l'algoritmo calcola un sottoinsieme $C$ tale che $s\in C,t\in V\setminus C$ e $$|\{(u,v):u\in C\land v\in V\setminus C\}|=\min_{C'\subset V:s\in C'\land t\in V\setminus C'}\left(|\{(u,v):u\in C'\land v\in V\setminus C'\}|\right)$$

Quindi, per calcolare una cut-community di un grafo possiamo procedere così:
- per ogni coppia di nodi distinti $s,t\in V$: calcoliamo l'insieme $C_{s,t}$ tale che $s\in C_{s,t},t\in V\setminus C_{s,t}$ e che minimizza il taglio
- la cut-community cercata è il sottoinsieme $C_{x,y}$ tale che: $$|\{(u,v):u\in C_{x,y}\land v\in V\setminus C_{x,y}\}|=\min_{s,t\in V:s\neq t}\left(|\{(u,v):u\in C'_{s,t}\land v\in V\setminus C'_{s,t}\}|\right)$$
Il problema è che tutti questi algoritmi non permettono di "controllare" i due insiemi che costituiscono il taglio.

Per capire meglio facciamo un'esempio

La situazione è la seguente 

![[Pasted image 20250809160924.png|center|200]]

Il grafo $G$ è l'unione di due clicque:
- Clicque $A$ sui nodi $u_0,u_1,u_2,u_3,u_4$ (nodi rossi)
- Clicque $B$ sui nodi $v_0,v_1,v_2,v_3,v_4$ (nodi blu)
- Ed è completato dagli archi che collegano $A$ e $B$ (archi verdi): il nodo $u_i$ è adiacente a $v_{i-1},v_i,v_{i+1}$ (somme e diff. modulo $5$)
- Ogni nodo del grafo ha grado $7$

Se applichiamo l'algoritmo per il calcolo della cut-community ci ritorna che la cut-community di questo grafo è solamente il nodo $u_0$, il che non è proprio ragionevole 
(vi direte voi, che cazzo lo abbiamo scritto a fare allora? non si sa, **quarto mistero della fede**)

## Web-Communities

Definiamo ora il concetto di **web-communities**

>[!definition]- Web-Community
>Una **web-community** è un sottoinsieme dei nodi di un grafo, ciascuno dei quali ha più vicini fra i nodi del sottoinsieme che fra quelli esterni ad esso.
>Formalmente, dato un grafo $G=(V,E),C\subset V$ è una (**strong**) web-community se $C\neq\emptyset$ e $$\forall u\in C:|N(u)\cap C|\gt|N(u)\setminus C|=|N(u)\cap (V\setminus C)|$$
>- equivalentemente, dato che $|N(u)\cap C|+|N(u)\setminus C|=|N(u)|,\frac{|N(u)\cap C|}{|N(u)|}\gt \frac{1}{2}$
>
>Analogamente, dato un grafo $G=(V,E),C\subset V$ è una (**weak**) web-community se $C\neq\emptyset$ e $$\forall u\in C:|N(u)\cap C|\geq|N(u)\setminus C|$$
>- equivalentemente $\frac{|N(u)\cap C|}{|N(u)|}\geq \frac{1}{2}$

Definizione semplice e intuitivamente ragionevole (se col cazzo), che può essere generalizzata richiedendo $$\frac{|N(u)\cap C|}{|N(u)|}\gt \alpha(\geq\alpha)$$per qualche $\alpha\in[0,1]$

### Cut e weak Web-Communities

Le definizioni di cut e web community non sono del tutto scorrelate, vale infatti il seguente teorema:

>[!teorem]- Teorema
>Sia $G=(V,E)$ un grafo, se $C\subset V$ è una cut-community per $G$ tale che $|C|\gt1$ allora $C$ è una weak web-community

**dimostrazione**

Supponiamo **per assurdo** che $C$ non sia una weak web-community, allora esiste un nodo $u\in C:|N(u)\cap C|\lt|N(u)\setminus C|$.
Poichè $|C|\gt1$, allora esiste in $C$ un nodo $v$ distinto da $u$: ovvero $C\setminus\{u\}\neq\emptyset$.
Inoltre vale che:
$$\begin{align*}
&|\{(x,y)\in E:x\in C\setminus\{u\}\land y\in (V\setminus C)\cup\{u\}\}|=\\&=|\{(x,y)\in E:x\in C\land y\in (V\setminus C)\}|-|\{(u,z):z\in N(u)\setminus C\}|+|\{(u,z):z\in N(u)\cap C\}|=\\&=|\{(x,y)\in E:x\in C\land y\in (V\setminus C)\}|-|N(u)\setminus C|+|N(u)\cap C|\\&\lt|\{(x,y)\in E:x\in C\land y\in (V\setminus C)\}|
\end{align*}$$
E dunque, $C'=C\setminus\{u\}$ è un sottoinsieme proprio e non vuoto di $V$ e il numero di archi del taglio indotto da $C'$ è minore del numero di archi del taglio indotto da $C$, contradicendo così l'ipotesi che $C$ è una cut-community $\blacksquare$

Okay, cut e weak web community sono correlate, ma abbiamo già cisto che c'è un problema che rimane tale, ovvero che nel calcolare la cut-community è difficile controllarne la cardinalità, e gli algoritmi che calcolano cut-communities possono restituire comunità contenenti un solo nodo (come nell'esempio), e quindi poco significative

Inoltre, non è detto che una cut-community di un solo nodo sia anche una web-community.

Se riprendiamo la figura dell'esempio, abbiamo che $C=\{u_0\}$ è una cut-community, ma l'insieme $C=\{u_0\}$ non può essere una web-community, perchè $u_0$ ha ovviamente più vicini in $V\setminus C$ che in $C$

## Partizionare un grafo in comunità

Prima di questo argomento ci sarebbe una piccola introduzione alla teoria della **NP-Completezza**, ma darò per scontato che chi leggerà questi appunti sappia bene di cosa stiamo parlando (anche perchè per leggere questi appunti bisogna essere iscritti in Magistrale, e in Triennale c'è un intero corso tenuto, sempre dalla cara Di Ianni, sulla NP-Completezza)

Più che individuare una singola comunità in un grafo quello che ci interessa è partizionare il grafo in comunità

Le motivazioni per questo interesse sono molteplici:
- esempio, conoscere le comunità può aiutarci a capire come fluisce l'informazione nella rete (in linea con l'esperimento di Granovetter)
- possiamo vedere come si diffondono idee, innovazioni, epidemie in quella rete (ci torneremo poi)
- serve anche a studiare reti di dimensioni molto molto grandi, riducendone la granularità (ossia, considerando le comunictà come se fossero dei **macro-nodi** e studiando il grafo dei macro-nodi)

**Oss**: Se $C$ è una cut-community, allora anche $V\setminus C$ è una cut-community, questo perchè $V\setminus C\neq V,V\setminus C\neq\emptyset$ e il taglio indotto da $V\setminus C$ è lo stesso di quello indotto da $C$

Perciò, un algoritmo che calcola un taglio minimo individua una partizione di un grafo in due comunità.

Inoltre, se C è una cut-community con $|C|\gt1\land|V\setminus C|\gt1$ allora $\langle C,V\setminus C\rangle$ è una partizione del grafo in due waek web-community
- semplice generalizzazione del teorema precedente

Detto questo quindi, possiamo affermare che è possibile calcolare una partizione di un grafo $G$ in due cut-communities in **tempo polinomiale in $|G|$**, ma ***non possiamo garantire che $|C|\gt1,|V\setminus C|\gt1$***

In effetti, calcolare una partizione di un grafo in due web-communities è un compito molto più complesso

Effettivamente, mentre esiste sempre una partizione di un grafo in due cut-communities (perchè un taglio minimo esiste sempre!), non è detto che sia sempre possibile partizionare in due web-communities

Vale quindi che, **decidere se un grafo è partizionabile in due web-communities è un problema NP-Hard**

Analizziamo quindi il problema in questione, dimostrando un teorema fondamentale

### Partizionare un grafo in due web-communities

>[!definition]- Problema Strong Web-Communities Partitioning (SWCP)
>Il problema **Strong Web-Communities Partitioning (SWCP)** è così definito.
>Dato un grafo $G=(V,E)$, ***decidere se esiste*** un sottoinsieme (proprio e non vuoto) $C$ di $V$ tale che $C$ e $V\setminus C$ sono due strong web-communities

Per risolvere il problema in questione, diamo l'enunciato e la dimostrazione del seguente teorema:

>[!teorem]- Teorema
>Il problema SWCP è NP-Completo

**dimostrazione teorema**

Prima di dimostrare il teorema, dimostriamo un lemma di appoggio

>[!teorem]- Lemma
>Se $G=(V,E)$ è partizionabile in due strong web-community ed esistono $x,y,z\in V$ tale che $N(x)=\{y,z\}$ (quindi $x$ ha grado $2$) ***allora*** $\forall C\subset V$ tale che $C$ e $V\setminus C$ sono due strong web-communities vale che $x,y,z\in C$ oppure $x,y,z\in V\setminus C$

**dimostrazione lemma**

Sia $C\subset V$ tale che $C$ e $V\setminus C$ sono due strong web-communities, w.l.o.g assumiamo che $x\in C$.
Vediamo i valori che $y,z$ possono assumere:
- $y\in V\setminus C,z\in V\setminus C\implies|N(x)\cap C|=0\lt|N(x)\cap(V\setminus C)|=2$
- $y\in C,z\in V\setminus C\implies|N(x)\cap C|=1=|N(x)\cap(V\setminus C)|$
	- analogamente se $y\in V\setminus C,z\in C$

In tutte e due i casi verrebbe contraddetta lìipotesi che $C$ e $V\setminus C$ sono due strong web-communities $\blacksquare$

Torniamo alla dimostrazione del teorema.

Il problema è in NP: un certificato valido per il problema è un sottoinsieme $C\subset V$, e verificare che $C$ e $V\setminus C$ sono strong web-communities richiede tempo **polinomiale** in $|G|$

Per dimostrare che il problema SWCP è NP-Completo, riduciamo ad esso il famoso problema $3$-SAT.

Siano $X=\{x_1,\dots,x_n\}$ e $f=c_1\land c_2\land\dots\land c_m$, con $c_j=l_{j1}\lor l_{j2}\lor l_{j3}$ e $l_{jh}\in X$ oppure $\lnot l_{jh}\in X$, per $j=1,\dots,m$ e $h=1,2,3$
- $f$ è un'istanza di $3$-SAT

Da qui, costruiamo un grafo costituito da:
- due nodi "specializzati" $T,F$ che potranno appartenere alla stessa comunità $C\iff C=V$[^3]
- un **gadget** per ogni variabile
- un **gadget** per ogni clausola

![[Pasted image 20250811103416.png|center|150]]

In figura i due nodi "specializzati" $T,F$ e il gadget per la variabile $x_i$:
- il gadget contiene i nodi $x_i,w_i,z_i,t_i,f_i$, e tanti nodi senza nome (quelli neri in figura): al nodo $x_i(w_i)$ sono collegati tanti nodi senza nome quante sono le clausole contenenti la variabile $x_i(\lnot x_i)$ più uno
	- nell'esempio la variabile $x_i$ è contenuta in due clausole e $\lnot x_i$ in una

Se $T,F$ sono in due comunità distinte, diciamo $T\in C$ e $F\in V\setminus C$, poichè $t_i,f_i$ hanno grado $2$ allora $T,t_i,y_i$ devono essere contenuti in $C$, e $F,f_i,z_i$ devono essere contenuti in $V\setminus C$

Per far sì che questo sia possibile, **è necessario che esattamente uno** dei nodi $x_i,w_i$ sia contenuto in $C$ ed **esattamente uno** dei nodi $x_i,w_i$ sia contenuto in $V\setminus C$, e ovviamente, ciascun nodo senza nome deve essere contenuto nella stessa comunità che contiene il padre.

![[Pasted image 20250811104217.png|center|350]]

In figura i due nodi "specializzati" $T,F$ e il gadget per la variabile $c_j$ e i suoi collegamenti con i gadget variabile:
- il gadget per la variabile $c_j$ contiene i nodi $c_j,l_{j1},l_{j2},l_{j3}$
- il nodo $c_j$ è collegato ai letterali contenuti nella clausola $c_j$: al nodo $x_i$ se $c_j$ contiene il letterarle $x_i$, al nodo $w_i$ se $c_j$ contiene il letterale $\lnot x_i$
	- nell'esempio in figura $c_j=x_1\lor\lnot x_2\lor x_3$

Se $T,F$ sono in due comunità distinte, diciamo $T\in C$ e $F\in V\setminus C$, poichè $l_{j1},l_{j2},l_{j3}$ hanno grado $2$ allora $T,c_j$ devono essere contenuti in $C$

Per far sì che questo sia possibile, **è necessario che almeno uno** dei nodi nei gadget variabile collegato a $c_j$ sia contenuto in $C$ [^4], altrimenti $c_j$ avrebbe tanti vicini in $C$ quanti in $V\setminus C$

![[Pasted image 20250811104931.png|center|500]]

Una visione di insieme: in figura abbiamo la funzione $$f(x_1,x_2,x_3)=c_1\land c_2,\quad c_1=x_1\lor\lnot x_2\lor x_3,c_2=\lnot x_1\lor\lnot x_2\lor\lnot x_3$$
Se $T,F$ sono **nella stessa comunità** $C$, allora tutti i nodi sono in $C$:
- per ogni $1\leq j\leq m$: poichè $l_{j1},l_{j2},l_{j3}$ hanno grado $2$ allora $l_{j1},l_{j2},l_{j3},c_j$ devono essere contenuti in $C$
- per ogni $1\leq i\leq n$: poichè $t_i,f_i$ hanno grado $2$ allora $t_i,y_i,f_i,z_i$ devono essere contenuti in $C$
- Allora, per ogni $1\leq i\leq n$: se il letterale $x_i$ è contenuto in $k$ clausole allora il nodo $x_i$ ha $k+2$ vicini con nome in $C$
	- perciò, per poter essere inserito in $V\setminus C$ il nodo $x_i$ dovrebbe avere almeno $k+2$ vicini in $V\setminus C$, ma gli altri vicini di $x_i$ sono $k+1$ nodi senza nome, e non sono abbastanza per permettere a $x_i$ di non far parte di $C$ !
	- Perciò, se $x_i$ e i $k+1$ nodi senza nome ad esso collegati devono essere in $C$
- Analogamente il tutto può essere fatto per il letterale $\lnot x_i$ e il nodo $w_i$

![[Pasted image 20250811110657.png|center|500]]

Una visione d'insieme: Se $T,F$ sono due comunità diverse allora:
- per ogni clausola $c_j$ i nodi $l_{j1},l_{j2},l_{j3},c_j$ sono con $T$ (rossi)
- per ogni variabile $x_i$ i nodi $t_i,y_i$ sono con $T$ (rossi) e i nodi $f_i,z_i$ sono con $F$ (blu)
- Allora, dobbiamo 'colorare' i nodi $x_i,w_i$ per ogni variaible $x_i$, in modo che l'insieme dei nodi rossi e l'insieme dei nodi blu siano due strong web-communities

Vale quindi che $G$ è partizionabile in due strong web-communites $C,V\setminus C$ se e solo se $T,F$ **non** sono entrambi in $C$ e **non** sono entrambi in $V\setminus C$ 

Affinchè $T\in C,F\in V\setminus C$ devono valere due punti:
1) Per ogni variabile $x_i\in X$, **esattamente uno dei nodi** $x_i,w_i$ deve essere contenuto in $C$ ed **esattamente uno dei nodi** $x_i,w_i$ deve essere contenuto in $V\setminus C$
	1) allora, ogni partizione di $G$ in due strong web-communites corrisponde ad una assegnazione di verità di $a$ per $X$: possiamo decidere, per ogni $i\in[n]$, che se $x_i\in C$ (insieme con $T$) e $w_i\in V\setminus C$ allora $a(x_i)=$vero, mentre se $x_i\in V\setminus C$ e $w_i\in C$ allora $a(x_i)$=falso, e anche viceversa ovviamente
	2) ma in base a quale criterio scegliamo? in base all'insieme dove collochiamo i nodi $c_j$ (vedi poi)
2) Per ogni clausola $c_j$, il nodo $c_j$ **deve** appartenere a $C$ (che contiene $T$)
	1) e perchè questo sia possibile, è necessario che almeno uno dei nodi nei gadget variabile collegato a $c_j$ sia contenuto in $C$, ovvero uno dei nodi corrispondenti a un letterale nella clausola $c_j$ deve essere contenuto in $C$

Non ci resta che concludere la prova: mostriamo che $G$ è partizionabile in due strong web-communities se e solo se $f$ è soddisfacibile

**dimostrazione parte $\implies$**

Se $G$ è partizionabile in due strong web-communities $C,V\setminus C$ allora $T,F$ ***non*** sono nella stessa comunità; sia $T\in C,F\in V\setminus C$
Allora, per ogni variabile $x_i\in X$, esattamente uno dei nodi $x_i,w_i$ deve essere contenuto in $C$ ed esattamente uno dei nodi $x_i,w_i$ deve essere contenuto in $V\setminus C$

Allora poniamo 
$$\begin{align*}
&a(x_i)=\text{vero }\forall x_i\in X:x_i\in C\\&a(x_i)=\text{falso }\forall x_i\in X:x_i\in V\setminus C
\end{align*}
$$
Inoltre, per ogni clausola $c_j$, il nodo $c_j$ deve appartenere a $C$, e perchè questo sia possibile, è necessario che almeno uno dei nodi nei gadget variabile collegato a $c_j$ sia contenuto in $C$, ovvero uno dei nodi corrispondenti a un letterale nella clausola $c_j$ deve essere contenuto in $C$: sia $l_{jh}$ tale letterale, allora se 
$$\begin{align*}
&l_{jh}=x_i\implies x_i\in C\land a(x_i)=\text{vero}\\&l_{jh}=\lnot x_i\implies w_i\in C\land a(x_i)=\text{falso}
\end{align*}
$$
Quindi, $a(\cdot)$ è un **assegnazione di verità** che soddisfa ogni clausola di $f$, quindi $f$ è soddisfacibile

**dimostrazione parte $\Leftarrow$**

Se $f$ è soddisfacibile, sia $a(\cdot)$ una assegnazione di verità per $X$ che soddisfa ogni clausola $c_j\in f$ 

Costruiamo $C$: inseriamo in $C$
- il nodo $T$, e $\forall j\in[m]$ i nodi $c_j$ e $l_{j1},l_{j2},l_{j3}$
- per $i\in[n]$, i nodi $x_i,y_i,t_i$ e i senza nome adiacenti a $x_i$ tali che $a(x_i)$=vero
- per $i\in[n]$, i nodi $w_i,y_i,t_i$ e i senza nome adiacenti a $w_i$ tali che $a(x_i)$=falso

$C$ è una comunità, infatti dato che $a$ soddisfa tutte le clausole in $f$ , allora, per ogni $j = 1,\dots , m$, il nodo $c_j$ ha 4 dei suoi 7 vicini nella stessa comunità di $T$ (i tre nodi $l_{j1},l_{j2},l_{j3}$, oltre al nodo corrispondente al suo letterale vero): dunque, per ogni $j = 1,\dots , m$, il nodo $c_j$ può essere effettivamente inserito nella stessa comunità di $T$

Ragionamento simile per $V\setminus C$

La dimostrazione segue poi dal fatto che costruire $G$ richiede tempo polinomiale in $|f|$ e $X$, quindi abbiamo dimostrato con successo che il problema SWCP è NP-Completo $\blacksquare$

>[!info]
>Una dimostrazione alternativa di questo teorema può essere trovata nella Dispensa $2$ sulla pagina del corso

### Partizionare un grafo in comunità: approccio euristico

Sono stati proposti numerosi metodi "euristici" per partizionare un grafo in comunità, dove adesso con comunità intendiamo un insieme coeso di nodi

Per grandi linee, possiamo classificare le tecniche per il partizionamento di grafi in metodi partitivi (o divisivi) e metodi agglomerativi

In un **metodo partitivo** si inizia considerando l'intero grafo come un'unica grande comunità e poi, man mano, si rimuovono gli archi fino a quando il grafo risulta partizionato in componenti connesse
- il processo viene poi iterato su ciascuna componente, fino a quando si ottiene un livello di granularità ritenuto adeguato o un insieme di comunità di dimensioni ritenute adeguate

In un **metodo agglomerativo** si inizia considerando ciascun nodo come una piccola comunità e poi, man mano, si aggiungono gli archi del grafo fino a quando si ottengono un numero di comunità ritenuto adeguato o comunità di dimensioni adeguate

Sia i metodi partitivi che agglomerativi permettono di ottenere partizionamenti nidificati:
- in un metodo partitivo: ad ogni passo otteniamo comunità contenute in quelle ottenute al passo precedente
- in un metodo agglomerativo: ad ogni passo otteniamo comunità che contengono quelle ottenute al passo precedente

Così facendo otteniamo uno schema di partizionamento ad albero, come si vede dalla figura 

![[Pasted image 20250811142504.png|center|300]]

I diversi metodi partitivi/agglomerativi proposti si distinguono per il criterio utilizzato per scegliere ad ogni passo:
- quale arco rimuovere (partitivo)
- quale arco aggiungere (agglomerativo)

#### Betweenness di un arco

Vediamo ora un particolare criterio per rimuovere gli archi in un metodo partitivo

Il critero è basato sul concetto di **betweenness di un arco**, a sua volta basato sui concetti di bridge e local bridge:
- un bridge (per definizione) collega due regioni del grafo altrimenti non connesse
- un local bridge connette due regioni che, senza di esso, sarebbero connesse in modo meno efficiente
- perciò, possiamo dire che sia i bridge che i local brisge connettono regioni che, senza di loro, avrebbero difficoltà ad interagire

Inoltre, abbiamo visto che i brisge e local bridge sono **weak ties**, e gli archi che rimangono dopo la loro rimozione sono gli **strong ties** - quelli delle relazioni forti

Da queste considerazioni nasce l'idea: rimuovendo bridge e local brisge il grafo viene partizionato in componenti che bene possono essere considerate comunità

Ma la domanda sorge spontanea: cosa succede se la rete appare come in figura? quindi senza local bridge ma con due regione dense?

![[Pasted image 20250811143351.png|center|250]]

Per rispondere a questa domanda, dobbiamo utilizzare una proprietà diversa da quella di (local) bridge [^5]

Questa proprietà è basata sulla nozione di traffico: gli archi che possiamo considerare i "nuovi ponti" sono quelli attraverso i quali passa **più traffico**, il che sembra ragionevole, e il traffico lo possiamo misurare con una sorta di flusso di un qualche fluido:
- per ogni coppia di nodi $s,t$ assumiamo che $s$ voglia inviare a $t$ un'unità di flussp che, viaggiando nella rete, si suddivide equamente fra tutti gli shortest paths che collegano $s,t$

La **betweenness di un arco** è quindi la quantità totale di fluido che lo attraversa, ottenuta sommando le frazioni di fluido per tutte le coppie $(s,t)$

Un'arco è tanto più "nuovo ponte" quanto maggiore è la sua betweenness

Descriviamola formalmente:

>[!definition]- Betweenness di un arco
>Dato un grafo $G=(V,E)$ (non orientato), per ogni coppia di nodi $(s,t)\in V$ e per ogni arco $(u,v)\in E$ definiamo $$\sigma_{st}(u,v)=\text{num. shortest paths fra s e t che attraversano (u,v)}$$
>La betweenness **relativa** di $(u,v)$ rispetto alla coppia $(s,t)$ è la frazione degli shortest paths fra $s,t$ che attraversano $(u,v)$, ovvero:
>$$b_{st}(u,v)= \frac{\sigma_{st}(u,v)}{\sigma_{st}}$$
>Infine, la **betweenness di un arco** $(u,v)\in E$ è la semi-somma delle betweenness relative ad ogni coppia di nodi, quindi: 
>$$b(u,v)=\frac{1}{2}\sum\limits_{s,t\in V}(b_{st}(u,v))$$[^6]


#### Il metodo di Girvan-Newman

Il metodo di Girvan-Newman è un metodo partitivo basato sulla betweenness:
- si inizia considerando l'itero grafo come una grande comunità
- poi si calcola l'arco di betweenness massima e si rimuove; se il grafo residuo è non connesso allora è stata ottenuta una prima partizione in comunità
- il procedimento viene poi iterato calcolando gli archi di betweenness massima e rimuovendoli
- si termina quando si raggiunge un livello di granularità ritenuto adeguato

Come facciamo però per calcolare la betweenness di un arco? Provare a calcolare tutti gli shortest paths di un grafo è una cosa impensabile, dato che il loro numero è esponenziale nelle dimensioni del grafo (dovreste già saperla questa cosa)

Vediamo allora uno schema algoritmico per calcolare la betweenness di un arco.

Per ogni $s\in V$ si eseguono i seguenti passaggi:
1) calcola il sottografo $T(s)$ degli shortest paths uscenti da $s$ mediante una BFS
2) mediante visita top-down di $T(s)$, per ogni $v\in V$ calcola $\sigma_{sv}$
3) mediante visita bottom-up di $T(s)$, e usando quanto calcolato al punto 2, per ogni $(u,v)\in T(s)$ calcola $b_{s}(u,v)=\sum\limits_{t\in V\setminus\{s\}}b_{st}(u,v)$[^7]

Infine, per ogni $(u,v)\in E$ calcola $b(u,v)=\frac{1}{2}\sum\limits_{s\in V}b_{s}(u,v)$

Vediamo nel dettaglio i singoli punti

##### 1) BFS da $s\in V$

Calcoliamo $T(s)$ come insieme di archi e, contemporaneamente, una partizione in livelli di $V$:
- $L_{0}\gets\{s\},T(s)\gets\emptyset$
- per $h\geq0$  e finchè $L_{h}\neq\emptyset$ calcola $$\begin{align*}
&L_{h+1}\gets\left\{u\in V\setminus\bigcup_{0\leq i\leq h}L_{i}:\exists v\in L_{h}:(v,u)\in E\right\}\\&T(s)\gets\left\{(u,v)\in E:v\in L_{h}\land u\in L_{h+1}\right\}
\end{align*}$$
![[Pasted image 20250811150601.png|center|400]]


##### 2) Visita top-down di $T(s)$

##### 3) Visita bottom-up di $T(s)$

[^1]: segue dall'esperimento Granovetter che i bridge sono gli archi che hanno maggiore "valore informativo"

[^2]: grafo dinamico: grafo che evolve nel tempo

[^3]: Così facendo risulta che C non è una comunità, poichè non è contenuta propriamente in $V$

[^4]: nell'esempio in figura almeno uno fra $x_1,w_2,x_3$ deve essere contenuto in $C$

[^5]: anche se, come il (local) bridge, vuole ancora descrivere una crescente difficoltà di collegamento indotta dalla rimozione di un arco che la soddisfa

[^6]: NB: quella che abbiamo definito è la ***edge***-betweenness; analogamente si può definire la node-betweenness

[^7]: qui calcoliamo $b_{s}(u,v)$ per i soli archi $(u,v)\in T(s)$. Infatti, gli archi che non sono in $T(s)$ non fanno parte di alcuno shortest paths uscente da $s$
