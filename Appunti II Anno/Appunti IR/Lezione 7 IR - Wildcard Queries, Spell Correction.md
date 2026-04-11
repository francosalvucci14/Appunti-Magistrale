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
2. Tra tutti i candidati generati, il sistema deve decretare il vincitore. Per farlo, applica il **Noisy Channel Model**, una teoria matematica che calcola la probabilità che l'utente intendesse scrivere una determinata parola ma che il "canale rumoroso" ne abbia alterato l'output. A seconda del tipo di errore, il modello si applica in due modi:
	- **Correzione base (per le Non-word):** Il sistema usa il Noisy Channel "isolato". Guarda solo la singola parola sbagliata, calcola quanto è probabile l'errore di battitura e lo moltiplica per la frequenza assoluta di quel candidato nella lingua.
	- **Context-Sensitive Spelling Correction (per le Real-word):** È una variante avanzata del Noisy Channel che entra in gioco per controllare se la parola "ha senso" nel testo. Invece di valutare la parola isolata, valuta la probabilità dell'**intera frase** guardando le parole circostanti (usando i _word n-grams_).
	    - _L'esempio classico:_ Se un utente cerca _"Flying form Heathrow to LAX"_, la parola "form" esiste nel dizionario (quindi supererebbe il controllo base). Tuttavia, il sistema _Context-Sensitive_ analizza il contesto (voli e aeroporti) e calcola che la sequenza _"Flying from"_ ha una probabilità statistica di avere senso immensamente superiore a _"Flying form"_, correggendo così l'errore.

>[!info]- Parentesi sulla Terminologia
>L'ultima slide fa un'importante precisazione tecnica. Quando sminuzziamo i testi per analizzarli, possiamo farlo a due livelli:
>- **Character k-grams:** Scompongono la singola parola in lettere (es. "star" diventa `st`, `ta`, `ar`). Sono utilissimi per trovare candidati con _spelling simile_ in caso di errori di battitura.
>- **Word n-grams:** Scompongono la frase in blocchi di parole intere (es. "palo alto", "flying from"). Questi sono il vero motore dietro l'analisi del _contesto_.
## Il Noisy Channel Model

Il **Noisy Channel Model** (Modello del Canale Rumoroso) è uno dei concetti più eleganti e affascinanti dell'Informatica e della Teoria dell'Informazione. Originariamente sviluppato da Claude Shannon nel 1948 per le telecomunicazioni, è stato poi brillantemente adattato per risolvere il problema della correzione ortografica.

Immagina che tu abbia in mente una parola esatta che vuoi scrivere, chiamiamola $w$ **(Word)**. Questa parola deve viaggiare dal tuo cervello, passare per le tue dita e arrivare alla tastiera.

Questo percorso fisico e cognitivo è il nostro **"canale rumoroso"**. A causa della fretta, di un dito che scivola o di una distrazione (il "rumore"), la parola originale $w$ viene corrotta e ciò che appare sullo schermo è un'osservazione sbagliata, che chiameremo $x$.

Il compito del motore di ricerca è fare il percorso inverso: **guardando solo la parola sbagliata $x$ (es. _acress_), deve indovinare quale fosse la parola originale $w$ (es. _actress_, _across_, _acres_)**.

![center|500](img/Pasted%20image%2020260411122534.png)
### Formulazione Matematica

In termini probabilistici, il sistema cerca di trovare la parola $w$ (all'interno di tutto il vocabolario $V$) che ha la probabilità massima di essere quella giusta, dato l'errore $x$. 
La formula si scrive come: $$\hat{w}=arg\max_{w\in V}​P(w|x)$$

Tuttavia, calcolare direttamente $P(w|x)$ è molto difficile. Qui entra in gioco il famoso **Teorema di Bayes**, che ci permette di "capovolgere" il problema:

$$P(w|x)=\frac{P(x)P(x|w)}{P(w)}​$$

Poiché il denominatore $P(x)$ (la probabilità di scrivere quella specifica parola sbagliata) è identico per tutti i candidati che stiamo valutando, possiamo tranquillamente ignorarlo per stilare la nostra classifica.

La formula semplificata diventa il vero cuore del Noisy Channel Model:

$$\hat{w}=arg\max_{w\in V​}\underbrace{P(x|w)}_{\text{Noisy Channel}}\underbrace{P(w)}_{\text{Prior}}$$
La formula che abbiamo appena ricavato è geniale perché divide la decisione in due modelli separati che si bilanciano a vicenda

1. **$P(w)$ (Prior Probability):** È la probabilità a priori che l'utente volesse scrivere la parola $w$. Dipende unicamente dalla frequenza della parola nella lingua (un modello linguistico). Ad esempio, la parola _across_ è molto più usata in inglese rispetto ad _actress_, quindi avrà un peso maggiore.
2. **$P(x|w)$ (Noisy Channel Model):** È la probabilità che, volendo scrivere $w$, l'utente abbia commesso l'errore $x$. Questo ci dice quanto è "facile" confondere ortograficamente o sulla tastiera le due parole.
### Generazione dei candidati

Valutare l'equazione di Bayes per _tutte_ le parole del vocabolario sarebbe computazionalmente impossibile in tempo reale. Per questo, il sistema prima filtra una lista ristretta di **candidati**. Come si trovano? Si cercano parole nel dizionario che abbiano:

- **Spelling simile:** una "distanza di edit" molto piccola rispetto alla parola errata.
- **Pronuncia simile:** una distanza fonetica ridotta (errori dovuti a come suona la parola).

#### Candidate Testing: Distanza di Damerau-Levenshtein

Per calcolare quanto due parole siano simili (e stimare indirettamente la componente del Noisy Channel), si usa la distanza di Damerau-Levenshtein. Questa metrica conta il numero minimo di "operazioni" necessarie per trasformare una stringa nell'altra.

Le operazioni consentite sono 4:

1. **Insertion (Inserimento):** Aggiungere una lettera.
2. **Deletion (Cancellazione):** Rimuovere una lettera.
3. **Substitution (Sostituzione):** Cambiare una lettera con un'altra.
4. **Transposition (Trasposizione):** Scambiare di posto due lettere adiacenti (questa operazione è l'aggiunta di Damerau rispetto alla classica distanza di Levenshtein, molto utile perché scambiare due tasti vicini è un errore umano frequentissimo).

Vediamo come un errore (acress) a distanza 1 da vari candidati possa originarsi tramite diverse operazioni. Guardando dal punto di vista dell'utente che ha sbagliato:

- Se voleva scrivere **actress**, ha "dimenticato" la _t_ (Errore di **Deletion**).
- Se voleva scrivere **cress**, ha "aggiunto" una _a_ all'inizio (Errore di **Insertion**).
- Se voleva scrivere **caress**, ha scambiato _ca_ con _ac_ (Errore di **Transposition**).
- Se voleva scrivere **access**, ha digitato una _r_ invece di una _c_ (Errore di **Substitution**).

Mettendo insieme tutto questo: il sistema genera questi candidati tramite la distanza di Damerau-Levenshtein, calcola per ognuno il punteggio combinato moltiplicando P(x∣w) (basato su quanto è comune quello specifico errore di battitura) e P(w) (quanto è comune la parola), e infine suggerisce all'utente la parola con il punteggio più alto.

![center|500](img/Pasted%20image%2020260411134703.png)

Come abbiamo visto, calcolare le distanze per ogni parola del vocabolario è troppo lento. Vediamo alcune euristiche basate sull'osservazione statistica degli errori umani:

- **La regola della distanza 1 e 2:** L'80$\%$ degli errori di battitura si trova a una distanza di edit pari a 1 dalla parola corretta (es. manca una lettera o ce n'è una in più). Quasi _tutti_ gli errori rientrano in una distanza di edit pari a 2. Questo ci permette di limitare drasticamente la ricerca: non cerchiamo parole a distanza 3 o 4, perché statisticamente è quasi impossibile che l'utente abbia fatto un errore così grave se voleva scrivere quella specifica parola.
- **Spazi e trattini:** Un buon sistema deve considerare anche l'inserimento accidentale o la dimenticanza di spazi e trattini. Ad esempio, "thisidea" viene corretto in "this idea", e "inlaw" in "in-law".
- **Unione di parole (Merging):** Similmente, si valuta l'unione di parole separate, come "data base" che diventa "database". Nelle query di ricerca brevi, spesso l'intera stringa viene trattata come un unico blocco da cui generare le correzioni
#### Come generiamo i candidati?

Vediamo ora cinque semplici approcci algoritmici per trovare effettivamente queste parole simili nel dizionario. Dal più ingenuo al più avanzato:

1. **Scansione del dizionario:** Il metodo più lento. Passi in rassegna ogni singola parola del dizionario e calcoli la distanza di edit rispetto all'errore. Impraticabile per dizionari enormi in tempo reale.
2. **Generazione e Intersezione:** Prendi la parola sbagliata e generi _tutte_ le possibili varianti matematiche con distanza 1 o 2 (aggiungi lettere a caso, togli lettere, scambi lettere). Poi, prendi questo enorme set di stringhe senza senso e lo incroci (intersezione) con il dizionario. Quelle che "sopravvivono" all'intersezione sono parole vere e diventano i tuoi candidati.
3. **Indici a k-grammi e Jaccard:** Dividi la parola errata in piccoli blocchi di lettere (es. trigrammi: _acr_, _cre_, _res_...) e cerchi nel dizionario parole che condividono molti di questi blocchi, calcolando la somiglianza tramite il Coefficiente di Jaccard.
4. **Levenshtein finite state transducer:** Si usano strutture dati molto avanzate (Automi a Stati Finiti) che permettono di trovare i percorsi di correzione in modo estremamente rapido, quasi istantaneo.
5. **Mappe precalcolate (Caching):** L'approccio più pratico per i sistemi in produzione. Si crea un database in cui si pre-salvano gli errori più comuni e le loro correzioni (es. se vedo "teh", so già che la correzione è "the" senza dover fare calcoli).
##### Un paradigma fondamentale

In un mondo ideale, vorremmo sempre calcolare e trovare la _migliore correzione assoluta_. Nella realtà, questo richiede troppa potenza di calcolo e troppo tempo. Quindi, si usa un **paradigma ricorrente**:

- Invece di cercare il migliore in assoluto tra milioni di opzioni, si estrae un sottoinsieme di elementi "abbastanza buoni" (ad esempio, solo i candidati a distanza di edit massima di 2).
- A quel punto, si analizza a fondo solo questo piccolo gruppo e si sceglie il migliore _al suo interno_.
- Anche se forse abbiamo scartato la vera "parola perfetta" al primo giro, questo compromesso ci permette di avere risposte veloci ed estremamente precise nel 99% dei casi. Si fa la stessa cosa per trovare le migliori pagine web, le migliori risposte o i migliori annunci pubblicitari.

#### Language Model

Torniamo alla nostra formula del Noisy Channel Model calcolata con il Teorema di Bayes. Avevamo stabilito che per trovare la parola migliore $\hat{w}$ dobbiamo massimizzare due fattori: $P(x|w)$ (probabilità dell'errore) moltiplicato per $P(w)$ (probabilità a priori della parola). 

La domanda allora è: **Come si calcola $P(w)$?**

La risposta è: con il **Language Model (Modello Linguistico)**. 
Per sapere quanto è "probabile" che un utente voglia scrivere una certa parola, ci basiamo sulla frequenza con cui quella parola viene usata nel mondo reale.

- Si prende un'enorme collezione di testi (un corpus, come l'intera Wikipedia o milioni di articoli di giornale).    
- Si conta il numero totale di parole in questo corpus (che chiamiamo $T$ token).
- Si conta quante volte compare specificamente la nostra parola candidata (che chiamiamo $C(w)$).

La formula sarà semplicemente:

$$P(w)=\frac{C(w)}{T​}$$

Quindi, se stiamo valutando il candidato "across", conteremo quante volte "across" appare in tutto il nostro archivio diviso per tutte le parole dell'archivio. 

Più una parola è usata comunemente nella lingua, più alto sarà il suo $P(w)$, e quindi sarà più probabile che il sistema la scelga come correzione vincente. 

In applicazioni specifiche, invece di testi generici, questo corpus può essere costituito dallo storico delle query digitate dagli utenti, per avere un vocabolario ancora più aderente a ciò che la gente cerca realmente!

**Unigram Prior Probability**

Vediamo un esempio reale di come si calcola $P(w)$, usando la formula $P(w)=\frac{C(w)}{T​}$​ 

Qui viene applicata usando il COCA (Corpus of Contemporary American English), un enorme database testuale contenente oltre 404 milioni di parole ($T=404.253.213$).

Nella tabella vediamo i nostri famosi candidati per correggere l'errore _acress_.

- La parola **across** compare ben 120.844 volte. Dividendo questo numero per i 404 milioni totali, otteniamo una probabilità a priori di circa 0.000298.
- La parola **cress** (crescione) compare solo 220 volte, ottenendo una probabilità infinitesimale. Questo passaggio matematico dice al sistema: _"Prima ancora di guardare l'errore di battitura, sappi che è immensamente più probabile che un utente stia parlando di 'across' piuttosto che di 'cress'."_ 

![center|500](img/Pasted%20image%2020260411141118.png)

**Channel model probability**

Ora passiamo alla parte difficile: stimare $P(x|w)$. Definiamo formalmente le nostre stringhe:

- $x$ è la parola sbagliata digita dall'utente, composta dalle lettere $x_1​,x_2​,x_3,\dots,x_m​$.
- $w$ è la parola corretta (il nostro candidato), composta dalle lettere $w_1​,w_2​,w_3​,\dots,w_n​$.

La probabilità $P(x|w)$ è essenzialmente la **probabilità dell'edit**, ovvero: _qual è la probabilità statistica che un essere umano commetta esattamente quell'inserimento, cancellazione, sostituzione o trasposizione che trasforma $w$ in $x$?_

**Confusion Matrix**

Come fa il computer a sapere quali errori sono più frequenti? Usa le **Matrici di Confusione**. Sono enormi tabelle statistiche pre-calcolate (analizzando milioni di errori di battitura reali) che tengono il conto di quante volte le persone sbagliano specifiche lettere.

Abbiamo quattro matrici, una per ogni tipo di operazione:

- `del[x,y]`: Quante volte un utente, volendo scrivere _xy_, ha per sbaglio digitato solo _x_ (cancellando la _y_).
- `ins[x,y]`: Quante volte, volendo scrivere solo _x_, ha digitato _xy_ (inserendo una _y_ di troppo).
- `sub[x,y]`: Quante volte, volendo scrivere _y_, ha digitato la lettera sbagliata _x_.
- `trans[x,y]`: Quante volte, volendo scrivere _xy_, ha invertito le lettere scrivendo _yx_.

**Un dettaglio cruciale:** notiamo giustamente che _l'inserimento e la cancellazione sono condizionati dal carattere precedente_. Quando scriviamo, non cancelliamo una 't' a caso; cancelliamo una 't' che magari seguiva una 'c' (come in _actress_ → _acress_). La probabilità dell'errore dipende dalla sequenza delle dita sulla tastiera.

![center|500](img/Pasted%20image%2020260411141637.png)

Qui vediamo uno spaccato della matrice di **Sostituzione**. 

Se notiamo attentamente i numeri, noteremo che non sono distribuiti a caso. Le persone sostituiscono molto più frequentemente lettere che sono **vicine sulla tastiera QWERTY** (es. 'a' con 's') o che hanno un **suono simile** (es. vocali scambiate tra loro), mentre è rarissimo scambiare una 'a' con una 'z' se non si è del tutto distratti.
### Channel Model : Formula finale

Mettiamo insieme i pezzi del puzzle di Kernighan, Church e Gale. 

Per ottenere una probabilità percentuale ($P(x|w)$) a partire dai meri "conteggi" grezzi delle matrici, dobbiamo dividere il numero di volte in cui è avvenuto lo specifico errore per il numero di volte in cui _sarebbe potuto_ avvenire.

Il sistema calcola un valore diverso a seconda di quale singola operazione trasforma $w$ in $x$

- **Se l'errore è una Cancellazione (Deletion):** $$P(x|w)=\frac{del[w_{i-1​},wi​]}{count[w_{i-1}​w_i​]}$$(Il numero di volte che le lettere $w_{i-1}​w_i$​ sono state scritte perdendo l'ultima lettera, diviso per tutte le volte in cui quella specifica coppia di lettere compare nel testo originario).
- **Se l'errore è un Inserimento (Insertion):** $$P(x|w)=\frac{ins[w_{i-1},x_i​]}{count[w_{i-1}​]}$$(Il numero di volte che dopo la lettera $w_{i-1}$​ è stata inserita erroneamente la lettera $x_i$​, diviso per la frequenza totale della singola lettera $w_{i-1}$​).
- **Se l'errore è una Sostituzione (Substitution):** $$P(x|w)=\frac{sub[x_i​,w_i​]}{count[w_i​]}$$​(Il numero di volte in cui $w_i$​ è stata sostituita da $x_i$​, diviso per la frequenza assoluta della lettera corretta $w_i$​).
- **Se l'errore è una Trasposizione (Transposition):** $$P(x|w)=\frac{trans[w_i​,w_{i+1}​]}{count[w_{i}​w_{i+1​}]}$$​(Il numero di volte in cui la coppia $w_i​w_{i+1}$​ è stata scambiata, diviso per la frequenza della coppia corretta).

**In conclusione:** Per correggere _acress_, il sistema calcola la prior probability $P(w)$ per _actress_ e _across_. Poi, usando queste ultime formule e le matrici di confusione, calcola la probabilità dell'errore $P(x|w)$ (es. quanto è probabile "dimenticare una t dopo la c" per _actress_, rispetto a "sostituire la o con una e" per _across_). Moltiplica i due fattori per ciascun candidato e ti suggerisce la parola con il punteggio finale più alto!
#### Il problema degli zeri: Add-1 Smoothing

Prima di fare i calcoli finali, analizziamo un problema logico e matematico molto insidioso: cosa succede se un particolare errore non è **mai** comparso nel nostro corpus di addestramento?

Se guardiamo le matrici di confusione e cerchiamo quante volte qualcuno ha digitato "a" invece di "q", potremmo trovare uno zero.

Matematicamente, se $P(x∣w)=0$, quando andiamo a moltiplicarlo per la prior probability, il risultato finale sarà zero. 
Il sistema considererà quell'errore _impossibile_. Ma in realtà, "q" e "a" sono vicinissimi sulla tastiera.
È assurdo considerarlo un errore impossibile solo perché i nostri dati passati non l'hanno registrato.

La soluzione è elegante e si chiama **Add-1 Smoothing** (o correzione di Laplace): "ammorbidiamo" le probabilità aggiungendo artificialmente un **+1** a tutti i conteggi degli errori. In questo modo, facciamo finta che ogni singolo errore possibile sia accaduto _almeno una volta_.
Per mantenere la matematica corretta (le probabilità devono sempre sommare a 1), aggiungiamo al denominatore la grandezza del nostro alfabeto (indicata con A). Nessuna probabilità sarà mai più pari a zero.

Esempio con la **sostituzione**:
$$P(x|w)=\frac{sub[x,w]+1}{count[w]+A}$$

Vediamo i risultati del calcolo di $P(x|w)$ per i nostri candidati, applicando le formule viste in precedenza (e tenendo conto dello smoothing). La tabella ci mostra la probabilità del singolo "scivolone" sulla tastiera:

- Per passare da **actress** ad _acress_, l'errore è omettere una 't' dopo una 'c' (indicato come `c|ct`). Questa specifica dimenticanza ha una probabilità del **.000117**.
- Per passare da **across** ad _acress_, l'errore è sostituire una 'o' con una 'e' (indicato come `e|o`). La probabilità di scambiare questi due tasti è **.000093**.

Se ci basassimo _solo_ sugli errori di battitura, il sistema penserebbe che l'utente volesse scrivere "actress", perché dimenticare quella 't' è statisticamente un po' più facile che scambiare 'o' ed 'e'. 

![center|500](img/Pasted%20image%2020260411143132.png)

Si uniscono poi i due mondi:

1. Il modello dell'errore: $P(x|w)$
2. Il modello linguistico (la frequenza della parola): $P(w)$

Il sistema moltiplica questi due valori. 

![center|500](img/Pasted%20image%2020260411143333.png)

**Guardiamo i risultati finali:**

- Il punteggio per **actress** è **2.7**
- Il punteggio per **across** è **2.8**

**Il vincitore è "across"!**

![center|500](img/Pasted%20image%2020260411143401.png)

**Perché ha vinto?** Questa è la vera magia del Teorema di Bayes applicato allo spelling. Anche se l'errore di battitura per "actress" era leggermente più probabile (il canale era più rumoroso in quel senso), la parola "across" è **così tanto più comune** nella lingua inglese (ha un P(w) molto più alto) che ha ribaltato il risultato finale.

Il sistema ha ragionato così: _"Sì, dimenticare la 't' di actress è un errore molto comune, ma la gente usa la parola 'across' di continuo, mentre 'actress' si usa molto meno. Quindi, tutto sommato, scommetto che l'utente voleva scrivere 'across'"_.
### Variante: Context-Sensitive Spelling Correction

Questa è l'evoluzione del Noisy Channel per risolvere gli errori in cui la parola digitata esiste, ma è sbagliata nel contesto.

Analizziamo la realtà del problema con alcuni esempi in cui un correttore ortografico classico (che guarda le parole singolarmente) fallirebbe miseramente:

- "...fifteen **minuets**..." (minuetti invece di _minutes_, minuti)
- "The design **an** construction..." (_an_ invece di _and_)
- "Can they **lave** him..." (_lave_ esiste, ma intendeva _leave_)
- "...mainly **be** John Black." (_be_ invece di _by_)

Secondo uno studio (Kukich 1992), questi errori non sono rarità: rappresentano ben il **25-40%** di tutti gli errori di battitura! Serviva quindi un sistema che leggesse l'intera frase.

Poiché il sistema non sa _quale_ parola sia sbagliata (dato che sono tutte presenti nel dizionario), deve sospettare di **tutte**.

Per ogni singola parola nella frase (chiamiamola $x_i$​):

1. **Genera i candidati:** Il sistema prende la parola e crea un set di alternative. Include la parola stessa (perché magari è già giusta!), tutte le parole a distanza di edit 1 (es. togliendo o aggiungendo una lettera) e le parole omofone (che suonano uguali, come _peace/piece_).
2. **Applica il Noisy Channel:** Ora non cerca più di massimizzare la probabilità della singola parola, ma cerca la **sequenza di parole** $W$ (l'intera frase candidata) che ha la probabilità massima, data la frase originale digitata.
#### Bigram Language Model

Per decidere se sia meglio "fifteen _minuets_" o "fifteen _minutes_", abbiamo bisogno di un Modello Linguistico (Language Model) superiore. 
Invece degli unigrammi (che guardano la frequenza di una parola da sola), usiamo un **Bigram language model**.

L'idea è che la probabilità di una parola dipende strettamente dalla parola che la precede. La probabilità dell'intera frase $P(w_1​\dots w_n​)$ si calcola moltiplicando le probabilità condizionate di ogni parola rispetto alla precedente:

$$P(w_1\dots w_n​)=P(w_1​)P(w_2​|w_1​)\dots P(w_n​|w_{n-1}​)$$

In pratica, il sistema calcolerà P(minutes∣fifteen) e lo confronterà con P(minuets∣fifteen). 

Poiché nei testi reali "fifteen minutes" compare spessissimo e "fifteen minuets" quasi mai, il sistema capisce l'errore contestuale e lo corregge.

Tuttavia, passando ai bigrammi, il problema delle "probabilità a zero" (che avevamo visto con le lettere) esplode. È facilissimo che una specifica coppia di parole (un bigramma) non sia mai comparsa nel nostro corpus di addestramento, portando l'intera probabilità della frase a zero.

L'Add-1 Smoothing qui funziona male perché le combinazioni di due parole sono milioni e aggiungeremmo troppi "+1" finti, sballando le statistiche.

La soluzione più elegante è l'**Interpolazione lineare**:

$$P_{li}​(w_k|w_{k-1}​)=\lambda P_{uni}​(w_k​)+(1-\lambda)P_{bi}​(w_k​|w_{k-1}​)$$

Cosa significa questa formula?

creiamo una "probabilità ibrida" $(P_{li})$ mescolando la probabilità del bigramma ($P_{bi}$​) con la probabilità dell'unigramma base ($P_{uni}$​), pesandole tramite un parametro $\lambda$ (lambda, un valore tra 0 e 1, es. 0.8). 
In questo modo, se il bigramma "Flying from" non è mai stato visto (probabilità 0), l'equazione non si azzera! Viene "salvata" dal fatto che la singola parola "from" (unigramma) ha comunque una sua probabilità di esistere.

Vediamo ora le "fine points", ovvero i trucchetti per far funzionare questo modello nella vita reale sui computer. Il punto più importante riguarda l'**Underflow**.

Quando calcoliamo la probabilità di una frase lunga, ci ritroviamo a moltiplicare tra loro molti numeri piccolissimi (es. 0.001×0.0004×0.000002). I processori dei computer hanno un limite fisico per i decimali: se il numero diventa troppo piccolo, il computer "sbiella", lo arrotonda a uno zero assoluto e il programma si rompe (questo si chiama _floating point underflow_).

**La soluzione? Lavorare con i logaritmi.** C'è una proprietà matematica stupenda per cui il logaritmo di una moltiplicazione è uguale alla somma dei logaritmi. Quindi, invece di moltiplicare probabilità minuscole, **sommiamo** i loro logaritmi (che sono numeri negativi più gestibili dal computer):

$$\log P(w_1\dots w_n​)=\log P(w_1​)+\log P(w_2​|w_1​)+\dots+\log P(w_n​|w_{n-1}​)$$

Invece di cercare il prodotto più alto, il computer cercherà la somma (meno negativa) più alta. Il risultato logico è identico, ma il computer non va in crash!