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
# Il valore dei dati

I dati aperti che possiamo trovare in giro per il web hanno diversi valori intrinsechi, dipendenti dal contesto in cui si trovano, ad esempio in contesti sociali, economici, legali

I dati possono essere utili *indipendentemente* dall'applicazione che li usa, e possono essere usati da diverse applicazioni, per diverse applicazioni

Abbiamo diversi esempi di sfruttamento di dati (siano essi privati o pubblici), per lo più nell'offerta di servizi con un valore commerciale:
- Anagrafica e preferenze/opinioni: call center, pubblicità mirata, etc..
- Ambientali: miglioramento della capacità di produzione nell'agricoltura, etc..
- Geografici: mappe, navigatori, etc..
- Commerciali: uniti con dati geografici per fornire indicazioni localizzate
- Dati normativi e legali: utili riferimenti per legali e operatori nel settore della giurisprudenza
## Genesi e uso tradizionale dei dati

Tradizionalmente, i dati vengono:
- generati per supportare dei servizi, e asserviti ai servizi stessi
- prodotti per un preciso modello di mercato, e venduti nello stesso
- i dati rimangono isolati (Knowledge Silos), fruiti tramite le applicazioni che ne fanno uso, ma anche opacizzati dalle stesse
### Dati nelle PA

I dati all'interno delle PA (Pubbliche Amministrazioni) hanno tipicamente due tipi di *genesi*:
- (Per lo più visibili, pechè prodiotti per il pubblico) Generati direttamente come risultato primario dell'attività di un'amministrazione, ad esempio:
	- dati cartografici
	- catasto
	- informazioni meteorologiche
	- etc..
- (Generalmente invisibili, perchè pensati per uso interno) Dati acquisti: organizzati e impiegati dall'amministrazione nell'adempimento dei propri obiettivi istituzionali (sono il mezzo e non il risultato), ad esempio:
	- base di dati dei tempi medi di percorrenza dei mezzi pubblici
	- mappa geografica dei codici di avviamento postale

Nel complesso questi dati vengono denominati: **Informazioni del Settore Pubblico, Public Sector Information (PSI)**

I dati presenti nelle PA sono un patrimonio immenso, spesso gestito con mentalità antiquate

I dati forniti dalle PA garantiscono (o almeno dovrebbero poter garantire):
- **Precisione e completezza** (in quanto fonte autorevole e autoritativa): tutto ciò che riguarda un determinato argomento è coperto in modo appropriato dall'organismo ad esso preposto
- **Neutralità**: i dati non sono soggetti a bias dovuto ad interessi privati

Limiti dell'offerta PA

- Accessibilità
	- *Modalità di accesso al dato*: esempio sono spesso pubblici, ma ottenerli dalla PA richiede tempo (burocrazia) e denaro (costi di accesso, che dovrebbero in realtà coprire solo i costi di produzione per la PA, e risultano invece a volte più ampi), scarso aggiornamento alla pubblicazione
	- *Mezzo per la fruizione*: tipo di media (cartaceo, elettronico,etc..), formato del media (scansioni, PDF, testo, documento editabile,etc..)
- Fornitura: la PA spesso difetta delle risorse economiche e umane, nonchè dello slancio di innovazione, per sostenere una opportuna disseminazione dei dati presso il cittadino
- Perdita delle loro potenzialità: i servizi forniti su di essi non sono all'altezza delle potenzialità dei dati sottostanti

La soluzione a tutto ciò? Liberare i dati!

I vantaggi per la PA sono:
- *Demandare* a terzi lo sviluppo (ed i relativi costi) di applicazioni utili al cittadino
- *Ritorno economico passivo*: il cittadino gode di migliori servizi, e ha un impatto minore in termini di richieste dirette alla PA
- *Ritorno economico attivo*: in ultima analisi, chi sviluppa servizi basati sui dati, anche se questi saranno gratuiti, pagherà comunque delle tasse
- *Ritorno d'immagine*: un paese dove vi sono più servizi, pubblici o privati che siano, è un paese migliore

Analisi costi/benefici per la PA:

Da analisi effettuate su casi d’uso reali, l’introito proveniente dalla vendita di dati pubblici (e quindi vincolati a non avere margine di guadagno, includendo costi marginali e tariffe di transazione) sia proporzionale se non maggiore ai costi per mantenere il servizio di fornitura

Vantaggi per il cittadino: trasparenza e accessibilità!
- Sapere in ogni momento se i soldi pubblici sono spesi bene
- *Accedere meglio e più facilmente* ai dati tramite una pletora di servizi: grazie alla spinta di mercato sui dati aperti, diverse aziende offriranno servizi, diversi ma anche simili ed in concorrenza
- Ma *accedere anche ai dati grezzi*!: se i servizi disponibili non sono sufficienti, sarà comunque possibile accedere ai dati grezzi per ottenere le informazioni desiderate
- *Accesso in tempo reale*; match making: bandi di concorso, forniture e interessi della PA per fare analisi di mercato sulla PA
# Open Data: definizione

Semplice definizione di ***Data***: [^1]
- Fatti o informazioni usati usualmente per calcolare, analizzare o pianificare qualcosa
- Informazione che viene prodotta o memorizzata da un computer

>[!cite]- Discussione sui dati
>I dati hanno una vita propria, indipendente dal termine datum, di cui originariamente erano il plurale. Si presentano in due costruzioni: come sostantivo plurale (come guadagni), con verbo plurale e modificatori plurali (come questi, molti, pochi) ma non numeri cardinali, e come riferimento per pronomi plurali (come loro, loro); e come sostantivo astratto di massa (come information), accompagnato da un verbo singolare e da modificatori singolari (come this, much, little) e a cui si riferisce un pronome singolare (it). Entrambe le costruzioni sono standard. La costruzione plurale è più comune nella stampa, evidentemente perché lo stile interno di diversi editori lo impone.

Definizioni selezionate di Open [^2]
- Privo di barriere di recinzione o confinamento, accessibile su tutti o quasi tutti i lati -bestiame al pascolo in un prato aperto-
- non limitato a un particolare gruppo o categoria di partecipanti -aperto al pubblico- -open housing-: come 
	- **a** : accessibile sia a concorrenti dilettanti che professionisti -un torneo aperto- 
	- **b** : accessibile a un elettore registrato indipendentemente dall'affiliazione politica -primarie aperte-

Definizione di Open da [^3]

La definizione di Open stabilisce i principi che definiscono l' "apertura" in relazione ai dati e ai contenuti. Precisa il significato di "aperto" nei termini "dati aperti" e "contenuti aperti" e garantisce così la qualità e incoraggia la compatibilità tra diversi pool di materiale aperto.

Si può riassumere con la seguente affermazione:

>[!cite]- 
>"Aperto significa che **chiunque** può **accedere, utilizzare, modificare e condividere** liberamente per **qualsiasi scopo** (soggetto, al massimo, a requisiti che preservano la provenienza e l'apertura)".

Più succintamente:

“I dati e i contenuti aperti possono essere **liberamente utilizzati, modificati e condivisi** da chiunque per qualsiasi scopo”.


[^1]: http://www.merriam-webster.com/dictionary/data

[^2]: http://www.merriam-webster.com/dictionary/open

[^3]: http://opendefinition.org/

# Riutilizzo dei dati

La Direttiva 2013/37/UE [^4] definisce il **riutilizzo** come l'uso di documenti detenuti da enti pubblici da parte di persone fisiche o giuridiche a fini commerciali o non commerciali diversi dallo scopo iniziale nell'ambito dei compiti di servizio pubblico per i quali i documenti sono stati prodotti

>[!cite]- Parole Chiave: Riutilizzo
>Chi si occupa di informazione del settore pubblico parla spesso di “riutilizzo” (o “riuso”), anziché di “utilizzo” (o “uso”). La scelta del termine riutilizzo sottolinea il fatto che stiamo parlando di **usi diversi e ulteriori, rispetto all'uso istituzionale, per cui il dato è stato raccolto o generato dalla PA. Il riutilizzo va anche chiaramente distinto dal mero accesso**. Ciò che interessa non è solo la possibilità di accedere ai dati; approcci tipo “guardare, ma non toccare”, infatti, non facilitano la vita degli sviluppatori e la creazione di servizi utili ai cittadini. Poter vedere i dati è solo il primo passo per poterli acquisire e poi finalmente riutilizzare, cioè modificare, mescolare e/o trasformare per renderli più utili ed interessanti (per alcuni specifici scopi, senza togliere ad altri la possibilità di fare altrettanto, in modo diverso, per i loro differenti obiettivi)



[^4]: http://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32013L0037
