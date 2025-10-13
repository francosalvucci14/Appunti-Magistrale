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
1) **Clustering**: Identificazione di sottoinsiemi di elementi simili all'interno del set di dati. Questo processo comporta il raggruppamento dei punti dati in base alle loro somiglianze intrinseche, rivelando strutture o segmenti naturali nei dati.
2) **Density Estimation**: Determinazione della distribuzione degli elementi nel loro dominio. Questo approccio mira a modellare la funzione di densità di probabilità sottostante che ha generato i dati osservati, fornendo informazioni sulle proprietà statistiche dei dati e sui potenziali processi generativi.
3) **Dimensionality Reduction**: Proiezione di elementi su sottospazi di dimensione inferiore preservando il maggior numero possibile di informazioni. Ciò può essere ottenuto attraverso due approcci principali: 
	1) *Selezione delle caratteristiche* (***Feature Selection***): identificazione e conservazione del sottoinsieme più informativo delle caratteristiche originali.
	2) *Estrazione delle caratteristiche* (***Feature Extraction***): creazione di nuove rappresentazioni dei dati a dimensione inferiore che ne catturano le caratteristiche essenziali.
	3) Queste tecniche di riduzione della dimensionalità mirano a caratterizzare gli elementi utilizzando un insieme più piccolo di caratteristiche, rivelando potenzialmente strutture latenti e riducendo la complessità computazionale per le analisi successive.

Anche nel contesto dell'apprendimento non supervisionato, dove mancano variabili target esplicite, è prassi comune definire e applicare un modello adeguato che catturi le relazioni e i modelli tra le caratteristiche dei dati. 

Questo modello ha diversi scopi:
1. Fornisce una rappresentazione compatta della struttura sottostante dei dati.
2. Può essere utilizzato per generare nuovi punti dati sintetici che condividono le caratteristiche del set di dati originale.
3. Consente il rilevamento delle anomalie identificando i punti dati che si discostano in modo significativo dai modelli appresi.
4. Facilita l'interpretazione e la visualizzazione dei dati ad alta dimensionalità.

La scelta del modello dipende dallo specifico compito di apprendimento non supervisionato e dalla natura dei dati.

Ad esempio:

- **Per il clustering**, potremmo utilizzare modelli come **$k$-means**, **Gaussian Mixture Models** (modelli di miscela gaussiana) o **algoritmi di clustering gerarchico**.
- **Per la stima della densità**, potrebbero essere impiegati la **stima della densità del kernel** o modelli parametrici come le **distribuzioni Gaussiane**.
- **Per la riduzione della dimensionalità**, potrebbero essere utilizzate tecniche come **l'analisi delle componenti principali** (***PCA***), **$t$-SNE** o **autoencoder**.

Applicando queste tecniche e modelli di apprendimento non supervisionato, possiamo ottenere informazioni preziose sulla struttura intrinseca dei nostri dati, anche in assenza di variabili target predefinite. 

Questo approccio è particolarmente utile per definire ***modelli generativi*** (come LLM e tutti i sistemi di IA generativa), analisi esplorativa dei dati, feature engineering e come fase di pre-elaborazione per successive attività di apprendimento supervisionato.
# Definizione formale di un task di Machine Learning

Un task di Machine Learning è definita su una coppia di domini:

- **Domain Set** $\mathcal X$: Si tratta dell'insieme di oggetti che desideriamo etichettare o su cui desideriamo fare previsioni. Ogni oggetto $\overline{x}\in\mathcal X$ è solitamente **modellato come un array di feature** [^1] . Il numero di caratteristiche è indicato come **dimensionalità** del problema. Formalmente, possiamo quindi rappresentare un oggetto come $\overline{x} = [x_1, x_2, \dots, x_d]$, dove $d$ è la dimensionalità.
- **Label Set** $\mathcal Y$: Si tratta dell'insieme dei possibili valori delle etichette associate agli oggetti in $\mathcal X$ . La natura di $\mathcal Y$ determina il tipo di attività di apprendimento:
	- Se $\mathcal Y$ è ***continuo***, siamo di fronte a un task di **regressione**
	- Se $\mathcal Y$ è ***discreto***, siamo di fronte a un task di **classificazione**:
		- quando $|\mathcal Y|=2$, abbiamo il caso di **classificazione binaria**
		- quando $|\mathcal Y|\gt2$, abbiamo il caso di **classificazione multi-class**

Il **learner** (un **algoritmo** $\mathcal A$) ha accesso a un *set di addestramento* (***Training Set***) $\mathcal T$, ovvero una collezione di coppie elementi-etichette fatto in questo modo: $$\mathcal T = \{(\overline{x}_1, t_1), \dots , (\overline{x}_n, t_n)\}$$
Di solito indicheremo con $X$ la matrice degli elementi (***matrice delle feature***), ovvero
$$X=\begin{bmatrix}
-\overline{x}_{1}-\\\vdots\\-\overline{x}_{n}-
\end{bmatrix}$$
e come $\overline{t}$ il vettore delle etichette (***vettore target***), ovvero
$$\overline{t}=\begin{bmatrix}
t_{1}\\\vdots\\t_{n}
\end{bmatrix}$$

Al learner viene richiesto di restituire, per un dato training set $\mathcal T$, una **regola di previsione** (***classificatore, regressore***) $$\mathcal A = \mathcal A(\mathcal T) = h : \mathcal X \to \mathcal Y$$
Il predittore dovrebbe essere in grado di generare una previsione $y$ per qualsiasi elemento $x\in \mathcal X$ : ciò può essere fatto secondo diversi approcci.

1) *Previsione diretta del valore target*: in questo caso, l'algoritmo $\mathcal A$ prevede un valore $y$ che è una supposizione del target di $\overline{x}$. Cioè, calcola direttamente una funzione $$h :\mathcal X\to \mathcal Y$$
2) *Previsione della distribuzione di probabilità*: in questo caso, l'algoritmo $\mathcal A$ distribuisce la probabilità su $\mathcal Y$ che, per qualsiasi $y\in\mathcal Y,\mathcal A$ restituisce una probabilità stimata $p(y|\overline{x})$ che $y$ sia il valore target di $\overline{x}$. Al fine di restituire un valore unico $y$, questo approccio deve essere accompagnato da una regola indipendente per derivare, dato $p(y|\overline{x})$, il valore da prevedere.
## Derivare un Predittore Funzionale

Ci sono molteplici modi per derivare un **predittore funzionale**

### Direct Prediction Computation

In questo caso, per ogni previsione viene applicato un algoritmo predefinito $\mathcal A$: l'algoritmo calcola una funzione $$h : \mathcal X \times (\mathcal X \times \mathcal Y)^{n}\to\mathcal Y$$In particolare, calcola la previsione $y$ per un elemento $\overline{x}$ calcolando $h(\overline{x},\mathcal X, \overline{t})$: ovvero, tiene conto dell'intero training set per ogni previsione.

Si osservi che non viene effettuato alcun apprendimento (ovvero, derivare alcune regole di previsione dagli esempi da applicare alle previsioni)

Lo schema generale di questo approccio è il seguente:

![[Pasted image 20251012190730.png|center|300]]

Esempio di questo approccio: algoritmo dei $k$ vicini più prossimi ($\text{kNN}$) per la classificazione.

La classe prevista per l'elemento $\overline{x}$ è la classe maggioritaria nell'insieme dei $k$ elementi di $\mathcal X$ che sono più vicini a $\overline{x}$ secondo una misura predefinita.
### Model-Based Learning Approach

Il secondo approccio per ricavare un predittore consiste nell'apprendere una funzione da una classe predefinita di modelli.

Questo metodo, spesso denominato approccio basato sul modello (***Model-Based Learning Approach, MBLA***), può essere formalizzato come segue:

1) Definiamo una classe di funzioni $\mathcal H : \mathcal X\to\mathcal Y$
2) Impieghiamo un algoritmo di apprendimento $\mathcal A$ che derivi una funzione specifica $h_{T}\in\mathcal H$ dal training set $\mathcal T$ . Cioè, $\mathcal A$ implementa una funzione da $\mathcal T$ a $\mathcal H$

L'idea, in questo caso, è che $\mathcal A$ trovi la funzione in $\mathcal H$ (ovvero un algoritmo $\mathcal A_{\mathcal T}$ che implementa questa funzione) che "meglio" [^2] preveda $y$ da $\overline{x}$ quando applicata agli esempi in $\mathcal T$, ovvero che preveda al meglio $t_{i}$ da $x_i$ per tutte le coppie $(x_i, t_i)\in\mathcal T$

Per ogni nuovo elemento $\overline{x}$, il valore target corrispondente viene calcolato come $h_{\mathcal T} (\overline{x})$, ovvero applicando $A_{\mathcal T}$ all'input $\overline{x}$.

Come vedremo, un caso rilevante qui è quando $\mathcal H$ è un insieme di funzioni parametriche (indicato come $\mathcal H_\overline{\theta}$, dove $\overline{\theta} = (\theta_1,\dots , \theta_m)$ è l'insieme dei parametri) con la stessa struttura e che differiscono tra loro per i valori dei parametri in $\overline{\theta}$.

In questo caso, cercare una funzione in $\mathcal H_\overline{\theta}$ equivale a cercare un valore per $(\theta_1,\dots , \theta_m)$.

![[Pasted image 20251013095103.png|center|500]]

Un semplice esempio di questo approccio è la **regressione lineare**, in cui il valore previsto per l'elemento $\overline{x}$ viene calcolato come ***combinazione lineare*** dei valori delle sue features $x_1, x_2, \dots , x_d$ ciascuno ponderato da un parametro costante adeguato $w_1, w_2,\dots , w_d$, più un ***bias*** $w_{0}$.
In altre parole, la previsione viene calcolata come: $$y=\sum\limits_{i=1}^{d}w_ix_i+w_{0}=\overline{w}^{T}\hat{x}$$
Dove:
- $\overline{w}$ è il vettore [^3] $$\begin{bmatrix}
w_0\\w_1\\\vdots\\w_{d}
\end{bmatrix}$$
- $\hat{x}$ è il vettore $$\begin{bmatrix}
1\\w_1\\\vdots\\x_{d}
\end{bmatrix}$$


[^1]: In realtà, nei casi avanzati gli oggetti potrebbero avere strutture più complesse, come ad esempio sequenze o grafi

[^2]: Si noti che è necessario specificare cosa si intende per “migliore” in questo contesto, ovvero quale misura di qualità della previsione applicare.

[^3]: In generale, tutti i vettori introdotti di seguito saranno considerati vettori colonna.
