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

