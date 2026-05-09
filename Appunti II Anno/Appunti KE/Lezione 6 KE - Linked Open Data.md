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

![center|500](img/Pasted%20image%2020260509161948.png)

#### C. Metadati Strutturali (Structural Metadata)

I metadati strutturali forniscono informazioni preziose sull'organizzazione interna e sulle dimensioni del dataset. Questo è cruciale per i consumatori di dati, in quanto permette loro di valutare se il dataset è adatto ai loro scopi prima di interrogarlo o scaricarlo.

I metadati strutturali in VoID si dividono in diverse aree chiave: esempi, partizioni e statistiche.

##### 1. Orientamento Iniziale: Esempi e Vocabolari

Prima di addentrarsi nei numeri, VoID permette di fornire un "assaggio" del dataset:

- **Risorse di esempio (`void:exampleResource`):** Questa proprietà collega il dataset ad alcune risorse rappresentative. L'obiettivo è dare all'utente un'idea immediata del tipo di dati presenti, senza dover esplorare l'intero grafo.
	- ![center|500](img/Pasted%20image%2020260509162505.png)    
- **Vocabolari utilizzati (`void:vocabulary`):** Elenca i vocabolari fondamentali (come FOAF, Dublin Core, ecc.) impiegati nel dataset. Questo è essenziale per sapere quali termini (classi e proprietà) usare quando si interroga il dataset tramite SPARQL.
    
    - ![center|500](img/Pasted%20image%2020260509162619.png)
- **Spazio degli URI (`void:uriSpace` e `void:uriRegexPattern`):** Definisce lo spazio dei nomi (namespace) o i pattern che accomunano gli URI delle risorse descritte nel dataset.
    
    - `void:uriSpace` indica un prefisso comune, ad esempio: ![center|500](img/Pasted%20image%2020260509162543.png)
        
    - Per scenari complessi, `void:uriRegexPattern` permette di usare un'espressione regolare che gli URI del dataset devono soddisfare.
        
##### 2. Organizzazione Interna: Sottoinsiemi e Partizioni

Spesso i dataset sono molto grandi e complessi. VoID permette di descrivere l'architettura interna usando la proprietà `void:subset`, che collega un dataset principale a un suo sottoinsieme (anch'esso di tipo `void:Dataset`). 

![center|500](img/Pasted%20image%2020260509162709.png)

![center|500](img/Pasted%20image%2020260509162739.png)

Questo permette di assegnare metadati specifici solo a certe parti del grafo.

VoID offre costrutti per definire due tipi specifici di partizioni logiche (entrambe sono sottoclassi di `void:Dataset`):

- **Partizioni basate sulle Classi (`void:classPartition`):** Definisce un sottoinsieme che contiene solo le istanze di una specifica classe.
    
    - _Esempio:_ Un sottoinsieme che raggruppa solo le istanze di tipo `foaf:Organization`. ![center|500](img/Pasted%20image%2020260509162759.png)
        
- **Partizioni basate sulle Proprietà (`void:propertyPartition`):** Definisce un sottoinsieme che contiene esclusivamente le triple che utilizzano un determinato predicato.
    
    - _Esempio:_ Un sottoinsieme contenente solo le triple che usano la proprietà `foaf:homepage`. ![center|500](img/Pasted%20image%2020260509162812.png)

##### 3. Informazioni Statistiche

L'aspetto forse più quantitativo dei metadati strutturali sono le statistiche. VoID definisce proprietà specifiche per quantificare i vari elementi del grafo. È importante notare che queste stesse proprietà possono essere usate anche per descrivere le partizioni (class/property-based) viste sopra.

Ecco le proprietà statistiche principali:

- **`void:triples`:** Il numero totale di triple contenute nel dataset.
    
- **`void:entities`:** Il numero totale di entità (risorse con un URI che rispetta l'eventuale `void:uriRegexPattern`) descritte nel dataset.
    
- **`void:classes`:** Il numero di classi _distinte_ presenti nel dataset (cioè gli URI unici che compaiono come oggetto in triple con predicato `rdf:type`).
    
- **`void:properties`:** Il numero di proprietà _distinte_ utilizzate nel dataset (gli URI unici che compaiono nella posizione del predicato).
    
- **`void:distinctSubjects`:** Il numero di soggetti (URI o blank node) _distinti_ presenti nel dataset.
    
- **`void:distinctObjects`:** Il numero di oggetti (URI, blank node o letterali) _distinti_ presenti nel dataset.
    
- **`void:documents`:** Questa proprietà indica il numero totale di documenti (es. file RDF/XML o pagine RDFa), ed è destinata a dataset in cui è difficile determinare il numero esatto di triple o entità.

![center|500](img/Pasted%20image%2020260509162847.png)

![center|500](img/Pasted%20image%2020260509162930.png)

La maggior parte di queste statistiche non deve essere calcolata a mano, ma può essere derivata automaticamente eseguendo specifiche query SPARQL sul dataset.
#### D. La Descrizione dei Link (`void:Linkset`)

Questa è la caratteristica più potente e unica di VoID, e risponde alla Regola n.4 dei Linked Data (collegarsi al resto del mondo).

Un **Linkset** (rappresentato dalla classe `void:Linkset`) è, concettualmente, un tipo speciale di dataset. La sua particolarità è che contiene _esclusivamente_ triple il cui scopo è collegare un soggetto che risiede in un dataset a un oggetto che risiede in un _altro_ dataset.

Per definire un Linkset, VoID usa queste proprietà:
##### 1. Definire i Target (Le estremità del ponte)

Per prima cosa, devi dichiarare quali sono i due dataset messi in comunicazione dal linkset.

- **`void:target`:** È la proprietà generica. Dichiari semplicemente che il linkset connette il Dataset A e il Dataset B, senza specificare la direzione della connessione.
    
    - _Esempio:_ ![center|500](img/Pasted%20image%2020260509163547.png)

- **`void:subjectsTarget` e `void:objectsTarget`:** Queste due proprietà specializzano `void:target` e offrono una precisione maggiore. Ti permettono di indicare la _direzione_ dei link, specificando in quale dataset si trovano i soggetti delle triple e in quale si trovano gli oggetti.
    
    - _Esempio:_ ![center|500](img/Pasted%20image%2020260509163637.png)

##### 2. L'Appartenenza del Linkset (Dove si trova il ponte?)

I link (le triple di connessione) possono essere fisicamente ospitati all'interno di uno dei due dataset collegati, oppure possono risiedere in un terzo dataset indipendente (un hub di collegamento).

Le slide affrontano il caso più comune: i link sono forniti da uno dei due dataset stessi (ad esempio, il mio dataset contiene i link `owl:sameAs` che puntano a DBpedia).
In questo scenario, la best practice di VoID è dichiarare che il Linkset è un **sottoinsieme (`void:subset`)** del dataset che lo ospita.

##### 3. Il Predicato di Collegamento (`void:linkPredicate`)

Questa è un'informazione cruciale per i software che consumano i dati. Oltre a sapere quali dataset sono collegati, devono sapere *come* sono collegati. Qual è la natura semantica della relazione?

La proprietà **`void:linkPredicate`** indica l'URI della proprietà RDF utilizzata per formare i link all'interno di quel linkset.

*   *L'uso più frequente:* Nella stragrande maggioranza dei casi nel mondo dei Linked Open Data, lo scopo di un linkset è dichiarare che un'entità in un dataset è esattamente la stessa entità in un altro. In questo caso, il predicato è `owl:sameAs`.
    *   *Esempio:* ![center|500](img/Pasted%20image%2020260509163717.png)

##### 4. Quantificare i Link (`void:triples`)

Infine, come per qualsiasi altro dataset o sottoinsieme, è prassi comune indicare le dimensioni del linkset utilizzando la proprietà statistica `void:triples`.

*   *Esempio:* `void:triples 1000` indica che ci sono mille connessioni esatte (mille "ponti") tra i due dataset bersaglio all'interno di questo specifico linkset. Questa informazione aiuta a valutare quanto forte e integrata sia la connessione tra le due fonti di dati.

## Consumare i LD

È il momento di passare dall'altra parte della barricata. Finora abbiamo visto come _pubblicare_ e descrivere i dati. Ora esaminiamo come le applicazioni e gli sviluppatori possono **consumare** (utilizzare e interrogare) questa immensa nuvola di Linked Data distribuita sul web.

### 1. Dove cercare i dati? (Discovery)

Prima di consumare i dati, devi trovarli. La nuvola dei Linked Open Data (LOD) non ha un unico punto di accesso centrale. Le slide elencano diverse fonti primarie per la ricerca:

- **Data Hub (datahub.io):** Una directory storica di dataset (costruita con CKAN). È un catalogo generale dove cercare set di dati aperti.
    
- **Linked Open Vocabularies (LOV):** Questo non è un catalogo di _dati_ puri, ma una rete di _vocabolari_ (schemi RDF e ontologie OWL). Se devi modellare un nuovo dominio, cerchi qui per vedere se esiste già un'ontologia da riutilizzare.
    
- **Entity Name System (ENS):** Sono _authority_ specializzate che assegnano identificatori canonici a specifiche entità (es. luoghi, persone famose). Se ti serve l'URI ufficiale di "Roma", lo cerchi in un ENS.
    
- **Portali Governativi e Settoriali:** Molte nazioni hanno i propri portali Open Data (spesso basati su CKAN) come `dati.gov.it` o `data.gov`. Esistono poi istituti di statistica (ISTAT, Eurostat) e portali settoriali verticali (es. BioPortal per le scienze della vita).
### 2. Consumare LD: Dereferenziazione

Il metodo più basilare per consumare i Linked Data è sfruttare la regola fondamentale degli URI HTTP: la dereferenziazione.

- **Come funziona:** L'applicazione invia una semplice richiesta HTTP GET all'indirizzo URI della risorsa di interesse. Il server risponde restituendo il documento RDF che descrive quella specifica risorsa (spesso usando il pattern SCBD visto nelle lezioni precedenti).
    
- **Chi lo usa:** I browser semantici (come Tabulator o Disco) navigano il grafo in questo modo, "cliccando" da un URI all'altro. Esistono anche linguaggi di interrogazione specializzati (come _LD Path_) che formulano query semplici seguendo questi "cammini" diretti.
    
- **Pro e Contro:**
    
    - _Pro:_ Massima **freschezza dell'informazione**. Ottieni il dato esatto nel momento in cui lo richiedi, direttamente dalla fonte.
        
    - _Contro:_ Elevata **latenza** (ogni salto nel grafo richiede una nuova chiamata HTTP). Crea un forte **carico sull'infrastruttura** di chi pubblica i dati (che riceve continue richieste GET). Inoltre, l'**espressività è limitata**: non puoi fare query complesse o aggregazioni globali.
        
### 3. Consumare LD: SPARQL Federato

Se la dereferenziazione è troppo lenta per query complesse, l'alternativa è usare **SPARQL**, il linguaggio di interrogazione ufficiale.

- **L'Endpoint SPARQL:** Un publisher serio dovrebbe offrire un _endpoint SPARQL_ pubblico per consentire un accesso efficiente ai propri dati.
    
- **Il problema della distribuzione:** Cosa succede se la mia query ha bisogno di unire i dati sui politici europei (su un endpoint) con i dati sui loro partiti (su un altro endpoint)?
    
- **La soluzione: SPARQL 1.1 Federated Query:** Questa estensione dello standard introduce la keyword `SERVICE`. Come mostriamo nell'esempio, si può scrivere una singola query in cui deleghi esplicitamente una _sotto-query_ (la parte dentro le parentesi graffe di `SERVICE`) a un endpoint remoto.
    
- **Il collo di bottiglia:** L'esperienza derivata dai vecchi database relazionali distribuiti ci insegna che è **molto difficile ottimizzare** l'esecuzione di queste query. Se sbagli l'ordine con cui chiami i vari `SERVICE`, rischi di trasferire gigabyte di dati inutili sulla rete, bloccando l'applicazione.

![center|500](img/Pasted%20image%2020260509171437.png)
### 4. Consumare LD: SPARQL Euristico

Il limite più grande dello SPARQL Federato standard è che _devi conoscere a priori_ l'indirizzo esatto di tutti gli endpoint che contengono i dati necessari.

In un Web dei Dati aperto e organico, questo è spesso irrealistico (non sai in anticipo chi ha pubblicato cosa).

- **L'Approccio Ibrido:** Per superare questo limite, i ricercatori hanno sviluppato approcci "ibridi" (o basati su _link traversal_).
    
- **Come funziona:** L'applicazione riceve una normale query SPARQL (senza la clausola `SERVICE`). Il motore di esecuzione inizia a valutare la query e, usando delle **euristiche**, analizza in tempo reale i risultati parziali o i link scoperti nel grafo locale. Man mano che scopre nuovi URI rilevanti, va a dereferenziarli al volo per scaricare i "dati necessari" mancanti.
    
- **Pro e Contro:** È un approccio molto flessibile per interrogare la nuvola in modo dinamico, ma a causa della natura euristica (va a "tentativi" guidati), _non può garantire la piena conformità alla semantica formale di SPARQL_ (potrebbe perdersi dei dati validi nascosti in parti del web non esplorate).
    
### 5. Consumare LD: Linked Data Fragments (LDF)

C'è un conflitto fondamentale nell'ecosistema: offrire un semplice data dump (scaricare l'intero file) ha un costo bassissimo per il server ma è terribile per il client; viceversa, offrire un endpoint SPARQL potentissimo è fantastico per il client, ma ha un **costo altissimo per il server** (che spesso va offline se riceve query complesse).

I **Linked Data Fragments (LDF)** nascono per trovare una via di mezzo, bilanciando il carico tra client e server.

- **Il Concetto:** Invece di chiedere al server di risolvere l'intera query complessa (SPARQL), o di scaricare l'intero database (Data Dump), il client richiede al server solo "frammenti" specifici del grafo.
    
- **Triple Pattern Fragment (TPF):** È il tipo più comune di LDF. Il server non accetta query SPARQL complete, ma accetta solo semplici "Triple Pattern" (es. "Dammi tutte le triple dove il soggetto è Roma e il predicato è Popolazione").
    
- **Come funziona:** Il server (che ora ha un compito facilissimo e non va in crash) restituisce la pagina con i dati richiesti, ma aggiunge dei **metadati** (es. "Ci sono in totale 10.000 risultati") e dei **controlli** (es. link ipertestuali per chiedere la "Pagina 2", "Pagina 3" dei risultati).
    
- Il grosso del lavoro computazionale (unire i vari frammenti, filtrare, ordinare) viene spostato sul software del client.
### 6. Consumare LD: L'Approccio Crawler (Data Warehousing)

Tutti i metodi visti finora interrogano il Web "in diretta". Ma per le applicazioni enterprise che richiedono altissima affidabilità e velocità, dipendere dalla rete in tempo reale è un rischio. La soluzione finale è l'approccio tramite **Crawler** (il modello Data Warehouse).

- **Cos'è un Crawler LD:** È un "bot" (un agente software, es. _LDspider_) che naviga instancabilmente la nuvola dei Linked Data seguendo i link, con lo scopo di **raccogliere informazioni**.
    
- **Il Processo:** Il crawler scarica i dati e crea una **copia locale (cache)** sul tuo server aziendale.
    
- **L'Elaborazione (Data Access, Integration and Storage Layer):** Una volta che hai i dati in casa (nel tuo Triple Store integrato), puoi elaborarli pesantemente offline. Come mostrano gli schemi architetturali, questa fase (gestita da framework come LDIF) include:
    
    1. _Schema mapping_ (tradurre vocaboli esterni nei tuoi vocaboli interni).
        
    2. _Object consolidation/Identity Resolution_ (fondere entità che sono la stessa cosa).
        
    3. _Quality management/Data Fusion_ (valutare di quali fonti fidarsi di più e pulire i dati).
        
- **Pro e Contro:** L'applicazione finale interroga solo il database locale super-ottimizzato tramite un'API locale, garantendo velocità e permettendo ragionamenti logici complessi senza caricare i server pubblici. Il compromesso è che i dati nella cache potrebbero non essere freschi, richiedendo al crawler cicli di aggiornamento continui.

![center|500](img/Pasted%20image%2020260509171549.png)

![center|500](img/Pasted%20image%2020260509171603.png)

---
# Note Finali

Chiudiamo l'argomento analizzando i limiti della semantica pura, il motivo per cui questo movimento è nato e la fondamentale distinzione tra "Dati Collegati" (Linked Data) e "Dati Aperti" (Open Data).
## 1. Oltre la semantica RDF: Il problema del mondo reale

Tutta l'infrastruttura logica che abbiamo studiato (RDF, OWL) si basa su un assunto matematico fondamentale: **assume che le triple siano accurate**. Se in un grafo c'è scritto che "Parigi è la capitale della Germania", il motore di inferenza lo accetta come una verità assoluta e ci ragiona sopra.

Tuttavia, quando passiamo dall'accademia al contesto distribuito della _Linked Data cloud_, navigando tra migliaia di dataset disparati creati da sconosciuti, questa assunzione crolla. Emergono quindi tre problemi cruciali che vanno "oltre" la semantica:

- **Tracking Provenance (Tracciamento della provenienza):** Chi ha generato questo dato? Da quale database originale è stato estratto?
    
- **Judging Trustworthiness (Valutazione dell'affidabilità):** Posso fidarmi di chi ha pubblicato questo dato? È un istituto di statistica ufficiale o un utente anonimo?
    
- **Evaluating Data Quality (Qualità del dato):** I dati sono aggiornati, formattati correttamente e privi di refusi?
    

Questi problemi sono facilmente gestibili all'interno di applicazioni chiuse che usano pochi dataset super-controllati, ma diventano **estremamente difficili da risolvere in generale** sull'intera nuvola globale dei Linked Data.

## 2. Perché i Linked Data? (La "Liberazione" dei Dati)

Perché fare tutta questa fatica? Oggi i grandi fornitori del web (Google, Meta, X) sono molto "felici" di fornire agli sviluppatori delle API (interfacce di programmazione) per invocare i propri servizi. Tuttavia, sono **timorosi di condividere i dati veri e propri**. Questo fenomeno è noto come **"database hugging"** (tenersi stretti i propri database per mantenere il monopolio dell'informazione).

Il cuore del movimento dei Linked Data è l'esatto opposto: promuove la **liberazione dei dati nella loro forma grezza**. Solo mettendo a disposizione degli sviluppatori di tutto il mondo i dati puri e interconnessi, si creano i presupposti per la nascita di scenari d'uso innovativi e applicazioni che i creatori originali del dato non avrebbero mai potuto immaginare.
## 3. Open Data e Open Government

Questa spinta alla "liberazione" si sposa perfettamente con il movimento dell'Open Data.

- **Definizione di Open Data:** Secondo la Open Definition, un dato è considerato "aperto" se **chiunque è libero di usarlo, riusarlo e ridistribuirlo**. Le uniche condizioni generalmente imposte sono la richiesta di _attribuzione_ (citare la fonte) o la condivisione _allo stesso modo_ (share-alike, ovvero se modifichi il dato devi ripubblicarlo aperto).
    
- **L'Open Government:** È il risvolto politico e civico di questo fenomeno. Il movimento chiede alle Pubbliche Amministrazioni di aprire i propri database per due motivi inattaccabili:
    
    1. I dati sono stati raccolti e gestiti usando i soldi dei contribuenti, quindi appartengono ai cittadini.
        
    2. Esiste una fondamentale esigenza democratica di trasparenza.
        
- I frutti di questo movimento sono i **grandi portali governativi**, come _data.gov_ negli Stati Uniti, _data.gov.uk_ nel Regno Unito e _dati.gov.it_ in Italia.
    
## 4. La matrice finale: Open Data vs Linked Data

Arriviamo al chiarimento definitivo. Spesso i termini vengono confusi, ma **Open Data e Linked Data sono concetti ortogonali** (cioè indipendenti l'uno dall'altro).

La matrice nella tua ultima slide li divide in due dimensioni:

1. **Dimensione relativa alla Licenza (Legale):** Dati Aperti (Open data) contro Dati Chiusi/Proprietari (Closed data).
    
2. **Dimensione relativa alla Pubblicazione (Tecnica):** Dati Scollegati (Unlinked Data, come un PDF o un file Excel isolato) contro Dati Collegati (Linked Data, formattati in RDF).
    

Da questo incrocio capiamo che:

- Un dato può essere **Open ma non Linked:** Ad esempio, il bilancio del tuo Comune caricato online in un file PDF. Tutti possono vederlo (è Open), ma nessuna macchina può incrociarlo con altri dati in automatico (è Unlinked).
    
- Un dato può essere **Linked ma non Open:** Ad esempio, il grafo delle conoscenze interne della CIA o i dati clinici dei pazienti di un ospedale. Sono formattati in RDF e iper-connessi tra loro, ma sono rigorosamente chiusi al pubblico per motivi di sicurezza o privacy.
    

**Il trionfo dei LOD (Linked Open Data):**

Il vero ecosistema del Web Semantico nasce nel quadrante in alto a destra, dove le due dimensioni si incontrano.

- I **Linked Data** forniscono i _mezzi tecnici_ avanzati per permettere il riuso e l'integrazione delle informazioni.
    
- Gli **Open Data** forniscono la licenza legale e la _massa critica_ (il volume di dati) necessaria affinché questo fenomeno globale possa avere successo.