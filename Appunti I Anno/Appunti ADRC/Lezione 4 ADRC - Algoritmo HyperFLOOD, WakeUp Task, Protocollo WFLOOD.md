# Ancora su Hypercube

>[!definition]- Hypercube scalabile
>L'architettura Hypercube si dice **scalabile** se vale che $$deg(\mathcal H)=Diam(\mathcal H)=\text{poly-log}$$

Ricordiamo che in $\mathcal H$ abbiamo che : 
- $|V|=n=2^d$
- $|E|=\frac{n\log(n)}{2}=\frac{2^dd}{2}$

Definiamo ora la distanza tra due nodi $\hat{x},\hat{y}\in\mathcal H$, usando la metrica **distanza di Hamming**

>[!definition]- Distanza di Hamming
>Siano $\hat{x},\hat{y}\in\{0,1\}^d$ due stringhe di bit (ovvero due nodi in $\mathcal H$)
>Allora, definiamo la distanza di Hamming tra questi due nodi come $$d_{H}(\hat{x},\hat{y})=\left|\{i\in[d]:x_i\neq y_i\}\right|$$

A questo punto possiamo definire il vicinato di un nodo $\hat{x}$ negli Hypercube

>[!definition]- Vicinato di un nodo
>Sia $\hat{x}\in\{0,1\}^d$ un nodo in $\mathcal H$.
>Il suo vicinato è $$N(\hat{x})=\{\hat{y}\in\{0,1\}^d:d_{H}(\hat{x},\hat{y})=1\}$$
>

Vediamo ora qualche proprietà strutturale interessante
$\forall x\in V$
1. **Fatto 1** $|N(x)|=d=\log_2n$
2. **Fatto 2** $diam(\mathcal H_d)=d=\log_2n$

***dimostrazione fatto 2*** (vedi bene slides di Andrea)

$\forall x,y\in V\implies\exists x\to y$ di dimensione $\leq d$

Prendiamo i nodi $x,y$ come sequenze di bit $\hat{x}=\langle x_d,x_{d-1},\dots,x_j,\dots,x_1\rangle,\hat{y}=\langle y_d,y_{d-1},\dots,y_j,\dots,y_1\rangle$

Da sinistra verso destra :
- Controllo i due bit
	- Se sono uguali non facciamo nulla
	- Altrimenti, prendo il bit di $\hat{x}$ e riscrivo $\hat{x}$ con quel bit al complemento. In questo modo avremo che la $d_H$ sarà pari a $1$, e quindi $\exists$ arco (ho costruito un pezzo del cammino)
	- Vado avanti al più $d$ volte, e quindi la lunghezza del cammino sarà $\leq d\quad\blacksquare$

Ora, essendo che $|E|=\frac{2^dd}{2}$, l'algoritmo FLOOD avrà msg_complexity pari a $\Theta(n\log(n))$

## Algoritmo HyperFLOOD

1. L'initiator invia il messaggio a tutti i suoi vicini
2. Un nodo che riceve il messaggio dal link $l$, lo invia solo sui links con etichetta $l'\lt l$ 

**Protocollo Gerarchico** : L'initiator informa un nodo in ogni sub-hypercube di dimensione $k'\lt k$. A questo punto, il messaggio va in ognugno di essi.

**Correttezza** : Si basa sul fatto che ***ogni nodo viene toccato (Spanning Property)***

Per ogni coppia di nodi $x,y$ esiste un percorso di **etichette decrescenti**. Il messaggio verrà inviato su quel percorso.

In altre parole, gli archi usati formano un Sottografo di tip **Spanning** del Hypergrafo originale

![[Pasted image 20250324144354.png|center|500]]


La **message complexity** di questo algoritmo è quindi $n-1$, e di conseguenza OTTIMALE
- Perchè ogni entità riceve le informazioni una sola volta

**dimostrazione** : Se così non fosse, allora gli **archi usati** formerebbero un ciclo contraddizione con le trasmissioni su percorsi con solo etichette decrescenti.

>[!teorem]- Tempo ideale
>Nel worst-case il tempo ideale è $O(\log n)$ ed è OTTIMALE

---

# WakeUP Task

Cambiamo problema.

Abbiamo $V$ insieme dei nodi

- **Configurazione iniziale** : 
	- Sottoinsieme $W\subset V$ di nodi che stanno nello stato **awake** e $V-W$ nodi nello stato **asleep**. 
	- Ogni nodo di $W$ può iniziare una qualunque computazione (non abbiamo la restrizione $UI$)
- **Configurazione Finale** : Tutti i nodi in $V$  devono essere nello stato **awake**

Le restrizioni standard sono $R=\{TR,BL,CN\}$

## Protocollo WFLOOD

```
ASLEEP
Spontaneamente
	Invia (wake-up) a N(x)
	Diventa AWAKE

Ricezione(wake-up)
	Invia (wake-up) a N(x)-{sender}
	Diventa AWAKE
```

Il protocollo in questione ha : 
- **msg_comp** : $\underbrace{2m-n+1}_{\text{(*)}}\leq M(WFLOOD)\leq \underbrace{2m}_{\text{(**)}}$ (ottimale)
- **time ideal** : $Time(WFLOOD)=D$ (ottimale)

$(*)=\sum\limits_{w\in W}|N(w)|+\sum\limits_{v\in V-W}|N(v)|-1=2m-n+1$

$(**)=\sum\limits_{v\in V}|N(v)|=2m$

Per quanto riguarda gli alberi : 
$M(WFLOOD/Tree)=n+k^*-2$, dove $k^*=$ num. initiator

Più $k^*$ aumenta, più la complessità tende a $n-2$

# WakeUP Task su Grafi completi con Etichette uniche

In questa versione, abbiamo la restrizione che ogni nodo ha un nome univoco

>[!teorem]- Teorema
>$M(WFLOOD/K,Id)=O(n\log(n))$, dove $K=$Clique

Possiamo fare di meglio? la risposta è *NO*

Vogliamo infatti dimostrare che $M(WFLOOD/K,Id)=\Omega(n\log(n))$

**dimostrazione**

Provare un lower-bound nel calcolo distribuito è un gioco a $2$ : Protocollo PROT vs Avversario ADV

ADV, guarda il protocollo PROT, e decide:
1. le etichette dei nodi
2. quali sono gli initiator, e quando iniziano la computazione
3. **ritardo dei messaggi**
4. **combinare i link con l'etichettatura delle porte (per ogni sender)**

**Idea-Chiave** : ADV massimizza il num. di messaggi *inutili* tra tutti i nodi in stato AWAKE
- Gli strumenti che userà sono (3) e (4)

Diamo ora la definizione di sottoinsiemi connessi : 

>[!definition]- Sottoinsiemi Connessi
>$2$ sottoinsiemi $A,B$ si dicono **connessi** al tempo $t$ se : $$\exists a\in A\land b\in B : \text{a e b si scambiano messaggi al tempo t}$$

ADV sveglia la sorgente $s$. Quando $s$ invia $m(s)$, ADV imposta l'etichetta $l$ sull'arco $e$ di $y$.
Usando (3) $y$ non riceve $m(s)$ finché $y$ non invia $m(y)$ su $l'$.
-> ADV assegna $l'$ all'arco $e$.

Quindi, ADV consente a $s$ e $y$ di ricevere i messaggi **nello stesso momento**, quando sono già svegli.

Regole generali di ADV

Sia $A=\{\text{nodi svegli}\}$ a un certo tempo $t$

- **Goal di ADV** : i messaggi sono inviati ai nodi svegli e $A$ è sempre connesso

Quando un nodo in stato AWAKE seleziona una porta UTILIZZATA, allora ADV non fa nulla, in quanto il messaggio è inutile.

Mentre...

Sia $x\in A$ un nodo che esegue $send(msg(x))$ su una **porta con etichettamento non assegnata** $a$. Allora ADV distingue due casisitche diverse :
1. $x$ ha un'arco libero $e$, che collega un nodo AWAKE
	1. Allora ADV assegna $a\to e$
2. Nessun collegamento libero. ADV crea un nuovo sottoinsieme di nodi $B$ e poi lo collega ad $A$ (nuovo STAGE)

Sia $k$ il num. di nodi AWAKE

Partendo da $A=\{x_0=s,x_1,\dots,x_k\}$ si crea un sottinsieme $B$ di cloni -> $B=\{z_0,\dots,z_k\}\implies |A|=|B|$

Sia $x=x_i$ per un qualche $i\implies m(x_i)$ verrà inviato a $z_i$
ADV farà si che la storia di $B$ sia indipendente e identica a quella di $A$ $(x_i \sim z_i)$ :

Per ogni $i=1,\dots,k$ : $z_i$ si comporterà esattamente come $x_i$.
ma, quando $z_i$ avrà utilizzato tutti i suoi collegamenti a $B$ (**Fase 1**), allora il msg $m(x_i)$ inviato a $z_i$ **verrà ritardato** fino a che $z_i$ non vorrò inviare $m(z_i)$ su un'etichetta libera e tutti i collegamenti a B saranno stati utilizzati.

A quel punto (**Fase 2**), ADV assegna l'etichetta libera al collegamento $z_i \iff x_i$

## Analisi dei costi

>[!definition]- Active(i)
>Sia $Active(i)=\{\text{tutti i nodi in stato AWAKE allo stage i}\}$
>$$New(i)=Active(i)-Active(i-1)$$

**Fatto 1** : $Active(0)=\{s\}$ e $|New(i)|=|Active(i-1)|$

>[!definition]- M(i-1)
>$M(i-1)=$ numero di messaggi scambiati prima dello stage $i$

**Fatto 2** : ADV obbliga PROT (cioè i nodi attivi) a lasciare che i **nuovi** nodi scambino almeno lo stesso numero di messaggi dello stage $(i-1)$ prima di connettere $A$ a $B$, cioè
$$\text{num. messaggi} = M(i-1)$$
**Conseguenza** : ***Numero totale di messaggi*** prima della connessione $A-B$ allo stage $i$ è $$\underbrace{M(i-1)}_{\text{Stage i}}+\underbrace{M(i-1)}_{\text{Stage i prima di A-B}}=2M(i-1)$$
**Domanda principale** : Quanti messaggi PRIMA della fase $i+1$? (è necessaria l'analisi della fase 2)

Il numero esatto dipende dal PROT ma possiamo dare un Lower-bound

**Osservazioni**. ADV non inizia un nuovo STAGE finché
* C'è $x \in Active(i)$ che invia $m(x)$ su una nuova etichetta $l$
- Tutti i collegamenti da $x$ ad $Active(i)$ non sono liberi

**Conseguenza**. $x$ ha comunicato con tutti i nodi in
$$Active(i) = Active(i-1) \cup New(i)$$
Due casi:
- $x \in Active(i-1)$. Allora, i msg $x \iff New(i)$ avviene nella Fase $i$
	- Quindi, dopo la connessione (Fase 2) $$\text{num. msg(i)} \geq |New(i)| = |Active(i-1)|$$
- $x\in New(i)$. Allora tutti i messaggi stanno in fase $i$
	- Ancora $$\text{num. msg(i)} \geq |New(i)| = |Active(i-1)|$$
- Combinando otteniamo $$M(i)\geq \underbrace{2M(i-1)}_{\text{Fase 1}}+\underbrace{|Active(i-1)|}_{\text{Fase 2}}$$
Abbiamo quindi che $$|Active(i)|=\begin{cases}1&i=0\\2|Active(i-1)|&i\geq1\end{cases}$$
Di conseguenza,per un $i$ generico vale che $|Active(i)|=2^i$

E quindi : $$M(i)\geq2M(i-1)+2^{i-1}\geq i\cdot2^{i-1}\underbracket{=}_{\text{Num. Stage=}\log(n)}\Omega(n\log(n))\quad\quad\blacksquare$$
Abbiamo quindi dimostrato che il lower-bound della message complexity per il protocollo *WFLOOD* su *clique (K)* con etichettamento dei nodi (ID) è pari a $\Omega(n\log(n))$
