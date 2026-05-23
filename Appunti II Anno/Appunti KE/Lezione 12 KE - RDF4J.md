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
# Gestione dei dati RDF con Eclipse RDF4J

## Architettura ed Ecosistema

**Eclipse RDF4J**, precedentemente conosciuto come OpenRDF Sesame, è un framework basato su Java progettato specificamente per l'elaborazione di dati RDF. La sua funzione principale è fornire agli sviluppatori un set di strumenti completi per gestire ogni aspetto del ciclo di vita dei dati RDF all'interno di applicazioni Java.

Le sue capacità operative coprono diverse aree fondamentali. Permette, innanzitutto, di rappresentare termini e _statement_ RDF nativamente nel codice Java e di leggere o scrivere questi dati utilizzando varie sintassi concrete. Offre inoltre la possibilità di interfacciarsi con i database RDF, noti come _triplestore_, sia che questi siano integrati direttamente nell'applicazione, sia che si trovino su server remoti. Oltre all'accesso ai dati, il framework gestisce nativamente lo storage, l'indicizzazione, l'esecuzione di query e i processi di inferenza sui dati RDF.

Questo ecosistema si rivolge principalmente a due tipologie di utenti. Da un lato, ci sono gli sviluppatori di applicazioni per il Web Semantico, che necessitano di strumenti robusti per memorizzare ed elaborare i dati. Dall'altro, ci sono gli implementatori di triplestore stessi; questi ultimi possono trarre vantaggio dall'architettura stratificata e modulare del framework, utilizzando i suoi componenti già pronti per leggere e scrivere le sintassi più comuni, effettuare il parsing e valutare le query.

Per quanto riguarda la memorizzazione dei dati, il framework include nativamente due diverse implementazioni di triplestore, pensate per scenari differenti. La prima è il _Memory store_, ideale per dataset di piccole dimensioni che possono essere mantenuti interamente nella memoria RAM disponibile, offrendo comunque l'opzione di rendere i dati persistenti su disco. La seconda è il _Native store_, progettato per dataset di medie dimensioni (fino a circa 100 milioni di triple), che basa sia la memorizzazione che l'elaborazione direttamente su disco. È comunque garantita la flessibilità di integrare triplestore commerciali di terze parti, a patto che questi si conformino all'architettura generale del framework.

L'architettura del sistema è fortemente stratificata. Alla base si trova l'RDF Model, che rappresenta le fondamenta dei dati. Sopra di esso operano moduli specifici come le Sail API, Rio (dedicato all'input/output) e un HTTPClient. Salendo di livello, troviamo le implementazioni dei repository (come SailRepository e HTTPRepository), che sono gestite attraverso la Repository API. È proprio a questo livello più alto, o tramite un HTTP Server, che l'applicazione finale interagisce con il framework. L'HTTPClient ha inoltre il compito di gestire le comunicazioni esterne, ad esempio interfacciandosi con un server HTTP remoto.

![center|500](img/Pasted%20image%2020260522104350.png)

Dal punto di vista della configurazione e dell'integrazione, l'uso del framework è reso molto snello grazie alla pubblicazione dei suoi artefatti su Maven Central. In un progetto basato su Apache Maven, è sufficiente includere le dipendenze desiderate nel file POM. Spesso basta aggiungere una singola dipendenza "raccoglitore", come `rdf4j-client` o `rdf4j-storage` (tipicamente con `<type>pom</type>`), per importare a cascata tutti i moduli necessari. A livello di configurazione del progetto, è raccomandato impostare le proprietà del compilatore Maven (source e target) alla versione 1.8 di Java.

Proprio in relazione a Java 8, c'è un dettaglio tecnico importante che riguarda la gestione delle eccezioni. In passato, con OpenRDF Sesame, la maggior parte delle eccezioni era di tipo _checked_, il che obbligava lo sviluppatore a gestirle esplicitamente in blocchi try-catch o a dichiararle nella clausola `throws` dei metodi. Con il passaggio ad Eclipse RDF4J, le eccezioni specifiche del framework sono state convertite in tipo _unchecked_. Questo significa che non è più obbligatorio dichiararle se non vengono gestite internamente. Questa scelta architetturale non è casuale, ma è stata motivata principalmente dalla volontà di rendere il framework pienamente compatibile e più facile da utilizzare in combinazione con le _lambda expression_ introdotte in Java 8.
## Il Package Model

Il package **Model** di Eclipse RDF4J rappresenta il nucleo concettuale per la gestione dei dati, fornendo le interfacce fondamentali per rappresentare i termini RDF, gli _statement_ e le loro collezioni, denominate **modelli**. Per supportare la manipolazione degli statement RDF direttamente in memoria, il framework mette a disposizione specifiche implementazioni di questi modelli, come le classi `LinkedHashModel` e `TreeModel`.

### La Gerarchia dei Termini RDF

Il framework modella i termini RDF attraverso una gerarchia di interfacce ben definita e tipizzata:

- **Value:** È l'interfaccia radice della gerarchia. Espone il metodo `stringValue()`, che restituisce la stringa rappresentativa del valore. Da questa interfaccia derivano due rami principali: `Resource` e `Literal`.
    
- **Resource:** È l'interfaccia che definisce le risorse generali. Da essa derivano:
    
    - **IRI:** Rappresenta un identificatore di risorsa internazionale. Tra le sue funzioni espone il metodo `getLocalName()`.
        
    - **BNode:** Rappresenta un _Blank Node_ (nodo anonimo). Mette a disposizione il metodo `getID()` per recuperare l'identificatore del nodo.
        
- **Literal:** Rappresenta un valore letterale (es. stringhe, numeri, date). È dotata di metodi specifici per estrarre le sue componenti interne: `getLabel()` (restituisce il valore testuale), `getDatatype()` (restituisce un IRI che descrive il tipo di dato) e `getLanguage()` (restituisce un `Optional<String>` contenente il tag di lingua, se presente).

![center|500](img/Pasted%20image%2020260522104759.png)
### Uguaglianza tra Valori

In RDF4J, il concetto di uguaglianza tra i termini è implementato in modo rigoroso. Tutte le classi che concretizzano l'interfaccia `Value` sovrascrivono i metodi standard di Java `Object.equals(Object o)` e `Object.hashCode()` per garantire che il confronto avvenga sul valore logico e non sul riferimento in memoria. Nello specifico:

- Due **IRI** sono considerati uguali se e solo se possiedono il medesimo `stringValue`.
    
- Due **Literal** sono considerati uguali se presentano esattamente la stessa _label_, lo stesso _datatype_ e, quando specificato, lo stesso _language_.
    

### La struttura degli Statement e il Contesto

Un singolo **statement** nel framework rappresenta una tripla RDF ed è composto rigorosamente da tre componenti, definiti da interfacce precise:

1. Un **soggetto** (di tipo `Resource`).
    
2. Un **predicato** (di tipo `IRI`).
    
3. Un **oggetto** (di tipo `Value`).
    

Esiste anche la possibilità di aggiungere un quarto componente opzionale, chiamato **contesto** (di tipo `Resource`). Questo elemento permette di raggruppare e isolare insiemi di statement. L'utilizzo del contesto è particolarmente utile per:

- Tracciare la _provenance_ (provenienza), indicando esplicitamente l'origine o la fonte di determinati statement.
    
- Circoscrivere la valutazione di una query a un sottoinsieme specifico di statement, filtrando per contesti determinati.
    
- Fornire un'alternativa più snella ed efficiente alla reificazione RDF standard.

![center|300](img/Pasted%20image%2020260522104823.png)
### Il Pattern ValueFactory

Poiché tutti gli elementi descritti finora (`IRI`, `BNode`, `Literal`, `Statement`) sono interfacce, il linguaggio Java non ne consente l'istanziazione diretta. Per ovviare a questo e gestire la creazione degli oggetti in modo centralizzato, Eclipse RDF4J utilizza il _design pattern_ della **Factory Astratta**.

L'interfaccia `ValueFactory` definisce l'API necessaria per istanziare i tipi del package Model. Un'implementazione concreta di questa factory può essere recuperata, ad esempio, aprendo una connessione verso un repository. Tramite una `ValueFactory` è possibile generare tutti i termini necessari:

- **Creazione di IRI:** È possibile creare un IRI passando l'indirizzo per esteso (es. `vf.createIRI("http://example.org/Socrates")`) oppure concatenando un _namespace_ e un _local name_ (es. `vf.createIRI(ns + "Socrates")`). Inoltre, per i vocabolari semantici di uso comune (come RDF, RDFS, ecc.), RDF4J offre classi contenenti costanti predefinite (es. `RDF.TYPE`), che evitano di dover istanziare manualmente IRI ricorrenti.
	- ![center|500](img/Pasted%20image%2020260522104859.png)
	- ![center|500](img/Pasted%20image%2020260522104916.png)
- **Creazione di BNode:** Si può generare un nodo anonimo chiamando il metodo privo di argomenti `vf.createBNode()`, oppure fornire un identificatore personalizzato come stringa (es. `vf.createBNode("abc...")`). È fondamentale notare che l'identità di un BNode in RDF4J è basata su questo identificatore di nodo locale, il quale non ha alcuna validità o esistenza in ambito globale.
	- ![center|500](img/Pasted%20image%2020260522104941.png)
- **Creazione di Literal:** La factory permette di generare letterali con tag di lingua (es. `vf.createLiteral("dog", "en")`) o associati a specifici tipi di dato, passando l'IRI del _datatype_ corrispondente (es. usando la costante `XMLSchema.DATETIME`). È supportata anche la conversione a partire da oggetti Java, come quelli legati al tempo (`GregorianCalendar` o `XMLGregorianCalendar`).
	- ![center|500](img/Pasted%20image%2020260522104957.png)
- **Creazione di Statement:** Una volta creati un soggetto, un predicato e un oggetto, questi possono essere assemblati in una singola asserzione richiamando `vf.createStatement(soggetto, predicato, oggetto)`.
	- ![center|500](img/Pasted%20image%2020260522105017.png)

### I Model

Proseguendo l'analisi del framework, il nucleo della gestione delle collezioni di triple è rappresentato dall'interfaccia **Model**.

Un `Model` è, a tutti gli effetti, un insieme di `Statement`. A livello di codice, questa interfaccia estende le strutture dati standard di Java, come `Set<Statement>` e `Serializable`, combinandole con interfacce specifiche del contesto semantico, come `Graph` e `NamespaceAware`.

![center|500](img/Pasted%20image%2020260522120120.png)

Per gestire queste collezioni di statement direttamente in memoria (tipicamente per dataset di dimensioni contenute), il framework mette a disposizione due implementazioni principali:

- **LinkedHashModel:** Un'implementazione che basa il suo funzionamento su una struttura a hash-table.
    
- **TreeModel:** Un'implementazione che utilizza alberi Red-Black, garantendo che i dati vengano mantenuti ordinati secondo l'ordine lessicale dei termini RDF.

La creazione di un modello avviene semplicemente istanziando una di queste classi (es. `Model model = new LinkedHashModel();`).

![center|500](img/Pasted%20image%2020260522120139.png)

![center|500](img/Pasted%20image%2020260522120340.png)
#### Interrogazione e Modifica del Modello: Il Ruolo dei Wildcard

Rispetto a una generica collection di Java (come un `LinkedHashSet`), il `Model` di RDF4J semplifica notevolmente le operazioni di interrogazione. Mentre su un set standard per testare la presenza di una tripla tramite il metodo `contains()` è necessario istanziare e passare un oggetto `Statement` completo, il `Model` permette di passare direttamente i singoli costituenti della tripla (soggetto, predicato, oggetto).

In queste operazioni di verifica (`contains`) e di rimozione (`remove`), il valore **`null`** assume un ruolo cruciale funzionando da _wildcard_ (jolly).

Basandosi sulla documentazione Javadoc ufficiale, ecco come si comportano queste operazioni utilizzando il wildcard:

- `model.contains(s1, null, null)`: restituisce `true` se esiste _almeno uno_ statement che ha `s1` come soggetto, ignorando quale sia il predicato o l'oggetto (logica identica per il `remove`, che eliminerà tutti gli statement con quel soggetto).
    
- `model.contains(null, null, null, c1)`: agisce specificamente sul quarto parametro, il contesto, verificando la presenza (o rimuovendo) ogni statement appartenente al contesto `c1`.
    
- `model.contains(null, null, null, (Resource)null)`: utilizzando un cast esplicito a risorsa nulla per il contesto, si intercettano tutti quegli statement che _non_ hanno alcun contesto associato.
    
- `model.contains(null, null, null, c1, c2, c3)`: è possibile anche passare una lista di contesti, operando quindi su qualsiasi statement che appartenga al contesto `c1`, oppure a `c2`, oppure a `c3`.

![center|500](img/Pasted%20image%2020260522120405.png)

Vediamo anche per quanto riguarda i `remove`

![center|500](img/Pasted%20image%2020260522120455.png)
#### Viste e Filtri sui Dati

Un'altra funzionalità potente del `Model` è la capacità di generare delle **viste** dinamiche sui dati.

Utilizzando il metodo `filter(subject, predicate, object, contexts...)`, è possibile ottenere un nuovo `Model` ridotto (filtrato) che contiene esclusivamente gli statement corrispondenti ai parametri indicati. La caratteristica fondamentale di questa vista è la sua natura bidirezionale: qualsiasi modifica apportata al modello di partenza si rifletterà automaticamente sulla vista filtrata, e viceversa.

![center|500](img/Pasted%20image%2020260522120515.png)

Inoltre, se si ha bisogno di estrarre solo parti specifiche delle triple, è possibile chiedere al modello una vista diretta sui singoli set di componenti tramite i metodi:

- `model.subjects()` per ottenere un `Set<Resource>`.
    
- `model.predicates()` per ottenere un `Set<IRI>`.
    
- `model.objects()` per ottenere un `Set<Value>`.

![center|500](img/Pasted%20image%2020260522120537.png)
#### La Classe di Utilità Models

Per semplificare ulteriormente le operazioni più comuni e avanzate, RDF4J fornisce la classe di utilità **`Models`**.

Questa classe permette, ad esempio, di estrarre agilmente componenti di un tipo specifico dal modello. Richiamando `Models.objectLiterals(model)`, il framework restituirà tutti e soli gli oggetti presenti nel modello che sono di tipo letterale, filtrando via IRI o BNode.

Infine, la classe `Models` supporta un **approccio basato sulle proprietà**, che risulta spesso più intuitivo rispetto alla manipolazione diretta degli statement:

- **Lettura:** Tramite `Models.getPropertyString(model, subject, property)` si ottiene direttamente (sotto forma di `Optional<String>`) il valore testuale associato a un soggetto tramite una specifica proprietà. Questa è un'alternativa più compatta rispetto al dover filtrare prima il modello e poi estrarre la stringa dell'oggetto.
    
- **Scrittura/Aggiornamento:** Il metodo `Models.setProperty(model, subject, property, value)` permette di assegnare un nuovo valore a una determinata proprietà. Eseguendo questa operazione, il framework si occupa automaticamente di cancellare tutti i valori precedenti associati a quella proprietà per quel soggetto (limitatamente ai contesti indicati, o all'intero modello se non si specifica alcun contesto).

![center|500](img/Pasted%20image%2020260522120558.png)

## RIO (RDF Input/Output)

Il modulo **RIO** (acronimo di RDF Input/Output) di Eclipse RDF4J è il componente dedicato alla gestione dei flussi di ingresso e uscita dei dati RDF. Concentrandoci specificamente sulla fase di lettura, il protagonista assoluto è l'**RDFParser**, il cui compito è prendere in input un documento RDF scritto in una sintassi concreta (come Turtle, RDF/XML, ecc.) e tradurlo in oggetti Java conformi alle interfacce definite nel package _Model_ (viste in precedenza).
### RIO Parser
#### Creazione e Istanziazione del Parser

Per ottenere un'istanza di un parser specifico per il formato che si desidera leggere, il framework offre due strade.

La prima è un approccio più esplicito e rigoroso che passa attraverso l'uso di un registro:

1. Si interroga l'`RDFParserRegistry` per ottenere l'istanza del registro contenente tutti i parser attualmente disponibili sul _classpath_.
    
2. Si richiede la _factory_ del parser per un formato specifico (ad esempio, `RDFFormat.TURTLE`).
    
3. Poiché il parser potrebbe non essere disponibile, il metodo restituisce un `Optional`. Se il formato non è supportato, viene lanciata un'eccezione dedicata (`Rio.unsupportedFormat`).
    
4. Se la factory è presente, si invoca il metodo `getParser()` per istanziare finalmente il parser.
    

La seconda strada è una comoda **scorciatoia** offerta dalla classe di utilità `Rio`. Tramite il metodo `Rio.createParser(rdfFormat [, valueFactory])`, è possibile istanziare direttamente il parser passandogli il formato desiderato e, opzionalmente, la `ValueFactory` da utilizzare.

![center|500](img/Pasted%20image%2020260522121632.png)
#### Configurazione del Parser

Una volta ottenuto l'oggetto `RDFParser`, è possibile configurarne il comportamento tramite una serie di impostazioni opzionali prima di avviare la lettura vera e propria:

- **`setValueFactory(...)`**: Definisce quale factory utilizzare per creare le istanze dei termini RDF (IRI, Literal, BNode) durante la lettura.
    
- **`setParseErrorListener(...)`**: Associa un listener che verrà notificato ogni volta che il parser incontra un errore di sintassi.
    
- **`setParseLocationListener(...)`**: Associa un listener per monitorare il progresso della lettura.
    
- **`setRDFHandler(...)`**: Questa è l'impostazione concettualmente più importante. Definisce il gestore (l'`RDFHandler`) a cui il parser "consegnerà" gli statement man mano che li estrae dal documento.
    

Per configurazioni più avanzate e specifiche dei singoli parser, si utilizza la classe `ParserConfig`. È possibile istanziare un oggetto `ParserConfig`, settarvi dei parametri rappresentati da oggetti `RioSetting<T>` (ognuno con il proprio valore), e infine passare l'intera configurazione al parser tramite `setParserConfig(config)`. Per conoscere quali impostazioni sono supportate da un determinato parser, si può invocare il suo metodo `getSupportedSettings()`.

![center|500](img/Pasted%20image%2020260522121700.png)

#### L'Architettura di Parsing: L'Approccio "Push"

Il processo di lettura viene innescato richiamando il metodo `parse(inputStreamOrReader, baseURI)`.

L'aspetto fondamentale da comprendere è che l'RDFParser opera utilizzando un **approccio _push_**, del tutto analogo a quello utilizzato dalle API SAX per il parsing dei documenti XML. Il parser legge il file in modo sequenziale e, non appena riconosce un elemento valido, lo "spinge" (push) verso l'`RDFHandler` precedentemente configurato, senza caricare l'intero documento in memoria tutto in una volta.

La sequenza delle operazioni segue un ciclo di vita preciso:

1. Inizia il parsing invocando `startRDF()` sull'handler.
    
2. Avvia un ciclo in cui analizza il testo. Man mano che incontra elementi, invoca metodi specifici sull'handler:
    
    - `handleNamespace(prefix, name)` quando incontra la dichiarazione di un prefisso (es. `@prefix ex: <http://example.org/>`).
        
    - `handleStatement(st)` quando estrae una tripla completa (soggetto, predicato, oggetto).
        
    - `handleComment(comment)` se incontra dei commenti nel file.
        
3. Al termine del documento, chiude il processo invocando `endRDF()`.

![center|500](img/Pasted%20image%2020260522121726.png)

![center|500](img/Pasted%20image%2020260522121747.png)
#### Raccogliere i Dati: StatementCollector e Scorciatoie

Poiché l'interfaccia base `RDFHandler` si limita a ricevere i dati in streaming, se si desidera memorizzarli e conservarli (ad esempio in un `Model` o in una semplice collection), RDF4J fornisce un'implementazione concreta chiamata **`StatementCollector`**. Questo componente funge da handler e si occupa di accumulare automaticamente tutti gli statement e i namespace ricevuti durante il parsing all'interno di una collezione in memoria.

Infine, per i casi d'uso più comuni in cui l'obiettivo è semplicemente caricare un intero file RDF all'interno di un modello in memoria, il framework fornisce un'ulteriore, potentissima **scorciatoia**. Invece di istanziare il parser, configurare l'handler e avviare il parsing manualmente, è possibile utilizzare un unico metodo statico:

```Java
Model model = Rio.parse(inputStreamOrReader, baseURI, rdfFormat, [settings, valueFactory, errorListener], contexts...)
```

Questa singola istruzione esegue l'intero ciclo: crea il parser adatto, legge i dati dallo stream e restituisce direttamente un oggetto `Model` pronto per essere interrogato.

### RIO Writer

Passando alla fase di serializzazione e output, il modulo RIO mette a disposizione l'**RDFWriter**. Il suo compito è speculare a quello del parser: prende in input gli _statement_ RDF, rappresentati come oggetti Java conformi alle interfacce del package Model, e li scrive su un flusso di uscita codificandoli in un documento testuale secondo una specifica sintassi concreta (come, ad esempio, il formato Turtle).

#### Creazione e Istanziazione del Writer

Anche per la creazione di un writer il framework offre due approcci distinti, mantenendo una simmetria architetturale con la fase di lettura.

Il primo metodo è esplicito e basato sul registro di sistema:

1. Si ottiene l'istanza del registro interrogando `RDFWriterRegistry.getInstance()`, il quale contiene tutti i writer individuati nel _classpath_ del progetto.
    
2. Si richiede la _factory_ specifica per il formato desiderato (ad esempio, tramite `.get(RDFFormat.TURTLE)`).
    
3. Essendo il risultato incapsulato in un `Optional<RDFWriterFactory>`, in caso di formato non supportato si gestisce l'assenza lanciando un'eccezione dedicata tramite `.orElseThrow(Rio.unsupportedFormat(...))`.
    
4. Infine, dalla factory si ottiene l'oggetto writer invocando `.getWriter(outputStreamOrWriter [, baseURI])`, fornendo il flusso su cui scrivere e, opzionalmente, l'URI di base.
    

Il secondo metodo, più immediato, consiste nell'usare una **scorciatoia** fornita dalla classe di utilità `Rio`:

Tramite l'istruzione `Rio.createWriter(rdfFormat, outputStreamOrWriter [, base URI])` si delega al framework l'intero processo di ricerca nel registro e istanziazione, ottenendo direttamente il writer pronto all'uso.

![center|500](img/Pasted%20image%2020260522122614.png)
#### Configurazione del Writer

Prima di avviare la scrittura, è possibile personalizzare il comportamento del serializzatore. Questo avviene attraverso la classe `WriterConfig`.

Il processo richiede di istanziare un oggetto `WriterConfig` e di popolarlo aggiungendo i vari parametri tramite il metodo `set(setting, value)`. Ogni parametro è rappresentato da un oggetto di tipo `RioSetting<T>`. Per garantire la correttezza della configurazione, è possibile interrogare il writer stesso invocando `getSupportedSettings()`, che restituisce l'elenco esatto delle impostazioni riconosciute da quello specifico serializzatore.

Una volta completata la configurazione, la si applica al writer richiamando `setWriterConfig(config)`.

#### Esecuzione della Scrittura

Per innescare il processo di serializzazione di una collezione di triple (un oggetto _Iterable_ in Java), si utilizza nuovamente la classe di utilità `Rio`:

- **Metodo standard:** Se si ha a disposizione il writer già configurato, basta richiamare `Rio.write(iterable, w);`.
    
- **Scorciatoia diretta (Shorthand):** È possibile compattare l'intero ciclo di vita (creazione, configurazione e scrittura) in una singola riga di codice invocando: `Rio.write(iterable, outputStreamOrWriter [, base URI], format, [writerConfig]);`

![center|500](img/Pasted%20image%2020260522122627.png)
#### Il Vantaggio Architetturale: Efficienza in Memoria

C'è un principio architetturale di vitale importanza che accomuna l'intero modulo RIO (sia per la lettura che per la scrittura): **non c'è mai bisogno di avere tutti gli statement caricati simultaneamente in memoria.**

Il framework è progettato per operare su flussi continui in modo estremamente efficiente:

- Durante il parsing, i _reader_ inviano all'handler i dati elaborando **uno statement alla volta**.
    
- In maniera del tutto speculare, un _writer_ è progettato per ricevere e serializzare sul flusso di output **uno statement alla volta**.


Questa natura incrementale garantisce che il consumo di memoria (RAM) rimanga costante e ridotto, permettendo al sistema di elaborare e trasferire moli di dati potenzialmente infinite senza rischiare blocchi o crash dell'applicazione.
## Repository

Procedendo nell'analisi del framework, abbandoniamo le semplici collezioni in memoria e incontriamo il vero cuore della gestione dei dati persistenti e strutturati: il **Repository**.

Un `Repository` rappresenta il punto di accesso ufficiale a un database RDF (il _triplestore_). Rispetto ai `Model` visti in precedenza, i repository sono strumenti molto più avanzati e progettati per scenari reali di produzione. Le loro caratteristiche distintive includono il supporto per:

- **Connessioni concorrenti** da parte di molteplici utenti simultaneamente.
    
- **Transazioni**, garantendo la possibilità di effettuare _commit_ o _rollback_ di gruppi di operazioni e gestendo diversi livelli di isolamento tra transazioni concorrenti.
    
- **Linguaggi di interrogazione e modifica**, offrendo supporto nativo e strutturato per l'esecuzione di query, tipicamente utilizzando SPARQL.
    

Un aspetto architetturale fondamentale è che l'utente o l'applicazione non esegue mai le operazioni di lettura o scrittura direttamente sull'oggetto `Repository`. Quest'ultimo funge da "fabbrica": per interagire con i dati è obbligatorio ottenere da esso una **`RepositoryConnection`**, attraverso la quale transitano tutte le operazioni.

![center|500](img/Pasted%20image%2020260523145350.png)
### Tipologie di Repository

Il framework fornisce diverse implementazioni dell'interfaccia `Repository` (e delle relative `RepositoryConnection`), ognuna adatta a un contesto specifico:

- **SPARQLRepository:** È pensato per accedere a un _endpoint SPARQL_ generico. Poiché si affida al protocollo standard SPARQL per le comunicazioni, è soggetto alle limitazioni del protocollo stesso (ad esempio, limitazioni nella gestione di transazioni complesse o nell'uso di BNode come parametri di input). Per questo motivo, il suo utilizzo è consigliato principalmente per singole operazioni SPARQL isolate. Prevede anche un costruttore specifico (un _overload_) per indicare un endpoint separato dedicato esclusivamente alle operazioni di modifica.
	- ![center|500](img/Pasted%20image%2020260523145415.png)
- **HTTPRepository:** Viene utilizzato per accedere a un repository remoto che espone i propri servizi specificamente attraverso l'API REST di RDF4J. Supporta la configurazione di credenziali (username e password) nel caso in cui l'accesso al server richieda autenticazione.
	- ![center|500](img/Pasted%20image%2020260523145440.png)
_Nota pratica sul ciclo di vita:_ Per entrambi questi repository, l'invocazione esplicita del metodo `init()` per l'inizializzazione è diventata opzionale nelle versioni recenti. È invece sempre obbligatorio e cruciale rilasciare le risorse invocando `shutDown()`, pratica che andrebbe sempre inserita all'interno di un blocco `finally` per assicurarne l'esecuzione.

### Il cuore locale: SailRepository e l'interfaccia Sail

La terza, e concettualmente più importante, implementazione è il **`SailRepository`**. Questo repository è un "contenitore" che avvolge un oggetto **`Sail`** (acronimo di _Storage and Inference Layer_).

L'interfaccia `Sail` rappresenta il vero e proprio motore del database: è il livello che si occupa fisicamente dello storage, dell'esecuzione delle query e della logica di inferenza. Questa netta separazione tramite interfacce serve a **disaccoppiare** le implementazioni di basso livello del triplestore da tutti gli altri moduli di alto livello del framework (come i parser, le API per l'utente o i motori di analisi). Anche in questo caso, la divisione dei compiti è replicata specularmente: al `Sail` corrisponde una `SailConnection` per le operazioni dirette sui dati.

#### Esempio: MemoryStore e la gestione della persistenza

Un'implementazione classica di `Sail` è il `MemoryStore`. Se istanziato di base, opera esclusivamente in memoria RAM ed è perciò "non persistente" (i dati svaniscono alla chiusura).

![center|300](img/Pasted%20image%2020260523145512.png)

Tuttavia, il framework permette di renderlo persistente configurando una directory per i dati e invocando `setPersist(true)`. Il contenuto verrà così salvato in un file denominato `memorystore.data`.

Le dinamiche di scrittura su questo file sono controllate minuziosamente dal parametro **`syncDelay`**:

- **`syncDelay = 0`:** La scrittura su file avviene in maniera _sincrona_ a ogni commit. Questo massimizza la sicurezza (durabilità) dei dati, ma rallenta la transazione, che deve attendere i tempi fisici del disco. Inoltre, molte transazioni ravvicinate si traducono in continue e frammentate scritture fisiche.
    
- **`syncDelay > 0`:** La scrittura diventa un task _asincrono_ eseguito in background dopo il lasso di tempo indicato. La transazione in corso non deve più attendere i tempi del disco, migliorando drasticamente le prestazioni a fronte di una brevissima finestra di potenziale perdita di dati in caso di crash improvviso.
    
- **`syncDelay < 0`:** I dati vengono scaricati sul file esclusivamente alla fine, quando il `Sail` viene spento.

![center|300](img/Pasted%20image%2020260523145541.png)
#### Architettura Avanzata: Stackable e Notifying Sail

La flessibilità dell'architettura Sail raggiunge il suo apice con il concetto di **Stackable Sail** (Sail impilabile).

![center|500](img/Pasted%20image%2020260523145644.png)

Uno Stackable Sail non conserva i dati in prima persona, ma opera come un "involucro" (wrapper) posizionato al di sopra di un altro Sail sottostante (chiamato _base_ o _delegate_).

Questa architettura a strati permette di intercettare e modificare le operazioni in volo. Una connessione derivata da uno Stackable Sail restituisce un wrapper intorno alla connessione originaria. Questo è estremamente utile per iniettare logiche speciali al momento del commit o del rollback, oppure per intercettare e filtrare ogni singola richiesta di lettura, scrittura o query prima che raggiunga il database fisico.

Per operare efficacemente, questi strati intermedi si avvalgono di un sistema ad eventi:

- Uno Stackable Sail può sottoscriversi per ricevere notifiche generate da un Sail di base configurato come **`NotifyingSail`**. Tramite appositi _listener_ (come il `SailChangedListener`), viene informato ogniqualvolta uno statement viene aggiunto o rimosso.
    
- Parallelamente, il wrapper della connessione può sottoscriversi agli eventi della `NotifyingSailConnection` sottostante (tramite un `SailConnectionListener`), venendo notificato con precisione su quali statement sono stati _effettivamente_ modificati e confermati durante il ciclo di vita di una singola transazione.

### Inferenza: ForwardChaining e SchemaCaching

Il framework RDF4J permette di arricchire il repository base con capacità di ragionamento (reasoning) sfruttando l'architettura _stackable sail_. Vengono presentati due inferencer, sebbene entrambi siano contrassegnati come **deprecati**:

- **`ForwardChainingRDFSInferencer`:** Questo stackable sail implementa il reasoning RDFS utilizzando il _forward chaining_. Il suo funzionamento si basa su due fasi:
    
    1. Aggiunge al repository le triple assiomatiche base (ad esempio, definisce che la proprietà `rdfs:subClassOf` ha come range la classe `rdfs:Class`).
        
    2. Al momento del _commit_ di una transazione, il reasoner calcola tutte le nuove triple implicate logicamente. Lo fa applicando in modo iterativo le regole che specificano la semantica RDFS.
	    - **Gestione della Monotonia:** Poiché la semantica di RDFS (e OWL) è monotona, l'aggiunta di una nuova tripla non può mai invalidare le inferenze già fatte; il reasoner deve solo tentare di applicare nuovamente le regole. Al contrario, la _cancellazione_ di una tripla può invalidare le conclusioni precedenti. Se ciò accade, il reasoner è costretto a cancellare tutte le triple inferite e riavviare l'intero processo di reasoning da zero
        
- **`SchemaCachingRDFSInferencer`:** Un altro stackable sail deprecato per il reasoning RDFS. A differenza del precedente, non usa un approccio _rule-based_ (basato su regole applicate iterativamente), ma colleziona lo schema in una _cache_ interna, utilizzata per produrre le inferenze in modo più veloce.

![center|500](img/Pasted%20image%2020260523150018.png)

![center|500](img/Pasted%20image%2020260523150042.png)
### Note Architetturali sulle Configurazioni

Un aspetto importante di RDF4J è che **non distingue tra la creazione di un nuovo repository e l'apertura di uno creato in precedenza**.

A livello interno, quando viene inizializzato un repository persistente, questo ispeziona la propria directory dei dati. Se trova dei file, carica i dati salvati in precedenza; altrimenti parte da zero. A causa di questo comportamento, è fondamentale che l'oggetto `Repository` venga **sempre configurato nello stesso identico modo** ad ogni avvio. Cambiare la configurazione (ad esempio, istanziando un _native store_ su dati creati da un _memory store_) può corrompere lo stato, a meno che non si tratti di un cambiamento esplicitamente sicuro (come l'aggiunta di indici non esistenti).

### Gestione della RepositoryConnection

Per interagire con i dati (lettura, scrittura, query), l'utente deve ottenere una connessione invocando `rep.getConnection()`.

Poiché la connessione impegna risorse di sistema (memoria, file handle, lock del database), **deve essere sempre chiusa** al termine delle operazioni. Ci sono due pattern principali in Java per garantire questo:

1. **Blocco try-finally:** Si apre la connessione, si eseguono le operazioni nel blocco `try`, e si garantisce la chiusura invocando `conn.close()` nel blocco `finally`.
    
2. **Try-with-resources (Consigliato in Java moderni):** Si dichiara l'apertura della connessione direttamente all'interno delle parentesi del blocco `try`. Java chiuderà automaticamente la risorsa al termine del blocco, rendendo il codice più pulito e sicuro.

![center|500](img/Pasted%20image%2020260523150131.png)
#### Inserimento Dati: Il metodo `add`

La classe `RepositoryConnection` offre il metodo `add()` per inserire nuove triple nel database. Il framework mette a disposizione numerosi _overload_ (varianti) di questo metodo, rendendolo estremamente flessibile. Può accettare in input:

- Singoli oggetti `Statement`.
    
- Le singole componenti esplose di uno statement (soggetto, predicato, oggetto).
    
- Collezioni di statement (`Iterable` o `Iteration`).
    
- Sorgenti esterne come `File`, `InputStream` o `Reader` (in questi casi il metodo legge il file, esegue il parsing e inserisce i dati direttamente).
    

È cruciale notare che se si passa il parametro opzionale **context**, si specifica esplicitamente in quali contesti (o grafi nominati) le triple devono essere inserite, _sovrascrivendo_ eventuali contesti già associati agli statement in input.

![center|500](img/Pasted%20image%2020260523150150.png)
#### Estrazione Dati: Il metodo `export`

Speculare all'inserimento, il metodo `export()` permette di estrarre i dati dal repository e serializzarli.

Per utilizzarlo, occorre configurare un `RDFHandler` (un writer, come visto in precedenza nel modulo RIO) e passarlo al metodo `export`. È possibile filtrare l'estrazione passando i contesti desiderati come parametri successivi. Ad esempio, `conn.export(nquadOutputter, g1)` esporterà solo i dati appartenenti al contesto identificato dall'IRI `g1`. Se non si specifica alcun contesto, verrà esportato l'intero contenuto del repository.

![center|500](img/Pasted%20image%2020260523150243.png)

Un dettaglio molto importante è che `RepositoryConnection.export()` esporta **unicamente gli statement espliciti**. Non estrarrà mai le triple generate logicamente dagli inferencer (se presenti nello stack).

![center|500](img/Pasted%20image%2020260523150305.png)

Infine, per rendere l'output testuale più leggibile, è possibile registrare dei prefissi (namespace) direttamente sulla connessione usando `conn.setNamespace(prefix, URI)`. Durante l'esportazione, il writer utilizzerà questi prefissi al posto degli URI estesi.

![center|500](img/Pasted%20image%2020260523150323.png)

Analizziamo come la `RepositoryConnection` permette di interrogare e manipolare i dati, partendo dai metodi di base fino ad arrivare all'esecuzione di query SPARQL complesse.

#### Recupero Dati: Il metodo `getStatements`

Per recuperare statement specifici dal repository senza utilizzare SPARQL, si utilizza il metodo `conn.getStatements()`. Il suo funzionamento è del tutto analogo a quanto visto per la ricerca all'interno dei `Model`, basandosi sull'uso dei wildcard (`null`) per filtrare soggetto, predicato, oggetto o contesto.

L'invocazione di questo metodo restituisce un oggetto **`RepositoryResult<Statement>`**. Questo oggetto è essenzialmente un iteratore che permette di scorrere i risultati uno alla volta (usando i classici metodi `hasNext()` e `next()`).

È fondamentale ricordare che, trattandosi di una risorsa aperta verso il database, l'iterazione deve avvenire all'interno di un blocco _try-with-resources_ per garantirne la chiusura automatica al termine della lettura.

- **Inferenza di default:** Un aspetto cruciale di `getStatements()` è che, **per impostazione predefinita, include nei risultati anche gli statement inferiti** (se è configurato un reasoner). Se si desidera ottenere _esclusivamente_ gli statement espliciti, è necessario utilizzare un _overload_ del metodo che accetta un parametro booleano finale, passandogli il valore `false` (cioè `includeInferred a false`).

![center|500](img/Pasted%20image%2020260523150943.png)

In alternativa al classico ciclo `while`, la classe di utilità `QueryResults` offre metodi più moderni basati sugli stream di Java. Ad esempio, si può convertire il risultato in uno stream e stamparlo direttamente con un'unica riga: `QueryResults.stream(result).forEach(System.out::println);`.

![center|500](img/Pasted%20image%2020260523150953.png)
#### Rimozione Dati: Il metodo `remove`

In perfetta simmetria con il metodo `add()`, la connessione offre il metodo `remove()` per eliminare triple dal database.

Anche qui troviamo diversi _overload_ che permettono di passare input differenti:

- Una collezione (`Iterable` o `Iteration`) di statement.
    
- Un singolo oggetto `Statement`.
    
- Le componenti separate (soggetto, predicato, oggetto), utilizzando anche in questo caso il `null` come wildcard per indicare "cancella tutti gli statement che corrispondono a questo pattern".
    

Come per l'inserimento, l'uso del parametro **context** è determinante:

- Se specificato, il metodo rimuoverà le triple indicate **solo dai grafi nominati specificati**, sovrascrivendo eventuali contesti presenti nell'input.
    
- Se non viene specificato alcun contesto (né come argomento del metodo né all'interno degli statement passati in input), l'operazione di cancellazione avverrà sull'intero repository, indistintamente.
    
#### Esecuzione di Query SPARQL

RDF4J supporta pienamente l'esecuzione di interrogazioni strutturate in linguaggio SPARQL. Il framework distingue i tipi di query in base al formato del risultato atteso.

##### 1. Tuple Query (SELECT)

Le Tuple Query corrispondono alle query SPARQL di tipo `SELECT`. Il loro scopo è restituire un set di "tuple", ovvero una tabella in cui ogni riga è un risultato e ogni colonna è una variabile richiesta.

1. Si prepara la query passando la stringa SPARQL al metodo `conn.prepareTupleQuery()`.
    
2. Si possono legare dinamicamente dei valori alle variabili della query prima dell'esecuzione usando `query.setBinding()`.
    
3. Si esegue la query chiamando `query.evaluate()`. Il risultato è un **`TupleQueryResult`**.
    
4. Iterando sul risultato (sempre in un blocco try-with-resources), si estraggono i singoli `BindingSet` (le righe dei risultati). Da ogni `BindingSet` si può poi recuperare il `Value` associato a una specifica variabile nominata nella `SELECT` (es. `bindingSet.getValue("acquaintance")`).

![center|400](img/Pasted%20image%2020260523151016.png)
##### 2. Graph Query (CONSTRUCT / DESCRIBE)

Le Graph Query corrispondono alle interrogazioni SPARQL di tipo `CONSTRUCT` o `DESCRIBE`. A differenza delle tuple, queste query non restituiscono una tabella di variabili, ma generano un **nuovo grafo RDF** (quindi un insieme di statement completi).

1. Si prepara la query con `conn.prepareGraphQuery()`.
    
2. Si esegue sempre con `query.evaluate()`. In questo caso, il risultato è un **`GraphQueryResult`**.
    
3. L'iterazione su questo risultato non restituisce dei `BindingSet`, ma direttamente oggetti **`Statement`** completi (soggetto, predicato, oggetto), pronti per essere manipolati o stampati.
    
4. _Scorciatoia:_ Se si desidera caricare l'intero grafo risultante direttamente in memoria, si può usare la comodissima utilità `QueryResults.asModel(query.evaluate())`, che restituisce un oggetto `Model`.

![center|500](img/Pasted%20image%2020260523151121.png)
##### 3. Update (INSERT / DELETE)

Le operazioni di aggiornamento SPARQL, che modificano lo stato del database, sono gestite separatamente.

1. Si prepara l'operazione passando la stringa SPARQL di aggiornamento (es. combinazioni di `DELETE` e `INSERT` basate su un blocco `WHERE`) al metodo `conn.prepareUpdate()`.
    
2. Poiché questa operazione non restituisce dati, non si utilizza il metodo `evaluate`, ma si invoca semplicemente **`update.execute()`**.

![center|400](img/Pasted%20image%2020260523151159.png)

_Nota sull'inferenza nelle Query:_ Come per `getStatements`, tutte le query e le operazioni di update includono di default i dati inferiti. È sempre possibile disabilitare questo comportamento invocando `setIncludeInferred(false)` sull'oggetto query/update prima di eseguirlo.

### Il Modello a Transazioni: Dall'Autocommit al Controllo Esplicito

Per impostazione predefinita, RDF4J opera in modalità **autocommit**. Questo significa che ogni singola operazione eseguita su una `RepositoryConnection` (un inserimento, una cancellazione, un update) viene considerata autonoma e confermata in modo permanente nel repository non appena completata.

Tuttavia, in scenari reali e complessi, è spesso necessario raggruppare diverse operazioni affinché vengano trattate come un'unica unità logica (es. trasferire fondi implica sottrarre da un conto _e_ aggiungere a un altro; entrambe devono riuscire, o nessuna delle due). Per questo, il framework permette di **gestire esplicitamente le transazioni**.

Il flusso classico per gestire una transazione prevede tre fasi principali:

1. **Apertura:** Si invoca `conn.begin()` per segnalare l'inizio della transazione e sospendere l'autocommit.
    
2. **Esecuzione e Conferma:** All'interno di un blocco `try`, si eseguono le varie operazioni (le "cose utili"). Se tutte vanno a buon fine, si invoca `conn.commit()` per rendere le modifiche permanenti e atomiche.
    
3. **Gestione degli Errori:** Si predispone un blocco `catch` per intercettare eventuali eccezioni (tipicamente `RepositoryException`). Se si verifica un errore, si invoca **`conn.rollback()`** per annullare tutte le operazioni effettuate dall'inizio della transazione, riportando il database allo stato precedente.
    

_Nota di sicurezza:_ Indipendentemente da come si conclude la transazione (commit o rollback), la connessione va sempre chiusa. Se si utilizza il costrutto `try-with-resources`, e si verifica un'eccezione non gestita _prima_ del commit, il metodo `close()` (chiamato automaticamente alla fine del blocco) forzerà un rollback di sicurezza prima di chiudere la connessione.

![center|500](img/Pasted%20image%2020260523151545.png)
### I Livelli di Isolamento (Isolation Levels)

Quando più utenti (o thread) operano contemporaneamente sullo stesso database, le loro transazioni si incrociano. I **livelli di isolamento** definiscono quanto strettamente una transazione debba essere protetta (isolata) dalle modifiche apportate dalle altre transazioni concorrenti in corso.

RDF4J permette di specificare il livello di isolamento passando un parametro specifico al metodo `begin()`. Ecco i livelli supportati, in ordine crescente di rigore:

1. **NONE:** È il livello di isolamento più basso. Non c'è alcuna garanzia di isolamento tra le transazioni. Una transazione vede le proprie modifiche, ma potrebbe non essere in grado di effettuare un rollback. Questo livello estremo è usato quasi esclusivamente per le operazioni massive di caricamento dati (_bulk data upload_) dove la velocità è l'unica priorità e non ci sono altri utenti a fare da interferenza.
    
2. **READ_UNCOMMITTED:** Le transazioni possono essere annullate (rollback), ma l'isolamento non è garantito. Il problema principale qui sono i _dirty reads_ (letture sporche): una transazione può leggere dati che un'altra transazione concorrente ha modificato ma non ancora confermato (se l'altra fa rollback, si è letto un dato "fantasma").
    
3. **READ_COMMITTED:** Risolve il problema delle letture sporche: una transazione può vedere solo i dati che le altre transazioni hanno già confermato (_committed_). Tuttavia, se una transazione legge lo stesso dato due volte, e nel mezzo un'altra transazione lo modifica e lo conferma, la seconda lettura darà un risultato diverso (problema della _non-repeatable read_). È tipicamente usato per operazioni di lunga durata.
    
4. **SNAPSHOT_READ:** Oltre a garantire che si leggano solo dati confermati, garantisce che una query osservi uno "snapshot" coerente (una fotografia) del database al momento in cui la query inizia. Se altre transazioni modificano i dati mentre la query è in esecuzione, il risultato della query non ne sarà influenzato.
    
5. **SNAPSHOT:** Più rigoroso del precedente, fa sì che l'intera transazione operi su uno snapshot fissato. La transazione vedrà o tutti gli effetti completi delle altre transazioni concluse, o nessuno. È fondamentale negli scenari in cui un'operazione di scrittura dipende direttamente dal risultato di un'operazione di lettura eseguita precedentemente nella stessa transazione.
    
6. **SERIALIZABLE:** È il livello più alto e restrittivo. Oltre a garantire lo snapshot, assicura un isolamento totale, come se tutte le transazioni venissero eseguite rigorosamente in fila (serialmente), una dopo l'altra, eliminando alla radice qualsiasi anomalia di concorrenza.
### Supporto nei Triplestore Nativi

Le due implementazioni principali di storage fornite dal framework, il **MemoryStore** e il **NativeStore**, supportano pienamente tutti i livelli di isolamento descritti (da `NONE` a `SERIALIZABLE`).

Il livello di isolamento **predefinito**, se non se ne specifica un altro chiamando `begin()`, è lo **`SNAPSHOT_READ`**.

A livello di meccanica interna, per gestire questa concorrenza senza bloccare continuamente il database, entrambi questi triplestore utilizzano la tecnica del **locking ottimistico**.

L'approccio ottimistico assume, come dice il nome, che i conflitti tra transazioni concorrenti siano rari. Pertanto, permette a più transazioni di eseguire contemporaneamente le loro scritture. Solo al momento di confermare (`commit`), il sistema verifica se le modifiche si scontrano (ad esempio, due transazioni hanno modificato esattamente lo stesso dato). Se rileva un conflitto reale e insormontabile, fa fallire (rollback) una delle transazioni per preservare l'integrità del database.
## RDF4J Server & Workbench

Spostandoci dall'uso strettamente programmatico e locale in Java, il framework mette a disposizione l'**RDF4J Server**. Si tratta di una vera e propria applicazione web progettata per esporre uno o più `Repository`, rendendoli accessibili dall'esterno attraverso un'**API REST** dedicata.

Questa API non è costruita da zero, ma si basa sull'estensione e la combinazione di standard preesistenti. Nello specifico, integra:

- Il **SPARQL 1.1 Protocol**, utilizzato per inviare le query e le operazioni di update ai processori sottostanti.
    
- Il **SPARQL 1.1 Graph Store HTTP Protocol**, che è lo standard dedicato alla gestione diretta dei _named graph_ (permettendo operazioni mirate come l'aggiunta, la rimozione o lo scaricamento di interi grafi).
    

La principale e più importante estensione apportata dall'API di RDF4J rispetto a questi protocolli standard riguarda il supporto per la **gestione delle transazioni** attraverso chiamate HTTP. Dal punto di vista sistemistico, il server viene fornito sotto forma di archivio WAR, pronto per essere distribuito all'interno di un _servlet container_ standard, come ad esempio Apache Tomcat.

Per interagire graficamente e in modo agevole con i repository esposti dal server, l'ecosistema fornisce una seconda applicazione web chiamata **RDF4J Workbench**. Anch'essa distribuita come file WAR da far girare su un contenitore come Tomcat, funge da interfaccia utente visiva per interrogare, esplorare e amministrare i repository ospitati dall'RDF4J Server.

### L'alternativa integrata: GraphDB Workbench

Un'alternativa molto diffusa è il **Workbench di GraphDB**. Sebbene lo scopo di base sia analogo a quello degli strumenti nativi di RDF4J, l'architettura di GraphDB è molto più integrata e "pronta all'uso":

- Può essere avviato autonomamente come programma a sé stante, senza avere alcun bisogno di configurare un _servlet container_ esterno.
    
- Integra all'interno dello stesso pacchetto sia la _user interface_ (il workbench vero e proprio) sia la componente _server_. Il server espone internamente i repository (zero o più) tramite un'API REST, e questa stessa API viene consumata direttamente dal workbench per mostrare i dati e le interfacce di amministrazione all'utente.

**Connessione programmatica a GraphDB**

Quando si sviluppa un'applicazione Java e si desidera utilizzare un database ospitato su GraphDB (istanzio quindi un `HTTPRepository` nel codice), è necessario conoscere l'indirizzo esatto a cui puntare.

L'interfaccia del Workbench di GraphDB rende questa operazione molto semplice. Nella dashboard principale, all'interno del riquadro del repository attualmente attivo (dove vengono mostrate le statistiche generali, come il numero totale di statement, divisi tra espliciti e inferiti, e l'expansion ratio), è presente una serie di piccole icone d'azione.

Cliccando sull'icona a forma di collegamento (una catena), il Workbench apre una finestra di dialogo in sovraimpressione contenente l'**URL completo del repository** (ad esempio, terminante con `/repositories/Test` se il repository si chiama "Test"). Questo URL è la stringa esatta che deve essere copiata e passata al costruttore in Java per stabilire correttamente la connessione via API.

![center|500](img/Pasted%20image%2020260523151844.png)

![center|500](img/Pasted%20image%2020260523151908.png)