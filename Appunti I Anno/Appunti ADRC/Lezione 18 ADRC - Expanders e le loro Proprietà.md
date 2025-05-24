# Expanders

Proprietà fondamentali nella Network Theory **riguardano** il diametro e la fault-tolerance di un grafo $G$

È chiaro che vogliamo che $G$ abbia un **diametro piccolo** e una **buona connettività** anche se qualche arco non funziona.

Per analizzare le due proprietà di cui sopra, dobbiamo introdurre un **concetto fondamentale** in teoria dei grafi : 

>[!definition]- Definizione 4.1
>Dato un grafo $G(V,E)$ $\Delta-$regula, con $|V|=[n]$, la **(node)-expansion** di oni sottoinsieme $S\subset[n]$ è definita come : $$|N(S)|\quad N(S)=\{w\in V\setminus S:(v,w)\in E\text{ per qualche }v\in S\}$$
>Allora, per un $\alpha\gt0$ fissato, diciamo che un grafo $G$ è detto $\alpha-$expander ***se ogni sottoinsieme*** $S\subset[n]$, con $|S|\leq n/2$, ha espansione almeno pari a $\min\{n,\alpha|S|\}$



