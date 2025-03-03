# Introduzione al corso

Corso diviso in 3 fasi : 

1. **Problemi Classici di Consenso** (Anni 80')
2. **Bitcoin** (2008-)
3. **Soluzioni Layer-2**
	1. Lightnining Network

Esame : Presentazione su paper + progetto python su Bitcoin + orale 
- Orale sicuro, poi a scelta tra presentazione e/o progetto

--- 

# Parte 1 : Problemi Classici di Consenso

## Byzantine Broadcast Problem (BB)

Ci troviamo in un sistema distribuito : 
- $n$ nodi $[n]=\{1,2,\dots,n\}$
- Ogni nodo esegue computazioni locali e comunicazioni arbitrarie con altri nodi

Il problema $BB$ è il seguente :
- Degli $n$ nodi, ce ne sono $0\leq f\leq n$ che sono ***corrotti***.
- Al nodo sorgente (il nodo 1) viene affidato un messaggio (un bit) $b\in\{0,1\}$
- Vogliamo progettare un *protocollo* al termine del quale ogni nodo *onesto* $i$ dia in output un bit $y_i\in\{0,1\}$, tale che : 
	1. **Validity** : Se la sorgente è un nodo onesto, allora $y_i=b,\forall i$ onesto
	2. **Consistency** : Se $i,j$ sono onesti, allora $y_i=y_j$

