Struttura dati per preprocessing similarità temporali con J.Sim (e simili) e Range Tree

Struttura dati preprocessing del nodo, per ogni snapshot temporale, fa sketch di similarità nei vicini allo snapshot i-esimo

Poi rispondere a query diverse

Alcune idee di downtime problems (?) :
- Temporal Degree Centrality
- asd

Metriche per SD:
- size
- quiry time
- building time

---

Idea 1: Usare Range Tree o sua variante

Ogni foglia identifica un timestamp $t_{i}$, e contiene lo sketch del vicinato del nodo a tempo $t_i$
Ogni nodo interno è semplicemente il merge dei due sketch, e quello identificherà lo sketch del vicinato da tempo $t_i\to t_j,i\neq j$ 

Esempio:
- nodo $u$ ha vicini ${a,b,c}$
- vale che:
	- a tempo $1$: ${(u,a),(u,b)}$
	- a tempo $2$: ${(u,a),(u,c)}$
	- a tempo $3$: ${(u,a),(u,b),(u,c)}$

Avrè albero con $3$ foglie:
- folgia $1$ rapp. timestamp $1$ e contiene sketch di ${(u,a),(u,b)}$
- foglia 2 rapp. timestamp $2$ e contiene sketch di ${(u,a),(u,c)}$
- foglia 3 rapp. timestamp $3$ e contiene sketch di ${(u,a),(u,b),(u,c)}$

Nodo interno $1$ conterrà il merge degli sketch di foglia 1 e foglia 2
Radice conterrà il merge degli sketch di Nodo interno $1$ e foglia 3

