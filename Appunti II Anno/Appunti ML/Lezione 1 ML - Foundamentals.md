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
# Foundamentals

Le fondamenta del ***Machine Learning*** (**apprendimento automatico**) risiedono nel nostro accesso a una raccolta di punti dati, ciascuno dei quali rappresenta l'osservazione dei valori di un insieme di variabili predefinite, generate da un processo sconosciuto. 

Il punto cruciale di questo quadro è la premessa che questi dati, lungi dall'essere casuali, possiedono una **struttura intrinseca**, anche se **spesso difficile da identificare**.

L'essenza dell'apprendimento automatico risiede in due obiettivi primari, ciascuno dei quali affronta un aspetto diverso dell'analisi dei dati:

1) **Unsupervised Learning** : In questo caso, il nostro obiettivo è quello di estrarre approfondimenti significativi sulla struttura sottostante dei dati, approfondendo così la nostra comprensione della loro natura intrinseca. Questo approccio spesso comporta tecniche quali il ***clustering***, la ***riduzione della dimensionalità*** o la ***modellazione generativa***. Un'applicazione particolarmente interessante dell' apprendimento non supervisionato è la capacità di generare algoritmicamente nuovi punti di dati che sono, in larga misura, indistinguibili dal set di dati originale. Questi punti di dati sintetici sembrano essere prodotti dallo stesso processo sconosciuto, imitando efficacemente le caratteristiche intrinseche e le distribuzioni dei dati.
2) **Supervised Learning**: In questo paradigma, miriamo a prevedere informazioni aggiuntive per ogni elemento di dati sulla base delle conoscenze esistenti. Ciò comporta tipicamente l'addestramento di modelli su dati etichettati per fare previsioni su istanze non viste. L'apprendimento supervisionato comprende una vasta gamma di compiti, tra cui la ***classificazione***, la ***regressione*** e la ***previsione di sequenze***.

In entrambi questi scenari, partiamo da una serie di osservazioni già prodotte dal processo sconosciuto. 
Questo set di dati iniziale funge da base su cui costruiamo i nostri modelli e ricaviamo le nostre intuizioni.

Un quadro alternativo, distinto dai paradigmi supervisionati e non supervisionati, è l'**apprendimento per rinforzo**. (***Reinforcement Learning***)
In questo approccio, ipotizziamo una relazione interattiva con il processo sottostante.

Anziché lavorare con un set di dati statico, ci impegniamo in una procedura dinamica e iterativa:

1. Ad ogni passo, interagiamo con il processo scegliendo ed eseguendo un'azione da una serie di opzioni
	1. di conseguenza, otteniamo una risposta sotto forma di ricompensa
2. l'obiettivo generale è quello di identificare una strategia ottimale per interagire con il processo sconosciuto, che massimizzi la ricompensa cumulativa.

Questo quadro trova applicazione in settori quali i giochi, la robotica e i sistemi autonomi, dove la capacità di apprendere e adattarsi attraverso tentativi ed errori è fondamentale.

Mettendo da parte il paradigma dell'apprendimento per rinforzo, approfondiamo lo scenario comune che si presenta nell'apprendimento supervisionato e non supervisionato:

- Un **set di addestramento** (***Training Set***) di $n$ elementi è rappresentato come un insieme di vettori di input $x_1,\dots, x_n$. Questi vettori racchiudono le caratteristiche o gli attributi di ciascun punto dati (***features***) e fungono da materia prima da cui deriviamo il nostro **modello**. La dimensionalità e la natura di questi vettori possono variare notevolmente a seconda del dominio specifico del problema, spaziando da dati numerici a bassa dimensionalità a rappresentazioni ad alta dimensionalità di immagini, testo o strutture complesse
- Nel caso dell'apprendimento supervisionato, il set di addestramento viene arricchito con informazioni aggiuntive. Nello specifico, include un vettore ***target*** $t = \{t_1,\dots , t_n\}$, dove ogni $t_i$ specifica il ***valore da prevedere*** sulla base del corrispondente vettore di input $x_{}i$. Questo accoppiamento di input e target costituisce la base per l'addestramento di modelli predittivi in grado di generalizzare dati non visti.

Si osservi che i vettori nel set di addestramento sono in generale una ***rappresentazione specifica di elementi*** (che sono entità del mondo reale), proprio come le tuple in un database sono solo modelli (secondo un modello di dati predefinito) di entità. 

L'insieme di features utilizzato nel processo di apprendimento è una componente fondamentale in tale processo e può avere un effetto importante sulla qualità e l'efficienza delle previsioni. 

La regolazione dell'insieme di features (sia definendo nuove caratteristiche da composizioni funzionali adeguate di quelle date, sia identificando caratteristiche significative per il compito da svolgere) è ***una questione fondamentale nel Machine Learning***, che può coinvolgere sia competenze specifiche del settore sia sofisticati approcci algoritmici, applicati nei quadri di riferimento dell'apprendimento non supervisionato.

Vediamo ora i due tipi di apprendimento fondamentali
## Supervised Learning

Il nostro obiettivo è ***prevedere*** il valore sconosciuto di una feature aggiuntiva, denominata *target*, per un dato elemento $x$, sulla base dei valori di una serie di caratteristiche. 

Questo compito di previsione assume due forme principali:
1) **Regressione**: quando il target è un reale $t\in\mathbb R$
2) **Classificazione** : quando il target è un valore discreto, determinato da un insieme predefinito $t\in\{1,\dots,K\}$

Per ottenere questo risultato, utilizziamo un approccio generale che prevede la definizione di un modello (*funzionale o probabilistico*) della relazione tra i valori delle features e quelli target. 

Questo modello è derivato attraverso un processo di apprendimento da una serie di esempi che illustrano la relazione tra l'insieme delle features e il target. 

Gli esempi sono raccolti in un training set $\mathcal T = (X, t)$ e ciascuno di essi comprende:
- Un vettore di caratteristiche $x_i = \{x_{i_1},\dots , x_{i_m}\}$
- Il valore target corrispondente $t_i$

Il modello che costruiamo può assumere due forme:

1) Una **funzione** $y(\cdot)$ che, per qualsiasi elemento $x$, restituisce un valore $y(x)$ come stima di $t$. Questa funzione agisce come un ***predittore diretto***, mappando le caratteristiche di input allo spazio target.
2. Una **distribuzione di probabilità** che associa ogni possibile valore $\overline{y}$ nel dominio target alla sua corrispondente probabilità $p(y = \overline{y}|x)$. Questo approccio probabilistico fornisce una visione più sfumata, catturando l'incertezza inerente al compito di previsione.

La scelta tra questi tipi di modelli dipende spesso dai requisiti specifici del problema in questione, dalla natura dei dati e dall'interpretabilità desiderata dei risultati. 

L'approccio function-based offre previsioni dirette, mentre il modello probabilistico fornisce una rappresentazione più ricca delle incertezze sottostanti e dei potenziali risultati.

In entrambi i casi, il modello funge da ponte tra le features osservate e il target che intendiamo prevedere, sfruttando i modelli e le relazioni appresi dai dati di addestramento per fare previsioni informate su nuovi casi non ancora osservati.
## Unsupervised Learning

L'obiettivo è quello di rilevare modelli e strutture intrinseche all'interno di una determinata raccolta di elementi, nota come **dataset** $X = \{x_1, \dots , x_n\}$, dove nessun valore target è associato agli elementi, al fine di estrarre informazioni sintetiche da tali dati. 

Le informazioni sintetiche che cerchiamo di estrarre possono assumere diverse forme:
1) **Clustering**
2) **Dimensionality Reduction**
