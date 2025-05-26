# Protocollo PULL su $\Delta$-regular Expanders

Consideriamo il seguente protocollo di comunicazione sparso su un grafo $\Delta$-regular, con $\Delta=O(1)$, partendo da una sorgente fissata $s\in V$ avente un pezzo dell'informazione $M$
Il goal è quello di far si che tutti i nodi di $G$ siano informati su $M$

**Protocollo Randomizzato PULL(G(V,E);s)**

- Fase $0$ (Wake-Up) : Il nodo informato è solo $s$, mentre tutti gli atrli sono in stato ACTIVE
- Fase $1$ : Ogni nodo $v$ in stato ACTIVE sceglie u.a.r uno dei suoi vicini $w\in N(v)$
	- Allora, se $w$ è nello stato INFORMED, il nodo $u$ fa il PULL del messaggio e si mette nello stato INFORMED
	- I nodi nello stato INFORMED non fanno nulla

Vale quindi il seguente teorema : 

>[!teorem]- Teorema 5.1
>Sia $G(V,E)$ un grafo $\Delta$-regolare con espansione $\alpha$, dove $\alpha$ è una costante positiva. 
>Allora, partendo da ogni sorgente $s$, il protocollo PULL$(G(V,E),s)$ informa tutti i nodi di $G$ entro $O(\log(n))$ tempo w.h.p

**dim**
Per semplicità, eseguiremo solo l'analisi in aspettazione.

Definiamo le v.a $$I_0=\{s\},\quad I_{t}=\{v\in V:\text{v è INFORMED in un qualche round }t'\leq t\}$$
Il nostro prossimo obiettivo è dimostrare che la dimensione attesa di $I_t$ aumenta **esponenzialmente** con $t \to\infty$. 
Per farlo sfruttiamo **l'espansione** di $I_t$ e la ***casualità*** del protocollo PULL. 

In dettaglio, si fissi un qualsiasi $t \geq 1$ e si consideri il sottoinsieme di nodi nella frontiera di $I_t$
cioè $$N(I_{t})=\{v\in V\setminus I_{t}:\text{v è connesso a qualche nodo in }I_t\}$$
![[Pasted image 20250526111241.png|center|500]]

Definiamo inoltre la v.a $$\forall v\in N(I_{t}),\space Y_{v}=1\iff\text{v sarà informato al round t+1}$$
Allora, per ogni $v\in N(I_t)$, vale che $$Pr(Y_v=1)=\frac{|N(v)\cap I_t|}{\Delta}\geq\frac{1}{\Delta}$$
D'altra parte, possiamo fornire un **lower bound** al numero di ndoi in $N(I_t)$ usando le proprietà di espansione del grafo $G$.

Infatti, fintanto che $|I_t|\lt\frac{n}{2}$ sappiamo che $$|N(I_t)|\geq\alpha|I_t|$$
Usando le ultime due disuguaglianze, possiamo dare un lower bound al **numero atteso di nuovi nodi informati al round** $t+1$, come segue : $$\mathbb E[|I_{t+1}|]=|I_{t}|+\sum\limits_{v\in N(I_{t})}Y_{v}\geq|I_{t}|+\alpha|I_{t}|\frac{1}{\Delta}\geq\left(1+\frac{\alpha}{\Delta}\right)|I_{t}|\geq(1+\Omega(1))|I_{t}|$$La disuguaglianza di cui sopra mostra che, fintanto che $|I_t|\lt\frac{n}{2}$, la sua dimensione **ATTESA** incrementa di un fattore costante, dato che $G$ è $\Delta$-regular con $\Delta=O(1)$

Quindi, dopo $O(\log(n))$ rounds, almeno $\frac{n}{2}$ nodi saranno informati, in **media**

Per concluedere al $100\%$ la dimostrazione, dovremmo dimostrare che il numero di nodi informati passa da $\frac{n}{2}$ a $n$ in un numero logaritmico di round, ma questa parte viene omessa. $\blacksquare$

---
# Majority Consensus via the $3$-Majority Dynamics

Il problema di trovare un *agreement* tra i nodi di una rete distribuita è uno dei problemi più importanti nei sistemi distribuiti moderni.

Qui studieremo questo problema, noto con il nome di **Majority Consensus Problem**, e vedremo un protocollo per tale problema, chiamato $k$-MAJ


## Unbalanced $2$-coloring with $3$-MAJ
