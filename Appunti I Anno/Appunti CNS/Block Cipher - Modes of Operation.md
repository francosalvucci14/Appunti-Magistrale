# Cifrari a Blocchi e Modalità di Operazione

In questo modulo abbandoniamo l'idea di cifrare bit per bit (Stream Ciphers) per passare all'elaborazione di blocchi di dati di dimensione fissa. Analizzeremo perché un algoritmo di cifratura da solo (come AES) non è sufficiente e necessita di una "Modalità di Operazione" per essere sicuro e utile.

---

## 1. Fondamenti Teorici: Il Cifrario a Blocchi

Un cifrario a blocchi è una primitiva crittografica che opera su blocchi di testo in chiaro 
($P$) di lunghezza fissa $n$ (es. 128 bit per AES) e produce blocchi di testo cifrato ($C$) della stessa lunghezza $n$, utilizzando una chiave $K$.

![center|500](BlockCipher1.png)

Il loro goal è quello di andare "generalizzare" i cifrari a sostituzione
### 1.1 Definizione come PRP (Pseudo-Random Permutation)

Dal punto di vista matematico, un cifrario a blocchi ideale modella una **Permutazione Pseudo-Casuale (PRP)**.

- **Permutazione:** È una funzione biiettiva (invertibile) $E: \{0,1\}^n \to \{0,1\}^n$. Mappa ogni possibile input in un unico output e viceversa.
- **Pseudo-Casuale:** La permutazione specifica scelta dalla chiave $K$ deve essere indistinguibile da una permutazione scelta uniformemente a caso dall'insieme di tutte le permutazioni possibili.

Un'esempio con $n=3$ bits

![center|600](PRP.png)

### 1.2 Lo Spazio delle Permutazioni (Perché serve la Chiave?)

Se operiamo su blocchi di $n=3$ bit, l'insieme dei possibili messaggi $S$ ha dimensione $2^3 = 8$.
Quante permutazioni possibili esistono su 8 elementi? Sono $8! = 40320$.

Tuttavia, quando $n$ cresce, il numero esplode.

Per **AES (Advanced Encryption Standard)** ($n=128$), il numero di possibili permutazioni è $2^{128}!$ (fattoriale).

Utilizzando l'approssimazione di Stirling, questo numero è circa $2^{2^{135}}$, una cifra inimmaginabilmente grande (una chiave per selezionare una permutazione da questo insieme richiederebbe $10^{40}$ cifre) .

Poiché non possiamo gestire tutte queste permutazioni, la **Chiave $K$** (es. 128 o 256 bit) serve a selezionare un sottoinsieme molto piccolo ma "ben distribuito" di queste permutazioni. Anche se $2^{256}$ è molto minuscolo rispetto a $2^{128}!$, è sufficiente per la sicurezza pratica.
Le permutazioni di AES sono molto meno del PRP ideale, ma vanno ancora bene dal punto di vista crittografico

---

Partiamo subito con i primi problemi dell'approccio Block Cipher
## 2. Il Fallimento dell'Approccio Ingenuo: ECB

La modalità più semplice e intuitiva per cifrare un messaggio lungo è dividerlo in $n$ blocchi e cifrare ciascuno separatamente con la stessa chiave. 
Questa modalità è chiamata **Electronic Code Book (ECB)**.

![center|600](ECB1.png)

Come possiamo vedere in figura, il messaggio originale viene diviso in $n$ chunks
Ogni chunk viene passatto alla funzione PRP, con chiave $K$ (notiamo che $K$ è uguale per tutti), e viene generato il testo cifrato relativo a quel blocco (es. $c[0]$ è il ciphertext del blocco $m[1]$)

Abbiamo quindi una cifratura indipendente per ogni blocco

Questo approccio però porta con se un problema molto imporante
### 2.1 Funzionamento e Debolezza

Come abbiamo detto, e come si vede dalla figura, quello che avviene per ogni blocco del messaggio è la seguente operazione:
$$C_i = ENC(K, P_i)$$
Dove sta il problema di ECB? sembra abbastanza sicuro!
Il problema fatale di ECB è che è deterministico.

- Se nel messaggio appare due volte lo stesso blocco di testo in chiaro (es. "CIAO" e poi di nuovo "CIAO"), verrà prodotto due volte lo stesso identico blocco di testo cifrato. ![center](ECB2.png)
- **Analisi del Traffico:** Un attaccante vede pattern ripetuti nel ciphertext e deduce pattern nel plaintext .

**Esempio Visivo (Il Pinguino):** Se cifriamo un'immagine bitmap in ECB, le aree di colore uniforme (es. lo sfondo bianco o la pancia del pinguino) generano blocchi cifrati identici. L'immagine cifrata mostra ancora chiaramente i contorni della figura originale. **ECB non garantisce la sicurezza semantica.** .

---

Un'altro problema con i block cipher è il seguente
## 3. Initialization Vector (IV) e Randomizzazione

Per ottenere la sicurezza semantica (IND-CPA), dobbiamo garantire che cifrare due volte lo stesso messaggio produca due ciphertext diversi.

![center|600](ECB3.png)

Come visto negli Stream Ciphers, introduciamo un Initialization Vector (IV).

L'IV deve essere un valore casuale (nonce) che non si ripete mai per la stessa chiave.
- ricordare la differenza con SHA-$256$, qui gli IV sono ***CASUALI***, in SHA-$256$ gli IV sono ***COSTANTI***

Lo schema di questo approccio è il seguente:
1. Eseguo lo XOR $\oplus$ del mio plaintext con il valore IV, passo poi il risultato alla funzione PRP con chiave $K$, e ottengo il ciphertext corrispondente ![center](IV_BC1.png)
2. Per trasmettere il messaggio semplicemente inviamo sia il ciphertext appena generato sia il valore IV che abbiamo usato ![center](IV_BC2.png)
3. Per decifrare il messaggio appena ricevuto, prendo il ciphertext e lo passo all'***inversa*** della funzione PRP, sempre con chiave $K$, e del risultato ne faccio lo XOR insieme al valore di IV ricevuto, così facendo riottengo il plaintext originale ![center](IV_BC3.png)
Ora, la cosa su cui dobbiamo prestare attenzione è che gli IV NON si devono ripete, ma devono essere ANCHE non-predictabili (ovvero un valore random **vero**, che mai si ripete)

>Rivedi esempio/esercizio a 0.39.34 Lezione 9

---

Abbiamo visto quindi che con i block cipher ci sono $2$ grossi problemi, che sono il dividere il messaggio quando la sua dimensione supera quella dei blocchi (es. 128 in AES), e garantire che ad ogni cifratura dello stesso messaggio bisogna ottenre un ciphertext diverso
Per venire in soccorso ai block cipher standard, sono stati inventati varie metodologie, chiamate "Modalità di Operazioni", che adesso vedremo.
## 4. Modalità di Operazione Sicure

Come abbiamo visto, se abbiamo solamente $1$ blocco (e solo in questo caso) possiamo usare ECB senza alcun problema
Se invece abbiamo messaggi ripetuti dobbiamo usare un initialization vector

Se però abbiamo molteplici messaggi, dobbiamo trovare un modo "sicuro" per combinare i blocchi, e qui ci vengono in aiuto le modalità di operazione sicure

Perchè sicure? perchè permettono di garantire la sicurezza semantica, ovvero rispettano e garantiscono la IND-CPA

Vediamo ora quali sono queste modalità

![center|500](ListModes.png)

I più usati sono:
- Cipher Block Chaining (CBC)
- Counter Mode (CTR)

I raccomandati dal NIST, che però non vengono molto usati nella pratica sono:
- Cipher Feedback Mode (CFB)
- Output Feedback Mode (OFB)

Altri che garantiscono altre proprietà più avanzate (quali confidentiality + integrity) sono:
- Galois Counter Mode (GCM)
- Offset Codebook Mode (OCB)
- etc...

La differenza sostanziale fra le prime due classi e l'ultima è che:
- le prime due garantiscono la IND-CPA
- l'ultima garantisce la IND-CCA, che è una versione più forte di sicurezza rispetto a IND-CPA, perchè garantisce sicurezza anche contro attaccanti attivi, e non solo da quelli passivi come IND-CPA
### 4.1 CBC (Cipher Block Chaining)

È la modalità storicamente più usata. L'idea è "concatenare" i blocchi in modo che la cifratura del blocco corrente dipenda da tutti i precedenti.

- Encryption: Prima di cifrare il blocco $P_i$, facciamo lo XOR con il testo cifrato precedente $C_{i-1}$. Per il primo blocco vale la seguente operazione: $$C_0 = ENC(K, P_0 \oplus IV)$$ ![center|600](CBC1.png)
Per ogni altro blocco vale questo: $$C_i = ENC(K, P_i \oplus C_{i-1})$$ ![center|600](CBC2.png)
In questo modo, anche se $P_1 = P_2$, l'input al cifrario sarà diverso perché $C_0 \neq C_1$ (grazie all'IV iniziale e alla diffusione) .
- Decryption: Per ogni blocco vale la seguente operazione: $$P_i = DEC(K, C_i) \oplus C_{i-1}$$ ![center|600](CBC3.png)


**Pro e Contro di CBC:**

- **(+) Sicurezza:** Standard robusto se l'IV è casuale e imprevedibile .
	- altrimenti, poter predirre gli IV porta ad attacchi di tipo CPA, come è avvenuto in TLS (TLS Beast Attack)
- **(-) Sequenziale:** La cifratura NON è parallelizzabile. Devi aver calcolato $C_1$ prima di calcolare $C_2$. Questo rallenta l'hardware ad alte prestazioni .
- **(-) Padding:** Richiede che il messaggio sia multiplo della dimensione del blocco. Serve uno schema di padding (es. PKCS#7) .
	- possibile attacco:  Padding Oracle Attack (usare il padding per rompere la cifratura)
- **(+-) Overhead** : Abbiamo solamente l'IV iniziale che è in più, e quindi marginale per quanto riguarda il peso di questo algoritmo 
- Un'altro problemino è che la cifratura e decifratura richiedono due circuiti diversi:
	- Enc = PRP, Dec = PRP$^{-1}$
	- le altre modalità, come CTR,CFB,OFB usano PRP sia per Enc che per Dec
- **Nota:** La decifratura è parallelizzabile (poiché conosci già tutti i $C_i$).
### 4.2 CTR (Counter Mode)

La modalità CTR trasforma un cifrario a blocchi in uno stream cipher. È la modalità preferita nei protocolli moderni (es. AES-GCM in TLS 1.3).

- Funzionamento: Non cifriamo direttamente il messaggio. Cifriamo un "Contatore" (che include l'IV) per generare un keystream, che poi viene messo in XOR col messaggio.
    
    $$Keystream_i = ENC(K, Nonce || Counter_i)$$
    
    $$C_i = P_i \oplus Keystream_i$$
    
    Il contatore viene incrementato per ogni blocco .
    

**Pro e Contro di CTR:**

- **(+) Performance:** Sia cifratura che decifratura sono **completamente parallelizzabili**. Possiamo pre-calcolare il keystream prima ancora che arrivi il messaggio.
    
- 
    
    **(+) Accesso Casuale:** Possiamo decifrare l'ultimo blocco del file senza decifrare quelli prima.
    
- 
    
    **(+) Niente Padding:** Poiché agisce come uno stream cipher (XOR), non serve padding; il ciphertext ha la stessa lunghezza del plaintext.
    
- **(!) Attenzione:** Mai riutilizzare la coppia $(Key, Nonce)$. Come per l'OTP, se il contatore si ripete, la sicurezza crolla catastroficamente.
    

### 4.3 CFB (Cipher Feedback) e OFB (Output Feedback)

Queste modalità trasformano il block cipher in stream cipher usando un registro a scorrimento.

- **OFB:** L'output del cifrario diventa l'input per il blocco successivo. Il keystream è indipendente dal messaggio. Genera un flusso sincrono.
    
    - 
        
        _Problema:_ Se l'IV è sfortunato, si può entrare in un "ciclo corto" (short cycle), ripetendo il keystream troppo presto .
        
- **CFB:** Il _ciphertext_ precedente diventa l'input per il blocco successivo. È "auto-sincronizzante" (se si perde un pezzo di ciphertext, l'errore si propaga solo per pochi blocchi poi si ristabilisce) .
    

---

## 5. Padding (Riempimento)

Poiché i cifrari a blocchi (in modalità ECB e CBC) richiedono input di lunghezza esatta (es. multipli di 16 byte), se il messaggio non raggiunge tale lunghezza, dobbiamo aggiungere dati extra.

- **PKCS#7 Padding:** È lo standard più comune. Se mancano $N$ byte per completare il blocco, aggiungiamo $N$ byte, ciascuno di valore $N$.
    
    - Esempio (mancano 4 byte): `... DATI 04 04 04 04`
        
    - Se il messaggio è già allineato, si aggiunge un intero blocco di padding (es. 16 byte di valore 16) per evitare ambiguità in decifratura.
        

---

## 6. Sintesi Comparativa

| **Modalità** | **Tipo**         | **Parallelizzabile (Enc)** | **Parallelizzabile (Dec)** | **Padding Richiesto?** | **Integrità?** | **Note**                                                             |
| ------------ | ---------------- | -------------------------- | -------------------------- | ---------------------- | -------------- | -------------------------------------------------------------------- |
| **ECB**      | Pattern insicuro | Sì                         | Sì                         | Sì                     | No             | **NON USARE MAI**. Preserva pattern visivi.                          |
| **CBC**      | Chaining         | No                         | Sì                         | Sì                     | No             | Standard storico. IV deve essere imprevedibile.                      |
| **CTR**      | Stream           | **Sì**                     | **Sì**                     | **No**                 | No             | **Standard Moderno**. Veloce, random access.                         |
| **OFB**      | Stream           | No                         | No                         | No                     | No             | Pre-computabile. Attenzione ai cicli.                                |
| **GCM**      | Authenticated    | Sì                         | Sì                         | No                     | **Sì**         | Evoluzione di CTR che aggiunge autenticazione (trattata in seguito). |

**Conclusione:** Per la sola confidenzialità ad alte prestazioni, **CTR** è la scelta eccellente. Se serve compatibilità legacy, CBC è accettabile (con IV corretti). Per sistemi moderni, si preferiscono modalità autenticate come **GCM** (Galois Counter Mode) che combinano CTR con un MAC per garantire sia confidenzialità che integrità.