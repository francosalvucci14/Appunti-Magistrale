# Un'altro algoritmo randomizzato per CD

Nella lezione scorsa avevamo introdotto un primo algoritmo randomizzato per il problema del Coloring Distribuito, ottenendo un $(2\Delta)$-coloramento.

Ora vediamo il secondo algoritmo distribuito, che da $2\Delta$ ci farà raggiungere il $(\Delta+1)$-coloramento.
## Procedura Rand-Delta+

In questa procedura facciamo due **cambiamenti chiave**

In ogni fase : 
1. Ogni nodo sopravvisuto $v$ prima sceglie u.a.r un bit $c(v)\in\{0,1\}$
	1. Se $c(v)=0$ allora $v$ viene ***sconfitto*** e salta alla prossima fase
	2. Altrimenti, il nodo $v$ sceglie un colore $C(v)$ u.a.r dalla palette $[\Delta+1]\setminus F_v$

A questo punto, il protocollo procede come Rand-$2\Delta$

![[Pasted image 20250418160753.png|center]]

**Fatto 3** : Se *tutti* i nodi terminano (es. $V=0$) , allora il protocollo Rand-$\Delta^+$ calcola un (legale) $(\Delta+1)$-coloramento per il grafo $G$

**dim** : identica a quella per il protocollo Rand-$2\Delta$

### Rand-Delta+ : Analisi

**Fatto 4** : **Dopo** $O(\log(n))$ fasi, con alta probabilità, *tutti* i nodi terminano

**dim** : 

Fissiamo $v$ e una fase $t$

Per un $u\in N(v)$ fissato, abbiamo che $$Pr[c(u)=c(v)]\leq\frac{1}{2(\Delta+1\setminus|F_v|)}\quad (1)$$
Usando lo Union Bound su ***tutti i vicini sopravvisuti*** $u\in N(v)$ ***che hanno scelto*** $b=1$, dall'equazione $(1)$ si ha che $$Pr[\mathcal E_{v}=\exists u\in N(v):c(u)=c(v)]\leq\frac{\overbracket{(\Delta+1\setminus|F_v|)}^{\text{num. vicini attivi di v}}}{2(\Delta+1\setminus|F_v|)}\leq\frac{1}{2}\quad (2)$$
Quindi, si ha che $$Pr[c(v)\gt0\land\lnot\mathcal E_v]\geq\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}$$
Da qui in poi, si prosegue come la dimostrazione del Fatto 2

---

# Random Leader Election

Spostiamoci dal problema del Coloring Distribuito, e torniamo per un secondo al vecchio problema della Leader Election.

Ricordando che nella Leader Election avevamo mostrato che, senza l'assuzione di Unique Identifier, era impossibile risolvere problema in modo ***deterministico***

Qui studiamo un'approccio probabilistico che risolve il problema della Leader Election, nella situazione in cui tutti i nodi sono **anonimi**

## RLE in Grafi non etichettati

---
# Maximal Indipendent Set Distribuito

