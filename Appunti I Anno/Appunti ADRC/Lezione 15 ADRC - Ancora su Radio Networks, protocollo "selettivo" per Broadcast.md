# Continuo protocollo Round Robin

## Non-Conoscenza di $|V|$ 

Fin'ora abbiamo assunto che i nodi conoscessero una buona approssimazione di $|V|=n$, ma cosa succede se i nodi non conoscono $n$?

Devono in qualche modo "indovinarlo", sfruttando l'idea della **Ricerca Binaria**, e poi simulare il protocollo $RR$ usando il valore "indovinato".

Adremo quindi a incrementare il valore di $n$ in maniera *esponenziale*

Vediamo allora come funziona questo nuovo protocollo, chiamato **GEN-RR(L)**

**GEN-RR(L):**
For $L=2,3,\dots$ DO
- For $T=1,2,...,2^L$:
	- Ogni nodo $i$ fa:
		- if $i\equiv T\space(\text{mod }2^L)\land\text{status=INFORMED}$
			- Trasmette e imposta il suo status a DONE (Do Nothing)

Analizziamo il seguente protocollo : 
Sia $l=\min\{L:2^L\geq n\}$, allora $$TIME(GEN-RR(l))=2^l\cdot D$$
Di conseguenza, avremo che 
$$TIME(GEN-RR(n))=\sum\limits_{l=1}^{\lceil\log(n)\rceil}2^{l}D=D\sum\limits_{l=1}^{\lceil\log(n)\rceil}\leq\ D\sum\limits_{l=1}^{\lceil\log(n)\rceil}n=(Dn)\log(n)$$
Anche qui, $D$ potrà essere al più $n-1$, quindi la complessità temporale del protocollo **GEN-RR(n)** sarà $O(((n-1)n)\log(n))=O(n^2\log(n))$ 

# Protocollo "selettivo"

Vediamo ora un'altro protocollo per il problema del Broadcast, che sfrutta un'osservazione fondamentale.

**oss** : il protocollo RR non *sfrutta per niente* il parallelismo 

Vediamo quindi il metodo "selettivo"

>[!definition]- Definizione (Famiglia (n,k)-selettiva)
>Dato $[n]\in\{1,2,\dots,n-1\}$ e $k\leq n$, una famiglia di sottoinsiemi $$\mathcal H=\{H_1,H_2,\dots,H_t\}$$è detta $(n,k)-$selettiva se $$\forall S\subseteq[n]:|S|\leq k\implies\exists H\in\mathcal H:|S\cap H|=1$$

Una famiglia $(n,k)-$selettiva banale è la famiglia composta da tutti **singleton**, ovvero sottoinsieme composti da un singolo elemento, come segue :
$$\mathcal H=\{\{1\},\{2\},\dots,\{n\}\}$$
Detto questo, come può una famiglia selettiva essere usata per il problema del Broadcast?

Mettiamoci nella restrizione che tutti i nodi conoscono $n$ e $d$, allora : 

**set-up** : tutti i nodi conoscono la stessa famiglia $(n,d)-$selettiva $\mathcal H=\{H_1,H_2,\dots,H_i,\dots,H_t\}$ dove $d=\text{massimo grado(G)}$ 
Il protocollo sarà il seguente : 

**protocollo SELECT1**
- Lavora in fasi consecutive $J=1,2,\dots$ (come RR)
- Al time slot $i$ di ogni fase, ogni **nodo informato** $\in H_i$ trasmette il messaggio

Analizziamo il protocollo, vale il seguente lemma

**Lemma 1** : Dopo la fase $j$, tutti i nodi a distanza al più $j$ saranno informati

**dim** : per induzione su $j$
- *Caso base* : $j=0$ solo la sorgente sarà informata (come RR) e di conseguenza sarà l'unica a trasmettere
- *Caso induttivo* : Consideriamo un nodo $y$ a distanza $j$. Consideriamo il sottoinsieme $$N(y)=\{z\in V:\text{z è vicino di y}\land\text{z si trova a distanza j-1}\}$$Dato che $N(y)\subseteq[n]$ e $|N(y)|\leq n$, se applichiamo la $(n,d)-$selettività otteniamo la tesi
	- Infatti, $\forall v\in L_j\implies|N(v)\cap L_{j-1}|\leq V$ 

Ma è corretto questo protocollo? La risposta è **NO**

Infatti non stiamo considerando l'impatto dei nodi $z$ **informati** nel livello $j$ durante la fase $j$
Valgono infatti due casistiche : 
1) se poniamo $z\in N(y),z$ potrebbe essere selezionato ma non ancora informato
2) se non poniamo $z\in N(y),z$ potrebbe essere informato e creare **collisioni**

Come possiamo sistemare la situazione? Usando una *semplice* modifica

"Solo i nodi che sono stati informati DURANTE la fase $j-1$ saranno nello stato ACTIVE durante la fase $j$"

Adesso, il lemma1 è vero, quindi dopo $D$ fasi tutti i livelli $L_0,\dots,L_D$ saranno informati

Quindi, il **tempo di completamento** del protocollo SELECT1 è pari a $O(D\cdot|\mathcal H|)$, dato che ogni fase impiega tempo $|\mathcal H|$.

Ci serve quindi una famiglia selettiva ***min-size***. Vale quindi il seguente teorema, di cui non faremo la dimostrazione : 

>[!teorem]- Teorema (ClementiMontiSilvestri)
>Per un $n$ e $k\leq n$ sufficientemente grandi : $$\exists\mathcal H=\{H_1,H_2,\dots,H_t\}:\mathcal H\text{ è (n,k)-selettiva}\land|\mathcal H|=\Theta(k\log(n))\lt\lt n\log(n)$$ed è ottimale

Quindi, se mettiamo questa famiglia selettiva all'interno del protocollo otteniamo che $$\text{COMPL-TIME(SELECT1)}=O(D\cdot d\log(n))$$
Quindi se $D$ e $d$ sono entrambi **piccoli**, abbiamo un tempo di completamento **molto migliore** del RR

