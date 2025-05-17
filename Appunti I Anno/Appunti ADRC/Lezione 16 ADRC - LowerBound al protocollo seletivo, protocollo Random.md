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