# 1. Introduzione ai Protocolli Sigma

Prima di affrontare il protocollo di Schnorr, il capitolo introduce il concetto più generale di **Protocolli Sigma** ($\Sigma$-protocols). Questi sono una classe di protocolli interattivi a tre passaggi tra un Prover (P) e un Verifier (V), caratterizzati da:

- **Commitment (Impegno):** P invia un messaggio di impegno a V.
- **Challenge (Sfida):** V invia una sfida casuale a P.
- **Response (Risposta):** P invia una risposta a V.

I Protocolli Sigma sono noti per godere di tre proprietà fondamentali:

- **Completezza (Completeness):** Se il Prover conosce il segreto e segue il protocollo, il Verifier accetterà sempre la prova.
- **Robustezza della Conoscenza (Soundness of Knowledge):** Se il Verifier accetta la prova, allora il Prover deve effettivamente conoscere il segreto (o potrebbe essere "estratto" il segreto da un Prover malevolo che riesce a ingannare il Verifier). Questa proprietà è cruciale per i protocolli di identificazione.
- **Conoscenza Zero (Zero-Knowledge):** Il Verifier non apprende alcuna informazione sul segreto del Prover oltre al fatto che il Prover lo possiede. Questa è la proprietà distintiva che rende questi protocolli "a conoscenza zero". Spesso si parla di "conoscenza zero onesta del Verifier" (honest-verifier zero-knowledge), il che significa che un Verifier che segue onestamente il protocollo non apprende nulla.

# 2. Il Protocollo di Identificazione di Schnorr

Il protocollo di Schnorr è un esempio paradigmatico di protocollo Sigma, specificamente progettato per dimostrare la **conoscenza di un logaritmo discreto**. È ampiamente utilizzato come base per schemi di identificazione e firma.

**Scenario:** Un Prover (P) vuole dimostrare a un Verifier (V) di conoscere un segreto $x$, tale che $h = g^x$, dove $g$ è un generatore di un gruppo ciclico $G$ di ordine primo $q$, e $h$ è la chiave pubblica corrispondente.

**Passaggi del Protocollo:**

1. **Paso 1 (Commitment - Impegno):**
    - P sceglie un numero casuale $r$ (detto "nonce" o "witness") da $Z_q$.
    - P calcola $A = g^r$.
    - P invia $A$ a V.
    - _Significato:_ $A$ è un "impegno" al valore $r$, che P userà nella risposta.
2. **Paso 2 (Challenge - Sfida):**
    - V sceglie un numero casuale $c$ (la "sfida") da $Z_q$.
    - V invia $c$ a P.
    - _Significato:_ La casualità di $c$ impedisce a P di precalcolare la risposta e ingannare V.
3. **Paso 3 (Response - Risposta):**
    - P calcola $z = r + c \cdot x\mod q$.
    - P invia $z$ a V.
    - _Significato:_ $z$ lega il nonce $r$ al segreto $x$ e alla sfida $c$.
4. **Paso 4 (Verification - Verifica):**
    - V verifica se l'uguaglianza $g^z = A \cdot h^c$ è valida.
    - Se l'uguaglianza è vera, V accetta la prova; altrimenti, la rifiuta.
    - _Dimostrazione dell'uguaglianza:_ $g^z = g^{(r + c\cdot x)} = g^r \cdot g^{(c\cdot x)} = g^r \cdot (g^x)^c = A \cdot h^c$. Questa uguaglianza è valida solo se P conosce $x$.

**Proprietà Chiave del Protocollo di Schnorr:**
- **Identificazione:** Permette a un utente di autenticarsi dimostrando la conoscenza di un segreto.
- **Conoscenza Zero:** Il Verifier non apprende `x`. Se si volesse estrarre `x`, si dovrebbe "riavvolgere" il Prover e porgli due sfide diverse per lo stesso impegno iniziale, il che è possibile solo in un'analisi teorica (simulazione).
- **Robustezza della Conoscenza:** Se un Prover può convincere il Verifier con probabilità non trascurabile, allora esiste un "estrattore" che può ricavare il segreto `x` dal Prover.

# 3. Firme di Schnorr

Le firme di Schnorr sono una delle applicazioni più importanti e pratiche del protocollo di identificazione. Trasformano il protocollo interattivo in uno schema di firma digitale non interattivo utilizzando la **trasformazione di Fiat-Shamir**.

Trasformazione di Fiat-Shamir:

Questa tecnica converte un protocollo interattivo a conoscenza zero in un protocollo non interattivo sostituendo la sfida casuale del Verifier con l'output di una funzione hash crittografica applicata ai messaggi precedenti del protocollo e al messaggio da firmare.

**Schema di Firma di Schnorr:**

1. **Generazione delle Chiavi:**
    - Si scelgono parametri di gruppo pubblici ($G$, $q$, $g$).
    - L'utente (firmatario) sceglie una chiave privata $x$ casuale da $Z_q$.
    - Calcola la chiave pubblica $h = g^x$.
2. **Firma (di un messaggio `m`):**
    - Il firmatario sceglie un nonce casuale $r$ da $Z_q$.
    - Calcola $A = g^r$.
    - Calcola la sfida $c = H(m || A)$, dove $H$ è una funzione hash crittografica (spesso modellata come un random oracle) e $||$ denota la concatenazione.
    - Calcola la risposta $z = r + c \cdot x \mod q$.
    - La firma è la coppia $(c, z)$. (A volte la firma è $(A, z)$ e $c$ viene ricalcolato dal verificatore).
3. **Verifica (di un messaggio `m` con firma `(c, z)` e chiave pubblica `h`):**
    - Il verificatore calcola $A' = g^z \cdot h^{-c}$.
    - Il verificatore calcola $c' = H(m || A')$.
    - La firma è valida se $c' = c$.
    - _Dimostrazione dell'uguaglianza:_ Se la firma è valida, $g^z = g^{(r + c\cdot x)} = g^r \cdot g^{(c\cdot x)} = A \cdot (g^x)^c = A \cdot h^c$. Quindi $g^z \cdot h^{-c} = A$. Ricalcolando $c'$ con $A$ si ottiene l'originale $c$.

**Proprietà di Sicurezza delle Firme di Schnorr:**

- **Autenticità:** Solo chi conosce la chiave privata `x` può generare una firma valida per un messaggio.
- **Integrità:** Qualsiasi modifica al messaggio `m` o alla firma `(c, z)` renderà la verifica non valida.
- **Non Ripudiabilità:** Il firmatario non può negare di aver generato la firma, poiché è legata alla sua chiave privata.
- **Sicurezza:** La sicurezza delle firme di Schnorr è dimostrabile sotto l'assunzione della difficoltà del problema del logaritmo discreto (DLP) nel modello dell'oracolo casuale.
# 4. Aspetti Avanzati e Considerazioni

Il capitolo potrebbe anche toccare aspetti più avanzati:

- **Modello dell'Oracolo Casuale:** La discussione sulla sicurezza delle firme di Schnorr si basa spesso sul modello dell'oracolo casuale, che è una potente astrazione teorica per le funzioni hash. Il capitolo potrebbe discutere i pro e i contro di questa astrazione.
- **Estrazione del Conoscitore (Knowledge Extractor):** Il concetto di "estrattore" è fondamentale per dimostrare la robustezza della conoscenza. Si tratta di un algoritmo che, data la capacità di un Prover di convincere il Verifier, può effettivamente "estrarre" il segreto che il Prover afferma di conoscere.
- **Varianti e Applicazioni:**
    - **Firme Aggregate/Multifirme (Multi-signatures/Aggregate Signatures):** Le firme di Schnorr sono particolarmente adatte per la creazione di schemi in cui più parti possono collaborare per produrre una singola firma valida per un messaggio (es. MuSig).
    - **Prove di Conoscenza Non Interattive (NIZK):** La trasformazione di Fiat-Shamir è un metodo generale per costruire NIZK, e Schnorr è un esempio chiave.
    - **Applicazioni in Blockchain:** Le firme di Schnorr sono diventate popolari in contesti di criptovalute (es. Bitcoin con Taproot) per la loro efficienza, la compatibilità con le multifirme e la loro robustezza.
