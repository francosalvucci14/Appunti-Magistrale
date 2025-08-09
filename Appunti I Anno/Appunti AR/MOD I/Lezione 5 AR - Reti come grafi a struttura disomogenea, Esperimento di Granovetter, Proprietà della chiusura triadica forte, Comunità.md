# Introduzione

Il materiale descritto qui si può trovare anche nel capitolo $3$ del libro e nella dispensa Communities (che useremo più avanti come appoggio)

Fin'ora abbiamo studiato grafi che modellano reti a livello statistico.

Così facendo, ci siamo disinteressati delle *peculiarità dei singoli nodi*, piuttosto abbiamo studiato proprietà che valevano *mediamente* per i nodi.

Da qui in poi "cambieremo" il punto di vista, andando ad analizzare la posizione dei singoli nodi all'interno della rete, per poter studiare:
- se è possibile evidenziare particolari strutture nella rete
- se tutti i nodi si trovano, grosso modo, nella stessa situazione all'interno della rete, oppure se vi sono differenze osservabili fra nodo e nodo
- e se i nodi possono trarre vantaggio (e di quale tipo) da queste differenze
# L'esperimento di Granovetter

Negli anni $'60$ il sociologo Mark Granovetter intervistò un gruppo di individui che avevano recentemente cambiato lavoro

Granovetter fece loro una serie di domande volte a capire in che modo erano venuti a conoscenza della possibilità di ottenere l'impiego che avevano ottenuto

Il risultato di tale esperimento fu che molti degli intervistati avevano avuto le informazioni, che li avevano condotti alla loro occupazione attuale, attraverso una comunicazione da parte di qualcuno che conoscevano (una specie di passa-parola, che può essere ben prevedibile)

Il fatto abbastanza inaspettato che emerse dalle sue interviste fu che spesso, l'informazione era arrivata da qualcuno che conoscevano superficialmente, non dagli amici più stretti

Allora l'esperimento di Gravenotter sembra suggerire che:
1) non è tanto la forza del legame quella che ha aiutato a trovare lavoro
2) **quanto il tipo di informazione che una relazione è capace di veicolare**

In effetti, pensandoci bene, i nostri più cari amici frequentano, grosso modo, gli stessi posti che frequentiamo anche noi (questo perchè si presuppone che abbiamo una serie di cose che ci accomunano parecchio). 

Così facendo, noi e i nostri amici abbiamo accesso alle stesse fonti di informazione

Invece, i nostri conoscenti frequentano posti diversi da quelli che frequentiamo noi, cosicchè hanno accesso a fonti di informazione diverse, e così facendo vanno ad ampliare il nostro "**raggio d'azione**"

## Bridges e Local Bridges

Se consideriamo il grafo $G=(V,E)$ che modella la rete, gli archi che "aumentano" le nostre informazioni sono quelli che ci collegano a regioni della rete *inaccessibili* ai nostri amici

Vale quindi la seguente definizione:

>[!definition]- Bridge
>Definiamo un **bridge** come un arco la cui rimozione disconnette la rete [^1]

D'altra parte, sappiamo che una rete contiene con buona probabilità componenti giganti densamente connesse, e dunque la presenza di bridge è poco probabile, pertanto possiamo "*rilassare*" la definizione precedente:

>[!definition]- Local Bridges
>Chiamiamo un arco **local bridges** se i suoi vicini non hanno vicini in comune, ovvero $$(u,v)\in E\text{ è local bridge se }N(u)\cap N(v)=\emptyset$$

Dato che, come abbiamo visto dall'esperimento, spesso l'informazione arriva da qualcuno conosciuto solo superficialmente (e quindi no da amici stretti), possiamo riconoscere $2$ tipi di relazione, all'interno di una rete sociale
- **relazioni forti**: quelle che ci collegano agli amici stretti
- **relazioni deboli**: quelle che ci collegano a semplici conoscenti

Conseguentemente, possiamo modellare una rete del genere mediante un grafo $G$ in cui gli archi sono partizionati in due sottoinsiemi:
- **archi forti** (**strong ties**)
- **archi deboli** (**weak ties**)

Quindi, avremo che $$G=(V,S\cup W),\quad S\cap W=\emptyset$$
Come ha dimostrato Granovetter, gli archi deboli veicolano informazioni alle quali non avremmo accesso tramite gli archi forti: e questa viene chiamata **forza degli archi deboli**

Detto questo, se c'è una relazione fra i nodi $a,b$ e una relazione fra $a,c$ (quindi sia $(a,b)$ che $(a,c)$ sono **archi forti**), **allora è probabile che prima o poi si creerà anche l'arco $(b,c)$**, vale a dire, si andrà a creare la vecchia ***chiusura triadica*** (incontrata nel fenomeno Small World)

L'esistenza di chiusure triadiche ci impone che, per descrivere queste reti, abbiamo bisogno di grafi dinamici[^2]

Alla base della creazione di chiusure triadiche possiamo individuare ragioni di:
- *opportunità* di incontrarsi
- *incentivo* a stringere una nuova relazione
- *fiducia*

Lasciamo ora che la rete evolva, ovvero che si vadano a formare man mano tutti i triangoli, fino a raggiungere una configurazione stabile (ovvero una configurazione in cui la rete non cambia più nel tempo)

Cosa possiamo dire della struttura del grafo $G=(V,S\cup W)$ corrisponde a una rete in una configurazione stabile? 
La risposta è che, probabilmente, tutti i triangoli possibili si sono formati

Definiamo ora la **proprietà di chiusura triadica forte**

>[!definition]- Proprietà di Chiusura Triadica Forte (STCP)
>Sia $G=(V,S\cup W)$; un nodo $u$ soddifa **STCP** se, per ogni coppia di archi forti incidenti a $u$, i loro estremi sono collegati da un arco. 
>Formalmente vale che:
>$$u\in V\text{ soddisfa SCTP se }\forall(u,v)\in S\left[(v,z)\in S\cap W\right]$$
>$G$ soddisfa la SCTP se tutti i suoi nodi la soddisfano

### STCP e Local Bridges

Vale quindi il seguente teorema

>[!teorem]- Teorema
>Sia $G=(V,S\cup W)$; se un nodo $u$ soddisfa SCTP, e se esistono due nodi distinti $x,z:(u,x)\in S,(u,z)$ è local bridge, allora $(u,z)\in W$

**dimostrazione**

Poichè l'arco $(u,z)$ è local bridge, allora per definizione deve valere che $N(u)\cap N(z)=\emptyset$

Se $(u,z)\in S$ allora, poichè $(u,x)\in S$ e soddisfa SCTP, dovrebbe valere che $(x,z)\in S\cup W$, e quindi $x\in N(u)\cup N(z)$, ma di conseguenza $N(u)\cup N(z)\neq\emptyset$ - contraddizione $\blacksquare$

Questo teorema mostre come **una proprietà globale (essere local bridge) si riflette in una proprietà locale (essere un weak ties)** 
- essere weak ties è proprietà **locale**: un nodo sa da solo se un suo vicino è un amico o un conoscente
- essere local bridge è una proprietà **globale**: un nodo deve chiedere a tutti i suoi vicini se qualcuno di loro conosce un suo conoscente per sapere se è un local bridge

In effetti, nell'esperimento di Granovetter, i waek ties erano anche local bridge (in quanto portatori di informazione)

Con il passare del tempo, una chiusura triadica dopo l'altra, si andrà a formare nella rete **un gruppo di nodi fortemente coeso**, con un elevato grado di interconnessione fra i nodi che lo compongono.

Questo gruppo coeso prende nome di **cluster/comunità**

La domanda ora è, quand'è che possiamo dire che un gruppo di nodi è *abbastanza* coeso per poterlo definire una comunità?

## Comunità e coefficiente di clustering



[^1]: segue dall'esperimento Granovetter che i bridge sono gli archi che hanno maggiore "valore informativo"

[^2]: grafo dinamico: grafo che evolve nel tempo

