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
# OWL
## Il compromesso fondamentale: I Sottolinguaggi di OWL

Nella rappresentazione della conoscenza esiste un teorema matematico ineludibile: **più un linguaggio è espressivo (cioè ti permette di dire cose complesse), più il ragionamento automatico su di esso diventa computazionalmente pesante, fino a diventare "indecidibile"** (ovvero, un computer potrebbe non finire mai di calcolare una deduzione).

Per gestire questo compromesso, OWL 1 è stato diviso in tre "sottolinguaggi" o profili, definiti attraverso precise restrizioni sull'uso dei suoi costrutti:

- **OWL Full:** È il linguaggio completo. In OWL Full non ci sono restrizioni: una risorsa può essere contemporaneamente trattata come una Classe, come un'Istanza e come una Proprietà. È il massimo dell'espressività, ma il prezzo da pagare è altissimo: **il ragionamento in OWL Full è matematicamente indecidibile**. Nessun software può garantire di inferire tutte le conseguenze logiche in un tempo finito.
    
- **OWL DL (Description Logic):** È il cuore pulsante del Web Semantico. Per garantire che il ragionamento sia **decidibile** (il computer prima o poi ti darà sempre una risposta corretta), OWL DL impone una _stretta separazione (disgiunzione)_ tra le entità. In OWL DL, un URI può essere o una Classe, o una Proprietà, o un Individuo, ma non può mescolare i ruoli. Offre il miglior bilanciamento tra potenza espressiva e ragionabilità.
    
- **OWL Lite:** È una versione fortemente ristretta di OWL DL. Non permette, ad esempio, di usare cardinalità arbitrarie (puoi usare solo cardinalità 0 o 1). È stato progettato per garantire la massima **efficienza computazionale** e per facilitare agli sviluppatori la creazione di software di _reasoning_ (ragionatori) più semplici e veloci.
    
## Le Classi in OWL

In OWL, le classi sono gli insiemi astratti a cui appartengono gli individui.

Definire una classe è molto semplice. Si introduce dandole un nome (un IRI) tramite il costrutto `owl:Class`:

`<owl:Class rdf:ID="Person" />`

Una volta definita la classe, la si utilizza per tipizzare gli individui (le istanze). In RDF/XML, come mostrano le tue slide, ci sono due approcci sintattici equivalenti:

1. **Forma abbreviata:** Usare il nome della classe direttamente come tag XML.
    
    `<Person rdf:ID="manuel" />`
    
1. **Forma estesa (standard RDF):** Dichiarare l'entità come un generico `owl:Thing` (la super-classe universale di cui ogni cosa in OWL fa parte) e poi esplicitare il tipo tramite `rdf:type`.
    ```XML
    <owl:Thing rdf:ID="manuel">
        <rdf:type rdf:resource="#Person" />
    </owl:Thing>
    ```
## Le Proprietà in OWL

A differenza di RDF e RDFS (dove esiste solo il generico `rdf:Property`), OWL DL richiede una separazione rigorosa di come le risorse si collegano tra loro. Per questo, introduce tre tipi distinti di proprietà:

- **Object Property (`owl:ObjectProperty`):** Mettono in relazione due individui (due risorse dotate di URI).
    
    _Esempio:_ La proprietà "ama".
    ```XML
    <owl:ObjectProperty rdf:ID="ama">
        <rdfs:domain rdf:resource="#Persona" /> <rdfs:range rdf:resource="#Persona" />  <rdfs:subPropertyOf rdf:resource="#conosce" /> </owl:ObjectProperty>
    ```
    
- **Datatype Property (`owl:DatatypeProperty`):** Mettono in relazione un individuo con un valore letterale primitivo (stringhe, numeri interi, date, ecc.), tipicamente appoggiandosi ai tipi di dato di XML Schema (`xsd`).
    
    _Esempio:_ La proprietà "nome".
    ```XML
    <owl:DatatypeProperty rdf:ID="nome">
        <rdfs:domain rdf:resource="#Persona" />
        <rdfs:range rdf:resource="&xsd;string" /> 
    </owl:DatatypeProperty>
    ```
    
- **Annotation Property:** Servono per aggiungere metadati (commenti, etichette umane come `rdfs:label` o `rdfs:comment`). La cosa fondamentale è che il motore di inferenza (il reasoner) **le ignora completamente**; stanno al di fuori della semantica logica dell'ontologia.
## Descrivere gli Individui (L'uso pratico)

Unendo Classi e Proprietà, possiamo istanziare la nostra conoscenza. Nelle tue slide troviamo un esempio concreto di due individui, Armando e Manuel.


```XML
<Persona rdf:ID="armando">
    <conosce rdf:resource="#manuel" /> <nome rdf:datatype="&xsd;string">Armando</nome> </Persona>

<owl:Thing rdf:ID="manuel">
    <rdf:type rdf:resource="#Persona" />
    <nome rdf:datatype="&xsd;string">Manuel</nome>
</owl:Thing>
```

Notiamo come, semanticamente, le due scritture (una che usa `<Persona>` e l'altra che usa `<owl:Thing>` + `<rdf:type>`) portino esattamente allo stesso risultato logico nel grafo.

### Gestire l'Identità: Sconfiggere la NUNA (`owl:differentFrom` e `owl:AllDifferent`)

Ricordi la **No Unique Name Assumption (NUNA)** discussa in precedenza? OWL per impostazione predefinita non assume che URIs diversi indichino cose diverse nel mondo reale (Armando e Manuel potrebbero benissimo essere la stessa persona che usa due pseudonimi).

Se vogliamo che il ragionatore sappia con certezza che stiamo parlando di entità distinte (ad esempio per far scattare un errore di cardinalità), dobbiamo dirglielo noi esplicitamente.

**Approccio 1: `owl:differentFrom` (A coppie)**

Possiamo dichiarare, all'interno della definizione di un individuo, che esso è logicamente distinto da un altro:

```XML
<Persona rdf:ID="armando">
    <owl:differentFrom rdf:resource="#manuel" />
    <owl:differentFrom rdf:resource="#andrea" />
</Persona>
```

Questo metodo va bene per 2 o 3 individui. Ma se avessi 100 dipendenti e volessi dire che sono tutti persone diverse? Dovrei scrivere migliaia di queste righe (dichiarando le differenze a coppie)!

**Approccio 2: `owl:AllDifferent` (Per collezioni)**

Per risolvere il problema dell'esplosione combinatoria, OWL ci fornisce un costrutto specifico per dichiarare che un intero gruppo di individui è composto da elementi mutuamente distinti (nessuno è uguale all'altro):

```XML
<owl:AllDifferent>
    <owl:distinctMembers rdf:parseType="Collection">
        <owl:Thing rdf:about="#armando" />
        <owl:Thing rdf:about="#manuel" />
        <owl:Thing rdf:about="#andrea" />
    </owl:distinctMembers>
</owl:AllDifferent>
```

Usando il costrutto `<owl:distinctMembers>` con il tipo di parsing `Collection` (che in RDF genera una lista chiusa), diciamo al motore inferenziale: _"Prendi tutti i membri di questa lista e assumi che ciascuno di essi sia rigorosamente diverso da tutti gli altri"_. Questo è fondamentale per permettere al _reasoner_ di contare gli individui in maniera corretta quando si applicano restrizioni di cardinalità.

## Descrizione di Classi

In RDFS potevamo solo dichiarare l'esistenza di una classe e creare gerarchie (sottoclassi). OWL, invece, ci permette di _descrivere_ intensionalmente o estensionalmente le classi. Nelle slide fornite, vediamo che OWL offre sei metodi per descrivere una classe:

1. Assegnando un **nome** (URI).
    
2. Tramite **enumerazione** esaustiva delle istanze.
    
3. Imponendo una **restrizione su una proprietà**.
    
4. Tramite **intersezione** (AND logico).
    
5. Tramite **unione** (OR logico).
    
6. Tramite **complemento** (NOT logico).
    

Analizziamo nel dettaglio 
### 1. Descrizione tramite Nome (URI)

È il costrutto base, già accennato in precedenza. Si definisce una classe semplicemente dichiarando un identificatore univoco.

- **Sintassi RDF/XML:**
    
    
    ```XML
    <owl:Class rdf:ID="Human" />
    ```
    
- **Notazione Logica Descrittiva (DL):**
    $\text{Human}$    

Questa descrizione dichiara semplicemente che esiste un concetto chiamato "Human" nel nostro dominio, senza aggiungere (per il momento) alcun vincolo logico sulle sue caratteristiche.

---

### 2. Descrizione tramite Enumerazione (`owl:oneOf`)

Questo metodo permette di definire una classe _estensionalmente_, ovvero elencando in modo esplicito ed esaustivo tutti e soli gli individui che vi appartengono. Qualsiasi individuo non presente in questa lista **non fa parte della classe**.

- **Sintassi RDF/XML:**
    ```XML
    <owl:Class>
        <owl:oneOf rdf:parseType="Collection">
            <owl:Thing rdf:about="#Europe"/>
            <owl:Thing rdf:about="#Africa"/>
            <owl:Thing rdf:about="#Asia"/>
            <owl:Thing rdf:about="#America"/>
            <owl:Thing rdf:about="#Australia"/>
            <owl:Thing rdf:about="#Antarctica"/>
        </owl:oneOf>
    </owl:Class>
    ```
    
- **Notazione Logica Descrittiva (DL):**
    
    $\{\text{Europe}, \text{Africa}, \text{Asia}, \text{America}, \text{Australia}, \text{Antarctica}\}$

**Nota Formale:** Si noti l'assenza di un `rdf:ID` nel tag `<owl:Class>`. Stiamo creando una _classe anonima_ definita unicamente dal suo contenuto. L'attributo `rdf:parseType="Collection"` è fondamentale: garantisce che la lista sia "chiusa" e ordinata, comunicando al _reasoner_ che l'enumerazione è terminata e non esistono altri continenti al di fuori di quelli elencati.

### 3. Descrizione tramite Restrizioni su Proprietà (`owl:Restriction`)

Questo è il meccanismo inferenziale più potente di OWL. Invece di assegnare individui a una classe manualmente, definiamo una classe anonima formata da **tutti gli individui che soddisfano un determinato vincolo (restrizione) sull'uso di una certa proprietà**.

Le restrizioni si dividono in due macro-categorie: **Vincoli sul valore** (quali entità possono essere oggetto della relazione) e **Vincoli sulla cardinalità** (quante relazioni di quel tipo possono esistere, che vedremo più avanti).

Analizziamo i tre vincoli sul valore:

#### A. Restrizione Universale (`owl:allValuesFrom`)

Definisce la classe degli individui per i quali **tutti** i valori di una specifica proprietà (se esistono) devono necessariamente appartenere a una classe specifica (o a un tipo di dato).

- **Sintassi RDF/XML:**
    
    ```XML
    <owl:Restriction>
        <owl:onProperty rdf:resource="#hasParent" />
        <owl:allValuesFrom rdf:resource="#Human" />
    </owl:Restriction>
    ```
    
- **Notazione Logica Descrittiva (DL):**
    
    $\forall \text{hasParent} . \text{Human}$
    

**Implicazione Logica:** Questo assioma crea la classe di _"tutte le cose i cui genitori, se ne hanno, sono esclusivamente Umani"_. Attenzione a una peculiarità matematica (la verità vacua): un individuo che **non ha alcun genitore** soddisfa automaticamente questa restrizione e appartiene a questa classe anonima.

#### B. Restrizione Esistenziale (`owl:someValuesFrom`)

Definisce la classe degli individui che possiedono **almeno un** valore per una specifica proprietà che appartenga a una determinata classe.

- **Sintassi RDF/XML:**
    ```XML
    <owl:Restriction>
        <owl:onProperty rdf:resource="#hasParent" />
        <owl:someValuesFrom rdf:resource="#Physician" />
    </owl:Restriction>
    ```
    
- **Notazione Logica Descrittiva (DL):**
    
    $\exists \text{hasParent} . \text{Physician}$
    

**Implicazione Logica:** Questo assioma definisce la classe di _"chiunque abbia almeno un genitore che sia un Medico (Physician)"_. A differenza della restrizione universale, qui è obbligatorio che la relazione esista affinché l'individuo faccia parte della classe. Può avere anche genitori non medici, purché ne esista almeno uno medico.

#### C. Restrizione su Valore Specifico (`owl:hasValue`)

Definisce la classe degli individui che sono connessi tramite una certa proprietà a un **individuo specifico** o a un **letterale specifico** (non a un'intera classe).

- **Sintassi RDF/XML:**
    ```XML
    <owl:Restriction>
        <owl:onProperty rdf:resource="#hasParent" />
        <owl:hasValue rdf:resource="#clinton" />
    </owl:Restriction>
    ```
    
- **Notazione Logica Descrittiva (DL):**
    
    $\exists \text{hasParent} . \{\text{clinton}\}$ oppure $\text{hasParent} \ni \text{clinton}$
    

**Implicazione Logica:** Definisce estensionalmente l'insieme ristretto di individui che hanno esattamente "clinton" (l'istanza specifica) come genitore. Crea di fatto il concetto logico dei "figli di Clinton".

Queste classi anonime, basate su restrizioni, vengono poi tipicamente collegate ad altre classi dotate di nome tramite assiomi di equivalenza (`owl:equivalentClass`) o sussunzione (`rdfs:subClassOf`), permettendo al motore semantico di derivare automaticamente gerarchie e appartenenze complesse.

### 4. Descrizione tramite Restrizioni sulla Cardinalità 

Mentre `owl:allValuesFrom` o `owl:someValuesFrom` vincolano la classe di destinazione, le restrizioni di cardinalità definiscono una classe anonima basata sul **numero esatto, minimo o massimo di relazioni** che un individuo deve avere tramite una specifica proprietà.

**ATTENZIONE - Il dettaglio cruciale:** Le slide sottolineano giustamente che si parla di "valori _semanticamente_ diversi". Questo è un richiamo diretto alla **No Unique Name Assumption (NUNA)** vista in precedenza. Per il motore di inferenza, contare due URI non significa necessariamente contare due entità distinte, a meno che non sia esplicitamente dichiarato (tramite `owl:differentFrom`).

Analizziamo i tre costrutti:

#### A. Cardinalità Massima (`owl:maxCardinality`)

Definisce la classe di tutti gli individui che sono connessi a **non più di $N$** individui distinti tramite la proprietà specificata.

- **Sintassi RDF/XML:**
    ```XML
    <owl:Restriction>
        <owl:onProperty rdf:resource="#hasParent" />
        <owl:maxCardinality rdf:datatype="&xsd;nonNegativeInteger">2</owl:maxCardinality>
    </owl:Restriction>
    ```
    
- **Notazione in Logica Descrittiva (DL):**
    
    $\leq 2 \text{ hasParent}$
    
- **Implicazione Logica:** Definisce chi ha al massimo 2 genitori. Se nel sistema un individuo risulta avere 3 genitori con URI diversi, il _reasoner_ non darà subito errore. Prima, a causa della NUNA, cercherà di inferire che almeno due di quegli URI rappresentano in realtà la stessa persona (`owl:sameAs`). Darà errore (inconsistenza) solo se avevamo precedentemente dichiarato che quei 3 individui sono mutuamente diversi.
    

#### B. Cardinalità Minima (`owl:minCardinality`)

Definisce la classe di tutti gli individui che sono connessi ad **almeno $N$** individui distinti tramite la proprietà.

- **Sintassi RDF/XML:**
    
    ```XML
    <owl:Restriction>
        <owl:onProperty rdf:resource="#hasParent" />
        <owl:minCardinality rdf:datatype="&xsd;nonNegativeInteger">2</owl:minCardinality>
    </owl:Restriction>
    ```
    
- **Notazione in Logica Descrittiva (DL):**
    
    $\geq 2 \text{ hasParent}$
    
- **Implicazione Logica:** Qui entra in gioco la **Open World Assumption (OWA)**. Se definisci che un individuo ha questa restrizione, ma nel database locale è registrato un solo genitore, il sistema _non_ si lamenta. Semplicemente, deduce che il secondo genitore esiste da qualche parte nel mondo non ancora modellato.
    

#### C. Cardinalità Esatta (`owl:cardinality`)

È una scorciatoia sintattica (syntactic sugar). Definisce la classe degli individui che hanno **esattamente $N$** relazioni distinte. Logicamente, equivale all'intersezione tra `minCardinality N` e `maxCardinality N`.

- **Sintassi RDF/XML:** Sostituisce i tag precedenti con `<owl:cardinality>`.
    
- **Notazione in Logica Descrittiva (DL):**
    $= 2 \text{ hasParent}$
### 5. Operatori Booleani (Costrutti Insiemistici)

Poiché in Logica Descrittiva le classi non sono altro che insiemi matematici di individui, OWL ci permette di creare nuove classi combinando quelle esistenti attraverso le classiche operazioni della teoria degli insiemi (AND, OR, NOT).

Anche in questo caso, come per `owl:oneOf`, la sintassi RDF/XML utilizza le collezioni chiuse (`rdf:parseType="Collection"`) per elencare gli operandi, garantendo al motore logico che la lista sia esaustiva.

#### A. Intersezione (`owl:intersectionOf` - AND Logico)

Definisce una classe i cui membri sono **tutti e soli** gli individui che appartengono contemporaneamente a _tutte_ le classi indicate nella collezione.

- **Sintassi RDF/XML:**
    
    ```XML
    <owl:Class>
        <owl:intersectionOf rdf:parseType="Collection">
            <owl:Class rdf:about="#LandVehicle" />
            <owl:Class rdf:about="#SeaVehicle" />
        </owl:intersectionOf>
    </owl:Class>
    ```
    
- **Notazione in Logica Descrittiva (DL):**
    
    $\text{LandVehicle} \sqcap \text{SeaVehicle}$
    
- **Implicazione Logica:** È l'area di sovrapposizione nei diagrammi di Venn. Ad esempio, se unisci "Veicolo Terrestre" e "Veicolo Acquatico", ottieni la classe (qui anonima, ma potresti chiamarla `AmphibiousVehicle`) dei mezzi anfibi. Un individuo deve avere entrambi i `rdf:type` per farne parte.

![center|400](img/Pasted%20image%2020260507144911.png)

#### B. Unione (`owl:unionOf` - OR Logico)

Definisce una classe i cui membri appartengono ad **almeno una** delle classi indicate nella collezione.

- **Sintassi RDF/XML:**

    ```XML
    <owl:Class>
        <owl:unionOf rdf:parseType="Collection">
            <owl:Class rdf:about="#LandVehicle" />
            <owl:Class rdf:about="#SeaVehicle" />
        </owl:unionOf>
    </owl:Class>
    ```
    
- **Notazione in Logica Descrittiva (DL):**
    
    $\text{LandVehicle} \sqcup \text{SeaVehicle}$
    
- **Implicazione Logica:** Se dico che una patente è valida per `LandVehicle ⊔ SeaVehicle`, significa che un individuo che possiede un'auto (terrestre) è valido, un individuo che possiede una barca (acquatico) è valido, e chi li ha entrambi è altrettanto valido.

![center|400](img/Pasted%20image%2020260507144924.png)
#### C. Complemento (`owl:complementOf` - NOT Logico)

Definisce la classe costituita da tutti gli individui del dominio che **NON appartengono** a una certa classe.

- **Sintassi RDF/XML:**
    ```XML
    <owl:Class>
        <owl:complementOf>
            <owl:Class rdf:about="#Meat"/>
        </owl:complementOf>
    </owl:Class>
    ```
    
- **Notazione in Logica Descrittiva (DL):**
    
    $\neg \text{Meat}$
    
- **Implicazione Logica:** Nel diagramma di Venn, è tutto lo spazio esterno all'insieme specificato. Questo operatore è potentissimo ma va usato con cautela a causa della OWA: in un mondo aperto, se il sistema non sa se un ingrediente è "Carne" (`Meat`), non può dedurre automaticamente che appartenga a `¬Meat` (potrebbe essere carne ma semplicemente non è stato ancora dichiarato). Questo rende il ragionamento con i complementi computazionalmente molto complesso.

![center|400](img/Pasted%20image%2020260507144954.png)
## Assiomi sulle classi

Finora abbiamo visto come _costruire_ o _descrivere_ singole classi (usando restrizioni, unioni, intersezioni, ecc.). Ora dobbiamo capire come **mettere in relazione queste classi tra loro** per formare la vera e propria struttura logica (la tassonomia) dell'ontologia.

Per farlo, OWL utilizza gli **assiomi sulle classi**. Un assioma è una dichiarazione logica che il motore di inferenza assume come vera. Le slide ne presentano tre fondamentali: `rdfs:subClassOf`, `owl:equivalentClass` e `owl:disjointWith`.

Analizziamoli con il consueto rigore formale.
### Sussunzione (`rdfs:subClassOf`)

È l'assioma di base per creare gerarchie, ereditato direttamente da RDFS, ma in OWL DL assume una valenza logica molto più precisa. Stabilisce una relazione di **sottoinsieme** matematico.

- **Significato Logico:** Se dichiariamo che la classe A è sottoclasse di B ($A \sqsubseteq B$), stiamo affermando che **ogni istanza di A è necessariamente anche un'istanza di B**.
    
- **Sintassi e Flessibilità:** OWL espande enormemente il potere di `rdfs:subClassOf`. Non serve solo a collegare due nomi (es. "Cane" sottoclasse di "Animale"), ma può collegare un nome a una _descrizione complessa anonima_ (class expression).
    

**L'esempio del Vino Bianco:**

Vediamo un esempio eccellente:

```XML
<owl:Class rdf:ID="VinoBianco">
    <rdfs:subClassOf>
        <owl:Class>
            <owl:intersectionOf parseType="Collection">
                <owl:Class rdf:about="#Vino" />
                <owl:Restriction>
                    <owl:onProperty rdf:resource="#colore" />
                    <owl:hasValue rdf:datatype="&xsd;string">bianco</owl:hasValue>
                </owl:Restriction>
            </owl:intersectionOf>
        </owl:Class>
    </rdfs:subClassOf>
</owl:Class>
```

**Cosa significa in Logica Descrittiva?** $\text{VinoBianco} \sqsubseteq (\text{Vino} \sqcap \exists \text{colore} . \{\text{"bianco"}\})$

Qui stiamo dicendo: _"Tutto ciò che io definisco come VinoBianco è, di conseguenza, un Vino ed ha colore bianco"_.

**Attenzione però al limite della sussunzione:** è una freccia a senso unico (implicazione logica). Se nel sistema appare un individuo che sappiamo essere un Vino e di colore bianco, il reasoner **NON** lo classificherà automaticamente come `VinoBianco`. Perché? Perché la sussunzione dice solo quali sono le proprietà del Vino Bianco, ma non dà la definizione _necessaria e sufficiente_.

![center|300](img/Pasted%20image%2020260507151444.png)
### Equivalenza (`owl:equivalentClass`)

Per risolvere il limite appena descritto, usiamo l'equivalenza. Due classi sono equivalenti se contengono **esattamente le stesse istanze** (sono lo stesso insieme matematico).

- **Significato Logico:** $A \equiv B$. In Logica Descrittiva, l'equivalenza è semplicemente una doppia sussunzione: ($A \sqsubseteq B$) AND ($B \sqsubseteq A$).
    

**Rivediamo l'esempio del Vino Bianco:**

Se sostituiamo `<rdfs:subClassOf>` con `<owl:equivalentClass>` nello snippet precedente, la semantica cambia radicalmente.

```XML
<owl:Class rdf:ID="VinoBianco">
    <owl:equivalentClass>
        </owl:equivalentClass>
</owl:Class>
```

**Cosa significa ora?**

$\text{VinoBianco} \equiv (\text{Vino} \sqcap \exists \text{colore} . \{\text{"bianco"}\})$

Ora abbiamo dato una **definizione necessaria e sufficiente**. Non solo tutti i Vini Bianchi sono vini di colore bianco, ma **qualsiasi** individuo nel nostro database che sia riconosciuto come Vino e che abbia la proprietà `colore` uguale a "bianco", **verrà inferito (classificato automaticamente) dal reasoner come `VinoBianco`**. Questo è il vero potere del ragionamento automatico in OWL!

L'equivalenza è anche utilissima per allineare ontologie diverse, dichiarando che un URI di una tua ontologia è esattamente lo stesso concetto di un URI di un'ontologia esterna (es. `owl:equivalentClass rdf:resource="http://other.com/WhiteWine"`).

![center|500](img/Pasted%20image%2020260507151522.png)

### Disgiunzione (`owl:disjointWith`)

In un mondo aperto (OWA), non possiamo dare per scontato che due classi siano separate solo perché hanno nomi diversi. Se non diciamo nulla, per il reasoner un individuo potrebbe benissimo essere contemporaneamente un "Cane" e un "Gatto". L'assioma di disgiunzione serve proprio a impedirlo.

- **Significato Logico:** Se A è disgiunto da B, l'intersezione tra i loro insiemi è vuota ($A \sqcap B \equiv \bot$). Le due classi **non possono avere istanze in comune**.
    
**L'esempio della Biologia:**

Se vogliamo separare i Regni biologici, dobbiamo farlo esplicitamente:

```XML
<owl:Class rdf:ID="Animale">
    <owl:disjointWith rdf:resource="#Vegetale" />
    <owl:disjointWith rdf:resource="#Fungo" />
</owl:Class>

<owl:Class rdf:ID="Vegetale">
    <owl:disjointWith rdf:resource="#Fungo" />
</owl:Class>
```

**Implicazione Logica:** Questo costrutto è fondamentale per **trovare errori e inconsistenze**. Se per un qualsiasi motivo, a causa di dati errati o di inferenze a catena, il motore logico deduce che l'individuo "Pippo" ha sia `rdf:type Animale` sia `rdf:type Fungo`, il sistema si bloccherà segnalando un'**inconsistenza logica** (una violazione del vincolo di disgiunzione).

**Nota su OWL 1:** Come si vede dallo snippet, in OWL 1 per dichiarare che tre o più classi sono tutte reciprocamente esclusive, bisogna scrivere le disgiunzioni _a coppie_ (Animale-Vegetale, Animale-Fungo, Vegetale-Fungo). Questo può diventare verboso se le classi sono decine, ma in OWL 1 era l'unico modo formalmente corretto per farlo.

![center|400](img/Pasted%20image%2020260507151550.png)

## Caratteristiche delle Proprietà

Eccoci pronti ad esplorare un'altra delle potenzialità inferenziali di OWL: le **Caratteristiche delle Proprietà** (Property Axioms).

Mentre in RDFS potevamo solo definire gerarchie di proprietà (`rdfs:subPropertyOf`) e limitare il dominio o il range, OWL ci permette di definire il "comportamento matematico" delle relazioni. Quando diciamo al motore di inferenza che una proprietà possiede certe caratteristiche, gli stiamo fornendo le regole per creare nuovi archi (nuove triple) nel nostro grafo o per dedurre l'identità di alcuni nodi.

### Proprietà Transitive (`owl:TransitiveProperty`)

Questa caratteristica modella il classico ragionamento a catena.

- **Definizione Logica:** Se una proprietà $P$ è transitiva, e sappiamo che l'individuo $x$ è relazionato a $y$ tramite $P$ ($x P y$), e $y$ è relazionato a $z$ tramite $P$ ($y P z$), allora **il motore inferenziale dedurrà automaticamente che $x$ è relazionato a $z$ tramite $P$ ($x P z$)**.
    
- **Sintassi in RDF/XML:** Può essere definita direttamente o aggiungendo il tipo a una proprietà esistente.
    
    ```XML
    <owl:TransitiveProperty rdf:ID="parteDi" />
    
    <owl:ObjectProperty rdf:ID="parteDi">
        <rdf:type rdf:resource="&owl;TransitiveProperty" />
    </owl:ObjectProperty>
    ```
    
- **L'esempio geografico:** Si vede il grafo: `Roma --parteDi--> Lazio --parteDi--> Italia --parteDi--> Europa`. Grazie all'assioma di transitività, non c'è bisogno di scrivere a mano tutte le connessioni. Il reasoner dedurrà da solo le frecce tratteggiate: `Roma --parteDi--> Italia`, `Roma --parteDi--> Europa`, ecc.
    
- **Vincoli strutturali in OWL DL:** Per mantenere il ragionamento decidibile (per evitare calcoli infiniti), OWL DL impone una regola severa: **nessuna proprietà transitiva (o sua super-proprietà) può avere vincoli di cardinalità.** Immagina di dire che una proprietà è transitiva _e_ che può avere al massimo 1 valore: il sistema andrebbe in tilt matematico nel cercare di risolvere la catena.

![center|500](img/Pasted%20image%2020260507152115.png)

### Proprietà Simmetriche (`owl:SymmetricProperty`)

Modella le relazioni bi-direzionali, dove non c'è una gerarchia tra soggetto e oggetto.

- **Definizione Logica:** Se una proprietà $P$ è simmetrica, e l'individuo $x$ è relazionato a $y$ tramite $P$ ($x P y$), allora **il motore dedurrà automaticamente la relazione inversa, ovvero che $y$ è relazionato a $x$ tramite $P$ ($y P x$)**.
    
- **Sintassi in RDF/XML:**
    ```XML
    <owl:SymmetricProperty rdf:ID="vicino" />
    ```
    
- **L'esempio geografico:** Nel grafo si vede che `Italia --vicino--> Francia`. Poiché "vicino" è stata dichiarata simmetrica, il reasoner crea istantaneamente l'arco di ritorno tratteggiato: `Francia --vicino--> Italia`. È una freccia a doppio senso.
    
- **Nota sui domini/range:** Se una proprietà è simmetrica, il suo dominio e il suo range dovrebbero coincidere logicamente (es. una nazione è vicina a una nazione, non a un numero).

![center|500](img/Pasted%20image%2020260507152152.png)
### Proprietà Funzionali (`owl:FunctionalProperty`)

Questa è una caratteristica cruciale per la gestione dell'identità (NUNA) e della cardinalità, in quanto afferma che per ogni soggetto esiste **al massimo un** oggetto per quella proprietà.

- **Definizione Logica:** Se una proprietà $P$ è funzionale, significa che è "a valore singolo" (single-valued). Se troviamo nel database che $x P y$ e contemporaneamente troviamo che $x P z$, il motore di inferenza deduce necessariamente che **$y$ deve essere uguale a $z$ ($y = z$)**.
    
- **Sintassi in RDF/XML:**
    ```XML
    <owl:FunctionalProperty rdf:ID="produttore" />
    ```
    
- **L'esempio delle aziende:** Nel grafo vediamo un prodotto, `foo`. Il database contiene due triple: `foo --produttore--> company1` e `foo --produttore--> company2`.
    
    - **In RDFS:** Niente di strano, `foo` ha due produttori.
        
    - **In OWL (con `produttore` come funzionale):** Poiché la regola impone un solo produttore, il reasoner applica la OWA/NUNA. Dice: _"Non può avere due produttori diversi. Poiché non ho informazioni contrarie, deduco che `company1` e `company2` sono in realtà due nomi diversi per la stessa identica azienda"_. Genererà quindi l'arco logico `owl:sameAs` tra i due nodi.
        
    - **Quando c'è l'errore?** Come visto in precedenza, il sistema andrebbe in errore logico (inconsistenza) solo se avessimo precedentemente dichiarato in modo esplicito (tramite `owl:differentFrom`) che `company1` e `company2` sono due entità distinte.
        
- **Applicabilità:** A differenza della transitività e della simmetria (che si applicano solo alle `ObjectProperty` che collegano individui), le slide specificano un dettaglio tecnico importante: **anche le `DatatypeProperty` possono essere funzionali**. Ad esempio, la proprietà "codiceFiscale" (che punta a una stringa) è funzionale, perché una persona ha al massimo un codice fiscale. Se trovassi due stringhe diverse, andrei incontro a un'inconsistenza (le stringhe testuali non possono essere fuse con `owl:sameAs` come si fa con gli URI).

![center|500](img/Pasted%20image%2020260507152218.png)

### Proprietà Inverse (`owl:inverseOf`)

Spesso, nel linguaggio naturale e nella modellazione della conoscenza, descriviamo la stessa relazione da due prospettive diverse. `owl:inverseOf` serve a dire al motore logico che due proprietà distinte sono in realtà le due facce della stessa medaglia.

- **Definizione Logica:** Dire che una proprietà $P1$ è l'inversa di $P2$ significa che:
    
    $X \ P1 \ Y$ **se e solo se** $Y \ P2 \ X$
    
    In altre parole, se inverto il soggetto e l'oggetto di una tripla che usa $P1$, devo necessariamente usare $P2$ per mantenere il significato.
    
- **Sintassi in RDF/XML:** Nelle slide troviamo il classico esempio della genitorialità.
    ```XML
    <owl:ObjectProperty rdf:ID="hasChild">
        <owl:inverseOf rdf:resource="#hasParent" />
    </owl:ObjectProperty>
    ```
    
- **Implicazione Logica (Inferenza):** Se nel mio grafo inserisco l'asserzione `(Pippo, hasChild, Pluto)`, il _reasoner_ creerà automaticamente e immediatamente una nuova tripla di ritorno: `(Pluto, hasParent, Pippo)`.
    
- **Differenza con `owl:SymmetricProperty`:** Attenzione a non confonderle.
    
    - In una proprietà **simmetrica** (es. `vicinoDi`), il nome della proprietà rimane _lo stesso_ anche se inverti soggetto e oggetto (`Italia vicinoDi Francia` -> `Francia vicinoDi Italia`).
        
    - Con `owl:inverseOf`, stai collegando due proprietà con **nomi (URI) diversi** che hanno significati speculari.
        
### Proprietà Inversa Funzionale (`owl:InverseFunctionalProperty`)

Se la proprietà _Funzionale_ (vista in precedenza) serviva a identificare univocamente l'_oggetto_ di una relazione (dato un soggetto, c'è un solo oggetto possibile), la proprietà _Inversa Funzionale_ serve a identificare univocamente il **Soggetto**. In termini di database tradizionali, si tratta di definire una **Chiave Primaria (Primary Key)**.

- **Definizione Logica:** Se una proprietà $P$ è inversa funzionale, significa che per ogni oggetto $z$ esiste **al massimo un soggetto** che punta ad esso tramite $P$.
    
    Quindi, se sappiamo che $x \ P \ z$ e contemporaneamente $y \ P \ z$, il _reasoner_ deduce necessariamente che **$x$ e $y$ devono essere la stessa identica cosa ($x = y$)**.
    
- **Sintassi in RDF/XML:**
    ```XML
    <owl:InverseFunctionalProperty rdf:ID="capitaleDi" />
    
    <owl:ObjectProperty rdf:ID="capitaleDi">
        <rdf:type rdf:resource="&owl;InverseFunctionalProperty" />
    </owl:ObjectProperty>
    ```
    
- **L'esempio della Capitale:** Nelle slide c'è un grafo che mostra due triple:
    
    1. `Roma --capitaleDi--> Italia`
        
    2. `Caput --capitaleDi--> Italia`
        
    
    Poiché abbiamo dichiarato che `capitaleDi` è inversa funzionale, il ragionamento procede così: _"Una nazione (l'oggetto 'Italia') può essere il target di questa relazione da parte di un solo soggetto. Dato che vedo due soggetti diversi ('Roma' e 'Caput') che puntano entrambi a 'Italia' con questa proprietà, per la No Unique Name Assumption (NUNA) devo dedurre che 'Roma' e 'Caput' sono lo stesso nodo"_.
    
    Il sistema genererà quindi l'arco `owl:sameAs` tra Roma e Caput.
    
- **Uso pratico (Le Chiavi):** Questa proprietà è fondamentale nel Web Semantico per unire dati provenienti da database diversi. Se due database parlano di persone diverse, ma in entrambi trovo un nodo che ha la proprietà inversa funzionale "haCodiceFiscale" che punta allo stesso numero "RSSMRA...", il motore di inferenza fonderà (merge) i due nodi persona in uno solo, perché sa che non possono esistere due soggetti diversi con lo stesso codice fiscale.

![center|500](img/Pasted%20image%2020260507152812.png)