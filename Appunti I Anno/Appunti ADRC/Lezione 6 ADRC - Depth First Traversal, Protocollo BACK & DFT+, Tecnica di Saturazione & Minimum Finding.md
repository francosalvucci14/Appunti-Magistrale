Spostiamoci ora nel problema noto come **Depth First Traversal (DFT)**
# Problema Depth First Traversal

In questo problema andiamo a vedere la capacità di **somministrare** un token (risorsa) ad ogni nodo del SD, in modo mutualmente esclusivo (ad ogni istante di tempo, uno e un solo nodo avrà il token)

Ci mettiamo sotto le assunzioni standard $R={UI,BL,TR,CN}$

Vediamo la prima versione del protocollo per DFT, chiamato protocollo Back

## Protocollo Back

Per ogni nodo $x\in V$
1. Quando visitato per la **prima volta** - ricorda chi è il (**padre**)
	1. Invia il token a uno dei vicini non visitati
	2. aspetta la risposta
2. Quando il vicino riceve il **token**
	1. Se già visitato, rimanda il token al padre usando un **back-links**
	2. Altrimenti, **lo invia in modo sequenziale a tutti** i vicini non visitati prima di rimandarlo indietro
3. Se non ci sono più nodi inesplorati, ritorna il token (**reply**) al padre
4. Alla ricezione di un reply, invia il token ad un'altro vicino non visitato

### Message Complexity

Abbiamo 3 tipi di messaggi : token, back, return

- I messaggi di tipo Token vengono sempre inviati almeno una volta -> $O(m)$
- O vengono inviati o i messaggi Return (se in stato idle quando ricevo il token) **oppure** i messaggi back -> $O(m)$

Su ogni arco quindi passano due copie di messaggi, perchè return e back sono esclusive (o una o l'altra)

Quindi $$M(Back)=2m=O(m)$$
Notiamo che $\Omega(m)$ è un lower-bound anche qui

### Time Complexity (Ideal Time)

Ricordiamo che per fare l'analisi della time complexity dobbiamo metterci nel mondo sincrono, impostando i ritarti tutti a "1".

L'algoritmo per DFT, ovvero Back, è **sequenziale**. Quindi : 
$$Time(Back)=M(DFS)=\Theta(m)$$
>[!teorem]- Lower Bound generale
>$$Time(DFT)=\Omega(m)$$

Possiamo migliorare questo algoritmo? SI, migliorando il tempo ideale

## Protocollo DFT+

**oss** : In grafi densi, il più dei messaggi potrebbe essere sui back-links, e di conseguenza il più del tempo è speso su questi archi

Dovremmo riuscire ad evitare l'invio di messaggi sui back-links

**Idea** : Il nodo $x$ informa in parallelo $||$ tutto $N(x)$ quando viene visitato

![[Pasted image 20250328115209.png|center|300]]
![[Pasted image 20250328115233.png|center|300]]

$N(x)$ invia il messaggio **ok** indietro, sempre in $||$
- Questo è necessario quando il sistema non è sincrono

![[Pasted image 20250328115352.png|center|300]]

**Dopo** aver ricevuto **tutti gli akcs**, il nodo $x$ invia il token a uno dei suoi vicini ***non visitati*** ($x$ già li conosce tutti)

![[Pasted image 20250328115453.png|center|300]]
![[Pasted image 20250328115507.png|center|300]]
![[Pasted image 20250328115525.png|center|300]]

Il nodo $y$ sa che $x,w$ sono stati già visitati e che $z$ è suo padre, quindi i back-links vengono scoperti in **parallelo**

### Message Complexity

I messaggi sono : Token, Return, Visited, Ack (OK)

Ogni entità (tranne l'initiator) : riceve $1$ token, invia $1$ return -> $2(n-1)$

Ogni entità invia $1$ Visited a tutti i suoi vicini tranne che al sender
- Sia $s$ l'initiator, allora $$|N(s)|+\sum\limits_{x\neq s}(|N(x)|-1)=2m-(n-1)$$
- Stessa cosa per gli Ack : $2m-(n-1)$

Quindi in totale $$M(DFT+)=4m-2(n-1)+2(n-1)=4m$$
Notare che abbiamo peggiorato la message complexity da Back a DFT+

### Time Complexity

Se il sistema è sincrono : 
- Token e Return sono inviati **sequenzialemte** : $2(n-1)$
- Visited e Ack sono inviati in **parallelo** : $2n$

Totale $$Time(DFT+)=4n-2$$
Il tempo è **lineare** in $n$ e non in $m$ (TOP)

---
# Computazioni in Alberi

