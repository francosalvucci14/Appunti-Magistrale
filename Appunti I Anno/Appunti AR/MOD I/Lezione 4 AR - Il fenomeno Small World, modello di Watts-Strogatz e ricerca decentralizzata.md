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

Il ragionamento di Watts-Strogatz è basato su considerazioni intuitive, successivamente Bollobas-Chung (1988) hanno formalmente dimostrato questo punto, e hanno anche individuato la lunghezza media degli shortest paths nei grafi generati in accordo al modello Watts-Strogatz

Il ragiuìonamento intuitivo di Watts-Strogatz può essere ripetuto su un modello in cui è presente di gran lunga meno casualità: infatti, è sufficiente che **soltanto da un nodo su $k$ partano archi random** e che, inoltre, **da tale nodo parta un solo arco random**

Vediamolo con un esempio:
- raggruppiamo quadrati di $k\times k$ nodi della griglia in "città", dove una città ha uno e uno solo arco random uscente
- ripetiamo il ragionamento di cui sopra a livello di "città" (non più di singolo individuo): in $h$ passi possiamo giungere in $k^h$ città
- Una volta dentro la città, ci muoviamo attraverso gli archi della griglia

Possiamo quindi concludere che **poca casualità è sufficiente per avere tanti shortest paths**

## 2) Percorsi brevi facili da trovare

Consideriamo ora la seconda questione che abbiamo riscontrato con l'esperimento di Milgram

Mettiamoci nella casistica di essere il nodo $u$ in un grafo di Watts-Strogatz.

Vogliamo inviare un messaggio ad una certa destinazione $v$ , di cui però **conosciamo solo le coordinate** (e da esse sappiamo che $u$ e $v$ sono molto distanti)
Naturalmente, vorremo che il messaggio arrivi il più velocemente possibile, ovvero cerchiamo di fare in modo che il messaggio venga consegnato attraverso uno shortest path che collega $u$ (noi) a $v$

Il problema è che $u$ conosce solo i suoi contatti, ovvero i suoi vicini nella rete (tutti i nodi $x:x\in N(u),N(u)=\text{vicinato di u}$)

Cosa facciamo? Semplice, facciamo tante copie del messaggio quanti sono i nostri vicini e mandiamo una copia a ciascuno dei vicini

Pur volendo non possiamo fare altro, dato che **conoscere l'indirizzo dela destinazione non ci aiuta**
- si potrebbe pensare di scegliere, fra tutti i nostri vicini quello le cui coordinate sono più prossime a quelle di $v$, ma la casualità dei *weak ties* potrebbe far sì che, invece, un vicino che al momento appare peggiore ha un arco random che lo collega direttamente a $v$...

Vediamo un esempio di questa situazione

![[Pasted image 20250808113714.png|center|350]]

In figura abbiamo che:
- $s$ deve inviare un messaggio a $d$
	- fra i vicini di $s$, il più vicino a $d$ *sulla griglia* è $a$
		- perchè $b$, sempre *sulla griglia*, è più lontano di $a$ da $d$
	- questo è tutto ciò che $s$ sa
- quindi, $s$ inoltra il messaggio ad $a$, che dovrà seguire i nodi della griglia per giungere a $d$
- se $s$ avesse inoltrato il messaggio a $b$, allontanandosi momentaneamente da $d$, avrebbe raggiunto $d$ in soli $3$ passi !

Ritornando al discorso di prima, abbiamo detto quindi che generiamo una copia del messaggio per ogni vicino di $u$ ($|N(u)|$ è la max. $8-9$ non so perchè) e le mandiamo ai rispettimi destinatari, i quali sono costretti ad eseguire la nostra stessa operazione, in quanto anche loro non conoscono nulla della rete.

Così facendo, dopo $h$ passi circoleranno nel grafo $\approx 7^h$ copie del messaggio

Tecnicamente parlando, per spedire un messaggio da un nodo $u$ ad un nodo $v$, è stato utilizzato un **flooding**

Però cosa c'è di diverso dall'esperimento di Milgram? Li non circolavano $\approx 7^h$ copie del messaggio, ma solo tanti messaggi quanti ne aveva creati Milgram (ovvero i messaggi **non aumentavano** ad ogni passo). 

Eppure anche i partecipanti all'esperimento di Milgram erano a conoscenza solo dei propri vicini e dell'indirizzo del destinatario, esattamente le stesse informazioni del modello di Watts-Strogatz, ma allora cosa manca a noi?

Evidentemente, il modello di Watts-Strogatz non ***riesce a descrivere*** qualche caratteristica di una rete sociale che rende possibile la ricerca di Milgram

La risposta a questo quesito è che sostanzialmente, i partecipanti all'esperimento di Milgram, hanno applicato un algoritmo di ricerca specifico, chiamato **algoritmo di ricerca decentralizzata** (o **ricerca miope**)

Un algoritmo di **ricerca decentralizzata** (o ricerca miope) è tale che:
- ciascun nodo non conosce della rete altro che i propri vicini (oltre al target)
- i nodi non comunicano in alcun modo se non nell'invio del messaggio da consegnare

Osserviamo: probabilmente, ad ogni passo, un individuo inoltrata la copia della lettera in suo possesso a quello fra i suoi contatti che stimava essere "più vicini possibile" al destinatario:
- dove con "più vicino" intendiamo vicino secondo metriche diverse quali: più vicino geograficamente, rispetto alla posizione lavorativa, rispetto agli interessi culturali, etc..

Allora, la struttura della rete ha qualche caratteristica che fa sì che "inoltrare al più vicino" funziona bene:
- in qualche modo, la struttura della rete garantisce che, se ad un passo sono nel nodo $u$ e invio al nodo $v$, allora fra gli amici di $v$ c'è (probabilmente) qualcuno **molto** più vicino di $u$ alla destinazione
- la struttura quindi garantisce che ad ogni passo mi avvicino alla destinazione,e che probabilmente ci sono ***tanti passi*** in cui la distanza della estinazione ***diminusice drasticamente***

Riconsideriamo quindi il modello di Watts-Strogatz
- certamente, ciascun nodo ha un vicino sulla griglia più vicino di se alla destinazione
- d'altra parte, se seguiamo un percorso costituito di soli archi della griglia, impieghiamo un sacco di passi per giungere a destinazione - $O(\sqrt{n})$ passi
- allora, se vogliamo trovare un percorso breve dobbiamo usare archi random

C'è un piccolo problema, ovvero non c'è garanzia che, in un grafo di Watts-Strogatz, usando la regola "invia al tuo vicino che è il più vicino alla destinazione" incontreremo una seria di archi random in modo tale che in un piccolo numero di passi giungeremo a destinazione.

In effetti, è stato dimostrato che nel modello Watts-Strogatz la ricerca decentralizzata, di un percorso da $s$ a $t$, individua mediamente un percorso più lungo di uno shortest path

Questo perchè nel modello Watts-Strogatz l'estremo di un arco random uscente da un nodo è scelto u.a.r fra tutti gli altri nodi.

Gli archi random non tengono conto in alcun modo di quanto sono "vicini" i nodi che congiungono, detto altrimenti, **gli archi random sono troppo random**

Analizziamo quindi un modello *corretto* per la ricerca decentralizzata

### Un modello per la ricerca decentralizzata

Vogliamo definire un modello generativo a cui corrispondano grafi che:
- contengono molti triangoli
- nei quali esistono molti shortest paths fra le coppie di nodi
- e nei quali **trovare gli shortest paths mediante ricerca decentralizzata sia possibile**

Danl nostro ragionamento precedente, possiamo ben pensare che, per soddisfare l'ultimo punto, è necesario che gli archi random siano scelti in modo da tener conto di quanto sono "vicini" i nodi che congiungono

Il nostro nuovo modello è ancora basato su un'ossatura deterministica, ovvero la stessa griglia arricchita e wrapper di Watss-Strongatz, e da ogni nodo esce un arco random.

La cosa che cambia è che ora, la probabilità che l'arco uscente dal nodo $u$ sia $(u,v)$ è inversamente proporzionale alla distanza, *sulla griglia*, dei nodi $u,v$, quindi avremo che:
$$Pr((u,v)\in E)=\frac{1}{Z_u}\cdot \frac{1}{d(u,v)^q}$$
dove:
- $d(u,v)$ indica la distanza di uno shortest path fra $u$ e $v$ **sulla griglia** (ovvero percorso che non contiene archi random)
- $Z_u$ indica un fattore di **normalizzazione**
	- dato che da ogni nodo deve uscire un solo arco random, deve valere che: $$\sum\limits_{v\in V\setminus\{u\}}Pr((u,v)\in E)=1\implies\sum\limits_{v\in V\setminus\{u\}}\frac{1}{Z_u} \frac{1}{d(u,v)^q}=1\implies Z_u=\sum\limits_{v\in V\setminus\{u\}}\frac{1}{d(u,v)^q}$$
	- Poichè la griglia wrapped è simmetrica, vale che il fattore $Z_u$ ha lo stesso valore per ogni nodo $u$, quindi indicheremo come fattore di normalizzazione il valore $Z$
- $q$ indica il parametro chiamato **esponente di clustering**
	- per ogni valore di $q$ otteniamo un modello diverso, con $q=0$ ri-otteniamo Watts-Strogatz
	- In generale, gli archi random sono "troppo random" quando $q$ è piccolo, viceversa quando $q$ è grande

Naturalmente abbiamo visto che con alcuni valori di $q$ la ricerca decentralizzata funziona meglio, e con altri peggio
- ad esempio con $q=0$ abbiamo visto poc'anzi che non funziona per niente.

Quello che vogliamo provare è che esiste una scelta di $q$ che rende efficiente la ricerca decentralizzata, ovvero permette di trovare percorsi la cui lunghezza non è troppo lontanta da quella degli shortest paths.

Anzi, quello che cerceremo è che esiste **un valore di $q$ ottimale** per la ricerca decentralizzata

**Nel caso in cui la componente deterministica del grafo è una griglia (wrapped) bidimensionale** allora l'esponente di clustering ottimale è $q=2$

In generale, se la componente deterministica del grafo è una griglia (wrapped) $d$-dimensionale, ovvero i nodi sono immersi nello spazio $\mathbb R^d$, allora l'esponente di clustering ottimale è $q=d$

Ripensiamo all'esperimento di Milgram:
- se il destinatario della lettera che Milgram consegna al newyorkese Pippo vive all'altro capo del mondo rispetto a Pippo, diciamo a Roma Garbatella, Pippo cerca fra i suoi amici qualcuno che vive in Europa
- Pippo questo amico ce l'ha, si chiama Pluto e vive a Mosca
- Pluto cerca qualcuno che viva in Europa Occidentale, e così la lettera finisce a Parigi
- Poi a Milano (Italia), Perugia (Italia Centrale), Latina (Lazio), Roma Centocelle, Roma Garbatella (Destinazione)

Il tragitto della lettera quindi segue, grosso modo, uno schema a "scale di riduzione"
- prima viaggia da un continente all'altro, poi all'interno del continente, poi all'interno della nazione,della regione e infine della città

Formalizziamo ora quello che abbiamo osservato in questo momento
#### Casistica $q=2$

Fissiamo un nodo $u$ e partizioniamo i nodi rimanenti per blocchi definiti in base alla distanza da $u$: i nodi a distanza compresa fra $2,4$, i nodi a distanza $4,8$,$\dots$, i nodi compresi a distanza $2^{h},2^{h+1}$

Il numero di nodi nel blocco $2^{h-1}-2^h$ è $$\approx\pi(2^{h+1})^2-\pi2^{2h}=\pi 2^{2h}(4-1)=3\pi 2^{2h}$$
è quindi **proporzionale a $2^{2h}$** 

Scelto ora $v$ nel blocco $2^{h-1}-2^h$ , la probabilità che l'arco random uscente da $u$ sia $(u,v)$ **è proporzionale a $\frac{1}{2^{2h}}$**

Allora, la probabilità che l'arco random uscente da $u$ cada nel blocco $2^{h-1}-2^h$ è **indipendente da $h$**, e quindi indipendente da quale blocco si stia considerando.

Di conseguenza, la probabilità di raggiungere un nodo a distanza $2,4,64,1024,\text{etc..}$ è la stessa

Questo significa che i **weak ties** sono distribuiti uniformemente su tutte le scale di risoluzione, e questo fa si che, anche se per un certo numero di passi occorre utilizzare gli archi della griglia [^1], non occorreranno molti passi prima di arrivare ad un nodo il cui arco random diminuisce ***drasticamente*** la distanza dall'obiettivo

E ora, dopo l'intuizione, l'ottimalità di $q=d$ nel caso della $d$-dimensionalità non ci resta che dimostrarla formalmente
#### Prestazioni della ricerca miope nel modello (caso grafi ad anello, $q=d=1$)

Analizziamo formalmente le prestazioni della ricerca miope nel modello descritto solo nella casistica $d=1$
- perchè ovviamente è più facile, anche se la generalizzazione ad altre dimensione è basata sugli stessi argomenti

La topologia di grafo che stiamo considerando è: grafo ad anello, il quale sono aggiunti archi random, in accordo al modello descritto in precedenza

Così facendo il coefficiente di clustering risulterà essere $q=1$

![[Pasted image 20250808172452.png|center|250]]

Formalmente, consideriamo un grafo $G$ dove:
- $V=[n]$
- $\{(i,i+1):1\leq i\lt n\}\cup\{(n,1)\}\subseteq E$ 

Al quale vengono aggiunti archi random: $$\forall u,v\in V: Pr((u,v)\in E)=\frac{1}{Z} \frac{1}{d(u,v)}$$
Osserviamo che, in questa casistica, per ogni $u\in V$ abbiamo che:[^2]
$$Z=\sum\limits_{v\in V\setminus\{u\}} \frac{1}{d(u,v)}=2\sum\limits_{1\leq h\leq \frac{n}{2}} \frac{1}{h}\leq2\sum\limits_{h=1}^\infty \frac{1}{h}=2\ln(n)$$
Scegliamo poi, u.a.r, due nodi $s,t\in G$, e utilizziamo l'algoritmo di ricerca decentralizzata per calcolare un percorso da $s$ a $t$

Indichiamo con $X$ la v.a che denota la lunghezza di tale percorso, allora vale il seguente teorema

>[!teorem]- Teorema
>$$\mathbb E[X]\in O(\ln^2(n))$$

Per fissare le idee, visualizziamo l'esecuzione dell'algoritmo di ricerca decentralizzata che costruisce in $G$ un percorso $s,t$ come segue:
- inizialmente $s$ possiede una copia della lettera
- al passo $1$ la trasmette ad un suo vicino (ovvero il più prossimo alla destinazione)
- al passo $2$ il nodo che ha ricevuto la copia al passo $1$ ri-esegue la stessa identica operazione di prima, e così via fino a che la lettera non raggiunge il nodo $t$

Suddividiamo in fasi il processo di trasmissione della lettera da un nodo ad un'altro

Durante la fase $j$ la lettera è in possesso di un nodo $u$ tale che $$\frac{d(s,t)}{2^{j+1}}\lt d(u,t)\leq \frac{d(s,t)}{2^j}$$

in modo da far iniziale il processo con la fase $0$

Dato che $d(s,t)\leq\frac{n}{2}$ e ad ogni fase si dimezza la distanza fra il nodo che possiede la lettera e $t$, allora **il numero di fasi risulterà essere $\leq\log_2(n)$**

Indichiamo ora con $X_j$ la durata della $j$-esima fase ($X_j$ è il num. di nodi che entrano in possesso della lettere durante la fase $j$)

Allora vale che $X=\sum\limits_{1\leq j\leq\log_2(n)}X_j$ e $\mathbb E[X]=\sum\limits_{1\leq j\leq\log_2(n)}\mathbb[X_j]$

Per dimostrare il teorema, è quindi sufficiente dimostrare che $$\forall j,\mathbb[X_j]\in O(\ln(n))$$
Ovviamente dimostriamolo:

Supponiamo di trovarci nel nodo $v$ durante la fase $j$: allora vale che $\frac{d(s,t)}{2^{j+1}}\lt d(v,t)\leq \frac{d(s,t)}{2^j}$

La fase $j$ termina sicuramente se esiste un nodo $z$ tale che:
- $(v,z)\in E$
- $d(z,t)\leq\frac{d(v,t)}{2}$, perchè $d(z,t)\leq\frac{d(v,t)}{2}\leq \frac{1}{2}\frac{d(s,t)}{2^j}$

Quindi abbiamo che:
$$\begin{align}Pr(\text{termina fase j})&=Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(s,t)}{2^{j+1}}\right)\\&\geq Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(v,t)}{2}\right)\end{align}$$[^3]

Indichiamo con $\mathcal I$ l'insieme dei nodi che distano da $t$ non più della metà di quanto dista $v$ da $t$
Formalmente:
$$\mathcal I=\left\{u\in V:d(u,t)\leq\frac{d(v,t)}{2}\right\}$$
Allora vale che:
$$\begin{align*}
Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(v,t)}{2}\right)&=Pr(\exists z\in\mathcal I:(v,z)\in E)\\&=Pr(\exists z\in\mathcal I:(v,z)\text{ è arco dell'anello o random})\\&=\sum\limits_{z\in\mathcal I}Pr(\exists z\in\mathcal I:(v,z)\text{ è arco dell'anello o random})\\&\geq\sum\limits_{z\in\mathcal I}Pr((v,z)\text{ è random})\\
\end{align*}
$$

SIa $z\in\mathcal I$, allora vale che: 
$$d(v,z)\leq d(v,t)+d(t,z)=d(v,t)+d(z,t)\leq d(v,t)+\frac{d(v,t)}{2}=\frac{3d(v,t)}{2}$$
Allora, per ogni $z\in\mathcal I$ vale che:
$$\begin{align*}
Pr((v,z)\text{ è random})&= \frac{1}{Z} \frac{1}{d(v,z)}\geq \frac{1}{Z} \frac{2}{3d(v,t)}\\&\geq \frac{1}{2\ln(n)} \frac{2}{3d(v,t)}\quad(\text{perchè }Z\leq2\ln(n))\\&= \frac{1}{3d(v,t)\ln(n)}
\end{align*}$$
Allora, concludiamo dicendo che:
$$Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(v,t)}{2}\right)\geq\sum\limits_{z\in\mathcal I} \frac{1}{3d(v,t)\ln(n)}= \frac{1}{3d(v,t)\ln(n)}|\mathcal I|$$

Rimane "solamente" da valutare $|\mathcal I|$

Siano $v_{sx},v_{dx}$ i due nodi in $\mathcal I$ a distanza **massima da $t$**, allora vale che $$d(v_{sx},t)=d(v_{dx},t)=\left\lfloor\frac{d(v,t)}{2}\right\rfloor$$[^4]

Siano poi $v_{sx1},v_{dx1}$ i due nodi adiacenti a $t$ (rispettivamente a sx e dx), allora vale che $\mathcal I$ contiene:
- il nodo $t$
- tutti i $\left\lfloor\frac{d(v,t)}{2}\right\rfloor$ nodi da $v_{sx}\to v_{sx1}$
- tutti i $\left\lfloor\frac{d(v,t)}{2}\right\rfloor$ nodi da $v_{dx}\to v_{dx1}$

![[Pasted image 20250809100827.png|center|150]]

Di conseguenza, abbiamo che $$|\mathcal I|=1+\left\lfloor\frac{d(v,t)}{2}\right\rfloor+\left\lfloor\frac{d(v,t)}{2}\right\rfloor\geq 1+\frac{d(v,t)-1}{2}+\frac{d(v,t)-1}{2}=d(v,t)$$
Concludendo, abbiamo che 
$$Pr(\text{fase j termina})\geq\frac{1}{3d(v,t)\ln(n)}d(v,t)= \frac{1}{3\ln(n)}$$

**Ora ci resta solo da dimostrare che $\forall j,\mathbb E[X_j]\in O(\ln(n))$**

La prob che la fase $j$ *non* termina è $\leq 1- \frac{1}{3\ln(n)}$, allora 
$$Pr(X_j\geq h)=Pr(\text{fase j *non* termina dopo h passi})\leq \left[1- \frac{1}{3\ln(n)}\right]^h$$
Calcoliamo ora $\mathbb E[X_j]$ (useremo la definizione formale di valore atteso di una v.a, vedi corso PROB2) (io non ho voglia di fare tutti i calcoli del cazzo)

$$\begin{align*}
\mathbb E[X_j]&=1\cdot Pr(X_j=1)+2\cdot Pr(X_j=2)+\dots+ \frac{n}{2}\cdot Pr\left(X_j=\frac{n}{2}\right)\quad\left(d(s,t)\leq \frac{n}{2}\right)\\&=\sum\limits_{1\leq h\leq \frac{n}{2}}Pr(X_j\geq h)\leq\sum\limits_{1\leq h\leq \frac{n}{2}}\left[1- \frac{1}{3\ln(n)}\right]^h\\&\leq\sum\limits_{h\geq0}\left[1- \frac{1}{3\ln(n)}\right]^h=\frac{1}{1-\left[1- \frac{1}{3\ln(n)}\right]}=3\ln(n)
\end{align*}$$
**Concludiamo il tutto**: (ricordando che il num. di fasi è pari a $\log_2(n)$)
$$\mathbb E[X]=\sum\limits_{j=1}^{\log_2(n)}\mathbb E[X_j]\leq\sum\limits_{j=1}^{\log_2(n)}3\ln(n)=\log_2(n)3\ln(n)\in O(\ln^2(n))\quad\quad\blacksquare$$
Come Volevasi Dimostrare (porco di dio)

# Perchè $q=d$ funziona bene in $\mathbb R^d$

Gli "ingredienti" che permettono di dimostrare che la ricerca decentralizzata si comporta "bene" nell'anello sono:
1) fissato $d$, il num. di nodi a distanza (al più) $d$ dalla destinazione $t$ sono, all'incircà, $d$
2) il fattore di normalizzazione è $Z\leq 2\ln(N)$

Questi due "ingredienti" permettono di dimostrare che, trovandoci in un nodo $v$ a distanza $d$ da $t$, la probabilità che $v$ abbia un vicino $z$ a distanza $\leq \frac{d}{2}$ da $t$ è proporzionale a $\frac{1}{\ln(n)}$ **indipendentemente da $d$**, infatti ricordiamo che
$$Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(v,t)}{2}\right)\geq\frac{1}{3d(v,t)\ln(n)}|\mathcal I|= \frac{1}{3\ln(n)},\quad|\mathcal I|=d(v,t)$$

Considerazioni analoghe possono essere fatte nel **caso bidimensionale con $q=2$**
1) in questo caso, $|\mathcal I|=\alpha d(v,t)^2$ per qualche costante $\alpha$ (area del quadrato di lato $\approx d(v,t)$)
2) ora, $Z=\sum\limits_{v\in V\setminus\{u\}} \frac{1}{d(v,t)^2}$ e si può dimostrare che $Z\leq\beta\ln(n)$ per qualche costante $\beta$
3) Allora: $$Pr\left(\exists z\in V:(v,z)\in E\land d(z,t)\leq\frac{d(v,t)}{2}\right)\geq\sum\limits_{z\in\mathcal I}\frac{1}{Zd(v,t)^2}\geq\frac{4}{Z9d(v,t)^2}|\mathcal I|\geq\frac{4\alpha}{9\beta\ln(n)}$$
E come si può vedere, anche nel caso $q=d=2$ la probabilità che $v$ abbia un vicino a distanza $\leq \frac{d}{2}$ da $t$ è proporzionale a $\frac{1}{\ln(n)}$ indipendentemente da $d$

Allo stesso modo, possiamo fare considerazioni analoghe anche per $d\gt2$
# Perchè $q\neq d$ funziona male in $\mathbb R^d$

Cerchiamo ora di capire perchè il nostro modello, nel caso $q\neq d$ (ed. es. $d=1,q=0$), mal si presta alla ricerca decentralizzata[^5]

La probabilità che l'arco random uscente dal nodo $u$ sia $(u,v)$, in questo caso, è 
$$Pr((u,v)\in E)=\frac{1}{Z} \frac{1}{d(u,v)^0}=\frac{1}{Z}$$
Ma, dato che questa quantità deve essere una distribuzione di probabilità, ovvero deve valere che $\sum\limits_{v\in V\setminus\{u\}}Pr((u,v)\in E)=1$, allora deve necessariamente valere che 
$$\sum\limits_{v\in V\setminus\{u\}} \frac{1}{Z}=1\implies Z=\frac{1}{n-1}$$
Da cui otteniamo che la prob. che l'arco random uscente dal nodo $u$ sia $(u,v)$ è:
$$Pr((u,v)\in E)= \frac{1}{n-1}$$

Come abbiamo già osservato, nel caso "anello e $q=1$" è "facile" entrare in regioni del grafo contenenti nodi sempre più vicini a $t$, ovvero gli insiemi $\mathcal I$

Mostriamo ora (molto informalmente eh, non vi spaventate dio porco) che nel caso "anello e $q=0$" è "difficile" entrare nell'insieme $$R=\{u\in[n]:d(u,t)\leq\sqrt{n}\}$$
Scegliamo $t$, e poi scegliamo $s\not\in R$

Allora vale che: 
$$\forall u\in R\land\forall v\in[n]\setminus R:Pr((v,u)\in E)\gt \frac{1}{n}$$[^6]

Di conseguenza $$\forall v\not\in R: Pr(\exists u\in R:(v,u)\in E)\gt\frac{|R|}{n}=\frac{2\sqrt{n}}{n}=\frac{2}{\sqrt{n}}$$
Sia ora $Y$ la v.a che rappresenta il num. passi per raggiungere da $s$ un qualuque nodo in $R$, allora vale che:
$$\begin{align*}
&Pr(Y\geq h)\lt\left(1-\frac{2}{\sqrt{n}}\right)^h\\&\mathbb E[Y]=\sum\limits_{h\geq0}Pr(Y\geq h)\leq\sum\limits_{h\geq0} \left(1-\frac{2}{\sqrt{n}}\right)^h=\frac{1}{1-\left(1-\frac{2}{\sqrt{n}}\right)}=\frac{\sqrt{n}}{2}
\end{align*}$$
che è **esponenzialmente più grande di** $\mathbb E[X]\in O(\ln^2(n))$ del caso $q=1$

Quindi, per entrare nella regione $R$ servono mediamente $\frac{\sqrt{n}}{2}$ passi.
Vediamo quanti ne servono per entrare nella regione $$R_2=\left\{u\in[n]:d(u,t)\leq\frac{\sqrt{n}}{2}\right\}$$
Analogamente a quanto fatto prima, vale che:
- $\forall v\in R\setminus R_2:Pr((v,u)\in E)\geq\frac{|R_2|}{n}= \frac{1}{\sqrt{n}}$
- $Pr(Y_2\geq h)\lt\left(1-\frac{1}{\sqrt{n}}\right)^h$
- $E[Y_2]=\sum\limits_{h\geq0}Pr(Y_2\geq h)\leq\sum\limits_{h\geq0} \left(1-\frac{1}{\sqrt{n}}\right)^h=\frac{1}{1-\left(1-\frac{1}{\sqrt{n}}\right)}=\sqrt{n}$

Questo significa che, una volta entranti nella regione $R$, per entrare nella regione $R_2$ utilizzare archi random è mediamente equivalente a muoversi lungo gli archi dell'anello.

Ovver, quando si raggiunge una distanza dall'obiettivo dell'ordine di $\sqrt{n}$ glia rchi random non sembrano giocare più alcun ruolo, e la ragione di ciò è il fatto cbhe gli archi random sono troppo random (come visto con Watts-Strogatz)


[^1]: perchè gli archi random che si incontrano fanno allontanare dall'obiettivo, e dunque ognuno di questi ci si avvicina solo di un'inezia all'obiettivo

[^2]: perchè in un anello $u$ ha due vicini a distanza $1$, due a distanza $3$ e così via

[^3]: $\geq$: perchè potrebbe essere $d(v,t)=\frac{d(s,t)}{2^j}$, in tal caso esisterebbe arco $(v,z)$ dell'anello tale che $d(z,t)=d(v,t)-1\lt\frac{d(s,t)}{2^j}$, e tale arco farebbe sicuramente terminare la fase $j$

[^4]: usiamo le parti intere inferiori perchè la quantità $\frac{d(v,t)}{2}$ potrebbe essere non intera

[^5]: ovvero, quando si esegue la ricerca decen. di un percorso in un anello con archi random generati secondo il modello con $q=0$, si trova mediamente un percorso di lungh. parecchio elevata

[^6]: "$\gt$" sia perchè $\frac{1}{n-1}\gt\frac{1}{n}$, sia perchè $\frac{1}{n-1}$ è la prob. di esistenza aroc random, ma $u,v$ potrebbero essere vicini nell'anello
