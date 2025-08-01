# Premessa

Partiamo dall'obiettivo del corso, ci occuperemo di **reti**, nell'accezione del termine più ampia possibile,

Le reti le analizzeremo da molti punti di vista: **prestazioni,struttura, utilizzo...**, utilizzando tecniche prese in prestito da molte discipline.

I contenuti del corso sono una sintesi fra :
- Matematica/Informatica (modelli, analisi, algoritmi, complessità)
- Economia (relazione come incentivo/disincentivo a comportamenti)
- Scienze sociali (studio di strutture e interazioni caratteristiche di gruppi e popolazioni)
# Reti

Genericamente parlando, una rete è uno **schema di interconnessione** fra un insieme di entità.

Dipendentemente dal tipo di entità parliamo di reti fisiche, reti sociali, reti di informazioni etc..

L'idea alla base di questo corso è la seguente: **ampia popolazione che reagisce ale azioni dei singoli**

Ciò che studieremo sarà il comportamento *aggregato* di gruppi di individui:
- Come la presenza di legami influsice sul comportamento dei singoli individui (effetti informativi, fenomeni di diffusione, ricerca decentralizzata di percorsi brevi)
- Come la presenza di legami modifica la struttura stessa della rete (stabilità, **fenomeno rich-get-richer**)
- Come la struttura dell'insieme dei legami permette di desumere informazioni (web-search, sistemi di voto)

## Struttura di una rete

È difficile rappresentare e studiare puntualmente reti di milioni di individui.

Possiamo però analizzare proprietà "globali" di una rete di grandi dimensioni, infatti possiamo: 
- vedere se la rete contiene **Componenti Giganti**
- all'interno di una componente connessa può avere interesse ricercare porzioni *densamente* connesse
- si può studiare se la rete presenta una struttura centro / periferia
- si può studiare il ruolo dei nodi che costituiscono una porzione densamente connessa, suddividendoli in entità centrali / periferiche
- etc..

Talvolta, lo studio dei fenomeni lo porteremo avanti a *livello di popolazione*, senza quindi considerare i singoli individui
- Ad esempio, quando studieremo il **fenomeno rich-get-richer**, andremo a vedere quall'è, ***mediamente***, la frazione di individui che ha un elevato grado di popolarità
- Non studieremo quindi la popolarità individuo per individuo

Talvolta per comprendere altri fenomeni occorrerà considerare la struttura fisica della rete
- Ad esempio, per comprendere il ruolo di una certa relazione all'interno di una data rete, dobbiamo studiare precisamente la topologia di quella rete, come accade nello studio dei **fenomeni di diffusione**

In ogni caso, poichè una rete è un insieme di individui e delle relazioni che intercorrono fra essi, ovviamente la rete viene modellata come un grafo.

E quindi, essendo la rete modellata come un grafo, per studiare i fenomeni che avvengono all'interno di essa utilizzeremo tutte le tecniche / nozioni che già conosciamo bene dalla **Graph Theory**, come :
- Grafi orientati e non
- Percorsi
- Spanning Tree
- Componenti Connesse
- BFS
- Diametro
- etc..

(Si assume la conoscenza pregressa di tutte queste nozioni)

Alcuni esempi di reti sono : 

![[Pasted image 20250801094851.png|center|500]]

**Fig 1** : Rete sociale di un gruppo di tennis universitario di 34 persone

Oppure 

![[Pasted image 20250801094932.png|center|500]]

**Fig 2** : Rete sociale basata sulle comunicazioni tramite e-mail di 436 impiegati aziendali

## Diversificare le reti

Per studiare i fenomeni che avvengono all' interno di una rete, *quella* rete bisogna averla sotto gli occhi.

Se qualcuno, ad esempio, ci mostra una certa rete, noi la modelliamo tramite grafo,e poi ne studiamo le proprietà discusse prima.

Però, potremmo essere interessanti a studiare le stesse questioni da un altro punto di vista, come ad esempio: 
- qual è, **mediamente**, il diametro di una rete sociale espresso in funzione del numero di nodi?
- in funzione del grado, qual'è **mediamente** la frazione del numero di nodi che ha un certo grado in una rete sociale?
- E così via...

Per occuparci di queste questioni occorre considerare tante (anche troppe) reti, e la domanda sorge spontanea: 
- Tutte queste reti da dove le prendiamo?

Infatti ottenere dati di una rete vera non è proprio una questione di poco conto, infatti chi detiene i dati di una rete ha tutto l'interesse a tenerseli per sè, e comunque rimane anche il problema che di reti vere, in circolazione, ce ne sono ben poche.

Tutto questo a cosa ci porta quindi? Ci porta a doverci "***inventare***" le reti

## Modelli generativi di grafi casuali

Ma cosa significa "inventare" una rete? Bhe significa sostanzialmente **generare un grafo in modo casuale**
- Ovvero un grafo in cui gli archi fra i nodi sono scelti sulla base di un evento aleatorio, ad esempio il lancio di moneta

Durante il corso del tempo sono stati proposti diversi modelli per generare grafi casuali, ma noi ne studieremo solamente quattro.

Naturalmente, alcuni di questi modelli riproducono taluni fenomeni che sono stati osservati nelle reti reali, **ma non tutti**.

Noi cerchemo di capire *quali modelli* usare per riprodurre il fenomeno che stiamo cercando.

Studiamo quindi il primo modello generativo, ovvero il modello di **Erdos-Renyi**

# Il modello di Erdos-Renyi

Fissiamo $n\in\mathbb N$ e $p\in[0,1]$.

A partire da questi $n,p$ costruiamo un grafo nel modo seguente: 
- l'insieme dei nodi è $[n]=\{1,2,\dots,n\}$
- per ogni coppia di elementi distinti $i,j\in[n]$, con ***probabilità*** $p$ viene inserito l'arco $(i,j)$ nel grafo, formalmente : $$Pr((i,j)\in E)=p,Pr((i,j)\not\in E)=1-p$$
Il grafo costruito in questo modo è un evento aleatorio che indicheremo con la notazione $G_{n,p}$

Il grafo $G_{n,p}$ assume quindi il nome di ***grafo aleatorio***, di cui studieremo alcune caratteristiche, come :
- esistenza di una componente gigante
- grado dei nodi

Ovviamente, il tutto sfruttando il calcolo delle probabilità (per dio)

Osserviamo innanzi tutto che, fissato il numero di nodi $n$, *al variare* di $p$ si otterrano grafi con caratteristiche molto differenti:
- Quando $p=0$ sarà possibile ottenere un **unico** grafo $G_{n,0}$ , ovvero il grafo tale per cui $|E|=\emptyset$
- Analogamente, quando $p=1$ sarà possibile ottenere anche qui un **unico** grafo $G_{n,1}$ , il grafo completo su $n$ nodi, ovvero il grafo tale per cui $|E|=n^2$

In generale vale che $G_{n,p}$ conterrà, **mediamente**, tanti più archi quanto più $p$ si avvicina a $1$
In particolare, **mediamente**, un nodo avrà tanti più vicini quanto più $p$ si avvicina a 1

Non ci resta quindi che quantificare.
## Erdos-Renyi : Componenti Giganti

Diamo una definizione. 

>[!definition]- Componente GIgante
>Una **componente gigante** in un grafo è una componente connessa che contiene una frazione del numero di nodi

Molte reti reali contengono una componente gigante

La prima domanda che ci poniamo è : il modello di Erdos-Renyi riesce a rappresentare questa caratteristica di molte reti reali?

Più precisamente, esistono dei valori del parametro $p$ per i quali $G_{n,p}$ contiene componenti giganti?

Come primo risultato dimostreremo che, se $p\gt\frac{\ln(64)}{n}$ allora **con altra probabilità** $G_{n,p}$ contiene una componente connessa costituita da almeno metà dei suoi nodi

Prima di partire a bomba con il teorema chiariamo un paio di concetti: 
- **Con alta proabilità** significa con **probabilità proporzionale almeno a** $(1-\frac{b}{n^c})$ per qualche coppia di costanti positive $b,c$
- poi, definiamo con $X$ la v.a corrispondente al **numero di nodi nella più grande componente connessa di** $G_{n,p}$

Il teorema è quindi enunciato formalmente così: 

>[!teorem]- Teorema
>Se $p\gt\frac{\ln(64)}{n}$ allora $$Pr\left(X\geq\frac{n}{2}\right)\geq1-2^{-\frac{n}{8}}$$

Prima di dimostrare il teorema, diamo l'enunciato di un lemma molto importante: 

>[!info]- Lemma
>Se $X\lt\frac{n}{2}$ allora $\exists A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}$ e non esistono archi fra i nodi in $A$ e i nodi in $[n]\setminus A$   

**Dimostrazione lemma**

Siano $C_1,C_2,\dots,C_k$ tutte le componenti connesse di $G_{n,p}$ e assumiamo che siano **ordinate** per cardinalità non decrescente, ovvero $$|C_1|\leq|C_2|\leq\dots\leq|C_k|$$
Dato che per ipotesi $X\lt\frac{n}{2}$, allora $|C_i|\lt\frac{n}{2},\forall i=1,\dots,k$

Scegliamo ora un indice $h$ tale che 
$$\begin{align}(1)&\sum_{i=1}^{h-1}|C_i|\lt\frac{n}{4}\\(2)&\sum_{i=1}^{h}|C_i|\geq\frac{n}{4}\end{align}$$
Ovvero: 
- $(1)=|C_1|+|C_2|+\dots+|C_{h-1}|\lt\frac{n}{4}$
- $(2)=(1)+|C_h|\geq\frac{n}{4}$

Risulta subito che $h\lt k$, se così non fosse ($h=k$) allora avremmo che 
$$|C_1|+\dots+|C_{k-1}|+|C_k|\lt\frac{n}{4}+\frac{n}{2}\lt n$$
Scegliamo ora l'insieme $A$ come $A=C_1\cup C_{2}\cup\dots\cup C_h$, vale quindi che $A\neq\emptyset$ e $[n]\setminus A\neq\emptyset$

Si vede subito che, per costruzione dello stesso insieme $A$ vale che:
- $|A|\geq\frac{n}{4}$ (primo punto del lemma okay)
- $|A|=\underbrace{|C_1|+|C_2|+\dots+|C_{h-1}|}_{\lt\frac{n}{4}}+|C_h|\lt\frac{n}{4}+\frac{n}{2}\lt\frac{3n}{4}$ (seconda parte okay)
Dimostriamo ora la non esistenza di archi fra $A$ e $[n]\setminus A$, terminando così la dimostrazione del lemma.

Avendo preso quindi un indice $h(\lt k)$ e un insieme $A=C_1\cup C_{2}\cup\dots\cup C_h$ vale che l'insieme $[n]\setminus A=|C_{h+1}|\cup\dots\cup|C_k|$

Per costruzione dello stesso, dato che $C_1,C_2,\dots,C_k$ sono **tutte** componenti connesse dello stesso grafo $G_{n,p}$, allora non ci possono essere archi fra $A$ e $[n]\setminus A$, altrimenti, se ci fosse un arco fra $C_i,C_j$ con $i\leq h,j\gt h$ allora $C_i\cup C_j$ sarebbe un'unica componente connessa, e questo è assurdo. $\blacksquare$ 

Chiamiamo **buono** l'insieme $A$ individuato dal lemma, vale quindi la seguente osservazione: 

>[!warning]- Osservazione
>Il lemma ci assicura che **la probabilità che la più grande componente connessa di $G_{n,p}$ contenga meno di $\frac{n}{2}$ nodi è $\leq$ alla probabilità che $G_{n,p}$ contenga almeno un insieme di nodi buono**

Possiamo quindi dimostrare il teorema di prima, che per semplicità riporto sotto

>[!teorem]- Teorema
>Se $p\gt\frac{\ln(64)}{n}$ allora $$Pr\left(X\geq\frac{n}{2}\right)\geq1-2^{-\frac{n}{8}}$$

**Dimostrazione teorema**

Calcoliamo $Pr\left(X\lt\frac{n}{2}\right)$, ossia la probabilità che la massima componente connessa in $G_{n,p}$ contenga meno di $\frac{n}{2}$ nodi, che è l'evento complementare dell'evento $\{X\geq\frac{n}{2}\}$ che è quello che ci interessa.

In virtù dell'osservazione fatta pocanzi, vale che $$Pr\left(X\lt\frac{n}{2}\right)\leq Pr(\exists A\subseteq[n]:\text{A è buono})$$
Allora vale che 
$$\begin{align}Pr\left(X\lt\frac{n}{2}\right)&\leq Pr(\exists A\subseteq[n]:\text{A è buono})\\&=Pr\left(\bigcup_{A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}}Pr[\text{no archi fra }A,[n]\setminus A]\right)\\\text{Union Bound}\to&\leq\sum_{A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}}Pr[\text{no archi fra }A,[n]\setminus A]\\\text{num. archi poss. fra A e [n]-A è |A|(n-|A|)}\\\text{e prb. di non avere arco è (1-p)}\\&=\sum_{A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}}(1-p)^{|A|(n-|A|)}\\(1-p)^{z}\text{max per z minimo}\\\text{e |A|(n-|A|) min. per |A|=}\frac{n}{4}\\&\leq\sum_{A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}}(1-p)^{\frac{3n^2}{16}}\end{align}$$
Quindi, dato che $[n]$ contiene $2^n$ sottoinsiemi otteniamo che 

$$\begin{align}Pr\left(X\lt\frac{n}{2}\right)&\leq\sum_{A\subset[n]:\frac{n}{4}\leq|A|\lt\frac{3n}{4}}(1-p)^{\frac{3n^2}{16}}\\&\leq2^{n}(1-p)^{\frac{3n^2}{16}}\\&\lt2^{n}\left(1-\frac{\ln(64)}{n}\right)^{\frac{3n^2}{16}}\\&=2^{n}\left[\left(1-\frac{\ln(64)}{n}\right)^{n}\right]^{\frac{3n}{16}}\\\text{molt. e div. l'esp. n per -}\ln(64)&=2^{n}\left[\left(1-\frac{\ln(64)}{n}\right)^{-\frac{n}{\ln(64)}(-\ln(64))}\right]^{\frac{3n}{16}}\end{align}$$

Ora, poichè vale che $$\lim_{n\to\infty}\left(1-\frac{\ln(64)}{n}\right)^{-\frac{n}{\ln(64)}}=e$$
Allora, per $n$ suff. grande otteniamo che $$\left(1-\frac{\ln(64)}{n}\right)^{-\frac{n}{\ln(64)}(-\ln(64))}\approx e^{-\ln(64)}=64^{-1}$$
E quindi otteniamo che $$Pr\left(X\lt\frac{n}{2}\right)\lt2^{n}[64^{-1}]^{\frac{3n}{16}}=2^{n}2^{-\frac{18n}{16}}=2^{-\frac{n}{8}}$$
Da cui segue il teorema. $\blacksquare$

Il teorema può essere generalizzato in questo modo : 

1) Se $p(n-1)\lt1$ allora **quasi sicuramente** tutte le componenti connesse di $G_{n,p}$ hanno $O(\log(n))$ nodi
2) Se $p(n-1)=1$ allora **quasi sicuramente** $G_{n,p}$ ha una componente connessa di $\approx n^{\frac{2}{3}}$ nodi
3) Se $p(n-1)\gt1$ allora **quasi sicuramente** $G_{n,p}$ ha una componente connessa di $\Omega(n)$ nodi e tutte le altre hanno $O(\log(n))$ nodi

"quasi sicuramente" significa che, al tendenre di $n$ all'infinito la prob. dell'evento tende a $1$

In conclusione, la presenza di componenti giganti dipende dal prodotto $p(n-1)$, ma cosa rapprensenta effettivamente $p(n-1)$?
## Erdos-Renyi : Grado dei nodi

Per $i\in[n]$, se indichiamo con $\delta_i$ la v.a **che esprime il grado del nodo $i$**, abbiamo che il valore atteso del grado di un nodo è: $$\mathbb E[\delta_i]=\sum\limits_{j\in [n]\setminus\{i\}}[1p+0(1-p)]=\sum\limits_{j\in[n]\setminus\{i\}}p=(n-1)p$$
Questo significa che, se $p$ è costante, il grado dei nodi cresce (in media) linearmente con il numero di nodi.

Cerchiamo ora di capire se $G_{n,p}$ ben si presta a descrivere una rete sociale, costituita da tantissimi individui

Se il grado medio di un nodo è $(n-1)p$, e $p$ è un valore costante, allora mediamente il numero di contatti di un individuo in una rete è proporzionale agli individui che costituiscono una rete sociale, il che non è propriamente ragionevole

Per questa ragione, al fine di modellare significativamente reti reali di grandi dimensioni è opportuno che $p$ sia una funzione decrescente di $n$, del tipo $p=p(n)=\frac{\lambda}{n}$ per qualche costante positiva $\lambda$

Fissato un intero $k\lt n$, vogliamo ora calcolare con quale probabilità un nodo in $G_{n,p}$ ha grado $k$

Sia $i\in[n]$: la prob. che un nodo $i$ abbia grado $k$ è la probabilità che *esattamente* $k$ altri nodi siano adiacenti a $i$:
- il numero di possibili $k$-uple di nodi scelti nell'insieme $[n]\setminus\{i\}$ è $\binom {n-1}{k}$ 
- la prob che vi sia un arco fra $i$ e *ciascuno* dei nodi della $k$-upla è $p^k$
- la prob che **non** vi sia un arco fra $i$ e *ciascuno* dei nodi non contenuto nella $k$-upla è $(1-p)^{n-k-1}$

Mettendo tutto insieme quindi otteniamo che: 
$$Pr(\delta_i=k)=\binom{n-1}{k}p^k(1-p)^{n-k-1}$$
Sviluppando, otteniamo che:
$$\begin{align}Pr(\delta_{i}=k)&=\binom{n-1}{k}p^{k}(1-p)^{n-k-1}\\\text{sostituiamo }\left(p=\frac{\lambda}{n}\right)\to&=\binom{n-1}{k}\left(\frac{\lambda}{n}\right)^{k}\left(1-\frac{\lambda}{n}\right)^{n-k-1}\\&=\frac{(n-1)(n-2)\dots(n-k)}{k!}\cdot\frac{\lambda^{k}}{n^{k}}\left(1-\frac{\lambda}{n}\right)^{n-k-1}\\\text{dato che }(1-x)\lt e^{-x}\to&\lt\frac{(n-1)(n-2)\dots(n-k)}{k!}\cdot\frac{\lambda^{k}}{n^{k}}\cdot e^{\frac{-\lambda(n-k-1)}{n}}\\&\lt\frac{n^{k}}{k!}\cdot\frac{\lambda^{k}}{n^{k}}\cdot e^{\frac{-\lambda(n-k-1)}{n}}\\\text{per n suff. grande}\to&\approx\frac{n^{k}}{k!}\cdot\frac{\lambda^{k}}{n^{k}}\cdot e^{-\lambda}\end{align}$$
Quindi, per riassumere abbiamo che 
$$Pr(\delta_i=k)\lt\frac{\lambda^{k}}{k!}\cdot e^{-\lambda}$$
E dato che $k!\approx\sqrt{2\pi k}\cdot\left(\frac{k}{e}\right)^k$ (Approx. di Stirling), otteniamo che 
$$Pr(\delta_i=k)\lt\frac{(\lambda\cdot e)^k}{\sqrt{2\pi k}\cdot k^k}\cdot e^{-\lambda}=\frac{e^{-\lambda}}{\sqrt{2\pi k}}\left(\frac{\lambda\cdot e}{k}\right)^k$$
Dunque possiamo concludere che **la prob. che un generico nodo abbia grado $k$** decresce *molto velocemente* al crescere di $k$
- Più precisamente, decresce come $k^{-k}$, ossia **decresce esponenzialmente in $k$**

Adesso, ci chiediamo quale sia la frazione del numero di nodi che hanno grado $k$

Per rispondere a questa nuova domanda, indichiamo con $F_k$ la v.a che esprime tale frazione, e indichiamo con $\delta_{i,k}$ la v.a composta in questo modo: 
$$\delta_{i,k}=\begin{cases}1&\delta_i=k\\0&\text{altrimenti}\end{cases}$$
Allora, per costruzione vale che $$F_k=\frac{1}{n}\sum\limits_{i\in[n]}\delta_{i,k}$$
Calcoliamo quindi il valore atteso di $F_k$

Vale che 
$$\begin{align}\mathbb E[F_k]&=\mathbb E\left[\frac{1}{n}\sum\limits_{i\in[n]}\delta_{i,k}\right]\\&=\frac{1}{n}\sum\limits_{i\in[n]}\mathbb E[\delta_{i,k}]\quad\text{per linearità}\\&=\frac{1}{n}\sum\limits_{i\in[n]}Pr(\delta_i=k)\\\text{dal conto precedente}\to&\lt\frac{e^{-\lambda}}{\sqrt{2\pi k}}\left(\frac{\lambda\cdot e}{k}\right)^k\end{align}$$
Quindi, in media, la frazione del numero di nodi che hanno grado $k$ decresce come $k^{-k}$, ovvero **decresce esponenzialmente in $k$**
