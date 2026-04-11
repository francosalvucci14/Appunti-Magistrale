# Wild-Card Queries

Un motore di ricerca non deve solo trovare parole esatte, ma deve anche permettere all'utente di cercare "parole che iniziano per..." o "parole che finiscono per...". Queste sono le **Wildcard Queries** (ricerche con caratteri jolly, rappresentati dall'asterisco `*`)

La posizione dell'asterisco cambia drasticamente la difficoltà della ricerca:

- **Jolly alla fine (`mon*`):** È facilissimo. Se il dizionario è organizzato in ordine alfabetico usando un albero (B-tree), basta cercare tutte le parole comprese nel range tra `mon` e `moo`.
- **Jolly all'inizio (`*mon`):** Più difficile. I motori di ricerca risolvono questo problema mantenendo un _secondo_ B-tree con tutte le parole del dizionario scritte al contrario (backwards). Così, la ricerca `*mon` diventa una banale ricerca per `nom*` nell'albero rovesciato.
- **Jolly in mezzo (`co*tion`):** Questo è il vero problema. Potremmo cercare `co*` nel primo albero e `*tion` nel secondo albero e poi incrociare (intersect) le due liste risultanti. Tuttavia, questa operazione è disastrosamente lenta e costosa in termini di tempo di calcolo.

Per risolvere il problema del jolly in mezzo alla parola, sono state inventate due strutture dati apposite.
## Permuterm Index

L'idea geniale dell'indice Permuterm è **trasformare qualsiasi query in modo che l'asterisco si trovi sempre e solo alla fine**.

- **Come si costruisce:** Prendi ogni parola del dizionario (es. _hello_) e aggiungi un simbolo speciale di terminazione, come il dollaro `$`, ottenendo *hello*\$. Dopodiché, generi tutte le rotazioni possibili di questa stringa e le inserisci nell'albero alfabetico (B-tree): `hello$, ello$h, llo$he, lo$hel, o$hell, $hello`.
- **Come si interroga:** Quando arriva una query con un jolly in mezzo, come `X*Y`, il sistema aggiunge il dollaro alla fine e la ruota fino a spingere l'asterisco all'estrema destra, trasformandola in `Y$X*`. (Es. per cercare `h*lo`, il sistema ruota e cerca `lo$h*`). Se ci sono più asterischi (es. `X*Y*Z`), l'algoritmo esegue una ricerca per `X*Z` (ruotata in `Z$X*`) e poi fa un filtraggio a posteriori (post-filter) per verificare se la `Y` è presente.
- **Il prezzo da pagare:** Essendo molto veloce, ha un costo enorme in termini di spazio. Aggiungendo tutte le rotazioni, empiricamente **il dizionario quadruplica le sue dimensioni**.

![center|300](img/Pasted%20image%2020260411115404.png)

Altri esempi di processing della query sono i seguenti:

1. Ricerca esatta (`X`)
	- **Come funziona:** Nessun jolly. L'utente cerca la parola esatta.
	- **Regola:** Si aggiunge semplicemente il `$` alla fine.
	- **Esempio:** Cerchi `hello` $\to$ il motore cerca `hello$` nell'indice.
2. Ricerca per prefisso (`X*`)
	- **Come funziona:** L'utente sa come inizia la parola.
	- **Regola:** La parola viene trasformata in `X*$`, e per portare l'asterisco in fondo viene ruotata in `$X*`.
	- **Esempio:** Cerchi `hel*` $\to$ il motore cerca `$hel*`. Il database troverà tutte le stringhe ruotate che iniziano per `$` (cioè l'inizio della parola originale) seguito da `hel`.
3. Ricerca per suffisso (`*X`)
	- **Come funziona:** L'utente sa come finisce la parola.
	- **Regola:** La parola diventa `*X$`, la ruotiamo per mettere l'asterisco in fondo e otteniamo `X$*`.
	- **Esempio:** Cerchi `*llo` $\to$ il motore cerca `llo$*`. Troverà tutte le rotazioni che iniziano per `llo` e finiscono immediatamente (segnalato dal `$`).
4. Ricerca "Contiene" (`*X*`)
	- **Come funziona:** La parola deve contenere un frammento di lettere da qualche parte.
	- **Regola speciale:** In questo caso l'asterisco a sinistra cade e si cerca semplicemente `X*` (senza il dollaro).
	- **Esempio:** Cerchi `*ell*` $\to$ il motore cerca `ell*`. Perché senza dollaro? Perché se una parola contiene "ell", il Permuterm ha sicuramente generato una sua rotazione che inizia proprio con "ell", indipendentemente da dove si trovino l'inizio o la fine originali.
5. Jolly in mezzo (`X*Y`)
	- **Come funziona:** L'utente sa l'inizio e la fine, ma non il centro.
	- **Regola:** La parola `X*Y$` viene ruotata fino a portare l'asterisco in fondo, diventando `Y$X*`.
	- **Esempio:** Cerchi `h*lo` (inizia con 'h', finisce con 'lo') $\to$ il motore cerca `lo$h*`. Cerca cioè le rotazioni che partono con 'lo' (la fine), toccano il confine della parola ('$'), e poi hanno 'h' (l'inizio).
 6. Multi-Jolly (`X*Y*Z`)
	- **Come funziona:** Il caso peggiore. L'utente mette più asterischi (es. inizia per X, contiene Y in mezzo, finisce per Z). Non possiamo ruotare due asterischi alla fine contemporaneamente!
	- **Regola (Ricerca + Filtraggio):** Si ignora la parte centrale (`Y`) e si esegue una ricerca per gli estremi (`X*Z`, che come abbiamo visto al punto 5 si ruota in `Z$X*`). Una volta trovati i risultati, si scartano quelli sbagliati controllandoli uno a uno (post-filter).
	- **Esempio:** Cerchi `h*a*o`.
	    1. Ignori la 'a' e cerchi `h*o`.
	    2. Ruoti e cerchi `o$h*` nell'indice.
	    3. Il database ti restituisce parole vere come `hello` e `halo`.
	    4. Passi al post-filtraggio: `hello` contiene una 'a' in mezzo? No, la scarti. `halo` contiene una 'a'? Sì, la tieni!

## Bigram (k-gram) indexes

Per non far esplodere la memoria, si usa un approccio diverso: sminuzzare le parole.

- **Cos'è un k-gram:** È una sequenza di k caratteri consecutivi. Se k=2 si chiama Bigramma. Per generare i bigrammi, si aggiunge il simbolo speciale `$` ai confini della parola per indicarne l'inizio e la fine.
- **La costruzione:** Dalla parola "month" (diventata `$month$`), estraiamo i frammenti a due a due: `$m`, `mo`, `on`, `nt`, `th`, `h$`.
- **Il secondo indice:** Si crea un dizionario invertito speciale che non punta più ai documenti, ma punta **dal bigramma alle parole del dizionario normale** che lo contengono. Ad esempio, il bigramma `mo` punterà a un elenco che contiene parole come `among` e `amortize`.

![center|500](img/Pasted%20image%2020260411120400.png)

**Il problema del falso positivo:** 

Se un utente cerca `mon*`, il motore la scompone in tre pezzi (AND booleano): `$m` AND `mo` AND `on`. 
Questo sistema troverà sicuramente la parola `month`, ma **troverà erroneamente anche la parola `moon`** (perché `moon` inizia per `$m`, contiene `mo`, e contiene `on`). 

Per questo motivo, l'indice a $k$-grammi è ***spazialmente molto efficiente***, ma obbliga il server a eseguire un filtraggio successivo (post-filter) per scartare termini falsi come `moon` controllandoli contro la query originale.

## L'Esecuzione Finale del Processing

Sia che tu usi il Permuterm, sia che tu usi il $k$-gram index, questa è solo la primissima fase!

- **Dal termine al documento:** Una volta che abbiamo trovato l'enumerazione di _tutti_ i termini reali del dizionario che soddisfano la nostra wildcard (es. scopriamo che `mon*` corrisponde a `monday`, `money`, `monkey`), dobbiamo andare a pescare le lunghissime liste di documenti (postings) per ciascuno di essi.
- **Esplosione della query:** Se l'utente digita una query complessa come `se*ate AND fil*er` oppure `pyth* AND prog*`, il sistema prima deve trovare decine di variazioni per la prima parola, poi decine per la seconda, e infine unire (OR) le liste di documenti di tutte queste variazioni prima di poter fare l'incrocio finale (AND). Questo genera query interne mostruose che appesantiscono i server.

---
# Spelling Correction

L'ortografia è uno dei problemi più comuni (e frustranti) che i motori di ricerca devono affrontare. Quando un utente sbaglia a digitare, il motore di ricerca deve essere in grado di capire l'errore e correggerlo "al volo" per restituire risultati pertinenti.

Analizziamo l'architettura dei sistemi di **Spelling Correction** (Correzione Ortografica)

Prima di tutto vediamo che gli errori di battitura non sono rari, ma la loro frequenza dipende pesantemente dal contesto (dall'applicazione utilizzata).

- Nelle **query sul Web**, il tasso di errore è altissimo: ben il **26**$\%$. Questo perché gli utenti digitano in fretta, usano slang o non conoscono l'esatta ortografia di ciò che cercano.
- Nella semplice ribattitura senza possibilità di usare il tasto _backspace_ (cancella), il tasso è del 13$\%$.
- Su dispositivi piccoli (come i vecchi organizer o i telefoni), il tasso scende al $2\%-7\%$ (a seconda di quanti errori l'utente corregge manualmente).
- Nella dattilografia standard e attenta, il tasso è fisiologico e si attesta sull'$1-2\%$.
## Le Task: Detection e Correction

Il processo si divide in due fasi distinte:

1. **Spelling Error Detection (Rilevamento):** Il sistema deve prima accorgersi che c'è un errore.
2. **Spelling Error Correction (Correzione):** Una volta trovato, deve correggerlo. Questo può avvenire in tre modi:
    - **Autocorrect (Autocorrezione):** Il sistema cambia la parola in automatico senza chiedere permesso (es. cambia `hte` nel frequentissimo `the`).
    - **Suggest a correction:** Il motore propone una singola alternativa (il classico "Forse cercavi: ..." di Google).
    - **Suggestion lists:** Mostra un menu a tendina con diverse opzioni valide tra cui scegliere.
## Anatomia dell'Errore: "Non-word" vs "Real-word"

Questa è la distinzione fondamentale in linguistica computazionale. Gli errori non sono tutti uguali.

- **Non-word Errors (Parole inesistenti):** L'utente digita una sequenza di lettere che non forma alcuna parola valida (es. digita `graffe` invece di `giraffe`).    
    - **Come si rilevano?** È facile: basta guardare nel dizionario. Se la parola non c'è, è un errore. Più il dizionario è grande, meglio è, ma con un limite: il Web stesso è talmente pieno di errori che non può essere usato come dizionario perfetto.
    - Storicamente, la correzione di questi errori era "context insensitive" (insensibile al contesto), ovvero il sistema correggeva la parola isolata senza guardare il resto della frase.
- **Real-word Errors (Parole reali, contesto sbagliato):**
    - L'utente digita una parola che esiste nel dizionario, ma è sbagliata per quel contesto. Possono essere:
        - _Errori tipografici:_ Sbaglia a premere un tasto (es. scrive `three` invece di `there`).
        - _Errori cognitivi (Omofoni):_ Usa parole che suonano allo stesso modo ma si scrivono diversamente (es. `piece` invece di `peace`, o `your` invece di `you're`).
    - **Come si rilevano?** È difficilissimo, perché il dizionario non basta (la parola esiste!). Richiedono quasi obbligatoriamente un'analisi sensibile al contesto (context sensitive).
### Il Motore di Correzione (Come si sceglie l'alternativa giusta?)

Sia per le _non-word_ che per le _real-word_, l'algoritmo di correzione segue passaggi simili:

1. **Generare i Candidati:** Per ogni parola dubbia $w$, il sistema crea un set di alternative. Cerca nel vocabolario parole che hanno uno _spelling_ (scrittura) simile o una _pronunciation_ (pronuncia) simile. La parola originale $w$ viene sempre inclusa in questo set per sicurezza.
2. **Scegliere il migliore (Ranking):** Tra tutti i candidati generati, il sistema deve decretare il vincitore. Lo fa usando due metriche principali:
    - **Shortest weighted edit distance:** Vince la parola che richiede il minor numero di modifiche (inserimenti, cancellazioni, sostituzioni di lettere) per trasformarsi in quella originale.
    - **Highest noisy channel probability:** Una teoria matematica che calcola la probabilità che l'utente intendesse scrivere una determinata parola ma che il "canale rumoroso" (la sua tastiera o il suo cervello) ne abbia alterato l'output.
3. **Il Controllo del Contesto (Make Sense):** Soprattutto per le _real-word_, si guarda alle parole vicine per capire se la frase "ha senso". L'esempio classico: se un utente cerca "Flying _form_ Heathrow to LAX", la parola _form_ esiste, ma analizzando il contesto (voli e aeroporti), il sistema capisce che l'utente intendeva "Flying _from_" (volare da).

>[!info]- Parentesi sulla Terminologia
>L'ultima slide fa un'importante precisazione tecnica. Quando sminuzziamo i testi per analizzarli, possiamo farlo a due livelli:
>- **Character k-grams:** Scompongono la singola parola in lettere (es. "star" diventa `st`, `ta`, `ar`). Sono utilissimi per trovare candidati con _spelling simile_ in caso di errori di battitura.
>- **Word n-grams:** Scompongono la frase in blocchi di parole intere (es. "palo alto", "flying from"). Questi sono il vero motore dietro l'analisi del _contesto_.

