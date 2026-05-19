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
# Informazione linguistica in ontologie/dataset

Abbandoniamo per un momento la struttura logica dei dati e affrontiamo un problema altrettanto cruciale: **come facciamo dialogare le ontologie formali con il linguaggio umano?** Per quanto un'ontologia sia matematicamente perfetta, se le macchine e gli esseri umani non riescono a comunicare sui significati, il modello perde gran parte della sua utilità. È qui che entra in gioco l'inserimento dell'informazione linguistica nei dataset semantici, un percorso che parte da strumenti molto semplici per arrivare a modelli complessi come **OntoLex-Lemon** (Lexicon Model for Ontologies).
## Il livello base: Etichette e Descrizioni

Inizialmente, il modo più immediato per "spiegare" un concetto a un essere umano è attaccargli delle etichette testuali. I linguaggi del Web Semantico forniscono nativamente delle proprietà per gestire questa documentazione di base:

- **Le Etichette (Labels):** Servono a dare un nome leggibile a una risorsa (es. tramite `rdfs:label`) o a gestirne sinonimi e varianti (tramite il vocabolario SKOS con `skos:prefLabel`, `skos:altLabel`, ecc.).
    
- **I Commenti e le Definizioni:** Forniscono una descrizione estesa e testuale del significato del concetto (es. tramite `rdfs:comment`, `dcterms:description` o `skos:definition`).
    
- **L'informazione implicita:** Spesso, il linguaggio naturale si nasconde persino negli identificatori (URI) stessi. Se una risorsa ha come parte finale dell'URI `.../generalCouncil`, è possibile applicare regole di trasformazione per estrarre implicitamente le parole "general" e "council".
    
## Cosa possiamo fare con le informazioni linguistiche di base?

Anche solo con queste semplici stringhe di testo, è possibile realizzare applicazioni estremamente utili:

- **Localizzazione delle Interfacce Utente (UI):** Se un'ontologia contiene etichette multilingue (es. "Sciences"@en e "Scienze"@it), è possibile costruire software e interfacce web che cambiano lingua dinamicamente. L'albero di navigazione di un sito si popolerà automaticamente con i termini corretti in base alle preferenze dell'utente, attingendo direttamente dai dati senza bisogno di file di traduzione separati.
	- ![center|500](img/Pasted%20image%2020260519144933.png)
- **Generazione Automatica di Documentazione:** Esistono strumenti in grado di scansionare il codice RDF di un'ontologia, estrarre le gerarchie, le classi, le definizioni (`skos:definition`) e i commenti, e impaginarli automaticamente in pagine web leggibili (simili a dei glossari o manuali tecnici). Questo azzera lo sforzo di dover scrivere la documentazione a mano.
	- ![center|500](img/Pasted%20image%2020260519144949.png)
- **Ontology Matching (Allineamento di Ontologie):** Quando si devono integrare due database o vocabolari diversi (magari uno in inglese e uno in italiano), la struttura logica da sola non basta. Gli algoritmi utilizzano il linguaggio naturale come "terreno comune" per confrontare i concetti. Analizzando e traducendo le etichette e le definizioni (spesso con l'aiuto di dizionari esterni o risorse di supporto), il sistema può dedurre che il nodo A del primo sistema corrisponde al nodo B del secondo.
	- ![center|500](img/Pasted%20image%2020260519145006.png)

## Il muro invalicabile: L'Elaborazione del Linguaggio Naturale (NLP)

Fin qui abbiamo usato il testo solo per "mostrarlo" a un utente o per fare semplici confronti di stringhe. I problemi nascono quando vogliamo usare le ontologie per compiti di **Elaborazione del Linguaggio Naturale (NLP)** avanzati:

- **Interpretazione del Testo:** Leggere una frase scritta da un umano (es. un articolo di giornale o una cartella clinica) e mappare automaticamente i concetti espressi nel testo con i nodi esatti dell'ontologia, normalizzando i vari modi in cui un concetto può essere espresso.
    
- **Verbalizzazione (Natural Language Generation):** Fare il processo inverso. Prendere un set di triple RDF (Dato A è collegato a Dato B tramite Proprietà C) e far generare alla macchina un discorso coerente, grammaticalmente corretto e fluido in linguaggio umano.
    

**Il limite strutturale:** Le semplici etichette viste prima (`rdfs:label` o `skos:prefLabel`) sono **completamente insufficienti** per svolgere queste attività. Un'etichetta è solo una stringa "muta". Non dice alla macchina se quella parola è un sostantivo maschile o femminile, se è plurale o singolare, come si coniuga se è un verbo, o come si comporta sintatticamente all'interno di una frase complessa.

L'obiettivo ultimo di tutta questa infrastruttura semantica e linguistica è tanto ambizioso quanto affascinante: permettere a un essere umano di dialogare con una macchina usando il linguaggio naturale, nascondendo completamente la complessità dei dati sottostanti.
# Question Answering su Ontologie 

Questo campo di applicazione prende il nome di **Question Answering su Ontologie**. Invece di costringere un utente a studiare la struttura di un database e a imparare la complessa sintassi di SPARQL, gli si permette di fare una domanda diretta, con le proprie parole. Sarà il sistema a farsi carico di tradurre questa richiesta umana in una query formale.

Ma come avviene questa "magia"? Esaminiamo le sfide e le soluzioni che i sistemi devono affrontare per comprendere una semplice domanda.

## L'Anatomia di una Domanda: Il caso "Moby Dick"

Prendiamo una domanda apparentemente banale: _"Chi ha scritto Moby Dick?"_. Per un essere umano la risposta è immediata, ma per un sistema semantico (che ad esempio interroga DBpedia) questa frase innesca una serie di deduzioni logiche e linguistiche molto sofisticate:

1. **Analisi Sintattica (Parsing):** Il sistema scompone la frase. Riconosce che "ha scritto" è il verbo principale (transitivo), che "Chi" è il soggetto grammaticale e che "Moby Dick" è l'oggetto diretto.
    
2. **Mappatura Semantica:** Il sistema deve ora tradurre le parole in URI. "Moby Dick" viene associato alla risorsa identificativa del romanzo. Il verbo "scrivere" viene mappato sulla proprietà ontologica corrispondente (ad esempio, `dbo:author`).
    
3. **Allineamento degli Argomenti:** Qui entra in gioco la sintassi complessa. Il sistema sa che la proprietà `author` collega un'opera al suo creatore. Deve quindi allineare gli argomenti grammaticali con quelli semantici: l'oggetto grammaticale ("Moby Dick") corrisponde al _Soggetto RDF_ della tripla, mentre il pronome "Chi" corrisponde all'_Oggetto RDF_ (il valore che stiamo cercando con la nostra variabile SPARQL `?x`).
    
4. **Disambiguazione e Inferenza:** "Moby Dick" è una parola ambigua: potrebbe riferirsi al famoso romanzo, ma anche all'omonimo film del 1956. Come fa la macchina a non confondersi? Usa i vincoli logici dell'ontologia. Sapendo che il verbo "scrivere" (nella sua accezione autoriale) ha senso solo se applicato a un "Lavoro Scritto" (una `WrittenWork`), il sistema esclude automaticamente il film. Inoltre, il pronome interrogativo "Chi" (rispetto a "Cosa") suggerisce implicitamente che la risposta attesa, ovvero il codominio (range) della proprietà, debba appartenere alla classe "Persona".
    

Da questo semplice esempio emerge chiaramente che per interpretare una frase non basta un dizionario di sinonimi: serve una comprensione profonda di come le parole si comportano nella grammatica e di come queste si aggancino alla logica dell'ontologia.

![center|500](img/Pasted%20image%2020260519145404.png)
## I Due Livelli della Conoscenza Linguistica

Per dotare i sistemi di questa intelligenza, la conoscenza linguistica viene divisa in due grandi blocchi:

- **Conoscenza Indipendente dal Dominio:** Riguarda le regole fisse del linguaggio umano (la struttura delle frasi, la differenza tra nomi e verbi, come si formula una negazione, l'uso dei tempi verbali). Questa parte viene modellata una volta per tutte usando grammatiche generali e analizzatori sintattici (parser). Non cambia se stiamo parlando di medicina o di letteratura.
    
- **Conoscenza Specifica di Dominio (Le "Content Words"):** Riguarda le parole che evocano concetti precisi all'interno di un settore. Come si esprime il concetto di "Autore"? Quali verbi si usano? Quali sostantivi? Questa conoscenza cambia da ontologia a ontologia e richiede la creazione di un **Lessico Ontologico**.

### Il Lessico Ontologico: Un dizionario "esterno"

Un Lessico Ontologico è un modello che specifica esattamente in che modo le classi, le proprietà e gli individui di una specifica ontologia prendono vita nel linguaggio naturale.

Il principio fondamentale di un lessico ontologico moderno è che deve essere **definito esternamente** all'ontologia di riferimento. L'ontologia rimane il regno della logica pura, indipendente dalla lingua. Il lessico funge da "ponte" o "interfaccia" esterna. Questo design è potentissimo: permette di prendere una singola ontologia medica, ad esempio, e di affiancarle un lessico ontologico in italiano, uno in inglese e uno in giapponese, mantenendo il modello dati centrale pulito e inalterato.

### Lo Standard Definitivo: OntoLex-Lemon

Per standardizzare la creazione di questi lessici ontologici, il W3C ha prodotto il modello **OntoLex-Lemon**. Nato dall'unione delle migliori menti e dei precedenti modelli di ricerca (come il progetto Monnet), OntoLex-Lemon è diventato lo standard di fatto per collegare il Web Semantico al linguaggio umano.

Per gestire l'enorme complessità della lingua, il modello non è un blocco monolitico, ma è suddiviso in moduli altamente specializzati:

- **Core (`ontolex`):** È l'ossatura del sistema. Definisce le entrate lessicali di base (le parole) e stabilisce come queste puntino ai concetti astratti dell'ontologia.
    
- **Syntax and Semantics (`synsem`):** È il modulo più cruciale per applicazioni come il Question Answering. Descrive il comportamento sintattico di una parola (es. un verbo transitivo) e mappa esplicitamente gli argomenti grammaticali (soggetto, oggetto) sugli argomenti semantici (Soggetto e Oggetto di una tripla RDF), permettendo alla macchina di generare query corrette.
    
- **Decomposition (`decomp`):** Molte parole non sono semplici, ma composte. Questo modulo permette di scomporre espressioni complesse o parole composte (es. parole polirematiche come "macchina da presa" o termini medici complessi) nei loro elementi costitutivi.
    
- **Variation and Translation (`vartrans`):** Gestisce la rete delle relazioni prettamente linguistiche. Serve a codificare traduzioni tra lingue diverse, variazioni morfologiche e relazioni di sinonimia tra i vari sensi delle parole.
    
- **Linguistic Metadata (`lime`):** Fornisce gli strumenti per descrivere il lessico stesso (chi lo ha creato, per quale lingua è pensato, quante parole copre rispetto all'ontologia totale), facilitando la condivisione e la scoperta di queste risorse sul web.

Entriamo nel cuore della questione. Per capire veramente la potenza del modulo principale (il **Core**) di **OntoLex-Lemon**, il modo migliore è costruirlo mentalmente passo dopo passo, partendo dai metodi più ingenui fino ad arrivare all'architettura formale completa.

L'obiettivo è insegnare alla macchina non solo che una parola è associata a un concetto, ma _come_ quella parola si comporta grammaticalmente.
#### Il problema di partenza: Il caos delle etichette piatte

Immaginiamo di voler mappare il concetto ontologico di "Autore" (es. la proprietà `dbo:author` in DBpedia) con il verbo inglese "to write" (scrivere).

L'approccio più basilare, tipico dei primi vocabolari semantici, consisteva nell'usare una semplice proprietà come `rdfs:label` per collegare direttamente l'entità ontologica alla stringa di testo `"write"@en`.

Tuttavia, il linguaggio naturale è flessibile: un testo potrebbe non usare l'infinito "write", ma il passato "wrote" o il participio "written". Se ci limitiamo ad attaccare tutte queste varianti testuali direttamente al concetto ontologico usando sempre `rdfs:label`, creiamo un vicolo cieco. La macchina vedrà solo un mucchio di stringhe scollegate; non saprà mai che "wrote" è il tempo passato di "write". Per lei, avranno lo stesso esatto peso logico.

![center|500](img/Pasted%20image%2020260519145906.png)
#### L'ingresso della "Lexical Entry"

Per mettere ordine, dobbiamo smettere di collegare direttamente le stringhe di testo grezze all'ontologia. Dobbiamo introdurre un'entità intermedia, un vero e proprio "lemma" da dizionario: la **Lexical Entry** (Entrata Lessicale).

Invece di lavorare con le stringhe, creiamo un nodo specifico (es. `ex:write-v`) che rappresenta il verbo "scrivere" in quanto unità astratta del linguaggio. Questo nodo fa da ponte: da un lato indica (o _denota_) l'entità ontologica `dbo:author`, dichiarando così il suo significato logico. Dall'altro lato, deve gestire le forme fisiche in cui la parola si presenta.

![center|500](img/Pasted%20image%2020260519145919.png)
#### Dalla stringa alla "Forma"

Come colleghiamo ora le parole fisiche ("write", "wrote") alla nostra Lexical Entry? Non possiamo ancora usare semplici stringhe di testo, perché vogliamo associare a ciascuna parola le sue proprietà grammaticali.

OntoLex introduce la classe **Form** (Forma). La Lexical Entry non possiede direttamente il testo, ma possiede delle Forme:

- **Canonical Form (Forma Canonica):** È la forma base che si troverebbe in un dizionario (per i verbi è l'infinito, per i nomi il singolare). Il nostro nodo `ex:write-v` avrà una forma canonica che punterà finalmente alla rappresentazione scritta `"write"@en`.
    
- **Other Form (Altre Forme):** Sono le declinazioni o le coniugazioni. Creeremo altre forme per il passato e il participio, collegandole alle rispettive rappresentazioni scritte (`"wrote"@en`, `"written"@en`).
    

Il vantaggio enorme di questo passaggio è che ora possiamo aggiungere metadati specifici a ogni singola forma. Ad esempio, possiamo dire che la forma "wrote" ha il tratto grammaticale del tempo passato, o possiamo associare alla forma "write" la sua esatta pronuncia fonetica tramite l'alfabeto IPA (es. `"raɪt"@en-US-fonipa`), cosa impossibile da fare se avessimo usato solo stringhe grezze.

![center|500](img/Pasted%20image%2020260519145935.png)
#### La Reificazione del Significato: Il "Lexical Sense"

Arrivati a questo punto, l'architettura sembra solida: abbiamo le Forme che descrivono l'ortografia, raggruppate in una Lexical Entry, la quale punta all'Ontologia. Ma c'è un'ultima, cruciale limitazione linguistica da superare: **la polisemia e l'ambiguità**.

Il verbo "scrivere" non significa _sempre e solo_ essere l'autore di un'opera letteraria (`dbo:author`). Può significare scrivere dati su un disco rigido, o tracciare fisicamente dei segni su un foglio di carta. Il collegamento diretto tra Lexical Entry e Ontologia è troppo rigido.

Per risolvere questo problema, OntoLex compie un'operazione di **reificazione**: trasforma il concetto stesso di "significato" in un oggetto a sé stante, chiamato **Lexical Sense** (Senso Lessicale).

- L'Entrata Lessicale non denota più direttamente l'entità ontologica, ma possiede uno o più "Sensi".
    
- È il singolo _Senso_ a puntare (tramite la proprietà di `reference`) all'entità logica nell'ontologia.
    

Perché questo è il pezzo forte del modello? Perché ora possiamo attaccare delle regole direttamente al _significato_. Possiamo dire alla macchina: _"Il verbo 'write' possiede il Senso X. Questo Senso X fa riferimento alla proprietà ontologica `dbo:author`, ma **solo a condizione che** (Usage) il soggetto dell'azione sia un'opera scritta"_.

Due entrate lessicali diverse che puntano alla stessa identica entità ontologica avranno due risorse "Senso" distinte, permettendo sfumature di significato indipendenti.

![center|500](img/Pasted%20image%2020260519145950.png)

![center|500](img/Pasted%20image%2020260519150007.png)
#### Sintesi del Modello Architetturale Completo

L'architettura finale del modulo Core di OntoLex-Lemon si delinea quindi come un ecosistema elegante e stratificato:

1. **Lexical Entry (Il Lemma):** Il centro del modello. Può essere una singola parola (_Word_), un'espressione composta (_Multiword Expression_) o un affisso (_Affix_).
    
2. **Form (La Morfologia):** Si dirama dalla Lexical Entry. Raccoglie le forme canoniche e le varianti.
    
3. **Representation (Il Testo e il Suono):** Si dirama dalle Forme. Contiene le stringhe fisiche (`writtenRep`) o fonetiche (`phoneticRep`).
    
4. **Lexical Sense (L'Anello di Congiunzione Logico):** Si dirama dalla Lexical Entry. Rappresenta una specifica accezione della parola in un contesto preciso.
    
5. **Ontology Entity (La Logica Pura):** L'entità formale (Classe, Proprietà, Individuo) referenziata dal Senso Lessicale.
    
6. **Lexical Concept (L'Anello di Congiunzione Concettuale):** Il modello prevede anche un ponte verso i vocabolari "leggeri" tipo SKOS. Un'entrata lessicale può "evocare" un concetto astratto (Lexical Concept) che fa parte di un _Concept Set_ più ampio (come una tassonomia o un tesauro gerarchico), garantendo l'interoperabilità sia con logiche stringenti (OWL) che flessibili (SKOS).

![center|500](img/Pasted%20image%2020260519150057.png)

## La Delega Linguistica: LexInfo e compagni

OntoLex-Lemon è un modello strutturale, ma è volutamente **agnostico** rispetto alle teorie linguistiche. Non possiede un vocabolario interno per definire cos'è un verbo, un sostantivo, un caso genitivo o un tempo passato. Se lo facesse, costringerebbe tutti ad adottare una singola visione della grammatica, che potrebbe non andare bene per lingue molto diverse tra loro.

La soluzione è la **delega**. OntoLex si affida a ontologie linguistiche esterne, create appositamente dai linguisti, come **LexInfo**, **OLiA** o **GOLD**.

Quando creiamo la nostra Lexical Entry per la parola "write", usiamo una proprietà per collegarla al concetto di "Verbo" definito dentro LexInfo. Allo stesso modo, prendiamo la forma declinata "written" e la colleghiamo ai concetti LexInfo di "Tempo Passato" e "Participio".

In questo modo, la struttura (OntoLex) e la competenza grammaticale (LexInfo) rimangono separate, permettendo di descrivere con precisione chirurgica qualsiasi variazione morfologica.

![center|500](img/Pasted%20image%2020260519151004.png)

## Il re dei dizionari semantici: WordNet

Per capire la portata di questi strumenti, dobbiamo guardare alla risorsa lessico-semantica più famosa al mondo: **WordNet**, nata all'Università di Princeton per l'inglese americano.

WordNet non è un normale dizionario alfabetico, ma una vera e propria rete neurale di significati. La sua struttura si basa su tre pilastri:

- **Le Parole:** Divise per categorie sintattiche (nomi, verbi, aggettivi, avverbi). Raramente include nomi propri (entità nominate), concentrandosi sui termini comuni.
    
- **I Sensi:** Le diverse accezioni che una singola parola può assumere.
    
- **I Synset (Cognitive Synonyms):** È la vera genialità del sistema. Un synset è un raggruppamento di sensi di parole diverse che esprimono esattamente lo **stesso concetto**. Ogni synset è corredato da una "glossa" (una definizione testuale ed esempi d'uso).
    

Le parole "President" e "Chairman" sono stringhe diverse, ma in uno specifico contesto aziendale sono sinonimi perfetti. In WordNet, i rispettivi sensi di queste due parole puntano allo stesso identico Synset.

Inoltre, i synset sono collegati tra loro da relazioni semantiche: ad esempio l'iperonimia (un "cane" è un tipo di "mammifero") o l'antonimia (opposti).

![center|500](img/Pasted%20image%2020260519151031.png)
### La sfida della Disambiguazione

Questa ricchezza modella perfettamente l'ambiguità del linguaggio umano, ma pone un problema ai computer. Se una parola ha 5 sensi diversi (e quindi punta a 5 synset diversi), come fa la macchina a sapere quale stiamo usando in una frase?

Questo problema prende il nome di **Word Sense Disambiguation (WSD)**: il software deve analizzare il contesto della frase per "spegnere" i sensi sbagliati e isolare l'unico senso corretto inteso dall'autore, risalendo così al concetto esatto.

### WordNet nel Web Semantico

Cosa succede quando uniamo l'enorme rete di WordNet con gli standard del Web Semantico? Nasce il porting ufficiale di **WordNet in RDF**, e lo fa utilizzando esattamente il modello **OntoLex-Lemon**!

La traduzione da dizionario tradizionale a grafo RDF è elegantissima:

- La parola inglese (es. "write") diventa una **Lexical Entry**.
    
- Le varie accezioni della parola diventano i **Lexical Sense** associati a quell'entrata.
    
- L'oggetto logico finale, il famoso Synset di WordNet, diventa il **Lexical Concept**.
    
    Il Senso fa da ponte tra l'entrata lessicale e il concetto. In questo modo, l'intero database di WordNet è diventato navigabile e interrogabile tramite le query SPARQL che abbiamo visto in precedenza.
    
### Un'infrastruttura Globale

L'impatto di WordNet è stato tale che il suo modello non è rimasto confinato all'inglese (che peraltro continua ad evolversi con fork open source come l'English WordNet).

Oggi esistono _wordnets_ per decine di lingue diverse. Iniziative come la **Global WordNet Association** o l'**Open Multilingual Wordnet** (che raccoglie oltre 30 wordnet con licenza aperta) permettono di mappare i synset di una lingua con quelli di un'altra.

Avendo un'infrastruttura comune (RDF e OntoLex), possiamo passare dal concetto di "cane" in italiano, al suo synset, da lì saltare al synset corrispondente in inglese, e infine recuperare la Lexical Entry "dog". Il tutto con un rigore logico e semantico che un semplice traduttore statistico non possiede.

---

Con questo livello di profondità, chiudiamo il cerchio che va dalla singola stringa di testo alla logica concettuale interconnessa. Vuoi approfondire in che modo queste reti multilingue vengono utilizzate praticamente per l'allineamento dei dati, o c'è un altro macro-argomento che ti aspetta nelle prossime slide?