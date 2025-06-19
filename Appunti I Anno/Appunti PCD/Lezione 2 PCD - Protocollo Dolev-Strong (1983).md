# Protocollo DS per BB

Nella prima lezione abbiamo affrontato il problema Bynzatine Broadcast.

In questa lezione vedremo un protocollo che risolve BB soddisfando le assunzioni Validity e Consistency

Il protocollo in questione è **Dolev-Strong**, e funziona così : 

**ROUND 0**
- Sorgente "1" riceve bit $b\in\{0,1\}$
- Ogni nodo $i$ inizializza un insieme, detto $\mathcal E_i=\emptyset$
- La sorgente invia a tutti i nodi il messaggio $\langle b\rangle_1$

**FOR ROUND** $r=1,\dots,f$:
- Ogni nodo $i$ : 
	- Se nel round $r-1$ ha ricevuto $\langle \hat{b}\rangle_{1,j_1,j_2,\dots,j_{r-1}}$ (con $r$ firme distinte, inclusa quella della sorgente)
		- Se $\hat{b}\not\in\mathcal E_i$:
			- Aggiungi $\hat{b}$ in $\mathcal E_i$
			- Spedisci a tutti $\langle \hat{b}\rangle_{1,j_1,j_2,\dots,j_{r-1},i}$

**AL ROUND** $f+1$
- Ogni nodo $i$:
	- Se nel round $f$ ha ricevuto $\langle \hat{b}\rangle_{1,j_1,j_2,\dots,j_{f}}$ ($f+1$ firme distinte, inclusa la sorgente)
		- Se $\hat{b}\not\in\mathcal E_i$:
			- Aggiungi $\hat{b}$ in $\mathcal E_i$
		- Se $\mathcal E_i$ contiene un solo bit $\hat{b}\in\{0,1\}$:
			- $y_i=\hat{b}$
		- Altrimenti :
			- $y_i=0$

Andiamo ora a fare l'analisi di questo protocollo, e vediamo se effetivamente è corretto oppure no

## Analisi protocollo DS

>[!warning]- Osservazione
>Le firme che vedremo sui messaggi sono **firme digitali**, che dipendono dal messaggio stesso.
>Esse non sono falsificabili in nessun modo.


>Validity

Se la sorgente è onesta, allora "1" invia $\langle b\rangle_1$, e quindi, al round 1 avremo che $\mathcal E_i=\{b\}$. Validity OK

>Consistency

Per dimostrare che anche consistency viene rispettata, dobbiamo dimostrare due lemmi

**Lemma 1**
Se $i$ è un nodo onesto e $\hat{b}\in\mathcal E_i$ a un round $r\leq f$ allora, $\forall$ nodo onesto $j$ avremo che $\hat{b}\in\mathcal E_j$ al round $r+1$

***dimostrazione lemma 1***

Supponiamo che $\hat{b}\in\mathcal E_i$ al round $r$ e nodo $i$ onesto.
Sia $t\leq r$ il round in cui il nodo $i$ ha inserito $\hat{b}\in\mathcal E_i$.

Allora : 
Il nodo $i$ ha ricevuto $\hat{b}$ nel round $t-1$, con $t$ firme valide $$\langle\hat{b}\rangle_{1,j_1,j_2,\dots,j_{t-1}}$$
Quindi, nel round $t$, il nodo $i$ ha inviato a tutti $\langle\hat{b}\rangle_{1,j_1,j_2,\dots,j_{t-1},i}$

Di conseguenza, ogni nodo onesto $j$, se non aveva già $\hat{b}$ in $\mathcal E_j$ al round $t+1$, lo inserisce in quel round. $\square$ 

Vediamo ora il Lemma 2

**Lemma 2**
Se un nodo onesto $i$ ha un bit $\hat{b}$ nel suo insieme $\mathcal E_i$ al round $f+1\implies$ ogni nodo onesto $j$ ha $\hat{b}$ in $\mathcal E_j$ al round $f+1$

***dimostrazione lemma 2***

Sia $i$ un nodo onesto che ha $\hat{b}$ in $\mathcal E_i$ al round $f+1$.
Si identificano due casistiche :
- **Caso (1)** :
	- Se $i$ ha inserito $\hat{b}$ in $\mathcal E_i$ in uno dei round precedenti, il lemma 1 implica che tutti i nodi onesti hanno $\hat{b}$ nel loro insieme $\mathcal E$ al round $f+1$
- **Caso (2)** :
	- Se $i$ ha inserito $\hat{b}$ in $\mathcal E_i$ nel round $f+1$, allora nel round $f$ deve essergli arrivato per forza $\langle \hat{b}\rangle_{1,j_1,j_2,\dots,j_{f}}$ con $f+1$ firme valide
	- Una di queste firme deve essere er forza di un nodo onesto.
	- Questo nodo onesto deve aver ricevuto $\hat{b}$ in un round precedente $t\lt f+1$. 
	- Allora : 
		- Tutti i nodi onesti, per il lemma 1 devono aver ricevuto $\hat{b}$ al round $t+1$
- $\square$

Diamo ora il teorema generale :

>[!teorem]- Teorema protocollo DS
>Il protocollo Dolev-Strong funziona correttamente fintanto che il numero di nodi corrotti $f\leq n-2$
>(Importante, devono esserci almeno $2$ nodi onesti, altrimenti perde di significato la condizione di consistency)

**oss**
Da notare che abbiamo usato le assunzioni PKI e Sincronia.

