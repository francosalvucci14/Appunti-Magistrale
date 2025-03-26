Spostiamoci ora nel problema noto come **Depth First Traversal (DFT)**
# Problema Depth First Traversal

In questo problema andiamo a vedere la capacità di **somministrare** un token (risorsa) ad ogni nodo del SD, in modo mutualmente esclusivo (ad ogni istante di tempo, uno e un solo nodo avrà il token)

Ci mettiamo sotto le assunzioni standard $R={UI,BL,TR,CN}$

Vediamo la prima versione del protocollo per DFT, chiamato protocollo Back

## Protocollo Back

Per ogni nodo $x\in V$
1. Quando visitato per la **prima volta** - ricorda chi è il (**padre**)
	1. Invia il token a uno dei vicini non visitati
	2. aspetta la risposta
2. Quando il vicino riceve il **token**
	1. Se già visitato, rimanda il token al padre usando un **back-links**
	2. Altrimenti, **lo invia in modo sequenziale a tutti** i vicini non visitati prima di rimandarlo indietro
3. Se non ci sono più nodi inesplorati, ritorna il token (**reply**) al padre
4. Alla ricezione di un reply, invia il token ad un'altro vicino non visitato

### Message Complexity

Abbiamo