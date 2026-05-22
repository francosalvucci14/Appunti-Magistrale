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