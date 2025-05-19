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

# Modello GOSSIP


 