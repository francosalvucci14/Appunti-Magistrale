# Ambiente Permissionless

I problemi e i protocolli che abbiamo considerato finora erano formulati per un ambiente *permissioned*, ossia quando i nodi che partecipano al protocollo sono noti a tutti e non cambiano durante l’esecuzione del protocollo.

In un ambiente ***permissionless*** invece i nodi che partecipano al protocollo non sono noti a
priori e possono variare durante l’esecuzione del protocollo. Partecipare al protocollo significa essenzialmente scaricare un software ed eseguirlo, entrando in comunicazione con gli altri nodi che lo stanno eseguendo.

In un ambiente permissionless è necessario introdurre delle misure atte a mitigare la possibilità di ***sybil attacks***, ossia limitare la capacità di un singolo nodo corrotto di generare più identità e quindi "simulare" più nodi.

Il protocollo di consenso introdotto da Satoshi Nakamoto usa la **proof-of-work** sia per impedire che un singolo nodo corrotto possa agire come più nodi onesti, sia per fare in modo che tutti i nodi onesti concordino su quali sono i dati "corretti" da tenere in memoria.

Con il termine proof-of-work si intende una breve "dimostrazione", che può essere facilmente (da un punto di vista computazionale) "verificata" che una certa quantità di lavoro computazionale è stata eseguita.

Per esempio, il seguente programma ha impiegato diverse ore su un normale pc prima di dare in output una stringa di testo formata dal nome "Francesco", cognome "Pasquale" e un numero il cui hash crittografico $sha256$ espresso in esadecimale iniziasse con una sequenza di nove zeri (ossia, che rappresentasse un numero inferiore a $2^{256−9\cdot4}$). 

```python
from hashlib import sha256

nonce = 0
flag = False
while not flag:
	nonce += 1
	text = "Francesco Pasquale " + str(nonce)
	flag =  (sha256(text.encode(’utf8’)).hexdigest()[:9] == ’000000000’)
print(text)
```

Siccome $sha256$ è una funzione hash crittografica, non c’è altro modo per risolvere un tale
problema (trovare un numero che concatenato con la stringa Francesco Pasquale dia un hash al di sotto di quella soglia) che andare per tentativi.

Una volta che tale lavoro è stato fatto, chiunque può verificarlo in una frazione di secondo eseguendo il calcolo di un unico hash.

```python
from hashlib import sha256

nonce = ’88843838094’
text = ’Francesco Pasquale’ + nonce
print(text)
print(sha256(text.encode(’utf8’)).hexdigest())
```

Quindi il nonce $88843838094$ è una "prova" che con altissima probabilità qualche computer da
qualche parte deve aver fatto miliardi di hash per trovarne uno che soddisfacesse i requisiti. 

Inoltre, se qualcuno volesse trovare un **nonce** per una stringa iniziale diversa dal nome "Francesco" e cognome "Pasquale", non avrebbe nessun modo di avvantaggiarsi del lavoro già svolto per per la mia stringa.

## Remark su Funzioni Hash Crittografiche

Ricordiamo brevemente cos'è una funzione hash crittografica

>[!definition]- Funzione Hash Crittografica
>Una f.h.c $H$ è una funzione $$H:\{0,1\}^\star\to\{0,1\}^\lambda$$ che si comporta come un "Random Oracle", ovvero $$x\to H(x)\text{ scelto u.a.r. su }\{0,1\}^\lambda$$

Ci sono 3 proprietà fondamentali che una funzione hash crittografica $H$ deve rispettare : 

1. **Preimage Resistance** : Deve essere "difficile", dato $y\in\{0,1\}^\lambda$, trovare $x\in\{0,1\}^\star$ tale che $H(y)=x$
	1. L'unico modo deve essere con algoritmo BruteForce
2. **Second Preimage Resistance** : Deve essere "difficile", dato $x_1\in\{0,1\}^\star$, trovare $x_2\neq x_1:H(x_2)=H(x_1)$
3. **Collision Resistance** : Deve essere "difficile" trovare $x_1\neq x_2:H(x_1)=H(x_2)$

# Protocollo di Consenso : Bitcoin

Nel caso di Bitcoin il protocollo vuole fare in modo che:

- Ogni nodo onesto mantenga una copia locale di un vettore block a cui vengono periodicamente aggiunte nuovi elementi, che chiamiamo blocchi. Il vettore di blocchi è la cosiddetta ***blockchain***.
- (*Eventual Consistency*): Le copie locali **block** dei vettori dei singoli nodi onesti concordino, eccetto al più per un numero limitato di blocchi alla fine del vettore.
- (*Liveness*): Se un nodo onesto riceve in input una transazione $tx$ (per il momento pensiamo a una transazione semplicemente come a un "dato"), questa prima o poi viene inserita in un blocco.
- Un nodo onesto che entri a far parte della rete in qualunque momento e chieda ad altri nodi nella rete di fornirgli il vettore block condiviso dagli altri, deve avere un modo di discernere quale sia il vettore "corretto", in caso riceva informazioni discordanti da nodi diversi

Il protocollo di consenso di Nakamoto (aka Bitcoin), può essere sintetizzato in quest righe di codice

![center|600](img/Pasted%20image%2020250414113113.png)

## Blocchi della blockchain

Ogni blocco è diviso in **header** e **data**. 

L' header è **formato** esattamente da $80$ byte: $32$ byte ciascuno per **prev_hash** e **data_hash**, che sono rispettivamente lo $sha256$ dello header del blocco precedente e lo $sha256$ del data (opportunamente serializzati), e $4$ byte ciascuno per **ver, timestamp, target, nonce**. 

Il **ver** è un numero di versione che in genere non ha nessun ruolo e **timestamp** è la data e ora attuale rappresentata in Unix time, ossia un numero intero che indica il numero di secondi trascorsi dalla mezzanotte del 1 gennaio 1970. 
Il target è un elemento cruciale, di cui parleremo fra un attimo, che viene utilizzato per fare in modo che il numero di blocchi creati si mantenga, in media, a un ritmo di $1$ blocco ogni $10$ minuti circa, indipendentemente da quanti siano i nodi della rete e quale sia il loro potere computazionale. 
Il nonce è un numero intero qualunque a $32$ bit tale che, dati gli altri 5 campi, faccia in modo che lo $sha256$ dello header sia minore del target.

Osserviamo che : 

1. Come nel caso dell’esempio precedente in python, trovare un nonce adeguato richiede la computazione di un numero di hash che dipende dal **target** (in media questo numero sarà $\frac{2^{256}}{target}$), invece verificare che un certo header abbia un hash al di sotto del target in esso contenuto richiede la ***computazione di un unico hash***
2. Per *produrre* una blockchain con $t$ blocchi, un nodo dovrà eseguire un numero di hash che in media sarà $$2^{256}\cdot\sum\limits_{i=1}^n\frac{1}{block[i].header.target}$$ Questo numero è quello che viene indicato come output della funzione WORK, riga 29 dello pseudocodice. Per *verificare* che in una catena con $t$ blocchi l’hash di ogni blocco è al di sotto del target invece un nodo deve eseguire soltanto t hash.
3. Siccome l' header di ogni blocco contiene l’hash del blocco precedente **prev_hash**, se un nodo volesse modificare il contenuto dell’$i$-esimo blocco in una catena di $t$ blocchi, dovrebbe **ricalcolare un nonce opportuno per ognuno dei blocchi** dall’$i$-esimo al $t$-esimo (questo implica l'impossibilità, almeno teorica, di riuscire a rompere la blockchain di Bitcoin, in quanto per fare ciò servirebbe una potenza di calcolo pari almeno al $51\%$ della potenza dell'intera rete Bitcoin)

Vediamo ora come viene calcolato il **target** in Bitcoin.
## Calcolo del target

La scelta implementativa di Satoshi Nakamoto in Bitcoin è stata la seguente.

Il target iniziale è fissato nel ***genesis block*** (ovvero il blocco $0$ della blockchain di Bitcoin), e ogni $2016$ blocchi, che corrispondono a 14 giorni se i blocchi vengono prodotti a un ritmo di esattamente 1 al minuto, si ricalcola il target che verrà usato per i successivi $2016$ blocchi: se la differenza fra i timestamp contenuti nell’ultimo e nel primo blocco di un’epoca
di 2016 blocchi è maggiore di 14 giorni allora il target **va aumentato** di una quantità opportuna, se la differenza e minore di 14 giorni il target va diminuito di una quantità opportuna. 

**La quantità opportuna** è quella che garantisce che, se il numero di hash al secondo nella prossima epoca di 2016 blocchi sarà uguale a quello dell’epoca appena conclusa, allora i 2016 blocchi della prossima epoca saranno prodotti, in media, in 14 giorni.

Un’ultima osservazione a proposito del target è che si tratta di un numero intero positivo minore di $2^{256}$ ma viene memorizzato in soli $4$ **byte**, quindi chiaramente non tutti i numeri sono possibili target. 
In Bitcon viene utilizzata una rappresentazione in notazione scientifica *custom*, che usa l’ultimo dei quattro byte per codificare l'esponente **exp** e i primi tre byte per il **coefficiente**

