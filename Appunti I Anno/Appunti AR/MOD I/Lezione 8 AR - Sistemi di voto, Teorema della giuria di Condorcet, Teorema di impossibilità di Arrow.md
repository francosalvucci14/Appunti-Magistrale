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
## Voto non sincero - maggioranza
 
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

Consideriamo la strategia di un giocatore rispetto al suo segnale privato:
- se estrae una gialla, vale che $$Pr(UG|g)=\frac{ \frac{10}{11} \frac{1}{2}}{\frac{10}{11} \frac{1}{2}+ \frac{1}{10} \frac{1}{2}}= \frac{10}{11}$$
- ma se estrae una verde, allora vale che $Pr(UV|v)=1$

Mettiamoci ora nei panni di uno dei giocatori, per capire quale ragionamento possa fare per rispondere in modo da massimizzare la prob. di vincere:
- io giocatore so che noi tre giocatori vinciamo se almeno due di noi indovinano
- la domanda quindi è: quando la mia risposta è **davvero influente** ai fini della vittoria?
- la risposta è: quando le risposte degli altri due giocatori sono discordi
	- perchè se sono concordi, in quel caso qualunque sia la mia risposta non verrà modificata la maggioranza

Però se le risposte dei due giocatori sono discordi, allora uno di essi ha risposto $UV$. [^1]

Perciò, assumendo che gli altri rispondano sinceramente, la mia risposta è influente ai fini della vittoria solo quando l'urna è $UV$, e quindi, qualunque pallina estraggo, mi conviene rispondere $UV$
## Voto non sincero - unanimità

Una situazione simile si presenta nelle giurie, durante i processi

Quando si deve decidere se un imputato è colpevole $(C)$ o innocente $(I)$, e a priori vale che $$Pr(C)=Pr(I)= \frac{1}{2}$$ciascun girato riceve un segnale $c$ o  $i$, come nel caso dell'herding, e quindi $$Pr(c|C)=Pr(i|I)=q\gt \frac{1}{2}$$In questo caso occorre aggregare i voti dei giurati per giungere a un verdetto di colpevolezza o di innocenza, e per condannare un imputato è necessario che l'insieme $S$ dei segnali ricevuti dai giurati siano indice di colpevolezza con prob. molto alta (è richiesto che $Pr(C|S)\gt\gt \frac{1}{2}$)

Diciamo quindi che per condannare un'imputato è necessario che ***tutti*** i giurati votino in favore della condanna

In questo caso, se io sono un giurato: in quale situazione la mia risposta è davvero influente ai fini del verdetto?
- se fra gli altri giurati c'è qualcuno che è in favore dell'innocenza, che io voti per la colpevolezza o per l'innocenza non altera il verdetto
- ma se tutti gli altri giurati sono in favore della colpevolezza, allora è proprio dal mio voto che dipende il verdetto

Supponiamo che la giuria consti di $k$ giurati e che tutti (tranne me) votino in accordo ai propri segnali.

Calcoliamo quindi la prob. $Pr(C|ic^{k-1})$ che l'imputato sia colpevole quando un solo giurato riceve un segnale $i$:
$$\begin{align*}
Pr(C|ic^{k-1})&=\frac{Pr(ic^{k-1}|C)Pr(C)}{Pr(ic^{k-1}|C)Pr(C)+Pr(ic^{k-1}|I)Pr(I)}\\&=\frac{(1-q)q^{k-1} \frac{1}{2}}{(1-q)q^{k-1} \frac{1}{2}+q(1-q)^{k-1} \frac{1}{2}}\\&=\frac{q^{k-2}}{q^{k-2}+(1-q)^{k-2}}
\end{align*}$$
e dunque: $$\lim_{k\to\infty}Pr(C|ic^{k-1})=\lim_{k\to\infty}\frac{1}{1+\left(\frac{1-q}{q}\right)^{k-2}}=1\quad q\gt \frac{1}{2}\implies \frac{1-q}{q}\lt 1$$
E quindi, al crescere del numero dei giurati, *se uno solo di essi riceve il segnale $i$* allora l'imputato è colpevole quasi sicuramente.
# Sistemi di voto

Fin'ora abbiamo considerato due metodi per ottenere una decisione collettiva a partire da un insieme di decisioni individuali, nel caso in cui le alternative fra le quali scegliere fossero due:
- la maggioranza
- l'unanimità

In generale comunque, ci vengono presentate più alternative fra le quali esprireme le nostre preferenze, e spesso più che decretare semplicemente il vincitore, viene stilata una classifica, ovvero un ***ranking***

Infine, naturalmente possono essere considerate numerose regole per derivare una decisione collettiva a partire da un insieme di decisioni individuali, ed esse prendono il nome di **sistemi di voto**
## Voto Individuale

Formalizziamo il concetto di voto individuale:
- $A=\{a_1,a_2,\dots,a_n\}$ è un insieme di alternative
- $V=\{v_1,v_2,\dots,v_k\}$ è un insieme di votanti

Ciascun votante $v_h\in V$ esprime il suo voto in una di due forme possibili:
1) nella forma di una **graduatoria (ranking)** $r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$
	1) ovvero una sequenza ordinata delle $n$ alternative, nella quale al primo posto si trova l'alternativa preferita fra tutte, al secondo posto la seconda scelta, etc..
	2) un ranking è quindi un elemento dell'insieme $\Pi(A)$, ovvero l'elemento delle permutazioni degli elementi di $A$
2) nella forma di **relazione binaria completa e transitiva $\gt_{h}$**
	1) *completa*: per ogni coppia di alternative $a$ e $a'$, vale che $a\gt_{h}a'$ oppure $a'\gt_{h}a$ (ricordiamo che $a\gt_{h}a'$ significa che $a$ è preferito ad $a'$ per il votante $h$)
	2) *transitiva*: se $a\gt_{h}a'$ e $a'\gt_{h}a''$ allora $a\gt_{h}a''$. per qualunque terna di alternative $a,a',a''$

Le due forme possibili di espressione di un voto sono fra loro equivalenti

Derivare una relazione binaria completa e transitiva $\gt_h$ da ranking $r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$ è immediato: per ogni indice $i\in[n]$ e per ogni indice $j\in [n]$ tale che $j\gt i$, poniamo $a_{hi}\gt_h a_{hj}$ 

Derivare un ranking $r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$ da una relazione binaria completa e transitiva $\gt_h$ è invece un compito più complesso.
Allo scopo, procediamo come segue:
- poichè $\gt_{h}$ è completa e transitiva, allora esiste $l\in [n]$ tale che, per ogni $j\in[n]\setminus\{l\}$ vale che $$|\{i\in[n]:a_l\gt_h a_i\}|\gt|\{i\in[n]:a_{j}\gt_{h}a_i\}|$$
	- lemma 1, dimostrato più avanti
- allora, per ogni $j\in[n]\setminus\{l\}$ vale che $a_l\gt_h a_j$
	- lemma 2, dimostrato più avanti
- Quindi poniamo $a_{h1}=a_l$ e, osservando che $\gt_h$ è completa e transitiva sull'insieme $A\setminus\{a_{h1}\}$, ripetiamo il ragionamento sull'insieme $A\setminus\{a_{h1}\}$ per individuare $a_{h2}$, e così via per individuare $a_{h3},\dots,a_{hn}$

Dimostriamo quindi i due lemmi appena citati

>[!teorem]- Lemma 1
>Se $\gt_h$ è una relazione binaria completa e transitiva nell'insieme $A=\{a_1,a_2,\dots,a_n\}$, allora esiste $l\in[n]$ tale che, per ogni $j\in[n]\setminus\{l\}$ vale che $$|\{i\in[n]:a_l\gt_h a_i\}|\gt|\{i\in[n]:a_{j}\gt_{h}a_i\}|$$

**dimostrazione**:

Per ogni alternativa $j\in[n]$, indichiamo con $p_{j}$ il numero di alternative che $j$ batte nel voto del votante $h$: $$p_j=|\{i\in[n]:a_j\gt_ha_{i}\}|$$

Supponiamo che esista $m\in[n]\setminus\{l\}$ tale che $$p_l=|\{i\in[n]:a_l\gt_h a_i\}|=|\{i\in[n]:a_m\gt_h a_i\}|=p_m$$
Poichè $\gt_h$ è completa e transitiva, allora $a_{l}\gt_h a_m$ oppure $a_{m}\gt_h a_l$

Vediamo le due casistiche:

1) $a_{m}\gt_h a_l$ : poichè $\gt_h$ è completa e transitiva allora, per ogni $j$ tale che $a_{l}\gt_h a_j$ si ha che $a_{m}\gt_h a_j$, ovvero $\{i\in[n]:a_l\gt_h a_i\}\cup\{a_l\}\subseteq\{i\in[n]:a_{m}\gt_h a_i\}$,e quindi poichè $a_{l}\not\in\{i\in[n]:a_l\gt_{h}a_i\}$ vale che $$p_m=\left|\{i\in[n]:a_{m}\gt_h a_i\}\right|\geq|\{i\in[n]:a_{l}\gt_h a_i\}|+1\gt|\{i\in[n]:a_{l}\gt_h a_i\}|=p_l$$che è assurdo: $p_{l}=p_m$ e $p_m\gt p_{l}$


  
## Sistemi di voto - maggioranza
## Sistemi di voto - posizionali

## Sistemi di voto - affidabili

## Due principi per i sistemi di voto
### Il teorema di impossibilità di Arrow





[^1]: Ovvero, *assumendo* che gli altri giocatori rispondano *sinceramente* (in accordo ai loro segnali privati), le risposte degli altri due giocatori sono discordi quando uno di loro estrae una pallina verde, e quindi quando l'urna è $UV$
