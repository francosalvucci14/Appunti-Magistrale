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
# Il World Wide Web

Nella serie di lezioni corrispondenti a questi lucidi ci interessiamo al problema di individuare all’interno di una rete ed estrarre da essa informazioni rilevanti ad una data richiesta, e lo faremo nel caso in cui la rete sia il Web
- che è una rete diversa dalle reti fino ad ora considerate in questo corso, perché è una rete costituita da documenti, collegati mediante hyperlink

Naturalmente, utilizzeremo ancora il grafo come modello di rete e, questa volta, lo strumento sarà l’algebra lineare (super dio cane)

**Il World Wide Web** è un’applicazione progettata per condividere informazione su Internet, da Tim Berners-Lee, il cui progetto è basato su una architettura client-server
- i documenti sono resi disponibili, sotto forma di pagine web, memorizzandoli in zone pubblicamente accessibili di taluni computer (server)
- e l’accesso a tali pagine avviene mediante un’applicazione (browser) eseguita dal client e che accede agli spazi pubblici dei server

Il principio logico fondazionale del web è l’**ipertesto**
- nel quale l’informazione è organizzata in una struttura di rete, ovvero i documenti che costituiscono il web sono nodi di un grafo diretto
- si tratta, perciò di una organizzazione non lineare

L’ipertesto è una implementazione del concetto di ***memoria associativa***

Esistono in effetti numerosi precursori dell'ipertesto:
- le citazioni
- i crossing reference
- le mappe concettuali
- etc..

Vediamo ora il prototipo **MEMEX**
# MEMEX

Vannevar Bush, in un articolo del 1945 (“As we may think”) provò a immaginare in che modo la nascente tecnologia dell’informazione poteva modificare il modo in cui le informazioni vengono memorizzate, e con il quale si può accedere ad esse

Egli osservò che, mentre i metodi tradizionali per rappresentare l’informazione (in
libri, ma anche in biblioteche) sono sostanzialmente lineari, il modo in cui l’essere umano pensa e memorizza (e accede a) le sue esperienze è ***associativo***
- inizia a pensare a una cosa, che gliene fa venire in mente una seconda, e così via

Bush immaginò anche un prototipo: **MEMEX**
- una versione digitalizzata della conoscenza umana nella quale i dati sono collegati da link associativi

# Struttura del web

Inizialmente, il Web era costituito da un insieme di pagine al cui interno erano (possibilmente) presenti alcuni **hyperlink**, ciascuno dei quali collegava quella pagina ad un’altra pagina
- sono appunto gli hyperlink che implementano l’idea di memoria associativa

Con il tempo, il Web si è evoluto:

Intorno all’ossatura costituita dalle pagine "statiche", sono state progettate anche pagine che permettevano di *eseguire azioni*, e i link contenuti in queste pagine permettono di concludere le azioni (vengono chiamati **transazionali**, per distinguerli dai link **navigazionali**)

Anche il Web "navigazionale" può essere modellato come un grafo, in particolare, come un grafo diretto:
- i cui nodi sono le pagine
- ed esiste un arco diretto $(u, v)$ se la pagina ***$u$ contiene un hyperlink alla pagina $v$***
	- in questo caso diciamo che ***$u$ punta a $v$***

Osserviamo che i nodi non hanno coscienza degli archi entranti: infatti una pagina Web non ha modo di conoscere le pagine che la puntano

![center|350](img/Pasted%20image%2020250827151834.png)

In `[Broder et al., 2000]` viene studiata la struttura del grafo del web
- ogni nodo del grafo studiato è una **SCC** del grafo del Web, ed è stato rilevato che esso aveva una struttura bow-tie contenente una (unica) SCC gigante

Affrontiamo ora il problema di ricerca e classificazione di documenti all'interno del Web
# Ricerca e classificazione

La ricerca di documenti è un problema antico, ma tradizionalmente, era richiesta solo in ambiti specifici, e tipicamente, la difficoltà nella ricerca era causata dalla scarsità di documenti disponibili.

L'avvento del Web ha cambiato sostanzialmente le carte in tavola, e la difficoltà è ora la sovrabbondanza di documenti disponibili

Il Web infatti è un'immensa collezione di documenti appartenenti alle categorie più disparate, e chiunque cerca nel Web.

In questo modo, il numero di parole chiave da utilizzare per effettuare una ricerca sul web è ***potenzialmente illimitato***, e la stessa parola può avere tanti *significati diversi*

Perciò, affinché uno strumento di web search sia effettivamente efficace, è necessario che disponga di mezzi che gli permettano di "sfoltire" l’immensa mole di pagine individuate in prima battuta come risposta ad una richiesta, eliminando le pagine ritenute meno rilevanti, così da proporre al cercatore una lista di pagine relativamente breve
- e, soprattutto, nella quale le pagine siano elencate in ordine di (presunta) rilevanza non decrescente
- ovvero, individuando un **ranking** delle pagine più rilevanti

## Link Analysis

Le caratteristiche interne di una pagina non consentono, da sole, di capire quanto una pagina sia rilevante per una ricerca.

Ci vengono in aiuto gli hyperlink, e per capire il perchè di questo facciamo un breve esempio esplicativo

ESEMPIO: stiamo preparando la tesi di laurea
- il relatore ci indica un articolo sull'argomento sul quale verterà la tesi, e ci dice, per approfondire, che possiamo attingere alla bibliografia di quell'articolo
- andiamo a guardare la bibliografia e ci accorgiamo che consta di "numero a cazzo" riferimenti
- il problema è che non possiamo leggerli tutti, dobbiamo quindi capire quali tra quelli sono i più rilevanti, ai fini della nostra tesi.
- la risposta è semplice, se in bibliografia c'è un articolo che e stato citato dalla maggioranza degli altri, esso sarà, molto probabilmente, un articolo molto rilevante anche per il nostro argomento

Generalizziamo l'esempio.

Dopo aver individuato un insieme di pagine significative rispetto a una richiesta, consideriamo maggiormente rilevanti le pagine che sono molto puntate da altre pagine nell'insieme

Per capirci meglio, sarà proprio la struttura del grado del Web a fornirci le indicazioni circa la rilevanza di una determinata pagina web

Questa rilevanza sarà quindi calcolata tramite **analisi dei link** che la coinvolgono
### HITS : Hubs and Authorities

Abbiamo detto che la rilevanza di una pagina web sarà calcolata tramite analisi dei link che la coinvolgono, bene, ma non è tutto oro quel che luccica

Il primo problema che ci si para davanti è: quando una pagina è autorevole nel suo conferire rilevanza ad una pagina alla quale punta?

Per rispondere alla domanda dobbiamo introdurre ed analizzare un metodo, molto importante, proposto da Kleinberg.

Il metodo in questione è il metodo **Hyperlink-Induced Topic Search (HITS; Hubs and Authorities)**

Osserviamo intanto che, ad ogni pagina, possiamo associare due indici:
- un indice di **autorità** : che esprime la *rilevanza* della pagina ai fini della ricerca
- un indice di **hub** : che esprime l'**autorevolezza** della pagina a conferire autorità alle pagine alle quali punta

Potremmo pensare che il valore di autorità di una pagina $i$, che indichiamo con $a_{i}$ , sia il numero di pagine nell'insieme di pagine attinenti alla ricerca che puntano ad essa, ovvero detto in termini matematici, $$a_i=|\{j:j\text{ è attinente alla ricerca}\land j\to i\}|,\quad j\to i=\text{pagina j punta alla pagina i}$$
Ora, se indichiamo con $M$ la matrice di adiacenza del sottografo del Web attinente alla ricerca, assumendo che contenga $n$ pagine, ovvero $$1\leq i,j\leq n,M[i,j]=\begin{cases}1&j\to i\\0&\text{altrimenti}\end{cases}$$
allora possiamo scrivere $a_i$ come $$a_i=\sum\limits_{1\leq j\leq n}M[j,i]$$
Analogamente, il valore di hub di una pagina $i$, indicato con $h_{i}$, potrebbe essere il numero di pagine nell'insieme delle pagine attinenti alla ricerca alle quali esse punta, ovvero in termini matematici $$h_i=|\{j:j\text{ è attinente alla ricerca}\land i\to j\}|,\quad i\to j=\text{pagina i punta alla pagina j}$$
E quindi, rifacendo il discorso della matrice anche qui otteniamo che $$h_{i}=\sum\limits_{1\leq j\leq n}M[i,j]$$
In realtà, possiamo raffinare l'idea appena illustrata osservando che:
- il valore di autorità di una pagina è tanto più elevato quanto più autorevoli sono le pagine che la puntano
- il valore di hub è tanto più elevato quanto più rilevanti sono le pagine a cui essa punta

Quindi, se in qualche modo ci viene suggerito un valore di hub iniziale $h_i^{(0)}$ per ciascuna pagina $i$, allora possiamo dire che $$a_i^{(1)}=\sum\limits_{1\leq j\leq n}M[j,i]h_j^{(0)}$$
Ma allora, essendo variato il valore di autorità di ciascuna pagina, potremmo ricalcolare i valori di hub per ottenere una valutazione più raffinata:
$$h_{i}^{(1)}=\sum\limits_{1\leq j\leq n}M[i,j]a_j^{(1)}$$
A questo punto, i nuovi valori di hub ci permetterebbero di raffinare i valori di autorità, e così via, ottenendo un **procedimento iterativo**
$$\begin{align*}
&a_i^{(k+1)}=\sum\limits_{1\leq j\leq n}M[j,i]h_j^{(k)}\\&h_{i}^{(k+1)}=\sum\limits_{1\leq j\leq n}M[i,j]a_j^{(k+1)}
\end{align*}$$

C'è un piccolo problema, in generale all'inizio non si hanno informazioni circa il valore di hub delle pagine che si stanno considerando.

In questo caso, possiamo assumenre che tali valori siano uguali per tutte le pagine, e quindi $$h_{i}^{(0)}=1\space\forall 1\leq i\leq n$$
Le due forme $$\begin{align*}
&a_i^{(k+1)}=\sum\limits_{1\leq j\leq n}M[j,i]h_j^{(k)}\\&h_{i}^{(k+1)}=\sum\limits_{1\leq j\leq n}M[i,j]a_j^{(k+1)}
\end{align*}$$
possono essere scritte in forma compatta, ovvero:
$$\begin{align*}
&a^{(k+1)}=M^{T}h^{(k)}\\&h^{(k)}=Ma^{(k)}
\end{align*}$$
dove:
- $a^{(k+1)},a^{(k)},h^{(k)}$ sono vettori colonna - ad esempio $a^{(k)}=\left(a_1^{(k)},a_2^{(k)},\dots,a_n^{(k)}\right)$
- $M^{T}$ è la matrice trasposta di $M$
- $M^{T}h^{(k)},Ma^{(k)}$ indicano il consueto prodotto righe per colonne fra matrice e vettore

L'obiettivo ora è ottenere, ad ogni iterazione, valori che descrivano meglio (rispetto all'iterazione precedente) la rilevanza di una pagina ai fini della ricerca; ma perchè questo accada, è necessario che vi sia una sorta di convergenza verso certi valori limite che, in tal caso, sarebbero i "veri" valori di hub e di authority delle pagine

Osserviamo subito che la convergenza vera e propria non si può avere: infatti le espressioni che permettono di calcolare i vettori $a^{(k)}$ e $h^{(k)}$ sono somme di termini non negativi

Dunque possiamo parlare di convergenza solo in presenza di opportuna **normalizzazione**

In effetti, vale il seguente teorema

>[!teorem]- Teorema Principale
>Esistono un valore $c\in\mathbb R^{+}$ e un vettore $\hat z\in\mathbb R^{n}$ non nullo tali che, comunque si scelga un vettore $h^{(0)}$ a coordinate positive, $$\lim_{k\to\infty}\frac{h^{(k)}}{c^{k}}=\lim_{k\to\infty}\frac{a^{(k)}}{c^{k}}=\hat z$$ 

^1acb62

Prima di dimostrare il teorema, richiamiamo qualche nozione di algebra lineare:

Data una matrice quadrata $A\in Mat(n\times n)$, un vettore (complesso) $n$-dimensionale $\hat x$ e un numero $\lambda\in\mathbb C$ non nullo sono, rispettivamente, un **autovettore** e un **autovalore** per $A$ se $$A\hat x=\lambda\hat x$$
Vediamo, adesso, un paio di strumenti concernenti la relazione fra la struttura di $A$ e quella degli insiemi degli autovettori e degli autovalori di $A$ che giocheranno un ruolo fondamentale ai fini della dimostrazione della convergenza del metodo HITS, ovvero, del Teorema Principale qui sopra

>[!teorem]- Teorema 1
>Se $A$ è una matrice reale e simmetrica $n\times n$, allora $A$ ha $n$ autovalori e $n$ autovettori reali e, inoltre, gli autovettori formano una base ortonormale per $\mathbb R^{n}$

Una **base** per $\mathbb R^{n}$ è un insieme di $n$ vettori $\hat z_{1},\hat z_{2},\dots,\hat z_{n}$ tali che ogni altro vettore $x\in\mathbb R^n$ può essere come combinazione lineare di $\hat z_{1},\hat z_{2},\dots,\hat z_{n}$, ossia: $$\forall x\in\mathbb R^{n}:x=\sum\limits_{1\leq i\leq n}p_iz_i$$
**ortonormale** : detto $\hat z_i=\left(z_{i1},z_{i2},\dots,z_{in}\right)$ si ha che 
$$\begin{align*}
\forall i=1,\dots,n:\hat z_{i}\cdot\hat z_{i}=\hat z_{i1}^2+\hat z_{i2}^2+\dots+\hat z_{in}^2=1\quad&\text{(normalità)}\\\forall i\neq l:\hat z_{i}\cdot\hat z_{l}=\hat z_{i1}\hat z_{l1}+\hat z_{i2}\hat z_{l2}+\dots+\hat z_{in}\hat z_{ln}=0\quad&\text{(ortogonalità)}
\end{align*}$$

Una matrice $A$ simmetrica e reale si dice **semidefinita positiva*** se $$\forall\hat x\in\mathbb R^{n}:\hat x^{T}A\hat x\geq0$$

>[!teorem]- Teorema 2
>Se $A$ è una matrice semidefinita positiva allora:
>1) gli autovalori di $A$ sono non negativi
>2) se $A$ è non nulla allora almeno un autovalore di $A$ è strettamente positivo


Bene, torniamo ora al [](.md#^1acb62|Teorema%20Principale), vedremo a breve il ruolo dei due teoremi appena descritti nella dimostrazione del teorema principale

Intanto, osserviamo che $(MM^{T})$ è una matrice reale e simmetrica, infatti $$(MM^{T})_{ij}=\sum\limits_{1\leq k\leq n}M_{ik}M_{kj}=(MM^{T})$$
Allora, $(MM^{T})$ ha una **base ortonormale di autovettori per $\mathbb R^{n}$ e tutti gli autovalori reali**

$(MM^{T})$ è anche semidefinita positiva, infatti comunque scelgo $\hat x\in\mathbb R^{n}$ si ha $$\hat x^{T}(MM^{T})\hat x=(\hat x^{T}M)(M^{T}\hat x)$$ e dunque, ponendo $(M^{T}\hat x)=y=(y_1,y_2,\dots,y_n)$ si ottiene $$\hat x^{T}(MM^{T})\hat x=y^{T}y=\sum\limits_{1\leq k\leq n}y_{k}^{2}\geq0$$
Allora, poichè $(MM^{T})$ è non nulla, il suo **autovalore massimo è strettamente positivo**

Cominciamo ora, finalmente, con la dimostrazione del Teorema Principale [^1]

**dimostrazione**

Cominciamo scrivendo in modo diverso le formule per calcolare $h^{(k)},a^{(k)}$:
$$\begin{align*}
&h^{(1)}=Ma^{(1)}=MM^{T}h^{(0)}\quad\text{poichè }a^{(k+1)}=M^{T}h^{(k)}\forall k\\&h^{(2)}=Ma^{(2)}=MM^{T}h^{(2)}=(MM^{T})(MM^{T})h^{(0)}=(MM^{T})^{2}h^{(0)}\\
&h^{(3)}=Ma^{(3)}=MM^{T}h^{(3)}=(MM^{T})(MM^{T})^2h^{(0)}=(MM^{T})^{3}h^{(0)}\\
&\vdots
\end{align*}$$

e così via, induttivamente, possiamo esprimere $h^{(k)}$ nelle due forme $$\begin{align*}
&h^{(k)}=MM^{T}h^{(k-1)}\\
&h^{(k)}=(MM^{T})^{k}h^{(0)}
\end{align*}$$
Scegliamo un vettore $h^{(0)}$ a coordinate positive.

$(MM^{T})$ è una matrice simmetrica, semidefinita positiva e non nulla:
- siano $\hat z_{1},\hat z_{2},\dots,\hat z_{n}$ i suoi autovettori reali - **base** ortonormale per $\mathbb R^{n}$
- sia, per $i=1,\dots,n,c_i$ l'autovalore **reale e non negativo** corrispondente a $\hat z_i$, quindi $(MM^{T})\hat z_i=c_i\hat z_i$
- w.l.o.g assumioamo che $c_{1}\geq c_2\geq\dots\geq c_n$ e $c_1\gt0$

Allora, possiamo esprimere $h^{(0)}$ come combinazione lineare degli autovettori: $$h^{(0)}=\sum\limits_{1\leq i\leq n}q_i\hat z_i$$
E dunque, 
$$\begin{align*}
h^{(k)}&=(MM^{T})^{k}h^{(0)}=(MM^{T})^{k}\sum\limits_{1\leq i \leq n}q_i\hat z_i\\
&=(MM^{T})^{k-1}\sum\limits_{1\leq i \leq n}q_i(MM^{T})\hat z_i\\
&=(MM^{T})^{k-1}\sum\limits_{1\leq i \leq n}q_i c_i\hat z_i\quad\text{per definizione di autovalore}\\
&=(MM^{T})^{k-2}\sum\limits_{1\leq i \leq n}q_i c_i(MM^{T})\hat z_i=(MM^{T})^{k-2}\sum\limits_{1\leq i \leq n}q_i c_i^{2}\hat z_i\\
&=\dots=\sum\limits_{1\leq i \leq n}q_i c_i^{k}\hat z_i
\end{align*}$$

Ora dividiamo ambo i membri per $c_1^{k}$ e otteniamo
$$\frac{h^{(k)}}{c_{1^k}}=\sum\limits_{1\leq i\leq n}q_i\left(\frac{c_i}{c_1}\right)^k\hat z_i$$
Sia $l\leq n$ tale che $c_1=c_2=\dots=c_l\gt c_{l+1}\geq c_{l+2}\geq\dots\geq c_n$

Allora,
$$\begin{align*}
\lim_{k\to\infty}\frac{h^{(k)}}{c_1^{k}}&=\lim_{k\to\infty}\left[q_1\hat z_1+\dots+q_l\hat z_l+q_{l+1}\left(\frac{c_{l+1}}{c_{1}}\right)^k\hat z_{l+1}+\dots+q_{n}\left(\frac{c_{n}}{c_{1}}\right)^k\hat z_{n}\right]\\
&=q_1\hat z_1+q_2\hat z_2+\dots+q_l\hat z_l
\end{align*}$$

[^2]

Resta ora da mostrare che $q_1\hat z_1+q_2\hat z_2+\dots+q_l\hat z_l$ è un vettore non nullo, e lo dimostriamo solo nel caso particolare $l=1$, ovvero $c_{1}\gt c_2$

Se $c_{1}\gt c_2$ allora $$\lim_{k\to\infty}\frac{h^{(k)}}{c_1^{k}}=\lim_{k\to\infty}\frac{(MM^{T})^{k}h^{(0)}}{c_1^{k}}=q_1\hat z_{1}$$
Per completare la dimostrazione del teorema è sufficiente mostrare che, *comunque si scelga un vettore $h^{(0)}$ a coordinate positive*, $q_1\neq0$
- infatti $\hat z_1$ è un vettore reale perchè elemento di una base di $\mathbb R^{n}$
- $\hat z_1$ è anche un vettore non nullo perchè la base è ortonormale: $\hat z_1\cdot\hat z_{1}=\hat z_{11}^2+\hat z_{12}^2+\dots+\hat z_{1n}^2=1$

Innanzi tutto, osserviamo che $q_{1}=h^{(0)}\cdot\hat z_1$
- infatti $$h^{(0)}\cdot\hat z_{1}=\left(\sum\limits_{1\leq i\leq n}q_i\hat z_i\right)\cdot\hat z_1=\sum\limits_{1\leq i\leq n}q_i(\hat z_i\cdot\hat z_1)=q_i(\hat z_1\cdot\hat z_1)=q_1$$
- allora, $$q_1\neq0\iff h^{(0)}\cdot\hat z_1\neq0$$

Allora dobbiamo dimostrare che, *comunque si scelga un vettore $h^{(0)}$ a coordinate positive*, $$h^{(0)}\cdot\hat z_1\neq0$$
Lo dimostreremo in due punti

**Punto $1)$** : iniziamo dimostrando che ***esiste*** un vettore $\hat y$ a coordinate positive tale che $\hat y\cdot\hat z_1\neq0$
- ricordiamo che $\hat z=(\hat z_{11},\hat z_{12},\dots,\hat z_{1n})$ nel sistema di riferimento iniziale
- supponiamo per assurdo che per ogni $\hat x\in\mathbb R^{n}$ a coordinate positive sia $\hat x\cdot\hat z_{1}=0$
- sia $\hat y\in\mathbb R^{n}$ tale che $\hat y=(\hat y_{1},\hat y_{2},\dots,\hat y_{n})$ con $\hat y_{i}\gt0$ per ogni $i=1,\dots,n$, e sia, per ogni $l=1,\dots,n,\hat y^{(l)}$ il vettore tale che $\hat y^{(l)}_i=\hat y_i\forall i\neq l$ e $\hat y^{(l)}_l=\hat y_l+1$ [^3] 
- allora, per ogni $l=1,\dots,n$ vale che $$\begin{cases}
\hat y\cdot\hat z_{1}=0\\\hat y^{(l)}\cdot\hat z_{1}=0
\end{cases}$$ovvero $$\begin{cases}
\hat y_1\hat z_{11}+\dots+\hat y_l\hat z_{1l}+\dots+\hat y_n\hat z_{1n}=0 \\
\hat y_1\hat z_{11}+\dots+(\hat y_l+1)\hat z_{1l}+\dots+\hat y_n\hat z_{1n}=0
\end{cases}$$da cui, sottraendo la prima equazione alla seconda, otteniamo che $\hat z_{1l}=0$

Quindi, $$\forall l=1,\dots,n\to\hat z_{1l}=0\quad\text{ assurdo perchè }\hat z_{1}\cdot\hat z_{1}=1$$
**Punto $2)$** : mostriamo che per ogni vettore $\hat x$ a coordinate positive vale che $\hat x\cdot\hat z_1\neq0$
- sia $\hat y \in\mathbb R^{n}$ a coordinate positive un vettore tale che $\hat y \cdot\hat z_1 \neq 0$ ($\hat y$ esiste per punto $1$)
- esprimiamo $\hat y$ nel sistema $$\hat z_1, \dots , \hat z_n : \hat y = p_1\hat z_1 + p_2 \hat z_2 + \dots + p_n \hat z_n$$
- allora, come abbiamo visto, l’espressione $\frac{(MM^{T})^k\hat y}{c_{1}^k}$ converge a $p_1\hat z_1$
- e poiché l’espressione $\frac{(MM^{T})^k\hat y}{c_{1}^{k}}$ contiene solo valori non negativi allora le coordinate di $p_1\hat z_1$ sono tutte non negative, e poiché $p_1= \hat y\cdot \hat z_1 \neq 0$, allora $p_1\hat z_1$ ha almeno una coordinata strettamente positiva
- sia $\hat x = (\hat x_1, \hat x_2, \dots , \hat x_n)$ un qualunque vettore in $\mathbb R^n$ a coordinate positive tale che $x \neq y$
- allora nell’espressione $$p_1 \hat z_1 \cdot \hat x = p_1 \hat z_{11}\hat x_1 + p_1 \hat z_{12}\hat x_2 + \dots + p_1 \hat z_{1n}\hat x_n$$tutti gli addendi sono non negativi e almeno uno di essi è positivo

E quindi, $$\hat x \cdot \hat z_1 = \hat z_1 \cdot x = \frac{1}{p_1}\left(p_1 \hat z_{11}\hat x_1 + p_1 \hat z_{12}\hat x_2 + \dots + p_1 \hat z_{1n}\hat x_n\right) \neq 0\quad\quad\blacksquare$$
Due osservazioni riguardo al teorema

**oss $1$** : Abbiamo dimostrato che $\hat z$ è non nullo nel solo caso $c_1\gt c_2$: tecniche analoghe permettono di dimostralro nel caso generale

**oss $2$** : come abbiamo visto nel caso $c_{1}\gt c_2$, qualunque sia il vettore iniziale $h^{(0)}$ a coordinate positive, $\frac{h^{(k)}}{c_1^{k}}$ converge al vettore $q_{1}\hat z_1$, dove $q_1=h^{(0)}\cdot\hat z_1$. Questo significa che a partire da qualunque valutazione dei valori di hub iniziali, se $c_1\gt c_2$, il mteodo HITS converge sempre ad un vettore parallelo all'autovettore $\hat z_1$, e quindi, la valutazione dei valori di hub delle pagine individuata da HITS è sempre la stessa, da qualunque valutazione dei valori di hub iniziali si parta, e dunque ***dipende solo dalla matrice $M$***

HITS valuta ciascuna pagina rispetto a due ruoli diversi: 
- come authority – la sua rilevanza ai fini della ricerca in atto
- come hub – la sua attitudine ad assegnare rilevanza alle pagine alle quali punta

E per ciascuna pagina, ciascuno dei due ruoli è valutato utilizzando un diverso insieme di link che coinvolgono quella pagina:
- i link entranti nella pagina concorrono alla valutazione come authority
- i link uscenti dalla pagina concorrono alla valutazione come hub

Questo significa che una pagina può conferire rilevanza, ai fini di una ricerca, ad un’altra pagina pur essendo essa poco rilevante per quella ricerca e, dunque, il metodo HITS ben si presta a modellare situazioni nelle quali le pagine sono naturalmente partizionate in due sottoinsiemi "semanticamente" distinti, come avviene, ad esempio, in ricerche di prodotti da acquistare
# PageRank

In altre situazioni, invece, assumere un tale partizionamento delle pagine non è ragionevole
- ad esempio, quando cerchiamo un articolo di ricerca: articoli “importanti” citano articoli “importanti” e sono citati da articoli “importanti”

Il **PageRank** ben modella queste situazioni

Si tratta ancora di un metodo iterativo, basato, però, sull’*analisi dei soli link entranti* in una pagina

Esso assume che nella porzione di rete, attinente alla ricerca in atto, sia presente una unità di fluido inizialmente distribuita equamente fra tutti i nodi[^4] e che poi, iterativamente, ciascun nodo distribuisca equamente il fluido fra i suoi vicini – alla fine, una pagina sarà ***tanto più rilevante quanto maggiore è la quantità di fluido in suo possesso***

Indichiamo quindi, $$\forall i=1,\dots,n,f_i^{(0)}= \frac{1}{n}$$
Ad ogni iterazione, ciascun nodo distribuisce equamente il fluido fra i suoi vicini - distribuisce quindi il fluido in suo possesso, e contestualmente, riceve quello dei vicini

Formalmente:
- per ogni $j=1,\dots,n$ indichiamo con $\omega_{j}$ il numero di archi uscenti dalla pagina $j$, ovvero $$\omega_{j}=|\{i\in[n]:j\to i\}|$$
- allora, $$\forall i=1,\dots,n,\space f_{i}^{(k+1)}=\sum\limits_{1\leq j\leq n:\space j\to i}\frac{f_{j}^{(k)}}{\omega_j}$$

Analogamente a quanto fatto con HITS, indichiamo con $f^{(k)}$ il vettore $\left(f_1^{(k)},f_2^{(k)},\dots,f_n^{(k)}\right)$ 

Vale quindi il seguente teorema:

>[!teorem]- Teorema
>Se il grafo delle pagine attinenti alla ricerca è fortemente connesso allora $$\exists!\lim_{k\to\infty}f^{(k)}$$

Osserviamo che, ad ogni iterazione $k$, la quantità di fluido totale presente nel grafo è sempre pari ad $1$
- al passo $k+1$, ciascun nodo redistribuisce il fluido in suo possesso al passo $k$
- senza generarne di nuovo

Allora, possiamo pensare al vettore limite degli $f^{(k)}$, chiamiamolo $f^\star$, come ad un vettore che esprime una sorta di **configurazione di equilibrio** del fluido, ovvero, redistribuendo il fluido a partire dal $f^\star$ il vettore non varia : $$\forall i=1,\dots,n,\space f_i^\star=\sum\limits_{1\leq j\leq n:\space j\to i}\frac{f^{\star}}{\omega_j}$$
In figura è modtraro il vettore limite di un grafo, a partire da $f^{(0)}=\frac{1}{8}$ per $i=A,B,C,D,E,F,G,H$

![center|350](img/Pasted%20image%2020250828152014.png)

Il teorema affermava l'unicità del limite nel caso in cui il grafo è fortemente connesso, ma se il grafo *NON* è fortemente connesso, le cose cambiano, vediamo un esempio

![center|650](img/Pasted%20image%2020250828152410.png)

Il flusso, da come si può vedere, tende ad accumularsi nei nodi gialli:
- inizialmente, i tre nodi $(C,F,G)$ possiedono $\frac{3}{8}\lt \frac{1}{2}$ del flusso totale
- nell'ultima iterazione mostrata ne possiedono $\frac{96}{128}=\frac{3}{4}$
## Scaled PageRank

Se il grafo non è fortemente connesso, il fluido tende a concentrarsi nelle regioni del grafo dalle quali non si può uscire, e da ciò che conosciamo riguardo la struttura del Web, di tali regioni il grafo ne contiene

Allora, è necessario modificare il procedimento iterativo che aggiorna il fluido associato ai nodi:
- ad esempio, non distribuendo tutto il fluido (d’ora in avanti, il ***rank***) contenuto in ciascun nodo equamente lungo gli archi uscenti da quel nodo
- ma "mettendone un po’ da parte" per evitare che esso si concentri nei "vicoli ciechi" del grafo

Nello **Scaled PageRank** viene fissato un parametro $s \in [0,1]$ e, ad ogni iterazione, una frazione pari a $s$ del rank contenuto in ciascun nodo è distribuito equamente lungo gli archi uscenti da quel nodo, e la parte rimanente, ossia, una frazione pari a $(1 – s)$ del rank contenuto in ciascun nodo, è distribuita uniformemente fra tutti i nodi del grafo e, poiché il rank totale presente nella rete è $1$, allora, ad ogni iterazione, ciascun nodo riceve una quantità di rank almeno pari a $\frac{1-s}{n}$

Detto quindi $r_i^{(k)}$ il *rank* posseduto dal nodo $i$ all'iterazione $k$, vale che $$r_i^{(k+1)}=\left(\sum\limits_{1\leq j\leq n: j\to i}s\frac{r_j^{(k)}}{\omega_j}\right)+\frac{1-s}{n}$$
La matrice $N$  che descrive l'evoluzione del rank è tale che, per $1\leq i,j\leq n$, 
$$N[i,j]=\begin{cases} \frac{s}{\omega_j}+\frac{1-s}{n}&j\to i\\\frac{1-s}{n}&\text{altrimenti}\end{cases}$$

Infatti, detto $r^{(k)}$ il vettore $\left(r_1^{(k)},r_2^{(k)},\dots,r_n^{(k)}\right)$, l'elemento $i$-esimo di $Nr^{(k)}$ è 
$$
\begin{align*}
\sum\limits_{1\leq n\leq n}N[i,j]r_j^{(k)}&=\sum\limits_{1\leq j\leq n:\space j\to i}\left[\frac{s}{\omega_j}+\frac{1-s}{n}\right]r_j^{(k)}+\sum\limits_{1\leq j\leq n:\space j\text{ non punta a } i}\frac{1-s}{n}r_j^{(k)}\\&=\sum\limits_{1\leq j\leq n:\space j\to i}\frac{s}{\omega_j}r_j^{(k)}+\sum\limits_{1\leq j\leq n}\frac{1-s}{n}r_j^{(k)}\\&=\sum\limits_{1\leq j\leq n:\space j\to i}\frac{s}{\omega_j}r_j^{(k)}+\frac{1-s}{n}\sum\limits_{1\leq j\leq n}r_j^{(k)}=\sum\limits_{1\leq j\leq n:\space j\to i}\frac{s}{\omega_j}r_j^{(k)}+\frac{1-s}{n}r_j^{(k)}
\end{align*}
$$
E quindi $$r^{(k+1)}=Nr^{(k)}$$
Analogamente al caso del PageRank non scalato, anche in quello scalato, ad ogni iterazione $k$, la quantità di rank totale presente nel grafo è sempre pari ad $1$:
- al passo k, ciascun nodo redistribuisce il fluido in suo possesso al passo $k$
- senza generarne di nuovo
- e questa caratteristica è stata usata nell’ultima uguaglianza nel calcolo precedente

Allora, possiamo pensare al vettore limite degli $r^{(0)}$, chiamiamolo $r^\star$, come ad un vettore che esprime una sorta di **configurazione di equilibrio** del rank, ovvero, redistribuendo il rank a partire da $r^\star$ il vettore non varia: $$r^\star = Nr^\star$$

Il vettore limite dovrebbe essere un ***autovettore della matrice*** $N$ con determinate caratteristiche, ovvero
- il corrispondente autovalore deve essere $1$
- gli elementi devono essere non negativi
- la somma degli elementi deve essere pari a $1$
- e deve essere anche l’unico autovettore con queste proprietà

Ma chi ci dice che $N$ ha una coppia autovettore-autovalore con tutte queste proprietà?

Semplice, il **teorema di Perron**

>[!teorem]- Teorema di Perron (versione semplificata)
>Se $A$ è una matrice reale $n\times n$ a elementi positivi, allora:
>1) $A$ ha un autovalore $c\in\mathbb R^{+}$ tale che, $c\gt|c'|$ per ogni altro autovalore $c'$ di $A$
>2) l'autovettore $\hat x$ di $A$ corrispondente a $c$ è unico ed è a elementi reali e positivi la cui somma è $1$

La matrice $N$ da noi descritta soddisfa le ipotesi del teorema di Perron, e quindi ha un coppia autovalore-autovettore con *quasi* tutte le proprietà da noi cercate

In effetti, la matrice $N$ ha tutte le proprietà tranne una: se potessimo esser certi che $c=1$ potremmo concludere che $r^\star=Nr^\star$

Aiutiamoci con un'altro teorema, che segue però la definizio di **matrice stocastica**

>[!definition]- Matrice Stocastica
>Una matrice quadrata si dice **stocastica** se i suoi elementi sono non negativi e:
>1) la somma degli elementi su ciascuna riga è $1$ (stocastica per righe)
>2) oppure la somma degli elementi su ciascuna colonna è $1$ (stocastica per colonne)
>
>Se valgono sia $1)$ che $2)$ si dice che la matrice è **doppiamente stocastica**

Vediamo ora il teorema:

>[!teorem]- Teorema sulle matrici stocastiche
>Se $A$ è una matrice stocastica allora $A$ ha un autovalore $\lambda$ tale che $|\lambda|=1$ e $\lambda$ è ***l'autovalore di modulo massimo*** di $A$

La nostra matrice $N$ è stocastica per colonne: dato che $\sum\limits_{1\leq i\leq n:\space j\to i} \frac{1}{\omega_j}=1$ allora vale che $$\sum\limits_{1\leq i\leq n}N[i,j]=\sum\limits_{1\leq i\leq n:\space j\to i}\left[\frac{s}{\omega_j}+\frac{1-s}{n}\right]+\sum\limits_{1\leq i\leq n:\space j\text{ non punta a } i}\frac{1-s}{n}=\sum\limits_{1\leq i\leq n:\space j\to i}\frac{s}{\omega_j}+\sum\limits_{1\leq i\leq n}\frac{1-s}{n}=1$$
Allora:
- per il teorema di Perron $N$ ha un autovalore $c\in\mathbb R^{+}$ tale che, $c\gt|c'|$ per ogni altro autovalore $c'$ di $N$ e un unico autovettore $\hat x$ corrispondente a $c$ a elementi reali e positivi la cui somma è $1$
- per il teorema sulle matrici stocastiche $c=1$

Quindi, possiamo affermare che: 
$$N\hat x=\hat x\space\land\space r^{\star}=\hat x$$
## PageRank e Random Walks

Abbiamo introdotto il PageRank descrivendolo come una sorta di fluido che circola nella rete
- che viene iterativamente redistribuito fra i nodi, senza che ne venga alterata la quantità

Il PageRank ha anche un’altra interpretazione, legata al concetto di ***random walk in un grafo*** (diretto $G=(V,A)$)
- inizialmente scegliamo **u.a.r** un nodo $u$ del grafo
- da $u$, scegliamo **u.a.r** un arco uscente da quel nodo, che ci condurrà ad un altro nodo dal quale sceglieremo **u.a.r** un arco uscente, e continuando in tal modo, percorreremo un *percorso aleatorio* nel grafo

Per individuare la relazione fra PageRank e random walk, calcoliamo la probabilità di trovarsi in un qualsiasi nodo del grafo dopo un random walk di $k$ passi

Per ogni $i\in V$, indichiamo con $W_i^{k}$ la variabile aleatoria il cui valore è :
$$W_i^{k}=\begin{cases}1&\text{se al passo k ci troviamo nel nodo i}\\0&\text{altrimenti}\end{cases}$$

Allora, per ogni $i\in V$ vale che: $$Pr(W_i^{0}=1)= \frac{1}{n}= f_i^{(0)}$$
E, per ogni $i\in V$, detto $\omega_{j}$ il numero di archi uscenti dal nodo $j$, vale che:
$$Pr(W_i^{1}=1)=\sum\limits_{j\in V:(j,i)\in A} \frac{1}{\omega_j}Pr(W_j^{0}=1)=\sum\limits_{j\in V:(j,i)\in A}\frac{f_j^{(0)}}{\omega_j}=f_i^{(1)}$$
Induttivamente, per ogni $k\gt0$ e per ogni $i\in V$

$$Pr(W_i^{k}=1)=\sum\limits_{j\in V:(j,i)\in A} \frac{1}{\omega_j}Pr(W_j^{k-1}=1)=\sum\limits_{j\in V:(j,i)\in A}\frac{f_j^{(k-1)}}{\omega_j}=f_i^{(k)}$$
### Scaled PageRank e Random Walks

Cosideriamo ora un random walk scalato in un grafo diretto $G = (V,A)$ eseguito in accordo alle seguenti regole: sia $s \in [0,1]$
- inizialmente scegliamo uniformemente a caso un nodo $u$ del grafo e, da $u$
	- con probabilità $s$ scegliamo u.a.r un arco uscente da quel nodo
	- e con probabilità $(1 – s)$ scegliamo u.a.r un altro nodo del grafo

Per ogni $i \in V$, indichiamo con $SW_{i}^{k}$ la variabile aleatoria il cui valore è
$$SW_i^{k}=\begin{cases}1&\text{se al passo k del nuovo RW scalato ci troviamo nel nodo i}\\0&\text{altrimenti}\end{cases}$$

Allora, per ogni $i \in V$ vale che:
$$Pr(SW_i^{0}=1)= \frac{1}{n}= r_i^{(0)}$$
E, per ogni $k\gt0$ e $i\in V$, è semplice verificare che
$$Pr(SW_i^{k}=1)=\sum\limits_{j\in V:(j,i)\in A} \frac{s}{\omega_j}Pr(SW_j^{k-1}=1)+\frac{1-s}{n}=r_i^{(k)}$$


[^1]: nota a margine, la dimostrazione viene fatta per $h^{(k)}$, e per $a^{(k)}$ è del tutto analoga

[^2]: perchè $c_i\in\mathbb R^{+}\cup\{0\}\forall\space i=1,\dots,n$ e $\forall i=l+1,\dots,n\space\left[0\leq\frac{c_i}{c_1}\lt 1\right]$

[^3]: esempio: $\hat y^{(2)}=(\hat y_{1},\hat y_2+1,\dots,\hat y_n)$ 

[^4]: se il numero di nodi è $n$, ciascuno di essi possiede inizialmente $\frac{1}{n}$ di fluido
