# Deterministic Distribuited Graph Coloring

In questa sezione, studieremo vari metodi per risolvere il problema del coloramento su sistemi distribuiti.

Più nello specifico, vogliamo cercare di ottenere una colorazione del sistema come se stessimo risolvendo il problema COL su grafi centralizzati.

Prima di vedere le due procedure fondamentali, diamo la definizione formale del problema.

**Problema Distribuited Coloring (DCP)**
- Modello del sistema
	- Il sistema distribuito è formalizzato come un grafo etichettato $G(V,E,Id)$, con $\Delta$ il grado max. del grafo $G$
	- Ci mettiamo nel modello *LOCAL*, sotto le assunzioni Standard, e con l'utilizzo di un clock globale che scandisce il tempo in round sincroni $t=1,2,\dots$ (notiamo quindi che stiamo nel sistema **sincrono** e non più asincrono)
- Definizione del problema DCP
	- **Configurazione iniziale** : un coloramento (iniziale) *legale* $C:V\to[n]$ t. c. $C:=ID$, dove ogni nodo $v$ conosce il suo coloramento $C(v)$  
	- **Configurazione finale** : un coloramento legale $\hat{C}:V\to[\Delta+1]$, dove ogni nodo $v$ conosce il suo coloramento finale $\hat{C}$

Ricordiamo che per coloramento legale intendiamo un coloramento dove $$\forall x,y\in V,(x,y)\in E|C(x)\neq C(y)$$
>[!teorem]- Teorema
>Ogni grafo $G(V,E)$ con grado massimo $\Delta$ **ammette un coloramento legale** che usa al più $\Delta+1$ colori

Il nostro goal è quindi quello di trovare un $(\Delta+1)$-coloramento nel modo distribuito.

>[!info]- Remark + Oss
>Piccolo remark sul coloramento, si ha che $3-COL\in NPC$ 
>Osservazione : Non è detto che il $(\Delta+1)-COL$ sia quello ottimale, infatti possono esserci topologie di sistema distributo tale che il coloramento ottimale sia ad es. il $2-COL$

Vediamo ora la prima procedura per questo problema
## The Basic Color Reduction Procedure (BCP)

**BCP Task su G** : 
- **Configurazione iniziale** : un coloramento (iniziale) $C:V\to[a]$ t. c. $a\gt\Delta+1$, dove ogni nodo $v$ conosce il suo coloramento $C(v)$  
- **Configurazione finale** : un $(\Delta+1)$-coloramento $\hat{C}:V\to[\Delta+1]$, dove ogni nodo $v$ conosce il suo coloramento finale $\hat{C}$

La procedura è la seguente : 
- for each $k=a,a-1,\dots,\Delta+2$ do (in modo sequenziale)
	- each node $v$ do in parallelo
		- $v$ invia il suo colore $C(v)$ a tutto $N(v)$ ; $v$ riceve da tutti i suoi vicini i colori da loro usati $C(N(v))$
		- $(**)$ If $C(v)=k$ then
			- $v$ sceglie un qualunque $\underbrace{\hat{j}\in[k-1]-N(C(v))}_{\text{Esiste sempre per (*)}}$ e imposta $C(v)=\hat{j}$ (sostanzialmente sceglie un nuovo colore dalla tavolozza di colori disponibili, togliendo però i colori usati dal suo vicinato)
	- Ogni nodo $v$ imposta il suo colore finale $\hat{C}(v)=C(v)$ e si ferma

$(*)$ : questo vale perchè $k\geq\Delta+2\land deg(v)\leq\Delta$
### BCP : Analisi I (Correttezza)

- **Fatto 1** : Ad ogni fase $k$, per ogni nodo $v$, il colore $\hat{j}$ esiste sempre. 
- **Fatto 2** : Alla fine di ogni fase $k\gt\Delta+1$, il coloramento $C:V\to[a-k]$ è legale
- **Corollario** : BCP ritorna un $(\Delta+1)$-coloramento $\hat{C}:V\to[\Delta+1]$ legale.

Dimostriamo : 

Il fatto $1$ è trivia, il fatto $2$ è conseguenza del fatto che i nodi con colore $k$ non sono ***mai adiacenti*** per definizione di coloramento e per lo step $(**)$ di BCP

### BCP : Analisi 2 (Time/Message Complexity)

Vediamo la **time complexity**

Abbiamo che il numero di fasi che la procedura BCP eseguirà sono $\Theta(n-\Delta)$, ma $1\leq\Delta\leq n-1$, di conseguenza il worst-case si ha quando $\Delta=O(1)\implies$ numero di fasi risulta essere $\Theta(n)$ (non efficiente)

Vediamo invece la **message complexity**

Per ogni arco passano $2$ messaggi -> $2m$
La procedura lavora in $\Theta(n-\Delta)$ round, quindi otteniamo che : $$M(BCP)=\Theta(m(n-\Delta))$$
In generale, vale il seguente teorema : 

>[!teorem]- Teorema generale
>Su un grafo $G(V,E,Id)$, con coloramento iniziale $C:=ID$ (e con $a=n$), la procedura BCP converge entro $O(n-\Delta)$ round a un $(\Delta+1)$-coloramento, e ha messagge complexity pari a $O((n-\Delta)m)$ 

Vediamo adesso l'altra procedura, quella che sfrutta la parellizzazione in modo molto più efficiente
## Khun-Wattenhofen Color Reduction Procedure (KW-CRP)

Configurazione iniziale e finale come per il task $BCP$

**KW-CRP** : 
- Dato un coloramento $C:V\to[a]$, con $a\gt\Delta+1$, si partiziona l'insieme $V$ :
	- impostiamo $k=\frac{a}{\Delta+1}$, e ogni nodo calcola la sua partizione $V_i$ nel seguente modo $$V_{i}=\{v\in V:(i-1)\cdot(\Delta+1)+1\leq C(v)\leq i\cdot(\Delta+1)\},i=1,\dots,k$$
	- ricordiamo che $V=\{V_1,V_2,\dots,V_k\}$

**Fatto 3** : Il coloramento $C:V\to[a]$ induce un $(2(\Delta+1))$-coloramento, chiamato $F_{12}$ sul ***sottografo indotto*** $G(V_1\cup V_2,E)$, infatti $$F_{12}:V_1\cup V_2\to[2(\Delta+1)]$$
**oss** : Il coloramento $C:V\to[a]$ è un $a$-coloramento su *ogni* sottografo indotto $G$

### KW-CRP : Ingredienti Chiave

**Fatto 4** : Definiamo $F_{i(i+1)}:V_{i}\cup V_{i+1}\to[2(\Delta+1)]$ per ogni $i=1,\dots,k-1$ come nel fatto 3. Allora vale : 
1. $F_{i(i+1)}:V_{i}\cup V_{i+1}\to[2(\Delta+1)]$ è un $[2(\Delta+1)]$-coloramento per il sottografo $G(V_i\cup V_{i+1},E)$
2. L'insieme dei colori usati nei vari $F_{i(i+1)}$ **sono mutualmente disgiunti**

**KW-CRP** Idea Chiave (*Fase*): Applicare BCP, **in parallelo**, su ogni sottografo indotto $G(V_i\cup V_{i+1},E)$, partendo dal $[2(\Delta+1)]$-coloramento $F_{i(i+1)}$
- la procedura BCP trasformerà ogni $[2(\Delta+1)]$-coloramento iniziale $F_{i(i+1)}$, in un $[(\Delta+1)]$-coloramento $F_{i(i+1)}$ per il sottografo indotto $G(V_i\cup V_{i+1},E)$
- Il numero di round paralleli di una *Fase* è pari a $\Delta$

**Fatto 5** : 
1. Dopo **una** applicazione parallela della fase BCP, la funzione globale $\langle F_{12},\dots,F_{i(i+1)},\dots,F_{(k-1)k}\rangle$ diventa un $[\frac{a}{2}]$-coloramento legale per il grafo $G$. (Conseguenza di Fatto 4 e del fatto che gli archi che collegano due classi $V_i,V_j$, detti **Ponti**, non corrompono il coloramento fra queste due classi)
2. Dopo $t$ applicazioni parallele della fase BCP, la funzione globale $\langle F_{12},\dots,F_{i(i+1)},\dots,F_{(k-1)k}\rangle$ diventa un $[\frac{a}{2^t}]$-coloramento per il grafo $G$

### KW-CRP : Time Complexity

>[!teorem]- Teorema
>Partendo da un coloramento inziale (es. $a=n$), dopo $t=\log(\frac{n}{\Delta})$ fasi parallele, la funzione globale $\langle F_{12},\dots,F_{i(i+1)},\dots,F_{(k-1)k}\rangle$ sarà trasformata in un $(\Delta+1)$-coloramento per il grafo $G$.
>Essendo che ogni fase impiega tempo $\Delta$, si avrà che la time complexity generale sarà $O(\Delta\cdot\log(\frac{n}{\Delta}))$

**dim** 
Questo vale perchè (Fatto 5,p.2) dopo $t$ applicazioni avremo un $[\frac{a}{2^t}]$-coloramento per il grafo $G$

Ora, vediamo i calcoli : $$\frac{a}{2^t}\leq\Delta+1\implies2^t\geq\frac{a}{\Delta}\underbrace{\implies}_{\text{minimo t}}t=\Theta\left(\log\left(\frac{n}{\Delta}\right)\right)$$
Ripetendo il tutto per $\Delta$ volte otteniamo $$Time(\text{KW-CRP})=\Theta\left(\Delta\log\left(\frac{n}{\Delta}\right)\right)$$
### KW-CRP : Message Complexity

Su ogni arco passano $2$ messaggi, quindi il num. di messaggi scambiati sarà $\Theta(2m)$
Ripetendo $\Delta\log\left(\frac{n}{\Delta}\right)$ volte otteniamo che : 
$$M(\text{KW-CRP})=\Theta \left(m\left[\Delta\log\left(\frac{n}{\Delta}\right)\right]\right)$$

