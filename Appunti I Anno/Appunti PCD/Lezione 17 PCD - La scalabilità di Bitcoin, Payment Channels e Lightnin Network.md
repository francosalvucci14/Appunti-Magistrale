# Scalabilità di Bitcoin

Il sistema Bitcoin è *by design* poco scalabile, nel senso che il limite imposto dal meccanisco di consenso sulla dimensione dei blocchi e sul tempo medio che intercorre fra la creazione di due blocchi consegutivi fa sì che il numero massimo di transazioni che possono essere incluse nella blockchain è molto piccolo (meno di una decina di transazioni al secondo), se confrontato con altri sistemi di pagamento elettronico centralizzati

Dall’introduzione di Bitcoin sono stati proposti diverse soluzioni per ovviare a questa limitazione intrinseca, che hanno avuto più o meno successo. 

Quella di cui ci occuperemo noi è quella che consiste nella costruzione di una ***rete di canali di pagamento***, e nello specifico delle tecniche usate per progettare e implementare la ***Lightning Network***
## Canali di pagamento : Funding e Refunding Transactions

Supponiamo che Alice abbiamo $10$btc in un output non speso di una certa transazione con id $b8ff\dots11f0$

![[Pasted image 20250527151015.png|center]]
dove **pkA0** è una chiave pubblica di cui lei ha la corrispondente chiave privata **skA0**, e decida di costruire la seguente transazione, che chiamiamo *funding transaction* per ragioni che saranno chiare (spero) a breve., che spende quei $10$btc

![[Pasted image 20250527151134.png|center]]

dove **pkA** è una chiave pubblica di cui Alice ha la corrispondente chiave privata **skA**, mentre **pkB** è una chiave pubblica di cui un altro soggetto,Bob,ha la corrispondente chiave segreta **skB**

Se Alice firmasse questa *FundingTx* in $(2)$ con la chiave segreta **skA0** - quella autorizzata a spendere l'output nella transazione $(1)$ - e la inviasse alla rete Bitcoin, successivamente per spendere l'output contenuto nella transazione $(2)$ Alice avrebbe bisogno della collaborazione di Bob, perchè bisognerebbe inviare alla rete una transazione firmata sia con **skA**, che è nota solo ad Alice, che con **skB**. che è nota solo a Bob.
Quindi Alice starebbe bloccando i suoi $10$btc in un output che non potrebbe più spendere senza la collaborazione di Bob.

Prima di inviare la *FundingTx* in $(2)$, Alice però genera una nuova coppia di chiavi **skAr0** e
**pkAr0** e costruisce anche la transazione seguente, che chiamiamo *refunding transaction* per ragioni che dovrebbero cominciare a chiarirsi, e chiede a Bob di firmarla con la sua **skB**

![[Pasted image 20250527151636.png|center]]

La transazione in $(3)$ spende l'output della transazione in $(2)$, che Alice non ha ancora inviato nella rete Bitcoin, e ha un unico output che è spendibile o da Alice,$n$ blocchi dopo che la transazione sia stata inserita nella Blockchain, oppure da chi conosce **skAr0** (che per il momento conosce solo Alice) e **skB** (che conosce solo Bob)

Osserviamo che nel momento in cui Alice ha in mano la *refunding transaction* in $(3)$ firmata da Bob con **skB**, può tranquillamente inviare alla rete Bitcoin la *funding transaction* in $(2)$: Se Bob non dovesse collaborare nel momento in cui Alice volesse spendere i $10$btc nell’output della *funding transaction* in $(2)$, Alice potrebbe firmare la *refunding transaction* in $(3)$ anche con **skA1** e inviarla alla rete Bitcoin, aspettare $n$ blocchi dopo che la transazione sia stata inserita nella Blockchain e poi spenderne l’output.

L’invio della *funding transaction* alla rete Bitcoin costituisce l’*apertura di un canale di pagamento* fra Alice e Bob, finanziato con $10$btc da Alice. 

L’esistenza della *refunding transaction* nelle mani di Alice con la firma di Bob è la garanzia, per Alice, che può tornare in possesso esclusivo dei suoi $10$btc in qualunque momento. 
La condizione per spendere l’output della refunding transaction relativa alle chiavi pubbliche **pkAr0** e **pkB** fa sì che la transazione sia, di fatto, *revocabile* da Alice.

Nella prossima sezione vedremo come, e perchè questo è necessario.
## Canali di pagamento : Aggiornamenti di bilancio del canale

Supponiamo che Alice voglia acquistare da Bob qualcosa del valore di $2$btc. 
Vediamo come è possibile fare in modo di modificare il ***bilancio*** del canale fra Alice e Bob, che attualmente è $10$ per Alice e $0$ per Bob, in $8$ per Alice e $2$ per Bob.

Alice e Bob generano due nuove coppie di chiavi, rispettivamente (**skAr1**, **pkAr1**) viene generata da Alice e (**skBr1**, **pkBr1**) viene generata da Bob, e costruiscono le due transazioni seguenti, che chiamiamo *Commit Transaction 1*.

Entrambe le transazioni sono progettate per spendere l’output della *funding transaction* in $(2)$.

![[Pasted image 20250527152439.png|center|600]]

La transazione *CommitTx1 - Alice* è nelle mani di Alice e deve essere firmata da Bob con **skB**,la transazione *CommitTx1 - Bob* è nelle mani di Bob e deve essere firmata da Alice con **skA**.

Si osservi che in questo modo sia Alice che Bob hanno in mano una transazione che potrebbero ***unilateralmente*** firmare e inviare alla rete Bitcoin, la transazione creerebbe due output, di cui $8$btc potrebbero essere spesi da Alice e $2$btc da Bob. 
Se Alice inviasse la sua *CommitTx1 - Alice*, allora Alice dovrebbe aspettare $n$ blocchi prima di poter spendere i suoi $8$btc, mentre Bob potrebbe spendere i suoi $2$btc subito.

Viceversa, se fosse Bob a inviare la sua *CommitTx1 - Bob* alla rete, Bob dovrebbe aspettare $n$ blocchi prima di poter spendere i suoi $2$btc, mentre Alice potrebbe spendere i suoi $8$btc subito.

Si osservi che Alice ha ancora in mano la *RefundingTx* in $(3)$ firmata da Bob che assegna $10$btc ad Alice e $0$ a Bob.
Cosa impedisce ad Alice di inviare questa transazione alla rete Bitcoin?

Qui entra in gioco il ruolo della seconda condizione dell’output: prima che l’update del bilancio da Alice:$10$ - Bob:$0$ a Alice:$8$ - Bob:$2$ si possa considerare concluso, Alice deve rivelare a Bob la chiave segreta **skAr0** (quella che corrisponde alla chiave pubblica contenuta nell’output delle *RefundingTx*). 

Se Bob conosce **skAr0**, Alice non può più inviare la *RefundingTx* in $(3)$ alla rete Bitcoin, perchè se lo facesse dovrebbe aspettare $n$ blocchi prima di poter spendere i $10$btc nell’output, ma nel frattempo Bob potrebbe immediatamente spendere quei $10$ btc inviandoli a una chiave sotto il suo controllo esclusivo e lasciando Alice senza nulla.

Si noti che dal punto di vista della rete Bitcoin, l’unica transazione visibile è la *FundingTx* che deve essere inserita nella Blockchain e segna l’apertura del canale. 

Tutti gli altri passaggi intermedi, finchè una delle due parti o entrambe non decidono di ***chiudere*** il canale effettuando una transazione che spende l’output della *FundingTx*, restano scambi di messaggi privati fra le due parti

