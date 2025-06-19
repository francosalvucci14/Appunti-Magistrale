# Protocollo "randomizzato" con BB 

Ci troviamo ancora senza l'assunzione PKI 

Nella lezione scorsa avevamo visto (e dimostrato) che non esiste un protocollo che rispetta validity e consistency per il problema BB, se il numero di nodi corrotti $f\geq\frac{n}{3}$

In realtà esistono ben due protocolli per BB, se il numero di nodi corrotti è $\lt\frac{n}{3}$. Vediamo il primo.

Prima diamo la definizione di **Random Oracle Model**

>[!definition]- Random Oracle Model
>È una funzione hash $$H:\{0,1\}^{*}\to\{0,1\}^{b}$$ che dato un input $x$, ritorna $H(x)$ scelto u.a.r su $\{0,1\}^b$
>Questa funzione è valida solo teoricamente, nella pratica si usano funzioni hash crittografiche

Il protocollo è il seguente :

ROUND 0:
- Sorgente "1" riceve $b\in\{0,1\}$
- Inizializza $sb_1=b$, dove $sb$ è lo sticky-bit
- Ogni nodo $i$ inizialliza $sb_i=\bot$ , dove $\bot$ sta per neutro
Per ogni $r=0,\dots,k-1$:
- ROUND $3r$:
	- Il leader $l_r=H(r)$:
		- Se $sb_{l_r}\neq\bot$ allora invia $sb_{l_r}$ a tutti i nodi
		- Altrimenti sceglie $\hat{b}\in\{0,1\}$ u.a.r e lo invia a tutti i nodi
- ROUND $3r+1$:
	- Ogni nodo $i$:
		- Se $sb_{i}\neq\bot$ allora invia a tutti $sb_i$
		- Altrimenti invia a tutti il bit $\hat{b}$ ricevuto dal leader $l_r$ al round $3r$
		- (se non ha ricevuto niente o entrambi i bit invia $0$ o $1$ arbitrariamente)
- ROUND $3r+2$:
	- Ogni nodo $i$:
		- Se c'è un bit $\hat{b}$ che ha ricevuto, nel round $3r+1$, "voti" da almeno $\frac{2n}{3}$ noti distinti, allora :
			- imposta $sb_i=\hat{b}$
		- altrimenti
			- imposta $sb_i=\bot$

END FOR
ROUND $3k$:
- Ogni nodo $i$ ritorna in output $sb_i$

Ora, per dimostrare la correttezza di tale protocollo, diamo l'enunciato di $4$ lemmi.

>[!teorem]- Lemma 1
>Alla fine di ogni iterazione non possono esserci $2$ nodi onesti $i$ e $j$ tale che $i$ ah ricevuto $\leq\frac{2n}{3}$ voti per $0$ e $j$ ha ricevuto $\leq\frac{2n}{3}$ voti per $1$

**Dimostrazione lemma 1**

Sia $S_i$=insieme dei nodi che hanno inviato $0$ a $i$
Sia $S_j=$ insieme dei nodi che hanno inviato $1$ a $j$

Sappiamo che $$n\geq|S_i\cup S_j|=\underbrace{=}_{\text{I.-E.}}|S_i|+|S_j|-|S_{i}\cap S_j|\leq\frac{4n}{3}-|S_{i}\cap S_j|\implies|S_{i}\cap S_j|\geq\frac{n}{3}$$ e questo è **assurdo** $\blacksquare$

Ora, prima di passare al secondo Lemma, diamo un'importante definizione.

>[!definition]- Iterazione Fortunata
>Un iterazione si dice **fortunata** se:
>1. il leader $l_r$ è onesto
>2. il bit $\hat{b}$ che sceglie di inviare il leader è lo stesso bit che hanno memorizzato nel loro $sb$ i nodi onesti

>[!teorem]- Lemma 2
>Se $r\leq k-1$ è un iterazione fortunata allora tutti i nodi onesti danno in output lo stesso bit al round $3k$

>[!teorem]- Lemma 3
>FIssata un iterazione $r\leq k-1$, la probabilità che $r$ sia fortunata, qualunque cosa sia successa nelle iterazioni precedenti, è $\geq\frac{1}{3}$

**dimostrazione lemma 3**

Abbiamo che $$\begin{align}&1.\space \mathbb P(l_r\text{ onesto})\geq\frac{2}{3}\\&2.\space\mathbb P(cond\space(2))\geq\frac{1}{2}\\&3.\space\mathbb P((1),(2))\geq\frac{1}{3}\end{align}$$
>[!teorem]- Lemma 4
>La probabilità che ci sia almeno una iterazione lucky nelle $k$ iterazioni è $\geq1-\left(\frac{2}{3}\right)^k$

**dimostrazione lemma 4**

Sia $E_r$ l'evento "iterazione $r$ è fortunata" $\implies\mathbb P(E_r)\geq\frac{1}{3}$

Siano $\bigcup_{r=1}^{k-1}E_r$ gli eventi che, uniti, formano l'evento "almeno 1 iterazione è fortunata"

Di conseguenza, $\bigcap_{r=1}^{k-1}E_r^c$ formano l'evento "nessuna iterazione è fortunata"

Quindi $$\mathbb P\left[\bigcap_{r=1}^{k-1}E_r^{c}\right]=\mathbb P\left[E_{k-1}^c|\bigcap_{r=1}^{k-2}E_r^{c}\right]\mathbb P\left[\bigcap_{r=1}^{k-2}E_r^{c}\right]\leq\dots\leq\left(\frac{2}{3}\right)^k$$
E di conseguenza $$\mathbb P\left[\bigcup_{r=1}^{k-1}E_r\right]=1-\mathbb P\left[\bigcap_{r=1}^{k-1}E_r^c\right]=1-\left(\frac{2}{3}\right)^k\quad\blacksquare$$
Quindi, dopo aver enunciato e dimostrato vari lemmi, siamo pronti per dare l'enunciato e la dimostrazione del teorema principale : 

>[!teorem]- Teorema
>Se il numero di nodi corrotti è $f \lt \frac{n}{3}$ allora il protocollo in questione soddisfa Validity con probabilità $1$ e Consistency con probabilità almeno $1-\left(\frac{2}{3}\right)^k$.

**dimostrazione teorema**

Per *Validty* osservare che, se la sorgente è onesta, nell’ iterazione $r = 0$ succede questo: 
- Nel Round $0$ tutti i nodi onesti ricevono dalla sorgente il bit $b$ (linea 7)
- Nel Round $1$ ogni nodo onesto invia $b$ a tutti (linea 12)
- Nel Round $2$ ogni nodo onesto riceve $b$ da almeno $\frac{2n}{3}$ nodi e quindi fissa il suo $sb_i = b$.
- Nelle iterazioni successive $r = 1,\dots , k − 1$ ogni nodo onesto $i$ continua a inviare $sb_i = b$ (linea 11) e quindi il valore di $sb_i$ rimane $b$ (linea 15). 

Per *Consistency* la dimostrazione procede seguendo i vari lemmi definiti sopra.



