# Problema dello SP egoistico

Il problema si colloca in un ambiente decentralizzato dove le risorse (gli archi della rete) sono controllate da agenti razionali ed egoisti.

- **Input del problema:** Viene fornito un grafo orientato o non orientato $G=(V,E)$, un nodo sorgente $s$ e un nodo destinazione $t$.
- **Agenti:** Ogni arco $e\in E$ rappresenta un singolo agente.
- **Asimmetria Informativa:** Ogni arco ha un costo di utilizzo intrinseco. Questo costo è informazione privata (il _tipo_ dell'agente) ed è noto solo all'agente stesso, non al meccanismo centrale. Il tipo è strettamente positivo (tipo$\gt0$).
- **Obiettivo (Social Choice Function - SCF):** Il meccanismo deve calcolare un _vero_ cammino minimo tra $s$ e $t$ sul grafo $G$, valutato rispetto ai pesi reali (tipi) degli archi, e non rispetto ai valori che gli archi potrebbero strategicamente dichiarare.

Per poter progettare un meccanismo, dobbiamo mappare gli elementi del problema su reti nei parametri standard del Mechanism Design.

In maniera più formale, possiamo definire il problema in questione nel seguente modo:

- **Spazio delle Soluzioni Ammissibili ($F$):** L'insieme $F$ è l'insieme di tutti i possibili cammini semplici nel grafo $G$ che connettono il nodo $s$ al nodo $t$. Una specifica soluzione $P\in F$ è quindi un sottoinsieme degli archi $E$.
- **Il Tipo dell'Agente** ($\tau_e$​): Viene introdotta la notazione $\tau_e$​ per indicare il tipo privato dell'agente $e$. Matematicamente, $\tau_e$ è il peso reale dell'arco, ovvero il costo operativo che l'agente sostiene se il suo arco viene inserito nella soluzione finale.
- **Funzione di Valutazione** ($v_e$​): Questa è la metrica fondamentale. Come valuta l'agente $e$ una data soluzione globale $P$? $$v_e​(\tau_e​,P)=\begin{cases}\tau_e&​e\in P\\0&\text{altrimenti}\end{cases}​$$Questa funzione a gradino è tipica dei **One-Parameter Mechanisms** (Meccanismi a Singolo Parametro): l'agente ha un solo valore di interesse ($\tau_e$​) e la sua valutazione dipende esclusivamente dall'essere selezionato o meno nella soluzione, indipendentemente da quali altri agenti vengano scelti.
- **Funzione di Utilità (ue​):** L'utilità quasi-lineare dell'agente, se dichiara un costo (possibilmente falso) e riceve un pagamento $p_e$​, è definita come $$u_e​=\begin{cases}p_{e}-\tau_e&\text{se arco "e" selezionato}\\0&\text{altrimenti}\end{cases}$$

![center|350](img/Pasted%20image%2020260418145516.png)

Ci poniamo quindi una domanda architetturale fondamentale: _"Come progettare un meccanismo truthful per questo problema?"_.

La risposta risiede nell'osservazione cruciale che collega la metrica di rete alla metrica economica.

Dobbiamo calcolare la lunghezza totale di un generico cammino $P$.
Nel contesto dei grafi, la lunghezza è banale: $\sum\limits_{e\in P}​\tau_{e}$​.
Nel contesto del Mechanism Design, se sommiamo le _valutazioni_ di tutti gli agenti nel sistema $E$ rispetto alla soluzione $P$, otteniamo: $$\sum\limits_{e\in E}​v_e​(\tau_e​,P)$$
Data la definizione della funzione di valutazione $v_e$​ (che si annulla per gli archi non in $P$), l'equazione diventa: $$\sum\limits_{e\in P}​\tau_e​=\sum\limits_{e\in E}​v_e​(\tau_e​,P)$$
**Perché questa osservazione è fondamentale?**

Un problema di ottimizzazione si definisce **utilitario** se e solo se la funzione obiettivo da minimizzare (o massimizzare) coincide esattamente con la somma delle valutazioni degli agenti. 
Poiché minimizzare lo shortest path significa minimizzare $\sum\limits_{e\in P}​\tau_{e}$​, e questo equivale a minimizzare $\sum\limits_{e\in E}​v_e​(\tau_e​,P)$, abbiamo appena dimostrato formalmente che il problema dello Shortest Path egoistico è un problema utilitario.

Poiché il problema è utilitario, per il teorema dimostrato in precedenza, possiamo applicare direttamente l'infrastruttura dei **Meccanismi VCG**.
## Meccanismo VCG - $M_{SP}$

Prima di tutto ricordiamo la formulazione per un meccanismo VCG, $M=\langle g(r),p(r)\rangle$:

- **Regola di allocazione $g(r)$:** Viene definita come $x^{\star}=arg\min_{x\in F}​\sum\limits_{j}​v_j​(r_j​,x)$. In parole povere, l'algoritmo sceglie la soluzione $x^{\star}$ (il cammino) che minimizza la somma delle valutazioni (ovvero la somma dei pesi dichiarati).
- **Regola di pagamento $p_e​(r)$ (Pivot di Clarke):** Questa è la traduzione matematica dell'esternalità che abbiamo discusso in precedenza. Il pagamento per un agente $e$ è: $$p_e​(r)=\sum\limits_{j\neq e}​v_j​(r_j​,g(r_{-e}​))-\sum\limits_{j\neq e}​v_j​(r_j​,x^{\star})$$ 
Il primo termine è il costo totale che gli _altri_ agenti avrebbero sostenuto nella soluzione ottima calcolata ignorando $e$ ($g(r_{-e}​)$). Il secondo termine è il costo totale sostenuto dagli _altri_ agenti nella soluzione ottima effettiva con $e$ ($x^{\star}$).

Applichiamo ora la formula generale al caso specifico dei grafi.

- **L'allocazione $g(r)$:** Diventa semplicemente il calcolo di un cammino minimo, indicato con $P_G​(s,t)$, sul grafo $G$ utilizzando i pesi dichiarati $r$.
- **Il pagamento $p_e​(r)$:** Viene analizzato in due casi distinti:
    1. **Se $e\not\in P_G​(s,t)$:** L'arco non fa parte del cammino minimo. In questo caso, la sua assenza non altera la soluzione ottima ($g(r_{-e}​)=g(r)$). L'esternalità è nulla e il pagamento è **0**.
    2. **Se $e\in P_G​(s,t)$:** L'arco è nel cammino minimo. Dobbiamo tradurre i due termini della formula di Clarke in metriche di grafo:
        - Il termine $\sum\limits_{j\neq e}=​v_j​(r_j​,g(r_{-e}​))$ rappresenta la lunghezza del cammino minimo da $s$ a $t$ se l'arco $e$ venisse fisicamente rimosso dal grafo. Questo viene definito **Cammino di Rimpiazzo** (Replacement Path) e la sua lunghezza è denotata come $d_{G-e}​(s,t)$.
        - Il termine $\sum\limits_{j\neq e}=​v_j​(r_j​,P_G​(s,t))$ è la somma dei costi di tutti gli _altri_ archi presenti nel cammino minimo effettivo. Matematicamente, questo equivale alla lunghezza totale del cammino minimo ($d_G​(s,t)$) meno il costo dichiarato dall'arco $e$ ($r_e$​).
- **La formula finale del pagamento:** Sostituendo i termini, otteniamo la formula calcolabile: $$p_e​(r)=\begin{cases}d_{G-e​}(s,t)-(d_G​(s,t)-r_e​)&e\in P_{G}(s,t)\\0&\text{altrimenti}\end{cases}$$L'implicazione algoritmica è severa: per calcolare i pagamenti di _tutti_ gli archi nel cammino minimo originale, l'algoritmo deve calcolare un ***cammino di rimpiazzo*** $P_{G-e}​(s,t)$ per ciascuno di essi.

Mostriamo ora un esempio numericp della formula appena derivata su una specifica topologia di rete, per calcolare il pagamento dell'arco centrale $e$ (dichiarato con costo $r_e​=2$).

1. **Analisi del Cammino Ottimo Originale ($P_G$​):** Il cammino minimo primario $P_G​(s,t)$ scende verticalmente passando per $e$. I costi degli archi che lo compongono sono: 4 (nodo superiore $\to$ medio), 2 (l'arco $e$), e 5 (nodo medio $\to t$). La lunghezza totale è: $d_G​(s,t)=4+2+5=11$. Il costo degli _altri_ archi nel cammino è $d_G-r_e​=11−2=9$.
2. **Analisi del Cammino di Rimpiazzo ($P{G-e}$​):** Immaginiamo di rimuovere l'arco $e$ (la "X" blu). Qual è il nuovo cammino minimo per andare da $s$ a $t$? Il percorso evidenziato in rosso aggira la rimozione: va a sinistra (costo 2), scende diagonalmente verso il nodo centrale inferiore (costo 5), e poi va a $t$ (costo 5). La lunghezza del cammino di rimpiazzo è: $d_{G-e}​(s,t)=2+5+5=12$.
3. **Calcolo del Pagamento ($p_e$​):** Applicando rigorosamente la formula di Clarke derivata precedentemente otteniamo:$$\begin{align}&p_e​=d_{G-e​}(s,t)-(d_G​(s,t)-r_e​)\\&p_e​=12-(11-2)\\& p_e​=12-9=3\end{align}$$

L'agente $e$ ha dichiarato un costo di 2, e il meccanismo lo ripaga con $3$. Possiamo notare immediatamente che l'utilità dell'agente è positiva ($u_e​=p_e​-r_e​=3-2=1$). 

L'agente trae un profitto netto pari esattamente a 1, confermando la proprietà di Razionalità Individuale del meccanismo VCG.

![center|350](img/Pasted%20image%2020260418153432.png)
### Analisi: Complessità Temporale

Affrontiamo ora l'analisi della **complessità temporale** e dei **vincoli topologici** del meccanismo $M_{SP}​$.

Prima di valutare le prestazioni, introduciamo un'ipotesi di lavoro fondamentale: **i nodi sorgente $s$ e destinazione $t$ devono essere $2$-edge connessi**.

Questo significa che nel grafo $G$ devono esistere almeno due cammini tra $s$ e $t$ disgiunti sugli archi. La necessità di questa assunzione emerge chiaramente analizzando il caso contrario:

- **Definizione di Ponte (Bridge):** Se $s$ e $t$ non sono $2$-edge connessi, esiste per forza almeno un arco nel cammino minimo $P_G​(s,t)$ la cui rimozione disconnette il grafo in due componenti separate $C_1$​ e $C_2$​ (con $s\in C_1$​ e $t\in C_2$​). 
- **Conseguenza Algoritmica:** Se l'arco $e$ è un ponte, non esiste alcun cammino di rimpiazzo in $G-e$. Matematicamente, la distanza di rimpiazzo diverge all'infinito: $d_{G-e}​(s,t)=\infty$.
- **Conseguenza Economica (Il Monopolio Assoluto):** Inserendo $\infty$ nella formula del pagamento VCG, otteniamo $p_e​=\infty$. L'agente che controlla un arco ponte possiede un monopolio assoluto sulla connessione tra $s$ e $t$. Il meccanismo collassa poiché l'agente "tiene in pugno" il sistema e può esigere una cifra arbitrariamente alta, distruggendo l'utilità del pianificatore centrale. La ridondanza strutturale (2-edge connectivity) è quindi obbligatoria per spezzare i monopoli e limitare i pagamenti.

Assunta la connettività necessaria, come calcoliamo i pagamenti? Si definisce l'approccio ingenuo (brute-force) per determinare il limite superiore della complessità temporale.

Siano $n=|V|$ i nodi e $m=|E|$ gli archi.

1. Calcoliamo il cammino minimo $P_G​(s,t)$ usando l'algoritmo di Dijkstra. Questo definisce l'allocazione e seleziona $k$ archi vincenti. Nel caso peggiore, il cammino contiene $k=O(n)$ archi.
2. Per calcolare i pagamenti, dobbiamo trovare il cammino di rimpiazzo $P_{G-e}​(s,t)$ per ciascuno di questi $O(n)$ archi.
3. La soluzione banale consiste nel rimuovere l'arco $e$, applicare Dijkstra da zero sul grafo decurtato $G-e$, e ripetere questo processo $\forall e\in P_G​(s,t)$.

Poiché l'algoritmo di Dijkstra ha una complessità di $O(m+n\log(n))$, iterarlo $O(n)$ volte produce una complessità temporale complessiva pari a:
$$O(n)\cdot O(m+n\log(n))=O(mn+n^2\log(n))$$

Sebbene sia una complessità polinomiale, un limite di $O(mn)$ è computazionalmente inaccettabile per il routing su reti su larga scala 

**Il Teorema di Ottimalità Computazionale**

Concludiamo enunciando un teorema fondamentale per l'Algorithmic Mechanism Design applicato ai grafi: **$M_{SP}$​ è calcolabile in tempo $O(m+n\log(n))$.**

Questo teorema dimostra che il limite asintotico di $O(mn+n^{2}\log(n))$ non è stretto. Esistono algoritmi avanzati che permettono di calcolare **simultaneamente** tutti i cammini di rimpiazzo necessari per i pagamenti VCG.

Invece di eseguire Dijkstra da zero per ogni arco rimosso, questi algoritmi sfruttano la struttura ad albero dei cammini minimi e riutilizzano gli stati di rilassamento degli archi non influenzati dalla rimozione di $e$.

Il risultato è straordinario: il tempo necessario per risolvere l'intero problema del Mechanism Design collassa esattamente alla stessa classe di complessità necessaria per calcolare un singolo Shortest Path in un ambiente non strategico: $O(m+n\log(n))$.


---
# Meccanismi One-Parameter