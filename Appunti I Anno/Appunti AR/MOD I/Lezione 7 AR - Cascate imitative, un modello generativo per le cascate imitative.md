# Herding: seguire il gregge

Da questo punto in poi, studieremo un aspetto diverso delle reti, ovvero **la rete come fonte di informazioni**

Andremo a studiare il contenuto informativo di una rete, che divideremo in $3$ contenuti:
- contenuto informativo che può indurre gli individui che compongono la rete a modificare il proprio comportamento 
	- (come vedremo in questa sezione)
- contenuto informativo che deve essere sintetizzato per derivare una informazione comulativa che tenga conto, in qualche modo, dei pezzi di informazione derivanti dai singoli individui 
	- (come vedremo nella sezione "sistemi di voto" )
- contenuto informativo dal quale deve essere individuato ed estratto quello rilevante ad una data richiesta 
	- (come vedremo nella sezione "Web Search" )

L'informazione presente in una rete può indurre gli individui che la compongono a modificare il proprio comportamento, come abbiamo visto quando abbiamo parlato di diffusione

Il punto di vista qui è sensibilmente diverso, infatti nei processi di diffusione un individuo cambia comportamento:
1) come conseguenza di **comunicazioni esplicite** di una serie di informazioni da parte di individui con i quali è in relazione
2) per ottenere una serie di benefici dalla presenza della rete

Da adesso invece studieremo il fenomeno in virtù del quale un individuo modifica il proprio comportamento semplicemente *osservando* il comportamento che *globalmente* hanno gli altri individui nella rete
- questo significa che considereremo una visione globale e non puntuale della rete, e quindi non ci interessererà l'analisi diretta delle singole relazioni personali

SE TI VA VEDITI ESEMPI "CENARE IN UNA CITTÀ SCONOSCIUTA" E "A NASO IN SU" (PORCO DIO CHE NOMI DEL CAZZO)

## Il gioco delle urne

C'è uno scommettitore, in una stanza chiusa, e un insieme di giocatori che attendono fuori dalla stanza

Lo scommettitore inserisce $2$ palline rosse e $1$ pallina blu in un’urna (che chiameremo MR, a maggioranza rossa), e $2$ palline blu e $1$ pallina rossa in una seconda urna identica alla prima (che chiameremo MB, a maggioranza blu)

Poi, “mischia” le due urne e ne sceglie una a caso

Le regole del gioco sono le seguenti:
 - un giocatore alla volta entra nella stanza, estrae una pallina dall’urna (che può essere rossa o blu), e poi re-inserisce la pallina nell’urna
 - il giocatore comunica allo scommettitore e a tutti gli altri giocatori se, sulla base delle informazioni in suo possesso, ritiene che si tratti dell’urna MR o dell’urna MB
 - ma il giocatore **non deve comunicare l’esito dell’estrazione** (pena la sconfitta per tutti i giocatori), ossia, se ha estratto una pallina rossa o una pallina blu

Al termine del gioco, solo i giocatori che hanno indovinato di quale urna si tratti
ricevono un premio

Cerchiamo ora, di capire
- in che modo risponderanno i giocatori
- in base a quali motivazioni prenderanno le loro decisioni

GIOCATORE 1:
- prima di estrarre la pallina, l’unica informazione in suo possesso è che le urne MR e MB sono equiprobabili
- dopo aver estratto una pallina, la probabilità che l’urna sia di un certo tipo verrà modificata: se estrae una pallina blu (rossa) il giocatore penserà che è più probabile che l’urna sia MB (MR)
- perciò, gli conviene rispondere in accordo alla pallina che ha estratto – diciamo, blu

GIOCATORE 2:
- ora, prima di estrarre la pallina, il giocatore deduce ciò che ha estratto il GIOCATORE 1: siccome sa che chi lo ha preceduto è il GIOCATORE 1, il GIOCATORE 2 sa che, se il GIOCATORE 1 ha risposto MB è perché ha estratto una pallina blu
- a questo punto, se il GIOCATORE 2 estrae una pallina rossa, sa che sono state estratte una pallina blu e una pallina rossa: quindi, si trova nella stessa situazione in cui si trovava il GIOCATORE 1 prima dell’estrazione e, di conseguenza, risponde MR - in accordo alla pallina che ha estratto
	- se estrae una pallina rossa, è come se il gioco iniziasse dal GIOCATORE 2... e quindi non consideriamo questo caso
- assumiamo che estragga una pallina blu; in questo caso, sa che sono state estratte due palline blu e questo rinforza l’ipotesi che l’urna sia MB: e quello che risponde è MB

GIOCATORE 3:
- prima di estrarre la pallina, il giocatore deduce ciò che hanno estratto il GIOCATORE 1 e il GIOCATORE 2: lo stesso ragionamento operato dal GIOCATORE 2 permette al GIOCATORE 3 di capire che il GIOCATORE 1 ha estratto una pallina blu, e, siccome sa che chi lo ha preceduto è il GIOCATORE 2, il GIOCATORE 3 sa che se il GIOCATORE 2 ha risposto MB è perché ha estratto una pallina blu
- se estrae una pallina blu sa che sono state estratte tre palline blu e questo rinforza l’ipotesi che l’urna sia MB: e questo è quello che risponde (e, fin qui, non ci piove)
- se estrae una pallina rossa sa che sono state estratte due palline blu e una rossa: perciò anche in questo caso sembra più probabile che sia un’urna MB che non MR - e MB è quello che il GIOCATORE 3 risponde

GIOCATORE 4:
- prima di estrarre la pallina, il giocatore deduce ciò che hanno estratto il GIOCATORE 1 e il GIOCATORE 2: lo stesso ragionamento operato dal GIOCATORE 3 permette al GIOCATORE 4 di capire che il GIOCATORE 1 ha estratto una pallina blu e il GIOCATORE 2 ha estratto una pallina blu
- invece, nulla può dedurre circa l’estrazione del GIOCATORE 3 perché sa che, qualunque fosse stata la sua estrazione, avrebbe comunque risposto MB!
- perciò, ha esattamente le stesse informazioni che aveva il GIOCATORE 3 e, di conseguenza, non può che comportarsi esattamente come il GIOCATORE 3: qualunque pallina estragga, risponderà MB!

GIOCATORE $x$, con $x \geq 5$:
- esattamente come il GIOCATORE 4

Si è innescato un fenomeno a cascata – una **cascata imitativa** (qualunque saranno le estrazioni, ogni giocatore risponderà MB)

Per capire se l'intuizione che ha guidato i giocatori sia fondata razionalmente, dobbiamo calcolare la probabilità di vittoria di ciascun giocatore

Per fare ciò, abbiamo bisogno del **teorema di Bayes**

>[!teorem]- Teorema di Bayes
>Dati due eventi $A,B$ vale che $$Pr(A|B)=\frac{Pr(B|A)Pr(A)}{Pr(B|A)Pr(A)+Pr(B|A^{c})Pr(A^{c})}$$

Vediamo poi come ciò sia utile per analizzare il gioco delle urne

Siano MR l'evento "l'urna è a maggioranza rossa" e MB = "l'urna è a maggioranza blu", r = "estratta rossa" e b = "estratta blu"

Dobbiamo quindi calcolare $$Pr(MB|b),Pr(MB|r),Pr(MR|r),Pr(MR|b)$$
sapendo che:
- $Pr(MB)=Pr(MR)=\frac{1}{2}$
- $Pr(r|MR)=\frac{2}{3}$ e $Pr(b|MR)=\frac{1}{3}$
- $Pr(b|MB)=\frac{2}{3}$ e $Pr(r|MB)=\frac{1}{3}$
- e ovviamente $MB^{c}=MR$ e $MR^{c}=MB$

Il GIOCATORE 1 estrae una blu, allora per il teorema di Bayes vale che 

$$\begin{align*}
&Pr(MB|b)=\frac{\frac{2}{3} \frac{1}{2}}{\frac{2}{3} \frac{1}{2}+ \frac{1}{3} \frac{1}{2}}= \frac{2}{3}\\&Pr(MR|b)=\frac{\frac{1}{3} \frac{1}{2}}{\frac{1}{3} \frac{1}{2}+ \frac{2}{3} \frac{1}{2}}=\frac{1}{3}\quad(1-Pr(MB|b))\\
\end{align*}$$
E quindi, seguendo la propria intuizione e rispondendo $MB$, il GIOCATORE $1$ ha risposto con l'alternativa che massimizza la sua probabilità di successo

Il GIOCATORE 2
- se estrae una rossa, vale che $$\begin{align*}
&Pr(MB|br)=\frac{\frac{2}{3} \frac{1}{3} \frac{1}{2}}{\frac{2}{3} \frac{1}{3} \frac{1}{2}+ \frac{1}{3} \frac{2}{3} \frac{1}{2}}= \frac{1}{2}\\&Pr(MR|br)=\frac{\frac{1}{3} \frac{2}{3} \frac{1}{2}}{\frac{1}{3} \frac{2}{3} \frac{1}{2}+ \frac{2}{3} \frac{1}{3} \frac{1}{2}}=\frac{1}{2}
\end{align*}$$Quindi, la sequenza di $2$ estrazioni non fornisce alcuna indicazione: il gicoatore risponde $MR$, coerentemente con la palla che ha estratto (il GIOCATORE 1 potrebbe aver anche mentito)
- se estrae una blu, vale che $$\begin{align*}
&Pr(MB|bb)=\frac{\frac{2}{3} \frac{2}{3} \frac{1}{2}}{\frac{2}{3} \frac{2}{3} \frac{1}{2}+ \frac{1}{3} \frac{1}{3} \frac{1}{2}}= \frac{4}{5}\\&Pr(MR|bb)=\frac{\frac{1}{3} \frac{1}{3} \frac{1}{2}}{\frac{1}{3} \frac{1}{3} \frac{1}{2}+ \frac{2}{3} \frac{2}{3} \frac{1}{2}}=\frac{1}{5}
\end{align*}$$Quindi, seguendo la propria intuizione e rispondendo $MB$, il GIOCATORE 2 ha risposto con l'alternativa che massimizza la sua prob i successo.

Il GIOCATORE 3, dopo che sono state estratte due blu:
- se estrae una blu $$\begin{align*}
&Pr(MB|bbb)=\frac{\frac{8}{27} \frac{1}{2}}{\frac{8}{27} \frac{1}{2}+ \frac{1}{27} \frac{1}{2}}= \frac{8}{9}\\&Pr(MR|bbb)=\frac{1}{9}\quad\text{vedi calcoli}
\end{align*}$$Quindi, seguendo la propria intuizione e rispondendo $MB$, il GIOCATORE 3 ha risposto con l'alternativa che massimizza la sua prob i successo - e questo è chiaro
- se estrae una rossa $$\begin{align*}
&Pr(MB|bbr)=\frac{\frac{4}{9} \frac{1}{3} \frac{1}{2}}{\frac{4}{9} \frac{1}{3} \frac{1}{2}+ \frac{1}{9} \frac{2}{3} \frac{1}{2}}= \frac{2}{3}\\&Pr(MR|bbr)=\frac{1}{3}\quad\text{vedi calcoli}
\end{align*}$$Quindi, nonostante l'estrazione di una rossa, la sequenza di estrazioni favorisce ancora l'eventualità che l'urna sia $MB$: rispondendo $MB$, il GIOCATORE 3 massimizza la sua probabilità di successo

Il GIOCATORE 4, sapendo che le prime due estrazioni sono state blu, risponde sempre $MB$: calcoliamo la prob. nelle $4$ estrazioni possibili
$$\begin{align*}
&Pr(MB|bbbb)=\frac{16}{17}\space\land\space Pr(MR|bbbb)=\frac{1}{17}\\&Pr(MB|bbbr)=\frac{8}{9}\space\land\space Pr(MR|bbbr)=\frac{1}{9}\\&Pr(MB|bbrb)=\frac{8}{9}\space\land\space Pr(MR|bbrb)=\frac{1}{9}\\&Pr(MB|bbrr)=\frac{1}{2}\space\land\space Pr(MR|bbrr)=\frac{1}{2}
\end{align*}$$
Quindi, seguendo la propria intuizione e rispondendo $MB$, il GIOCATORE $4$ non incappa mai nell'alternativa che minimizza la sua prob. di successo, tuttavia, se estrae una rossa e il GIOCATORE 3 aveva anch'egli estratto una rossa (eventualità che il GIOCATORE 4 non può conoscere) si trova, nuovamente, nella situazione in cui le eventualità $MB$ e $MR$ sono equiprobabili

Il GIOCATORE 5, sapendo che le prime due estrazioni sono state blu, risponde sempre $MB$: calcoliamo la prob. nelle $8$ estrazioni possibili 
$$\begin{align*}
&Pr(MB|bbbbb)=\frac{32}{33}\space\land\space Pr(MR|bbbbb)=\frac{1}{33}\\&Pr(MB|bbbbr)=Pr(MB|bbbrb)=Pr(MB|bbrbb)=\frac{8}{9}\space\\&\land\space Pr(MR|bbbbr)=Pr(MR|bbbrb)=Pr(MR|bbrbb)=\frac{1}{9}\\&Pr(MB|bbbrr)=Pr(MB|bbrbr)=Pr(MB|bbrrb)=\frac{2}{3}\space\\&\land\space Pr(MR|bbbrr)=Pr(MR|bbrbr)=Pr(MR|bbrrb)=\frac{1}{3}\\&Pr(MB|bbrrr)=\frac{1}{3}\space\land\space Pr(MR|bbrrr)=\frac{2}{3}
\end{align*}$$
Quindi, seguendo la propria intuizione e rispondendo $MB$, il GIOCATORE $5$ può anche incappare nell'alternativa che minimizza la sua prob. di successo,e per i giocatori successivi sarebbe anche peggio.

Tuttavia, se le prime due estrazioni sono blu, tutti i giocatori successivi al secondo rispondono blu, perchè ***sulla base di cio che conoscono*** è la scelta migliore

Sia il gioco delle urne, che i due esempi prima (che invito a leggere), hanno caratteristiche comuni, che sono: 
1) ogni individuo deve prendere una decisione
2) ogni individuo ha un'informazione privata
3) ogni individuo riceve dalla rete solo un'informazione incompleta
	1) sa *cosa* hanno deciso gli altri, ma non sa il *perchè*
4) le decisioni vengono prese ***sequenzialmente***: un individuo prende una decisione *dopo* aver osservato il comportamento di altri individui
5) ogni individuo prende le sue decisioni su una base puramente razionale
	1) inferisce quale sia la decisione che, sulla base delle osservazioni dell'ambiente e del comportamento degli altri individui, sembra essere quella che gli porterà i benefici maggiori
	2) non agisce sulla base di una pressione sociale a uniformarsi, come avviene nell'omofilia
6) la cascata imitativa si innesca solo quando una ***massa critica*** di individui ha preeso la medesima decisione
## Un modello generale

Definiamo ora un modello generale di decision making sequenziale, generalizzando le caratteristiche appena evidenziate:
1) ogni individuo deve prendere una decisione: accettare $(Y)$ o non accettare $(N)$ una proposta?
	- Una delle due è la scelta "giusta", l'altra quella "sbagliata"
	- La prob. che sia "corretto" accettare la proposta è $Pr(Y)=p$, e la prob che sia "corretto" non accettare la proposta è $Pr(N)=1-p$
	- Se un individuo **accetta** la proposta, lui può avere un profitto oppure una perdita:
		- se accettare è la scelta giusta, allora ha un profitto $v_{g}\gt0$
		- se accettare è la scelta sbagliata, allora ha un profitto $v_{b}\le0$
	- Se un individuo **non accetta** la proposta, non avrà ne profitto ne perdita
	- Affinchè sia equivalente per un individuo accettare o non accettare la proposta, in assenza di informazioni che permettano di guadagnare evidenza in favore di una delle due alternative, deve necessariamente valere che $$v_{g}p+v_b(1-p)=0$$[^1]
2) Ogni individuo ha un'informazione privata, che riceve nella forma di un segnale privato, che può avere uno dei due valori: $A$ (Accetta) o $R$ (Rifiuta)
	- Se la scelta giusta è accettare la proposta, la prob. di ricevere $A$ è $q\gt \frac{1}{2}$
	- Se la scelta giusta è non accettare la proposta, la prob. di ricevere $A$ è $1-q$
	- Simmetricamente, se la scelta giusta è accettare la proposta allora la prob. di ricevere $R$ è $1-q$, se la scelta giusta è non accettare allora la prob. di ricevere $R$ è $q$
	- Formalmente, vale che $$\begin{align*} &Pr(A|Y)=q\quad Pr(A|N)=1-q\\&Pr(R|Y)=1-q\quad Pr(R|N)=q\end{align*}$$
3) Ogni individuo riceve dalla rete solo un'informazione incompleta, infatti sa *cosa* hanno deciso gli altri, ma non il *perchè*
4) Le decisioni vengono prese sequenzialmente: un individuo prende una decisione *dopo* aver osservato il comportamento di altri individui
5) Ogni individuo prende le sue decisioni su una base puramente razionale
	- Se, dopo aver ricevuto il proprio segnale privato e aver osservato le scelte di altri individui nella rete, la prob. che la scelta giusta sia accettare la proposta è diventata $p'$, allora un individuo accetta la proposta se e solo se $$v_{g}p'+v_{b}(1-p')\geq0$$e poichè $v_{g}p+v_b(1-p)=0\implies v_{b}=-\frac{p}{1-p}v_{g}\leq0$, quanto sopra accade $\iff p'\geq0$
6) La cascata imitativa si innessa solo quando 

[^1]: il valore atteso del profitto in caso di accettazione o di non accettazione è lo stesso
