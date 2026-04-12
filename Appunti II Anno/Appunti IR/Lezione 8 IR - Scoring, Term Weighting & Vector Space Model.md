# I limiti del modello Booleano

Finora, i sistemi di ricerca classici si basavano sulle **Query Booleane** (usando operatori come AND, OR, NOT). Nel modello booleano, la logica è binaria: un documento o "macha" perfettamente la query, oppure no. Non ci sono vie di mezzo.

- **A chi piace?** Agli utenti esperti (es. bibliotecari, avvocati che cercano in database legali) che sanno esattamente cosa cercare, e alle applicazioni/software, che possono tranquillamente digerire e scorrere migliaia di risultati non ordinati.
- **Perché non va bene per il web?** L'utente medio odia le query booleane. Non sa scriverle, o comunque non ha voglia di farlo. Soprattutto, non ha nessuna intenzione di scorrere 1000 risultati disordinati per trovare quello che gli serve.
## Il problema: Feast or Famine

Qua introduciamo il concetto di **Feast or Famine** (letteralmente: abbuffata o carestia), che è il difetto fatale della ricerca booleana. Genera quasi sempre risultati agli estremi:

- **Abbuffata (Feast):** Se usi una query un po' generale (es. "world climate crisis"), il sistema ti restituisce 200.000 documenti. Troppi per poterli guardare tutti.
- **Carestia (Famine):** Se cerchi di restringere il campo aggiungendo un termine con un AND (es. "world climate crisis merkel"), basta che in un documento manchi _una sola_ di quelle parole per essere scartato. Risultato? Zero hit. Nessun documento trovato.

Trovare il giusto equilibrio con gli operatori logici richiede un'abilità enorme. La soluzione proposta è passare a un **"Soft AND"**: invece di scartare brutalmente i documenti che non hanno tutte le parole, li ordiniamo in base a quanto sono "buoni" rispetto alla ricerca.

Con il Ranked Retrieval (il recupero ordinato per rilevanza), il problema dell'"abbuffata" sparisce completamente. Se la tua ricerca produce 2 milioni di documenti pertinenti, non è un problema per l'utente, perché il motore di ricerca gli mostrerà solo **i migliori 10** nella prima pagina. L'utente non si sente sopraffatto. 

C'è però una **premessa fondamentale**: tutto questo castello sta in piedi solo se l'algoritmo di ranking funziona davvero, ovvero se è in grado di mettere matematicamente i risultati _più_ rilevanti in cima e quelli _meno_ rilevanti in fondo.
# Scoring

Come fa il computer a capire quale documento è più rilevante? Tramite lo **Scoring** (assegnazione di un punteggio). 

Il sistema prende ogni singola coppia "Query - Documento" e le assegna un punteggio numerico, ad esempio in un intervallo compreso tra `[0, 1]`. Questo numero rappresenta il grado di "match" (corrispondenza) tra quello che l'utente ha chiesto e quello che il documento contiene. 

Una volta calcolati i punteggi per tutti i documenti, il computer non deve fare altro che ordinarli dal più alto al più basso e stamparli a schermo.

Introduciamo le tre regole base (molto intuitive) su cui poi costruiremo la matematica avanzata del Vector Space Model:

1. **Nessuna corrispondenza:** Se nessuna parola della query compare nel documento, il punteggio deve essere **0**.
2. **Frequenza del termine:** Più volte una parola della query compare in un documento, più il punteggio di quel documento deve alzarsi (se cerco "gatto", un documento che ripete "gatto" 20 volte è probabilmente più rilevante di uno che lo nomina 1 sola volta).
3. **Quantità di termini diversi:** Se la query è formata da più parole (es. "gatto nero"), un documento che contiene _entrambe_ le parole avrà un punteggio più alto di uno che contiene solo la parola "gatto". Più termini della query sono presenti, più lo score sale.
## Un primo tentativo di Scoring: Il Coefficiente di Jaccard

Visto che ora vogliamo assegnare un punteggio numerico di "somiglianza" tra una Query e un Documento, l'idea più semplice è usare la teoria degli insiemi. Il **Coefficiente di Jaccard** è una metrica classica per misurare la sovrapposizione tra due insiemi A e B.

La formula è: $$JACCARD(A,B)=\frac{|A\cap B|}{​|A\cup B|}$$
Questa formula restituisce sempre un numero tra 0 (nessuna parola in comune) e 1 (insiemi identici).

**esempio pratico**

- **Query ($q$):** "ides of March" (3 parole uniche: _ides, of, March_)    
- **Documento ($d$):** "Caesar died in March" (4 parole uniche: _Caesar, died, in, March_)
- **Intersezione ($q\cap d$):** Solo la parola "March" è in comune (1 elemento).
- **Unione ($q\cup d$):** Tutte le parole uniche messe insieme (_ides, of, March, Caesar, died, in_) sono 6 elementi.
- **Punteggio Jaccard:** $\frac{1}{6}$.

Sembra funzionare, vero? Purtroppo, per i motori di ricerca, questo approccio è troppo primitivo.
### I tre difetti fatali di Jaccard

Purtroppo Jaccard non va bene quando si parla di testi testuali reali.

Vediamo i tre enormi limiti di questa metrica:

1. **Ignora la frequenza dei termini (Term Frequency - TF):** Jaccard guarda solo _se_ una parola esiste o no (vero/falso). Se il documento dell'esempio avesse ripetuto la parola "March" 100 volte, il punteggio Jaccard sarebbe stato sempre e solo 1/6. Un motore di ricerca moderno, invece, sa che se un documento ripete "March" 100 volte, sta parlando _esattamente_ di quello ed è molto più rilevante.
2. **Tratta tutte le parole allo stesso modo:** Nella query "ides of March", la parola "ides" è rarissima, mentre "of" è comunissima. Un documento che fa match sulla parola "ides" dovrebbe avere un punteggio immensamente più alto di uno che fa match solo su "of". Jaccard non considera questa "rarità" informativa (che in seguito chiameremo Inverse Document Frequency - IDF).
3. **Normalizzazione della lunghezza imperfetta:** Per penalizzare i documenti troppo lunghi (che farebbero match con tantissime parole solo per pura statistica), Jaccard divide per la dimensione dell'unione. Si è scoperto matematicamente che usare la "distanza del Coseno" è molto più efficace ed elegante per gestire documenti di lunghezze diverse.

>[!info]- Distanza del Coseno
>La **distanza del Coseno** è così definita:
>$$\frac{|A\cap B|}{\sqrt{​|A\cup B|}}$$

### Ripensare lo Scoring: Ripartire dalle basi

Dopo aver bocciato Jaccard, facciamo un passo indietro e poniamo le regole per il nostro nuovo sistema di punteggio. 

Prendiamo una query composta da una sola parola (one-term query):

- Se la parola non c'è, il punteggio è 0.    
- **La regola d'oro:** Più frequente è la parola della query all'interno del documento, più alto DEVE essere il punteggio. Per fare questo, dobbiamo abbandonare l'idea dei semplici insiemi e iniziare a contare le parole. Come lo diciamo al computer?
#### Dalla Presenza alla Frequenza: L'evoluzione delle Matrici

Per insegnare al computer a leggere un'intera collezione di documenti (come le opere teatrali di Shakespeare), usiamo le matrici. 
Mettiamo a confronto il "vecchio" mondo Booleano/Jaccard con il "nuovo" mondo del Ranked Retrieval.

**La Binary incidence matrix (Matrice di incidenza binaria):** 

Questo è il modello vecchio. Sulle righe c'è il nostro vocabolario ($V$), sulle colonne i documenti. Le celle contengono solo 0 o 1. Dal punto di vista matematico, ***ogni documento è rappresentato come un vettore binario*** appartenente all'insieme $\{0,1\}^{|V|}$, dove $|V|$ è il numero totale di parole nel nostro dizionario. 

Su questa matrice puoi fare calcoli booleani o usare Jaccard, ma non puoi sapere _quanto_ si parla di Giulio Cesare in quell'opera.

![center|500](img/Pasted%20image%2020260412161517.png)

**La Count matrix (Matrice dei conteggi):** 

Questo è il salto di qualità. La struttura è identica, ma le celle ora contengono il **numero reale di occorrenze** (Term Frequency). Guardiamo l'incrocio tra la riga "Caesar" e la colonna "Julius Caesar": c'è il numero 227. Questo significa che Giulio Cesare è nominato 227 volte in quel documento.
Ora ***ogni documento è rappresentato come un vettore di conteggi*** appartenente a $\mathbb N^{|V|}$ 

Questa "Count Matrix" è la fondamenta assoluta del **Vector Space Model**.

Trasformando i documenti in vettori di numeri (invece che in semplici liste di parole presenti/assenti), possiamo finalmente usare l'algebra lineare (come il Coseno) per calcolare punteggi precisissimi

![center|500](img/Pasted%20image%2020260412161641.png)
## Bag of Words Model

La prima cosa da capire su come un computer moderno legge un documento è che... **non lo legge davvero**. 
Nel modello "Bag of Words", il sistema prende l'intero testo di una pagina web, lo fa a pezzi e butta tutte le singole parole in un grande sacco, dimenticandosi completamente in che ordine erano scritte.

Un esempio perfetto è il seguente:

- _"John is quicker than Mary"_ (John è più veloce di Mary)
- _"Mary is quicker than John"_ (Mary è più veloce di John)

Per un essere umano, il significato è opposto. Ma per il "Bag of Words Model", questi due documenti sono **identici**, perché il sacchetto contiene esattamente le stesse parole ("John", "is", "quicker", "than", "Mary"), con le stesse identiche frequenze.

**Perché si fa questa cosa?** 

Ammettiamo che c'è una "perdita di informazione". 
Tuttavia, questa perdita è un prezzo bassissimo da pagare per ottenere una **drastica semplificazione del problema**. 
Ignorare la sintassi e la grammatica permette ai motori di ricerca di calcolare le frequenze su miliardi di documenti in frazioni di secondo, sfruttando l'algebra dei vettori. 

*Nota: per i casi in cui l'ordine è davvero vitale, si usano indici posizionali aggiuntivi, ma la base del ranking rimane la frequenza*
### La Term Frequency (TF)

Ora che abbiamo il nostro "sacchetto", dobbiamo contare cosa c'è dentro. 
Questo conteggio si chiama **Term Frequency (TF)**, indicata formalmente come $tf_{t,d}$​ (la frequenza del termine t nel documento d).

L'idea base l'avevamo già vista: se un utente cerca la parola "gatto", e un documento contiene la parola "gatto" dieci volte ($tf=10$), quel documento sarà sicuramente più rilevante di uno che la contiene una volta sola ($tf=1$).

**Ma c'è un problema insidioso:** La rilevanza non cresce in modo direttamente proporzionale alla frequenza. 
Un documento che ripete la parola "gatto" 10 volte è più rilevante di uno che la ripete 1 volta. Ma un documento che la ripete **100 volte** è davvero _dieci volte_ più rilevante di quello che la ripete 10 volte? No. Probabilmente è solo un po' più lungo o un po' più ripetitivo. La semplice "frequenza grezza" (raw frequency) sbilancerebbe troppo il sistema, premiando eccessivamente i testi lunghissimi o lo spam

La soluzione a questo problema è la seguente: ***Il peso Logaritmico (Log Frequency Weighting)***

Come facciamo a "schiacciare" questi numeri altissimi per evitare che dominino l'algoritmo, pur continuando a premiare chi usa la parola più spesso? Usiamo i **Logaritmi**. Questa è una delle formule più importanti dell'Information Retrieval:

- Se la parola **non c'è** nel documento ($tf_{t,d}​=0$), il peso ($w$) è banalmente **0**. 
- Se la parola **c'è** almeno una volta ($tf_{t,d}​>0$), applichiamo questa formula per calcolare il peso: $$w_{t,d​}=1+\log_{10}​tf_{t,d}​$$
**Perché funziona così bene?** Vediamo il seguente esempio

- Se la frequenza è **1**, il peso diventa $1+\log_{10}​(1)=1+0=1$
- Se la frequenza è **10**, il peso diventa $1+\log_{10}​(10)=1+1=2$
- Se la frequenza è **1000**, il peso diventa $1+\log_{10}​(1000)=1+3=4$
- etc..

Il logaritmo agisce come un formidabile ammortizzatore. Ripetere la parola 10 volte raddoppia il tuo peso rispetto a scriverla 1 volta. Ma per raddoppiare ancora il peso (arrivando a 4), non ti basta scriverla 20 volte, devi scriverla **1000 volte**! Questo "smorza" l'impatto delle altissime frequenze.

Il ***punteggio totale*** (matching score) per una coppia query-documento è semplicemente la somma dei pesi logaritmici di tutte le parole della query che appaiono in quel documento.

La formula è quindi:
$$\text{tf-matching-score}(q,d)=\sum\limits_{t\in q\cap d}(1+\log (tf_{t,d}))$$
#### Frequency in doc. vs Frequency in collection

Abbiamo calcolato la frequenza delle parole **all'interno del singolo documento** (Term Frequency). Ma nell'esercizio, la parola "on" ha pesato tanto quanto la parola "information". Questo è un disastro: "on" (su/di) è una preposizione banalissima che non porta quasi alcun significato, mentre "information" (informazione) è una parola chiave importante.

Per risolvere questo problema finale, non ci basterà più guardare quante volte la parola compare in quel documento, ma dovremo guardare **quante volte compare nell'intera collezione di tutti i documenti del mondo** (Frequency in collection). Una parola comunissima varrà quasi zero, una parola rara varrà tantissimo. Questo concetto (che studieremo a breve) si chiama **Inverse Document Frequency (IDF)**, e unito al nostro peso logaritmico TF formerà il leggendario algoritmo **TF-IDF**.

Analizziamo un problema logico che la sola Term Frequency (TF) non può risolvere.

Immagina un utente che cerca "aumento buono della linea" (una query non eccezionale, ma che contiene termini comunissimi in inglese: _good_, _increase_, _line_). Se ci basassimo solo sulla TF, un documento che ripete la parola "line" 50 volte avrebbe un punteggio altissimo. Ma la parola "line" è così generica che si trova in milioni di documenti! Non è un indicatore sicuro di rilevanza.

Ora immagina che la query contenga la parola **Phenethylamine**.

Questa è una parola _rarissima_. Se un documento contiene questa parola, anche solo una volta, è quasi matematicamente certo che stia parlando esattamente di ciò che l'utente sta cercando.

**La regola aurea che ne deriva:**

- I termini **rari** sono molto informativi → Vogliamo assegnare loro **pesi alti**.
- I termini **frequenti** sono poco informativi → Vogliamo assegnare loro **pesi bassi** (ma comunque positivi, non zero, perché fanno pur sempre parte della query).

Come facciamo a dire al computer se una parola è rara o frequente? Usiamo la **Document Frequency (DF)**. La DF non conta quante volte la parola appare in _un_ documento, ma **in quanti documenti totali della nostra collezione appare quella parola**. Se la mia collezione ha un milione di documenti e la parola "the" appare in un milione di documenti, la sua DF è altissima. Se "Phenethylamine" appare in 2 documenti, la sua DF è bassissima.
## IDF (Inverse Document Frequency)

Abbiamo detto che vogliamo pesi _alti_ per DF _basse_, e viceversa. 

C'è una relazione inversamente proporzionale. Per questo motivo definiamo l'**IDF (Inverse Document Frequency)** del termine t:

$$idf_t​=\log_{10}​\frac{N}{df_{t}}​$$ 

Cosa significano queste lettere?

- $N$: È il numero totale di documenti nel nostro intero database
- $df_t$​: È il numero di documenti che contengono la parola $t$.
- **La frazione** ​$\frac{N}{df_{t}}​$​: Questa è l'inversione. Se una parola è rarissima (DF minuscola), divideremo un numero enorme (N) per un numero piccolissimo, ottenendo un risultato gigantesco. Se una parola è comunissima (DF quasi uguale a N), la frazione sarà vicina a 1.
- **Il Logaritmo** ($\log_{10}$​): Come avevamo visto per la TF, usare i numeri grezzi creerebbe squilibri mostruosi. La frazione da sola produrrebbe pesi astronomici per le parole rare. Il logaritmo interviene per "smorzare" l'effetto, creando una curva molto più dolce

> _Nota importante:_ Da ora in poi, ricordati che usiamo il trucco del logaritmo sia per "schiacciare" le ripetizioni dentro il singolo testo (TF), sia per "schiacciare" la rarità globale della parola (IDF).

![center|500](img/Pasted%20image%2020260412165038.png)

### L'effetto dell'IDF sul Ranking finale

Si fa una precisazione vitale su quando l'IDF serve davvero. 

L'IDF modifica la classifica dei documenti **solo per le query che hanno almeno due parole**.

Perché? Immaginiamo che l'utente cerchi solo la parola "arachnocentric". 

L'IDF per questa parola sarà alto per _tutti_ i documenti che la contengono. Moltiplicare i punteggi di tutti i documenti per lo stesso numero costante non cambia l'ordine della classifica! Chi era primo resta primo.

La vera magia avviene nelle query composte, come **"arachnocentric line"**. 
In questo caso, l'algoritmo deve sommare i punteggi derivanti dalle due parole. 
Senza IDF, un documento che ripete "line" mille volte potrebbe battere un documento che contiene "arachnocentric" una volta sola. Ma **con l'IDF**, il peso relativo di "arachnocentric" viene moltiplicato immensamente (es. x6), mentre il peso relativo di "line" viene schiacciato quasi a zero (es. x0.5). Il sistema capisce che "arachnocentric" è il fulcro della query e premierà i documenti che la contengono, indipendentemente da quante volte ripetano la parola "line".

### DF vs CF: Perché contiamo i documenti e non le parole

Prima di unire le formule, dobbiamo rispondere a un dubbio legittimo: per calcolare quanto è rara una parola a livello globale, perché usiamo la **Document Frequency (DF)** (in quanti documenti compare) e non la **Collection Frequency (CF)** (quante volte in assoluto compare in tutto il database)?

Vediamo un esempio molto furbo:

- La parola **insurance** (assicurazione) ha una CF di 10.440 e una DF di 3.997.
- La parola **try** (provare) ha una CF di 10.422 e una DF di 8.760.

Noti la stranezza? Le due parole appaiono _esattamente_ lo stesso numero di volte in assoluto nella collezione (circa 10.400 volte). Se usassimo la CF per pesare le parole, "insurance" e "try" avrebbero lo stesso identico peso.

Ma la DF ci racconta una storia molto diversa. "Try" è sparpagliata ovunque (è in quasi 9.000 documenti). "Insurance" è concentrata in meno della metà dei documenti (neanche 4.000). Questo significa che chi scrive la parola "insurance" tende a ripeterla tantissime volte nello stesso testo, mentre "try" la si butta a caso in qualsiasi frase.

Pertanto, **"insurance" è un termine di ricerca immensamente migliore di "try"**. La Document Frequency riesce a cogliere questa sfumatura distributiva, ed è per questo che usiamo la DF (e di conseguenza l'IDF) per calcolare la rarità informativa.
## La Formula Regina: Il TF-IDF

Finalmente, uniamo le due anime del nostro sistema di punteggio. Il peso definitivo di un termine $t$ in un documento $d$ è il prodotto tra il suo peso locale (TF) e il suo peso globale (IDF).

$$w_{t,d​}=(1+\log​tf_{t,d}​)\cdot\log_{10}​\left(\frac{​N}{df_{t}​}\right)$$

Il peso finale (TF-IDF):

1. **Aumenta** se la parola viene ripetuta molte volte _all'interno di quello specifico documento_ (questa è la componente TF, che premia la pertinenza locale)    
2. **Aumenta** se la parola è _rara nell'intera collezione mondiale_ (questa è la componente IDF, che premia il potere informativo della parola).

Di contro:

- Se una parola è ovunque (come "il", "di", "per"), l'IDF è zero, e la moltiplicazione azzera tutto il punteggio, non importa quante volte tu l'abbia scritta nel documento.
- Se una parola rarissima non appare nel tuo documento, la TF è zero, e il punteggio è zero.

Questa formula è ancora oggi **lo schema di pesatura più famoso e fondamentale nei motori di ricerca**.

Mostriamo quindi l'ultimo stadio evolutivo di come il computer "vede" i documenti di testo. Ripercorriamo il viaggio:

1. **Binary Matrix:** C'erano solo 0 e 1 (Jaccard, modello Booleano).
2. **Count Matrix:** C'erano i numeri interi grezzi delle ripetizioni (157, 232, ecc.).
3. **Weight Matrix (La matrice dei pesi):** I numeri al suo interno non sono più conteggi, ma i risultati decimali![](Pasted%20image%2020260412171154.png) della formula TF-IDF

![center|500](img/Pasted%20image%2020260412171030.png)

Guardiamo l'incrocio tra la riga "Caesar" e la colonna "Julius Caesar". Il numero è **2.54**. Non significa che la parola compare 2,54 volte (sarebbe impossibile). Significa che combinando quante volte compare in quell'opera (TF) con quanto è comune nell'intera letteratura shakespeariana (IDF), il suo "peso di rilevanza" matematico è 2.54. Sorprendentemente, "Brutus" nello stesso documento ha un peso di **6.10**. Significa che "Brutus", matematicamente, è una parola molto più distintiva e informativa per trovare quel documento rispetto alla parola "Caesar".

Adesso, ogni documento nell'universo è rappresentato dal computer come un **vettore a valori reali** ($\mathbb R^{|V|}$). È una lunghissima lista di numeri decimali. Ed è proprio qui che entra in gioco la Geometria: se sia la query che i documenti sono vettori nello spazio, possiamo usare la trigonometria per vedere quali vettori "puntano nella stessa direzione"!

---
# Vector Space Model

## Documenti come vettori

Come facciamo a far "leggere" al computer i pesi TF-IDF che abbiamo appena calcolato? Li trasformiamo in coordinate spaziali. 
Immaginiamo uno spazio geometrico in cui **ogni singola parola del vocabolario è una dimensione (un asse)**.
Un motore di ricerca web crea uno spazio con decine di milioni di dimensioni ($|V|$ dimensioni, dove $V$ è la grandezza del vocabolario).

In questo ipotetico spazio a milioni di dimensioni:

- I termini sono gli **assi**.
- Ogni documento diventa un **punto** (o un vettore, una freccia che parte dall'origine e arriva a quel punto).
- Le coordinate di questo punto sono date esattamente dai pesi TF-IDF calcolati prima. Se la parola "Brutus" ha un peso di 6.10, il vettore si sposterà di 6.10 lungo l'asse della parola "Brutus".

Questo crea uno spazio vettoriale a valori reali matematicamente definito come $\mathbb R^{|V|}$. Poiché un documento contiene solo poche centinaia di parole rispetto ai milioni del vocabolario, quasi tutte le sue coordinate saranno zero (è un vettore "sparso").
## Query come vettori

Se un documento di mille parole è un vettore, cosa ci impedisce di trattare la query dell'utente (che ha solo 2 o 3 parole) allo stesso modo? Niente! **Anche la query diventa un vettore** nello stesso identico spazio multidimensionale.

L'intuizione geniale è questa: per trovare i documenti più rilevanti per una query, basta guardare quali documenti sono "fisicamente più vicini" alla query in questo spazio geometrico. 

**Prossimità = Similarità**. 

Dobbiamo quindi misurare la distanza tra il vettore della query e i vettori di tutti i documenti, e ordinare i risultati dal più vicino al più lontano. Ma qui nasce un problema insidioso: _come definiamo questa "distanza"?_
## Il fallimento della Distanza Euclidea

L'approccio più istintivo è prendere un "righello virtuale" e misurare la distanza in linea d'aria tra la punta del vettore query e la punta del vettore documento. 

In matematica, questa si chiama **Distanza Euclidea**.

La distanza Euclidea però è influenzata pesantemente dalla **lunghezza del vettore** (ovvero da quanto è lungo il testo del documento).

Diamo la prova visiva in uno spazio semplificato a 2 dimensioni (Asse X = "RICH", Asse Y = "POOR"):

- Il vettore della query q ("rich poor") punta a 45 gradi.
- Il documento d2​ ("Rich poor gap grows") usa molto entrambe le parole. È un documento lungo, quindi il suo vettore è una freccia lunghissima, ma punta _esattamente nella stessa direzione_ della query. Semanticamente, è un match perfetto!
- Il documento d1​ ("Ranks of starving poets swell") usa la parola "poor" ma non "rich". Punta tutto verso l'asse Y. È un documento corto.

Se usassimo la distanza Euclidea, noteremmo un'assurdità: la punta della freccia q è fisicamente **più vicina** alla punta di d1​ rispetto a quella di d2​, solo perché d2​ è stato "sparato" lontanissimo dalla sua lunghezza.

Il motore di ricerca ti darebbe un documento sbagliato solo perché è più corto di quello giusto.

![center|500](img/Pasted%20image%2020260412172716.png)
### La Soluzione: L'Angolo

Chiudiamo il ragionamento con un esperimento mentale brillante: Prendiamo un documento $d$ e facciamo copia-incolla del suo stesso testo, creando un documento $d'$ lungo il doppio.

- Semanticamente, hanno lo stesso identico contenuto. Dovrebbero avere una similarità massima.
- Siccome $d'$ è lungo il doppio, il suo vettore si estenderà per il doppio della distanza. La distanza Euclidea tra le due punte sarà enorme!
- Ma se guardiamo la direzione in cui puntano le frecce, è assolutamente identica. **L'angolo tra di loro è 0.**

Ecco la soluzione definitiva del Vector Space Model: per calcolare la similarità tra testi, **non dobbiamo misurare la distanza tra le punte dei vettori, ma l'ANGOLO tra di essi.** Documenti che parlano degli stessi argomenti useranno le stesse parole nelle stesse proporzioni, puntando nella stessa direzione, indipendentemente da quante pagine siano lunghi!

Misurare gli angoli in gradi (es. $45\degree$) in uno spazio a milioni di dimensioni è computazionalmente fastidioso. I matematici usano un trucco: invece di calcolare l'angolo, calcolano il **Coseno dell'angolo**.

Perché proprio il Coseno? Guardiamo il grafico.

![center|500](img/Pasted%20image%2020260412174727.png)

Nell'intervallo che ci interessa, ovvero da $0\degree$ a $180\degree$ (quando i vettori non hanno parole in comune e sono ortogonali), la funzione del Coseno è "monotonicamente decrescente". Significa che non fa curve strane: scende dritta e basta.

- Se l'angolo è $0\degree$ (**match perfetto**, i vettori sono sovrapposti), il Coseno è **1**.
- Se l'angolo è $90\degree$ (**match inesistente**, nessuna parola in comune), il Coseno è **0**.

Questo ci porta alla seguente rivelazione: **ordinare i documenti cercando l'angolo più piccolo è ESATTAMENTE UGUALE a ordinarli cercando il Coseno più grande (più vicino a 1)**.

Ora dobbiamo risolvere il problema visivo che avevamo nel grafico precedente (quello dei vettori): i documenti lunghi erano frecce lunghissime, quelli corti freccine corte.
La soluzione geometrica è la **Normalizzazione della lunghezza** .

Prendiamo ogni vettore e lo dividiamo per la sua stessa lunghezza (chiamata norma **euclidea** $L_2$​, ovvero la radice quadrata della somma dei suoi elementi al quadrato: $||x||_2​=\sum\limits_{i}x_{i}^2$)​.

Cosa succede fisicamente? Lo vediamo perfettamente nel grafico sottostante. 

![center|500](img/Pasted%20image%2020260412175134.png)

Tutte le punte delle frecce vengono "tirate" o "spinte" finché non toccano il bordo di un cerchio perfetto (o una sfera unitaria).

Ora **tutti i vettori hanno lunghezza 1**. I documenti lunghi e quelli corti sono perfettamente equiparati, e l'angolo $\theta$ tra la query $q$ e il documento $d_2$​ è diventato pulitissimo da misurare

Perché abbiamo fatto tutta questa fatica per normalizzare i vettori portandoli a lunghezza 1? Per una proprietà stupenda dell'algebra lineare

Se due vettori sono normalizzati, il Coseno del loro angolo si calcola semplicemente facendo il loro **prodotto scalare**:
$$cos(\vec{q},\vec{d})=\vec{q}\cdot\vec{d}=\sum\limits_{i}q_{i}d_{i}$$
In parole povere per il computer: _"Prendi il peso della parola 1 nella query e moltiplicalo per il peso della parola 1 nel documento. Fallo per tutte le parole in comune e somma i risultati"_. È un'operazione che i processori fanno a una velocità pazzesca!
## Cosine Similarity

Mettendo tutte queste nozioni insieme, otteniamo la formula per calcolare la similarità sfruttando il **coseno** e l'angolo $\theta$ risultate dall'applicazione vettoriale di query e documenti.

Questa formula prende il nome di **Cosine SImilarity**, ed è la seguente
$$\text{COS-SIM}(\vec{q},\vec{d})=\frac{\vec{q}}{|\vec{q}|}\cdot\frac{\vec{d}}{|\vec{d}|}=\frac{\sum\limits_{i=1}^{|V|}q_{i}d_{i}}{\sqrt{\sum\limits_{i=1}^{|V|}q_{i}^{2}}\sqrt{\sum\limits_{i=1}^{|V|}d_{i}^{2}}}$$
Dove:

- **Il Numeratore** $\left(\sum\limits_{i=1}^{|V|}q_{i}d_{i}\right)$​: È il prodotto scalare grezzo tra i pesi TF-IDF della query e quelli del documento. Più parole importanti hanno in comune, più questo numero cresce.
- **Il Denominatore** $(\sqrt{\dots}\sqrt{\dots})$: È la moltiplicazione tra la lunghezza del vettore query e la lunghezza del vettore documento. Questo è il fattore di **normalizzazione** che abbiamo visto prima, che serve ad abbassare i punteggi dei documenti che sono semplicemente troppo lunghi e "gonfiati".

Il risultato di questa frazione sarà sempre un numero tra 0 e 1. 

Il motore di ricerca calcola questo numero per tutti i documenti, li mette in fila, e ti mostra i dieci con il voto più vicino a 1.
### Cosine Score (pseudocodice)

Per prima cosa mostriamo l'algoritmo `CosineScore(q)`. 

È incredibilmente elegante e si basa su un approccio chiamato **TAAT (Term-At-A-Time)**, ovvero "un termine alla volta". Invece di prendere un documento e scansionare tutte le sue parole (cosa lentissima), il computer fa l'opposto: prende le parole della query e cerca i documenti.

Ecco come funziona passo per passo:

1. **Inizializzazione:** Il sistema crea un array enorme chiamato `Scores[N]` (dove N è il numero di tutti i documenti nel database) e lo riempie di zeri. Crea anche un array `Length[N]` dove sono già salvate le lunghezze dei documenti (il denominatore della nostra formula del coseno).
2. **Il ciclo esterno (per ogni termine della query):** Se cerchi "gatto nero", l'algoritmo parte dalla parola "gatto". Calcola il peso wt,q​ (il TF-IDF della parola "gatto" nella tua query) e va a pescare la **postings list** (la lista di tutti i documenti che contengono la parola "gatto").
3. **Il ciclo interno (per ogni documento nella lista):** Per ogni documento in quella lista, l'algoritmo calcola la moltiplicazione wt,d​×wt,q​ (il prodotto scalare) e lo **somma** al punteggio parziale di quel documento nell'array `Scores`. Poi ripete tutto per la parola "nero".
4. **La normalizzazione:** Finiti i termini della query, l'array `Scores` contiene i prodotti scalari grezzi. L'algoritmo fa un ultimo giro per dividere ogni punteggio per la sua `Length[d]`. Ecco fatto il Coseno!
5. **Il risultato:** Invece di ordinare milioni di documenti, usa una struttura dati super veloce chiamata **Priority Queue (o Heap)** per estrarre solo i migliori K documenti (es. i classici 10 risultati della prima pagina).

Lo pseudocodice è il seguente:

La Slide 2 fa un paio di appunti per gli sviluppatori:

- Esiste anche un approccio **DAAT (Document-At-A-Time)**, che valuta i documenti in parallelo.
    
- Per risparmiare memoria sui server, invece di salvare complessi numeri decimali (wt,d​) per ogni singola parola, si salva solo la frequenza grezza (TF) accanto al documento, e l'IDF lo si calcola al volo all'inizio della lista.

---
# Esercizi

## Esercizio 1

Mettere alla prova le due formule (Jaccard vs. TF-matching score) per capire concretamente perché il secondo metodo è migliore. 

Risoluzione del secondo esempio 

- **Query ($q$):** "information on cars" (3 termini unici)
- **Documento ($d$):** "information on trucks, information on planes, information on trains" (6 termini unici: _information, on, trucks, planes, trains_)

**Calcolo con Jaccard:**

- Intersezione ($q\cap d$): Le parole in comune sono "information" e "on" (2 elementi).
- Unione ($q\cup d$): Le parole uniche totali sono _information, on, cars, trucks, planes, trains_ (6 elementi).
- Score Jaccard = $\frac{2}{6}\approx0.33$

**Calcolo con il TF-matching score (Logaritmico):** Dobbiamo sommare i pesi delle sole parole della query che appaiono nel documento.

- **Termine "information":** Compare 3 volte. Il peso è $1+\log_{10}​(3)\approx1+0.477=1.477$
- **Termine "on":** Compare 3 volte. Il peso è $1+\log_{10}​(3)\approx1+0.477=1.477$
- **Termine "cars":** Compare 0 volte. Il peso è 0.
- Score TF totale = $1.477+1.477+0=2.954$.

Questo secondo punteggio riflette molto meglio la realtà: il documento parla _intensamente_ di informazioni, anche se non specificamente di macchine.