```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# Introduzione

Qui studieremo in che modo, e con quali esiti, possiamo sintetizzare le informazioni in possesso dei singoli individui in una rete al fine di derivare una singola informazione comulativa, che permetterà di prendere una decisione fra una serie di alternative, fra le quali scegliere la "migliore"

Iniziamo studiando cosa accade quando un insieme di individui deve prendere una decisione di gruppo:
- dando ad ogni individuo un segnale privato
- e prendendo decisioni individuali
# Un nuovo modello di decision making

Definiamo un modello di decision making individuale

1) Ogni individuo deve prencedere una decisione fra due alternative: $X,Y$
	- una delle due è "giusta", l'altra "sbagliata", e si esprime con il simbolo "$\gt$: ad es., scriviamo $X\gt Y$ se $X$ è la scelta giusta
	- le due alternative sono, a priori, equiprobabili: $Pr(X\gt Y)=Pr(Y\gt X)= \frac{1}{2}$
2) Ogni individuo riceve un segnale privato: $x,y$
	- $Pr(x|X\gt Y)=Pr(y|Y\gt X)=q\gt \frac{1}{2}$
3) Ogni individuo sceglie in accordo al proprio segnale privato
4) CIascun individuo opera la propria scelta fra $X$ e $Y$, la scrive su una scheda che poi introduce in un'urna
5) Infine, viene presa una decisione collettiva fra $X$ e $Y$ sulla base delle scelte dei singoli individui

Vale quindi il seguente teorema 

>[!teorem]- Teorema della giuria di Condorcet
>Nel modello di decision making appena definito, se $X\gt Y$ e il numero di individui coinvolti nella decisione è $k$ allora, quasi sicuramente vale che:
>$$\lim_{k\to\infty}\frac{|\{i:1\leq i\leq k\land r_i=X\}|}{k}=q$$
>Ovvero, vale che:
>$$\lim_{k\to\infty}Pr\left(\frac{|\{i:1\leq i\leq k\land r_i=X\}|}{k}=q\right)=1$$
>Dove con $r_{i}$ indichiamo **la scelta dell'individuo $i$**

Questo teorema dimostra che, qualora si dovesse prendere una ***decisione collettiva*** in favore di $X$ e $Y$ e si decidesse in accordo alla scelta della maggioranza degli individui, la decisione colletiva porterebbe a scegliere l'alternativa "giusta"
- Il che mostra come il modello di decision making appena definito sia un esempio nel quale si manifesta "la saggezza della folla"
## Voto non sincero
 
Questo teorema è quindi valido nel modello appena descritto, ove è previsto che *ogni individuo sceglie in accordo al proprio segnale privato* (punto $3$), e questo è perfettamente ragionevole, poichè nel modello si assume che il segnale in favore della scelta "giusta" sia quello più probabile (punto $2$)

Tuttavia, vi sono situazioni nelle quali un individuo può ritenere migliore la scelta in disaccordo al suo segnale privato, e questo lo abbiamo già visto nel caso dell'herding.

Vediamo ora come il voto "non sincero" (ossia, una scelta in disaccordo con il proprio segnale privato) abbia senso anche quando si debba prendere una decisione collettiva e *ciascun individuo scelga **senza** osservare gli altri*, ovvero casi in cui il voto non sincero di un individuo può massimizzare la probabilità che la scelta collettiva sia quella "giusta"

Facciamo un esempio pratico: torniamo al gioco delle urne

Questa volta abbiamo:
- un'urna $UG$ contenente $10$ palline gialle
- un'urna $UV$ contenente $9$ palline verdi e una pallina gialla

Come nel gioco delle urne scegliamo a caso un'urna, e quindi : 
$$Pr(UG)=Pr(UV)= \frac{1}{2}$$
In questo caso le regole del gioco sono un pò diverse:
- abbiamo $3$ giocatori, ciascuno dei quali estrae in segreto una pallina dall'urna scelta (e la reinserisce)
- *dopo* che i $3$ giocatori hanno estratto ciascuno una pallina, *simultaneamente* dichiarano ciascuno la propria scelta: $UG$ o $UV$
- se la maggioranza ha indovinato di quale urna si tratti, tutti e $3$ vincono un premio, altrimenti nessun vince

