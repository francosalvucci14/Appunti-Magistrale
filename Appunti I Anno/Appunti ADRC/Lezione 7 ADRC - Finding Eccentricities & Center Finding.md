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