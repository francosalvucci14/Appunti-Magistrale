# Leader Election

Nei SD spesso è necessario che una singola entità coordini il lavoro delle altre entità per la risoluzione dei task.

Tale entità prende il nome di **leader**, e trovare il leader in un insieme di entità è noto come il **Leader Election Problem**.

Fare Leader Election significa "Rompere" la simmetria

![[Pasted image 20250401120511.png|center|500]]

La configurazione iniziale è : $\forall x\in V,state(x)=asleep$
- quante sono le possibili configurazioni iniziali? -> $2^{n-1}$
La configurazione finale è : $\exists!x\in V:state(x)=leader\land\forall y\in V-\{x\}:state(y)=follower$
- quante sono le possibili configurazioni finali? -> $n$

Le restrizioni che usiamo sono $R=\{TR,BL,CN\}$

Notiamo come non abbiamo messo la restrizione $UI$, dato che ogni entità può essere il leader.

Allora vale il seguente teorema 

>[!teorem]- Angluin 80
>Il problema dell'**elezione** non può essere risolto in modo deterministico se le entità nel SD non hanno ***identità*** differenti.

La dimostrazione è identica a quella del triangolo, nel problema STP

**oss** : con differenti ID, il problema Minimum Finding diventa una elezione

![[Pasted image 20250401120736.png|center|400]]

## Elezione in alberi

Ad ogni nodo $x$ è associato un identificatore distinto $v(x)$

Un semplice algoritmo per fare leader election è : 
1. Esegui la technica della saturazione
2. Scegli il nodo saturato che ha il valore minimo

## Elezione in grafi ad anello

Cos'è un grafo ad anello? Un grafo ad anello è un grafo in cui : 
- $n$ entità
- $m=n$ links
- Topologia simmetrica
- Ogni entità ha esattamente due vicini
- C'è il senso della direzione (sx,dx)

Ad esempio 
![[Pasted image 20250401121153.png|center|400]]

Notiamo che gli ID dei nodi non sono necessariamente **consistenti**, cioè non è detto che $id(x_i)=i$ o $id(x_i)=k\implies id(x_{i+1})=k+1$

**definizione del problema**
- configurazioni iniziali -> $\forall x,state(x)=idle$, un nodo (o più) viene svegliato
	- il num di config. iniziali è $2^n$
- configurazione finale -> $\exists!v\in V:state(v)=leader\land\forall x\in V-\{v\}:state(x)=follower$ 
	- il num di config. finali è $n$

### Protocollo All The Way

**Idea base** : Ogni *id* viene trasmesso circolarmente nell'anello -> ogni entità vede tutte le *identità*

Assunzioni : 
- Ci sono due versioni -> link unidirezionali/bidirezionali
- Orientazione locale -> non nocessariamente presente il senso della direzione
- Identità distinte

Quando un nodo decide di fermarsi? 
- Risp 1 : Quando "finalmente" riceve il suo messaggio indietro
- Risp 2 : Quando riceve esattamente $n-1$ altre identità

Entrambe le risposte sono però sbagliate
1. Assume un'ordinamento dei messaggi (FIFO)
2. Assume che i nodi conoscano $n$

Vediamo ora il protocollo

Gli stati sono : 
- $S=\{ASLEEP,AWAKE,FOLLOWER,LEADER\}$
- $S_{init}=ASLEEP$
- $S_{term}=\{FOLLOWER,LEADER\}$

```
INITIALIZE

count = 0
size = 1
know = false
invia("Election",id(x),size) a destra
min = id(x)
```

```
ASLEEP

Spontaneamente
	INITIALIZE
	diventa AWAKE

Riceve("Election",value,counter)
	INITIALIZE
	invia indietro ("Election",value,counter+1) agli altri
	min = Min{min,value}
	count=count+1
	diventa AWAKE
```

```
AWAKE
Ricevo("Election",value,counter)
	if value != id(x) :
		invia("Election",value,counter+1) agli altri
		min = Min{min,value}
		count=count+1
		if known = true : /*solo se known=true conosco n e posso fare CHECK e TERMINATION*/
			CHECK
		endif
	else :
		ringsize=counter
		known = true
		CHECK
	endif
```

```
CHECK
if counter=ringsize : 
	if min = id(x) :  /*posso fermarmi qui*/
		diventa LEADER
	else
		diventa FOLLOWER
	endif
endif
```

#### Message Complexity

**Ogni** entità attraversa **ogni** link -> $n^2$
La grandezza di ogni messaggio è $\log(id+counter)$

Quindi abbiamo : 
- $O(n^2)$ messaggi
- $O(n^2\log(MaxID))$ bits necessari

**oss** : Il protocollo funziona sia per i link unidirezionali che per quelli bidirezionali

### Protocollo AsFar (as it can)

**Idea base** : Non è *necessario* mandare e ricevere messaggi con id **più grandi** degli id che sono stati già visti

Assunzioni le stesse dell'altro protocollo

![[Pasted image 20250407105544.png|center|400]]

Ricevo $y$ ***più piccolo*** di me : 
- **invio(y)** agli altri vicini

![[Pasted image 20250407105722.png|center|400]]

Ricevo $y$ ***più grande*** di me : 
- **invio(x)** agli altri vicini (se non è stato già inviato)

Vediamo il protocollo

Gli stati sono gli stessi dell'altro protocollo

```
ASLEEP
Spontaneamente
	invia("Election",id(x)) a destra
	min = id(x)
	diventa AWAKE

Ricevo("Election",value)
	invia("Election",id(x)) a destra
	min = id(x)
	if value < min : /*questo può essere evitato se id(x) > value */
		invia("Election",value) agli altri
		min = value
	endif
	diventa AWAKE
```

```
AWAKE
Ricevo("Election",value)
	if value < min : 
		invia("Election",value) agli altri
		min = value
	else
		if value = min : 
			NOTIFY
		endif
	endif

Ricevo(Notify)
	invio (Notify) agli altri
	diventa FOLLOWER
```

```
NOTIFY
	invia(Notify) a destra
	diventa LEADER
```

#### Correttezza e Terminazione

Il **Leader** sa che lui è Leader quando riceve ***il suo messaggio*** indietro.
Quindi lui può TERMINARE, ma quando gli altri sanno che possono terminare?
- è necessaria una **Notifica** dal Leader
#### Message Complexity

Dipende fortemente dalla configurazione degli ID sull'anello

$$rank(id)=\text{num. id più piccoli di id}+1$$

La situazione worst-case è : 

![[Pasted image 20250407110509.png|center|500]]

##### Analisi Worst-Case

Gli ID sono distribuiti in sequenza, da sx verso dx

![[Pasted image 20250407110936.png|center|400]]


Abbiamo che : 
- Dal nodo $1\to n$ links
- Dal nodo $2\to n-1$ links
- Dal nodo $3\to n-2$ links
- $\vdots$
- Dal nodo $n\to 1$ link

In totale quindi abbiamo : $n+(n-1)+(n-2)+\dots+1=\sum\limits_{i=1}^{n}\frac{n(n+1)}{2}$
Quindi abbiamo che : $$M(AsFar)_{worst-case}=\frac{n(n+1)}{2}+\underbracket{n}_{\text{notifica}}$$
Leggermente migliore del protocollo All The Way

##### Analisi Best-Case

![[Pasted image 20250407110957.png|center|400]]

- Dal nodo $1\to n$ links
- $\forall i\neq1\to1$ link (totale $n-1$)

In totale quindi : 
$$M(AsFar)_{best-case}=n+(n-1)+\underbracket{n}_{\text{notifica}}=O(n)$$
---

# Leader Election : Stage Technique

