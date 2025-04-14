# Transazioni

Ogni blocco della blockchain di Bitcoin è formato da **header** e **data**. 
Nella scorsa lezione abbiamo affrontato in dettaglio il contenuto dell’header, vediamo ora il contenuto del **data**. 
Ogni elemento in data è una transazione
## Input e Output

Una *transazione* $tx$, è una struttura formata da uno o più input e uno o più output (anche da un numero di versione e da un locktime, ma per il momento non ce ne preoccupiamo).
- Un **output** contiene due campi: un ammontare (valore), ossia un numero intero che corrisponde **all’ammontare di quell’output** e un **locking_script**.
- Un **input** è una struttura formata da $(1)$ un puntatore all’output di una precedente transazione, indicato con la coppia (**prev_tx, prev_id**), dove **prev_tx** è la transazione e **prev_id** è l’indice dell’output all’interno della transazione e $(2)$ un **unlocking_script** (c’è anche un sequence number, ma non ce ne occupiamo).

Diciamo che una transazione $tx_a$ ***spende output*** $tx_b.output$ di una precedente transazione $tx_b$ se uno degli input di $tx_a$ punta all’output $tx_b.output$.

## Script : Locking e Unlocking

Discuteremo in dettaglio gli script in una delle prossime lezioni. Per il momento diciamo solo che i due script, **locking_script** nell’output e **unlocking_script** nell’input, sono dei veri e propri "programmi" scritti in un linguaggio che tutti i nodi della rete possono interpretare. 

Data una transazione $tx$ e un suo input $tx.input$, se la concatenazione dello **unlocking_script** nell’input, $\text{tx.input.unlocking\_script}$, con il **locking_script** contenuto nell’output della transazione precedente puntato da quell’input, $\text{tx.input.(prev\_tx, prev\_id).locking\_script}$ forma un programma che restituisce True, allora l’input $tx.input$ è ***valido***.

Una transazione $tx$ è valida se $(1)$ tutti i suoi input puntano a degli output che non sono già stati spesi da qualche altra transazione e sono validi, e $(2)$ se la somma degli ammontare degli output, $\sum\limits\text{tx.output.ammontare}$ è *minore o uguale* alla somma degli ammontare degli output puntati dagli input, $\sum\limits\text{tx.input.(prev\_tx, prev\_id).ammontare}.$

La differenza, maggiore o uguale a zero, fra questi due valori è la ***transaction fee*** della transazione $tx$.

$$\text{tx.fee}=\sum\limits_{\text{tx.input}}\text{tx.input.(prev\_tx, prev\_id).ammontare}-\sum\limits_{\text{tx.output}}\text{tx.output.ammontare}$$

## Transazione Coinbase

Abbiamo detto che gli input di ogni transazione devono puntare ad output di transazioni precedenti.
C’è un' eccezione a questa regola (deve esserci, altrimenti andremmo a ritroso all’infinito): 
la prima transazione di ogni blocco, cosiddetta ***coinbase transaction***, non è soggetta a questo vincolo.

La coinbase transaction è dove nuovi bitcoin vengono *creati* (*minati*, nel gergo di Bitcoin). 

Affinchè la coinbase transaction dell’$i$-esimo blocco, per $i = 1, 2, \dots$ , sia valida, l’ammontare contenuto nell’output deve essere quello specificato dal protocollo per il blocco $i$-esimo, $new\_btc[i]$, più la somma delle **transaction fee** delle altre transazioni inserite nel blocco.

L’ammontare specificato dal protocollo per i nuovi bitcoin creati per ogni blocco parte da $50$ e si dimezza ogni $210000$ blocchi, $new\_btc[i] = 50/2^{\lfloor i/210000\rfloor}$. 

In questo modo, il totale dei bitcoin in circolazione sarà sempre minore o uguale a 21 milioni.

