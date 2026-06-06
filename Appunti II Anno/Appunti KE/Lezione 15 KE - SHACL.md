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
# Introduzione a SHACL: Validazione dei Dati RDF

Per garantire che i dati presenti in un database a grafo rispettino determinati standard di qualità, struttura e completezza, si utilizza il linguaggio **SHACL** (Shapes Constraint Language). Questo standard del W3C permette di definire regole precise per validare i grafi RDF.

## I Concetti Fondamentali

Il vocabolario di SHACL si basa su alcune entità logiche ben distinte che separano le regole dai dati effettivi:

- **Shape (Forma):** È il contenitore principale delle regole. Si tratta di una collezione logica che raggruppa due elementi essenziali: i "Target" (chi deve essere controllato) e i "Constraint components" (quali regole devono essere applicate).
    
- **Targets (Obiettivi):** Specificano in modo preciso quali nodi all'interno del grafo dei dati devono essere sottoposti a validazione e devono conformarsi a una determinata Shape.
    
- **Constraint components (Componenti di vincolo):** Determinano la natura della validazione. Definiscono le regole vere e proprie, come ad esempio la presenza obbligatoria di una proprietà, il tipo di dato (stringa, intero), o il numero minimo e massimo di valori consentiti.
    
- **Shapes graph:** È il grafo RDF che contiene esclusivamente le definizioni delle Shape (le regole).
    
- **Data graph:** È il grafo RDF che contiene le istanze e i dati concreti che devono essere analizzati e validati.
    
## Anatomia di una Validazione: Un Esempio Pratico

Per comprendere come queste entità interagiscono, immaginiamo di dover validare i profili di alcuni utenti. Si definisce una regola, ad esempio un `UserShape`, che impone determinati vincoli costruttivi.

Nello specifico, la regola può richiedere che ogni utente abbia obbligatoriamente un nome (`schema:name`), che questo nome sia esattamente uno (`sh:minCount 1` e `sh:maxCount 1`), e che sia formattato come una stringa testuale (`xsd:string`). Inoltre, la regola può richiedere un indirizzo email, specificando che debba essere un identificatore di risorsa (un IRI, tipicamente formattato con il prefisso `mailto:`).

Applicando questa Shape a un set di dati utente, si ottengono risultati diversi in base alla conformità strutturale:

- **Caso Valido:** Un utente (es. Alice) possiede la proprietà `schema:name` correttamente valorizzata e un'email formattata come risorsa IRI (`<mailto:alice@mail.org>`). Il nodo supera la validazione.
    
- **Casi Non Validi:** * Un utente (es. Bob) possiede un indirizzo email corretto, ma utilizza la proprietà `schema:firstName` invece della richiesta `schema:name`. Poiché il vincolo imponeva almeno una occorrenza di `schema:name`, la validazione fallisce.
    
    - Un altro utente (es. Carol) possiede il nome corretto, ma il suo indirizzo email è inserito come una semplice stringa di testo (`"carol@mail.org"`) anziché come un IRI valido. Anche in questo caso, il nodo viene scartato per non conformità al tipo di dato.

![center|500](img/Pasted%20image%2020260606115109.png)

## Le Dichiarazioni di Target (Come selezionare i nodi)

Il motore SHACL deve sapere da dove iniziare l'analisi. Le dichiarazioni di target sono il meccanismo di "aggancio" tra il grafo delle regole e il grafo dei dati. 

![center|400](img/Pasted%20image%2020260606115130.png)

Esistono diversi approcci per selezionare i nodi da validare:

1. **`targetNode`:** Punta in modo diretto ed esplicito a un nodo specifico tramite il suo identificatore univoco.
	1. ![center|500](img/Pasted%20image%2020260606115153.png)
2. **`targetClass`:** Seleziona in massa tutti i nodi che appartengono a una determinata classe.
	1. ![center|500](img/Pasted%20image%2020260606115210.png)
3. **`targetProperty`:** Seleziona tutti i nodi che agiscono come soggetto per una specifica proprietà, indipendentemente dalla loro classe di appartenenza.
4. **`target`:** Un meccanismo di selezione avanzato e generico, che permette di isolare i nodi bersaglio utilizzando la logica complessa delle interrogazioni SPARQL.

### Approfondimento sui meccanismi di Target

L'uso di questi meccanismi varia in base alle esigenze di scalabilità e architettura del modello:

- **Target Node (Selezione Diretta):** Dichiarando una proprietà come `sh:targetNode :alice, :bob, :carol`, si indicano esplicitamente al validatore i singoli URI da analizzare. È un approccio puntuale, utile per regole isolate, ma poco scalabile se il database contiene milioni di utenti, poiché richiederebbe un aggiornamento manuale della regola ad ogni nuovo inserimento.
    
- **Target Class (Selezione per Tipo):** Utilizzando l'istruzione `sh:targetClass :User`, il validatore si affida alle dichiarazioni ontologiche di base. Il motore va alla ricerca di tutti i nodi nel Data graph che possiedono una dichiarazione `rdf:type` corrispondente alla classe specificata (es. tutti i nodi che sono istanze di `:User`). Questo approccio è dinamico e universalmente scalabile.
    
- **Target Class Implicito (Scorciatoia Sintattica):** Per ottimizzare la scrittura del codice e unire l'ontologia alle regole di validazione, SHACL supporta una dichiarazione implicita. Se nel grafo delle regole un'entità viene definita contemporaneamente sia come classe dell'ontologia (`rdfs:Class`) sia come forma di validazione (`sh:NodeShape`), l'entità diventa lo _scope_ di se stessa.
	- In termini pratici, scrivendo `:User a sh:NodeShape, rdfs:Class ;`, si crea una forma che si applica automaticamente a tutte le istanze della classe `:User`. La dichiarazione `sh:targetClass` viene del tutto omessa dal codice perché dedotta implicitamente dall'intersezione dei due domini.
	- ![center|500](img/Pasted%20image%2020260606115225.png)

Entrando nel vivo del linguaggio SHACL, è fondamentale comprendere come è strutturata la sua logica di validazione e quali sono gli strumenti a disposizione per modellare le regole.
## La Tassonomia delle Forme (Types of Shapes)

Il fulcro di SHACL è il concetto generico di "Forma" (_Shape_), che funge da contenitore per le dichiarazioni di target (chi validare) e per i vincoli. Da questo concetto astratto derivano due tipologie principali e distinte di forme, progettate per operare su livelli diversi del grafo RDF:

1. **Node Shapes (Forme di Nodo):** Si concentrano esclusivamente sul nodo bersaglio stesso (definito _focus node_). I vincoli dichiarati all'interno di una Node Shape servono a verificare le caratteristiche intrinseche di quel preciso nodo, come ad esempio la sua natura (se è un IRI o un nodo vuoto).
	1. ![center|400](img/Pasted%20image%2020260606115656.png)
2. **Property Shapes (Forme di Proprietà):** Si concentrano sulle connessioni del nodo bersaglio. Definiscono vincoli che non si applicano al focus node in sé, ma ai valori raggiungibili seguendo uno specifico percorso (una specifica proprietà o catena di proprietà) a partire da esso.
	1. ![center|400](img/Pasted%20image%2020260606115714.png)

![center|500](img/Pasted%20image%2020260606115634.png)

A livello implementativo, una `PropertyShape` utilizza il costrutto `sh:path` per dichiarare quale proprietà deve essere percorsa e analizzata, per poi applicarvi i relativi componenti di vincolo.

### Percorsi Semplici e Complessi nelle Property Shapes

Il costrutto `sh:path` non è limitato alla singola indicazione di un predicato (es. "verifica l'email dell'utente"). Supporta la definizione di percorsi complessi che permettono di navigare il grafo in direzioni e modalità avanzate.


Un esempio molto potente è l'**Inverse Path** (`sh:inversePath`). Normalmente, una proprietà valida l'oggetto di una tripla in cui il focus node è il soggetto. Usando un percorso inverso, la prospettiva si ribalta: si istruisce il validatore a guardare "all'indietro", ovvero a cercare tutte le triple in cui il focus node funge da _oggetto_, e ad applicare i vincoli ai _soggetti_ di quelle triple.

![center|500](img/Pasted%20image%2020260606115830.png)

Ad esempio, se vogliamo verificare le caratteristiche di tutti gli account che _seguono_ un determinato utente, applicheremo un `inversePath` sulla proprietà `schema:follows`. Esistono anche altri operatori di percorso, come percorsi alternativi (`alternativePath`) o percorsi di lunghezza variabile (`zeroOrMorePath`, `oneOrMorePath`).

## Il Catalogo dei Componenti di Vincolo (Constraint Components)

SHACL offre una ricchissima libreria nativa di vincoli base (Core constraint components), suddivisibile in macro-categorie logiche:

- **Cardinalità:** Per imporre un numero minimo o massimo di occorrenze di una proprietà.
    
- **Tipi di valori:** Per restringere l'ontologia (classi), i tipi di dato (es. stringhe o interi) o la natura fisica del nodo (es. IRI).
    
- **Vincoli sui Valori:** Per forzare l'assunzione di un valore specifico o la selezione da una lista chiusa di opzioni (`in`).
    
- **Range e Stringhe:** Per imporre limiti matematici (maggiore/minore) o vincoli sintattici sulle stringhe di testo (lunghezza, espressioni regolari, restrizioni sulla lingua).
    
- **Logica e Forme Chiuse:** Operatori booleani (`not`, `and`, `or`) per combinare più regole, e la possibilità di dichiarare forme "chiuse" (che rifiutano qualsiasi proprietà non esplicitamente autorizzata dalla regola).
    
- **Confronto tra Proprietà:** Regole che mettono a confronto due proprietà diverse dello stesso nodo (es. la data di fine deve essere successiva alla data di inizio).

![center|500](img/Pasted%20image%2020260606115917.png)
### Analisi dei Vincoli Principali

Vediamo nel dettaglio il funzionamento dei vincoli più utilizzati nella pratica della modellazione semantica.

#### 1. Vincoli di Cardinalità (`minCount`, `maxCount`)

Definiscono i confini quantitativi. Il `sh:minCount` stabilisce il numero minimo di triple che devono collegare il focus node tramite un dato predicato (il suo valore di default è 0, il che rende la proprietà opzionale). Il `sh:maxCount` impone un tetto massimo (se omesso, non c'è limite).

_Se un utente deve avere un minimo di 2 follower e un massimo di 3, chi ne ha solo 1 viola il limite inferiore, chi ne ha 4 viola il limite superiore._

![center|500](Pasted%20image%2020260606115944.png)
#### 2. Restrizioni sul Tipo di Dato (`datatype`)

Assicura che i nodi valore (solitamente valori letterali) appartengano a un preciso tipo di dato XML Schema (XSD).

_Se la data di nascita (`schema:birthDate`) richiede il vincolo `sh:datatype xsd:date`, l'inserimento di una stringa formattata correttamente come `"1985-08-20"^^xsd:date` supererà il test, mentre l'inserimento del solo anno "1990" come numero intero semplice genererà un errore di validazione._

![center|500](img/Pasted%20image%2020260606120019.png)
#### 3. Restrizioni sulla Classe (`class`)

Questo vincolo verifica che i nodi bersaglio siano istanze di una specifica classe ontologica. Una caratteristica cruciale di questo vincolo in SHACL è la sua "intelligenza tassonomica": la validazione ha successo non solo se il nodo appartiene esattamente alla classe indicata, ma anche **se appartiene a una qualsiasi delle sue sottoclassi**.

_Se una regola impone che gli elementi seguiti da un utente debbano essere di classe `User`, la validazione accetterà senza problemi un nodo definito come `Manager`, purché l'ontologia di base abbia precedentemente dichiarato che `Manager` è una sottoclasse (`rdfs:subClassOf`) di `User`._

![center|500](img/Pasted%20image%2020260606120036.png)
#### 4. Restrizioni sulla Natura del Nodo (`nodeKind`)

In RDF, un nodo può fisicamente essere un IRI (un indirizzo web formale), un Nodo Vuoto (Blank Node, senza un identificatore universale) o un Valore Letterale (una stringa o un numero). Il vincolo `nodeKind` restringe le possibilità.

I valori impostabili sono molto granulari: `sh:IRI`, `sh:BlankNode`, `sh:Literal`, oppure combinazioni come `sh:BlankNodeOrIRI` (escludendo di fatto i valori letterali).

- Ad esempio, definendo che il nodo centrale di un utente debba essere `sh:IRI`, si impedirà la creazione di profili utente anonimi basati su Nodi Vuoti.
    
- Similmente, se la proprietà "nome" richiede un `sh:Literal`, sarà impossibile assegnarle come valore l'URI di un'altra risorsa; viceversa, se la proprietà "conosce" richiede `sh:BlankNodeOrIRI`, il sistema rigetterà qualsiasi tentativo di inserire una semplice stringa di testo al posto del collegamento a un'altra entità strutturata.

![center|500](img/Pasted%20image%2020260606120058.png)

#### 5. Vincoli sui Valori Specifici

A volte non basta definire il tipo di dato, ma è necessario imporre che un nodo assuma un valore esatto o che il suo valore appartenga a un insieme predefinito.

1. **Valore Esatto (`hasValue`):** Questo vincolo forza il focus node (o il nodo raggiunto tramite un path) ad avere esattamente il valore specificato nella regola.
    
    - _Esempio:_ Se la regola definisce che la proprietà `schema:affiliation` deve avere `sh:hasValue :OurCompany`, un utente (come `:alice`) affiliato a `:OurCompany` sarà considerato valido, mentre un utente (come `:bob`) affiliato ad `:AnotherCompany` verrà scartato.
        
2. **Elenchi Chiusi (`in`):** Fornisce una lista (un'enumerazione in sintassi RDF) di valori consentiti. Il nodo validato deve corrispondere a uno (e solo uno) degli elementi di questa lista.
    
    - _Esempio:_ Una regola per `schema:gender` potrebbe usare `sh:in (schema:Male schema:Female)`. L'utente `:alice` (Female) e `:bob` (Male) passeranno il controllo. L'utente `:carol`, avendo come genere `schema:Unknown` (non presente nella lista chiusa), non supererà la validazione.

![center|500](img/Pasted%20image%2020260606120403.png)
#### 6. Vincoli con Altre Forme e il Problema della Ricorsione

SHACL permette di creare regole modulari e nidificate utilizzando il costrutto **`sh:node`**. Questo vincolo stabilisce che tutti i valori raggiungibili tramite una certa proprietà devono, a loro volta, conformarsi a un'altra Shape predefinita.

- _Esempio:_ Una `NodeShape` per l'utente può dichiarare che la proprietà `schema:worksFor` deve puntare a un nodo che rispetta la forma `:Company` (la quale, a sua volta, esige che l'azienda abbia un nome in formato stringa). L'utente `:alice` che lavora per `:OurCompany` (che possiede regolarmente uno `schema:name "OurCompany"`) è valido. L'utente `:bob` che lavora per `:Another` fallirà la validazione, perché il nodo `:Another` possiede un nome formato da un numero intero (`23`), violando così la Shape `:Company`.

![center|500](img/Pasted%20image%2020260606120417.png)


**Il limite della Ricorsione:**

Questa capacità di concatenare le forme solleva un problema critico: cosa succede nei modelli di dati ciclici? Immaginiamo che la forma `:User` richieda che il datore di lavoro rispetti la forma `:Company`, e che la forma `:Company` richieda che i suoi dipendenti rispettino la forma `:User`. Questo creerebbe un loop infinito di validazione.

Per evitare il collasso del motore, **le specifiche attuali di SHACL vietano severamente la ricorsione**. Non è consentito definire un ciclo in cui una forma, tramite i suoi vincoli, finisce per richiamare se stessa.

![center|500](img/Pasted%20image%2020260606120441.png)

**La Soluzione SHACL per evitare la ricorsione:**

Per modellare relazioni bidirezionali senza incappare nel divieto di ricorsione, SHACL impone un approccio basato sulle classi ontologiche. Invece di usare `sh:node` per richiamare un'altra Shape, si utilizza il vincolo **`sh:class`** combinato con dichiarazioni `rdf:type` (dette "archi di tipo") esplicite nei dati.

- _L'approccio corretto:_ La regola `:User` stabilisce che la proprietà `schema:worksFor` deve puntare a un nodo di classe `:Company` (`sh:class :Company`). Specularmente, la regola `:Company` stabilisce che `schema:employee` deve puntare a un nodo di classe `:User` (`sh:class :User`). In questo modo, la validazione si appoggia alla tassonomia del grafo senza creare loop logici tra le regole di validazione stesse.

![center|500](img/Pasted%20image%2020260606120504.png)
### Operatori Logici in SHACL

Per creare condizioni di validazione sofisticate, SHACL mette a disposizione gli operatori booleani standard, permettendo di combinare intere Shape:

![center|400](img/Pasted%20image%2020260606120527.png)

1. **Congiunzione (`sh:and`):** Richiede che il nodo soddisfi _tutte_ le forme elencate in una data lista.
	- _Nota sul comportamento predefinito:_ In realtà, SHACL applica una congiunzione implicita di base. Se all'interno di una singola Shape si elencano più `sh:property`, il sistema esige che vengano rispettate tutte, esattamente come se fossero state racchiuse in un blocco `sh:and`. L'operatore esplicito diventa utile quando si vogliono combinare Node Shapes esterne e riutilizzabili.
	- ![center|400](img/Pasted%20image%2020260606120632.png)
2. **Disgiunzione (`sh:or`):** Richiede che il nodo soddisfi _almeno una_ delle forme presenti nella lista. È ideale per gestire schemi flessibili
    - _Esempio:_ Una regola può richiedere che il nome sia espresso tramite la proprietà `foaf:name` OPPURE tramite `schema:name`. Un nodo con `foaf:name` (es. `:bob`) è valido, uno con `schema:name` (es. `:alice`) è parimenti valido. Un nodo che usa un'altra proprietà (es. `:carol` con `rdfs:label`) verrà rigettato.
    - ![center|400](img/Pasted%20image%2020260606120655.png)
3. **Negazione (`sh:not`):** Inverte la logica. Il nodo supera il controllo solo se _NON_ soddisfa la forma specificata.
    - _Esempio:_ Se si crea una regola `:NotFoaf` che impone `sh:not` sulla presenza obbligatoria di `foaf:name`, i nodi che usano `schema:name` (come `:alice`) o `rdfs:label` (come `:carol`) saranno considerati validi, mentre il nodo `:bob`, che possiede esattamente la proprietà vietata `foaf:name`, fallirà la validazione.
    - ![center|400](img/Pasted%20image%2020260606120717.png)

Proseguendo l'esplorazione del linguaggio SHACL, ci addentriamo in categorie di vincoli ancora più granulari, che permettono di validare non solo la presenza o il tipo di un dato, ma anche il suo contenuto semantico, la sua formattazione e la sua relazione con altre proprietà all'interno dello stesso nodo.
### Vincoli sui Range Numerici (Value Ranges)

Quando si lavora con dati quantitativi (come date, interi o decimali), è spesso necessario imporre dei limiti matematici. SHACL fornisce quattro costrutti specifici per definire i confini di un intervallo accettabile:

- **`minInclusive`** e **`maxInclusive`**: Stabiliscono rispettivamente il limite inferiore e superiore, includendo il valore specificato nel range accettato (equivalente a $\ge$ e $\le$).
    
- **`minExclusive`** e **`maxExclusive`**: Stabiliscono i limiti escludendo il valore specificato (equivalente a $>$ e $<$).

_Esempio applicativo:_ Immaginiamo di dover validare un sistema di recensioni in cui il punteggio (`schema:ratingValue`) deve essere un numero intero compreso strettamente tra 1 e 5. Utilizzando `sh:minInclusive 1` e `sh:maxInclusive 5`, un punteggio di 3 (Average) o 5 (Very Good) supererà il controllo. Al contrario, l'inserimento di uno 0 (Zero) farà fallire la validazione, trovandosi al di fuori del range matematico consentito.

![center|500](img/Pasted%20image%2020260606121408.png)

### Vincoli basati sulle Stringhe (String Based Constraints)

![center|400](img/Pasted%20image%2020260606121429.png)

Molti dati nel Web Semantico sono rappresentati come stringhe di testo. SHACL offre un set di strumenti per analizzare la forma e la struttura di queste stringhe:

**1. Lunghezza della stringa (`minLength`, `maxLength`)**

Questi vincoli contano il numero di caratteri che compongono il valore. Se impostiamo, ad esempio, che il nome di un utente debba avere un `sh:minLength 4` e un `sh:maxLength 10`, il sistema accetterà "Alice" (5 caratteri) ma rifiuterà "Bob" (3 caratteri).

_Nota tecnica fondamentale:_ Questa validazione valuta la _rappresentazione testuale_ del nodo e non può essere applicata ai Nodi Vuoti (Blank Nodes). Se si tenta di far passare un nodo anonimo (es. `_:strange`) attraverso questo controllo, la validazione fallirà a prescindere dalla lunghezza del suo identificatore interno.

![center|400](img/Pasted%20image%2020260606121636.png)

**2. Espressioni Regolari (`pattern`)**

Per formattazioni complesse (come codici fiscali, targhe o ID prodotto), si utilizza `sh:pattern`, che verifica se la stringa corrisponde a una specifica espressione regolare (Regex). Può essere affiancato dal costrutto `sh:flags` per aggiungere modificatori, come ad esempio `"i"` per rendere il controllo _case-insensitive_ (insensibile alle maiuscole/minuscole).

_Esempio:_ Un codice prodotto deve iniziare per "P" seguita da 3 o 4 cifre. La regex `^P\\d{3,4}$` combinata con il flag `"i"` accetterà "P2345" ma anche "p567", mentre rifiuterà "P12" (troppe poche cifre) o "B123" (lettera iniziale errata).

![center|400](img/Pasted%20image%2020260606121654.png)


**3. Unicità della Lingua (`uniqueLang`)**

Nel Web Semantico, una singola proprietà può avere valori multipli tradotti in varie lingue, identificati dai language tag (es. `@it`, `@en`). Impostando `sh:uniqueLang true`, si impone che non ci possano essere due valori con lo stesso identico tag linguistico.

_Esempio:_ Definendo il nome di una nazione, è corretto avere "Spain"@en ed "España"@es. Ma se per errore i dati contenessero "USA"@en e "United States"@en, il sistema segnalerebbe un'infrazione, poiché la lingua inglese è stata utilizzata due volte per la stessa proprietà.

_(Esiste anche il vincolo `stem`, che permette di verificare semplicemente se tutti gli IRI analizzati iniziano con un prefisso testuale fisso)._

![center|400](img/Pasted%20image%2020260606121740.png)


## Confronto tra Coppie di Proprietà (Property Pair Constraints)

Un aspetto molto potente di SHACL è la capacità di eseguire validazioni "incrociate" tra due proprietà diverse che appartengono allo _stesso_ nodo, per garantire la coerenza interna dei dati.

I vincoli principali sono:

- **`equals`**: I valori della prima proprietà devono essere identici a quelli della seconda.
    
- **`disjoint`**: I valori delle due proprietà devono essere completamente diversi (nessuna sovrapposizione).
    
- **`lessThan` / `lessThanOrEquals`**: Utilizzati per l'ordinamento (es. la `dataDiNascita` deve essere minore della `dataDiMorte`).

_Esempio complesso:_ Immaginiamo una regola che richiede due condizioni contemporanee: il nome specificato in `schema:givenName` deve essere identico a quello in `foaf:firstName` (`sh:equals`) e, allo stesso tempo, deve essere diverso dal cognome `schema:lastName` (`sh:disjoint`).

- Il profilo di Alice (givenName "Alice", firstName "Alice", lastName "Cooper") è perfettamente valido.
    
- Il profilo di Bob (givenName "Bob", firstName "Robert") fallisce perché i due nomi propri non coincidono, violando l'uguaglianza.
    
- Il profilo di Carol (givenName "Carol", lastName "Carol") fallisce perché nome e cognome sono identici, violando la regola di disgiunzione.

![center|500](img/Pasted%20image%2020260606121811.png)

## Forme Chiuse (Closed Shapes)

L'architettura nativa di RDF si basa sull'"assunzione di mondo aperto" (_Open World Assumption_): se non è vietato esplicitamente, è permesso. Questo significa che, di base, a un nodo valido possono essere liberamente aggiunte decine di altre proprietà sconosciute senza che il validatore si lamenti.

A volte, però, si necessita di un controllo ferreo (modello a "mondo chiuso"). Aggiungendo l'istruzione **`sh:closed true`** alla definizione di una Shape, si impone che il nodo possa contenere _esclusivamente_ le proprietà elencate in modo esplicito nella regola. Qualsiasi proprietà aggiuntiva comporterà un errore di validazione.

Poiché alcune proprietà di sistema sono onnipresenti e necessarie (come `rdf:type` per definire la classe), SHACL mette a disposizione **`sh:ignoredProperties`**: una "lista bianca" di proprietà che il validatore deve ignorare, permettendone l'uso anche all'interno di una forma chiusa.

_Esempio:_ In una forma chiusa che autorizza solo nome e cognome e ignora la classe, un utente che possiede nome, cognome e `rdf:type` sarà valido. Un utente a cui è stata aggiunta anche la proprietà `rdfs:label` (non prevista dalla Shape) verrà immediatamente segnalato come non valido.

![center|500](img/Pasted%20image%2020260606122032.png)

## Vincoli Non Validanti e Interfacce Utente (Non-validating Constraints)

L'ultimo aspetto fondamentale di SHACL è che non serve solo a "punire" i dati errati, ma agisce anche come potente strumento di progettazione. SHACL include dei vincoli cosiddetti "non validanti", che non generano errori, ma servono ad arricchire la regola con metadati utili ai software esterni (ad esempio, per generare automaticamente i moduli di inserimento dati in un'interfaccia grafica).

![center|500](img/Pasted%20image%2020260606122111.png)

Tra questi troviamo:

- **`name`** e **`description`**: Forniscono etichette leggibili da un essere umano e testi di aiuto per spiegare cosa inserire in un determinato campo.
    
- **`order`**: Un numero intero che definisce in quale sequenza le proprietà dovrebbero apparire sullo schermo (es. il nome prima del cognome).
    
- **`group`**: Permette di raggruppare visivamente più proprietà correlate sotto un unico contenitore logico (definito come `sh:PropertyGroup`).
    

_Esempio UI:_ Sfruttando questi metadati, un programmatore può istruire GraphDB (o un'applicazione esterna) a leggere la Shape e costruire dinamicamente un modulo di registrazione a blocchi. Potrà creare una sezione chiamata "User details" (con i campi URL e Nome raggruppati) posizionata in alto (`order 0`), seguita da una seconda sezione chiamata "Location" (contenente Indirizzo e Nazione) posizionata in basso (`order 1`), rendendo la struttura dei dati non solo corretta dal punto di vista semantico, ma anche fruibile per l'utente finale.

![center|500](img/Pasted%20image%2020260606122132.png)

Proseguendo nell'analisi delle capacità avanzate di SHACL, superiamo i vincoli base per addentrarci in scenari di modellazione molto più complessi. Spesso le ontologie del mondo reale richiedono regole che non si limitano a contare le proprietà o a verificarne il tipo, ma che devono ispezionare sezioni intere del grafo o imporre restrizioni altamente specifiche.

## Forme Qualificate (Qualified Value Shapes)

I vincoli di cardinalità classici (`minCount`, `maxCount`) si applicano all'intero set di valori di una data proprietà. Tuttavia, a volte è necessario imporre limiti solo su un **sottoinsieme specifico** di quei valori.

Per risolvere questo problema, SHACL introduce i vincoli qualificati:

- **`qualifiedValueShape`**: Definisce la "condizione" (una Shape) che il sottoinsieme di valori deve soddisfare per essere conteggiato.
    
- **`qualifiedMinCount`** e **`qualifiedMaxCount`**: Stabiliscono il numero minimo e massimo di valori che devono soddisfare la forma specificata.

![center|400](img/Pasted%20image%2020260606123611.png)

_Esempio pratico:_ Supponiamo di voler modellare la classe "Famiglia Tradizionale Americana" (come stereotipo per un database). Non ci basta dire che la proprietà `ex:child` deve avere al massimo 3 valori. Vogliamo specificare che la famiglia deve avere _esattamente un figlio maschio_ e _esattamente una figlia femmina_.

Si utilizzeranno due blocchi di regole separate sulla proprietà `ex:child`. Il primo blocco imposterà una `qualifiedValueShape` che richiede il genere "Maschio", associata a un `qualifiedMinCount` e `maxCount` pari a 1. Il secondo blocco farà lo stesso per il genere "Femmina". In questo modo, SHACL valuterà i figli raggruppandoli per genere prima di contarli.

![center|400](img/Pasted%20image%2020260606123703.png)

### Percorsi di Proprietà Complessi (Property Paths)

Come accennato in precedenza, il costrutto `sh:path` non è limitato a un singolo predicato. SHACL adotta la stessa sintassi potente dei **Property Paths di SPARQL 1.1**, permettendo di validare nodi che si trovano a "più salti" di distanza dal nodo di partenza.

Oltre al percorso inverso (già visto), i percorsi più utili includono:

1. **Percorsi Alternativi (`alternativePath`):** Utile quando la semantica permette di raggiungere un dato tramite predicati diversi. Si definisce fornendo una lista RDF. Ad esempio, per cercare i genitori di una persona, il path può essere definito come alternativa tra `ex:father` e `ex:mother`.
    
2. **Percorsi Sequenziali (Sequence Paths):** Permettono di "concatenare" le proprietà. Se voglio validare non l'entità genitore, ma il _nome di battesimo_ del genitore, il percorso sarà una sequenza definita come `( ex:parent ex:firstName )`. Il motore SHACL seguirà prima l'arco "parent" e poi l'arco "firstName", applicando il vincolo sul nodo testuale finale.
    
3. **Percorsi Transitivi (Zero or More / One or More):** Permettono di navigare gerarchie di profondità sconosciuta (es. `sh:zeroOrMorePath`). Sono fondamentali per validare catene, come ad esempio verificare che tutti gli "antenati" (`ex:ancestor`) di un individuo, risalendo l'albero genealogico all'infinito, appartengano alla classe `ex:Person`.

![center|400](img/Pasted%20image%2020260606123752.png)

![center|400](img/Pasted%20image%2020260606123820.png)

## La Massima Flessibilità: Vincoli basati su SPARQL

Quando i componenti nativi di SHACL (cardinalità, tipi, espressioni regolari, ecc.) non sono sufficienti per esprimere una logica di business particolarmente intricata, il linguaggio offre una "via di fuga" assoluta: **`sh:sparql`**.

Questo costrutto permette di incorporare un'intera query SPARQL all'interno della regola di validazione.

![center|500](img/Pasted%20image%2020260606123844.png)

La logica di funzionamento è basata sulla ricerca di violazioni: la query deve essere scritta come una `SELECT` strutturata in modo tale da restituire dei risultati _solo se_ la regola viene infranta. Se la query non restituisce nulla, il nodo è considerato valido.

Per far dialogare la query con il motore di validazione, SHACL inietta dinamicamente delle variabili speciali nel codice SPARQL durante l'esecuzione:

- **`$this`**: È la variabile più importante. Rappresenta il _focus node_ attualmente sotto esame. La query SPARQL utilizzerà `$this` come punto di partenza per navigare il grafo e cercare incongruenze.
    
- **`$shapesGraph`**: Fa riferimento al grafo che contiene le regole.
    
- **`$currentShape`**: Rappresenta la forma specifica che ha innescato l'esecuzione della query.

![center|400](img/Pasted%20image%2020260606123902.png)

![center|400](img/Pasted%20image%2020260606123950.png)

Inoltre, SHACL aggiunge un meccanismo di estensione di SPARWL, in questo modo

![center|500](img/Pasted%20image%2020260606124027.png)
