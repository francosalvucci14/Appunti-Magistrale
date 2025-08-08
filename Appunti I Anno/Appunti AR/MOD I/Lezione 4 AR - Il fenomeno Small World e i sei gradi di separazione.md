# Esperimento di Milgram

Lo psicologo sociale Stanley Milgram nel $1967$ condusse il seguente esperimento:
1) scelse una persona, un *destinatario*, alla quale doveva essere recapitata una lettere della quale lo stesso Milgram era il mittente
	1) l'obiettivo e Milgram erano molto distanti fra loro, immaginiamo come se fossero sulle coste opposte degli Stati Uniti
2) Milgram ha poi scelto a caso un insieme di **iniziatori** e ha consegnato ad ognuno di essi una copia della lettera
	1) ha anche fornito ad ogni iniziatore informazioni sul destinatario come: nome,cognome, indirizzo, occupazione, passatempi, etc..
3) Milgram ha quindi chiesto ad ogni **iniziatore** di fare in modo di far giungere la copia dela lettera in suo possesso al destinatario, senza però inviargliela direttamente con mezzi postali
4) Ogni iniziatore doveva scrivere il suo nome sulla lettera e , con l'obiettivo di giungere la lettera al destinatario **nel minor numero di passi possibile**, consegnarla a un suo ***diretto*** conoscente chiedendogli di ripetere le medesime azioni

Cosa ha osservato Milgram con questo esperimento?
1) il numero di lettere che hanno raggiunto il destinatario erano circa un terzo delle totali
2) le lettere che hanno raggiunto il destinatario lo hanno fatto, **in media**, in $6$ pasi
	1) I "famosi" **$6$ gradi di separazione**

In base all'esito dell'esperimento di Milgram, possiamo trarre due conclusioni:
1) In una rete sociale è presente una moltidudine di percorsi molto brevi, che connettono qualunque coppia di nodi - il così detto **fenomeno Small World**
2) Che i percorsi brevi non solo esistono, ma *possono essere trovati con facilità*
	1) ovvero, da nodi che non conoscono altro della struttura della rete se non i propri immediati vicini

Analizziamo queste due conclusioni

## 1) Una moltidudine di percorsi brevi

La domanda che ci poniamo è: quale spiegazione intuitiva possiamo trovare al fatto che in una rete sociale esistano tanti **shortest paths** fra una coppia di nodi?

Intuitivamente, possiamo vederla così:
- Io ho 100 amici
- ciascuno dei quali ha 100 amici
- ciascuno dei quali ha 100 amici, e così via
- Questo significa che il grafo delle relazioni di questo gruppo di persone contiene $10000$ percorsi di lunghezza $2$ da me ad altre persone, e $100000$ percorsi di lunghezza $3$ da me ad altre persone della rete
	- cioè, io sono collegato a mezzo di percorsi molto brevi a un sacco di gente
- E poichè posso ripetere questo ragionamento per qualunque altro individuo che popola la rete,ecco la spiegazione dell'esistenza di tanti percorsi brevi in una rete sociale

Bene, intuitivo, ma ovviamente non funzionale...

Infatti questo ragionamento non tiene conto della così detta **chiusura triadica** (della quale avremo modo di parare in seguito)
- ovvero, il ragionamento non tiene conto del fatto che in una rete sociale esistono tanti triangoli
- se una persona $A$ conosce $B,C$ allora è probabile che prima o poi anche $B,C$ si consceranno

Quindi, ritornando a prima, fra i 100 amici dei miei amici, si troveranno anche alcuni dei miei amici

E invece che avere una situazione tipo questa (che rappresenta la pure crescita **esponenziale** che produce una small world)

![[Pasted image 20250808101518.png|center|500]]

Avremo più una situazione simile a questa (che rappresenta il fatto che la chiusura triadica riduce la frequenza di crescita (**growth rate**))

![[Pasted image 20250808101632.png|center|500]]

Ciò premesso, ci proponiamo quindi di studiare un modello generativo di grafi aleatori che generi:
1) Small Worlds
2) Contenenti molte chiusure triadiche
### Il Modello Watts-Strogatz

Il modello proposto da **Watts-Strogatz** consiste in un grafo fissato deterministicamente ed un insieme di archi casuali

Il grafo fissato lo possiamo vedere come una griglia "arricchita", che corrisponde sostanzialmente ad un **Unit Disk Graph** (vedi [[Lezione 3 AR - Grafi Geometrici Aleatori, Reti Wireless e il problema del minimo raggio di trasmissione#^8b5ecc|Lezione 3]])

**Informalmente**: 
- I nodi sono punti di uno spazio metrico bidimensionale
- I nodi sono disposti sui punti a coordinate intere di un quadrato centrato nell'origine degli assi cartesiani
- Ogni nodo è collegato a ciascuno dei nodi vicini in orizzontale, verticale e diagonale

**Formalmente**:

Fissato $n\in\mathbb N$ abbiamo che $$V=\{(i,j):0\leq i\leq n\land0\leq j\leq n\}$$
e ciascun nodo $(i,j)$ con $0\lt i\lt n$ e $0\lt j\lt n$ è collegato ai nodi $$\{i,j-1\},\{i+1,j-1\},\{i+1,j\},\{i+1,j+1\},\{i,j+1\},\{i-1,j+1\},\{i-1,j\},\{i-1,j-1\}$$

Poi, fissando un valore $k$, ogni nodo sceglierà u.a.r $k$ nodi che diventeranno i suoi vicini

C'è da notare che più che una griglia su una superficie piana, dobbiamo pensare a una **griglia "appoggiata" su una superficie sferica**, che si "richiude" su se stessa e che chiamereo ***wrapped***

![[Pasted image 20250808103214.png|center|300]]

Analizziamo ora questo grafo generato dal modello di Watss-Strogatz

1) Possiamo individuare una sorta di dicotomia relazioni locali / relazioni a distanza soggiacente fra gli archi deterministici e quelli random
	1) gli archi della griglia, che costituiscono "l'ossatura fissa" del grafo, rappresentano le relazioni fra nodi "fisicamente" vicini - ovvero quelli le cui coordinate differiscono di poco
	2) gli archi random esprimono relazioni fra nodi "fisicamente" lontani
2) Possiamo ben immaginare che i nodi "fisicamente" vicini abbiano **più probabilità** di incontrarsi rispetto ai nodi "fisicamente" lontani
	1) È più probabile che i nodi "fisicamente" vicini abbiano più frequentazioni assidue, quelli lontani no
	2) Possiamo allora pensare agli archi della griglia come archi che rappresentano **relazioni forti (strong ties)**
	3) E gli archi random come archi che rappresentano **relazioni deboli (weak ties)**
3) I triangoli sono sempre presenti a livello locale e sono poco probabili fra gli archi random
	1) Confermando l'idea di cui al punto $2)$: infatti i triangoli si formano quando individui che hanno un amico comune si incontrano, e per due amici di uno stesso individuo, che vivono ai due capi opposti della Terra, è improbabile che abbiano molte occasioni di incontrarsi

Dunque il modello di Watts-Strogetz ha molti triangoli, come si riscontra nelle reti sociali

Rimane un'altra questione: sarà vero che coppie di nodi qualunque sono collegati da numerosi percorsi brevi?

A tal proposito, Watts e Strogatz hanno osservato che: se partiamo da un nodo $u$ e a partire da $u$ ci muoviamo, per un certo numero di passi, lungo gli archi random, poichè gli archi random sono distribuiti u.a.r nel grafo è molto improbabile che, in questo procedimento, tocchiamo due volte lo stesso nodo.

Ovvero, molto probabilmente, in $h$ passi abbiamo la possibilità di raggiungere $k^h$ nodi

