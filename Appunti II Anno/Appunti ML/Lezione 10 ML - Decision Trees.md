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
# Decision Tree

Un **albero di decisione** è un classificatore espresso come partizione ricorsiva dello spazio istanziato.

La sua struttura è la seguente:
- Consiste in nodi che formano un'albero radicato
- Ogni nodo interno divide lo spazio instanziato in due o più sottospazi, seguendo una data funzione discreta dei valori degli attributi
- Di solito, ogni nodo è associato ad una partizione rispetto a un singolo attributo
- Ogni foglia è associata ad un sottospazio e:
	- a una classe, che rappresenta la previsione più appropriata per tutti i punti nel sottospazio
	- oppure a un vettore di probabilità delle classi

**esempio**

![center|500](img/Pasted%20image%2020251210173914.png)

![center|500](img/Pasted%20image%2020251219102305.png)

![center|500](img/Pasted%20image%2020251219102343.png)

![center|500](img/Pasted%20image%2020251219102412.png)

## Decision Tree: Classification

Dato un elemento $\mathbf{z} = (z_1,\dots , z_d)^{T}$ , l'albero decisionale viene attraversato a partire dalla sua radice.

Ad ogni nodo attraversato, con feature $x_i$ e funzione $f_i$ associate, viene calcolato il valore $f_i(z_i)$ per decidere quale sia il nodo successivo da considerare, tra l'insieme dei nodi figli.

Ciò equivale a considerare sottoregioni sempre più piccole dello spazio dei dati.

Un caso importante è quando viene definita una soglia $\theta_i$ e viene eseguito un confronto tra $z_i$ e $\theta_i$ per decidere quale sia il nodo successivo da considerare, tra due nodi figli.

La procedura si interrompe quando viene raggiunto un nodo foglia. 
La previsione restituita è data dalla classe corrispondente, o derivata dal vettore delle probabilità di classe
## Decision Tree: Construction

Lo spazio dei dati viene suddiviso in modo ricorsivo costruendo l'albero decisionale dalla radice alle foglie.

Ad ogni nodo:

1. Come eseguire una suddivisione della regione corrispondente (scegliendo caratteristica e funzione)?
2. Quando interrompere la suddivisione? Come assegnare le informazioni alle foglie?
## Decision Tree: Partitioning at each node

Selezionare la caratteristica e la funzione/soglia in modo tale che una data misura sia massimizzata all'interno delle intersezioni del training set con ciascuna sottoregione. 

**Misure di impurità** di classe all'interno di un set. Da minimizzare
### Impurity measure

Data una variabile aleatoria con dominio discreto $\{a_1, \dots , a_k\}$ e probabilità corrispondenti $p = (p_1,\dots , p_k)$, una **misura di impurità** $\phi : p\to\mathbb R$ ha le seguenti proprietà:

- $\phi(p) \geq 0$ per tutti i possibili $p$
- $\phi(p)$ è minimo se esiste $i, 1 \leq i \leq k$ tale che $p_i = 1$
- $\phi(p)$ è massima se $p_i = \frac{1}{k}$ per tutti gli $i$
- $\phi(p)=\phi(p^{'})$ per tutti i $p^{'}$ derivanti da una permutazione di $p$
- $\phi(p)$ è differenziabile ovunque
### Goodness of split

Nel nostro caso, consideriamo la classe di ogni elemento in $S$
- Per ogni insieme $S$ di elementi, il vettore di probabilità associato ad $S$ può essere definito come $p=\left(\frac{|S_{1}|}{|S|},\dots,\frac{|S_{k}|}{|S|}\right)$ dove $S_{h}\subseteq S$ è l'insieme di elementi di $S$ appartenenti alla classe $h$
- Data una funzione $f:S\to\{1,\dots,r\}$, sia $s_{i}=\{x\in S|f(x)=i\}$. La **bontà dello split** (goodness of split) di $S$ rispetto a $f$ è data da $$\Delta_{\phi}(S,f)=\phi(p_{S})-\sum\limits_{i=1}^{r}p_{i}\phi(p_{s_{i}})$$ ovvero dalla differenza tra l'impurità di $S$ e la media delle impurità dei sottoinsiemi risultanti dall' applicazione di $f$

In pratica, $f$ è solitamente definita considerando una singola feature e:
- se la feature è discreta, inducendo una partizione del suo codominio in $k$ sottoinsiemi 
	- come caso speciale, la partizione è tra elementi con lo stesso valore per la feature considerata
- se è continua, inducendo una partizione del suo codominio in un insieme di intervalli, definiti da soglie
	- come caso speciale, viene data una singola soglia e $f$ esegue una partizione binaria sugli elementi in $S$
#### Entropy and infomation gain

Per ogni insieme $S$ di elementi, sia $$H_{S}=-\sum\limits_{i=1}^{k}\frac{|S_{i}|}{|S|}\log_2\frac{|S_{i}|}{|S|}$$
l'**entropia** di $S$.

Osserviamo che l'entropia è *minimale* (uguale a 0) se tutti gli elementi di $S$ appartengono alla stessa classe, e *massimale* (uguale a $\log_{2}k$) se tutte le classi sono rappresentate in $S$ dallo stesso numero di elementi

Usando l'entropia come misura di impurità, la bontà dello split viene dato dall' **information gain**, definito come segue

L'information gain rispetto a una funzione di partizione $f$ è la diminuzione dell'entropia da $S$ alla media delle entropie di $s_i$, ovvero:
$$IG(S,f)=H_{S}-\sum\limits_{j=1}^{k}\frac{|s_{j}|}{|S|}H_{s_{j}}$$
#### Gini index

L'**indice di Gini** viene usato in molti casi come strumento per misurare la **divergenza dall'uguaglianza**.
Viene definito come:
$$G_{S}=1-\sum\limits_{i=1}^{k}\left(\frac{|S_{i}|}{|S|}\right)^{2}$$
Il **guadagno di Gini** (Gini gain) rispetto a una funzione di partizione $f$ è la diminuzione dell'indice di Gini da $S$ alla somma ponderata degli indici di Gini di $s_i$
$$GG(S,f)=G_{S}-\sum\limits_{j=1}^{r}\frac{|s_{j}|}{|S|}G_{s_{j}}$$
### Other goodness of split measures

Un'altra misura della bontà dello split è la cosìdetta **DKM**

DKM è una misura definita per la classificazione binaria, ed è definita nel modo seguente:
$$DKM_{S}=2\sqrt{\left(\frac{|S_{1}|}{|S|}\right)\left(\frac{|S_{2}|}{|S|}\right)}$$
ed il guagagno (gain) corrispondente risulta essere
$$DKMG(S,f)=DKM_{S}-\sum\limits_{j=1}^{r}\frac{|s_{j}|}{|S|}DKM_{s_{j}}$$

Un'altra misura è il **Gain Ratio** 

È una versione del guadagno di informazione normalizzata rispetto all'entropia originale, definito nel seguente modo
$$GR_{S}=\frac{IG(S,f)}{H_{S}}$$
Ovviamente possono essere definite altre misure
## Decision Tree: Leaves

Spesso, le condizioni per decidere quando interrompere la partizione sono predefinite (profondità massima dell'albero, numero massimo di foglie, numero di elementi in una sottoregione).

Quando si raggiunge una foglia, la classe corrispondente può essere definita come la classe maggioritaria nell'intersezione tra la sottoregione e il training set
### Pruning

L'interruzione anticipata tende a creare alberi decisionali piccoli e sottodimensionati.

L'interruzione approssimativa tende a generare alberi grandi e sovradimensionati.

Per risolvere il problema è possibile applicare metodi di "potatura" (**pruning**).

1. Viene utilizzato un criterio di arresto approssimativo, lasciando che l'albero decisionale risulti sovradimensionato.
2. L'albero sovradimensionato viene ridotto a un albero più piccolo rimuovendo opportunamente i rami che sembrano non contribuire all'accuratezza della generalizzazione. Diversi sottoalberi vengono uniti in singoli nodi, riducendo così le dimensioni dell'albero.

