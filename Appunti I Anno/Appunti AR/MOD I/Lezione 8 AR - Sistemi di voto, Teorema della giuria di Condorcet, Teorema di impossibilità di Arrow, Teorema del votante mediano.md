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

Quando si deve decidere se un imputato è colpevole $(C)$ o innocente $(I)$, e a priori vale che $$Pr(C)=Pr(I)= \frac{1}{2}$$ciascun girato riceve un segnale $c$ o  $i$, come nel caso dell'herding, e quindi $$Pr(c|C)=Pr(i|I)=q\gt \frac{1}{2}$$In questo caso occorre aggregare i voti dei giurati per giungere a un verdetto di colpevolezza o di innocenza, e per condannare un imputato è necessario che l'insieme $S$ dei segnali ricevuti dai giurati siano indice di colpevolezza con prob. molto alta (è richiesto che $Pr(C|S)\gg \frac{1}{2}$)

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
Certamente, esiste $l\in[n]$ tale che, per ogni $j\in[n]\setminus\{l\}$ $$p_l=|\{i\in[n]:a_l\gt_h a_i\}|\geq|\{i\in[n]:a_j\gt_h a_i\}|=p_j$$
Supponiamo ora che esista $m\in[n]\setminus\{l\}$ tale che $$p_l=|\{i\in[n]:a_l\gt_h a_i\}|=|\{i\in[n]:a_m\gt_h a_i\}|=p_m$$
Poichè $\gt_h$ è completa e transitiva, allora $a_{l}\gt_h a_m$ oppure $a_{m}\gt_h a_l$

Vediamo le due casistiche:

1) $a_{m}\gt_h a_l$ : poichè $\gt_h$ è completa e transitiva allora, per ogni $j$ tale che $a_{l}\gt_h a_j$ si ha che $a_{m}\gt_h a_j$, ovvero $\{i\in[n]:a_l\gt_h a_i\}\cup\{a_l\}\subseteq\{i\in[n]:a_{m}\gt_h a_i\}$,e quindi poichè $a_{l}\not\in\{i\in[n]:a_l\gt_{h}a_i\}$ vale che $$p_m=\left|\{i\in[n]:a_{m}\gt_h a_i\}\right|\geq|\{i\in[n]:a_{l}\gt_h a_i\}|+1\gt|\{i\in[n]:a_{l}\gt_h a_i\}|=p_l$$che è assurdo: $p_{l}=p_m$ e $p_m\gt p_{l}$
2) $a_l\gt_h a_{m}$ : poichè $\gt_h$ è completa e transitiva allora, per ogni $j$ tale che $a_{m}\gt_h a_j$ si ha che $a_{l}\gt_h a_j$, ovvero $\{i\in[n]:a_m\gt_h a_i\}\cup\{a_m\}\subseteq\{i\in[n]:a_{l}\gt_h a_i\}$,e quindi poichè $a_{m}\not\in\{i\in[n]:a_m\gt_{h}a_i\}$ vale che $$p_l=\left|\{i\in[n]:a_{l}\gt_h a_i\}\right|\geq|\{i\in[n]:a_{m}\gt_h a_i\}\cup\{a_m\}|\gt|\{i\in[n]:a_{m}\gt_h a_i\}|=p_m$$che è assurdo: $p_{l}=p_m$ e $p_l\gt p_{m}$

In entrambi i casi viene contraddetto quanto supposto circa $m$, e quindi $m$ non esiste, per ogni $j\in[n]\setminus\{l\}$ vale che $$|\{i\in[n]:a_l\gt_h a_i\}|\gt|\{i\in[n]:a_{j}\gt_{h}a_i\}|\quad\blacksquare$$

>[!teorem]- Lemma 2
>Sia $\gt_h$ una relazione binaria completa e transitiva nell'insieme $A=\{a_1,a_2,\dots,a_n\}$ e sia $l\in[n]$ tale che, per ogni $j\in[n]\setminus\{l\}$ vale che $$|\{i\in[n]:a_l\gt_h a_i\}|\gt|\{i\in[n]:a_{j}\gt_{h}a_i\}|$$
>Allora: $$\forall j\in[n]\setminus\{l\},a_l\gt_ha_j$$

**dimostrazione**

Osserviamo che $l\in[n]$ tale che, per ogni $j\in[n]\setminus\{l\}$ vale che $$|\{i\in[n]:a_l\gt_h a_i\}|\gt|\{i\in[n]:a_{j}\gt_{h}a_i\}|$$esiste in virtù del Lemma $1$

Supponiamo che esista un $m\in[n]\setminus\{l\}$ tale che $a_m\gt_ha_l$

Allora, per transitività di $\gt_h$, per ogni $j$ tale che $a_l\gt_ha_{j}$ si avrebbe che $a_m\gt_ha_j$, e quindi avremmo che $$\{i\in[n]:a_l\gt_h a_i\}\cup\{a_l\}\subseteq\{i\in[n]:a_{m}\gt_{h}a_i\}$$
E quindi, dato che $a_l\not\in\{i\in[n]:a_l\gt_h a_i\}$, allora $$|\{i\in[n]:a_m\gt_h a_i\}|\gt|\{i\in[n]:a_{l}\gt_{h}a_i\}|$$il che è un assurdo. $\blacksquare$

Abbiamo quindi detto che il sistema di voto è una *regola* che permette di associare un voto collettivo ad un insieme di voti individuali

Descriviamo formalmente questo concetto:
- poichè sono irrilevanti i nomi delle aternative e dei votanti, possiamo indentificare $A$ con l'insieme $[n]$ e $V$ con l'insieme $[k]$
- Per fissare le idee, assumiamo che i $k$ votanti esprimano i loro voti mediante ranking
- Un ***voto aggregato per $n$ alternative e $k$ votanti*** è quindi una funzione $$f_{n,k}:\Pi([n])^{k}\to\Pi([n])$$in modo che $$f_{n,k}(r_1,r_2,\dots,r_k)=r,\quad r_1,r_2,\dots,r_k,r\in\Pi([n])$$

Un **sistema di voto** è quindi un predicato $\sigma$ che specifica, per ogni $r_1,r_2,\dots,r_k\in\Pi([n])^k$ le regole che devono essere rispettate dal voto aggregato $f_{n,k}(r_1,r_2,\dots,r_k)$

Esistono vari tipi di sistema di voto, vediamone alcuni
## Sistemi di voto - maggioranza

>[!warning]- Predicato del sistema di voto a maggioranza
>Supponiamo che i voti individuali dei $k$ votanti siano espressi mediante relazioni binarie $\gt_1,\gt_2,\dots,\gt_k$ e indichiamo con $\succ$ la relazione binaria $f_{n,k}(\gt_1,\gt_2,\dots,\gt_k)$
>Il sistema di voto a maggioranza è quindi descritto dal predicato $\sigma_{M}$ tale che: $$\sigma_M(\gt_1,\gt_2,\dots,\gt_k)=\forall i,j\in[n]\left[i\succ j \iff |\{h\in[k]:i\gt_hj\}|\gt|h\in[k]:j\gt_hi|\right]$$
>Ovvero, nella votazione finale $i$ è preferito a $j$ se eoslo se $i$ è preferito a $j$ dalla maggioranza dei votanti

Il **sistema di voto a maggioranza** è un sistema molto semplice ed intuitivo, in particolar modo quando le aternative fra le quali scegliere sono due.

Tuttavia, se le alternative sono più di due potrebbero esserci problemi, vediamoli con un esempio

Consideriamo la situazione seguente: tre amici in vancanza, con budget limitato, devono scegliere se acquistare miele, cioccolata o marmellata
- Mario preferisce su tutto la cioccolata, poi la marmellata e infine il miele, quindi vale che $$\text{cioccolata}\gt_{M}\text{marmellata}\gt_{M}\text{miele}$$
- Paolo preferisce su tutto la marmellata, poi il miele e infine la cioccolata, quindi vale che  $$\text{marmellata}\gt_{P}\text{miele}\gt_{P}\text{cioccolata}$$
- Roberto preferisce su tutto il miele, poi la cioccolata e infine la marmellata, quindi vale che $$\text{miele}\gt_{R}\text{cioccolata}\gt_{R}\text{marmellata}$$
- Sono tutte e tre relazioni binarie complete e transitive

Tuttavia, se proviamo a produrre una relazione binaria $\succ$, aggregando secondo la regola della maggioranza le tre relazioni, otteniamo che 
- cioccolata è preferita a marmellata da due votanti $\to$ cioccolata $\succ$ marmellata
- marmellata è preferita a miele da due votanti $\to$ marmellata $\succ$ miele
- miele è preferito a cioccolata da due votanti $\to$ miele $\succ$ cioccolata

Otteniamo quindi che $$\text{cioccolata}\succ\text{marmellata}\succ\text{miele}\succ\text{cioccolata}$$
E in particolare, anche se cioccolata $\succ$ marmellata e marmellata $\succ$ miele **non è vero che** cioccolata $\succ$ miele, di conseguenza la relazione $\succ$ risulta **non essere transitiva**

La situazione appena descritta costituisce il **paradosso di Condorcet**: anche se le relazioni binarie individuali sono transitive, la relazione binaria collettiva ottenuta dalla loro aggregazione può non essere transitiva

Osserviamo quindi che la richiesta di transitività è necessaria affinchè l'aggregazione dei voti individuali sia significativa, perciò potrebbe essere problematico usare il sistema a maggioranza con **più di due alternative**

Partendo dal sistema a maggioranza possiamo costruire un nuovo sistema di voto, che non soffre più del paradosso di Condorcet: ***il torneo***
## Sistemi di voto - il torneo

I $k$ votanti esprimono ancora le proprie preferenze mediante relazioni binarie $\gt_1,\gt_2,\dots,\gt_{k}$, ma la graduatoria finale viene costruita sulla base di una successione di scontri diretti

**Se** si scontrano le due alternative $a$ e $a'$, risulterà $a\succ a'$ se $$|\{i\in[k]:a\gt_{i}a'\}|\gt|\{i\in[k]:a'\gt_{i}a\}|$$
- Ovviamente se $k$ è dispari allora per ogni coppia di alternative $a$ e $a'$ si avrà che $a\succ a'$ oppure $a'\succ a$, ovver si riuscirà sempre ad avere un vincitore nello scontro diretto

![[Pasted image 20250825154009.png|center|350]]

In un torneo non hanno luogo tutti gli scontri possibili, ma solo quelli fissati da una agenda.

Di conseguenza, **l'agenda può avere un ruolo determinante nel decretare il vincitore**

Esempio: torniamo ai tre coglioni in vacanza:
- Mario propone l'agenda secondo la quale il primo scontro è marmellata-miele e il vincitore si scontrerà con cioccolata
- Paolo propone l'agenda secondo la quale il primo scontro è miele-cioccolata e il vincitore si scontrerà con marmellata
- Roberto propone l'agenda secondo la quale il primo scontro è cioccolata-marmellata e il vincitore si scontrerà con miele
- Essendo che avevamo già osservato che cioccolata $\succ$ marmellata, marmellata $\succ$ miele e miele $\succ$ cioccolata, allora:
	- nell'agenda di Mario vincerà la cioccolata, in quella di Paolo la marmellata e in quella di Roberto il miele
	- quindi, ciascun amico ha proposto una agenda che portasse alla vittoria il proprio prodotto

Di conseguenza, alla luce di quanto descritto, possiamo affermare che il sistema di voto "a torneo" è sensibile allo **strategic agenda setting**
## Sistemi di voto - posizionali

Supponiamo ora che i voti individuali siano espressi mediante ranking, così che il voto del votante $h$ risulti essere $$r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$$
A ciascun ranking $r_{h}$ possiamo associare una funzione peso che assegna un valore numerico a ciascuna alternativa dipendentemente dalla sua posizione nel ranking:
- ad esempio, al ranking $r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$ possiamo associare la funzioen $w_h$ tale che $w_h(a_{hi})=100-10i$
- tipicamente la funzione peso è **decrescente nella posizione**

In un sistema posizionale quindi, dopo aver associato una funzione peso $w_h$ al ranking $r_h$, per ogni $h\in[k]$, il ranking collettivo $r$ è ottenuto:
- calcolando il peso totale di ciascuna alternativa come somma dei pesi che quella alternativa ha negli $h$ ranking, ovvero per ogni $a\in[n],w_(a)=\sum\limits_{1\leq h\leq k}w_h(a)$
- e poi ordinando le alternative secondo il loro peso totale

Il **Borda Count** è un particolare sistema di voto posizionale nel quale:
- per ogni $h\in[k]$, la funzione peso associata al ranking $r_{h}$ è la funzione suriettiva $$\rho_{h}:A\to\{0.1,\dots,n-1\}\text{ tale che }\rho_h(a_{hi})=n-i$$
- e le alternative vengono **ordinate per peso finale** $\rho$ non crescente

Anche nei sistemi posizionali si manifesta il paradosso di Condorcet, sotto forma di *ex aequo*

Esempio: torniamo ancora una volta all'esempio dei tre coglioni, e consideriamo i tre ranking corrispondenti alle relazioni di equivalenza e applichiamo il Borda Count:
- $r_{\text{mario}}=\langle\text{cioccolata, marmellata, miele}\rangle$ da cui otteniamo che $$\rho_{M}(\text{cioccolata})=2,\rho_{M}(\text{marmellata})=1,\rho_{M}(\text{miele})=0$$
- $r_{\text{paolo}}=\langle\text{marmellata, miele, cioccolata}\rangle$ da cui otteniamo che $$\rho_{P}(\text{cioccolata})=0,\rho_{P}(\text{marmellata})=2,\rho_{P}(\text{miele})=1$$
- $r_{\text{roberto}}=\langle\text{miele, cioccolata, marmellata}\rangle$ da cui otteniamo che $$\rho_{R}(\text{cioccolata})=1,\rho_{R}(\text{marmellata})=0,\rho_{R}(\text{miele})=2$$
- e quindi, abbiamo che $$\rho(\text{cioccolata})=3,\rho(\text{marmellata})=3,\rho(\text{miele})=3$$

In questi sistemi di voto, il problema degli ex aequo viene trattato in vari modi che noi non tratteremo (non ce ne frega un emerito cazzo)

Ci occupiamo di un'altra caratteristica indesiderabile dei sistemi di voto posizionali che introduciamo con un esempio

Esempio: cinque critici cinematografici devono scegliere se assegnare un premio al film "Il Padrino" o "Via col vento"
- Tre critici preferiscono "Via col vento" (VV) e gli altri due "Il Padrino" (IP), e detta così il premio andrebbe a VV
- Prima di arrivare alla votazione finale però, il comitato organizzatore decide di inserire fra le alternative anche "Pulp Fiction" (PF)
- Ciascuno dei cinque critici ritiene che PF sia inadatto alla competizione, però i due che preferiscono IP a VV si accorgono che possono ricorrere ad un espediente: possono entrambi votare secondo il ranking $\langle\text{IP,PF,VV}\rangle$, mentre i tre che preferiscono VV votano onestamente secondo il ranking $\langle\text{VV,IP,PF}\rangle$
- In questo modo, si avrà che $\rho(VV)=6,\rho(IP)=7,\rho(PF)=2$, facendo così vincere IP

Inserendo in posizione opportuna PF, i due che preferivano IP hanno fatto in modo che esso vincesse, e per farlo hanno classificato l'**alternativa irrilevante** ai fini della vittoria in posizione intermedia che non corrispondeva al loro giudizio[^2]

Riconsideriamo i ranking dei due gruppi di critici: $\langle\text{VV,IP,PF}\rangle$ e $\langle\text{IP,PF,VV}\rangle$

Osserviamo che, se ci limitiamo ad osservare le posizioni relative di $VV$ e $IP$ nei due ranking, $VV$ **precede** IP nella maggioranza dei votanti, e quindi sarebbe ragionevole aspettarsi che questo ordine venga rispettato nel voto collettivo, indipendentemente da come viene posizionato PF

Invece, il posizionamento opportuno di PF da parte di due votanti ha permesso di modificare le posizione relative di VV e IP nella graduatoria finale, e questo è un problema.
## Sistemi di voto affidabili

Fino a questo momento abbiamo incontrato tre sistemi di voto, quello a maggioranza, il torneo e il sistema di voto posizionale, dei quali non possiamo fidarci completamente
- perché non riescono sempre ad individuare una graduatoria finale
- perché la graduatoria finale dipende dall’ordinamento iniziale delle alternative
- perché i votanti possono “barare” per orientare la graduatoria finale

Ci domandiamo, a questo punto, se sia possibile progettare sistemi di voto affidabili

Ma la domanda sorge spontanea: quando un sistema di voto può essere considerato affidabile?
Come minimo, per essere considerato affidabile, un sistema di voto dovrebbe garantire
- la rappresentazione delle scelte di tutti i votanti nel caso in cui esse siano tutte concordi
- di non consentire l’utilizzo di alternative irrilevanti per orientare la graduatoria finale

E il paradosso di Condorcet? Non ci interessa più garantire che un sistema di voto non soffra di tale anomalia?! 
La risposta è sì e no

Nel senso che nei sistemi di voto che prenderemo in considerazione il voto aggregato (o collettivo) viene descritto mediante un ranking, e un ranking corrisponde sempre ad una relazione binaria transitiva
- e, per inciso, per poter produrre un ranking potrebbe essere necessario introdurre anche una regola che risolva gli ex aequo

Pertanto, per così dire, il paradosso di Condorcet viene eliminato alla radice
## Due principi per i sistemi di voto

Sia $\sigma$ un sistema di voto:
- sia $[n]$ un insieme di alternative e $[k]$ un insieme di votanti tali che, per ogni $h\in[k]$, il votante $h$ esprime il ranking $r_{h}=\langle a_{h1},a_{h2},\dots,a_{hn}\rangle$ sulle $n$ alternative
- indichiamo con $r$ il voto collettivo corrispondente ai voti individuali $r_{1},r_2,\dots,r_k$ derivato in accordo a $\sigma$ - ovvero $\sigma(r_{1},r_2,\dots,r_k)=\text{TRUE}$
- siano, per ogni $h\in[k],\rho_h$ la funzione peso (relativa al Borda Count) associata a $r_{h}$ e $\rho$ la funzione peso associata a $r$

I due principi che un sistema di voto deve avere sono i seguenti:

>[!teorem]- Principio di Unanimità (U)
>Il sistema di voto $\sigma$ soddisfa il **principio di unanimità** se $$\forall i,j\in[n]\left[\forall h\in[k]\rho_{h}(i)\gt\rho_{h}(j)\implies\rho(i)\gt\rho(j)\right]$$
>Cioè, **ogni qualvolta *tutti* i votanti preferiscono un'alternativa $i$ a un'alternativa $j$, allora $i$ è preferita a $j$ anche nella graduatoria finale**

>[!teorem]- Principio di Indipendenza dalle Alternative Irrilevanti (IIA)
>Il sistema di voto $\sigma$ soddisfa il **principio di indipendenza dalle alternative irrilevanti** se
>$$\begin{align*} &\forall i,j\in[n]\forall(r_1,r_{2},\dots,r_k),(r'_1,r'_{2},\dots,r'_k)\in\Pi([n])^{k}\\&\left[\forall h\in[k]:\rho_{h}(i)\gt\rho_{h}(j)\iff\rho'_{h}(i)\gt\rho'_{h}(j)\right]\implies\left[\rho(i)\gt\rho(j)\iff\rho'(i)\gt\rho'(j)\right]\end{align*}$$[^3]
>Questa formula si spiega così: ogni qualvolta si considerino due insieme di $k$ votanti per i quali due alternative $i,j$ hanno le stesse posizioni relative per ***tutte*** le coppie di votanti *omologhi*, allora $i,j$ hanno la stessa posizione relativa anche nelle graduatorie finali relative ai due gruppi di votanti.
>Ovvero, **la posizione relativa di due alternative nella graduatoria finale dipende unicamente dalle posizioni relative delle due alternative nelle graduatorie individuali**

Vediamo ora questo mostro di teorema del porco buddha
### Il teorema di impossibilità di Arrow

Il ***teorema di Arrow*** individua l'unico sistema di voto che rispetta i principi $U$ e $IIA$

>[!teorem]- Teorema di Arrow
>Se il sistema di voto $\sigma$ soddisfa i principi $U$ e $IIA$, allora per ogni $k\in\mathbb N$ e per ogni $n\in\mathbb N$ tale che $n\gt2$ esiste $j\in[k]$ tale che, per ogni $k-$upla $\langle r_{1},r_2,\dots,r_k\rangle$ di ranking per $n$ alternative, il voto collettivo corrispondente ai voti individuali $r_{1},r_2,\dots,r_k$ derivato in accordo a $\sigma$ è $r=r_j$

Riassumiamo: *per ogni insieme* $[k]$ di votanti esiste un $j\in[k]$ tale che il voto colelttivo corrispondente ai voti individuali $r_{1},r_2,\dots,r_k$ dei $k$ votanti derivato in accordo a $\sigma$ è $r=r_j$

Quindi, *per ogni insieme $[k]$ esiste $j\in[k]$ tale che $r=r_j$*, e di conseguenza, ***l'unico sistema di voto che rispetta U e IIA è la dittatura***

**Dimostrazione** : 

Prima di procedere con la dimostrazione abbiamo bisogno di qualche definizione:
- **profilo** : dati un insieme $[n]$ di alternative e un insieme di $[k]$ votanti, un profilo p una $k-$upla $P=\langle r_{1},r_2,\dots,r_k\rangle$ di ranking - ciascuno espressione del voto di uno dei votanti per quelle alternative
	- esempio: un profilo di $6$ votanti $(r_{1},r_2,\dots,r_6)$ su $4$ alternative (a,b,c,d) ![[Pasted image 20250825174521.png|center|200]]
- **alternativa polarizzante** : dati un insieme $[n]$ di alternative, un insieme di $[k]$ votanti e un profilo $P=\langle r_{1},r_2,\dots,r_k\rangle$, una alternativa polarizzante per $P$ è un alternativa $x\in[n]$ tale che, per ogni $h\in[k],\rho_h(x)=0$ oppure $\rho_h(x)=n-1$
	- esempio: ![[Pasted image 20250825174824.png|center|200]]

Dimostriamo il teorema di Arrow in tre passi:
1) dimostriamo che se $x$ è un'alternativa polarizzante per un profilo $P=\langle r_{1},r_2,\dots,r_k\rangle$ allora $\rho(x)=0$ oppure $\rho(x)=n-1$
	1) al solito, $\rho$ è la funzione peso associata al voto collettivo $r$ (che soddisfa $\sigma$) corrispondente a $P$
2) definiamo una successione di $k+1$ profili in ciascuno dei quali una stessa $x\in[n]$ è polarizzante e, tramite essi, individuiamo un **dittatore potenziale**
	1) $\sigma$ è un sistema di voto: allora è in grado di esprimere un voto collettivo per ogni profilo possibile per n alternative e k votanti
	2) e, dunque, anche per i k profili nei quali x è polarizzante
3) dimostriamo che il dittatore potenziale è, effettivamente, il dittatore cercato

#### Dimostrazione parte 1

Dimostriamo la parte $1)$: se $x$ è un'alternativa polarizzante per un profilo $P=\langle r_{1},r_2,\dots,r_k\rangle$ allora $\rho(x)=0$ oppure $\rho(x)=n-1$

Supponiamo per assurdo che $0\lt\rho(x)\lt n-1$: allora esistono due alternative $y,z\in[n]$ tali che $\rho(z)\lt\rho(x)\lt\rho(y)$

Creiamo un nuovo profilo $P'=\langle r'_{1},r'_2,\dots,r'_k\rangle$ nel modo seguente:
1) per ogni $i\in[k]$ tale che $\rho_{i}(y)\lt\rho_i(z)$, impostiamo $r'_i=r_i$
2) per ogni $i\in[k]$ tale che $\rho_{i}(y)\gt\rho_i(z)$, $r'_{i}$ è ottenuto da $_i$ spostando $z$ alla sinistra di $y$, in modo che $\rho'_i(z)=\rho'_{i}(y)+1$ ![[Pasted image 20250825180145.png|center]]

Poichè $x$ non è stata in alcun modo coinvolta negli spostamenti, $x$ è un'alternativa polarizzante anche per $P'$

Inoltre, per ogni $i \in [k]$, in $r_i$ e $r’_i$ non sono variati gli ordini relativi di $x$ e $y$ e di $x$ e $z$, inoltre, per ogni $i \in [k] \rho'_i(y) \lt\rho'_i(z)$

Poiché per ogni $i \in [k]$, in $r_i$ e $r’_i$ non sono variati gli ordini relativi di $x$ e $z$, allora, per il **principio IIA** vale che $$\rho(x) \lt \rho(z) \iff \rho'(x) \lt \rho'(z)$$
- ma abbiamo supposto $\rho(z)\lt\rho(x)\lt\rho(y)$: allora $\rho'(z) \lt \rho'(x)$

Poiché per ogni $i \in [k]$, in $r_i$ e $r’_i$ non sono variati gli ordini relativi di $x$ e $y$ , allora, per il **principio IIA** vale che $$\rho(x) \lt \rho(y) \iff \rho'(x) \lt \rho'(y)$$
- ma abbiamo supposto $\rho(z)\lt\rho(x)\lt\rho(y)$: allora $\rho'(x) \lt \rho'(y)$

Inoltre, per ogni $i \in [k]\rho'_i(y) \lt \rho'_i(z)$: allora, per il **principio U** deve valere che $\rho'(y) \lt \rho'(z)$, e quindi $$\rho'(z) \lt \rho'(x)\lt\rho'(y) \lt \rho'(z)$$
Il che **è un assurdo**, e quindi $\rho(x)=0$ oppure $\rho(x)=n-1$

#### Dimostrazione parte 2

Dimostriamo ora la parte $2)$ : definiamo una successione di $k+1$ profili in ciascuno dei quali una stessa $x \in [n]$ è polarizzante e, tramite essi, individuiamo un dittatore potenziale

Scegliamo $x\in[n]$.

Nel profilo $P^0=\left\langle r_1^0,r_2^0,\dots,r_k^0\right\rangle$ l'alternativa $x$ è in ultima posizione in tutti i ranking: $$\forall i\in[k],\rho_i^{0}(x)=0$$

Nel profilo $P^1=\left\langle r_1^1,r_2^1,\dots,r_k^1\right\rangle$ l'alternativa $x$ è in prima posizione nel ranking $r_{1}^1$, in ultima posizione in tutti gli altri ranking: $$\begin{align*}
&\rho_1^1(x)=n-1\\&\forall i\in[k]\setminus\{1\},\rho_i^1(x)=0
\end{align*}$$

In generale, nel profilo $P^h=\left\langle r_1^h,r_2^h,\dots,r_k^h\right\rangle$ l'alternativa $x$ è in prima posizione nei ranking $r_{1}^h$ con $i\leq h$, in ultima posizione in tutti gli altri ranking: $$\begin{align*}
&\forall i\leq h,\rho_1^h(x)=n-1\\&\forall i\gt h,\rho_i^h(x)=0
\end{align*}$$

Per ogni $h\in\{0,1,\dots,k\}$ indichiamo con $r^h$ il ranking collettivo associato al profilo $P^{h}$, e con la funzione $\rho^{h}$ la funzione peso ad esso associata

![[Pasted image 20250826143232.png|center|500]]

I due profili $P^{h-1}$ e $P^{h}$ differiscono solo per il modo in cui l'$h$-esimo votante giudica $x$: nel profilo $P^{h-1}$ l'$h$-esimo votante giudica $x$ in ultima posizione ($\rho_{h}^{h-1}(x)=0$), mentre nel profilo $P^{h}$ l'$h$-esimo votante giudica $x$ in prima posizione ($\rho_{h}^{h}(x)=n-1$), e le posizioni relative delle altre alternative rimangono invariate nei due profili

![[Pasted image 20250826143513.png|center|500]]

In virtù del principio $U$ (unanimità) vale che $$\rho^{0}(x)=0,\rho^{k}(x)=n-1$$
Allora $$\exists\text{ un profilo }j\in[k]:\rho^{h}(x)=0\space\forall h\lt j\space\land\space\rho^{j}(x)\gt0$$[^4]

E quindi, dato che $x$ è polarizzante per $P^{j}$ e $\rho^{j}(x)=n-1$, osserviamo che il votante $j$ ha molto potere nel posizionare $x$ nella graduatoria finale: la fa passare dall'ultima alla prima posizione.

**$j$ è quindi il dittatore potenziale** ^988d91
#### Dimostrazione parte 3

Dimostriamo il punto $3)$ : dimostriamo che $j$ è il dittatore cercato

Sia $Q=\left\langle r_1^Q,r_2^Q,\dots,r_k^Q\right\rangle$ un profilo di $k$ votanti per $n$ alternative

Per ogni $h\in[k]$ indichiamo con $\rho_h^{Q}$ la funzione peso associata a $r_h^{Q}$, e indichiamo con $r^{Q}$ il ranking collettivo (**che soddisfa $\sigma$**) corrispondente a $Q$ e con $\rho^{Q}$ la funzione peso associata a $r^{Q}$

Dobbiamo mostrare che **qualunque sia $Q,r^{Q}=r_{j}^{Q}$**
Ovvero, qualunque sia $Q$, comunque si scelgano due alternative $y,z\in[n]$, sia ha che $$\rho^{Q}(y)\gt\rho^{Q}(z)\iff\rho_j^{Q}(y)\gt\rho_j^{Q}(z)$$
Realizziamo questo obiettivo in $2$ passi:
- 3.1) dimostriamo che se $y\neq x$ e $z\neq x$ allora $\rho^{Q}(y)\gt\rho^{Q}(z)\iff\rho_j^{Q}(y)\gt\rho_j^{Q}(z)$
- 3.2) dimostriamo che se $y\neq x$ alora $\rho^{Q}(y)\gt\rho^{Q}(x)\iff\rho_j^{Q}(y)\gt\rho_j^{Q}(x)$

##### Dimostrazione parte 3.1

Senza perdità di generalità, supponiamo che sia $$\rho_j^{Q}(y)\gt\rho_j^{Q}(z)$$
Costruiamo da $Q$ un nuovo profilo $T$:
- Prima di tutto, per ogni $h\leq j$, poniamo $x$ in testa di $r_h^{T}$ lasciando tutte le altre alternative nello stesso ordine nel quale si trovano in $r_{h}^{Q}$
- Poi, per ogni $h\gt j$, poniamo $x$ in coda di $r_h^{T}$ lasciando tutte le altre alternative nello stesso ordine nel quale si trovano in $r_h^{Q}$
- Infine, spostiamo $y$ dalla posizione in cui si trova in $r_{j}^{Q}$ ponendola in testa a $r_{j}^{T}$

![[Pasted image 20250826145226.png|center|500]]

$T$ è molto simile a $P^{j}$:

![[Pasted image 20250826145348.png|center|500]]

Dato che $\rho^{j}(x)=n-1$ (come abbiamo visto [[Lezione 8 AR - Sistemi di voto, Teorema della giuria di Condorcet, Teorema di impossibilità di Arrow, Teorema del votante mediano#Dimostrazione parte 2|qui]]) allora $\rho^{j}(x)\gt\rho^{j}(z)$, ed essendo che l'ordine relativo di $x$ e $z$ è lo stesso sia in $P^{j}$ che in $T$, allora, per il principio $IIA$ vale che $$\rho^{T}(x)\gt\rho^{T}(z)$$
$T$ però è anche molto simile a $P^{j-1}$

![[Pasted image 20250826150026.png|center|500]]

Dato che $\rho^{j-1}(x)=0$ (come abbiamo visto [[Lezione 8 AR - Sistemi di voto, Teorema della giuria di Condorcet, Teorema di impossibilità di Arrow, Teorema del votante mediano#Dimostrazione parte 2|qui]]) allora $\rho^{j-1}(x)\lt\rho^{j-1}(y)$, ed essendo che l'ordine relativo di $x$ e $y$ è lo stesso sia in $P^{j-1}$ che in $T$, allora, per il principio $IIA$ vale che $$\rho^{T}(x)\lt\rho^{T}(y)$$

Ricapitolando:

- Abbiamo costruito da $Q$ il nuovo profilo $T$ nel quale $x$ è in testa di $r_h^{T}$ per $h \lt j$, $y$ è in testa seguito da $x$ in $r_j^{T}$ e $x$ è in coda di $r_j^{T}$ con $h \gt j$
- Dalla stessa posizione relativa di $x$ e $z$ in $P^j$ e in $T$, dal fatto che $\rho^j(x) \gt \rho^j(z)$, e in virtù del principio $IIA$, abbiamo concluso che $$\rho^{T}(x)\gt\rho^{T}(z)$$
- Dalla stessa posizione relativa di $x$ e $y$ in $P^{j-1}$ e in $T$, dal fatto che $\rho^j(x) \lt \rho^j(y)$, e in virtù del principio $IIA$, abbiamo concluso che $$\rho^{T}(x)\lt\rho^{T}(y)$$
E quindi, $$\rho^{T}(y)\gt\rho^{T}(z)$$
Osserviamo che, per tutti i votanti, l’ordine relativo di $z$ e $y$ è lo stesso in $Q$ e in $T$ e quindi, per il principio $IIA$, deve valere che $$\rho^Q(y) \gt \rho^Q(z)$$
E naturalmente, essendo che $y,z$ sono interscambiabili (variabili mute), questo rpova anche che se $$\rho_j^{Q}(y)\lt\rho_j^{Q}(z)\implies\rho^{Q}(y)\lt\rho^{Q}(z)$$
##### Dimostrazione parte 3.2

Poichè $n\gt2$ allora esiste un $z\in[n]$ tale che $z\neq x\land z\neq y$

Deriviamo da $P^{0},P^{1},\dots,P^{k}$ una nuova sequenza $T^{0},T^{1},\dots,T^{k}$ di profili spostando l'alternativa $z$:
- indichiamo $T^{h}=\left\langle t_1^h,t_2^h,\dots,t_k^h\right\rangle$
- $T^0$ è ottenuto spostando $z$ in ultima posizione in ciascun ranking del profilo $P^{0}$
- per $h\gt0,T^h$ è ottenuto dal profilo $P^{h}$: l'alternativa $z$ viene spostata in prima posizione nei ranking $t_i^h$ con $i\leq h$, in ultima posizione in tutti gli altri ranking, ovvero:$$\begin{align*}&\forall\space i\leq h,\rho_{i}^{T^{h}}(z)=n-1\\&\forall\space i\gt h,\rho_{i}^{T^{h}}(z)=0\\\end{align*}$$

Per ogni $h\in\{0,1,\dots,k\}$ indichiamo con $t^h$ il ranking collettivo associato a $T^{h}$, e con $\rho^{T^{h}}$ la funzione peso ad esso associata

La nuova sequenza $T^{0},T^{1},\dots,T^{k}$ di profili è quindi la seguente:

![[Pasted image 20250826151924.png|center|500]]

Esattamente come per i profili $P^{0},P^{1},\dots,P^{k}$ vale che: $$\exists\space l\in[k]:\rho^{T^{h}}(z)=0\space\forall h\lt l\land\space\rho^{T^{l}}(z)=n-1$$
Ed esattamente come abbiamo dimostrato per il dittatore potenziale $j$ al punto [3.1)](#^988d91), possiamo dimostrare che, **per ogni profilo $Q$, se $y\neq z\land v\neq z$ allora** $$\left[\rho^{Q}(y)\gt\rho^{Q}(v)\iff\rho_l^{Q}(y)\gt\rho_l^{Q}(v)\right]$$
Quindi, in particolare, **per ogni profilo $Q$, se $y\neq z$ e poichè $x\neq z$ allora** $$\left[\rho^{Q}(y)\gt\rho^{Q}(x)\iff\rho_l^{Q}(y)\gt\rho_l^{Q}(x)\right]$$
Per concludere questa dimostrazione è sufficiente mostrare che $l=j$, e lo faremo mostrando che:
- non può essere $l\lt j$
- non può essere $l\gt j$

**non può essere $l\lt j$**:
- per dimostralro, mostriamo che *esiste almeno un profilo* $P$ tale che $\rho^{P}\neq\rho_l^{P}$
- ricordiamo che, poichè abbiamo scelto $j$ tale che $\rho^{h}(x)=0$ per ogni $h\lt j$ e $\rho^j(x)\gt0$, allora nel profilo $P^{j-1}$ vale che $\rho^{j-1}(x)=0$ e quindi $$\rho^{j-1}(x)\lt\rho^{j-1}(y)$$
- ma, dato che $\rho_{i}^{h}(x)=n-1$ per ogni $i\leq h$, allora vale che $$\rho_l^{j-1}(x)=n-1$$
- allora $$\rho_l^{j-1}(x)\gt\rho_l^{j-1}(y)\implies\rho^{j-1}\neq\rho_l^{j-1}$$

E quindi, per il profilo $P=P^{j-1}$ vale che $\rho^{P}\neq\rho_l^{P}$

![[Pasted image 20250826153156.png|center|250]]

**non può essere $l\gt j$**
- per dimostralro, mostriamo che *esiste almeno un profilo* $P$ tale che $\rho^{P}\neq\rho_l^{P}$
- nel profilo $P^{j}$ vale che $\rho^{j}(x)=n-1$ e quindi $$\rho^{j}(x)\gt\rho^j(y)$$
- ma, dato che $\rho_{i}^{h}(x)=0$ per ogni $i\gt h$, allora $$\rho_l^{j}(x)=0$$
- allora, $$\rho_l^{j}(x)\lt\rho_l^{j}(y)\implies\rho^{j}\neq\rho_l^{j}$$

E quindi, per il profilo $P=P^{j}$ vale che $\rho^{P}\neq\rho_l^{P}$

E di conseguenza, $l=i\quad\quad\quad\blacksquare$ 

![[Pasted image 20250826153618.png|center|250]]

Il teorema di Arrow **getta un ombra scura** sui sistemi di voto perché afferma che un sistema di voto, per non essere soggetto a manipolazioni interessate (utilizzando alternative irrilevanti) ed essere in grado di rispecchiare la volontà dell’unanimità, deve **essere una dittatura**.

Che non è una prospettiva proprio rassicurante.

Tuttavia, se le alternative hanno certe caratteristiche, e se i ranking dei votanti soddisfano una certa proprietà (perfettamente plausibile in presenza di quelle caratteristiche delle
alternative), allora il teorema di Arrow può essere "aggirato"

# Single Peaked Preferences

Supponiamo che le alternative siano un insieme totalmente ordinato, ovvero: $$A=\{a_1,a_{2},\dots,a_n\},\quad a_{i}\lt a_{i+1}\forall\space i=1,\dots,n-1$$
Dove con "$\lt$" indichiamo una qualche relazione d'ordine

>[!definition]- Single Peaked
>Il ranking del votante $h,r^{h}=\left\langle a_{h1},a_{h2},\dots,a_{hn}\right\rangle$ è detto **single peaked** se, *comunque si scelgono tre alternative $a_i\lt a_{j}\lt a_l$, non accade che* $$\rho_{h}(a_j)\lt\rho_{h}(a_i)\land\rho_{h}(a_j)\lt\rho_{h}(a_l)$$
>Ovvero, $$\forall a_i,a_j,a_{l}\in A:a_i\lt a_{j}\lt a_l\left[\lnot\left(\rho_{h}(a_j)\lt\rho_{h}(a_i)\land\rho_{h}(a_j)\lt\rho_{h}(a_l)\right)\right]$$

Ovvero, considerando $\rho_h$ come una funzione definita su un dominio continuo $\rho_{h}$, non ha minimi relativi.

In figura, tre ranking single peaked:

![[Pasted image 20250826154700.png|center|350]]

Un ranking single peaked è, in effetti, un’ipotesi del tutto ragionevole in questa situazione

ESEMPIO 1:
- possiamo ordinare gli schieramenti politici lungo un asse a partire da quelli di estrema sinistra a quelli di estrema destra
- e difficilmente un elettore il cui schieramento politico preferito è di estrema sinistra avrà come seconda preferenza uno schieramento di estrema destra e come terza preferenza uno schieramento di centro

ESEMPIO 2:
- tipicamente, il livello di un college statunitense è tanto migliore quanto più elevata è la sua retta
- un genitore che deve iscrivere il figlio, tipicamente, avrà un range di preferenze concentrate intorno alla retta che può permettersi di pagare
- difficilmente avrà come prima preferenza il college più esclusivo, come seconda preferenza quello più popolare e come terza preferenza, di nuovo un college molto costoso

Supponiamo che, oltre ad avere l'insieme $A$ ordinato, ***ogni votante*** esprima un ranking single peaked

In questo caso, possiamo supporre ***senza perdità di generalità*** (ovvero, a meno di un riordinamento dei votanti) che, per ogni $h\in[k]$, il picco del votante $h$ non preceda il picco del votante $h+1$
- ovvero: sia $P=\langle r_{1},r_{2},\dots,r_k\rangle$ un profilo nel quale ogni ranking è single peaked
- per ogni $h\in[k]$, indichiamo con $M_h$ l'alternativa preferita dal votante $h$, cioè $$M_{h}\in A\land\rho_h(M_{h})=n-1$$
- allora vale che $M_{1}\leq M_2\leq\dots\leq M_{k}$

In figura, il votante 1 è quello blu, il votante 2 è quello rosa, il votante 3 è quello verde

![[Pasted image 20250826155313.png|center|350]]

## Il Teorema del Votante Mediano


[^1]: Ovvero, *assumendo* che gli altri giocatori rispondano *sinceramente* (in accordo ai loro segnali privati), le risposte degli altri due giocatori sono discordi quando uno di loro estrae una pallina verde, e quindi quando l'urna è $UV$

[^2]: Se avessero votato onestamente secondo il ranking $\langle\text{IP,VV,PF}\rangle$ avrebbe vinto VV

[^3]: dove $\rho'$ è la funzione peso associata al ranking collettivo corrispondente a  $(r'_1,r'_2,\dots,r'_k)$ derivata in accordo a $\sigma$

[^4]: osserviamo che $j\gt0$ perchè $\rho^{0}(x)=0$
