# Questioni di popolarità

Nella lezione scorsa abbiamo introdotto un modello di grafi aleatori, ovvero il modello di Erdos-Renyi, e abbiamo visto che, in un grafo generato in accordo al tale modello, al crescere di $k$ il numero di nodi aventi grado $k$ decresce esponenzialmente in $k$

Perchè la decrescita è così veloce? Per rispondere alla domanda ci viene in "aiuto" il **Teorema del Limite Centrale** che, in maniera intuitiva e informale, enuncia quanto segue:

>[!teorem]- Teorema del Limite Centrale (versione informale)
>La somma di **tanti** valori aleatori si distribuisce approssimativamente come una distribuzione normale (o gaussiana) intorno al suo valore atteso, che decresce molto velocemente quando ci si allontana dal valore atteso stesso.

La situazione è la seguente : 

![[Pasted image 20250801134357.png|center|500]]

Ma cosa c'entra il Teorema del Limite Centrale con la nostra situazione?

Nel grafo $G_{n,p}$ gli archi vengono aggiunti come una sequenza di oggetti, indipendentemente gli uni dagli altri, perciò il grado di un nodo è la somma di eventi indipendenti del tipo: $$\delta_i=\sum\limits_{j\in[n]\setminus\{i\}}e_{ij},\quad e_{ij}=\begin{cases}1&(i,j)\in E\\0&\text{altrimenti}\end{cases}$$
Ci troviamo allora nella esatta situazione descritta dal Teorema.

Il punto cruciale è che **la porzione di grafo che già è stata costruita non ha alcuna influenza sul prossimo arco che verrà creato**
# Power Law

Nella realtà però la situazione è abbastanza diversa.

Consideriamo ad esempio il grafo orientanto del web, dove i nodi sono le pagine e, se la pagina $a$ contiene un **hyperlink** verso la pagina $b$, allora $(a,b)$ è un arco (diretto) del grafo

Sono stati condotti vari studi al fine di analizzare la distribuzione dei gradi (archi entranti) nei nodi del grafo del web.

Quel che è stato osservato differisce ***sostanzialmente*** da quanto indicato nel Teorema del Limite Centrale: infatti la **frazione di pagine web che ha grado entrante $k$ è proporzionale a $\frac{1}{k^c}$, per qualche costante $c$, invece che $\frac{1}{k^k}$**.

>[!definition]- Power Law
>Una funzione che decresce come l'inverso di un polinomio è chimata **power law**

Quanto detto prima lo possiamo riscrivere come: **il numero di nodi del grafo del web che hanno grado entrate elevato è molto maggiore di quello che ci si aspetterebbe assumendo che gli archi si formino indipendentemente gli uni dagli altri**

Ma perchè vale questa cosa?
## Riconoscere una Power Law

Prima di cercare di capire le ragioni della power law, cerchiamo di capire come hanno fatto questi studiosi ad accorgersi di questo fenomeno, ovvero:
- partendo da un grafico (discreto) di un grafo dove, per ogni intero $k$ in ascissa riporta in ordinata il num di nodi del grafo aventi grafo $k$, come fai ad accorgerti che quella funzione decresce come l'inverso di un polinomio invece che come l'inverso di una esponenziale??

![[Pasted image 20250801135817.png|center|300]]

La risposta è più "facile" del previsto: è sufficiente considerare il grafico log-log, ovvero un grafico in cui gli assi rappresentano $\ln(x),\ln(y)$, e quindi invece che rappresentare $y=f(k)$ rappresentiamo $y=f(\ln(k))$ ($f(k)$ indica la funzione che esprime il num di nodi con grado $k$)

![[Pasted image 20250801140042.png|center|300]]

In questo modo, se $f(k)=\frac{1}{k^c}$, il grafo sarà grosso modo una retta: $\ln(y)\approx-c\ln(k)$ e in $(a)\to y=\frac{1}{x^2+1}$

Possiamo ora tornare a cercare di comprendere perchè si verifica la Power Law
## Power Law e fenomeno Rich-Get-Richer

Supponiamo di stare a costruire una pagina web, e mentre scriviamo ci accorgiamo che è opportuno inserire un hyperlink a qualche pagina che descrive qualcosa che ci serve

La domanda sorge spontanea, quale pagina scegliamo (tra le miriadi di pagine disponibili) di puntare dalla nostra pagina?

La risposta è alquanto immediata, scegliamo infatti fra tutte le pagine, quella che ci sembra più "**autorevole**". 
Ma anche qui la domanda sorge spontanea, come facciamo a capire l' "**autorevolezza**" di una pagina?

Ad esempio, questo accade perchè facendo una ricerca su un motore di ricerca, quella pagina appare in prima posizione (e vedremo poi che questo accade quando quella pagina ha tanti link entranti)

Cioè, stiamo **aumentando il grado di pagine che hanno già un grado elevato, e scegliamo quale arco aggiungere sulla base degli archi già presenti**

Un fenomeno del tutto analogo si verifica nelle reti sociali, con una rete che ,ad esempio, ci mostra i post dei nostri contatti, e quando loro commentano post di pagine che seguono, anche i noi potrebbe nascere l'interesse in quelle pagine, andando così di fatto a dare sempre più popolarità a pagine che ne hanno già molta.
## Un modello per la Power Law

Per quanto descritto precedentemente, vogliamo quindi definire un modello generativo di gradi nel quale, a differenza del modello di Erdos-Renyi, l'aggiunta di un nuovo arco dipenda dagli archi già presenti nel grafo, e vogliamo anche che il modello esibisca una Power Law

Il nostro modello sarà quindi basato sulla semplice osservazione che **gli individui tendono a copiare il comportamento di altri individui** (che vedremo nel dettaglio più avanti, quando si parlerà di herding)

Consideriamo quindi un processo di creazione di un grafo che ricorda il meccanismo di creazione delle pagine web:
- le pagine vengono create una alla volta, ovvero in **sequenza**
- quando viene creta una pagina, si decide a quali pagine esse debba puntare
- ciascun puntatore è un arco diretto

Come nel modello di Erdos-Renyi, fissiamo un parametro $p\in[0,1]$

I nodi vengono aggiunti in time-step discreti:
- al passo $1$ viene creato il nodo $1$
- al passo $2$ vengono creati il nodo $2$ e l'arco (diretto) $(2,1)$
- finita questa fase di inizializzazione, i nodi e gli archi vengono creati in accordo alla seguente regola:
	- al passo $i$ vengono creati il nodo $i$ e un arco uscente da $i$: viene scelto **uniformemente a caso** (u.a.r) un nodo $a\lt i$ e 
		- con prob. $p$ viene creato l'arco $(i,a)$
		- con prob, $1-p$ viene creato l'arco $(i,b)$, dove $(a,b)$ è l'arco uscente da $a$

Intuitivamente, man mano che il numero di archi entranti in un nodo aumenta, cresce la prob. che quel nodo **venga selezionato come estremo di un arco uscente da un nodo di nuova creazione**
- è quindi lo stesso fenomeno che abbiamo osservato nel web
- e di fatto abbiamo costruito un modello che descrive il fenomeno **Rich-Get-Richer**

>[!info]- Osservazione
>Osserviamo che ogni nodo $i\gt1$ ha esattamente un arco uscente

Vediamo graficamente cosa accade quando il nodo $i$ viene aggiunto al grafo

![[Pasted image 20250801142513.png|center|500]]

Come possiamo vedere dall'immagine, alla creazione del nodo $i$ avvengono le seguenti operazioni: 
1) viene scelto u.a.r il nodo $a$
2) con prob. $p$ si crea l'arco $(i,a)$ (e quindi si collega il nodo $i$ al nodo $a$)
3) con prob. $1-p$ si crea l'arco $(i,b)$

Il modello generativo che abbiamo appena descritto prende il nome di **modello di Barabase-Albert**

Resta quindi da verificare se i grafi generati in accordo a questo modello esibiscono una Power Law, ovvero che la funzione che descrive il numero atteso di nodi di grado $k$ si comporta come l'inverso di un polinomio

Per falro, occorre formalizzare: per ogni coppia di interi $i,j:i\gt j,i\geq2$ introduciamo la v.a $$d_{ij}=\begin{cases}1&(i,j)\in E\\0&\text{altrimenti}\end{cases}$$
Allora, in accordo alle regole che abbiamo descritto in precedenza, vale che: 
$$\begin{align}Pr(d_{ij}=1)&=p\cdot\text{"prob di scegliere nodo j"}+(1-p)\cdot\text{"prob scelgo h t.c }d_{hj}=1\text{"}\\&=\frac{p}{i-1}+(1-p)Pr\left(\bigcup_{h\lt i:(h,j)\in E}\{\text{scelgo h}\}\right)\\&=\frac{p}{i-1}+(1-p)\sum_{1\leq h\lt i:(h,j)\in E}Pr(\text{viene scelto h})\quad\text{(perchè sono eventi disgiunti)}\\&=\frac{p}{i-1}+\frac{1-p}{i-1}\sum_{1\leq h\lt i:(h,j)\in E}1\\&=\frac{p}{i-1}+\frac{1-p}{i-1}\sum_{1\leq h\lt i}d_{hj}\end{align}$$
Valgono alcune osservazioni chiave: 
1) **Oss.1**: Ha senso calcolare $Pr((i,j)\in E)$ per $i\gt1$ (questo perchè il nodo $1$ non ha archi uscenti)
2) **Oss.2**: Ogni nodo $i\gt1$ ha esattamente un arco uscente. Quindi deve valere che $$Pr(\exists j\lt i:(i,j)\in E)=1$$Infatti abbiamo che:
	1) $Pr(\exists j\lt i:(i,j)\in E)=\sum_{1\leq j\lt i}Pr((i,j)\in E)$, e procedendo per induzione otteniamo che:
		1) caso base $i=2$: $\sum_{1\leq j\lt 2}Pr((2,j)\in E)=1$ per costruzione
		2) caso induttivo: assumendo che $\sum_{1\leq j\lt a}Pr((a,j)\in E)=1,\forall a\leq i-1$ abbiamo che: $$\begin{align}\sum_{1\leq j\lt i}Pr((i,j)\in E)&=\sum_{1\leq j\lt i}\left[\frac{p}{i-1}+\frac{1-p}{i-1}\sum_{1\leq h\lt i}d_{hj}\right]\\&=\sum_{i\leq j\lt i}\frac{p}{i-1}+\sum_{i\leq j\lt i}\left[\frac{1-p}{i-1}\sum_{1\leq h\lt i}d_{hj}\right]\\&=\frac{(i-1)p}{i-1}+\frac{1-p}{i-1}\sum_{1\leq h\lt i}\sum_{1\leq j\lt i}d_{hj}\quad(1)\\&=p+\frac{1-p}{i-1}\sum_{1\leq h\lt i}1=p+(1-p)=1\end{align}$$dove $(1)$ vale perchè, per ogni $h\lt i$ ha esattamente un arco uscente e $\substack\sum_{i\leq j\lt i}d_{hj}=1$
3) **Oss.3**; Possiamo così interpretare la regola per costruire il grafo: 
	1) **Il nodo $j$ a cui connettere $i$ è scelto u.a.r con prob. $p$, e con prob. proporzionale al grado di $j$ con prob. $(1-p)$**
	2) che esprire chiaramente il fenomeno **Rich-Get-Richer**

## Dimostriamo la Power Law

Siamo pronti a dimostrare che il modello che abbiamo definito esibisce una Power Law

La dimostrazione procederà attraverso i seguenti $4$ passaggi:
1) Definizione della legge aleatoria che esprime la variazione del grado di un nodo nel tempo
2) *Approssimazione* deterministica e continua della legge al punto $1)$, che porterà ad una equazione differenziale (\*bestemmiando\*)
3) Risoluzione dell'equazione differenziale: la soluzione costituirà un'approssimazione della funzione che esprime il grado di un nodo nel tempo
4) Individuazione della Power Law

### 1) Legge aleatoria per la variazione del grado

Sia $D_j(t)$ la v.a che esprime il numero di archi entranti nel nodo $j$ al passo $t$ di generazione del grafo, ovviamente $D_j(t)$ è definita per $t\geq j$ e $\forall j\geq1$

Al passo $t=j$, il grado entrante di $j$ è $0:D_j(j)=0$ (**condizione iniziale**)

Esprimiamo ora la **variazione attesa** nel tempo della v.a $D_j(t)$:
- Al passo $t+1$, il grado di $j$ può essere inviariato rispetto al passo $t$ oppure può essere aumentato di una unità, e $D_j(t+1)=D_j(t)+1\iff(t+1,j)\in E$ 
- Quindi vale che: $$Pr(D_j(t+1)-D_j(t)=1)=Pr(d_{hj}=1)=\frac{p}{t}+\frac{1-p}{t}\sum_{1\leq h\lt t+1}d_{hj}=\frac{p}{t}+\frac{1-p}{t}D_j(t)$$
### 2) Approssimazione deterministica e continua

Abbiamo calcolato prima che $$Pr(D_j(t+1)-D_j(t)=1)=\frac{p}{t}+\frac{1-p}{t}D_j(t)$$con condizione iniziale $D_j(j)=0$

Per ogni $j\geq1$ definiamo una funzione *discreta deterministica* $X_j(t)$ che "assomiglia" a $D_j(t)$: 
- la funzione $X_j(t)$ è definita per $t\geq j$
- $X_j(j)=0$
- $X_j(t+1)-X_j(t)=\frac{p}{t}+\frac{1-p}{t}X_j(t)$

A questo punto, approssimiamo il comportamento di $X_j(t)$ con una funzione $x_j(t)$, definita su un dominio continuo e ancora definita per $t\geq j$:
- $x_j(j)=0$
- $\frac{d}{dt}x_j(t)=\frac{p}{t}+\frac{1-p}{t}x_j(t)$, che è una equazione differenziale

**Oss** : non è detto che l'andamento della funzione $x_j(t)$ sia effettivamente vicino al comportamento della variabile aleatoria $D_j(t)$

### 3) Risoluzione dell'equazione differenziale

Dobbiamo quindi risolvere l'equazione differenziale $$\frac{d}{dt}x_j(t)=\frac{p}{t}+\frac{1-p}{t}x_j(t)$$
Svolgiamo i calcoli: 
$$\frac{d}{dt}x_j(t)=\frac{p}{t}+\frac{1-p}{t}x_j(t)\implies\frac{d}{dt}x_j(t)=\frac{1}{t}\left[p+(1-p)x_j(t)\right]$$
E quindi 
$$\frac{1}{p+(1-p)x_j(t)}\cdot\frac{dx_j(t)}{dt}=\frac{1}{t}$$
Integrando otteniamo che 
$$\int\frac{1}{p+(1-p)x_j(t)}\cdot\frac{dx_j(t)}{dt}dt=\int\frac{1}{t}dt$$
Svolgendo i calcoli dell'integrale otteniamo che: 
$$\begin{align}&\int\frac{dx_j(t)}{p+(1-p)x_j(t)}dt=\int\frac{1}{t}dt\\\text{molt. a sx e dx per 1-p}\\&\int\frac{(1-p)dx_j(t)}{p+(1-p)x_j(t)}dt=(1-p)\int\frac{1}{t}dt\\\text{sostituiamo }y=p+(1-p)x_j(t)\\\text{da cui otteniamo che }dy=(1-p)dx_j(t)\\&\int\frac{dy}{y}=(1-p)\int\frac{1}{t}dt\end{align}$$
Da cui si ottiene come risultato $$\begin{align}&\ln[p+(1-p)x_j(t)]=(1-p)\ln(t)+c\\&\ln[p+(1-p)x_j(t)]=\ln(t)^{1-p}+c\\\text{esponenziando}\\&p+(1-p)x_j(t)=t^{1-p}e^c\end{align}$$
Prendendo $H=e^c$, e sfruttando la condizione iniziale $x_j(j)=0$, otteniamo $$p=Hj^{1-p}\implies H=\frac{p}{j^{1-p}}$$
E per concludere otteniamo che: 
$$x_j(t)=\frac{p}{1-p}\left[\left(\frac{t}{j}\right)^{1-p}-1\right]$$
### 4) Individuazione della Power Law

Calcoliamo infine, nel modello deterministico continuo, dati $k,t$ quale frazione dei nodi, al passo $t$ ha "grado" $k$

Dato che al passo $t$ l'insieme dei nodi p $[t]=\{1,2,\dots,t\}$, sia allora $A_t(k)=\{j\leq t:x_j(t)\geq k\}$

Vogliamo quindi calcolare $$\frac{1}{t}\left(|A_t(k)|-|A_t(k+1)|\right)$$
Per defizione $j\in A_{t}(k)\iff j\leq t,x_j(t)\geq k$, ma $x_j(t)=\frac{p}{1-p}\left[\left(\frac{t}{j}\right)^{1-p}-1\right]$ e quindi $x_j(t)\geq k$ quando: 
$$\begin{align}&\frac{p}{1-p}\left[\left(\frac{t}{j}\right)^{1-p}-1\right]\geq k\\&\left(\frac{t}{j}\right)^{1-p}\geq\frac{(1-p)}{p}k+1\\&\frac{t}{j}\geq\left[\frac{(1-p)}{p}k+1\right]^{\frac{1}{1-p}}\\&j\leq t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}\end{align}$$
Quindi, $j\in A_{t}(k)\iff j\leq t,j\leq t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}$, ma poichè $\frac{1-p}{p}k+1\gt1$ e $-\frac{1}{1-p}\lt0$ allora $\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}\lt1$ , e quindi $t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}\leq t$

Abbiamo visto che $j\in A_{t}(k)\iff j\leq t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}$ , di conseguenza $$A_t(k)=\left\{j\leq t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}\right\}$$e di conseguenza $$
|A_t(k)|=t\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}
$$
Ritornando alla richiesta principale, vogliamo calcolare $$\frac{1}{t}\left(|A_t(k)|-|A_t(k+1)|\right)$$
Sia $F(k)=\left[\frac{(1-p)}{p}k+1\right]^{-\frac{1}{1-p}}$

Allora $$\frac{1}{t}\left(|A_t(k)|-|A_t(k+1)|\right)=F(k)-F(k+1)=f(k)$$
Possiamo approssiamare $f(k)$ con $-\frac{dF(k)}{dk}$, infatti $$F(k)-F(k+1)=-\left[-\frac{F(k)-F(k+1)}{1}\right]=-\left[\frac{F(k+1)-F(k)}{1}\right]\approx-\frac{dF(k)}{dk}$$
Quindi 
$$\frac{1}{t}\left(|A_t(k)|-|A_t(k+1)|\right)=f(k)\approx-\frac{dF(k)}{dk}=-\frac{1-p}{p}\left[-\frac{1}{1-p}\right]\left[\frac{1-p}{p}k+1\right]^{-\frac{1}{1-p}-1}$$che è proprio una **Power Law** con esponente $1+\frac{1}{1-p}$

Quindi, abbiamo dimostrato effettivamente che il modello per il fenomeno Rich-Get-Richer esibisce effettivamente una Power Law $\blacksquare$ 
## Conclusioni sull'analisi del modello

Per analizzare il nostro modello Rich-Get-Richer, abbiamo approssimato mediante una funzione (deterministica e) continua la legge probabilistica che esprime la variazione del grado di un nodo fra due passi consecutivi, ma non abbiamo idea di quanto tale approssimazione si avvicini al modello disclreto e aleatorio

È stato dimostrato che, nel modello Rich-Get-Richer che abbiamo proposto, **con alta probabilità la frazione del numero di nodi di grado $k$ è proporzionale a** $k^{-\frac{1}{1-p}-1}$, esattamente come nell'approssimazione che abbiamo discusso.
## Impredicibilità della popolarità

Nel tempo sono stati fatti vari esperimenti per mostrare l'**impredicibilità** (unpredictability) degli effetti Rich-Get-Richer.

Nell'esperimento più famoso, sono riusciti a dimostrare che la fase iniziale del processo, ovvero quella di diventare popolari, **è molto fragile**.

Il processo che conduce alla popolarità è **pesantemente sensibile alle condizioni iniziali**
(ovvero dipende fortemente dalle condizioni iniziali)
# La "Long Tail"

Analizziamo la questione della popolarità da un'altro punto di vista, il punto **economico**

La distribuzione della popolarità può avere importanti effetti sulle attività commerciali, in particolar modo sui "magazzini virtuali", ovvero quelle società che commercializzano elevate quantità di prodotti che non potrebbero essere gestite da magazzini fisici

Il punto qui è: uno di detti venditori guadagna di più vendendo **tante copie di pochi libri molto popolari** oppure vendendo **poche copie di tantissimi libri poco popolari**?

Invece che interessarci a quanti sono i nodi di grado $k$, ci interessa ora sapere se, complessivamente, il volume di affari derivante dai nodi poco popolari (quelli di grado "basso") equivale al volume di affari dei nodi molto popolari (quelli di grado "alto").

Per gestire questa questione, quello che possiamo fare è ordinare i nodi per popolarità non crescente.

Andiamo quindi a creare un grafico, dove:
- lungo l'**asse delle ascisse** elenchiamo i nodi, ordinati per popolarità non crescente: il primo sarà il più popolare, seguito dal secondo più popolare e così via
- lungo l'**asse delle ordinate** elenchiamo le popolarità dei nodi: in corrispondenza al nodo $i$ indicheremo il grado del nodo $i$

I nodi poco popolari formeranno quindi la cosidetta **coda** del grafico appena costruito.

Il volume di affari che ci interessa è, grosso modo, l'area della regione compresa fra la coda del grafico e l'asse delle $x$

Ma com'è fatto questo grafico? Possiamo, in qualche modo, riutilizzare quanto studiato circa la distribuzione dei gradi dei nodi per ottenere questo grafico?

Per rispondere alle domande, quello che possiamo fare è la cosa seguente: invece che elencare lungo l'asse delle ascisse, uno per uno, tutti i nodi, elenchiamo con un solo punto tutti i nodi che hanno la stessa popolarità: l'ascissa di tale punto sarà quindi il num. di nodi aventi quella popolarità

La situazione è la seguente

![[Pasted image 20250801182825.png|center|500]]

Piccola osservazione chiave: **naturalmente**, per compiere questa modifica dobbiamo assumere che **a gradi di popolarità diversi corrispondano numeri di nodi diversi che hanno quelle popolarità**

Pensandoci bene, questo grafico è, grosso modo, ottenuto dal grafico che esprime il num. di nodi $n$ che hanno grado $k$, scambiando gli assi.

Se $d(k)$ è la funzione che esprime il num. di nodi aventi grado $k$, allora il grafico che ci occorre rappresenta, grosso modo, la funzione $f=d^{-1}(n)$ (ammesso che $d$ sia invertibile)

È possibile dimostrare che, se la funzione $f$ che esprime la frazione del numero di nodi aventi grado $k$ è una Power Law (come appare dai dati sperimentali), ovvero per qualche costante $c\gt0,f(k)\approx k^{-c}$, allora **anche $d$ esprime una Power Law**, anche qui $\exists a\gt0:d(k)\approx k^{-a}$, e dunque se $$n=d(k)\approx k^{-a}\implies k\approx n^{-\frac{1}{a}}$$ Questa quantità decresce *molto lentamente*, di conseguenza va a formare la **lunga coda**

![[Pasted image 20250806110128.png|center|500]]

## Gli effetti della web-search

La domanda che ci poniamo ora è: l'utilizzo dei motori di ricerca, per la ricerca su internet, ha impatto sul fenomeno **rich-get-richer**?

Da un lato, il fenomeno rich-get-richer è **amplificato** in virtù dell'utilizzo di motori di ricerca basati sul ranking (ossia, che elencano le pagine risultanti dalla ricerca in un ordine derivante dall'assegnazione di un punteggio a sua volta derivante, ad esempio, dal numero di link-entranti delle pagine).

D'altra parte, le richieste ad un motore di ricerca possono essere sottoposte in una enorme varietà di forme, dipendentemente dalle parole chiave scelte per effettuare una ricerca, e questo aumenta la possibilità di essere indirizzati a pagine che non sono nella "top list" (usando, ad esempio, parole chiavi inusuali), e tutto ciò non fa altro che **mitigare gli effetti** rich-get-richer.

Per sfruttare la lunga coda, ovvero per vendere i prodotti di "nicchia", i venditori online provano ad indirizzare gli utenti, ad esempio ricorrendo all'utilizzo di ***recommendation systems***, ovvero quando i motori di ricerca invitano gli utenti ad esplorare pagine poco popolari sulla base delle loro ricerche pregresse.

In conclusione, il progetto di strumenti di **web-search** è un esempio di utilizzo degli effetti feedback, volto ad indirizzare gli utenti nell'elaborare le loro richieste, in alcuni casi **amplificando** l'effetto rich-get-richer, in altri **attenuandolo**

