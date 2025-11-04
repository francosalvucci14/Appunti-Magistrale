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
# Semantic Web 

## Semantic Web : Ingredienti

Esprimere il significato

- Gli agenti software navigheranno sul web e svolgeranno compiti sofisticati per gli utenti.
- Le macchine saranno in grado di “comprendere” i dati che attualmente si limitano a visualizzare

Rappresentazione della conoscenza e ontologie
- Le macchine accedono a raccolte strutturate di informazioni.
- Le macchine utilizzano regole per trarre conclusioni, scegliere linee d'azione e rispondere a domande.

Agenti

- I servizi web si realizzano quando gli agenti “comprendono” sia la funzione offerta sia come trarne vantaggio.
- Sottoinsiemi di informazioni vengono passati da un agente all'altro, ciascuno dei quali aggiunge valore per costruire il prodotto finale richiesto da un utente.

Evoluzione della conoscenza
- Se progettato correttamente, il Web semantico può aiutare nell'evoluzione della conoscenza umana.
- Un Web universale aprirà la conoscenza e il funzionamento dell'umanità ad analisi significative da parte di agenti software, fornendo una nuova classe di strumenti con cui possiamo vivere, lavorare e imparare insieme.

>[!cite]- What the Semantic Web can represent, 1998
>The concept of machine-understandable documents does not imply some magical artificial intelligence which allows machines to comprehend human mumblings. It only indicates a machine's ability to solve a **well-defined** problem by performing **well-defined** operations on existing **well-defined** data. Instead of asking machines to understand people's language, it involves asking people to make the extra effort

## Semantic Web : La visione

La visione del Semantic Web è la seguente:

- "... un piano per realizzare una serie di applicazioni collegate per i dati sul Web in modo tale da formare una rete logica coerente di dati.." [^1]
- "... un'estensione dell'attuale web in cui alle informazioni viene attribuito un significato ben definito, consentendo a computer e persone di lavorare in modo più cooperativo... " [^2]

[^1]: T. Berners-Lee. Semantic Web RoadMap. http://www.w3.org/DesignIssues/Semantic.html

[^2]: T. Berners-Lee, J. Hendler & O. Lassila. The Semantic Web: A new form of Web content that is meaningful to computers will unleash a revolution of new possibilities. Scientific American, May 2001

## Rappresentare Informazioni sul Web

Le **ontologie** forniranno il vocabolario necessario per rendere i dati (e gli schemi ad essi associati) comprensibili alle macchine, offrendo:
- Modelli di dati universali
- Semantica standard
- Livelli di inferenza stratificati

Gli **agenti SW** sfrutteranno la conoscenza ontologica (e di base) distribuita per:
- Comprendere le richieste degli utenti rispetto al proprio vocabolario semantico
- Collaborare con altri agenti su basi comuni

Lo stack del Semantic Web è il seguente:

![center](img/Pasted%20image%2020251027113622.png)

# Ontologie

## Linguaggi Ontologici

L'impegno verso linguaggi per la rappresentazione della conoscenza sul Web, come **RDF** e **OWL**, dovrebbe garantire una reale interoperabilità della conoscenza tra fonti di informazione distribuite

Il passaggio dalla sintassi esplicita alla semantica non richiederà macchine intelligenti, ma solo standard che esse possano comprendere

## Modelli e Meta-Modelli : Semantica

OWL, RDF ecc. ***non sono*** modelli di mondo/dominio.

Sono modelli per la rappresentazione della conoscenza e quindi meta-modelli per descrivere oggetti del mondo reale.

Ad esempio, se dici che A p.B C, puoi affermare che:
- tutte le istanze di C sono anche istanze di A;
- tutte le istanze di C sono soggette alla restrizione di intervallo sulla proprietà p (che deve puntare a oggetti in B);
- etc..

Non è possibile dire:
- in che modo le istanze di A (o C) siano effettivamente correlate agli oggetti del mondo reale

## Semantiche Ontologiche

La semantica di ciascuna ontologia è definita da:
- L'interpretazione data dalle persone che utilizzano l'ontologia all'interno di un determinato quadro di riferimento
- L'uso che le applicazioni fanno dei concetti dell'ontologia all'interno del loro quadro di riferimento

Gli spazi dei nomi si comportano, sotto tutti gli aspetti, come riferimenti oggettivi all'interno dello stesso quadro di riferimento.
- ci si aspetta che gli esseri umani interpretino gli stessi nomi nello stesso namespace allo stesso modo, così come
- ci si aspetta che le macchine utilizzino questi dati in modo coerente

![center](img/Pasted%20image%2020251027123203.png)

**Cosa succede se non avviene un'accordo sulla semantica?**

Esistono molte ontologie diverse e indipendenti e molte altre saranno sviluppate in futuro su domini identici o sovrapposti.

È importante integrare le loro informazioni, sia a livello di:
- Schema
	- Migrazione delle conoscenze e interrogazione remota
- Dati
	- Espansione delle conoscenze sugli stessi oggetti

Questa integrazione deve essere eseguita tramite:
- Fusione delle ontologie (creando una risorsa globale da quelle esistenti)
- Mappatura ontologica (realizzazione di mappature tra risorse esistenti)

![center|300](img/Pasted%20image%2020251027123351.png)

# Possibili applicazioni del Semantic Web

Richieste complesse che richiedono **conoscenze di base**

- Trovare informazioni su "animali che utilizzano il sonar ma non sono né pipistrelli né delfini"

Individuare informazioni in **archivi di dati**

- Richieste di informazioni sui viaggi
- Prezzi di beni e servizi
- Risultati di esperimenti sul genoma umano

Trovare e utilizzare “**servizi web**”

- Visualizzare le interazioni superficiali tra due proteine

Delegare compiti complessi ad “**agenti**” web

- Prenotami una vacanza per il prossimo fine settimana in un posto caldo, non troppo lontano, e dove si parla francese o inglese