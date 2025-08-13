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

### Tool: Il Teorema di Bayes

Per capire se l'intuizione che ha guidato i giocatori sia fondata razionalmente, dobbiamo calcolare la probabilità di vittoria di ciascun giocatore

Per fare ciò, abbiamo bisogno del **teorema di Bayes**

>[!teorem]- Teorema di Bayes
>Dati due eventi $A,B$ vale che $$Pr(A|B)=\frac{Pr(B|A)Pr(A)}{Pr(B|A)Pr(A)+Pr(B|A^{c})Pr(A^{c})}$$

Vediamo poi come ciò sia utile per analizzare il gioco delle urne




