# Time complexity : tempo ideale

Per calcolare la **time complexity** dei protocolli ci dobbiamo mettere nell'assunzione del modello sincrono

In questa assunzione tutti i ritardi li impostiamo ad "1".

Sotto quuesta ipotesi, modifichiamo il lemma della lezione scorsa così

>[!teorem]- Lemma*
>$\forall s\in V$ sorgente, $\forall h\geq1,\forall v\in L_h(s)$ abbiamo che : 
>$$v\to\text{DONE entro }h\text{ steps}$$

Nel sistema sincrono, se prendiamo $v\in L_h,u\in L_{h+1}$ abbiamo che $v$ viene informato per forza **prima** di $u$

Di conseguenza, $\forall v\in V$ si ha che $d(s,v)\leq n-1$, per essere più precisi : 
$$\max_x\{d(x,s)\}=\text{eccentricità di s}\leq Diag(G)\leq n-1\implies O(n)$$
Quindi il protocollo termina entro $n-1$ steps

---

Rivedi al volo parte prima di lower bound

---

# Lower Bound per Broadcast

Ritorniamo al problema Broadcast affrontato in precedeza.

>[!teorem]
>Sotto le assunzioni $R=\{UniqueInitiator (UI),Connectivity (CN),TotalReliability (TR),BidirectionaLink (BL)\}$ ogni protocollo per Broadcast, nel caso peggiore, richiede l'invio di $m$ messaggi $\implies\Omega(m)$ **Lower-Bound per la message complexity**

**dim x assurdo**
Sia $A$ un algoritmo che scambia meno di $m(G)$ messaggio (con $m(G)$ indichiamo il numero di archi in $G$), allora c'è **almeno** un arco in $G$ dove non è passata neanche una copia del messaggio ^tesi

Sia $e=(x,y)$ tale arco. Prendiamo il grafo $G$ e da lui creiamo un nuovo grafo $G'$, dove aggiungiamo un nuovo nodo $z$, lo colleghiamo ad $x,y\to(z,x)\in E',(z,y)\in E'$ ed eliminiamo l'arco $(x,y)\in E$
(Questa modifica avviene proprio sul SD, non solo sul grafo).

Di conseguenza : $$G'=\{V\cup\{z\},E-e\cup\{(z,x),(z,y)\}\}$$
Ora ripetiamo l'algoritmo $A$ sia su $G$ che su $G'$, con la stessa sequenza di ritardi.

In $G$, i nodi $x,y$ non si sono mai scambiati il messaggio, questa cosa succederà anche su $G'$, e di conseguenza il nodo $z$ rimarrà nello stato SLEEPING

Così facendo, vediamo che la [tesi](#^tesi) non è valida, quindi $\Omega(m)$ per forza $\blacksquare$

---
# Labeled Hypercube

Spostiamoci sull'architettura **Labeled Hypercube** $\mathcal H$

Gli Hypercube sono un tipo di architettura parallela che offre un perfetto compromesso tra $deg(G)$ e $Diam(G)$

Ogni arco di $\mathcal H$ è etichettato dalla dimensione del bit per il quale il nome dei nodi differisce

Negli Hypercube si ha che $$Diam(\mathcal H)=deg(\mathcal H)=\Theta(\log(n))$$
Negli Hypercube di dimensione $d$ abbiamo che $|V|=2^d$

Per costruire un Hypercube di dimensione $d+1$ procediamo in questo modo :
1. prendiamo 2 copie di $\mathcal H$ di dimensione $d$ e le mettiamo parallele (una sopra l'altra)
2. L'etichetta dei nodi seguirà la sequente distribuzione : 
	1. Nella copia di sopra aggiungiamo il bit più significativo a $0$
	2. Nella copia di sotto aggiungiamo il bit più significativo a $1$
	3. Otteniamo quindi un quadrato 
3. Aggiungiamo quindi le etichette sugli archi
	1. L'etichetta è il bit che cambia quando passo da un nodo ad un altro. Ad es.$$00\to10$$cambia il primo bit da dx, quindi l'arco $(00,01)$ avrà etichetta 1
	2. $00\to10$ cambia il secondo bit da dx, quindi $(00,10)$ avrà etiochetta 2
	3. e così via

