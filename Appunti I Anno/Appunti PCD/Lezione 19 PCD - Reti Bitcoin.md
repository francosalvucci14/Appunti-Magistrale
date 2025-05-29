# La rete P2P di Bitcoin

La rete P2P di Bitcoin è sconosciuta *by design*: i nodi *raggiungibili* della rete sono noti, ma se fra due nodi $u$ e $v$ esiste o meno un arco è noto solo ai nodi $u$ e $v$. 

Cercare di capire se sia possibile progettare delle tecniche che rivelino la topologia della rete P2P di Bitcoin è un’area di ricerca attualmente attiva.

Al contrario della rete P2P di Bitcoin, la rete dei canali Lightning è **nota**. 
Ogni nodo è identificato da una chiave pubblica; i canali (gli archi) devono essere noti affinchè un nodo $u$, che debba effettuare un pagamento a un nodo $v$, possa cercare un cammino da $u$ a $v$ lungo il quale instradare il pagamento. 

Si osservi che la rete dei canali Lightning è in realtà un multigrafo, perchè fra due nodi $u$ e $v$ potrebbe esserci più di un arco.

Per un maggiore approfondimento sul discorso *Onion Routing* vedere [BOLT 4](https://github.com/lightning/bolts/blob/master/04-onion-routing.md)
