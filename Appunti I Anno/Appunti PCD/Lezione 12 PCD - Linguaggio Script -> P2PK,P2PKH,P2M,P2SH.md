>[!important]- IMPORTANTE
>I Locking_Script sono contenuti **negli output delle transaizoni**
>Gli Unlocking_script sono contenuti **negli input delle transazioni**


Abbiamo detto precedentemente che una transazione $tx_a$ può avere uno o più output $tx_a.output$, ogni output è costituito da un **ammontare** e da un **locking_script**.

Una transazione $tx_b$ che volesse *spendere* $tx_a.output$ deve contenere, nell'input che punta a $tx_a.output$, un **unlocking_script** tale che la concatenazione di $tx_b.input.unlocking\_script$ con $tx_a.output.locking\_script$ formi uno **script** che restituisca TRUE. 

Vediamo nel dettaglio questo processo

# Script

Il software di sistema Bitcoin, in esecuzione su ogni nodo della rete, contiene l'interprete di un semplice linguaggio di programmazione chiamato *Script*.

Il linguaggio Script è ***stateless*** (non ci sono variabili che possono salvare localmente un dato e andare a rileggerlo successivamente)

Un programma (uno script) è una sequenza di comandi (*istruzioni* o *dati*) che vengono eseguti secondo un modello *stack-based* : i *dati* e le *istruzioni* vengono inseriti in una *pila* (lo *stack*); quando una istruzioni viene inserita nella pila, può estrarre uno o più dati dalla pila, eseguire delle computazioni sui dati ed eventualmente inserire il risultato delle computazioni nella pila.

**esempio**

L'istruzione ***ADD*** nel linguaggio Script estrae due dati dalla pila e ne esegue la somma, quindi il seguente script $$\text{<2> <3> ADD}$$
verrebbe eseguito dall'interprete Script presente sui nodi della rete Bitcoin in questo modo : viene inserito nella pila il dato $2$, poi viene inserito il dato $3$, poi viene inserito nella pila l'istruzione ADD che estrae dalla pila i due dati sottostanti, e inserisce infine il valore $5$ nella pila.

![[Pasted image 20250426151433.png|center|400]]

Ci sono tanti tipi di Script che sono : 
- **Pay to Public Key** (p2pk) : Il più semplice
- **Pay to Public Key Hash** (p2pkh) : Più sicuro del precedente
- **Pay to Multisig** (p2m) : Usato per fare passare le transazioni a più sig
- **Pay to Script Hash** (p2sh) : Turing-completo

## Pay to Public Key (p2pk)

È il più semplice dei **locking_script** presenti in Bitcoin, ed è formato da due comandi $$\text{Locking Script :}\text{<pk> CHECKSIG}\quad(1)$$Il primo comando, **\<pk\>**, è un dato costituito da una chiave pubblica.

Il secondo,**CHECKSIG**, è una istruzione (OP_CODE nella terminologia di Bitcoin) che estrare dalla pila i due comandi sottostanti e verifica se il secondo è una firma corretta della transaizone rispetto alla chiave pubblica contenuta nel primo dato :
- in caso affermativo, inserisce nella pila TRUE e la transazione risulta valida
- in caso negativo, inserisce nella pila FALSE e la transazione viene rigettata come non valida

Se una transazione $tx_a$ ha output $tx_a.output$ con un locking\_script di questo tipo, allora per spendere quell'output una transazione $tx_b$ dovrà avere un input con un unlocking\_script costituito da un solo comando : $$\text{Unlocking Script :}<sig>$$
in modo che la concatenazione di $tx_b.input.unlocking\_script$ con $tx_a.output.locking\_script$ sia $$\text{Script (p2pk) :}\text{<sig> <pk> CHECKSIG}\quad(2)$$
e l'interprete Script che esegue lo script avrò sullo stack alla fine dell'esecuzione TRUE o FALSE a seconda che **\<sig\>** sia oppure no una firma valida per la chiave pubblica **\<pk\>** della transazione $tx_b$

![[Pasted image 20250426152917.png|center|400]]

Notiamo che **\<sig\>** non può contemporaneamente essere parte della transazione $tx_b$ ed essere una firma valida per $tx_b$.

Infatti, più precisamente possiamo dire che, afficnhè lo script in $(2)$ inserito in una transazione $tx_b$ ritorni TRUE, **<sig\>** deve essere una firma valida della sequenza di byte che si ottiene da $tx_b$ dove, nel campo $tx_b.input.unlocking\_script$ riservato a **\<sig\>**, viene inserito **<pk\>** 
## Pay to Public Key Hash (p2pkh)

Tutte le prime transazioni di Bitcoin avevano dei **locking\_script** del tipo **p2pk**

Successivamente, diversi nuovi tipi di locking\_script sono stati introdotti : il secondo, dopo p2pk, è stato quello chiamato **Pay to Publick Key Hash** (p2pkh).

In questo tipo di **locking\_script** non compare direttamente la chiave pubblica, ma l'hash della chiave pubblica **\<pkhash\>**.

Complessivamente il **locking\_script** è formato da cinque comandi : 
$$\text{Locking Script : } \text{DUP HASH160 <pkhash> EQUAL\_VERIFY CHECKSIG}$$
dove : 
- $DUP$ è un'istruzione che inserisce nello stack una copia dell'elemento sottostante. Per esempio lo script $\text{<1> DUP}$ verrebbe eseguito in questo modo : ![[Pasted image 20250426154129.png|center|200]]
- $HASH160$ è un'istruzione che estrae dallo stack l'elemento sottostante e inserisce nello stack il suo hash (opportunamente calcolato)
- **\<pkhash\>** è l'hash di una chiave pubblica
- $EQUAL\_VERIFY$ è un'istruzione che estrae due elementi sottostanti dallo stack e se sono uguali non fa nulla, altrimenti interrompe l'esecuzione dello script dichiarando transaizone non valida
- $CHECKSIG$ è il comando che abbiamo visto in precedenza in p2pk

L'unlocking_script invece è : $$\text{Unlocking Script : }\text{<sig><pk>}$$
## Pay to Multisig (p2m)

Con questo script si può decidere di far spendere l'output della transazione a più public key.

Come detto in precedenza, questo script non viene molto usato perchè tutte le public key si trovano nel locking script.

Il formato del locking\_script è il seguente : $$\text{Locking Script : } \underbrace{t}_{\text{soglia da rispettare}} <pk_1>\dots<pk_n>n\space \text{CHECKMULTISIG}$$

Mentre l'unlocking_script è
$$\text{Unlocking Script : } <sig_1>\dots<sig_n>$$
Esempio : Se voglio che su $3$ persone $2$ possano spendere l'output di una transizione, deve valere che :
- LS : $2<pk_1><pk_2><pk_3>3\space CHECKMULTISIG$
- US : $<sig_a><sig_b>$

## Pay to Script Hash (p2sh)

L'ultimo tipo di Script è il **Pay to Script Hash** (p2sh).

In questo script il locking_script e l'unlocking_script sono formati così : 
- LS : $HASH160\underbrace{\text{ <reedem-script hash> }}_{\text{20 byte}}EQUAL$
- US : $\text{<reedem-script>}$

Dove **EQUAL** è un'istruzione che estrae due elementi sottostanti nello stack e inserisce nello stack TRUE se sono uguali, FALSE altrimenti