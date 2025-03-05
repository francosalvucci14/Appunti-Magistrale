# Introduzione generale al corso

Prima parte del corso prof. Clementi
Seconda parte dott. Pepè

**Limiti SD** (Sistema Distribuito)

Esempio

***(Sistema Standard)***

Consideriamo un grafo $G(V,E)$. Il problema è dato il grafo trovare il MST $T\subseteq E$
Il grafo è rappresentato con matrice di adiacenza

Nei sistemi standard il problema è semplice dato che si ha una **visione globale** dell'input, ma la sua esecuzione è strettamente sequenziale. Si lavora con un solo processore.

***(Sistema Distribuito)***

In questo caso, il grafo fa sia da input del problema che da topologia di rete sui cui gira il sistema distribuito

Ho un processore su ogni nodo, che rappresenta una macchina.

A tempo $0$ ogni nodo ha una conoscenza limitata dell'input, infatti ogni nodo conosce solo il suo $ID\in[n]$ e l'etichetta dell'arco con i suoi vicini.

Si ha una **visione locale** dell'input, ma ci sono più processori su cui lavorare

L'algoritmo ha forti limiti sulla comunicazioni tra processori.

Nei SD bisogna in qualche modo determinare cos'è l'output dell'algoritmo, infatti definiamo due tipi di output : 
- **output globale** : Ogni nodo, al termine dell'esecuzione dell'algoritmo, deve conoscere la situazione finale (es. nel problema del MST, ogni nodo deve conoscere gli archi che compongono il MST)
- **output locale** : Ogni nodo conosce solamente la parte di soluzione interessata a lui (es. prob. del MST, ogni nodo conosce gli archi del MST incidenti a lui)

Nei SD, l'algoritmo diventa un ***insieme di regole***, immerse nel mondo distribuito : 
1. Ogni regola va assegnata ad ogni nodo
2. Ogni nodo vede la sua storia e lo stato in cui si trova, poi prende decisioni (esegue passo sotto)
	1. Cambia stato, aggiorna variabii locali secondo le regole, poi decide se e dove mandare messaggi (**azione atomica** al tempo $t$)

Bisogna chiarire la differenza tra algoritmo e protocollo nei SD : 

- Algoritmo distribuito : **Idea algoritmica**
- Protocollo : **Implementazione dell'idea algoritmica su uno specifico SD**

**Per costruire** il protocollo ci immergiamo in un nodo locale : regole locali sui nodi
**Per analizzare** il protocollo ci mettiamo un una visione globale del sistema

Nei sistemi centralizzati il concetto di spazio e tempo è ben definito

Nei sistemi distribuiti invece dobbiamo considerare non solo il tempo di esecuzione dei processori, ma anche i ritardi di trasmissione dei messaggi.

Prendiamo $\tau=t$ max di ritardo di trasmissione

I SD si dividono in due classi : 
- ***modelli sincroni*** :
	- il protocollo conosce $\tau$, e questo $\tau$ può essere codificato
	- il tempo di esecuzione è definibile
- **modelli asincroni** :
	- concetto di tempo non troppo fondamentale
	- il protocollo *non* conosce $\tau$
		- ***total reliability*** : Ci garantisce che prima o poi il sistema terminerà, non si sa quando ma sempre in un tempo finito.

Nei modelli sincroni troviamo il concetto di **tempo parallelo**, ovvero il numero di round affinchè tutti i processori raggiungano lo stato di terminazione.

