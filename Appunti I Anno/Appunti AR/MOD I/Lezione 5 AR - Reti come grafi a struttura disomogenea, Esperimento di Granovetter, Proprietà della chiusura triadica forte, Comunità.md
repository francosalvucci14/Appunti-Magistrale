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

## Comunità e coefficiente di clustering

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

### Cut-Communities

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

### Web-Communities

Definiamo ora il concetto di **web-communities**

>[!definition]- Web-Community
>Una **web-community** è un sottoinsieme dei nodi di un grafo, ciascuno dei quali ha più vicini fra i nodi del sottoinsieme che fra quelli esterni ad esso.
>Formalmente, dato un grafo $G=(V,E),C\subset V$ è una (**strong**) web-community se $C\neq\emptyset$ e $$\forall u\in C:|N(u)\cap C|\gt|N(u)\setminus C|=|N(u)\cap (V\setminus C)|$$
>- equivalentemente, dato che $|N(u)\cap C|+|N(u)\setminus C|=|N(u)|,\frac{|N(u)\cap C|}{|N(u)|}\gt \frac{1}{2}$
>
>Analogamente, dato un grafo $G=(V,E),C\subset V$ è una (**weak**) web-community se $C\neq\emptyset$ e $$\forall u\in C:|N(u)\cap C|\geq|N(u)\setminus C|$$
>- equivalentemente $\frac{|N(u)\cap C|}{|N(u)|}\geq \frac{1}{2}$

Definizione semplice e intuitivamente ragionevole (se col cazzo), che può essere generalizzata richiedendo $$\frac{|N(u)\cap C|}{|N(u)|}\gt \alpha(\geq\alpha)$$per qualche $\alpha\in[0,1]$

#### Cut e weak Web-Communities

Le definizioni di cut e web community non sono del tutto scorrelate, vale infatti il seguente teorema:

>[!teorem]- Teorema
>Sia $G=(V,E)$ un grafo, se $C\subset V$ è una cut-community per $G$ tale che $|C|\gt1$ allora $C$ è una weak web-community

**dimostrazione**

Supponiamo **per assurdo** che $C$ non sia una weak web-community, allora esiste un nodo $u\in C:|N(u)\cap C|\gt|N(u)\setminus C|$.
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

[^1]: segue dall'esperimento Granovetter che i bridge sono gli archi che hanno maggiore "valore informativo"

[^2]: grafo dinamico: grafo che evolve nel tempo
