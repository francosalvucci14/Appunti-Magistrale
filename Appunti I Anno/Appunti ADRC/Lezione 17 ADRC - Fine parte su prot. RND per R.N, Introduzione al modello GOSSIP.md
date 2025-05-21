# Continuo prot. RND per R.N

## Estendere BGI a grafi generali

Possiamo estendere il protocollo BGI a **grafi generali** per completare il Broadcast in temp $O(D\log^2(n))$ w.h.p

Per fare ciò dobbiamo metterci nella restrizione che i nodi conoscano $n$

Modifichiamo il protocollo BGI in questo modo, aggiungendo un ulteriore ciclo for : 

For $L=1,\dots,\lceil\log(n)\rceil$
- Nodo trasmette con probabilità $\frac{1}{2^L}$

Il protocollo modificato sarà quindi : 

For $K=1,\dots$ (stages)
- For $L=1,\dots,\lceil\log(n)\rceil$
	- For $j=1,2,\dots,c\log(n)$
		- Se nodo $x$ è stato informato in stage $k-1$, $x$ trasmette con probabilità $\frac{1}{2^L}$

Vediamo che : 
- Il ciclo for interno costa $O(\log(n))$
- Il secondo ciclo for costa anch'esso $O(\log(n))$
- Il ciclo for più esterno costa $O(D)=\text{diam(G)}$

In totale abbiamo che $$Time(BGI-Mod)=O(D\log^2(n))$$
Se i nodi non conoscono $n$, possono "indovinarne" il valore usando la ricerca **binaria**
- Così facendo però i nodi non possono terminare
- Il tempo di completamento diventa $O(D\log^3(n))$ w.h.p

---
# Modelli GOSSIP

Abbandoniamo il modello RADIO per introddure una nuova classe di modelli, ovvero i modelli **GOSSIP**. (nello specifico **GOSSIP PUSH e PULL**)

Per un grafo non diretto $G=(V,E)$, con $|V|=n$ e $|E|=m$, denotiamo il vicinato di un nodo $v\in V$ come $N(v)$ e $d(v)=|N(v)|$

>[!definition]- Definizione (Il modello GOSSIP PUSH (PULL))
>Dato un (non diretto) grafo $G(V,E)$, il modello di comunicazione **uniforme** PUSH (PULL) lavora in modo sincrono, con roud discreti. 
>Ad ogni round $t=0,1,\dots$ ogni nodo $v\in V$ **sceglie** u.a.r uno dei suoi vicini $u\in_uN(v)$ ed esegue l'operazione di **push (pull)** per prendere (inviare) un qualunque messaggio $M$ da (a) $u$
>Alla fine di ogni round $t$, il nodo $u$ (nodo $v$) avrà il messaggio $M$

## Proprietà dei modelli GOSSIP

Ad ogni round, il numero totale di comunicazioni (es. trasmissioni dei messaggi) è $n$ in entrambi i modelli.

In particolare, queste comunicazioni generano un grafo diretto delle comunicazioni al round $t$ chiamato $G_t(V_t,E_t)$, dove $E_t$ rappresenta l'insieme di **archi attivi** ad ogni round $t$.
Il grafo $G_t$ è sempre un **grafo sparso**.

Valgono quindi le seguenti proprietà
1. Nel modello **PUSH**, ad ogni round, il numero atteso di operazioni *push* **ricevute** da ogni nodo è $1$, e in totale è $O(\log(n))$ w.h.p
2. Nel modello **PULL**, ad ogni round, il numero atteso di operazioni *pull* **ricevute** da ogni nodo è $1$, e in totale è $O(\log(n))$ w.h.p

## Protocollo PULL su Clicque

Analizziamo il seguente PULL Broadcast Protocolo (***BP***) sul grafo completo $K(V,E)$

Sia $M$ l'informazione che ogni nodo deve possedere per completare il task del Broadcast.
Assumiamo che ogni entità $x\in V$ abbiamo un registro privato $c_x$ tale che : $$c_x=\begin{cases}\text{informed}&\text{x ha ricevuto M}\\\text{not-informed}&\text{x non ha ricevuto M}\end{cases}$$
In modo formale, il problema è descritto dalla tripla $\langle P_{init},P_{final},G_{pull}\rangle$, dove : 
- $P_{init}=\exists!x\in V:c_x=\text{informed}\land\forall y\neq x,c_y=\text{not-informed}$
- $P_{final} = \forall x\in V : c_x=\text{informed}$
- $G_{pull}=$ Restrizioni del modello GOSSIP $\cup$ KT
	- $KT=$Knowledge Topology

Vediamo ora il protocollo effettivo

Tutti i nodi, durante l'esecuzione del protocollo possono trovarsi nei due stati possibili, ovvero $\{\text{informed,not-informed}\}$ 

BP su $K_n,s\in V$: 
- Inizialmente la sorgente $s$ è l'unica nello stato $\text{informed}$, in quanto è l'unica a possedere il messaggio $M$. Tutti gli altri nodi si trovano nello stato $\text{not-informed}$
- Ad ogni round $t\geq1$ ogni nodo $v$ che si trova nello stato $\text{not-informed}$ esegue una operazione di **pull** su un'altro nodo $u\in_uN(v)$ : 
	- Se $u$ è un nodo nello stato $\text{informed}$, allora $v$ si fa inviare una copia di $M$ e passa allo stato $\text{informed}$
- Il protocollo termina globalmente quando tutti i nodi si trovano nellos tato $\text{informed}$


