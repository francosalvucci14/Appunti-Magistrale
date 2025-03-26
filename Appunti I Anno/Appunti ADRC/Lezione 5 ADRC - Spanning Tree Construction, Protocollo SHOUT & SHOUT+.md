Fin'ora abbiamo visto il problema Broadcast, andando a vedere diversi protocolli che lo risolvono.
Spostiamoci ora su un'altro problema, ovvero il problema **Spanning Tree Construction**

# Spanning Tree Construction

>[!definition]- Spanning Tree
>Uno spanning tree $T$ di un grafo $G=(V,E)$ è un sottografo aciclico di $G$ tale che $T=(V,E')$ e $E'\subset E$

Le assunzioni che andiamo a fare in questo problema sono le seguenti : 
- **Single Initiator**
- Bidirectional Links
- Total Reliability
- $G$ connesso.

## Motivazioni

Perchè vogliamo costruire uno spanning tree del sistema distribuito? 
Ci sono due motivazioni : 
1. Effettuare comunicazioni (**broadcast**) su una sottorete è molto più efficente ($m$ è più piccolo)
2. La subnet deve essere : 
	1. Spanning (cioè toccare tutti i nodi della rete)
	2. Connected

Ogni **Spanning Tree** è lo spanner connesso avente ***minimo*** numero di links

## Il problema ST Distribuito

**Configurazione iniziale** : $\forall x,Tree-neigh(x)=\{\}$
- Significa che all'inizio, ogni nodo ha variabile Tree-neigh vuota
- La situazione è la seguente $\downarrow$  

![[Pasted image 20250326100823.png|center|300]]

**Configurazione finale** : $\forall x,Tree-neigh(x)=\{\text{x-links che appartengono allo ST}\}$
- Quindi, alla fine, ogni nodo dovrà selezionare solo gli archi che fanno parte della soluzione globale, ovvero l'intero ST del sistema distribuito
- La situazione è la seguente $\downarrow$

![[Pasted image 20250326101033.png|center|300]]

>[!warning]- Osservazione cruciale
>I nodi possono ***non conoscere*** lo ST anche **dopo** la computazione

Vediamo ora i vari protocolli per questo problema

### Protocollo SHOUT

L'idea è : Come fa un nodo $x$ a selezionare i suoi vicini validi per ST?

Semplicemente **lo chiede** !

La risposta dei vicini sono : Rispondi sempre SI alla prima richiesta e NO alle altre

L'initiator inizia a chiedere e poi il protocollo procede come il **broadcast** con gli ***acks***

![[Pasted image 20250326101635.png|center|600]]

Vediamo ora il protocollo effettivo

Gli stati possibili 
- $S=\{Initiator,Idle,Active,Done\}$
- $S_{init}=\{Initiator,Idle\}$
- $S_{term}=\{Done\}$

```
INITIATOR
Spontaneamente
	root=True
	Tree-neigh = {}
	invia (Q) a N(x)
	counter = 0
	diventa ACTIVE
```

```
IDLE
Riceve(Q)
	root=False
	parent = sender
	Tree-neigh = {sender}
	invia (Yes) a sender
	counter = 1
	if counter = |N(x)|
		diventa DONE
	else
		invia (Q) a N(x)-{sender}
		diventa ACTIVE
```

```
ACTIVE

Riceve(Q)
	invia (No) a sender

Riceve(Yes)
	Tree-neigh = Tree-neigh U sender
	counter = counter+1
	if counter = |N(x)|
		diventa DONE

Riceve(No)
	counter = counter+1
	if counter = |N(x)|
		diventa DONE
```

**oss** : SHOUT=FLOOD+REPLY

#### Terminazione di SHOUT

>[!teorem]- Lemma
>Sotto le assunzioni standard $R$ su $G$, si ha che $\forall s\in V,\forall v\in V-\{s\}$, dopo l'esecuzione del protocollo SHOUT $\exists\space p:s\to v$ tale che :
>1. Da $s\to v$ è passato il messaggio $Q?$
>2. Da $v\to s$ è passato il messaggio $Yes$
>
>Questo cammino $\exists$ per le assunzioni TR e CN, in più c'è sempre un ordine.

$\not\exists$ ciclo perchè un nodo dovrebbe aver risposto $Yes$ a **due** "padri",e questo non è possibile
- Possono arrivare anche $1000$ messaggi $Q?$, ma le risposte saranno gestite una per una (ad es. usando una coda)

#### Correttezza di SHOUT

La correttezza del protocollo SHOUT si basa su queste assunzioni : 
- Se $x\in Tree-neigh(y)\implies y\in Tree-neigh(x)$
- Se $x$ invia Yes a $y$, allora $x\in Tree-neigh(y)$ ed è connesso all'initiator tramite una **catena** di Yes-links
- Ogni $x$ (eccetto l'initiator) invia esattamente un singolo Yes -> (no cicli !!)

Allora, lo spanning graph definito dalle relazione Tree-neigh risulta essere **connesso,aciclico** e contiene **tutti** i nodi.

#### Message Complexity

In modo informale, $$M(SHOUT)=2M(FLOOD)$$
Nel dettaglio : 
**Situazioni possibili** : ![[Pasted image 20250326103239.png|center|500]]
**Situazioni impossibili** : ![[Pasted image 20250326103321.png|center|500]]
Nel worst-case abbiamo che : 

**Numero totale di messaggi** $Q?$ 
![[Pasted image 20250326103408.png|center|500]]

Totale : $$2(m-(n-1))+(n-1)\implies 2m-n+1$$
**Numero totale di NO** : 
![[Pasted image 20250326103600.png|center|400]]
- $2(m-(n-1))$

**Numero totale di YES** : 
![[Pasted image 20250326103700.png|center|400]]
- Esattamente $(n-1)$

In totale : $$2m-n+1+2(m-(n-1))+n-1=4m-2n+2$$
Quindi $M(SHOUT)=4m-2n+2$

Notiamo che $\Omega(M)$ è **lower-bound** anche in questo caso

Cerchiamo di abbassare la complessità $4m$, raffinando il protocollo SHOUT

### Protocollo SHOUT+

I messaggi NO sono realmente necessari? la risposta è no
- un nodo ha bisogno di sapere quando può **terminare**

**oss** : 
Se $y$ manda No a $x$, allora deve accadere che $y$ ha mandato anche $Q?$ a $x$ PRIMA.
Quindi, ricevere $Q?$ può essre *interpretato* come un NO dalla stessa porta !!

Vediamo quindi il protocollo

Gli stati possibili 
- $S=\{Initiator,Idle,Active,Done\}$
- $S_{init}=\{Initiator,Idle\}$
- $S_{term}=\{Done\}$

```
INITIATOR
Spontaneamente
	root=True
	Tree-neigh = {}
	invia (Q) a N(x)
	counter = 0
	diventa ACTIVE
```

```
IDLE
Riceve(Q)
	root=False
	parent = sender
	Tree-neigh = {sender}
	invia (Yes) a sender
	counter = 1
	if counter = |N(x)|
		diventa DONE
	else
		invia (Q) a N(x)-{sender}
		diventa ACTIVE
```

```
ACTIVE

Riceve(Q) (da interpretare come NO)
	counter = counter+1
	if counter = |N(x)|
		diventa DONE

Riceve(Yes)
	Tree-neigh = Tree-neigh U sender
	counter = counter+1
	if counter = |N(x)|
		diventa DONE
```

#### Message Complexity

Su ogni link ci saranno esattamente $2$ messaggi : 

Questo : ![[Pasted image 20250326140212.png|center|400]]
Oppure questo :
![[Pasted image 20250326140236.png|center|400]]

Di conseguenza, $$M(SHOUT+)=2m$$
Che risulta essere **migliore** di $4m-2n+2$

**Terminazione locale** : Ogni nodo sa quando può smettere di lavorare
**Terminazione globale** : Può un qualunque nodo decidere **quando** tutti gli altri devono terminare??
- Possibile solo sotto l'assunzione UI, pagando un prezzo per la message complexity pari a $n-1$ in più

## Costruzione ST usando Broadcast

>[!teorem]- Teorema
>L'esecuzione di ogni protocollo di Boradcast costruisce uno ST

**idea della dimostrazione**

Definiamo il *father* di un nodo $x$

>[!definition]- Father(x)
>Il Father di un nodo $x$ è definito come : 
>$$Father(x)=[\text{il nodo che per primo invia il messaggio Init a x}]$$

**Fatto** : **l'ordine parziale** $Father(x)\gt x$ definisce uno ST con radice nell'Initiator

**oss** : Solo un Broadcast non è sufficiente (Non abbiamo la conoscenza locale dello ST)

## SPT : Considerazioni Finali

Diamo $2$ considerazioni finali : 

1. Lo ST calcolat (costruito) **dipende** dal Protocollo
2. Lo ST calcolat (costruito) **dipende** dall'*esecuzione* del Protocollo

Prendiamo per esempio il protocollo SHOUT+

Ogni possibile ST del grafo $G$ può essere l'output di SHOUT -> "basta gestire i delay dei msg"

Di conseguenza : $diam(ST)\gt\gt diam(G)$ (Problema)

E quindi sorge un nuovo problema, ovvero costrutire uno ST $T^*$ tale che $diam(T^{*})\simeq diam(G)$

## Costruzione ST usando Multiple Initiator

Le domande che ci poniamo in questa situazione sono :
1. Possiamo costrutire lo ST usando più Initiator?
2. E se usassimo il protocollo SHOUT+ per questo?
3. Possiamo creare un protocollo **deterministico** per questo problema?

La risposta a tutte e $3$ le domande è NO.

Vediamo un esempio più teorema dopo

![[Pasted image 20250326141410.png|center|500]]

>[!teorem]- Teorema
>Il problema del costruire lo ST è ***deterministicamente*** irrisolvibile sotto le assunzioni $R$

**dim**

Mettiamoci nel caso più semplice, ovvero $3$ nodi $x,y,z$ che formano un triangolo, che hanno gli stessi **stati iniziali**.
- tutti iniziano la computazione a tempo $t=0$
- Eseguzioni sincrone

**Fatto** : Ad ogni istante di tempo $t\gt0$, i $3$ nodi devono : 
- trovarsi nello **stesso stato**
- fare le **stesse cose**

Quindi, sarà **impossibile** per loro selezionare $2$ links su $3$

![[Pasted image 20250326141750.png|center|600]]

