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

"I dati e i contenuti aperti possono essere **liberamente utilizzati, modificati e condivisi** da chiunque per qualsiasi scopo".


[^1]: http://www.merriam-webster.com/dictionary/data

[^2]: http://www.merriam-webster.com/dictionary/open

[^3]: http://opendefinition.org/
## Riutilizzo dei dati

La Direttiva 2013/37/UE [^4] definisce il **riutilizzo** come l'uso di documenti detenuti da enti pubblici da parte di persone fisiche o giuridiche a fini commerciali o non commerciali diversi dallo scopo iniziale nell'ambito dei compiti di servizio pubblico per i quali i documenti sono stati prodotti

>[!cite]- Parole Chiave: Riutilizzo
>Chi si occupa di informazione del settore pubblico parla spesso di "riutilizzo" (o "riuso"), anziché di "utilizzo" (o "uso"). La scelta del termine riutilizzo sottolinea il fatto che stiamo parlando di **usi diversi e ulteriori, rispetto all'uso istituzionale, per cui il dato è stato raccolto o generato dalla PA. Il riutilizzo va anche chiaramente distinto dal mero accesso**. Ciò che interessa non è solo la possibilità di accedere ai dati; approcci tipo "guardare, ma non toccare", infatti, non facilitano la vita degli sviluppatori e la creazione di servizi utili ai cittadini. Poter vedere i dati è solo il primo passo per poterli acquisire e poi finalmente riutilizzare, cioè modificare, mescolare e/o trasformare per renderli più utili ed interessanti (per alcuni specifici scopi, senza togliere ad altri la possibilità di fare altrettanto, in modo diverso, per i loro differenti obiettivi)

## Il contesto normativo

Definizione di "dati di tipo aperto" fornita dall’ art. 68 del Codice dell’Amministrazione Digitale(CAD):

<<sono definiti come tali i dati accessibili e disponibili gratuitamente (o comunque non oltre i costi marginali di riproduzione e diffusione) attraverso le tecnologie dell'informazione e della comunicazione in formati aperti, ivi comprese le reti telematiche pubbliche e private, quando sussiste una licenza che ne permetta l'utilizzo da parte di chiunque, anche per finalità commerciali.>>

L’art. 7 del c.d. Decreto Trasparenza (richiamando a sua volta l’art. 68 del CAD) stabilisce che:
<< i dati oggetto di pubblicazione obbligatoria ai sensi della normativa vigente sono riutilizzabili
senza ulteriori restrizioni diverse dall'obbligo di citare la fonte e di rispettarne l'integrità.>>
### In Europa

Accesso e riutilizzo delle informazione del settore pubblico [^5]
- Iniziative di studio e discussione già a partire dalla seconda metà degli anni novanta.
- 1999: Libro verde sull’informazione del settore pubblico nella società dell’informazione della Commissione Europea
	- frutto di un processo di consultazione avviato nel 1996
	- evidenziati per la prima volta, all'interno di un unico documento, i principali profili giuridici, economici e tecnici connessi alla fruizione di dati prodotti dal settore pubblico.
- Successiva consultazione pubblica aperta a tutti gli operatori interessati su
	- profili di diritto d'autore;
	- tutela della sfera privata;
	- politiche sul prezzo e relativo impatto su accessibilità ed uso dell'informazione pubblica;
	- profili di concorrenza sleale connessi all'attività degli enti pubblici sul mercato dell'informazione;
	- impiego di metadati per facilitare l'acceso all'informazione)
- Direttiva 2003/98/CE del Parlamento europeo e del Consiglio, approvata il 17 novembre 2003 e pubblicata nella GUCE n. L 345 del 31 dicembre 2003 (c.d. Direttiva PSI)
	- rappresenta a tutt’oggi il testo normativo di riferimento in tema di riutilizzo dell'informazione del settore pubblico nell’Unione Europea.
	- Ha l’obiettivo di agevolare la "creazione di prodotti e servizi a contenuto informativo, basati su documenti del settore pubblico, estesi all'intera Comunità, nel promuovere un effettivo uso, oltre i confini nazionali, dei documenti del settore pubblico da parte delle imprese private, al fine di ricavarne prodotti e servizi a contenuto informativo a valore aggiunto e nel limitare le distorsioni della concorrenza sul mercato comunitario".
	- Naturalmente, la Direttiva non si applica indiscriminatamente a ogni dato detenuto dalle pubbliche amministrazioni, evitando dunque di pregiudicare diritti di terzi, tutela della sicurezza nazionale, segreto statistico o tutela della privacy

# Licenza (informatica)

I diritti esclusivi sono una prerogativa automaticamente assegnata all'autore di un’opera dell'ingegno, senza che questo debba farne richiesta, per consentire circolazione o altri utilizzi, serve esplicita autorizzazione
In assenza di esplicita **licenza**, quasi ogni utilizzazione è vietata dalla legge ai terzi

La licenza (in informatica) è un *contratto* tra il *detentore del copyright* e l'*utente*
## Licenza Creative Commons

Le licenze CC sono un set di licenze copyright che forniscono un modo semplice e
"standardizzato" per dare pubblicamente il permesso di condividere e usare opere d’ingegno secondo determinate condizioni.

Le licenze CC permettono di introdurre diverse sfumature di openness ai termini del copyright dal default di "all rights reserved" verso "some rights reserved."

Le licenze Creative Commons non sono una alternative al copyright. Sono uno strumento che affiance il copyright permettendo di modificarlo al fine di soddisfare specifiche esigenze

Ci sono 3 tipi di licenze:
- quelle per dettagliare la licenza in termini legali
- per renderla "human understandable"
- per renderla "machine understandable"

Per scegliere che tipo di licenza usare, ci sono dei servizi online che, grazie ad una specie di questionario, ti permettono di ottenere la licenza migliore per il tuo caso d'uso

![[Pasted image 20251018114730.png|center|500]]

![[Pasted image 20251018114813.png|center|500]]


[^4]: http://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32013L0037

[^5]:  http://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32003L0098
