# Expanders

Proprietà fondamentali nella Network Theory **riguardano** il diametro e la fault-tolerance di un grafo $G$

È chiaro che vogliamo che $G$ abbia un **diametro piccolo** e una **buona connettività** anche se qualche arco non funziona.

Per analizzare le due proprietà di cui sopra, dobbiamo introdurre un **concetto fondamentale** in teoria dei grafi : 

>[!definition]- Definizione 4.1
>Dato un grafo $G(V,E)$ $\Delta-$regula, con $|V|=[n]$, la **(node)-expansion** di oni sottoinsieme $S\subset[n]$ è definita come : $$|N(S)|\quad N(S)=\{w\in V\setminus S:(v,w)\in E\text{ per qualche }v\in S\}$$
>Allora, per un $\alpha\gt0$ fissato, diciamo che un grafo $G$ è detto $\alpha$-expander ***se ogni sottoinsieme*** $S\subset[n]$, con $|S|\leq n/2$, ha espansione almeno pari a $\min\{n,\alpha|S|\}$

Il nostro interesse nel grafi $\Omega(1)$-expander è ben motivato dal seguente teorema

>[!teorem]- Teorema 4.2
>COnsideriamo una famiglia di grafi infinita di dimensione crescente, ovvero 
>$$\{G_n(V_n,E_n):|V_n|=[n],n\geq1\}$$
>Se esiste una costante assoluta $\alpha\gt0$ tale che, per un $n$ suff. grande, il grafo $G_n$ è un $\alpha$-expander allora il suo **diametro** è $O(\log(n))$. 
>Inoltre, sotto le assunzioni di cui sopra, per **scollegare completamente** ogni sottoinsieme $S$ dal resto del grafo, il numero di **fault links** deve essere almeno lineare nella size di $S$

**dim**

Consideriamo un grafo fissato, suff. grande $G=G_n$

Fissiamo un qualunque nodo $s\in V$,ed eseguiamo una visita BFS partendo da $s$.
Dato che $G$ è $\alpha$-expander, possiamo definire l'insieme $$L_{t}=\{v\in V:d(s,v)=t\},t=0,1,\dots,n-1$$
Osserviamo quindi che $L_0=\{s\}$ e $L_1=N(s)\geq\alpha$, e quindi $L_1\geq1$ dato che $|N(s)|$ è intero.
Ora definiamo le seguenti famiglie di sottoinsiemi
$$I_{0}=L_{0};\quad I_{t}=I_{t-1}\cup L_t,\quad t=0,1,\dots$$
Notiamo che, per costruzione, vale che $N(I_{t-1})=L_t$ e che quindi $|I_t|=|I_{t-1}|+ |L_t|$
Ora, dato che $G$ è $\alpha$-expander, fintanto che $|I_{t-1}|\leq\frac{n}{2}$, noi otteniamo che $$|I_t|=|I_{t-1}|+ |L_t|\geq(1+\alpha)|I_{t-1}|\geq(1+\alpha)^2|I_{t-2}|\geq\dots\geq(1+\alpha)^{t-1}$$
Sia ora $L_\tau$ un livello tale che il numero di nodi che appartengono al livello al più $\tau$ è maggiore della metà dei nodi, quindi $$\tau=\min\left\{t\geq1:|I_t|\gt\frac{n}{2}\right\}$$
![[Pasted image 20250524145530.png|center|500]]

Allora $\tau$ indica la distanza entro la quale almeno la metà dei nodi del grafo sono distanti da $s$.
Otteniamo quindi che $$|I_\tau|\geq(1+\alpha)^{\tau-1}=\frac{n}{2}\iff\tau=\log_{1+\alpha}\left(\frac{n}{2}\right)+1$$
Quindi il numero di nodi a distanza $\tau=O(\log(n))$ da $s$ sono almeno $\frac{n}{2}$ (ovvero $|I_\tau|\geq\frac{n}{2}$) 

Ora consideriamo un qualunque altro nodo $w\in V\setminus I_\tau$ e ripetiamo il medesimo procedimento con la BFS, partendo da $w$.

Anche qui, grazie alla proprietà expander di $G$, dopo $\tau_1=O(\log(n))$ livelli dell'albero BFS radicato in $w$, otteniamo che il sottoinsieme corrispondente $I_{\tau_1}$ ha raggiunto dimensione almeno $\frac{n}{2}$
Dato che entrambe le visite (quella che parte da $s$ e quella che parte da $w$) raggiungono entrambe *almeno* la metà dei nodi, significa che i due alberi costruiti dalle BFS devono condividere *almeno* un nodo

![[Pasted image 20250524150259.png|center|500]]

Allora data una qualsiasi coppia di nodi $u, v \in V$ esiste sempre un cammino di lunghezza $O(\log n)$ tra $u$ e $v$. 
Ne segue quindi che il diametro di $G$ è $O(\log n),\quad\blacksquare$

