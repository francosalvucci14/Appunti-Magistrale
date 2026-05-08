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
# Linked Data (and Open Data)

Eccoci pronti ad affrontare un altro capitolo fondamentale: il passaggio teorico e pratico alla costruzione del **Web dei Dati**.

Finora abbiamo studiato i linguaggi (RDF, RDFS, OWL) che ci permettono di modellare e descrivere la conoscenza. Ora dobbiamo capire come queste descrizioni vengono pubblicate, condivise e interconnesse su scala globale. È qui che entrano in gioco i **Linked Data** (o Linked Open Data, se pubblicati con licenze aperte).

## Dal Web dei Documenti al Web dei Dati

Il World Wide Web classico è un "Web dei Documenti". È uno spazio informativo in cui gli identificatori globali (URI/URL) vengono usati per "cucire" insieme documenti ipertestuali (le pagine HTML). Noi navighiamo da una pagina all'altra, ma il computer non comprende il _significato_ dei collegamenti.

![center|400](img/Pasted%20image%2020260508104130.png)

Il **Web dei Dati** sfrutta le stesse identiche tecnologie di base (Internet, protocolli web, identificatori), ma per spargere e collegare un _grafo di dati_ su nodi remoti. Non colleghiamo più documenti testuali, ma le singole entità (nodi verdi nella slide) che compongono la nostra conoscenza.

![center|400](img/Pasted%20image%2020260508104150.png)

Per far sì che questo gigantesco grafo distribuito funzioni correttamente, nel 2006 **Tim Berners-Lee** (l'inventore del Web) ha formulato le **4 Regole dei Linked Data**. Analizziamole una per una nel dettaglio.
### Regola #1: Usa URI come nomi per le cose

Il primo passo per costruire il Web dei Dati è assegnare un **Uniform Resource Identifier (URI)** ai soggetti di nostro interesse.

Nel Web tradizionale, un URI identifica solitamente una _risorsa informativa_ (un file, un video, una pagina web). Nel Web dei Dati, l'orizzonte si allarga: l'URI identifica le **entità dell'universo del discorso**, che possono essere sia concrete (una persona, una città) sia astratte (un concetto, una relazione).

- **Identificazione Globale e Ambito (Scope):** La regola promuove fortemente l'uso degli URI al posto dei _blank node_ (nodi anonimi). Questo perché l'URI ha un ambito globale: permette a _chiunque_, in qualunque luogo, di parlare della _stessa identica risorsa_, garantendo l'integrazione di dati provenienti da terze parti.
    
- **La Coniazione (Minting):** La creazione di un nuovo URI si chiama "coniazione". Per evitare collisioni (due cose diverse con lo stesso nome), una convenzione sociale stabilisce che solo il proprietario di un dominio web (o i suoi delegati) ha il diritto di assegnare URI sotto quel dominio.
    
- **Il limite dell'URI:** Come specifica la RFC 3986, l'URI di base fornisce _soltanto l'identificazione_. Non garantisce in alcun modo che, inserendolo in un browser, si ottenga una risposta.
### Regola #2: Usa URI HTTP

Per risolvere il limite appena citato (identificatori "muti"), la seconda regola impone che gli URI coniati utilizzino lo **schema HTTP** (o HTTPS).

- Nel puro modello astratto RDF, l'URI è solo un nome logico.
    
- Imponendo lo standard HTTP, rendiamo quel nome **consultabile (look up)**. Il proprietario dell'URI si prende la responsabilità di far sì che, interrogando quell'indirizzo, le macchine o le persone possano recuperare informazioni utili sul _referente_ (l'entità reale) indicato da quell'URI.
    
- Mentre l'uso di URI HTTP per recuperare schemi tecnici (es. namespace XML) era già pratica nota, usarli per i _dati di base_ (ground data, le istanze) rappresenta la vera rivoluzione dei Linked Data.

### Regola #3: Fornisci informazioni utili usando standard

Quando qualcuno interroga il tuo URI HTTP, non devi restituire una pagina a caso, ma un set di informazioni strutturate secondo **standard precisi (RDF, SPARQL)**.

Questa regola poggia su pilastri teorici ben precisi, ottimali per un ambiente distribuito come il Web:

- Uso di formati di serializzazione ampiamente accettati (es. RDF/XML, Turtle).
    
- Adozione della **Open World Assumption (OWA)** e della **Semantica Monotona**, perfette per gestire dati intrinsecamente incompleti e provenienti da fonti con diversi livelli di dettaglio.
    

**Ma quali dati restituire esattamente? La SCBD:**

Se ti chiedo informazioni su Roma, non puoi restituirmi l'intero database mondiale. Un approccio standard per decidere _quante_ informazioni fornire è la **Symmetric Concise Bounded Description (SCBD)**. Questa regola stabilisce che la risposta deve contenere:

1. Tutte le triple (statement) in cui la risorsa compare come _soggetto_.
    
2. Tutte le triple in cui la risorsa compare come _oggetto_ (simmetria).
    
3. Ricorsivamente, tutte le triple collegate agli eventuali _blank node_ incontrati nei primi due passi.
    

**Il meccanismo tecnico: La Content Negotiation:**

L'esempio su DBpedia illustra _come_ il server capisce cosa restituire. Se un essere umano digita `http://dbpedia.org/resource/Rome` nel browser, il server legge l'header HTTP "Accept: text/html" e lo reindirizza alla pagina web leggibile. Se invece è un software semantico a fare la richiesta con "Accept: application/rdf+xml", il server utilizza la **Content Negotiation** per reindirizzarlo verso il file dati puro contenente le triple RDF.

![center|500](img/Pasted%20image%2020260508104402.png)
### Regola #4: Includi collegamenti (link) ad altri URI

Questa è la regola che trasforma dei database isolati (silos di dati) in un vero e proprio **Web**.

- Un link nel Web dei Dati non è altro che una **tripla RDF** in cui il _soggetto_ e l'_oggetto_ vivono in **dataset differenti** (governati da proprietari diversi).
    
- **Esempio:** `ex:fiorelli ex:livesIn dbpedia:Rome`. Qui stiamo unendo un'entità definita in un nostro vocabolario locale (`ex:fiorelli`) a un'entità governata dal namespace globale di DBpedia (`dbpedia:Rome`).
    

Questi link che attraversano i confini dei singoli dataset sono il vero motore dei Linked Open Data: supportano il **riuso** di identificatori già affermati, permettono una profonda **integrazione** della conoscenza distribuita e favoriscono la **scoperta** (discovery) di nuove informazioni tramite la navigazione automatica da un nodo all'altro del grafo globale.

## Il problema degli Identificatori: Proliferazione vs Aggregazione

Finora abbiamo definito le regole d'oro per creare il Web dei Dati (coniare URI, usare HTTP, restituire RDF tramite SCBD, e creare link). Ma quando passiamo dalla teoria alla pratica su scala globale, emergono delle sfide ingegneristiche notevoli.

Affrontiamo proprio questi problemi pratici: come gestire l'inevitabile "caos" degli identificatori e, soprattutto, **come pubblicare fisicamente** questi dati affinché siano facilmente consumabili.

Nel framework dei Linked Data, gli URI subiscono un vero e proprio **sovraccarico funzionale (overloading)**: ti servono sia come _identificatori astratti_ (per nominare una cosa) sia come _meccanismo di recupero fisico_ (per scaricare la sua descrizione tramite HTTP).

- **La Proliferazione:** Poiché il Web è aperto e distribuito, chiunque è libero di coniare un nuovo URI per una risorsa. Se io parlo di Roma, conierò `mioSito:Roma`; un altro utente conierà `suoSito:Roma`. Questo crea molteplici URI che si riferiscono alla stessa identica entità nel mondo reale (URI _coreferenti_).
    
- **Il Danno:** Questa proliferazione frammenta la conoscenza. Se le informazioni su Roma sono sparse sotto 10 URI diversi e scollegati, l'aggregazione dei dati (il vero scopo del Web Semantico) fallisce miseramente.
    

**La Soluzione: Riuso e Collegamento**

Per contrastare la frammentazione, le best practice impongono due regole di buon senso:

1. **Riuso dei termini:** Prima di inventare un nuovo URI, controlla se esiste già in _vocabolari popolari_ (es. FOAF per le persone, Dublin Core per i documenti) o in _dataset di terze parti_ consolidati (es. DBpedia, GeoNames). Se esiste, usa quello!
    
2. **Collegamento (Allineamento):** Se devi necessariamente creare un nuovo URI (magari per esigenze interne alla tua azienda), hai l'obbligo morale di **ancorarlo al resto della nuvola (cloud) dei Linked Data**. Se crei una classe, dichiarala sottoclasse (`rdfs:subClassOf`) di una nota; se crei un individuo, collegalo all'individuo globale usando il potente costrutto di equivalenza visto in precedenza: `owl:sameAs`.

## L'Integrazione dei Dati: Un processo in corso

Il Web dei Dati vive di una tensione costante tra due attori:

- **Chi pubblica (Publisher):** Vuole esporre i propri dati rendendoli il più accessibili possibile.
    
- **Chi consuma (Consumer):** Ha il difficile compito di prendere dataset disparati e combinarli per estrarre nuova conoscenza.
    

Il consumatore si scontra con una difficoltà computazionale enorme: **riconoscere che due risorse provenienti da dataset diversi sono in realtà la stessa cosa**. Le slide ci mostrano come questo problema sia affrontato a due livelli distinti (e con terminologie diverse a seconda della comunità scientifica che se ne occupa):

- **A livello di Individui (Istanze):** Capire se `persona_A` e `persona_B` sono la stessa persona umana. Questo processo prende il nome di _Identity Resolution_, _Object Consolidation_ o _Deduplication_ (deduplicazione).
    
- **A livello Concettuale (Classi/Proprietà):** Capire se la classe `Client` del database A è semanticamente equivalente alla classe `Customer` del database B. Questo processo si chiama _Schema Mapping_ o _Ontology Matching_.

## Pubblicazione
### Documenti Statici vs Dinamici

Una volta strutturati e allineati i dati, come li serviamo fisicamente su Internet?

**Approccio 1: Documenti Statici (Sconsigliato per grandi dataset)**

La via più semplice è salvare le descrizioni RDF (es. file `.ttl` o `.rdf`) come normali file su un server web (Apache, Nginx).

- **Il Problema (Inconsistenza):** Ricordi la regola della SCBD (Symmetric Concise Bounded Description) vista prima? Impone che le triple debbano apparire sia nel documento del Soggetto che in quello dell'Oggetto. Se pubblichi file statici, sei costretto a _duplicare_ fisicamente le informazioni in più file. Se un dato cambia, devi aggiornare a mano decine di file testuali. La manutenzione diventa impossibile e porta rapidamente a inconsistenze.

![center|500](img/Pasted%20image%2020260508105251.png)

**Approccio 2: Documenti Dinamici (La via maestra)**

La soluzione moderna è abbandonare i file di testo e inserire tutte le triple in un database ottimizzato per i grafi, chiamato **Triple Store**.

Sopra il Triple Store si espone un _Endpoint SPARQL_ (l'interfaccia per interrogare il database).

Tuttavia, gli esseri umani e i browser web normali non sanno usare SPARQL. Qui entrano in gioco i **Linked Data Frontend (o Linked Data Pubblisher)**:

- **Pubby:** È lo strumento pioniere in questo campo. Funziona come un intermediario intelligente. Quando un browser (HTML) o un client (RDF) richiede un URI dereferenziabile, Pubby "traduce" la richiesta in una query `DESCRIBE` verso il Triple Store. Il database risponde con le triple aggiornate in tempo reale, e Pubby le impagina in HTML per gli umani o le serializza in RDF per le macchine (tramite _content negotiation_). Genera la SCBD dinamicamente, eliminando i problemi di ridondanza!
    
- **LodView e Loddy:** Sono le naturali evoluzioni di Pubby. Pur mantenendo lo stesso principio architetturale (interrogare il Triple Store on-the-fly), offrono un'interfaccia utente (UI) molto più moderna, funzionalità extra per la navigazione visuale del grafo e, nel caso di Loddy (basato su JavaServer Faces), una maggiore facilità di personalizzazione per i web designer.


Come portiamo questo immenso patrimonio preesistente nel Web dei Dati? Il W3C ha sviluppato standard e vocabolari specifici proprio per questo scopo. 

Ne presentano tre fondamentali: **RDB2RDF**, **SKOS** e **Data Cube**.

### RDB2RDF: Dai Database Relazionali ai Linked Data

La stragrande maggioranza delle applicazioni web e dei sistemi informativi aziendali è alimentata da **Database Relazionali (RDB)**, basati su tabelle e SQL. Affinché il Web Semantico decolli davvero, è vitale sbloccare questo enorme bacino di dati e pubblicarlo sotto forma di Linked Data.

- **Il Linguaggio di Mapping (R2RML):** Il gruppo di lavoro W3C RDB2RDF ha standardizzato **R2RML** (_RDB to RDF Mapping Language_). Non si tratta di un software, ma di un linguaggio dichiarativo che permette di scrivere regole precise su come convertire le righe di una tabella SQL in triple RDF (es. definendo che la chiave primaria diventa l'URI del soggetto, i nomi delle colonne diventano i predicati, e i valori delle celle diventano gli oggetti).
    
- **L'Architettura di Pubblicazione:** Come mostra il diagramma nella seconda slide, il processo si interpone tra il Database Relazionale e i Consumatori finali, generando un **Grafo RDF** (che può essere materializzato, cioè esportato fisicamente, oppure _virtuale_, dove le query vengono tradotte al volo in SQL).
    
- **Le due vie di accesso (Consumer):** Una volta applicato il mapping, i dati sono serviti al mondo esterno in due modi:
    
    1. **Accesso via Query (SPARQL):** Per client avanzati che necessitano di fare interrogazioni complesse sul grafo (es. `SELECT * WHERE { ?s ?p ?o }`).
        
    2. **Accesso a livello di Entità (HTTP GET):** Per browser e crawler tradizionali, permettendo la dereferenziazione del singolo URI per ottenerne la descrizione (secondo i principi dei Linked Data visti prima).
        
- **Parallelo storico:** Le slide fanno un paragone molto calzante. Agli albori del Web, la crescita esplosiva fu garantita dalla possibilità di esporre via HTTP l'enorme mole di file già esistenti sui server FTP. RDB2RDF si propone di fare lo stesso salto evolutivo per i dati strutturati.

![center|500](img/Pasted%20image%2020260508110806.png)
### SKOS: Simple Knowledge Organization System

Non tutta la conoscenza è formalizzata in rigide ontologie OWL. Esistono innumerevoli **KOS (Knowledge Organization Systems)** tradizionali: tesauri, glossari, vocabolari controllati e tassonomie (es. classificazioni mediche, indici bibliotecari).

**SKOS** è un vocabolario RDF standard progettato per rappresentare questi sistemi in modo nativo sul Web Semantico. Offre un "percorso veloce" (fast-track) per migrare i KOS esistenti, fornendo la sintassi ma _non_ sostituendo le regole umane con cui questi glossari vengono compilati.

L'architettura di SKOS opera su due livelli:

- **Livello Concettuale (SKOS Base):**
    
    - **`skos:ConceptScheme`:** Rappresenta l'intero vocabolario o tesauro.
        
    - **`skos:Concept`:** L'unità fondamentale. È l'idea o il significato astratto (es. il concetto di "Acqua").
        
    - **Proprietà Lessicali:** A ogni concetto vengono associate delle stringhe di testo (literal) tramite proprietà specifiche:
        
        - `skos:prefLabel`: L'etichetta preferita (una sola per lingua).
            
        - `skos:altLabel`: Etichette alternative (sinonimi, acronimi).
            
        - `skos:hiddenLabel`: Etichette nascoste (es. errori di battitura comuni, utili per i motori di ricerca ma da non mostrare all'utente).
            
    - **Relazioni Semantiche (`skos:semanticRelation`):** Permette di collegare i concetti tra loro in modo meno rigido rispetto a OWL (es. `skos:broader` per i concetti più generali, `skos:narrower` per i più specifici, `skos:related` per concetti affini).
        
- **Livello Lessicale Avanzato (SKOS-XL):** A volte trattare le etichette come semplici stringhe testuali non basta (ad esempio se si vuole studiare l'etimologia di una parola o la relazione tra due sinonimi). **SKOS-XL** trasforma le etichette stesse in risorse dotate di URI (`skosxl:Label`). Questo permette di creare relazioni esplicite _tra le parole stesse_ (`skosxl:labelRelation`), separando nettamente il livello del significato (Concept) da quello linguistico-lessicale (Label).

![center|500](img/Pasted%20image%2020260508110835.png)
### RDF Data Cube Vocabulary

I governi e gli enti di ricerca producono immense quantità di dati statistici (PIL, censimenti, dati meteorologici). Questi dati sono intrinsecamente **multidimensionali** (i famosi "ipercubi" OLAP). Il **Data Cube Vocabulary** (sviluppato dal _W3C Government Linked Data Working Group_) è lo standard per modellare queste statistiche in RDF.

La struttura logica di un Data Cube si basa sui **Componenti**, che si dividono in tre categorie (come illustrato nel grafico cartesiano 3D):

1. **Dimensioni (Dimensions):** Definiscono lo spazio del cubo. Nell'esempio grafico, le dimensioni sono il Sesso (`ex:sex`), il Periodo temporale (`ex:period`) e la Regione geografica (`ex:region`).
    
2. **Misure (Measures):** È il valore reale osservato in uno specifico punto di intersezione delle dimensioni (es. l'Aspettativa di Vita, `eg:lifeExpectancy`).
    
3. **Attributi (Attributes):** Metadati aggiuntivi che qualificano la misura (es. l'unità di misura, se il dato è "stimato" o "definitivo").

![center|500](img/Pasted%20image%2020260508110934.png)

**L'Architettura RDF del Data Cube (Il Diagramma UML):**

Si mostra l'impalcatura che tiene in piedi tutto questo nel grafo:

- Il punto di partenza è il **`qb:DataSet`**.
    
- La "forma" del cubo (quali dimensioni e misure possiede) è definita dalla **`qb:DataStructureDefinition`** tramite specifiche dichiarazioni (`qb:ComponentSpecification`).
    
- I dati veri e propri sono contenuti nelle **`qb:Observation`**. Un'osservazione è letteralmente un punto nello spazio: avrà dei valori per ogni Dimensione e un valore per la Misura.
    
- Per organizzare grandi moli di dati, le osservazioni possono essere raggruppate in "fette" (**`qb:Slice`**), ad esempio "Tutte le aspettative di vita in Italia nel 2023 per ogni sesso".

![center|500](img/Pasted%20image%2020260508110950.png)

**L'integrazione con altri standard:**

Il Data Cube non reinventa la ruota. Per dichiarare i "concetti" alla base delle sue dimensioni (es. "Sesso" o "Area di Riferimento"), si appoggia costantemente ad altri due standard:

- **SKOS:** Utilizzato per definire le liste di codici (Code Lists), ad esempio l'elenco standard delle regioni.
    
- **SDMX (Statistical Data and Metadata eXchange):** Lo standard ISO preesistente per i dati statistici. Il vocabolario Data Cube importa direttamente i concetti SDMX (`sdmx-concept:sex`, `sdmx-concept:refArea`) garantendo immediata interoperabilità con i sistemi degli istituti di statistica tradizionali.

### Embedded RDF: Fondere dati e documenti

Finora abbiamo parlato di come pubblicare interi dataset e ontologie su server dedicati (i _Triple Store_). Ma cosa succede se un utente o un'azienda possiede solo un normale sito web e **non può pubblicare nient'altro che semplici pagine (X)HTML**?

Come facciamo a far capire alle macchine il significato del testo scritto in una pagina web tradizionale? La risposta è l'**Embedded RDF** (RDF incorporato) e l'**Annotazione Semantica**.

L'obiettivo dell'Embedded RDF è prendere i dati strutturati (le triple S-P-O) e "nasconderli" all'interno del codice sorgente di una normale pagina web, in modo che il browser continui a mostrare il testo formattato per gli umani, ma i _crawler_ (i bot che leggono le pagine) possano estrarre il grafo logico sottostante.

Esistono due approcci principali per farlo, standardizzati nel tempo:

**A. Dati inframezzati al contenuto visibile (Interleaved)**

In questo approccio, si usano attributi speciali direttamente dentro i tag HTML esistenti (`<span>`, `<div>`, `<a>`) per "etichettare" le parole mostrate a schermo.

- **RDFa (RDF in Attributes):** È lo standard W3C più rigoroso per fare questo. Come mostra l'esempio nelle slide, permette di usare attributi come `about=` (per definire il Soggetto/URI), `property=` (per il Predicato) e `content=` (per l'Oggetto testuale). Se in una pagina c'è scritto "Wikinomics di Don Tapscott", RDFa trasforma invisibilmente quel testo nella tripla Turtle: `:wikinomics dc:creator "Don Tapscott"`.
    
- **Microformati e Microdata:** Sono tecnologie simili nate per HTML5. Sebbene i _microdata_ condividano lo stesso scopo (usando attributi come `itemprop`), la slide precisa giustamente che _non_ sono legati esplicitamente al modello formale astratto di RDF, risultando meno rigorosi ma storicamente molto diffusi.
    

**B. Dati isolati dal contenuto visibile**

Invece di "sporcare" tutto il codice HTML con decine di attributi sparsi in ogni paragrafo (pratica che fa impazzire i web designer e rischia di rompersi se si cambia l'impaginazione), si crea un blocco dati separato, nascosto all'utente ma perfettamente leggibile dalle macchine.

- **JSON-LD (JavaScript Object Notation for Linked Data):** È il vincitore assoluto sul web moderno. È una sintassi RDF basata su JSON che viene inserita semplicemente all'interno di un tag `<script type="application/ld+json">` nell'intestazione (head) della pagina web.
    
#### Il Motore del Cambiamento: La SEO e Schema.org

Perché un'azienda dovrebbe spendere tempo e soldi per annotare semanticamente le proprie pagine web in RDFa o JSON-LD? Per molto tempo, la mancanza di incentivi commerciali ha frenato il Web Semantico.

La svolta è arrivata quando i giganti della ricerca (**Google, Bing, Yahoo! e Yandex**) si sono resi conto che l'intelligenza artificiale e la semantica servivano per fornire risultati migliori.

Hanno quindi fondato il progetto **Schema.org**. Non si tratta di una nuova sintassi, ma di un **vocabolario condiviso universale**. Invece di far inventare a ogni sviluppatore le proprie classi, Schema.org fornisce le definizioni ufficiali per descrivere qualsiasi cosa: un `Product`, una `Person`, un `Event`, una `Recipe`, ecc.

L'incentivo per i webmaster è diventato l'**Ottimizzazione per i Motori di Ricerca (SEO)**. Se annoti la tua pagina seguendo le linee guida di Google, usando il vocabolario _Schema.org_ (preferibilmente serializzato in _JSON-LD_, come raccomandato da Google stessa), il motore di ricerca non dovrà "tirare a indovinare" di cosa parla la tua pagina, ma avrà il grafo dei dati servito su un piatto d'argento.

#### I Risultati Pratici: Le "Search Result Features"

Cosa succede quando Google legge questi dati strutturati perfettamente formattati? Trasforma i classici, noiosi link blu in risultati arricchiti, chiamati **Rich Snippets** o _Search Result Features_.

La tua ultima slide mostra l'esempio perfetto, che tutti noi vediamo quotidianamente: la ricetta degli "Spaghetti Cacio e Pepe".

Senza annotazione semantica, Google mostrerebbe solo il titolo e un pezzo di testo a caso.

Grazie ai dati strutturati incorporati nella pagina web (che dichiarano esplicitamente `Type: Recipe`), Google estrae le singole entità logiche e costruisce una "scheda" interattiva che mostra:

- **L'Immagine (Picture):** Associata al predicato semantico dell'immagine del piatto.
    
- **La Valutazione (Rating):** Le famose stelline gialle (es. 4.5 su 228 voti), derivanti dal tipo `AggregateRating`.
    
- **Il Tempo di Cottura (Total time):** Estratto dal predicato specifico `totalTime` (es. 20 min).
    
- **La Descrizione (Dish description):** Il riassunto puntuale.
    

**In conclusione:**

Questo processo chiude il cerchio. Il Web Semantico non è rimasto un puro esercizio accademico relegato alla logica formale (OWL) o a database accademici. Attraverso l'annotazione semantica (JSON-LD) e vocabolari pragmatici (Schema.org), **il grafo della conoscenza è letteralmente fuso nel Web di tutti i giorni**, permettendo ai motori di ricerca di capire il mondo e agli utenti di trovare risposte precise e strutturate in millisecondi.

## VoID

Nel Web dei Dati, pubblicare un dataset RDF su un server non basta. Se non fornisci delle istruzioni chiare alle macchine su _cosa_ contiene quel dataset, _chi_ lo ha creato e _come_ interrogarlo, i tuoi dati saranno invisibili.

Per risolvere questo problema, nasce **VoID (Vocabulary of Interlinked Datasets)**: un vocabolario RDF standardizzato dal W3C progettato per creare i "metadati" dei tuoi Linked Data.

### La base di VoID: `void:Dataset`

Il cuore dell'ontologia è la classe principale **`void:Dataset`**.

Un dataset in VoID è definito come un insieme di triple RDF che sono pubblicate, mantenute o possedute da una singola entità. Quando descrivi il tuo grafo, la prima cosa che fai è dichiarare che il tuo progetto è un'istanza di questa classe.

VoID divide poi la descrizione del dataset in quattro grandi categorie di metadati:

![center|500](img/Pasted%20image%2020260508140909.png)

![center|500](img/Pasted%20image%2020260508140932.png)
#### A. Metadati Generali (General Metadata)

VoID non reinventa la ruota. Per descrivere le informazioni di base, suggerisce di riutilizzare vocabolari già famosissimi, primo fra tutti il **Dublin Core (`dcterms`)** e **FOAF**. Nelle slide vediamo l'uso di:

- `dcterms:title`: Il nome del dataset.
    
- `dcterms:description`: Un riassunto testuale di cosa contiene.
    
- `dcterms:creator` o `dcterms:publisher`: Chi ha creato o gestisce i dati.
    
- `dcterms:created` e `dcterms:modified`: Le date del ciclo di vita.
    
- `dcterms:subject`: L'argomento del dataset, spesso associato a concetti presi dalla DBpedia o da altre ontologie esterne.

![center|500](img/Pasted%20image%2020260508141100.png)

![center|500](img/Pasted%20image%2020260508141153.png)

![center|500](img/Pasted%20image%2020260508141219.png)
#### B. Metadati di Accesso (Access Metadata)

Queste sono le istruzioni tecniche per i software. Dicono a un client: "Ecco come puoi tecnicamente mettere le mani sulle mie triple". Si usano proprietà specifiche di VoID o FOAF:

- **`void:sparqlEndpoint`**: Fornisce l'indirizzo HTTP esatto del motore di ricerca dove il client può lanciare query SPARQL.
    
- **`void:dataDump`**: Fornisce il link diretto per scaricare l'intero archivio RDF in blocco (es. un file `.nt` o `.rdf` compresso).
    
- **`void:uriLookupEndpoint`**: L'indirizzo di base usato per la dereferenziazione (la ricerca tramite HTTP GET dei singoli URI).
    
- **`foaf:homepage`**: Il link a una pagina web in HTML leggibile da esseri umani che presenta il dataset.
    

#### C. Metadati Strutturali (Structural Metadata)

Queste sono le "statistiche" vitali del tuo grafo. Danno l'idea della grandezza e della ricchezza semantica del dataset, elementi cruciali per chi vuole riutilizzare i tuoi dati.

- **`void:triples`**: Il numero totale stimato di triple presenti nel dataset.
    
- **`void:classes`** e **`void:properties`**: Il numero di classi e predicati distinti utilizzati.
    
- **`void:entities`**: Il numero di individui (risorse) distinti.
    
- **`void:vocabulary`**: Una dichiarazione estremamente utile. Dice esplicitamente quali vocabolari esterni hai usato per modellare i tuoi dati (es. se indichi FOAF e SKOS, chi consuma i dati sa già che tipo di struttura aspettarsi).
    

#### D. La Descrizione dei Link (`void:Linkset`)

Questa è la caratteristica più potente e unica di VoID, e risponde alla Regola n.4 dei Linked Data (collegarsi al resto del mondo).

Un **Linkset** è esso stesso una sottoclasse di `void:Dataset`. Rappresenta un "pacchetto" di triple il cui **unico scopo è fare da ponte tra il tuo dataset e un dataset bersaglio (target)**.

Per definire un Linkset, VoID usa queste proprietà:

- **`void:target`**: Si indicano i due dataset che vengono messi in comunicazione.
    
- **`void:linkPredicate`**: Si specifica _quale predicato RDF_ viene usato per creare i ponti. Nella stragrande maggioranza dei casi (es. per allinearsi a DBpedia), questo predicato è `owl:sameAs`.
    
- Proprio come un dataset normale, anche un Linkset può avere la proprietà `void:triples` per indicare esattamente _quanti_ link fisici esistono tra i due grafi.