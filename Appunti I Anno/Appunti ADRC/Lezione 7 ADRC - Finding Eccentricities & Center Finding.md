# Finding Eccentricities

Il problema che vogliamo studiare qui è quello di trovare l'**eccentricità** di ogni entità $x$ nel SD con topologia ad albero

Vediamo che, l'eccentricità di un nodo $x$ è definita come : 
$$r(x)=\max_{y\in V}\{d(x,y)\},\quad d(x,y)=\text{distanza dal nodo x a y}$$
![[Pasted image 20250331100610.png|center|300]]

Notiamo che nell'esempio $r(x)=4$

Vediamo alcune topologie particolari : 
1. Clicque : $r(x)=1,\forall x$
2. Stella : $$r(x)=\begin{cases}1&\text{x è al centro}\\2&\text{Altrimenti}\end{cases}$$
3. Catena : $$r(x)=\begin{cases}\frac{n}{2}&\text{x è  al centro}\\\leq\frac{n}{2}&\text{se x non sta al centro e non sta agli estremi}\\n&\text{x è uno dei due estremi}\end{cases}$$
Ora, come facciamo a trovare l'eccentricità di ogni nodo?

## Idea 1 (Banale)

1. Ogni nodo effettua una richiesta (broadcast)
2. Le foglie inviano un messaggio per collezzionare le distanze (Convergecast)

La messagge complexity di questo protocollo è  $O(n^2)$
Abbiamo troppi messaggi **ridondanti**
Possiamo riciclare qualche valore??

## Idea 2 (Migliore usando Saturazione)

Anche qui usiamo la Saturation Technique
1. Trova l'eccentricità dei due nodi saturati usando il messaggio $M$ (fase di saturazione)
2. Propaga le informazioni **necessarie** in modo che gli altri nodi possano calcolarsi la loro eccentricità (nella fase di notifica)

La messagge complexity di questo protocollo vediamo essere la stessa della Saturazione

Vediamo ora qualche teorema

>[!teorem]- Step 1
>$$r(s_1)=\max\{h(T_1),1+r(s_2)\}$$
>![[Pasted image 20250331101840.png|center|500]]

>[!teorem]- Step 2
>$$r(x)=F(knw(x),M'+1)$$
>![[Pasted image 20250331102437.png|center|500]]
>Ricordiamo che $knw(x)$ è il valore di eccentricità del nodo $x$ relativa al suo sottoalbero (e la conosce grazie alla prima passata di saturazione)

E così via

![[Pasted image 20250331102513.png|center|500]]

Vediamo ora il protocollo
### Protocollo

Gli stati sono : 
- $S=\{Available, Active, Processing, Saturated\}$
- $S_{init}=Available$

L'idea del protocollo è : 
- Definisci una variabile locale **maxdist(y)** che prende la ***Depth*** del sottoalbero radicato in $y$
- Quando calcolata, $y$ invia $maxdist(y)$ al suo parent
- Quando un nodo $x$, in stato PROCESSING, riceve dal suo parent il messaggio $M=("Saturation",maxdist)$ (quindi $x$ diventa saturato) allora :
	- $x$ potrà calcolare la sua **eccentricità**
	- $x$ potrà inviare le **informazioni corrette** ad ognuno dei sui figli :
		- $x$ invia a $y$ -> $\max\{maxdist(z)|\text{z\#y è figlio di x}\}$ 

Il protocollo è : 

**definisci Distance[]**  

```
AVAILABLE
Spontaneamente
	Invia (Activate) a N(x)
	Distance[x]=0
	Vicini = N(x)
	If |Vicini| = 1 :
		maxdist = 1 + Max{Distance[*]}
		M=("Saturation",maxdist)
		parent = Vicini
		Invia (M) a parent
		diventa PROCESSING
	Else : 
		diventa ACTIVE

Invia (Activate) a N(x) - {sender}
	Distance[x]=0
	Vicini = N(x)
	If |Vicini| = 1 :
		maxdist = 1 + Max{Distance[*]}
		M=("Saturation",maxdist)
		parent = Vicini
		Invia (M) a parent
		diventa PROCESSING
	Else : 
		diventa ACTIVE
```

```
ACTIVE
Ricevo(M)
	Distance[{sender}] = Distanza_Ricevuta
	Vicini = Vicini - {sender}
	If |Vicini| = 1 :
		maxdist = 1 + Max{Distance[*]}
		M=("Saturation",maxdist)
		parent = Vicini
		Invia (M) a parent
		diventa PROCESSING
```

```
PROCESSING
Ricevo(M)
	Distance[{sender}] = Distanza_Ricevuta
	r(x) = Max{Distance[z]:z appartiene a N(x)}
	For all y appartenente a N(x)-{parent} do :
		maxdist = 1 + Max{Distance[z] : z appartiene a N(x)-{y}}
		invia ("Resolution",maxdist) a y
	EndFor
	diventa DONE
```

---
# Center Finding

Qui quello che ci chiediamo è trovare il **centro** dell'albero, ovvero quel nodo $x$ tale che $r(x)\leq r(y),\forall y\in V-\{x\}$. Per fare ciò, dobbiamo prendere, tra tutte le distanze massime, quella minimizzata

Introduciamo quindi il concetto di **percorso diametrale**, che in qualche modo può essere associato al longest path

![[Pasted image 20250331115242.png|center|400]]

Il centro è il nodo con eccentricità minima

![[Pasted image 20250331115319.png|center|400]]

Un'idea potrebbe essere : 
1. Trovare tutte le eccentricità -> $4n-4$
2. Trovare la più piccola -> $2n-2$
3. Totale $6n-6$

Una strategia migliore può essere trovata studianto le proprietà che il nodo centro ha.

>[!definition]- Proprietà 1
>In un albero c'è un unico centro, oppure due centri che sono però vicini

![[Pasted image 20250331115635.png|center|500]]

Come vediamo, se ci sono un numero **pari** di nodi sul diametro allora abbiamo 2 centri, altrimenti un centro solo.

>[!definition]- Proprietà 2
>I centri si trovano sui percorsi diametrali

Prima di definire la terza proprietà, definiamo : $$d_1[x]=\text{max distance},\quad d_2[x]=\text{seconda max distance}\quad\text{(attraverso vicini differenti)}$$
>[!definition]- Proprietà 3
>Un nodo $x$ è il centro $\iff d_1[x]-d_2[x]\leq1$
>(se $d_1[x]=d_2[x]$ allora c'è un solo centro)

A questo punto, l'idea per il Center Finding diventa : 
1. Trova tutte le eccentricità
2. Ogni nodo può capire localmente se è il centro o no
3. Totale : $4n-4$

**Un'altra idea migliore** : 
1. Trova l'eccentricità dei nodi saturati -> $3n-2$
2. Localmente controllo se sono il centro
3. Se non lo sono, propago l'informazione relativa alla distanza **solo** in direzione del centro -> $\leq\frac{n}{2}$
4. Totale : $\leq 3.5n-2$

