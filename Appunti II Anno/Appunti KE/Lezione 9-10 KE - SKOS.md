```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

Abbandoniamo per un attimo la sintassi delle query SPARQL e facciamo un passo indietro a livello concettuale. 

Questa parte fan da "ponte": vediamo un rapido riassunto a velocità smodata di cosa sono i linguaggi ontologici tradizionali, per poi capire **perché**, nonostante la loro potenza, abbiamo bisogno di uno strumento diverso (come **SKOS**) per costruire tesauri e vocabolari controllati.
# Riassunto su Ontology Languages
## Il "Bignami" dei Linguaggi Ontologici

Prima di chiederci se ci serve uno strumento nuovo, riepiloghiamo l'arsenale "pesante" che il Web Semantico ci ha già messo a disposizione:

- **RDF (Il modello base):** È l'infrastruttura di base. Tutto ruota attorno al concetto che "ogni cosa è una risorsa" descrivibile tramite **triple** (Soggetto - Predicato - Oggetto). Visivamente, si traduce in un **Grafo orientato ed etichettato**: i nodi sono i soggetti/oggetti, le frecce sono i predicati. Come dice la slide 3, RDF è formidabile per collegare i dati, ma di per sé è solo "sintassi": collega le cose, ma non sa cosa significhino davvero quelle cose.
    
- **RDFS (Lo scheletro):** Aggiunge un vocabolario per creare degli _schemi_. Introduce il concetto di **Classe**, **Proprietà** e le **Gerarchie** (`subClassOf`, `subPropertyOf`). Permette anche di definire vincoli di dominio e codominio (es. "la proprietà _haMadre_ collega solo esseri umani con esseri umani femminili").
    
- **OWL (Il cervello logico):** È l'apice della semantica. Estende RDFS introducendo regole logiche potentissime derivate dalle **Logiche Descrittive (DL)**. Con OWL puoi dire cose complesse come:
    
    - _Restrizioni contestualizzate:_ Un "Genitore" ha come figlio un "Essere Umano", ma un "Elefante" ha come figlio un "Elefante".
        
    - _Cardinalità:_ Un "Genitore" deve avere _almeno 1_ figlio ($\ge 1$).
        
    - _Sfaccettature delle proprietà:_ Dire che una proprietà è _transitiva_ (se A è antenato di B, e B è antenato di C, allora A è antenato di C) o _simmetrica_ (se A è sposato con B, B è sposato con A).
        

**Il grande compromesso:** OWL ci dà il **Supporto all'Inferenza**, ovvero permette ai computer di dedurre nuove informazioni non scritte esplicitamente. Tuttavia, c'è un prezzo da pagare: il _trade-off_ tra potenza espressiva e calcolo computazionale. Più regole logiche (OWL) usi, più il sistema diventa "pesante" e lento da processare per mantenere la coerenza e la decidibilità matematica.
## Obiettivi Raggiunti: Due piccioni con una fava

Con RDF, RDFS e OWL, la comunità scientifica ha centrato due traguardi epocali rispetto ai classici database relazionali degli anni '80:

1. **Dati direttamente sul Web:** Interconnessi a livello globale, non chiusi in server aziendali.
    
2. **Superamento del modello a tabelle:** Le ontologie sono molto più vicine a come l'essere umano pensa (ricordano i diagrammi Entità-Relazione). **Scalano molto meglio** (Slide 5): se in un database SQL vuoi aggiungere un'entità al centro del tuo modello, devi fare un _reengineering_ drammatico spaccando decine di tabelle e chiavi esterne. In un'ontologia a grafo, semplicemente aggiungi un nodo e tiri due frecce. In più, fondere (fare _merge_) di due ontologie diverse è enormemente più facile che fondere due database SQL.

## Il Paradosso: Ci serve davvero altro?

Arriviamo al punto focale che introduce **SKOS**. 

Si pone una domanda provocatoria: _"Con un set così ricco di linguaggi di Rappresentazione della Conoscenza (KR)... non dovrebbe essere facilissimo sviluppare semplici dizionari o tesauri?"_

In apparenza, la risposta è "Sì". Un tesauro (un vocabolario strutturato di concetti, come un glossario medico o un catalogo bibliotecario) è concettualmente **molto più semplice** di un'ontologia. Ha solo bisogno di gerarchie di concetti e qualche proprietà descrittiva. Visto che OWL fa cose difficilissime, figuriamoci se non sa gestire un tesauro. _Sembra che abbiamo già tutto ciò che ci serve._

**La doccia fredda:**

La risposta reale è: **Usare OWL per fare un tesauro è una pessima idea.**

Perché? Perché la semantica DL (Description Logics) di OWL porta con sé restrizioni e "impegni filosofici" (_commitment_) troppo pesanti per un semplice vocabolario.

I due problemi enormi sono:

1. **Limiti del Primo Ordine:** Le logiche descrittive di OWL non permettono di "predicare sui predicati" facilmente. Non sono fatte per annotazioni linguistiche leggere o per descrivere in modo sfumato come i termini si relazionano nel linguaggio umano.
    
2. **Il problema della Classificazione (Concept = Class?):** Questo è il **motivo principale per cui è nato SKOS**.
    
    - In **OWL**, una "Classe" è concepita in senso strettamente insiemistico/matematico: la classe "Cani" è l'insieme di tutti i cani fisici esistenti.
        
    - In un **Tesauro**, tu non stai catalogando gli individui fisici, ma stai organizzando **Unità di Pensiero (Concetti)**. Il concetto "Amore" o il concetto "Informatica" in un indice di biblioteca non sono insiemi di esseri fisici, sono solo "etichette semantiche".
        
    - Se forzi un concetto di un tesauro a diventare una Classe OWL, il motore logico cercherà di applicare regole matematiche su cose che sono puramente astratte e linguistiche, generando errori di ragionamento o complessità computazionale del tutto inutile.
        

**In sintesi:** OWL è come un bisturi laser per la chirurgia di precisione (logica ferrea). Ma per costruire un tesauro non ci serve un bisturi laser, ci serve uno strumento flessibile, leggero e pensato appositamente per organizzare "concetti astratti" e non insiemi matematici. **Quello strumento sarà SKOS (Simple Knowledge Organization System).**
# Il limite della Logica del Primo Ordine

Il problema centrale nel tradurre semplici vocabolari o tesauri in ontologie rigorose risiede nelle fondamenta matematiche su cui si basano linguaggi come OWL: la **Logica del Primo Ordine**.

Per capire perché questa rigidità diventi un ostacolo, dobbiamo analizzare come la logica formale divide il mondo della conoscenza e quali cortocircuiti si creano quando cerchiamo di forzarvi all'interno il linguaggio umano.

Nei linguaggi ontologici standard, l'universo è diviso in strati gerarchici molto netti:

- **Livello 0 (Gli Oggetti o Istanze):** Sono le entità specifiche e tangibili del dominio (es. _la tua automobile_, _il fiume Po_, _Socrate_).
    
- **Livello 1 (I Predicati o Classi):** Sono le categorie o le proprietà che usiamo per "descrivere" gli oggetti di livello 0 (es. _Automobile_, _Fiume_, _Essere Umano_).

![center|300](img/Pasted%20image%2020260518150917.png)

Il limite strutturale della logica del primo ordine è che **i predicati non possono descrivere se stessi**. Possono solo guardare "verso il basso", descrivendo gli oggetti. Se vogliamo aggiungere informazioni a un concetto (ad esempio, dire che il concetto "Fiume" è un termine obsoleto, o che è stato coniato in un certo anno), avremmo bisogno di predicati che descrivono altri predicati, entrando nel regno della **Logica di Secondo Ordine**. Linguaggi come OWL (basati sulle logiche descrittive) non sono progettati per questo, rendendo difficilissimo "parlare dei concetti" in quanto tali.

## Il cortocircuito tra Concetto e Classe

In un'ontologia formale, si usa tipicamente `owl:Class` per definire le categorie e `rdfs:subClassOf` per creare la gerarchia. Se tentiamo di usare questa stessa infrastruttura per un tesauro, ci rendiamo subito conto che i due modelli non combaciano:

1. **Mancanza di interesse per le istanze:** In un tesauro, l'obiettivo è organizzare la terminologia, non catalogare gli oggetti del mondo reale. Il livello 0 (le istanze) spesso non ci interessa minimamente; vogliamo solo muoverci tra i concetti.
    
2. **Impossibilità di caratterizzazione:** Come visto sopra, trattare un termine di un tesauro come un'astratta Classe OWL ci impedisce di arricchirlo facilmente con note editoriali, storiche o lessicali.
    
## La trappola della gerarchia: Il caso "Broader/Narrower"

L'incompatibilità più grave esplode quando si cerca di strutturare la gerarchia. I tesauri utilizzano relazioni molto intuitive e rilassate, tipicamente definite come **più ampio / più specifico** (_broader/narrower_).

Immaginiamo questa catena presente in un tesauro geografico:

_Zone Aride_ $\rightarrow$ _Deserti_ $\rightarrow$ _Deserto del Sahara_

Per un linguista o un bibliotecario, questa gerarchia è perfetta e coerente. Ma se la diamo in pasto a un motore logico OWL traducendo le frecce in `subClassOf`, commettiamo un gravissimo errore strutturale, un vero e proprio "salto di ordine logico".

Infatti, mentre "Deserto" è logicamente una sottoclasse di "Zona Arida", il "Deserto del Sahara" non è una sottoclasse dei deserti, ma ne è **un'istanza specifica** (un oggetto di Livello 0). Mescolare relazioni di sotto-classe e relazioni di appartenenza sotto un'unica relazione generica distrugge la consistenza semantica formale dell'intera struttura.

## Le conseguenze pratiche: Eccessiva ingegnerizzazione (Over-engineering)

Cosa succede quando si ignora questo divario filosofico e si tenta ostinatamente di convertire complessi tesauri (siano essi linguistici o legati a domini specifici come l'agricoltura) in rigide ontologie OWL? Il risultato è quasi sempre disastroso dal punto di vista pratico.

Per rispettare i severi vincoli formali necessari ai ragionatori logici (mantenendo la conformità allo standard OWL DL), i modellatori sono costretti a creare architetture estremamente contorte. Sono obbligati a separare nettamente il "concetto di dominio" puro (spesso ridotto a un codice numerico incomprensibile per l'uomo) dalla sua "lessicalizzazione" (la parola vera e propria usata dalle persone), collegandoli attraverso una fitta ragnatela di relazioni artificiali, tipi inferiti e nodi intermedi.

Queste formalizzazioni dedicate, pur essendo matematicamente ineccepibili, producono modelli inutilmente complessi, difficili da esplorare, impossibili da mantenere e, in ultima analisi, completamente inutili rispetto allo scopo originario per cui il vocabolario era stato creato.

Diventa quindi evidente la necessità di un paradigma alternativo: uno strumento che offra la portabilità e l'interconnessione del Web Semantico, ma senza il peso della logica formale.
# SKOS : Simple Knowledge Organization System

Il divario filosofico tra il rigore matematico di OWL e la natura fluida del linguaggio umano è esattamente ciò che ha portato alla nascita di **SKOS (Simple Knowledge Organization System)**. SKOS è una raccomandazione del W3C progettata specificamente per rappresentare tesauri, sistemi di classificazione, schemi di subject heading e tassonomie all'interno del Web Semantico.

## La Soluzione SKOS: Un Salto "Verso il Basso"

Il principio fondante di SKOS è geniale nella sua semplicità: **"Spostare tutto un livello logico più in basso!"**.

Invece di lottare con le Classi OWL (che, come abbiamo visto, vivono al Livello 1 della logica e non possono essere descritte facilmente), SKOS definisce l'entità fondamentale, lo `skos:Concept`, come un oggetto di **Livello 0** (un'istanza).

In SKOS, un "concetto" non è un contenitore di oggetti fisici, ma è esso stesso un oggetto di indagine. Noi _parliamo dei concetti_ (es. "quando è stato introdotto il concetto di 'Intelligenza Artificiale'?"), non li usiamo per catalogare il mondo reale.

Questa declassazione porta con sé un enorme vantaggio: **si perdono le forti assunzioni semantiche**. SKOS sostituisce la rigida gerarchia `rdfs:subClassOf` con relazioni semantiche molto più "rilassate" o "lasche" (_loose_):

- **Relazioni Intra-schema:** `skos:broader` (più ampio) e `skos:narrower` (più specifico). Queste relazioni tollerano benissimo le incongruenze linguistiche senza mandare in tilt i ragionatori logici. Dire che il "Sahara" ha un concetto più ampio in "Deserto" è perfettamente legale in SKOS.
    
- **Relazioni Extra-schema (Mapping):** Per collegare concetti tra tesauri diversi, SKOS offre proprietà di allineamento (es. `skos:exactMatch`, `skos:broadMatch`) che indicano similitudine d'uso, senza le pesanti conseguenze logiche dell'identità assoluta garantita da `owl:sameAs` o `owl:equivalentClass`.
## Le Caratteristiche Principali di SKOS per i Tesauri

SKOS è essenzialmente un vocabolario ristretto e mirato, basato su RDF, che offre strumenti specifici per la modellazione terminologica:

- **Viste Multiple (Concept Schemes):** Un singolo concetto può appartenere a più schemi organizzativi (attraverso `skos:inScheme`). Ad esempio, il concetto "Acqua" può trovarsi contemporaneamente nello schema "Risorse Naturali" e nello schema "Elementi Chimici". L'oggetto `skos:ConceptScheme` rappresenta l'intero vocabolario e permette di raggruppare i concetti (`skos:hasTopConcept`).
    
- **Identificatori (Notations):** Supporto per codici o classificazioni alfanumeriche tramite `skos:notation` (es. i codici della classificazione decimale Dewey).
    
- **Gestione Ricca delle Etichette (Labels):** SKOS permette di associare stringhe di testo ai concetti distinguendone il ruolo linguistico:
    
    - `skos:prefLabel`: L'etichetta preferita o raccomandata (ne è consentita solo una per lingua per ogni concetto).
        
    - `skos:altLabel`: Sinonimi o acronimi.
        
    - `skos:hiddenLabel`: Etichette utili per la ricerca (es. errori di battitura comuni o termini dispregiativi) che non devono essere mostrate all'utente finale.
        
- **Documentazione Dedicata:** Proprietà specifiche per aggiungere note editoriali (`skos:editorialNote`), note storiche sulle modifiche del termine (`skos:historyNote`), definizioni (`skos:definition`) ed esempi d'uso (`skos:example`).
    
## Le Condizioni di Integrità e le "Idiosincrasie" di SKOS

Nonostante la sua natura "rilassata", SKOS mantiene alcune regole di coerenza interna, anche se spesso queste regole non possono essere codificate strettamente come assiomi OWL, ma rimangono come raccomandazioni o controlli da effettuare a livello applicativo.

**Condizioni di Integrità:**

- Disgiunzione tra etichette: Un termine non può essere contemporaneamente la `prefLabel` e una `altLabel` (o `hiddenLabel`) dello stesso concetto nella stessa lingua. Le proprietà sono mutuamente esclusive (disgiunte a coppie).
    
- Disgiunzione relazionale: Due concetti non possono essere collegati contemporaneamente da una relazione associativa (`skos:related`) e da una relazione gerarchica transitiva (`skos:broaderTransitive`). Se un concetto "include" un altro, non ha senso dire che è solo "correlato" ad esso in senso orizzontale.
    
- Disgiunzione di mapping: `skos:exactMatch` non può sovrapporsi a relazioni di mapping gerarchico come `skos:broadMatch`.
    

**La Parziale Indipendenza da OWL:**

È un errore comune credere che SKOS sia un'alternativa completamente separata da OWL. Come sottolineato, **SKOS è esso stesso un vocabolario OWL**. Sfrutta le fondamenta di OWL (tipi di dato, proprietà oggetto e di annotazione) pur non imponendo la logica delle classi sui concetti che definisce.

Questa parentela genera alcune particolarità (le _idiosincrasie_):

- **La questione dell'Inferenza:** SKOS dichiara esplicitamente proprietà inverse (es. `broader` e `narrower`). Tuttavia, le _best practices_ suggeriscono di materializzare nei dati solo una delle direzioni (spesso il `broader`) per evitare ridondanze. Recuperare l'informazione inversa richiede quindi l'intervento di un ragionatore, reintroducendo quel carico computazionale che SKOS teoricamente cercava di alleviare (sebbene in forma molto più gestibile rispetto alla classificazione DL).
    
- **Top Concepts:** Per evitare interrogazioni troppo onerose sull'albero gerarchico, SKOS introduce proprietà come `skos:hasTopConcept`, che collegano esplicitamente lo schema alle sue radici. Questo agevola la lettura, ma aumenta l'onere di scrittura e manutenzione dei dati.
    

## SKOS-XL

SKOS è ottimo per sistemi semplici, ma mostra i suoi limiti quando si affrontano tesauri, dizionari o terminologie linguistiche complesse.

In SKOS base, le etichette (es. `skos:prefLabel "Mammal"@en`) sono semplici _literals_ testuali attaccati al concetto. Essendo stringhe grezze, **non possiamo descriverle ulteriormente**. Non possiamo dire che l'etichetta "Mammal" è stata creata da Armando Stellato, o che "Mammalyan" è un suo sinonimo arcaico, perché in RDF non si possono attaccare proprietà a un literal.

**SKOS Extension for Labels (SKOS-XL)** risolve questo limite operando una **reificazione** delle etichette.

In SKOS-XL, l'etichetta smette di essere una semplice stringa e viene "promossa" a oggetto di Livello 0: la risorsa `skosxl:Label`.

- Il concetto (es. `C1`) si collega all'oggetto etichetta (es. `L1`) tramite la proprietà `skosxl:prefLabel`.
    
- L'oggetto etichetta `L1` porta con sé il valore testuale grezzo tramite la proprietà `skosxl:literalForm` (es. "Mammal"@en).

![center|500](img/Pasted%20image%2020260518154012.png)

Questa promozione sblocca possibilità enormi per la modellazione linguistica:

1. **Metadati sulle Etichette:** Possiamo ora associare un autore (`dc:creator`), una data di creazione o un riferimento bibliografico all'oggetto etichetta `L1`.
    
2. **Relazioni tra Etichette:** SKOS-XL introduce la possibilità di collegare due oggetti etichetta tra loro tramite relazioni generiche (`skosxl:labelRelation`). Da qui si possono creare sottoproprietà specifiche (es. `abc:synonyms`, o relazioni per acronimi, derivazioni morfologiche) che legano direttamente le forme testuali, a prescindere dal concetto che rappresentano.

Il modello concettuale risultante (illustrato nell'applicazione su AGROVOC) mostra come SKOS-XL permetta di creare un layer puramente lessicale (gli oggetti Label e le loro relazioni) che si appoggia sul layer concettuale (i Concetti e le gerarchie), offrendo la flessibilità necessaria per modellare complesse risorse multilingue.

![center|500](img/Pasted%20image%2020260518154040.png)
### Questioni Aperte e Convivenza con OWL

Nonostante la potenza di SKOS e SKOS-XL, alcune questioni architettoniche rimangono aperte (i "dangling pointers" o questioni irrisolte):

- L'interazione tra i Named Graphs (i contenitori fisici dei dati) e i Concept Schemes logici non è normata.
    
- La gestione dell'identità delle `skosxl:Label` condivise tra più concetti può generare ambiguità.
    
- SKOS non fornisce un vocabolario normativo per i tipi specifici di relazioni linguistiche tra etichette, lasciando l'incombenza alle singole applicazioni.
    

In conclusione, **OWL e SKOS non sono nemici**. Sono strumenti diversi progettati per scopi complementari. Il compromesso ideale, suggerito dalle _best practices_ attuali, è quello di utilizzarli congiuntamente, mantenendo però una rigorosa separazione "igienica" dei dati.

Un'entità logica può essere modellata contemporaneamente come una Classe OWL (in un'ontologia per il ragionamento formale) e come un Concetto SKOS (in un tesauro per l'annotazione e la ricerca), purché le due rappresentazioni risiedano in dataset Linked Data distinti, evitando di fonderle brutalmente tramite importazioni dirette (`owl:import`), garantendo così sia la correttezza matematica che la flessibilità linguistica.