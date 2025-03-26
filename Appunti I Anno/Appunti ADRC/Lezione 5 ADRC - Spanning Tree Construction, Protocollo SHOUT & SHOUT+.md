Fin'ora abbiamo visto il problema Broadcast, andando a vedere diversi protocolli che lo risolvono.
Spostiamoci ora su un'altro problema, ovvero il problema **Spanning Tree Construction**

# Spanning Tree Construction

>[!definition]- Spanning Tree
>Uno spanning tree $T$ di un grafo $G=(V,E)$ è un sottografo aciclico di $G$ tale che $T=(V,E')$ e $E'\subset E$

Le assunzioni che andiamo a fare in questo problema sono le seguenti : 
- **Single Initiator**
- Bidirectional Links
- Total Reliability
- $G$ connesso.

## Motivazioni

Perchè vogliamo costruire uno spanning tree del sistema distribuito? 
Ci sono due motivazioni : 
1. Effettuare comunicazioni (**broadcast**) su una sottorete è molto più efficente ($m$ è più piccolo)
2. La subnet deve essere : 
	1. Spanning (cioè toccare tutti i nodi della rete)
	2. Connected

Ogni **Spanning Tree** è lo spanner connesso avente ***minimo*** numero di links

## Il problema ST Distribuito

**Configurazione iniziale** : $\forall x,Tree-neigh(x)=\{\}$
- Significa che all'inizio, ogni nodo ha variabile Tree-neigh vuota
- La situazione è la seguente $\downarrow$  

![[Pasted image 20250326100823.png|center|300]]

**Configurazione finale** : $\forall x,Tree-neigh(x)=\{\text{x-links che appartengono allo ST}\}$
- Quindi, alla fine, ogni nodo dovrà selezionare solo gli archi che fanno parte della soluzione globale, ovvero l'intero ST del sistema distribuito
- La situazione è la seguente $\downarrow$

![[Pasted image 20250326101033.png|center|300]]

>[!warning]- Osservazione cruciale
>I nodi possono ***non conoscere*** lo ST anche **dopo** la computazione

Vediamo ora i vari protocolli per questo problema

### Protocollo SHOUT

