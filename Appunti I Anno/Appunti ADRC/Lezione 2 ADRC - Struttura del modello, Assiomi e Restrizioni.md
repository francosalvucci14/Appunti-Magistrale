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

## Scambio messaggi

1. Il tempo di invio dei messaggi è un tempo finito
2. Ogni entità distingue i suoi vicini (abbiamo porte logiche numerate in locale sul nodo $x,\forall x$)

Possiamo avere che per un certo nodo $a$, la porta uscente verso il nodo $b$ sia etichettata con "2", mentre viceversa la porta sia etichettata con "16"

Il protocollo ***non si deve*** basare su questo tipo di etichettamento

La ***topologia*** : Grafo etichettato $(G,\lambda)$
- Per ogni nodo $x,\lambda_x(x,y)$ indica la numerazione della porta sull'arco da $x\to y$

La distinzione dei messaggi vale sia in uscita che in entrata

## Ordinamento messaggi

I messaggi arrivano uno alla volta.

Se arrivano più messaggi su un nodo,essi vengono organizzati secondo il modello **FIFO**:
- il primo arrivato viene letto
- gli altri si accodano in attesa.

Abbiamo quindi una struttura dati ***queue***
Non può accadere che venga letto prima l'ultimo messaggio arrivato

## Link bidirezionali

Se ci troviamo nella situazione in cui 
$$\begin{align}&\forall x,N_i(x)=N_o(x)=N(x)\space\land\\&\forall y\in N(x):\lambda_x(x,y)=\lambda_y(x,y)\end{align}$$
Allora possiamo parlare di ***link bidirezionali***

Possiamo quindi trattare gli archi orientati, entranti e uscenti, come archi non orientati, mantenendo l'etichettatura delle porte. 

In questo caso, i nodi possono riconoscere chi gli ha inviato il messaggio

## Assunzioni su reliability

- **Garanteed Delivery** : Ogni messaggi inviato sarà ricevuto senza corruzioni
- **Partial Reliability** : Non ci saranno faults $(*)$
- **Total Reliability** : Non ci sono stati faults (nel passato), non ci sono faults e non ci saranno faults a prescindere (in futuro)
	- Quasi sempre useremo questa assunzione

$(*)$ Faults : Errore che potrebbe capitare nel SD. Si dividono in due tipi : 
- Fault-Arco : Messaggio non arriva mai
- Fault-Nodo : Messaggio corrotto
## Restrizioni topologiche

- Grafo fortemente connesso
- Grafo ad anello
- etc..

## Restrizioni su conoscenza

- Conoscenza del numero di nodi
- Conoscenza sul numero di link
- Conoscenza del diametro della rete
- etc..

## Restrizioni sul tempo

- **Bounded Communication Delay** : $\exists$ costante $\Delta$ tale che, in assenza di errori, il delay dei messaggi è al più $\Delta$
- **Clock sincronizzati** : Tutti i clock sono incrementati di una unità in modo simultaneo e ad intervalli costanti

# Misure di complessità - Performance

Abbiamo sostanzialmente due misure per misurare la complessità del protocollo : 

1. P.O.V. del sistema : La misura è l'**ammontare di comunicazioni** = numero di bit scambiati da inizio a fine
2. P.O.V dell'utente : La misura è il **tempo**
	1. In questo caso, i vari delay dei messaggi non sono predictabili (non mi ricordo in italiano come si scrive)
	2. ***Il tempo ideale*** sarebbe : 1 unità di tempo $\times$ 1 messaggio

# Esempio Broadcast

Assunzioni = Restrizioni

- Abbiamo un unico INITIATOR (per def. del problema)
- Ci mettiamo nel caso di Total Reliability con Link Bidirezionali (assunzioni per semplificare)
- $G$ è connesso (altrimenti irrisolvibile)

## Algoritmo FLOOD

**Idea** : Se un'entità sa qualcosa, la manda ai suoi vicini

Abbiamo due tipi di entità : 
1. La prima, detta INITIATOR, che è colui che si "sveglia" per primo e fa partire tutto il protocollo.
	1. L'initiator è una sola entità, per assunzione del problema
2. La seconda, detta SLEEPING, che aspetta che un evento esterno la svegli

Le azioni che le due entità eseguono sono le seguenti : 

```
INITATOR
Spontaneamente
	invia (I) a N(x)
```

```
SLEEPING
Riceve(I)
	invia (I) a N(x)
```

Fatto in questo modo, il protocollo :
- è corretto
- in tempo finito termina il task $(*)$
- ***ma*** non termina mai $(!!!)$

Dimostriamo ora $(*)$ usando il seguente lemma

**Lemma** : 
$\forall l\geq0\exists$ un tempo $t\in\mathbb N$ tale che $$\forall v\in L_l(s),v\text{ è "informed"}$$
Definiamo con $L_l(s)$ i nodi a distanza $l$ dal nodo $s$

***dimostrazione per induzione su*** $l$
- Caso Base : $l=0\to$ trivial
- Caso Induttivo : $\forall v\in L_{l-1}(s)\to v$ è "informed"
	- Per il C.I tutti i nodi presenti in $L_{l-1}(s)$ hanno una copia del messaggio
	- $v\in L_l(s)$ implica che $\exists w\in L_{l-1}:(w,v)\in E$
	- Per le restrizioni che abbiamo imposto : $\exists t\in\mathbb N:v$ è "informed"

### Ottimizzazione

Come abbiamo visto, il protocollo cosi fatto risulta essere corretto, e ci garantisce che in un certo tempo finito completa il task.

Il problema sta nel fatto che questo protocollo non termina mai, anche dopo aver completato il task

Vediamo come migliorarlo : 
**Idea** : mando a tutti il messaggio tranne che al sender, poi mi metto in un nuovo stato chiamato DONE
- Ogni nodo quindi non ha più due stati {INITIATOR,SLEEPING} ma avrà tre stati {INITIATOR,SLEEPING,DONE}

L'algoritmo modificato è quindi il seguente : 

```
IF INITIATOR
	Spontaneamente
		invia (I) a N(x)
		diventa DONE
IF SLEEPING
	Riceve (I)
		invia (I) a N(x) - {sender}
		diventa DONE
IF DONE
	do-nothing
```



