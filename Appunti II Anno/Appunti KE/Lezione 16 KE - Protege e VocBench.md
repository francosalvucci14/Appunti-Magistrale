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
# Protégé

Introduciamo **Protégé**, un _editor di ontologie gratuito e open-source_ e un _framework per costruire sistemi intelligenti_.

Protégé esiste in **due edizioni principali**:

- **WebProtégé:** È la versione cloud. Viene offerta in modalità _Software-as-a-Service (SaaS)_ ospitata direttamente dalla Stanford University, ma viene precisato che può anche essere scaricata e installata localmente sul proprio server.
    
- **Protégé Desktop:** È l'applicazione classica da scaricare e installare sul proprio computer (nella slide è mostrata la versione 5.5.0). È disponibile per Windows, Linux e Mac OSX, oppure come pacchetto indipendente dalla piattaforma che richiede l'installazione di Java (versione 8 o superiore).

## WebProtégé vs Protégé Desktop (Tabella comparativa)

Qua mettiamo a confronto diretto le funzionalità delle due versioni.

- **Caratteristiche in comune:** Entrambe sono conformi agli standard W3C e sono inter-compatibili (ciò che crei in una versione può essere aperto nell'altra).
    
- **Punti di forza di WebProtégé:**
    
    - Interfaccia utente semplice e personalizzabile.
        
    - Fortemente ottimizzato per la _collaborazione_ tra più utenti.
        
    - Possiede un sistema di tracciamento delle modifiche e della storia delle revisioni (simile a un sistema di versioning).
        
    - Offre form web per l'editing specifico in base al dominio.
        
    - Supporta formati multipli di upload e download.
        
- **Punti di forza di Protégé Desktop:**
    
    - Interfaccia utente personalizzabile, ma orientata all'uso avanzato.
        
    - Offre strumenti nativi per la _visualizzazione grafica_ delle ontologie.
        
    - Supporta il _refactoring_ delle ontologie (ristrutturazione avanzata).
        
    - Ha un'interfaccia diretta per collegare i _reasoner_ (motori di inferenza per verificare la coerenza logica dell'ontologia).
        
    - Possiede un'architettura altamente basata su _plugin_, espandibile con strumenti di terze parti.
        

## WebProtégé (Introduzione alle interfacce)

Vediamo una panoramica sulle caratteristiche principali di WebProtégé.
### WebProtégé – Home page

![center|400](img/Pasted%20image%2020260606124725.png)

Questa immagine mostra la schermata iniziale (dashboard) dopo aver effettuato l'accesso.

- Sulla sinistra è presente il pulsante viola **"Create New Project"** per avviare una nuova ontologia. Sotto di esso ci sono dei filtri per visualizzare i progetti di propria proprietà ("Owned by Me"), condivisi da altri ("Shared with Me") o nel cestino ("Trash").
    
- Al centro c'è la lista dei progetti. In questo caso c'è un solo progetto chiamato "Test", creato dall'utente "Manuel Fiorelli" (identificato con l'icona MF). La tabella mostra anche quando il progetto è stato aperto e modificato l'ultima volta (in questo caso "2 minutes ago").

### WebProtégé – Editing di classi

![center|400](img/Pasted%20image%2020260606124755.png)

Questa schermata entra nel vivo dell'editor di ontologie web. L'interfaccia è divisa in pannelli:

- **A sinistra (Class Hierarchy):** Mostra la gerarchia delle classi. Si vede la classe radice `owl:Thing` da cui discendono due sottoclassi: `Person` e `Organization`. La classe `Person` è attualmente selezionata.
    
- **Al centro (Class):** Mostra i dettagli della classe `Person` selezionata.
    
    - Si vede l'**IRI** (l'identificativo univoco della risorsa sul web).
        
    - Nella sezione **Annotations** si nota il supporto multilingua: è stata inserita l'etichetta (`rdfs:label`) "Person" per l'inglese (en) e "Persona" per l'italiano (it).
        
- **A destra (Project Feed):** È un feed in tempo reale che registra le azioni degli utenti. Si vede che l'utente Manuel Fiorelli ha appena modificato la classe `Person` e la proprietà `worksFor`.

### WebProtégé – Storia delle modifiche su una risorsa

![center|400](img/Pasted%20image%2020260606124808.png)

Questa vista si concentra sulla tracciabilità delle azioni per una **singola entità** (in questo caso, sempre la classe `Person`).

- Il pannello centrale ("Changes by Entity") mostra la cronologia esatta di cosa è successo a questa specifica classe.
    
- Si legge che 6 minuti fa Manuel Fiorelli ha _creato_ la classe aggiungendo l'IRI e la label in inglese.
    
- Successivamente, 1 minuto fa, ha _modificato_ la classe aggiungendo la label in italiano ("Persona"@it).
    
- Questo dimostra la granularità con cui WebProtégé traccia chi fa cosa e quando, fondamentale per il lavoro collaborativo

### WebProtégé – Storia delle revisioni

![center|400](img/Pasted%20image%2020260606124820.png)

A differenza della slide precedente (che mostrava la storia di _una singola classe_), questa slide mostra la scheda **"History"**, ovvero la cronologia delle revisioni dell'intero progetto.

- Qui viene tracciata la creazione e la modifica di un'altra entità: la Object Property `worksFor`.
    
- Si vede che è stata creata (aggiungendo l'IRI e definendola come sotto-proprietà di `owl:topObjectProperty`).
    
- Successivamente le sono stati assegnati un Dominio (`Person`) e un Codominio/Range (`Organization`).
    
- **Dettaglio fondamentale:** Cliccando su una specifica revisione, compare un menù a tendina che offre l'opzione **"Revert changes in revision 4"** (Annulla le modifiche della revisione 4) o **"Download revision 4"**. Questo dimostra che WebProtégé funziona come un sistema di controllo versione (tipo Git), permettendo di tornare indietro in caso di errori.

## Protégé Desktop: Caratteristiche Principali

Questa slide introduce le specifiche tecniche e le funzionalità principali della versione desktop:

- Protégé Desktop è definito come un editor di ontologie OWL2.
    
- Offre il pieno supporto per la visualizzazione della "conoscenza inferibile", il che avviene collegando il software a un _reasoner_ (motore di inferenza).
    
- A partire dalla versione 4, il programma utilizza le **OWL API** per rappresentare e gestire le ontologie OWL direttamente in memoria.
    
- Dispone di una vasta libreria di plugin espandibili, tuttavia viene segnalato che questa libreria è frazionata e presenta incompatibilità tra le versioni principali del tool (in particolare tra la versione 3 e le versioni 4 o superiori).

### Interfaccia e Gerarchia Asserita (Asserted)

![center|400](img/Pasted%20image%2020260606133458.png)

L'immagine mostra l'interfaccia classica di Protégé Desktop durante la modellazione:

- Sulla sinistra è visibile la gerarchia delle classi (Class hierarchy), impostata sulla vista **"Asserted"** (le affermazioni inserite manualmente dall'utente).
    
- Nel pannello di sinistra è selezionata la classe `:Director`.
    
- Nel pannello di destra, sotto la sezione "Description", si vede che la classe `:Director` è stata definita come equivalente a (Equivalent To): la classe `:Person` unita all'assioma `(:headOf some :Program)`.

### Avvio del Reasoner

In questo passaggio viene mostrato come attivare il motore di inferenza:

- L'utente apre il menù "Reasoner" nella barra in alto e seleziona **"Start reasoner"** (scorciatoia Ctrl-R).
    
- Un tooltip spiega che questa azione avvia un nuovo reasoner e inizializza una cache con i risultati del ragionamento logico, includendo la gerarchia delle classi e i tipi di individui che sono stati _inferiti_ (dedotti logicamente) dal sistema.
    
- Il reasoner selezionato e in uso in questo specifico esempio è **HermiT 1.4.3.456**.

![center|400](img/Pasted%20image%2020260606133523.png)

### Risultati dell'Inferenza logica

Dopo aver avviato il reasoner, l'interfaccia mostra le nuove informazioni dedotte:

- Il menù a tendina sopra la gerarchia delle classi viene spostato da "Asserted" a **"Inferred"** (evidenziato con un cerchio rosso).
    
- Il sistema ha dedotto logicamente una nuova relazione non dichiarata esplicitamente: la classe `:Director` ora appare come sottoclasse (SubClass Of) di `:Employee`, e questa novità è evidenziata con uno sfondo giallo.
    
- Una freccia indica che è possibile cliccare sull'icona a forma di punto interrogativo ("?") accanto alla riga gialla per **"Ottenere una giustificazione della inferenza"**.
    
- Un fumetto ricorda un concetto teorico importante: reasoner diversi offrono garanzie differenti in termini di completezza ed efficienza computazionale.

![center|400](img/Pasted%20image%2020260606133544.png)
### Finestra di Giustificazione (Explanation)

Cliccando sul punto interrogativo, si apre una finestra popup che spiega _perché_ il reasoner ha dedotto quella specifica informazione:

- La finestra "Explanation for :Director SubClassOf :Employee" elenca la serie di assiomi logici che hanno portato a questa inferenza.
    
- Vengono proposte due diverse catene logiche per raggiungere la stessa conclusione, etichettate come "Explanation 1" ed "Explanation 2".
    
- Un fumetto aggiunto dal docente avvisa gli studenti: "Nella prova scritta le spiegazioni dovranno essere molto più chiare".

![center|400](img/Pasted%20image%2020260606133623.png)
### Rappresentazione Grafica della Giustificazione

Questa slide arricchisce la schermata precedente sovrapponendovi un diagramma per visualizzare la logica matematica dell'inferenza:

- Viene mostrato un diagramma di Eulero-Venn che descrive le relazioni insiemistiche tra le classi.
    
- Tutti gli elementi si trovano all'interno dell'insieme `:Person`.
    
- L'insieme blu rappresenta la classe `:Employee` (formata dalle persone che hanno una relazione `:worksFor some :Organization`).
    
- L'insieme rosso rappresenta la classe `:Director` (formata da chi ha una relazione `:headOf some :Program`), la quale è contenuta e inclusa totalmente all'interno dell'insieme più grande `:Employee`.

![center|400](img/Pasted%20image%2020260606133633.png)
### Giustificazioni Laconiche

Esploriamo un'ulteriore opzione nella finestra delle spiegazioni:

- L'utente ha selezionato il radio button **"Show laconic justifications"** (mostra giustificazioni laconiche) al posto della vista standard.
    
- Il testo parzialmente tagliato in alto a destra definisce queste spiegazioni come giustificazioni "i cui assiomi non contengono parti superflue".
    
- Di conseguenza, le spiegazioni mostrate (Explanation 1 ed Explanation 2) risultano più lunghe e frammentate in un numero maggiore di passaggi logici (ad esempio la Explanation 1 passa da 4 a 5 step e la Explanation 2 arriva a 7 step), analizzando la deduzione nei suoi componenti logici minimi ed essenziali.

![center|400](img/Pasted%20image%2020260606133657.png)


# VocBench

- VocBench è una piattaforma web-based e multilingua per lo sviluppo collaborativo.
    
- È progettata per gestire ontologie OWL, tesauri SKOS(/XL), lessici OntoLex-Lemon e, più in generale, dataset RDF.
    
- È un software gratuito e open-source rilasciato sotto licenza BSD-3-Clause.
    
- Rappresenta una soluzione di riferimento per i paesi dell'Unione Europea, essendo il suo sviluppo stato finanziato dal programma ISA² della Commissione Europea.

![center|400](img/Pasted%20image%2020260606134219.png)

## Funzionalità ed Ecosistema

- VocBench permette di gestire l'intero flusso di lavoro di pubblicazione (publication workflow) tramite un sistema integrato di validazione e cronologia (history) delle modifiche.
    
- L'interfaccia offre un editor SPARQL avanzato dotato di evidenziazione della sintassi (highlight) e completamento automatico.
    
- Integra i "Custom Forms", descritti come un potente linguaggio per la descrizione dei moduli che consente di personalizzare la rappresentazione dei dati in base alle specifiche esigenze del progetto.
    
- Il motore tecnologico alla base di VocBench è "Semantic Turkey".
    
- Semantic Turkey agisce come una "piattaforma a servizi per supportarli tutti", fungendo da base non solo per VocBench (focalizzato sull'editing), ma anche per un'altra applicazione gemella chiamata **ShowVoc**, dedicata alla pubblicazione di dati e all'hosting di portali di dati.

## Requisiti e Modalità di Installazione

- Per la versione di riferimento indicata nella documentazione (la 10.1.1), il sistema richiede l'installazione esatta di Java 8.
    
- Questa specifica versione è stata testata in abbinamento al database GraphDB versione 9.8.1.
    
- VocBench offre due principali opzioni di deployment:
    
    - **Modalità Desktop:** Può essere installato e utilizzato come una normale applicazione desktop su un singolo computer, configurando un utente amministratore predefinito.
        
    - **Modalità Server/Cloud:** È possibile ospitare un'istanza condivisa su una macchina server o in cloud, consentendo l'accesso simultaneo a una moltitudine di utenti.

## Architettura di Sistema

L'architettura del sistema è divisa in tre livelli principali in comunicazione tra loro:

- **Livello Interfaccia Utente (VOCBENCH 3 UI):** Interfaccia sviluppata in Angular che opera su un Web Application Server e comunica con il livello intermedio tramite richieste HTTP.
    
- **Livello Intermedio (Middle Layer - Semantic Turkey):** Basato su un motore Spring/OSGi, espone i servizi HTTP. Contiene il registro dei servizi di Semantic Turkey e gestisce componenti chiave come la gestione utenti (User Mgmt), la gestione progetti (Project Mgmt), i Custom Forms, CODA, MAPLE e vari servizi RDF. Questo livello sfrutta punti di estensione basati su OSGi per funzionalità come l'input/output, la generazione di metadati e URI.
    
- **Livello Dati (Data Layer):** Utilizza il Semantic Turkey Data Manager e le API RDF4J per interfacciarsi con i database. Supporta l'archiviazione su base locale (RDF4J Local Store, su file system o in memoria) e la connessione a specifici Triple Store esterni.

![center|400](img/Pasted%20image%2020260606134311.png)
