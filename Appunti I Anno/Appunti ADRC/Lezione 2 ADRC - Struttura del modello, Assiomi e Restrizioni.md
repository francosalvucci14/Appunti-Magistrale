# Struttura del modello

Per le definizioni formali ritornare con gli appunti di Clementi

Definiamo cos'è un Sistema Distribuito

> [!definition]- Sistema Distribuito
> Un SD è un **insieme di entità** (dette anche **nodi**,**agenti**,etc..) che eseguono computazioni locali e possono comunicare fra loro, mediante link di comunicazione.
> Ogni nodo nel SD ha un **clock locale**, che scandisce il tempo per le computazioni locali del nodo.
> I vari clock locali dei nodi non per forza sono sincronizzati fra loro

Il SD si rappresenta con una struttura a grafo $G$, dove : 
- $V$ è l'insieme dei nodi/entità
- $E$ è l'insieme dei link di comunicazione (archi)

La comunicazione fra le entità è dettata dallo scambio di messaggi, vedremo più avanti come sono fatti

## Operazioni e stato del nodo

Le operazioni che un singolo nodo può effettuare sono molteplici, tra cui : 
- Elaborare e salvare informazioni in locale (computazioni locali)
- Trasmettere messaggi ad altre entità (comunicazione)
- (Re)impostare il proprio clock
- etc..

Ogni nodo ha uno **stato**, che ci va ad indicare lo stato attuale del nodo, ad es. "sleeping","idle","computing",etc..

***Lo stato di "idle" è considerato lo stato di default.***

L'insieme degli stati del nodo è definito in questo modo $$\text{state}(x)=\text{insieme finito di possibili stati in cui il nodo si può trovare}$$
>[!warning]- Attenzione
>È importante ricordare che ad ogni istante di tempo, un nodo può trovarsi in uno e un solo stato ben definito (non abbiamo quindi stati intermedi, ambigui)

## Eventi possibili sul SD, Comportamento di un nodo e del sistema

Ogni entità al tempo $0$ si trova nello stato di "idle", cioè dormiente (tranne almeno una chiamata *INITIATOR*, vedi avanti)

Le varie entità possono essere stimolate da eventi esterni al SD, tra cui : 
- Tick del clock
- Impulso spontaneo (ad es. impulso generato da un sensore, in una rete di sensori)
- Ricezione del messaggio
- etc..

La **regola** generale che vale per ogni entità è la seguente : 
$$\text{stato}\times\text{evento}\to\text{azione}$$
Ciò significa che un'azione che l'entità esegue è ben definita e determinata dalla coppia (stato,evento)

L'azione di un nodo ha le seguenti proprietà : 
- è **atomica** : ciò significa indivisibile, non può essere interrotta
- è **terminale** : ciò significa che l'azione deve terminare entro un tempo finito

Da qui determiniamo il **comportamento** di un'entità
$$B(x)=\text{insieme di regole }\forall\text{ possibile stato ed evento}$$
Il comportamento di un nodo si dice : 
- **deterministico** : se alla coppia (stato,evento) è associata ***una*** sola azione
- **completo** : se $\forall$ coppia (stato,evento) $\exists$ un'azione.

**Comportamento del sistema**

Possiamo ora definire il comportamento dell'intero sistema, come $$B=\{B(x):x\in V\}$$
Tale comportamento si dice **simmetrico** se tutte le entità hanno stesso comportamento $$B(x)=B(y),\forall x,y\in V$$
## Comunicazioni

Abbiamo detto prima che i nodi possono comunicare fra loro mediante link di comunicazione, scambiandosi messaggi.

Un **messaggio** nel SD altro non è che una sequenza finita di ***bit***

Modelliamo il SD come un grafo diretto, usando il *modello point-to-point*

Indichiamo con : 
$$\begin{align}&N_o(x)=\text{insieme dei vicini uscenti da x}\\&N_i(x)=\text{insieme dei vicini entranti in x}\\&\forall x\in V\end{align}$$
Un qualunque nodo x può mandare messaggi solo a $N_o(x)$
Un qualunque nodo x può riceve messaggi solo da $N_i(x)$

# Assiomi/Restrizioni

Definiamo ora un pò di **assiomi/restrizioni** che applicheremo al nostro SD

