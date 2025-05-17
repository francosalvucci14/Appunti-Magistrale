# Lower Bound al protocollo selettivo

Il protocollo selettivo può essere **migliorato** nei grafi generali? La risposta è no, infatti vale il seguente teorema

>[!teorem]- Lower Bound
>Nei **grafi generali diretti**, l'uso di una famiglia selettiva è in qualche modo ***necessaria***.
>Infatti vale che $$\forall Dd\leq n\implies\Omega\left(Dd\log\left(\frac{n}{d}\right)\right)$$

Non faremo la dimostrazione di questo teorema, però è un risultato forte perchè ci afferma che meglio di $Dd\log\left(\frac{n}{d}\right)$ non possiamo fare.

## Random vs Deterministic : Gap Esponenziale

Prendiamo un grafo di esempio con $d\simeq n,D=c$ costante.
Abbiamo visto quindi che il lower bound per i protocolli deterministici è $\Omega(n\log(n))$

Cosa possiamo dire dei protocolli **randomizzati**?

Facciamo un breve esempio di protocollo randomizzato
### Protocollo probabilistico semplice

Ad ogni istante di tempo, ogni nodo informato trasmette con probabilità $\frac{1}{2}$ (lancio di moneta, indipendente)
- Abbiamo quindi che, $\forall v\in V,\forall t\to X_v^t=\begin{cases}1&\text{Esce Testa, il nodo trasmette}\\0&\text{altrimenti}\end{cases}$

Analizziamo questo protocollo su un grafo molto semplice, composto da $3$ livelli $L_0,L_1,L_2$
- $s\in L_0$
- $|L_1|=\frac{n}{2}-1$ nodi
- $|L_2|=\frac{n}{2}$ nodi, $y\in L_2$

Ipotizziamo che tutti i nodi in $L_1$ siano attivi e pronti a trasmettere
Vediamo che $T\leq \underbrace{T_1}_{\text{tempo per }L_1}+\underbrace{T_2}_{\text{tempo per }L_2}$

È facile vedere che $\mathbb E[T_1]=\frac{1}{p}=2$ perchè $p=\frac{1}{2}$

Per $\mathbb E[T_2]$ usiamo l'evento $\mathcal E(y)=\text{"y viene informato"}$. Abbiamo che $$\begin{align}Pr[\mathcal E(y)|\underbrace{L_1}_{\text{tutti i nodi in }L_1\text{informati}}]&=\underbrace{\binom{\frac{n}{2}-1}{1}}_{\text{num. nodi che possono trasmettere in }L_1}\overbrace{\left(\frac{1}{2}\right)}^{\text{nodo trasmette}}\overbrace{\left(\frac{1}{2}\right)^{\frac{n}{2}-1}}^{\text{esce Croce per }\frac{n}{2}-1\space nodi}\\&=\left(\frac{n}{2}-1\right)\left(\frac{1}{2}\right)^{\frac{n}{2}-1}\end{align}$$
Quindi $$Pr[\mathcal E(y)^t|L_1]\leq O\left(\frac{n}{2^{\frac{n}{3}}}\right)\sim\text{Geo}\left(p=\frac{n}{2^{\frac{n}{3}}}\right)$$
E di conseguenza $$\mathbb E[T_2]=\frac{1}{p}=\Theta\left(\frac{2^{\frac{n}{3}}}{n}\right)$$che è **esponenziale**, e di conseguenza non va bene.

Vediamo ora un'approccio sicuramente migliore

### Protocollo probabilistico BGI

Mettiamoci nel caso di grafi $d-$regular layered (ovvero grafi che possono essere organizzati a livelli $L_0,L_1,\dots,L_D$ dove tutti gli archi vanno da qualsiasi nodo di un livello $j$ ad un qualsiasi nodo del livello $j+1$, e il grado entranre di ogni nodo è esattamente $d$)

Il protocollo **RND BGI** è il seguente : 
For $K=1,2,\dots$ (stages)
- For $j=1,2,\dots,c\log(n)$
	- If nodo $x$ è ***stato informato*** nello stage $K-1$ allora trasmette con probabilità $\frac{1}{d}$

Analizziamo il protocollo 

Vale il seguente teorema : 

>[!teorem]- Teorema
>Il protocollo BGI completa il Broadcast entro $O(D)$ stages, e quindi il tempo di completamento è $O(D\log(n))\space w.h.p$

**dim** Per induzione sui livelli $L=1,\dots,D$

FARE DIMOSTRAZIONE