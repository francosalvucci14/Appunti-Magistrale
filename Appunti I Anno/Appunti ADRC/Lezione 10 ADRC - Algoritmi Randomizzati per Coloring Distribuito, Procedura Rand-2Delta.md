
# Primo algoritmo randomizzato per CD
## Phase Technique

Il paradigma della **Basic Phase Technique**

While $V\neq\emptyset$ do : (**Ogni esecuzione è una fase**)
1. Ogni nodo sopravvisuto $v$ esegue in parallelo :
	1. Sceglie u.a.r un colore $C(v)$ da un qualunque insieme $Z$ e informa tutto il suo vicinato $N(v)$
	2. In base al colore ricevuto dal suo vicinato, $C(N(v))$, imposta 
		1. (i) $C(v)$ come "sbagliato"
		2. (ii) $C(v)$ come "okay"
2. Se succede (i), $v$ **sopravvive** e continua a cercare il suo colore nella prossima fase
3. Se succede (ii), $v$ **ottiene** il suo colore finale $C(v)$, informa $N(v)$ e viene rimosso da $G$, ottenendo così un nuovo grafo $G'(V',E')$, con $$\begin{align}&V'=V\setminus\{v\}\\&E'=E\setminus\{(u,v)\in E,v\in V\}\end{align}$$
Dopo aver definito la Phase Technique, passiamo a definire il protocollo che sfrutterà questa tecnica, chiamato Rand-$2\Delta$
## Protocollo Rand-2Delta

![[Pasted image 20250418153134.png|center]]

**Fatto 1** : Se *tutti* i nodi terminano (es. $V=0$), allora la procedura Rand-$2\Delta$ calcola un (legale) $(2\Delta)$-coloramento per il grafo $G$

**dim** :
Dagli Step $6-10$, quando $v$ ottiene il suo colore finale $C(v)$ allora è considerato sicuro.
Tutti i suoi vicini sono o non ancora $F$-colorati, oppure sono colorati con altri colori. 
Questo perchè $C(v)$ è sempre scelto nell'insieme $[2\Delta]\setminus(F_v\cup T_v)$ 

### Rand-2Delta : Analisi

**Fatto 2** : Dopo $O(\log(n))$ Fasi, con alta probabilità *tutti* i nodi termineranno.

**dim**

Fissiamo un nodo $v\in V$ e una fase $t\gt0$

Abbiamo che $|F_v\cup T_v|\leq\Delta$, in quanto ogni vicino del nodo $v$ contribuisce con al più un colore a tale insieme, e il grafo $G$ è $\Delta$-regolare (cioè $|N(v)|=\Delta$)

Di conseguenza, abbiamo che 
$$Pr[\text{v termina alla fase t|v non è terminato prima}]\geq\frac{2\Delta\setminus(F_v\cup T_v)}{2\Delta}=\frac{1}{2}$$
Applicando la regola della catena (non importa il passato: si ha sempre il $50\%$ di chance), vale che 
$$Pr[\mathcal E_{v}=\text{v non termina dopo t Fasi}]\leq\left(\frac{1}{2}\right)^t$$
A questo punto, usando lo **Union Bound** su tutti gli $n$ eventi "cattivi" $\mathcal E_v$, otteniamo che : $$Pr[\mathcal E=\exists v\in V : \text{ v non termina dopo t Fasi}]\leq n\left(\frac{1}{2}\right)^t$$
Quindi, per $t\geq(c+1)\log(n)$ abbiamo che $$Pr[\mathcal E]\leq \frac{1}{n^{c-1}}\implies Pr[\hat{\mathcal E}]=1-Pr[\mathcal E]\leq1-\frac{1}{n^c}$$
E quindi abbiamo trovato che, con alta probabilità, ogni nodo termina entro $O(\log(n))$ rounds


