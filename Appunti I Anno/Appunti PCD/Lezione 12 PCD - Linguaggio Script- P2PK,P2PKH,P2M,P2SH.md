Abbiamo detto precedentemente che una transazione $tx_a$ può avere uno o più output $tx_a.output$, ogni output è costituito da un **ammontare** e da un **locking_script**.

Una transazione $tx_b$ che volesse *spendere* $tx_a.output$ deve contenere, nell'input che punta a $tx_a.output$, un **unlocking_script** tale che la concatenazione di $tx_b.input.unlocking\_script$ con $tx_a.output.locking\_script$ formi uno **script** che restituisca TRUE. 

Vediamo nel dettaglio questo processo

# Script

Il software di sistema Bitcoin, in esecuzione su ogni nodo della rete, contiene l'interprete di un semplice linguaggio di programmazione chiamato *Script*.

Il linguaggio Script è ***stateless*** (non ci sono variabili che possono salvare localmente un dato e andare a rileggerlo successivamente)

Un programma (uno script) è una sequenza di comandi (*istruzioni* o *dati*) che vengono eseguti secondo un modello *stack-based* : i *dati* e le *istruzioni* vengono inseriti in una *pila* (lo *stack*); quando una istruzioni viene inserita nella pila, può estrarre uno o più dati dalla pila, eseguire delle computazioni sui dati ed eventualmente inserire il risultato delle computazioni nella pila.

**esempio**

L'istruzione ***ADD*** nel linguaggio Script estrae due dati dalla pila e ne esegue la somma, quindi il seguente script $$<2><3>ADD$$
verrebbe eseguito dall'interprete Script presente sui nodi della rete Bitcoin in questo modo : viene inserito nella pila il dato $2$, poi viene inserito il dato $3$, poi viene inserito nella pila l'istruzione ADD che estrae dalla pila i due dati sottostanti, e inserisce infine il valore $5$ nella pila.

![[Pasted image 20250426151433.png|center|400]]

Ci sono tanti tipi di Script che sono : 
- **Pay to Public Key** (p2pk) : Il più semplice
- **Pay to Public Key Hash** (p2pkh) : Più sicuro del precedente
- **Pay to Multisig** (p2m) : Usato per fare passare le transazioni a più sig
- **Pay to Script Hash** (p2sh) : Turing-completo

## Pay To Public Key (p2pk)

È il più semplice dei **locking_script** presenti in Bitcoin, ed è formato da due comandi $$<pk>CHECKSIG$$
Il primo comando, **\<pk\>**, è un dato costituito da una chiave pubblica.

Il secondo,**CHECKSIG**, è una istruzione (OP_CODE nella terminologia di Bitcoin) che estrare dalla pila i due comandi sottostanti e verifica se il secondo è una firma corretta della transaizone rispetto alla chiave pubblica contenuta nel primo dato :
- in caso affermativo, inserisce nella pila TRUE e la transazione risulta valida
- in caso negativo, inserisce nella pila FALSE e la transazione viene rigettata come non valida

Se una transazione $tx_a$ ha output $tx_a.output$ con un locking\_script 