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
### Il Vantaggio Architetturale: Efficienza in Memoria

C'è un principio architetturale di vitale importanza che accomuna l'intero modulo RIO (sia per la lettura che per la scrittura): **non c'è mai bisogno di avere tutti gli statement caricati simultaneamente in memoria.**

Il framework è progettato per operare su flussi continui in modo estremamente efficiente:

- Durante il parsing, i _reader_ inviano all'handler i dati elaborando **uno statement alla volta**.
    
- In maniera del tutto speculare, un _writer_ è progettato per ricevere e serializzare sul flusso di output **uno statement alla volta**.


Questa natura incrementale garantisce che il consumo di memoria (RAM) rimanga costante e ridotto, permettendo al sistema di elaborare e trasferire moli di dati potenzialmente infinite senza rischiare blocchi o crash dell'applicazione.