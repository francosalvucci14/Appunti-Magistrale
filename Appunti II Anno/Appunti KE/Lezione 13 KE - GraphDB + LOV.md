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
# Ontotext GraphDB

**Ontotext GraphDB** è un database a grafo progettato come una famiglia di repository semantici altamente affidabili, scalabili e ricchi di funzionalità. È uno strumento pensato per gestire, interrogare e trarre inferenze da grandi moli di dati interconnessi.

L'ecosistema di GraphDB si articola in tre versioni principali per rispondere a diverse esigenze operative:

- **GraphDB Free:** È la versione gratuita, ideale per iniziare o per progetti non critici. Presenta una limitazione tecnica consistente nell'elaborazione di un massimo di due query in contemporanea (concorrenti).
    
- **GraphDB SE (Standard Edition):** È del tutto equivalente alla versione Free nelle sue funzionalità di base, ma rimuove completamente il limite sulle query concorrenti, permettendo un utilizzo molto più intensivo.
    
- **GraphDB EE (Enterprise Edition):** È la versione di punta, pensata per scenari critici. Opera in modalità cluster per garantire alta disponibilità, resilienza ai guasti (fault tolerance) e un throughput massimizzato.
    

Indipendentemente dalla versione, GraphDB offre una notevole flessibilità di rilascio, supportando tecnologie di deployment moderne come Docker o Puppet.
## Architettura e Funzionamento (GraphDB Free)

Per utilizzare la versione Free è sufficiente una registrazione sul sito di Ontotext, che permette di ricevere il link per il download via email. Dal punto di vista tecnico, GraphDB è implementato come un _Sail RDF4J_.

Viene tipicamente distribuito e utilizzato come un **server standalone**. Questa configurazione è estremamente pratica perché si tratta di una distribuzione autosufficiente: non richiede l'installazione e la configurazione di un servlet container esterno (come, ad esempio, Apache Tomcat). L'unico prerequisito è la presenza di Java 8 o superiore sul sistema ospite. L'avvio del server è rapido e avviene tramite l'esecuzione di un singolo script (es. `graphdb.cmd`).

Una volta in esecuzione, l'amministrazione del database avviene tramite il **GraphDB Workbench**, uno strumento grafico basato sul web, accessibile di default all'indirizzo locale sulla porta 7200.

### Prestazioni e Scalabilità

GraphDB è progettato per la gestione massiva di dati: è in grado di gestire decine di miliardi di statement RDF su un singolo server. Le operazioni di query e il ragionamento semantico (inferenza) si appoggiano su efficienti indici basati su file. La scalabilità del sistema si manifesta sia nel volume dei dati ospitabili, sia nella velocità di caricamento e di esecuzione delle deduzioni logiche.

Per agevolare l'inserimento di grandi moli di dati, è incluso lo strumento **LoadRDF**, che permette di creare e popolare i repository in tempi estremamente ridotti a partire da dataset molto grandi. Inoltre, il motore include un ottimizzatore di query avanzato che valuta dinamicamente diversi piani di interrogazione per garantire sempre la massima efficienza.

### Standard, Compatibilità e Integrazione

Il supporto agli standard del Web Semantico è totale. GraphDB offre pieno supporto al linguaggio di interrogazione **SPARQL 1.1** ed è nativamente compatibile con il framework RDF4J 2.0. Per chi utilizza ecosistemi differenti, è inclusa anche la compatibilità con Apache Jena tramite un apposito adattatore.

Il sistema gestisce perfettamente l'importazione e l'esportazione dei dati attraverso un'ampia varietà di sintassi RDF standard (come XML, N3, N-Triples, N-Quads, Turtle, TriG e TriX). Per gli sviluppatori che necessitano di estendere le funzionalità, il database espone un framework API per plugin, corredato di classi e interfacce pubbliche.

### Motore di Ragionamento (Reasoning) e Integrità dei Dati

Il cuore semantico di GraphDB è il suo motore di ragionamento, che deduce nuove informazioni (non esplicitamente dichiarate) a partire dai dati esistenti. Questo motore è pienamente compatibile con gli standard **RDFS** e **OWL 2** (nei profili RL e QL).

Oltre alle regole standard, il sistema supporta l'implementazione di regole personalizzate, che vengono ottimizzate per non degradare le prestazioni. È presente anche un supporto fortemente ottimizzato per l'integrazione di dataset disparati tramite la gestione del costrutto `owl:sameAs`.

Il database è intrinsecamente affidabile nel preservare la consistenza e l'integrità dei dati; ad esempio, gestisce in modo molto efficiente la "ritrazione" (la rimozione) degli statement che erano stati inferiti logicamente nel momento in cui i dati di origine subiscono aggiornamenti o cancellazioni.

### Indici Speciali e Ricerca Avanzata

Per coprire casi d'uso complessi, GraphDB affianca agli indici tradizionali delle strutture dati specializzate:

- **Indici Geo-spaziali:** Permettono di risolvere in modo molto efficiente interrogazioni basate su vincoli geografici, come la ricerca di elementi vicini (_near-by_), racchiusi in un perimetro (_within_) o a una certa distanza.
    
- **Ricerca Full-Text e Connettore Lucene:** Il database integra capacità di ricerca testuale basate su Apache Lucene. Il connettore Lucene integrato permette sia ricerche testuali normali che ricerche "faceted" (basate su aggregazioni e categorie) in modo estremamente veloce, mantenendosi automaticamente sincronizzato con i dati presenti in GraphDB.
    
- **RDF Rank:** Una funzionalità che permette di ordinare i risultati delle query non solo in ordine alfabetico o numerico, ma in base alla loro rilevanza o ad altre metriche di importanza nel grafo (simile all'algoritmo PageRank).
    
- **Notifiche:** Il sistema può generare notifiche sugli stream di aggiornamento, permettendo ad applicazioni client in ascolto di reagire in tempo reale alle modifiche apportate ai dati.

## Utilizzo di GraphDB 

L'avvio dell'ambiente di lavoro di GraphDB è un'operazione estremamente rapida. Trattandosi di una distribuzione _standalone_ (autosufficiente), una volta scompattato l'archivio di installazione, è sufficiente lanciare lo script eseguibile fornito nella cartella dei binari: `graphdb` per i sistemi basati su Linux o `graphdb.cmd` per gli ambienti Windows. Fatto ciò, l'interfaccia grafica di amministrazione, chiamata **Workbench**, diventa immediatamente accessibile tramite un qualsiasi browser web puntando all'indirizzo di rete locale, tipicamente sulla porta 7200 (ovvero `http://localhost:7200`).

Per facilitare un primo approccio, il sistema si avvia di default in modalità non sicura, ma è progettato per supportare nativamente robusti protocolli di sicurezza per gli ambienti di produzione. È infatti possibile abilitare l'autenticazione degli utenti, configurare un controllo degli accessi granulare basato sui ruoli (RBAC) e implementare la crittografia per proteggere i dati in transito.

### Il Workbench a colpo d'occhio

Accedendo al Workbench ci si trova di fronte a una dashboard organizzata e intuitiva. Sulla sinistra, un menu di navigazione verticale raggruppa tutte le funzionalità fondamentali: strumenti per l'importazione di dataset, l'esplorazione visuale e testuale del grafo, l'editor per scrivere ed eseguire interrogazioni SPARQL, i pannelli di monitoraggio delle performance e le impostazioni di sistema.

Al centro della schermata iniziale viene riportato lo stato delle connessioni attive; se non si è ancora connessi, il sistema invita a selezionare uno spazio di lavoro esistente o a crearne uno nuovo. Vengono inoltre mostrati i dettagli della licenza in uso (ad esempio, la validità perpetua e l'uso di core illimitati per la Free Edition).

![center|300](img/Pasted%20image%2020260526150201.png)
### La Creazione di un Repository

Il passaggio propedeutico e indispensabile per poter iniziare a lavorare con GraphDB è la creazione di un **repository**. Il repository è, a tutti gli effetti, il contenitore logico all'interno del quale verranno caricati e archiviati i dati (le triple RDF) ed è il soggetto primario su cui verranno eseguite quasi tutte le operazioni di interrogazione e inferenza. Il motore è capace di gestire e mantenere attivi molteplici repository contemporaneamente.

Il processo di creazione si articola in diverse fasi, iniziando dalla **scelta della tipologia**:

- **GraphDB Free (o standard):** È il database fisico tradizionale, che archivia concretamente i dati al suo interno, risponde alle query e gestisce gli aggiornamenti.
    
- **Ontop Virtual SPARQL:** È un repository virtuale. Non memorizza fisicamente i dati RDF, ma funge da intermediario che traduce "al volo" le interrogazioni SPARQL per interrogare un database relazionale (SQL) preesistente, esponendolo come un endpoint semantico.

![center|300](img/Pasted%20image%2020260526150223.png)

Una volta scelta la tipologia, si passa alla definizione dei **parametri di configurazione**, che modelleranno il comportamento del motore di ragionamento e di archiviazione:

**1. Inferenza, Validazione e Integrità**

- **Set di regole (Ruleset):** Definisce il livello di profondità dell'inferenza logica (ad esempio, profili RDFS o OWL). Si possono utilizzare regole integrate e altamente ottimizzate, oppure fornire set di regole personalizzate.
    
- **Ottimizzazione per `owl:sameAs`:** Questo costrutto, usato per dichiarare che due URI si riferiscono alla stessa entità, può essere molto oneroso da calcolare. È possibile regolarne il comportamento o disabilitarlo per massimizzare le performance durante l'ingestione di grossi volumi di dati.
    
- **Controllo di consistenza:** Se attivata, questa funzione vigila sull'integrità logica del grafo: qualora un'operazione di aggiornamento dovesse introdurre un'inconsistenza (una contraddizione logica rispetto all'ontologia di base), il sistema eseguirà un _rollback_, annullando la transazione.
    
- **Validazione SHACL:** Permette di attivare controlli strutturali sui dati in ingresso, assicurandosi che questi rispettino precisi schemi e topologie definite dall'utente, rifiutando le triple non conformi.
    
- **Modalità Sola Lettura (Read-only):** Questa opzione è pensata per "congelare" il database impedendo qualsiasi alterazione dei dati. Va solitamente attivata solo in un secondo momento, dopo aver concluso le fasi di creazione e popolamento del repository.

![center|300](img/Pasted%20image%2020260526150244.png)

**2. Indicizzazione e Limiti di Risorse**

- **Dimensione degli Entity ID:** GraphDB assegna un identificatore numerico interno a ogni elemento. Scegliendo un ID a 32-bit (sufficiente per la maggior parte dei casi d'uso), il database può supportare fino a poco più di 2 miliardi ($2^{31}$) di entità uniche. Esiste anche l'opzione a 40-bit per dataset di proporzioni mastodontiche.
    
- **Indice di Contesto (CPSO):** Abilitando questo indice si ottimizza drasticamente la gestione dei _named graphs_, facilitando le operazioni che coinvolgono il contesto (o la provenienza) delle triple.
    
- **Indice delle liste di predicati:** Attivando questa opzione, il sistema costruisce degli indici speciali (Subject-Predicate e Object-Predicate). Sono strutture dati che accelerano in maniera significativa le interrogazioni in cui il predicato non è esplicitato nella query, una situazione frequente in database che contengono una varietà estremamente vasta di predicati diversi.
    
- **Limiti operativi (Query e Timeout):** Per garantire la stabilità del server ed evitare che un'interrogazione scritta male o troppo complessa monopolizzi le risorse (bloccando il sistema), è possibile impostare delle soglie di sicurezza. Si può definire un tempo massimo di esecuzione (_Query timeout_) oltre il quale l'operazione viene recisa, e un numero massimo di risultati estraibili. Impostando questi valori su "0", si rimuove qualsiasi limite, permettendo esecuzioni illimitate nel tempo e nei risultati.

![center|300](img/Pasted%20image%2020260526150303.png)

Una volta completata la configurazione iniziale, il passaggio immediatamente successivo consiste nel connettersi al repository appena creato per renderlo operativo e iniziare a lavorarci.

### Selezione e Attivazione del Repository

L'interfaccia del Workbench rende l'attivazione dello spazio di lavoro molto intuitiva. Dalla schermata principale è possibile cliccare direttamente sul nome del repository di interesse (ad esempio, un ambiente denominato "Test") che appare nella lista degli spazi di lavoro non ancora connessi.

![center|300](img/Pasted%20image%2020260526150722.png)

In alternativa, l'interfaccia è provvista di un comodo menu a tendina situato in alto a destra, che permette di passare rapidamente da un repository all'altro in qualsiasi momento. Un aspetto molto utile di questo menu è la possibilità di ispezionare lo stato del database al volo: espandendo il menu e soffermandosi su un repository, il sistema fornisce un riepilogo dettagliato che include il tipo di database, i permessi (solitamente di lettura e scrittura) e un conteggio puntuale degli _statement_ (le triple RDF) presenti. Questo conteggio è particolarmente interessante perché divide nettamente le triple esplicitamente caricate dall'utente da quelle che il motore di inferenza ha dedotto logicamente, mostrando anche il rapporto di espansione tra i due insiemi.

![center|300](img/Pasted%20image%2020260526150733.png)
### Importazione dei Dati RDF

Con il repository attivo, lo step cruciale è popolarlo di dati. La procedura di importazione si avvia dal menu di navigazione laterale, espandendo la voce "Import" e selezionando l'opzione "RDF".

![center|300](img/Pasted%20image%2020260526150801.png)

L'ambiente di importazione è progettato per essere estremamente flessibile e offre due macro-strategie per caricare le triple nel database:

**1. User data (Dati inviati dal client)**

Questa modalità gestisce i dati inviati al server sotto forma di payload tramite una richiesta HTTP. È la scelta ideale per flussi di lavoro agili e per dataset di dimensioni contenute. Offre tre percorsi:

- **Upload RDF files:** Permette di caricare fisicamente i file dal proprio computer tramite il browser. Per evitare sovraccarichi del server, questa opzione ha tipicamente un limite di dimensione massima (es. 200 MB).
    
- **Get RDF data from a URL:** Consente di istruire GraphDB affinché vada a recuperare e scaricare autonomamente un file RDF ospitato su un server web esterno, fornendo semplicemente il suo indirizzo.
    
- **Import RDF text snippet:** Una comodissima area di testo in cui è possibile incollare direttamente righe di codice RDF, utilissima per test rapidi o per l'inserimento di pochissime triple senza dover creare un file apposito.

![center|300](img/Pasted%20image%2020260526150822.png)

**2. Server files (File residenti sul server)**

Questa è l'opzione d'elezione per importare dataset massivi. Consente di caricare triple attingendo a file che sono stati precedentemente trasferiti e posizionati in una specifica cartella all'interno del filesystem del server che ospita GraphDB. In questo modo si aggirano i limiti e le potenziali instabilità di un caricamento via browser per file di svariati gigabyte.

Il motore di importazione è altamente compatibile e riconosce nativamente tutti i principali standard di serializzazione del Web Semantico, tra cui `.ttl` (Turtle), `.rdf` (RDF/XML), `.rj`, `.n3`, `.nt`, `.nq`, `.trig`, `.trix`, `.brf` e `.owl`. Per ottimizzare i tempi di trasferimento e lo spazio di archiviazione, GraphDB è in grado di leggere e importare i dati direttamente da file compressi, accettando formati come `.gz` o archivi `.zip`.

## La Ricerca dell'Ontologia: Il ruolo di LOV

A questo punto, avendo compreso la meccanica di importazione, è necessario procurarsi dei dati concreti. Supponendo di voler strutturare una base di conoscenza che descriva le persone e le loro relazioni sociali, si pone il problema di trovare un vocabolario adatto senza doverlo reinventare da zero.

La soluzione standard per questa esigenza è **Linked Open Vocabularies (LOV)**, accessibile all'indirizzo _lov.linkeddata.es_. LOV non è un database a grafo da interrogare per estrarre istanze o dati, ma è un'infrastruttura fondamentale: un **catalogo curato** di vocabolari e ontologie.

LOV facilita immensamente il riuso delle ontologie nel Web Semantico grazie a diverse caratteristiche chiave:

- **Metadati strutturati:** I metadati che descrivono i vari vocabolari presenti nel catalogo sono a loro volta rappresentati in formato RDF. Per fare questo, LOV utilizza vocabolari specifici per la descrizione dei dataset, come VoID (Vocabulary of Interlinked Datasets) e VOAF (Vocabulary of a Friend).
    
- **Resilienza (Copia Cache):** Il Web è mutevole e i link possono rompersi. LOV conserva una copia cache di tutti i vocabolari indicizzati. Questo garantisce che, anche se il sito originale dell'autore dell'ontologia dovesse scomparire o risultare irraggiungibile, la definizione formale del vocabolario resterà comunque accessibile e scaricabile per l'importazione.
    
- **Accessibilità multicanale:** Il catalogo è pensato per integrarsi in vari flussi di lavoro. Può essere scaricato per intero tramite dump, interrogato con query semantiche attraverso uno SPARQL endpoint dedicato, o richiamato programmaticamente tramite API.
    
- **Ricerca mirata:** La sua interfaccia offre un potente motore di ricerca _full-text_ basato sui termini definiti dai vocabolari indicizzati. Inserendo concetti come "Person" o "knows", il motore restituisce un elenco delle ontologie più autorevoli e utilizzate che modellano esattamente quelle classi e proprietà, pronte per essere scaricate e importate in GraphDB.

L'esplorazione di un vocabolario all'interno del catalogo LOV (Linked Open Vocabularies) offre una panoramica estremamente ricca e dettagliata, fondamentale per valutare se un'ontologia sia adatta al proprio progetto prima di procedere all'importazione. Prendendo come esempio il popolarissimo vocabolario **FOAF (Friend of a Friend)**, progettato per descrivere le persone e le loro reti di relazioni, LOV espone una serie di cruscotti informativi cruciali.

### Analisi di un Vocabolario su LOV

La pagina dedicata a un vocabolario su LOV non si limita a fornire l'URI e il namespace, ma funge da vero e proprio hub di analisi semantica, strutturato in diverse sezioni:

**1. Statistiche e Metadati Base**

Viene presentato un riepilogo quantitativo del contenuto dell'ontologia, indicando l'esatto numero di Classi e Proprietà definite al suo interno (e le eventuali istanze o tipi di dato). Questo permette di capire immediatamente la complessità e la granularità del modello. Vengono inoltre esplicitati i linguaggi di rappresentazione utilizzati, definendo l'**espressività** del vocabolario (ad esempio, se sfrutta costrutti base di RDF o regole più complesse di RDFS e OWL).

**2. Integrazione con Servizi Esterni**

LOV facilita il lavoro dell'ingegnere della conoscenza mettendo a disposizione scorciatoie per analizzare il vocabolario tramite potenti strumenti di terze parti:

- **WebVOWL:** Permette di generare istantaneamente una visualizzazione grafica interattiva dell'ontologia, mostrando nodi e archi.
    
- **OOPS! (OntOlogy Pitfall Scanner):** Esegue una scansione diagnostica per rilevare potenziali errori logici, trappole architetturali o cattive pratiche nella costruzione dell'ontologia.
    
- **Vapour:** Un servizio utile per verificare la corretta "dereferenziazione" degli URI (ovvero assicurarsi che gli indirizzi web del vocabolario restituiscano effettivamente dati elaborabili dalle macchine) e generare documentazione HTML.
    
- **RDF Triple-Checker:** Un validatore sintattico per scovare refusi o problemi comuni nel codice RDF.
    

**3. Classificazione e Impatto nel Web dei Dati**

Ogni vocabolario è associato a dei **Tag** semantici (es. _People_) per facilitarne la scoperta. Ancora più importante, LOV si interfaccia con _LODStats_ per mostrare le **statistiche d'uso reali**: indica in quanti dataset pubblici (Linked Open Data) quel preciso vocabolario viene correntemente utilizzato. Un alto numero di riutilizzi è un forte indicatore di stabilità e standardizzazione.

**4. Interconnessioni (La Rete dei Vocabolari)**

Una delle visualizzazioni più potenti è il grafo dei collegamenti. Mostra graficamente come l'ontologia si inserisce nell'ecosistema globale:

- **Incoming Links:** Quali e quanti altri vocabolari esterni riutilizzano o puntano a FOAF.
    
- **Outgoing Links:** Su quali altri standard FOAF si appoggia (ad esempio, è normale vedere collegamenti in uscita verso _rdfs_, _owl_ o _dublin core_).
    
    I collegamenti sono classificati per tipologia tramite un codice colore, distinguendo se un'ontologia ne estende un'altra, la specializza, ne importa i concetti o ne dichiara l'equivalenza.
    

**5. Storico delle Versioni**

Infine, una timeline interattiva mostra l'evoluzione temporale del progetto, permettendo di rintracciare gli aggiornamenti passati e, se necessario per questioni di retrocompatibilità, scaricare specifiche versioni storiche.

### Importazione pratica in GraphDB tramite URL

Una volta individuata e validata l'ontologia su LOV, si può procedere a caricarla nel proprio ambiente GraphDB. Sfruttando la funzione **"Get RDF data from a URL"** (descritta in precedenza), il processo è rapido e controllato.

Inserendo l'indirizzo web dell'ontologia (ad esempio `http://xmlns.com/foaf/0.1/`), GraphDB aprirà un pannello di configurazione per definire le regole di importazione. Questa è una fase delicata in cui si decide la topologia del database:

- **Scelta del Grafo di Destinazione (Target Graph):** Si può scegliere di riversare tutte le nuove triple nel contenitore generico del database (il _default graph_) oppure, pratica caldamente consigliata per mantenere l'ordine, inserirle in un **Grafo Nominato (Named Graph)** specifico. Spesso si utilizza l'URL stesso dell'ontologia come nome del grafo, creando così un compartimento stagno che rende molto più semplice la futura gestione o rimozione di quel set di dati.
    
- **Gestione delle Sovrascritture:** Se il grafo di destinazione esiste già, il sistema permette di abilitare la sostituzione dei dati. Selezionando questa opzione (che richiede una spunta di conferma esplicita per evitare disastri), GraphDB svuoterà completamente il grafo nominato prima di importarvi i nuovi dati, garantendo che non rimangano triple orfane o obsolete da importazioni precedenti.
    
- **Impostazioni Avanzate:** È possibile accedere a un menu contestuale per definire dettagli tecnici, come la conservazione degli identificatori per i nodi vuoti (_bnode ID_) o forzare ulteriori controlli sintattici durante il parsing.

![center|300](img/Pasted%20image%2020260526151946.png)

Confermate le impostazioni, il sistema prende in carico la richiesta. L'interfaccia del Workbench mostrerà la risorsa in un elenco di attività in corso con lo stato "Importing...", offrendo all'utente la possibilità di interrompere forzatamente il processo tramite un pulsante "Abort" qualora ci si accorga di aver commesso un errore di configurazione.
## Visualizzazioni

Per estrarre reale valore e comprensione da un database a grafo, la semplice interrogazione testuale spesso non è sufficiente. Disporre di visualizzazioni opportune è un requisito indispensabile per navigare la complessità dei dati interconnessi, riconoscere pattern nascosti e, in ultima analisi, generare _insight_ (intuizioni e approfondimenti) utili.

Per rispondere a questa esigenza, l'ambiente di lavoro di GraphDB è equipaggiato con una suite di strumenti di esplorazione visiva, pensati per analizzare il dato da diverse prospettive:

- **Resource view:** un'ispezione tabellare dettagliata per leggere e modificare le triple legate a una singola entità.
    
- **Visual graph:** una rappresentazione a nodi e archi per esplorare interattivamente la connettività e i percorsi tra le risorse.
    
- **Domain-range graph:** utile per gli architetti dell'informazione, mappa le relazioni formali tra le classi definite nell'ontologia.
    
- **Class relationships:** una vista aggregata che mostra le connessioni basate non sulle definizioni astratte, ma sulle istanze reali delle classi presenti nei dati.
    

Un elemento che lavora dietro le quinte per migliorare la leggibilità di queste visualizzazioni è l'**RDF Rank**. Questo algoritmo calcola dinamicamente un indice di "importanza" per ogni nodo del grafo (in modo concettualmente simile al PageRank dei motori di ricerca). Nelle visualizzazioni complesse, l'RDF Rank viene sfruttato per esaltare i nodi centrali e tagliare le ramificazioni meno rilevanti, evitando di sommergere l'utente in una ragnatela illeggibile di informazioni.

### L'esplorazione macroscopica: Graph Overview

Il punto di partenza naturale per esplorare un repository appena popolato è la sezione **Graphs overview**, accessibile dal menu "Explore". Questa schermata offre una visione di altissimo livello sull'organizzazione logica dei dati.

Invece di mostrare le singole triple, presenta un elenco di tutti i **grafi nominati** (Named Graphs) attualmente presenti nel database, incluso il _Default graph_ (il contenitore generico). Questa vista funge da vero e proprio pannello di controllo amministrativo per i set di dati: da qui è possibile eseguire operazioni di pulizia radicale (_Clear repository_) o esportazione massiva (_Export repository_), così come agire chirurgicamente sui singoli grafi, svuotandoli o esportandone il contenuto in modo indipendente.

![center|300](img/Pasted%20image%2020260526152626.png)
### L'ispezione microscopica: Resource View

Se la _Graph overview_ offre una vista dall'alto, il **Resource view** rappresenta la lente d'ingrandimento del sistema. È una visualizzazione ad altissima risoluzione dedicata allo studio approfondito di una specifica risorsa (identificata dal suo URI).

Accedendo al Resource view di un'entità, il sistema organizza tutti gli _statement_ (le triple) che la coinvolgono in una chiara griglia composta da Soggetto, Predicato, Oggetto e Contesto (il grafo di appartenenza). La potenza di questo strumento risiede nei suoi filtri dinamici, che permettono di analizzare la risorsa sotto ogni sua sfaccettatura:

- Come **Soggetto**: per scoprire tutto ciò che definisce la risorsa (le sue proprietà e attributi).
    
- Come **Oggetto**: per tracciare i riferimenti in ingresso, ovvero quali altre entità del database puntano a questa risorsa.
    
- Come **Predicato**: per capire, qualora la risorsa sia una proprietà, tra quali soggetti e oggetti sta stabilendo una connessione.
    
- Per **Contesto**: per isolare le informazioni provenienti da uno specifico grafo nominato.

![center|400](img/Pasted%20image%2020260526152646.png)

L'interfaccia offre ulteriori strumenti di raffinamento essenziali per chi lavora con il Web Semantico. Un menu a tendina cruciale permette di filtrare i dati in base alla loro natura logica: si può scegliere di visualizzare solo gli statement **espliciti** (i dati grezzi originariamente importati), solo quelli **impliciti** (le nuove deduzioni matematicamente generate dal motore di ragionamento), oppure una visione combinata di entrambi.

Sono presenti anche comandi rapidi per mostrare o nascondere i _Blank Nodes_ (nodi anonimi senza un URI univoco, spesso usati per strutture dati complesse), un pulsante per scaricare istantaneamente il pacchetto di triple visualizzato in vari formati RDF, e un bottone per saltare direttamente dalla visualizzazione tabellare a quella grafica a nodi e archi (_Visual graph_).

Infine, il Resource view non è un ambiente di sola lettura. Funge anche da editor principale dell'interfaccia: permette agli utenti autorizzati di modificare, cancellare o aggiungere manualmente singoli statement, o persino di definire nuove risorse da zero direttamente dal browser.

Oltre all'ispezione delle singole risorse, GraphDB offre potenti strumenti visivi per comprendere la struttura logica e l'architettura dell'ontologia caricata. Questi strumenti sono fondamentali per gli ingegneri della conoscenza, in quanto permettono di validare il modello dati e di navigarlo a livello concettuale, prima ancora di analizzare i dati reali (le istanze).

### La Visualizzazione Tassonomica: Class Hierarchy

Accessibile dal menu "Explore", la sezione **Class hierarchy** fornisce una rappresentazione interattiva della tassonomia del vocabolario. Invece del classico albero a cartelle, GraphDB utilizza spesso un diagramma a bolle annidate o un grafo radiale per mostrare le relazioni di sussunzione (relazioni "is-a") tra le classi.

Questo strumento permette di visualizzare ed esplorare l'intera gerarchia: le bolle più grandi rappresentano le superclassi (ad esempio, `Agent`), mentre le bolle contenute al loro interno o collegate gerarchicamente verso il basso rappresentano le sottoclassi più specifiche (ad esempio, `Person` o `Organization` come sottoclassi di `Agent`).

Per gestire ontologie estremamente vaste senza sovraccaricare l'interfaccia visiva, la vista _Class hierarchy_ implementa meccanismi di filtraggio intelligenti:

- **Priorità per popolarità:** È possibile limitare il numero totale di classi disegnate a schermo, istruendo il sistema a dare la priorità (mostrare per prime) alle classi che possiedono il maggior numero di istanze effettive nel database.
    
- **Slider di conteggio:** Un selettore grafico (spesso una barra verticale sulla sinistra) permette di aggiustare dinamicamente quante classi visualizzare contemporaneamente (es. le "Top 14").

![center|400](img/Pasted%20image%2020260526153053.png)

Interagendo con le bolle (cliccando su una specifica classe, come `foaf:Person`), si apre un **pannello laterale di dettaglio**. Questo cruscotto fornisce informazioni essenziali in tempo reale:

- Le etichette descrittive (`rdfs:label`) e i commenti testuali (`rdfs:comment`) associati alla classe.
    
- Un contatore delle istanze (fino a un massimo di 1000 visualizzate direttamente, con un pulsante rapido per generare una query SPARQL che le estragga tutte).
    
- Un collegamento diretto per passare immediatamente all'analisi delle proprietà di quella specifica classe tramite la visualizzazione _Domain-Range Graph_. Se la classe selezionata non ha ancora istanze caricate nel database, il sistema mostrerà un avviso informativo, ma permetterà comunque di navigarne la struttura teorica.

![center|400](img/Pasted%20image%2020260526153124.png)

### L'Analisi Assiomatica: Domain-Range Graph

Mentre la _Class hierarchy_ mostra "chi è figlio di chi", il **Domain-Range Graph** si concentra sulle regole di connessione. È uno strumento di analisi assiomatica che mappa visivamente le relazioni tra le classi attraverso le proprietà (i predicati) definite nell'ontologia.

Quando si centra la vista su una specifica classe radice (ad esempio, il nodo centrale arancione `foaf:Person`), il grafo si espande mostrando due direzioni fondamentali:

1. **Proprietà in uscita (Domain):** Gli archi che partono dalla classe centrale mostrano le proprietà per le quali quella classe funge da "dominio" (Domain). In parole povere, risponde alla domanda: "Quali caratteristiche può avere una Persona?". Gli archi puntano verso i nodi che rappresentano il "codominio" o "range" consentito (es. `foaf:knows` punta verso un'altra `Person`, mentre `foaf:based_near` potrebbe puntare a una `SpatialThing`).
    
2. **Proprietà in entrata (Range):** Gli archi che puntano _verso_ la classe centrale mostrano le proprietà in cui quella classe è il "range" atteso. Risponde alla domanda: "Quali altre entità possono avere una Persona come attributo?". (es. un `foaf:Group` ha una proprietà `foaf:member` che punta a una `Person`).

![center|400](img/Pasted%20image%2020260526153148.png)

Per mantenere il grafo leggibile, le proprietà che condividono le stesse esatte classi di dominio e range vengono raggruppate (collassate) in un singolo arco in grassetto (es. "8 predicates" o "19 predicates"), cliccabile per svelare l'elenco completo dei predicati nascosti.

#### Il concetto di "Proprietà Implicita"

Una delle caratteristiche più avanzate del Domain-Range Graph è la capacità di gestire le **proprietà implicite**. Spesso, l'interazione tra le regole di dominio/range e la gerarchia delle classi crea deduzioni non scritte esplicitamente nel codice.

Il grafo utilizza stili di linea differenti (es. linee tratteggiate) per indicare queste proprietà ereditate. Ad esempio, se si analizza la proprietà `maker` tramite il Resource View, si potrebbe notare che il suo dominio è la classe molto generica `owl:Thing` e il suo range è `foaf:Agent`. Tuttavia, nel Domain-Range graph di `foaf:Person`, la proprietà `maker` appare in ingresso come proprietà implicita. Il motivo logico è che `Person` è una sottoclasse di `Agent`; pertanto, poiché qualsiasi cosa (`Thing`) può avere come "creatore" (`maker`) un `Agent`, il motore inferenziale deduce automaticamente che è perfettamente valido che il creatore sia, più specificamente, una `Person`. Questa visualizzazione rende palese questo livello di intelligenza del database.

![center|400](img/Pasted%20image%2020260526153205.png)
### Uno sguardo al futuro: Class Relationships

Oltre alle viste basate sullo schema teorico (come Hierarchy e Domain-Range), esiste la vista **Class relationships**. Questa visualizzazione è profondamente diversa: non si basa su ciò che l'ontologia _permette_ in teoria, ma analizza le relazioni tra le classi basandosi esclusivamente sui **legami reali esistenti tra le loro istanze** (i dati concreti caricati).

Se si tenta di aprire questo diagramma in un repository appena creato, contenente solo lo schema del vocabolario (come FOAF) ma senza alcun dato reale sulle persone, il sistema mostrerà un avviso indicando che non ci sono dipendenze da visualizzare. Questa vista diventa lo strumento principale di indagine solo nella fase successiva, dopo che il database è stato popolato con le istanze effettive.

Dopo aver caricato lo schema dell'ontologia (ad esempio, FOAF), il database possiede la struttura logica ma è ancora privo di dati reali. Per iniziare a testare query e visualizzazioni, è necessario popolarlo con alcune istanze. Un metodo rapido per farlo senza dover preparare file esterni è l'inserimento diretto tramite frammenti di testo (snippet).

## Importazione RDF tramite Text Snippet

Dalla sezione "Import" -> "RDF" del Workbench, si seleziona l'opzione **"Import RDF text snippet"**. Questa funzionalità apre una finestra di dialogo contenente un'area di testo libera, in cui è possibile incollare o digitare direttamente codice RDF.

Per l'inserimento manuale, il formato di serializzazione più comodo e leggibile è solitamente il **Turtle (`.ttl`)**. Un tipico snippet di popolamento si articola in due fasi:

1. **Dichiarazione dei prefissi:** Si indicano le abbreviazioni per i namespace utilizzati, per evitare di scrivere URI lunghissimi (es. `@prefix : <http://example.org/> .` per le risorse locali, e i prefissi standard come `foaf:`).
    
2. **Definizione delle istanze e delle relazioni:** Si dichiarano i soggetti e le loro proprietà. Ad esempio, si possono creare istanze di fantasia della classe `foaf:Person` (es. `:john a foaf:Person ; foaf:givenName "John"` ecc.) e definire relazioni tra di loro usando i predicati dell'ontologia (es. `:john foaf:knows :mary`).

**Esempio di inserimento dati**

![center|350](img/Pasted%20image%2020260526153902.png)

Una volta incollato il codice, il pulsante "Import" avvia il processo. Come avviene per l'importazione da URL, il sistema chiederà di specificare i _Target graphs_. Per mantenere l'ordine, è buona pratica non mescolare i dati grezzi con la definizione dell'ontologia, ma inserire le nuove triple in un **Grafo Nominato** dedicato (es. chiamato `http://example.org/`).

### Gestione dei Namespace (Setup)

Dopo aver caricato dati o ontologie, è utile verificare la configurazione dei namespace. Accedendo alla sezione **Setup -> Namespaces**, GraphDB mostra una tabella con tutti i prefissi attualmente registrati e i relativi URI completi.

Questa gestione è cruciale per la leggibilità. Quando l'ontologia FOAF è stata importata, GraphDB ha automaticamente estratto e registrato la definizione per il prefisso `foaf:`. Grazie a questo passaggio automatico, in tutte le visualizzazioni del Workbench (e nelle query SPARQL), il sistema è in grado di abbreviare gli URI lunghi, mostrando all'utente stringhe compatte e leggibili come `foaf:Person` al posto di `http://xmlns.com/foaf/0.1/Person`. Da questo pannello, l'utente può anche aggiungere manualmente nuovi prefissi o modificare quelli esistenti.

### Autocompletamento (Autocomplete Index)

Un'altra funzionalità fondamentale di "Setup" per migliorare l'esperienza d'uso è l'**Autocomplete index**. GraphDB non lo attiva di default su tutti i repository per risparmiare risorse di calcolo e memoria, ma è caldamente consigliato abilitarlo per gli spazi di lavoro attivi.

Andando su **Setup -> Autocomplete**, si trova un interruttore generale ("Autocomplete for repository X is OFF"). Attivandolo (spostandolo su ON), il sistema inizia a costruire un indice speciale. Questo indice analizza il testo presente nelle etichette delle risorse (solitamente la proprietà `rdfs:label`) in tutte le lingue supportate.

Una volta che l'indice è stato costruito (lo stato diventa "Ready"), la barra di ricerca universale presente in molte schermate del Workbench (come in "Explore -> Resource view") diventerà "intelligente": iniziando a digitare il nome di una persona, di una classe o di un concetto, il sistema suggerirà dinamicamente le risorse corrispondenti, eliminando la necessità di ricordare a memoria gli URI esatti.
## Visual Graph

L'esplorazione dei dati raggiunge il suo massimo livello di intuitività con il **Visual Graph**, uno strumento interattivo che permette di navigare le relazioni tra le risorse non attraverso tabelle o codice, ma visivamente, muovendosi da un nodo all'altro.

Accedendo alla sezione "Explore -> Visual graph", il Workbench offre tre diverse modalità di partenza per generare la visualizzazione:

- **Easy graph:** È la via più rapida. Sfruttando l'indice di autocompletamento (se attivato in precedenza), è sufficiente digitare il nome di una risorsa (ad esempio "john") per trovarne l'IRI esatto e generare il grafo istantaneamente, senza scrivere una singola riga di codice SPARQL.
    
- **Advanced graph configurations:** Dedicato agli utenti esperti, permette di definire regole di visualizzazione su misura scrivendo query SPARQL personalizzate, filtrando a monte cosa deve essere disegnato a schermo.
    
- **Saved graphs:** Un comodo archivio per richiamare istantanee di grafi visivi precedentemente salvate, utile per riprendere il lavoro o condividere una specifica vista.

![center|400](img/Pasted%20image%2020260526155028.png)
### L'esperienza di navigazione e l'interfaccia

Scegliendo l'approccio _Easy graph_ e centrando la vista su una risorsa specifica (come la nostra istanza di fantasia `:john`), l'interfaccia disegna una mappa concettuale dinamica.

Gli elementi visivi sono codificati per trasmettere informazioni a colpo d'occhio:

- **I Nodi (Cerchi):** Rappresentano le risorse individuali (es. John, Mary, Philip, Alice). Il colore del nodo è determinato automaticamente dalla classe di appartenenza (tutte le istanze di `foaf:Person` avranno lo stesso colore).
    
- **Gli Archi (Frecce):** Rappresentano i predicati che collegano le risorse, mostrando chiaramente la direzione della relazione (es. la freccia `knows` da John a Philip).
    

L'ambiente non è statico, ma altamente interattivo. In alto a destra è presente una barra degli strumenti che offre molteplici possibilità di configurazione del layout e il salvataggio della vista. Inoltre, interagendo direttamente con un nodo, appare un **menu contestuale radiale** che offre azioni rapide:

- Espandere il nodo per rivelare ulteriori connessioni nascoste.
    
- Centrare l'intero grafo su quel nodo specifico, cambiando il punto di vista.
    
- Rimuovere il nodo dalla visualizzazione per fare pulizia.
    
- Aprire il pannello delle informazioni.

![center|400](img/Pasted%20image%2020260526155105.png)

### Il Pannello delle Informazioni (Info Panel)

Cliccando sull'icona delle informazioni ("i") di un nodo, si apre un pannello laterale di dettaglio. Questo cruscotto è fondamentale perché, mentre il grafo mostra i collegamenti ad _altre risorse_ (Object Properties), il pannello laterale elenca tutte le proprietà intrinseche della risorsa stessa (Datatype Properties).

Qui è possibile leggere immediatamente:

- I **tipi** a cui la risorsa appartiene (es. `foaf:Person`).
    
- Le etichette testuali (`rdfs:label`) e i commenti (`rdfs:comment`).
    
- I valori letterali associati, come `foaf:givenName` ("John") o `foaf:familyName` ("Someone").
    
- Eventuali immagini associate (`foaf:depiction`), che GraphDB è in grado di renderizzare direttamente come miniature all'interno del pannello.

![center|400](img/Pasted%20image%2020260526155140.png)
### Il ruolo cruciale dell'RDF Rank nella visualizzazione

Quando si ha a che fare con nodi estremamente interconnessi (i cosiddetti _hub_, come potrebbe essere una grande città in un database geografico o un autore prolifico), disegnare tutti i collegamenti contemporaneamente renderebbe il grafo un groviglio illeggibile.

Qui entra in gioco l'**RDF Rank**, un valore numerico (visibile anche nel pannello info) che GraphDB calcola per stimare la popolarità e l'importanza di una risorsa all'interno del database:

1. **Gestione del limite:** Di default, il Visual Graph mostra al massimo 20 connessioni in uscita da un nodo. Se ne esistono di più, il sistema utilizza l'RDF Rank per scegliere quali mostrare, dando la priorità alle connessioni che puntano verso le risorse statisticamente più "importanti".
    
2. **Impatto visivo:** La dimensione fisica del nodo sullo schermo è direttamente proporzionale al suo RDF Rank. Un nodo con un rank elevato (es. 0.76) apparirà come una bolla visibilmente più grande rispetto a un nodo periferico con rank 0, permettendo all'utente di discriminare immediatamente i centri di gravità del database dalle risorse minori.

L'RDF Rank è un elemento centrale nell'ecosistema di GraphDB, essenziale per estrarre senso e ordine da grafi complessi e massivi. Per comprenderne appieno il valore e il funzionamento, è utile approfondirne le basi matematiche (vedi [qui](#^e63eee)) e le modalità operative all'interno del Workbench.
#### Configurazione e Calcolo nel Workbench

Poiché il calcolo di questi punteggi sull'intero grafo è un'operazione matematicamente intensiva, GraphDB non la esegue automaticamente di default, ma la affida al controllo dell'utente.

Accedendo al menu **Setup -> RDF Rank**, si entra nel pannello di amministrazione dedicato. L'interfaccia indica chiaramente lo stato attuale (es. "RDFRank not built yet"). Il calcolo non avviene tramite un motore separato, ma, in modo molto elegante, GraphDB sfrutta la sua stessa potenza semantica: dietro le quinte, il sistema lancia una serie di complesse query di **UPDATE SPARQL** direttamente sul repository per calcolare i valori e scriverli nel database come normali triple.

##### Filtri e Focus

Prima di avviare il calcolo, l'interfaccia offre un potente interruttore di **Filtering**. Attivandolo, si apre un pannello di configurazione avanzata che permette di "ritagliare" la porzione di grafo su cui l'algoritmo deve concentrarsi. Questo è cruciale in database enormi dove si vuole valutare l'importanza delle risorse solo in un contesto specifico.

- **Contenuto Logico:** Si può decidere se l'algoritmo debba navigare solo le triple _esplicite_ (caricate manualmente) o se debba percorrere anche le triple _implicite_ (inferite dal ragionatore).
    
- **Filtri Topologici:** Attraverso le schede "Graphs" e "Predicates", è possibile includere o escludere interamente specifici grafi nominati o specifici predicati dal calcolo (ad esempio, calcolare il rank basandosi solo sulle relazioni sociali `foaf:knows`, ignorando le proprietà descrittive come `rdfs:label`).
##### Ricomputo: Completo vs Incrementale

Una volta configurato, il pulsante **Compute Full** avvia il processo. Se il database è grande, questa operazione può richiedere tempo, poiché ricalcola la catena di Markov da zero.

Tuttavia, i database reali sono entità vive e in continua evoluzione (si aggiungono nuovi utenti, si creano nuove relazioni). Rifare un _Compute Full_ ad ogni singolo aggiornamento sarebbe computazionalmente insostenibile.

![center|400](img/Pasted%20image%2020260526155655.png)

Per risolvere questo problema operativo, una volta che il calcolo completo iniziale è stato eseguito con successo, GraphDB sblocca una funzionalità avanzata: il **ricomputo incrementale**. Questa modalità utilizza un algoritmo alternativo e molto più rapido che non riparte da zero, ma aggiorna i valori di RDF Rank preesistenti tenendo conto solo delle ultime modifiche apportate alla base di conoscenza. Sebbene questo metodo introduca delle lievi approssimazioni matematiche rispetto al calcolo completo, offre un compromesso eccellente, permettendo di mantenere i ranghi delle risorse costantemente aggiornati in un contesto di produzione dove gli inserimenti di dati sono frequenti.

### Class Relationships (Relazioni tra Classi Basate sui Dati)

In precedenza avevamo accennato al diagramma **Class relationships**. A differenza delle visualizzazioni basate sull'ontologia pura (che mostrano cosa è _possibile_ in teoria), questo strumento diventa prezioso solo dopo aver popolato il database, perché mostra cosa _esiste realmente_ nei dati.

Questa vista genera un diagramma a corda (chord diagram) circolare. Lungo la circonferenza sono disposte le classi presenti nel repository (es. `foaf:Person`, `foaf:Document`, `foaf:Group`). Tra queste classi vengono disegnati dei **fasci (chords)** che attraversano il cerchio.

La lettura di questo diagramma segue regole precise:

- **Il Fascio:** Ogni corda rappresenta un gruppo di collegamenti (statement) che uniscono istanze di due classi diverse.
    
- **L'Ampiezza:** Lo spessore del fascio alla base di una classe indica la quantità: più il fascio è largo, maggiore è il numero di link (le relazioni) stabiliti tra quelle due classi specifiche.
    
- **Il Colore e la Direzione:** Il fascio assume il colore della classe che riceve il maggior numero di link entranti da quella specifica relazione, aiutando a identificare a colpo d'occhio i flussi di dipendenza (chi punta a chi).

![center|400](img/Pasted%20image%2020260526160030.png)

A sinistra del diagramma, una tabella riepilogativa permette di filtrare la vista, mostrando solo le relazioni in ingresso (Incoming) o in uscita (Outgoing) per ogni classe, e riportando il numero esatto di link rilevati, fornendo così una mappa empirica di come i dati sono interconnessi nella realtà del nostro database.

## L'Editor SPARQL: Interrogare il Grafo

Le visualizzazioni sono eccellenti per l'esplorazione, ma per estrarre dati specifici, eseguire calcoli o aggiornare il database in modo massivo, si utilizza il linguaggio standard del Web Semantico: **SPARQL**. GraphDB fornisce un potente ambiente di sviluppo integrato (IDE) accessibile dalla sezione **SPARQL**.

L'interfaccia principale è l'**Editor Query & Update**, diviso in due aree principali: l'area di scrittura del codice in alto e l'area di presentazione dei risultati in basso.

### Scrivere ed Eseguire Query

L'editor di testo supporta funzionalità avanzate come l'evidenziazione della sintassi (syntax highlighting), l'autocompletamento (premendo `Alt+Enter`) e la gestione automatica dei prefissi (se dichiarati nella sezione Setup, non è necessario scriverli a mano nella query).

Per eseguire una query (ad esempio, una `SELECT` per trovare tutte le conoscenze di "John" e concatenare nome e cognome), si preme il pulsante **Run** (o la scorciatoia `Ctrl/Cmd+Enter`). Se la query è formulata correttamente, i risultati appariranno nella sezione sottostante sotto forma di tabella strutturata in colonne (le variabili richieste nella `SELECT`).

![center|400](img/Pasted%20image%2020260526160045.png)

![center|400](img/Pasted%20image%2020260526160106.png)
### Strumenti dell'Editor

Sulla destra dell'area di testo, una barra degli strumenti verticale offre opzioni essenziali per il flusso di lavoro dello sviluppatore:

- **Salvare e Aprire:** Icone per salvare la query corrente nel Workbench o caricare query precedentemente salvate, permettendo di costruire una libreria di interrogazioni utili.
    
- **Condividere (Link alla query):** Genera un URL diretto (spesso molto lungo) che incorpora l'intera query. È utile per inviarla a un collega; aprendo il link, l'editor si popolerà automaticamente con quel codice.
    
- **Espansione `owl:sameAs` (Icona a tre cerchi):** Questo è un interruttore cruciale. Se attivato, GraphDB espanderà i risultati considerando l'equivalenza delle entità (se A è `sameAs` B, i risultati includeranno i dati di entrambi). Se disattivato, tratterà i nodi equivalenti come entità rigidamente separate, considerando solo il rappresentante formale della classe di equivalenza. Questo pulsante è utilissimo per fare debugging sulle regole di integrazione dei dati.

![center|400](img/Pasted%20image%2020260526160122.png)

### Il Potere dell'Inferenza (Il pulsante ">>")

L'icona con la doppia freccia (`>>`), situata proprio sopra il pulsante Run, controlla il motore di ragionamento durante l'esecuzione della query.

Per capire la differenza, immaginiamo di chiedere a GraphDB: "Qual è il tipo (la classe) dell'istanza `:john`?" (`SELECT ?type { :john a ?type . }`).

- **Inferenza DISATTIVATA:** Il sistema si limita a leggere i dati grezzi che abbiamo inserito manualmente nello snippet. Il risultato sarà un'unica riga: `:john` è di tipo `foaf:Person`.
    
- **Inferenza ATTIVATA:** Il motore logico entra in azione. Sapendo (dall'ontologia FOAF che abbiamo importato all'inizio) che `Person` è una sottoclasse di `Agent`, e che `Agent` è a sua volta associato ad altri concetti (come `SpatialThing`), dedurrà logicamente tutte le appartenenze implicite. Il risultato mostrerà non una, ma molte righe: `:john` verrà classificato come `foaf:Person`, ma anche come `foaf:Agent`, `dcterms:Agent`, `wgs:SpatialThing`, ecc. Attivare o disattivare questo pulsante permette di esplorare l'abisso tra i dati crudi e la conoscenza dedotta.

![center|400](img/Pasted%20image%2020260526160134.png)

![center|400](img/Pasted%20image%2020260526160142.png)

### Gestione e Visualizzazione dei Risultati

L'area dei risultati non si limita a una semplice griglia. Offre diverse schede per analizzare l'output:

- **Table:** La visualizzazione standard a righe e colonne, con la possibilità di filtrare rapidamente i risultati testualmente. I risultati possono essere scaricati (Download as) in vari formati strutturati (CSV, JSON, XML) per l'uso in applicazioni esterne.
    
- **Raw Response:** Mostra la risposta grezza esatta (es. il file JSON) restituita dal server API, utile per gli sviluppatori.
    
- **Pivot Table:** Permette di raggruppare e incrociare i dati estratti per generare report tabellari complessi, simile alle funzioni dei fogli di calcolo.
    
- **Google Chart:** Questa scheda apre un editor grafico integrato. Permette di "agganciare" i dati tabellari appena estratti dalla query SPARQL e trasformarli istantaneamente in grafici visivi (a torta, a barre, a dispersione, mappe) sfruttando le librerie di Google Charts, fornendo così un rudimentale ma efficace strumento di business intelligence direttamente all'interno del database.

![center|400](img/Pasted%20image%2020260526160208.png)

Le prestazioni e il comportamento di GraphDB durante l'interrogazione (viste nel passaggio precedente) sono intimamente legate a come il sistema gestisce l'inferenza dietro le quinte.
## Reasoning
### La Strategia di Materializzazione Completa

GraphDB adotta un approccio al ragionamento semantico definito **materializzazione completa** (o _forward-chaining_ puro, nella sua implementazione di base).

Cosa significa in pratica? Quando l'inferenza è attiva, il motore applica ciclicamente tutte le regole logiche definite nel _ruleset_ scelto al momento della configurazione del repository. Questo processo iterativo continua fino a quando il sistema raggiunge un punto di saturazione, ovvero finché non è più matematicamente in grado di dedurre (inferire) alcuna nuova tripla dai dati esistenti. Tutte queste nuove triple dedotte vengono fisicamente scritte (materializzate) negli indici del database, esattamente come se fossero state inserite manualmente dall'utente.

Questa scelta architetturale ha un impatto profondo sulle performance:

- **Svantaggio in Scrittura:** Il "costo" computazionale del ragionamento viene interamente scaricato sulle operazioni di scrittura (inserimento, aggiornamento). Inserire nuovi dati è più lento, perché il sistema deve fermarsi a calcolare e scrivere tutte le conseguenze logiche prima di dichiarare conclusa la transazione.
    
- **Vantaggio in Lettura:** Le interrogazioni (query `SELECT`) sono estremamente veloci. Poiché tutte le possibili deduzioni sono già state pre-calcolate e salvate su disco, quando un utente lancia una query con l'inferenza attivata, GraphDB non deve fare alcun calcolo al volo; si limita a leggere i risultati già pronti dai suoi indici, garantendo tempi di risposta minimi.

### Gestione Monotona degli Aggiornamenti

La logica sottostante a questo meccanismo di inferenza è **monotona**. Questo significa che la conoscenza può solo crescere o restringersi in modo prevedibile.

- **Aggiunta di una tripla:** Inserire un nuovo dato non può mai invalidare o contraddire le deduzioni logiche fatte in precedenza. Può, al massimo, innescare nuove regole e generare _ulteriori_ inferenze. Pertanto, l'aggiornamento è efficiente: il sistema non riparte da zero, ma riprende il processo di iterazione partendo solo dalle regole attivate dalla nuova tripla appena inserita.
    
- **Rimozione di una tripla:** Questo è lo scenario critico. Cancellare un dato di partenza rischia di far crollare un intero castello di deduzioni (se la tripla A generava B, e rimuovo A, devo rimuovere anche B, a patto che non ci fosse un'altra tripla C che generava anch'essa B). L'approccio _naive_ (ingenuo) per risolvere questo problema sarebbe cancellare tutte le inferenze e ricalcolare tutto il database da zero ad ogni singola cancellazione. Ovviamente, man mano che il repository cresce, questo diventerebbe impossibile. Per ovviare a ciò, GraphDB implementa un raffinato algoritmo di **cancellazione incrementale**:
    
    1. Esegue una ricerca in avanti (_forward-chaining_) per identificare con precisione chirurgica solo le triple che derivavano direttamente dal dato appena rimosso.
        
    2. Successivamente, esegue un controllo a ritroso (_backward-chaining_) su quelle triple sospette, per verificare se esistano "vie alternative" per derivarle. Se una tripla inferita non ha più alcuna giustificazione valida nei dati rimanenti, viene rimossa in modo efficiente.
        

### L'Ottimizzazione di `owl:sameAs`

Una delle sfide computazionali più ardue nel Web Semantico è la gestione dell'identità. Il costrutto `owl:sameAs` dichiara che due risorse diverse si riferiscono allo stesso oggetto nel mondo reale.

Per le regole di OWL, questa proprietà è una **relazione di equivalenza** (è riflessiva, simmetrica e transitiva). L'implicazione matematica è pesante: se ho $N$ risorse dichiarate come equivalenti (una _clique_), il ragionatore standard genererà $N^2$ relazioni `sameAs` esplicite tra di loro. Ancora peggio, ogni singolo _statement_ associato a ciascuna risorsa verrebbe copiato e ripetuto per tutte le altre risorse del gruppo. In dataset complessi, questo causa un'esplosione combinatoria che intasa gli indici.

GraphDB risolve questo problema aggirando il motore a regole standard. Offre un'**implementazione non rule-based** altamente ottimizzata:

Invece di moltiplicare le triple all'infinito, il sistema raggruppa le risorse equivalenti in **classi di equivalenza** a livello fisico (nei suoi indici interni). Elegge una singola risorsa come "rappresentante" formale del gruppo e memorizza in modo ultracompatto tutte le proprietà condivise legandole solo al rappresentante. Questa architettura spiega perché l'editor SPARQL (visto nella sezione precedente) dispone di un pulsante dedicato per espandere i risultati `owl:sameAs`: permette all'utente di scegliere se vedere la rappresentazione fisica compatta o l'espansione logica completa.

### Oltre RDF: Dati Tabellari, Ricerca Testuale e Geospaziale

Sebbene RDF sia il suo cuore, l'ecosistema di GraphDB è progettato per integrarsi con scenari di dati più ampi.

1. **OntoRefine:** Riconoscendo che la maggior parte dei dati aziendali o aperti non nasce in formato semantico, il Workbench include **OntoRefine** (accessibile sotto "Import -> Tabular"). È uno strumento potente derivato da OpenRefine, progettato specificamente per ingerire dati in formati tabellari tradizionali (TSV, CSV, Excel, ma anche JSON e XML). Offre un'interfaccia interattiva per pulire i dati grezzi, trasformarli strutturalmente e, infine, mapparli su un'ontologia per importarli nel database a grafo come triple RDF perfette.
    
2. **Ricerca Full-text e Geospaziale:** Il motore non si limita a interrogazioni strutturali SPARQL. Sfruttando indici ausiliari specializzati (come i connettori Lucene), GraphDB supporta in modo nativo e performante la **Full-text search** (per cercare parole chiave all'interno dei testi lunghi o delle etichette descrittive) e interrogazioni **GeoSPARQL** (per calcolare distanze o intersezioni spaziali tra entità geografiche). Anche per la ricerca full-text, il sistema è progettato per aggiornare gli indici in maniera incrementale, garantendo che le ricerche testuali riflettano in tempo reale gli ultimi aggiornamenti apportati al database.

---
# Appendice

#### I Fondamenti Matematici dell'RDF Rank

^e63eee

Il concetto alla base dell'RDF Rank trae forte ispirazione dall'algoritmo **PageRank**, originariamente sviluppato da Google per valutare l'autorevolezza delle pagine web e ordinarle nei risultati di ricerca. Entrambi gli algoritmi condividono la stessa filosofia di fondo: l'importanza di un nodo non è determinata solo dal suo contenuto isolato, ma dal numero e dalla qualità delle sue interconnessioni all'interno dell'intera rete.

In termini matematici, il PageRank valuta il **long-term visit rate** (tasso di visita a lungo termine). Immaginate un "navigatore casuale" (random surfer) che si muove ininterrottamente sul Web: partendo da una pagina qualsiasi, sceglie ciecamente uno dei link in uscita e vi clicca sopra, procedendo così all'infinito, con uguale probabilità di seguire ciascun link disponibile sulla pagina in cui si trova. Il PageRank di una specifica pagina rappresenta la probabilità matematica che il navigatore si trovi su quella precisa pagina in un dato istante futuro.

Questo comportamento aleatorio viene modellato formalmente attraverso una **catena di Markov a tempo discreto**. Tuttavia, affinché la matematica funzioni (ovvero, affinché il calcolo del tasso di visita a lungo termine converga verso valori definiti e stabili), la teoria dei processi stocastici richiede che la catena di Markov sia **ergodica**.

Un grafo reale (come il Web o un database RDF), però, è raramente ergodico. Presenta difetti strutturali:

1. **Dead end (Vicoli ciechi):** Nodi che ricevono collegamenti ma non ne hanno in uscita. Il navigatore rimarrebbe bloccato per sempre.
    
2. **Spider traps (Trappole):** Piccoli gruppi di nodi isolati che puntano solo tra di loro, intrappolando il navigatore in un ciclo infinito e assorbendo tutto il "Rank" della rete.
    

Per forzare l'ergodicità e far funzionare il modello, l'algoritmo introduce un correttivo matematico chiamato **teleporting** (teletrasporto):

- Se il navigatore finisce in un vicolo cieco, la regola cambia: invece di fermarsi, viene "teletrasportato" con probabilità uniforme su una risorsa qualsiasi dell'intero grafo, potendo così riprendere il viaggio.
    
- Per evitare le trappole, si stabilisce che ad ogni singolo passo, il navigatore ha una certa probabilità (il _teleportation rate_, spesso impostato tra il 10% e il 15%) di ignorare completamente i link presenti e saltare a caso su un altro nodo del grafo.
    

Applicando questo modello corretto al database RDF (dove le "pagine" sono le risorse e i "link" sono i predicati), GraphDB calcola il rango di ogni singola entità, assegnando punteggi più alti a quelle maggiormente referenziate. Questo dimostra un principio teorico fondamentale: i dati RDF non si limitano ad essere una rappresentazione per l'archiviazione, ma costituiscono un vero e proprio **grafo elaborabile**, a cui è possibile applicare la vasta gamma di algoritmi matematici originariamente sviluppati per la teoria dei grafi.
