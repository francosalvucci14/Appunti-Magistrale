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

Gli $n-f$ nodi *onesti* applicheranno il nostro protocollo. Gli $f$ nodi *corrotti* non sappiamo come si potrebbero comportare: il *worst-case* è che tutti i nodi corrotti si coalizzeranno per far fallire il nostro protocollo.
Non sappiamo chi sono i nodi corotti.

Facciamo un paio di assunzioni

> Assunzione (1)

Ci troviamo in un sistema *sincrono* :
- C'è un ***global clock*** noto a tutti i nodi che scandisce il tempo in *round* discreti : $0,1,\dots$
- Ogni messaggio inviato in un round $t$ arriva a destinazione prima dell'inizio del round $t+1$

> Assunzione (2)

Esiste un setup particolare, chiamato ***Public Key Infrastructure (PKI)***
- Ogni nodo $i$ ha una coppia di chiavi $(sk_i,pk_i)$, dove $sk_i=$ chiave segreta, $pk_i=$ chiave pubblica
- L'insieme delle chiavi pubbliche $\{pk_i:i\in[n]\}$ è noto a tutti i nodi a priori
- Dato un messaggio $m$, indichiamo con $\langle m_i\rangle$ il messaggio $m$ con l'aggiunta di una firma valida eseguita con la chiave segreta $sk_i$

**Esempio/Esercizio** 
Vedi algoritmo Tentativo 1 fino a ROUND 2, lui soddisfa validity ma non consistency.
Questo perchè, se la sorgente dovesse essere un nodo corrotto, allora la sorgente invierebbe a tutti i nodi bit errati, e di conseguenza non si rispetterebbe la condizione di consistency