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

Il protocollo lavora in *Stages* -> Ogni nodo sa in quale Stage lui sta performando

**Analisi del protocollo** : Alla fine di ogni Stage, alcune **proprietà globali** vengono mantenute

## Controlled Distance

**Idea base** : Si lavora in Stages. Un'entità mantiene il controllo sul suo messaggio

Assunzioni : $\{BL,ID,LO\}$ 

Il senso della direzione è mantenuto solo per semplicità, non serve

Cosa ci serve?
1. Distanza limitata (per evitare che messaggi grandi viaggino troppo a lungo) -> stage $i$ distanza $2^{i-1}$
2. Messaggi di ritorno (se viene visto qualcosa più piccolo non si continua)
3. Controllo su ambo i lati
4. Il più piccolo vince sempre

Il protocollo lavora così -> I *candidati* iniziano l'algoritmo

Vediamo lo Stage $i$, per qualche $i$

1. Ogni candidato invia un messaggio con il proprio ID in entrambe le direzioni
2. Il messaggio viaggerà finchè non incontrerà un ID più piccollo o finchè non raggiungerà una certa distanza $(2^{i-1})$
3. Se il messaggio non incontra un ID più piccolo, allora tornerà indietro al proprietario. (chiamati **messaggi di feedback**) ![[Pasted image 20250409141925.png|center|500]]
4. Un candidato che **riceve il proprio messaggio di feedback da ambo le direzioni** sopravvive ed inizia il prossimo stage

Le entità incontrate lungo il percorso leggono il msg e : 
- Ogni entità $i$ con un ID **più grande** diventa **sconfitto** (passivo)
- Un entità **sconfitta** inoltra i messaggi originati da altre entità; se il messaggio è la **notifica** di terminazione, allora termina

![[Pasted image 20250409142227.png|center|500]]

Vediamo un piccolo riassunto

![[Pasted image 20250409142315.png|center|500]]

### Correttezza e Terminazione

Se un candidato riceve uno (sinistra/destra) dei suoi messaggi dal lato opposto (destra/sinistra) lo invia, diventa il ***leader*** e lo notifica

Alcune proprietà : 
- L'ID più piccolo percorrerà sempre la distanza massima sconfiggendo ogni entità che incontra
- La distanza aumenta monotonicamente diventando infine maggiore di $n$
- Il Leader eventualmente riceverà il suo messaggio dalla direzione opposta

**Problema** : Che succede se un'entità riceve il messaggio da uno stage maggiore del suo attuale?

Possibile situazione cattiva : Un nodo è sconfitto da un qualche messaggio allo stage $8$ e, dopo questo, riceve il suo messaggio di feedback dello stage $7$

**Soluzione** : L'aproccio greedy funziona sempre!

***Se a qualunque istante di tempo un nodo riceve un ID più piccolo (di qualunque stage), diventerà sconfitto e non aspetterà più per il suo messaggio di feedback***

### Message Complexity

Diamo una definizione importante : $n_i$ numero di nodi che iniziano lo stage $i$

>[!teorem]- Lemma
>Se $x$ inizia lo stage $i$ (ovvero sopravvive allo stage $i-1$) l'ID di $x$ deve essere più piccolo dell'ID dei vicini a distanza fino a $2^{i-2}$ su ogni lato

![[Pasted image 20250411131505.png|center|600]]

In un gruppo di $2^{i-2}+1$ entità consecutive **al più una** può sopravvivere allo stage $i-1$

Quindi : $$n_i\leq\frac{n}{2^{i-2}+1}$$
![[Pasted image 20250411131635.png|center|500]]

![[Pasted image 20250411131652.png|center|500]]

Vediamo ora il num di messaggi.

Abbiamo due tipo di messaggi -> "Forth" e "Feedback"

**Stage** $i\gt1$
- "Forth" : ognuno di essi viaggerà al più $2^{i-1}$ in entrambe le direzioni
	- Tot : $2n_i2^{i-1}$
- "Feedback" : 
	- ogni sopravvissuto ne riceverà uno da ogni lato
		- $2n_{i+1}2^{i-1}$
	- ogni entità che ha iniziato lo stage ma non è riuscita a sopravvivere ne riceverà uno o nessuno
		- $\leq\underbrace{(n_i-n_{i+1})}_{\text{Nodi che non superano lo stage i}}2^{i-1}$
	- Tot : $2n_{i+1}2^{i-1}+(n_{i+1}-n_i)2^{i-1}$

Quindi, mettendo le due cose insieme otteniamo 
$$\begin{align}M(Fase-i)&=2n_i2^{i-1}+2n_{i+1}2^{i-1}+(n_{i+1}-n_i)2^{i-1}=\\&=(3n_i+n_{i+1})2^{i-1}\\\left[n_i\leq\frac{n}{2^{i-2}+1}\right]\to&\leq\left(3\left\lfloor\frac{n}{2^{i-2}+1}\right\rfloor+\left\lfloor\frac{n}{2^{i-1}+1}\right\rfloor\right)2^{i-1}\\&\lt\frac{3n2^{i-1}}{2^{i-2}}+\frac{n2^{i-1}}{2^{i-1}}\\&=6n+n=7n\end{align}$$
Per lo stage $1$ la situazione è leggermente differente

**Stage** $1$
- Se tutti iniziano : 
	- I sopravvisuti mandano $4n_22^0$ messaggi -> 2 "Forth", 2 "Feedback"
	- Gli altri $3(n-n_2)2^0$ -> 2 "Forth", 1 "Feedback"

In totale abbiamo $$4n_2+3n-3n_2=n_2+3n\underbrace{\lt}_{\text{Ricordando }n_2\leq\frac{n}{2^0+1}}4n$$
**Numero di stage totali**

L'anello è attraversato completamente fintanto che $2^{i-1}$ è maggiore/uguale a $n$
$$2^{i-1}\gt n\iff i\geq\log(n)+1$$
Quindi abbiamo in totale $\log(n)+1$ stage

A questo punto, la message complexity totale sarà $$M(StageTechnique)\leq\sum\limits_{i=1}^{\log(n)}7n+\underbrace{O(n)}_{\text{primo stage}}=n\sum\limits_{i=1}^{\log(n)}7=7n\log(n)+O(n)\implies O(n\log(n))$$
## Congettura

>[!teorem]- Congettura
>In anelli non direzionati, la complessità nel caso peggiore è $n^2$; per avere una complessità di $O(n\log(n))$ messaggi, la bidirezionalità è necessaria

Questa congettura però non è vera

### Stages

**Idea base** : 
- Un messaggio viaggerà finhè non raggiungerà un'altro candidato.
- Un candidato riceverà un messaggio da ambo i lati

Le assunzioni sono le stesse della Stage Technique, aggiungendo il Message Ordering

Come funziona questa tecnica : 
- Ogni candidato invia il suo ID in entrambe le direzioni![[Pasted image 20250411134533.png|center]]
- Quando un candidato $i$ riceve due messaggi $ID_j$ (da dx) e $ID_k$ (da sx), determina se può diventare *passivo* (ovvero lui non è il valore più piccolo), oppure se deve rimanere *candidato* (ovvero è il più piccolo) ![[Pasted image 20250411134700.png|center|600]]
Dopo aver ricevuto il primo messaggio, l'entità effettua l'operazione **close-port** (ovvero accoda tutti i messaggi in arrivo dopo il primo)

Dopo aver ricevuto il secondo messaggio, l'entità effettua l'operazione **re-open-port**

#### Correttezza e Terminazione

L'entità con ID minimo non smetterà mai di inviare messaggi

Quando poi unìentità sa di essere Leader, invia un messaggio di Notifica che viaggerà su tutto l'anello

#### Complessità - Worst Case

**Ad ogni step** : Almeno la metà delle entità diventa passiva, quindi $n_{i+1}\leq\frac{n_i}{2}$

Quindi abbiamo che : 
$$n_0=n,n_1\leq\frac{n}{2},\dots,n_i\leq\frac{n}{2^i}$$
Ora, $$\frac{n}{2^k}\leq1\iff k\geq\log(n)$$
Quindi abbiamo **#step** al più $\log(n)$
Ogni entità invia o reinvia $2$ messaggi, quindi : 
- **#mess** : $2n$
- **#bits** : $2n\log(n)$

**L'ultima entità** invia $2n$ messaggi per capite che è l'ultima entità attiva, poi $n$ messaggi per notificare

In totale quindi : 
$$M(Stages)=2n\log(n)+3n=O(n\log(n))$$
---
# Architettura Mesh

Vediamo ora il problema della Leader Election all'interno dell'architettura Mesh

Una Mesh $M$ di dimensione $a\times b$ ha : 
- $n=a\times b$
- $m=a(b-1)+b(a-1)=O(n)$

All'interno della Mesh esistono tre tipologie di nodo : 
1. **Corner** : nodo che sta ai 4 angoli della Mesh
2. **Border** . nodo che sta sul perimetro della Mesh (bordo)
3. **Interior** : nodo interno alla Mesh

![[Pasted image 20250411135602.png|center|600]]

Alcuni fatti importanti : 

1. Fatto $1$ : Topologia **asimmetrica**
2. Fatto $2$ : Il sottografo indotto dai Corners+Borders è un **ANELLO**

Vediamo quindi Il protocollo per l'elezione nelle Mesh
## Protocollo per Leader Election

**Idea** : si elegge un Leader come uno dei $4$ Corner

Questo protocollo lavora in $3$ fasi : 
1. Fase di **Wake Up**
2. Fase di **Elezione** (sui bordi) solo tra i Corners
3. Fase di **Notifica** (Broadcast)

Vediamo nel dettaglio