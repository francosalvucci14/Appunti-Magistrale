# Phase Technique

Il paradigma della **Basic Phase Technique**

While $V\neq\emptyset$ do : (**Ogni esecuzione è una fase**)
1. Ogni nodo sopravvisuto $v$ esegue in parallelo :
	1. Sceglie u.a.r un colore $C(v)$ da un qualunque insieme $Z$ e informa tutto il suo vicinato $N(v)$
	2. In base al colore ricevuto dal suo vicinato, $C(N(v))$, imposta 
		1. (i) $C(v)$ come "sbagliato"
		2. (ii) $C(v)$ come "okay"
2. Se succede (i), $v$ **sopravvive** e continua a cercare il suo colore nella prossima fase
3. Se succede (ii), $v$ **ottiene** il suo colore finale $C(v)$, informa $N(v)$ e viene rimosso da $G$, ottenendo così un nuovo grafo $G'(V',E')$, con $$\begin{align}&V'=V-\{v\}\\&E'=E-\{(u,v)\in E,v\in V\}\end{align}$$
Dopo aver definito la Phase Technique, passiamo a definire il protocollo che sfrutterà questa tecnica, chiamato Rand-$2\Delta$
# Protocollo Rand-2Delta

