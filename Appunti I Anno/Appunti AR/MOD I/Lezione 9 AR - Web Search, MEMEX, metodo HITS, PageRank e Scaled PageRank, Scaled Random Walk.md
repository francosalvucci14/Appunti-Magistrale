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

![[Pasted image 20250827151834.png|center|350]]

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
Analogamente, il valore di hub di una pagina $i$, indicato con $h_{i}$, potrebbe essere il numero di pagine nell'insieme delle pagine attinenti alla ricerca alle quali esse punta, ovvero in termini matematici $$h_i=|\{j:j\text{ è attinente alla ricerca}\land i\to j\}|,\quad j\to i=\text{pagina i punta alla pagina j}$$
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

In questo caso, possiamo assumenre che tali valori siano uguali per tutte le pagine, e quindi $$h_{j}^{(0)}=1\space\forall 1\leq i\leq n$$
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
&\forall i=1,\dots,n:\hat z_{i}\cdot\hat z_{i}=\hat z_{i1}^2+\hat z_{i2}^2+\dots+\hat z_{in}^2=1\quad\text{(normalità)}\\&\forall i\neq l:\hat z_{i}\cdot\hat z_{l}=\hat z_{i1}\hat z_{l1}+\hat z_{i2}\hat z_{l2}+\dots+\hat z_{in}\hat z_{ln}=0\quad\text{(ortogonalità)}
\end{align*}$$

Una matrice $A$ simmetrica e reale si dice **semidefinita positiva*** se $$\forall\hat x\in\mathbb R^{n}:\hat x^{T}A\hat x\geq0$$

>[!teorem]- Teorema 2
>Se $A$ è una matrice semidefinita positiva allora:
>1) gli autovalori di $A$ sono non negativi
>2) se $A$ è non nulla allora almeno un autovalore di $A$ è strettamente positivo


Bene, torniamo ora al [[Lezione 9 AR - Web Search, MEMEX, metodo HITS, PageRank e Scaled PageRank, Scaled Random Walk#^1acb62|Teorema Principale]], vedremo a breve il ruolo dei due teoremi appena descritti nella dimostrazione del teorema principale

Intanto, osserviamo che $(MM^{T})$ è una matrice reale e simmetrica, infatti $$(MM^{T})_{ij}=\sum\limits_{1\leq k\leq n}M_{ik}M_{kj}=(MM^{T})$$
Allora, $(MM^{T})$ ha una **base ortonormale di autovettori per $\mathbb R^{n}$ e tutti gli autovalori reali**

$(MM^{T})$ è anche semidefinita positiva, infatti comunque scelgo $\hat x\in\mathbb R^{n}$ si ha $$\hat x^{T}(MM^{T})\hat x=(\hat x^{T}M)(M^{T}\hat x)$$ e dunque, ponendo $(M^{T}\hat x)=y=(y_1,y_2,\dots,y_n)$ si ottiene $$\hat x^{T}(MM^{T})\hat x=y^{T}y=\sum\limits_{1\leq k\leq n}y_{k}^{2}\geq0$$
Allora, poichè $(MM^{T})$ è non nulla, il suo **autovalore massimo è strettamente positivo**

Cominciamo ora, finalmente, con la dimostrazione del Teorema Principale [^1]

**dimostrazione**
# PageRank

## Scaled PageRank

## PageRank e Random Walks

### Scaled PageRank e Random Walks


[^1]: nota a margine, la dimostrazione viene fatta per $h^{(k)}$, e per $a^{(k)}$ è del tutto analoga
