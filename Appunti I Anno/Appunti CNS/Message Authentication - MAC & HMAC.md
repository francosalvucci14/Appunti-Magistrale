# Message Authentication Codes (MAC) e Integrità dei Dati

## 1. Introduzione: Integrità vs Confidenzialità

In ambito di sicurezza delle reti, è fondamentale distinguere tra due concetti che spesso vengono confusi: confidenzialità e integrità.

- **Confidenzialità:** Si occupa di nascondere il messaggio. Garantisce che solo il destinatario legittimo possa leggere il contenuto.
    
- **Integrità:** Si occupa dell'autenticità del messaggio. Garantisce che nessuno abbia modificato il messaggio durante la trasmissione e che solo la sorgente legittima possa averlo generato.
    

Un principio cardine è che la cifratura (Encryption) NON garantisce l'integrità. Un attaccante potrebbe modificare un messaggio cifrato in transito; anche se il risultato decifrato fosse privo di senso ("garbage"), il sistema ricevente potrebbe non accorgersene o, peggio, la modifica potrebbe risultare in un messaggio valido ma alterato (malleabilità).

Eccezione: Solo i cifrari AEAD (Authenticated Encryption with Associated Data) sono progettati per garantire contemporaneamente entrambe le proprietà.

![center|600](MA_sk1.png)

Dove:
- $k$ è il segreto conosciuto sia dal sender che dal receiver
- Generate-Tag è una funzione **crittograficamente forte** : prende in input $K$ e il msg, e come output da un codice di autenticazione relativamente "corto" (tag, comunque più corto dell'input)
	- perchè è forte? perchè non è reversibile! (per prendere la chiave devo fare **brute-force**)
	- è anche corretto chiamare il tag la **firma del messaggio** (da non confondere con la firma digitale, che è un'altra cosa)

**Esempio** : MSG = 10K bits, K=128 bits -> Generate-Tag ritorna un tag tale per cui $|TAG|\lt\lt10k$ 
## 2. Requisiti per l'Autenticazione dei Messaggi (Stallings Cap. 12)

Secondo Stallings, i meccanismi di autenticazione devono proteggere contro diverse minacce.

Ci sono però minacce che possono essere risolte con la Message Authentication, ed altre no

Alcune minacce risolte sono il MITM e il M.Spoofing

**Attacchi MITM (Man in The Middle)** : Un'entità non autorizzata legge il messaggio e lo modifica
Perchè la MA protegge da attacchi di questo tipo?
Analizziamo:
- l'attaccante può modificare tranquillamente il messaggio, però accadono le seguenti cose:
	- Lui vede sia $m$ che TAG, ma essendo $F$ la funzione "crittograficamente" forte, lui non potrà invertire $F$ per ottenere $K$
		- Ovviamente la dimensione della chiave deve essere "sufficientemente lunga", al giorno d'oggi almeno $128$ bits, quindi per trovare la chiave devo fare brute-force, e con $128$ bits abbiamo un numero di "prove" pari circa a $\frac{2^{128}}{2}$
	- Senza conoscere $K$, l'attaccante non può cambiare il TAG in TAG$^{\star}=F(K,m^{\star})$
	- E infine, non potrà cambiare $m$ in $m^{\star}$ in modo tale che $F(K,m)=F(K,m^{\star})$
- Il ricevente vede quindi $m^{\star}$ al posto di $m$, però quando poi si va a calcolare $F(K,m^{\star})=TAG^{\star}\neq TAG$ capisce che qualcuno ha modificato l'attacco.
	- La probabilità che TAG$^\star$ sia diverso da TAG originale è $\frac{1}{2^{|TAG|}}$, per questo motivo la funzione $F$ deve generare TAG che siano grandi

![center|500](MAC_MITM.png)

**Message Spoofing**: Un'entità non autorizzata finge di essere una sorgente valida.
Ipotizziamo che l'attaccante crei un messaggio personalizzato $X$, e trovi un modo per generare una firma valida per il messaggio (ovvero il TAG) (questa proprietà, se vale, viene chiamata **Forgiability**)
Ora, per le assunzioni fatte sulla funzione $F$, vale che $F$ garantisce la **non-Forgiability**, di conseguenza l'attaccante non potrà calcolare $F(K,X)$ senza conoscere $K$, e quindi il TAG che arriverà sarà un TAG invalido
Il ricevente può controllare questa cosa, e potrà accorgersi che il messaggio è stato *falsificato*

![center|500](MAC_MSpoof.png)

Un'esempio di minaccia che il MA non risolve è il così detto **Replay Attack**: i messaggi vengono ritardati o replicati.
Perchè non protegge? Analizziamo
Supponiamo di voler pagare $1000\$$ in una transazione, e un secondo dopo voglia ripagare altri $1000\$$ (es. compro due telefoni)
Dato che i messaggi sono *esattamente* gli stessi, e la chiave è **costante** nel tempo, allora il TAG risulterà essere lo stesso.

Ora l'attaccante può prendere il primo msg, copiarlo, e rimandarlo in un secondo momento alla, in questo caso, banca.
Così facendo, l'attaccante farà in modo che la vittima paghi più volte del dovuto

![center|600](MAC_RepAtt.png)

Per prevenire i replay attack, è necessario introdurre un **Nonce** (Number used ONCE), un valore che cambia per ogni messaggio e viene incluso nel calcolo del MA.

![center|600](MAC_NONCE.png)

Ci sono $3$ tipi di **Nonce**

| **Tipo di Nonce**   | **Descrizione**                         | **Vantaggi**                                     | **Svantaggi**                                                                              |
| ------------------- | --------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Sequence Number** | Un contatore incrementale ($N_x, N_y$). | Semplice da implementare.                        | Gestione complessa in caso di riavvio (reboot) o perdita di sincronizzazione.              |
| **Random Number**   | Un valore casuale grande.               | Non richiede stato o sincronizzazione temporale. | Il ricevente deve mantenere uno storico dei nonce visti per evitare duplicati (Windowing). |
| **Timestamp**       | L'orario corrente.                      | Previene replay ritardati significativamente.    | Richiede sincronizzazione degli orologi sicura e affidabile.                               |

Il calcolo del TAG diventerà quindi: $Tag = F(K, M || Nonce)$.

Osserviamo che nessuna di queste è meglio dell'altra
## 3. Message Authentication Code (MAC)

Prima di parlare dei MAC, dobbiamo vedere quali differenze si porta con le Firme Digitali (DS)

La firma digitale impone che **nessuno** può modificare un messaggio firmato digitalmente (ad eccezzione del creatore)
Il MAC impone che **nessuno eccetto Sender e Receiver** (che hanno la chiave) può modificare un messaggio autenticato con MAC
Entrambi quindi hanno lo stesso identico scopo, ovvero proteggerò l'integrità dei dati/messaggi
Però, a differenza del MAC, le DS garantiscono anche il non-ripudio (ovvero l'autenticazione della sorgente)
- abbiamo quindi che le DS sono una forma di autenticazione **più forte** dei MAC, ma richiedono nozioni di crittografia diverse, ovvero la crittografia asimmetrica

Vediamo ora nel dettaglio i MAC

Un MAC è un blocco di dati di dimensione fissa, noto come _tag_ crittografico, generato basandosi sul messaggio e su una chiave segreta.

![center|500](MAC.png)

### 3.1 Definizione Formale

Un MAC richiede tre elementi:

1. **Messaggio ($M$):** Di lunghezza arbitraria.
    
2. **Chiave Segreta ($K$):** Condivisa tra mittente e destinatario.
    
3. **Funzione MAC ($F$):** Una funzione crittograficamente forte che mappa $K$ e $M$ in un tag di lunghezza fissa.

La sicurezza dei MAC deriva dalla proprietà, descritta prima, della **non falsificabilità** (unforgeability): l'attaccante non deve essere in grado di creare/modificare un messaggio; questo implica che l'attaccante non deve essere in grado di estrarre la chiave dalla coppia $\{M,TAG(K,M)\}$


Il processo è il seguente:

- **Generazione:** Il mittente calcola $Tag = F(K, M)$ e invia $(M, Tag)$ .
- **Verifica:** Il destinatario riceve $(M', Tag')$, calcola $Tag_{calc} = F(K, M')$ e lo confronta con $Tag'$. Se coincidono, il messaggio è autentico .

### 3.2 Sicurezza del MAC

\- Gemini \-
La sicurezza di un MAC si basa sul fatto che è computazionalmente impossibile per un attaccante (che non possiede $K$) calcolare un tag valido per un messaggio $M^*$ o modificare $M$ in $M^*$ mantenendo valido il tag originale.

\- Bianchi \-
La sicurezza dei MAC deriva dalla proprietà, descritta prima, della **non falsificabilità** (unforgeability): l'attaccante non deve essere in grado di creare/modificare un messaggio; questo implica che l'attaccante non deve essere in grado di estrarre la chiave dalla coppia $\{M,TAG(K,M)\}$

Questo modello implica che il MAC protegge dagli attacchi Man-In-The-Middle (MITM) che tentano di modificare il payload.

---
Però, questa benedetta funzione $F$ come deve essere?
Per rispondere a questa domanda ci vengono in aiuto le funzioni Hash, e più nel dettaglio le funzioni Hash Crittografiche
Prima di parlare quindi di HMAC, facciamo prima una piccola digressione su cosa sono le Hash Crittografiche e come funzionano

## Interludio: Hash e Hash Crittografiche 

Prima di tutto, cos'è una funzione Hash?
Una funzione Hash è una funzione che prende in input un messaggio $X$ di lunghezza arbitraria (ovvero da $1$ bit a qualunque dimensione), e ritorna un'altro messaggio $Y=H(X)$ di lunghezza ***fissata*** (es. esattamente $256$ bits se si usa SHA-$256$)

![center|600](Hash1.png)

La stringa $Y=H(X)$ viene anche chiamata "fingerprint" (riepilogo corto) di $X$
La funzione $H(X)$ deve essere relativamente facile da calcolare per ogni $X$ dato

E cosa cambia con una funzione Hash **Crittografica**? 
Una funzione Hash Crittografica funziona esattamente come le Hash normali, con la differenza che, se prendiamo $X$, generiamo $Y=H(X)$ e poi modifichiamo $X$ in $X^{\star}$ (ad esempio cambiando qualche carattere nel messaggio), applicando la *stessa* Hash Crittografica applicata ad $X$, quello che otterremo sarà un rislutato completamente diverso $$Y^{\star}=H(X^\star),Y^{\star}\neq Y\quad(\text{sotto ogni punto di vista})$$
![center|500](HashC1.png)

Le H.C. però non hanno solo questa caratteristica, ma hanno altre bellissime proprietà che ci serviranno più avanti per i MAC

- **Preimage resistance (one-way)**: Dato $Y$ il risultato dell'hash, deve essere difficile trovare un qualunque $X$ tale per cui $X=H(Y)$; quindi da $Y$ non devo poter essere in grado di risalire a $X$ ![center|300](HC_digest.png)
- **Second Preimage Resistance** : Dato $X$, deve essere difficile trovare un'altro $X^{\star}$ tale che $H(X)=H(X^{\star})$
- 

>Vedi esercizio esame su registrazione a 1.15.20


## 4. MAC basati su Funzioni Hash (HMAC)

Stallings (Cap. 12.4) e le slide dedicano ampia parte all'utilizzo delle funzioni Hash per costruire MAC.

### 4.1 Perché non usare Hash semplici?

Una funzione hash crittografica $H(M)$ garantisce l'impronta digitale, ma non l'autenticazione, perché chiunque può calcolare l'hash di un messaggio modificato. È necessario includere la chiave segreta $K$.

Tuttavia, le costruzioni "ingenue" sono insicure a causa della struttura iterativa (Merkle-Damgård) delle funzioni hash comuni (MD5, SHA-1, SHA-2).

#### L'Attacco di Estensione della Lunghezza (Length Extension Attack)

Consideriamo la costruzione Secret Prefix: $Tag = H(K || M)$.

Le funzioni hash operano a blocchi. Lo stato interno dell'hash dopo aver processato $K || M$ è l'output finale dell'hash originale. Un attaccante può prendere l'hash legittimo e usarlo come stato iniziale per processare un blocco aggiuntivo (estensione), calcolando un nuovo hash valido per il messaggio $M || Padding || Estensione$ senza conoscere $K$ .

Questo rende insicuri i MAC costruiti come $H(K || M)$ .

Anche la costruzione **Secret Suffix** $H(M || K)$ è vulnerabile a collisioni sul messaggio che si riflettono sul MAC, anche se resiste all'estensione.

### 4.2 HMAC: La Soluzione Standard

Per risolvere questi problemi, nel 1996 è stato introdotto HMAC (RFC 2104), standardizzato anche dal NIST.

HMAC utilizza una struttura a due passaggi ("nested") che impedisce gli attacchi di estensione e isola l'uso della chiave .

#### Algoritmo HMAC

HMAC tratta la funzione hash $H$ come una "scatola nera". Definisce due costanti:

- **ipad (inner pad):** $0x36$ ripetuto.
    
- **opad (outer pad):** $0x5C$ ripetuto.
    

La formula è:

$$HMAC(K, M) = H((K^+ \oplus opad) || H((K^+ \oplus ipad) || M))$$

Dove $K^+$ è la chiave $K$ riempita con zeri (padding) fino alla dimensione del blocco della funzione hash .

**Funzionamento Logico:**

1. Si deriva una chiave interna $K_{in} = K^+ \oplus ipad$.
    
2. Si calcola l'hash interno: $Hash_{in} = H(K_{in} || M)$.
    
3. Si deriva una chiave esterna $K_{out} = K^+ \oplus opad$.
    
4. Si calcola l'hash finale: $Tag = H(K_{out} || Hash_{in})$ .
    

Questa struttura "blocca" il risultato dell'hash interno all'interno di un secondo hash, rendendo impossibile l'attacco di estensione della lunghezza. La sicurezza di HMAC è dimostrabile ed è legata alla pseudocasualità della funzione hash sottostante, non necessariamente alla sua resistenza alle collisioni.

![center](HMAC_struc.png)


---

## 5. MAC basati su Cifrari a Blocchi (DAA e CMAC)

Stallings (Cap. 12) discute approfonditamente l'uso dei cifrari a blocchi (come AES o DES) per creare MAC. Le slide accennano a questo concetto ma il libro fornisce i dettagli algoritmici.

### 5.1 DAA (Data Authentication Algorithm)

Storicamente, uno dei primi standard (FIPS 113) era il DAA, basato su **DES in modalità CBC (Cipher Block Chaining)**.

- Si cifra il messaggio con DES-CBC usando la chiave $K$ e un Vettore di Inizializzazione (IV) nullo.
    
- Il MAC è costituito dall'ultimo blocco del testo cifrato (o parte di esso).
    
- **Problema:** DAA ha problemi di sicurezza legati alla dimensione ridotta del blocco DES (64 bit) e limitazioni prestazionali.
    

### 5.2 CMAC (Cipher-based Message Authentication Code)

Per superare i limiti del DAA e gestire messaggi di lunghezza arbitraria senza vulnerabilità, il NIST ha standardizzato **CMAC** (SP 800-38B). CMAC può essere utilizzato con AES o Triple DES.

Funzionamento di CMAC:

CMAC risolve il problema dell'ultimo blocco di dimensione variabile introducendo due sotto-chiavi ($K_1, K_2$) derivate dalla chiave principale $K$.

1. Viene applicato l'algoritmo di cifratura (es. AES) a un blocco di zeri per generare $L$.
    
2. $K_1$ e $K_2$ sono derivati da $L$ tramite operazioni di shift a sinistra e XOR condizionale con una costante (dipendente dal polinomio irriducibile del campo di Galois).
    
3. Il messaggio viene diviso in blocchi.
    
    - Se l'ultimo blocco è completo, viene messo in XOR con $K_1$ prima dell'ultima cifratura.
        
    - Se l'ultimo blocco è incompleto, viene fatto il padding, poi XOR con $K_2$.
        
4. Il risultato è l'autenticazione sicura anche per messaggi di lunghezza variabile, prevenendo attacchi di estensione tipici del semplice CBC-MAC.
    

---

## 6. Authenticated Encryption (AE)

Un'evoluzione moderna discussa sia nelle slide che in Stallings (Cap. 12.6) è l'Authenticated Encryption.

Spesso si vuole sia confidenzialità che integrità. Combinare separatamente Cifratura e MAC (es. Encrypt-then-MAC, MAC-then-Encrypt) può portare a errori implementativi fatali (vedi attacchi di oracolo di padding su SSL/TLS).

I modi operativi **AEAD** risolvono questo problema integrando le due funzioni:

1. **CCM (Counter with CBC-MAC):** Combina la modalità CTR per la confidenzialità e CBC-MAC per l'autenticazione. Usato nel WiFi (WPA2).
    
2. **GCM (Galois/Counter Mode):** Combina la modalità CTR per la confidenzialità e una funzione di hash basata su campi di Galois (GHASH) per l'autenticazione. È molto efficiente in hardware e software parallelo.
    

---

## 8. Conclusioni e Best Practices

1.  **Non inventare crittografia:** Mai usare funzioni Hash "così come sono" per l'autenticazione o tentare di inserire la chiave in modi creativi (es. $H(M||K)$) .
    
2. **Usare Standard:** Utilizzare **HMAC-SHA256** o **AES-CMAC** per l'integrità pura. Utilizzare **AES-GCM** se serve anche confidenzialità.
    
3. **Gestione Replay:** Implementare sempre Timestamp o Numeri di Sequenza nei protocolli di autenticazione per prevenire il riutilizzo dei messaggi validi.
    
4. **Verifica a Tempo Costante:** La verifica del tag deve avvenire in tempo costante per evitare attacchi laterali (timing attacks) che potrebbero rivelare il contenuto del tag byte per byte.

