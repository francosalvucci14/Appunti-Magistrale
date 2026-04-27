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
# Introduzione ai Mechanism Desing

Fino ad ora abbiamo analizzato giochi già esistenti (come i _Connection Games_) per vedere come si comportano i giocatori egoisti.

Con il **Mechanism Design** (Progettazione di Meccanismi), facciamo l'esatto opposto: facciamo "ingegneria inversa" della Teoria dei Giochi. 

Noi siamo i creatori del gioco e vogliamo inventare delle regole affinché i giocatori egoisti, pur facendo i propri interessi, finiscano per realizzare l'obiettivo che vogliamo noi.

## 1. L'idea di base: Innescare il comportamento corretto 

Vediamo prima di tutto lo scopo del Mechanism Design: **indirizzare l'egoismo verso il bene comune**.

- **Il problema:** La società affronta problemi causati da comportamenti egoistici non regolamentati (es. il traffico congestionato a sinistra, o l'inquinamento delle fabbriche in basso a sinistra).
- **La soluzione:** L' incentivo economico (il simbolo del dollaro $).
- **Il risultato:** Trovando le "giuste regole e incentivi" (_Find correct rules/incentives_), possiamo spingere le persone a scegliere comportamenti socialmente utili, come prendere un'autostrada a pedaggio per snellire il traffico o installare pannelli solari.

## 2. L'ostacolo principale: Il problema dell'implementazione

Se fosse facile, lo farebbero tutti. Qui vediamo qual è il vero "muro" contro cui sbatte chi progetta queste regole.

- **Il ruolo del Planner:** Immagina di essere il decisore (il governo, un algoritmo di routing, un banditore d'asta). Vuoi massimizzare il benessere sociale (_social welfare_).
- **L'asimmetria informativa:** Il tuo problema enorme è che **tu non conosci le preferenze degli individui**. Non sai quanto un guidatore valuti il suo tempo, o quanto un utente valuti un oggetto all'asta.
- **Il setting "Strategico":** Non solo non conosci le preferenze, ma hai a che fare con giocatori razionali ed egoisti. Il concetto chiave: le opinioni dei giocatori (le loro preferenze) sono **private** e, se chiedi loro cosa vogliono, _potrebbero mentire per manipolare il sistema_ a loro vantaggio.

## 3. La definizione informale: Progettare un Gioco (Slide 3)

Definiamo tecnicamente cosa significhi fare Mechanism Design alla luce del problema appena visto.

- **Creare il gioco:** Progettare un meccanismo significa inventare le regole di un **gioco** in modo tale che, quando i giocatori lo giocano e raggiungono un equilibrio (Equilibrio di Nash o strategie dominanti), il risultato finale sia esattamente quello che tu, come creatore, desideravi ottenere fin dall'inizio.
- **Informazione Incompleta:** Questo gioco è molto diverso da quelli standard (come il Dilemma del Prigioniero o i Connection Games) dove tutti sanno tutto. Qui ci troviamo in un **Gioco a informazione incompleta**:
    - Ogni giocatore ha dei **valori privati** (detti anche _tipi_), ovvero sa quanto vale per lui una certa cosa, ma non conosce esattamente il valore che gli altri danno a quella cosa.
    - La matrice dei payoff non è fissa e nota a tutti, ma dipende proprio da questi "tipi" segreti.

Vediamo ora un'esempio fondamentale, il problema delle **aste a busta chiusa**

L'obiettivo di questo esempio è mostrare l'enorme differenza tra quello che i giocatori pensano (la verità) e quello che dichiarano (la strategia), e come questo complichi il lavoro di chi progetta l'asta.

Ecco i concetti chiave smontati pezzo per pezzo:

**1. La Verità Segreta vs. La Bugia Strategica**

Prendiamo quindi il seguente esempio

![center|500](img/Pasted%20image%2020260401111604.png)


Ogni partecipante ha due "nuvolette":

- **La nuvoletta di pensiero ($t_i$):** Rappresenta il vero valore massimo che il giocatore $i$ è disposto a pagare per il quadro. Questo è il suo **tipo privato** (la sua reale preferenza, che il banditore _non conosce_).
    - Il giocatore 1 lo valuta 10.        
    - Il giocatore 2 lo valuta 12.
    - Il giocatore 3 lo valuta 7.        
- **La nuvoletta parlante ($r_i$):** Rappresenta la sua **offerta** (_bid_), ovvero la cifra che scrive effettivamente nella busta chiusa e consegna al banditore. Questa è la sua _strategia_.
    
    - Il giocatore 1 offre 11 (offre _di più_ di quanto vale per lui).
    - Il giocatore 2 offre 10 (offre _di meno_, sperando di fare un affare).        
    - Il giocatore 3 offre 7 (dice la verità).

Poiché sono egoisti e razionali, i giocatori non dicono necessariamente la verità se pensano che mentire porti loro un vantaggio.

![center|350](img/Pasted%20image%2020260401111703.png)

**2. Cosa vogliono i giocatori: L'Utilità ($u_i$)**

Perché i giocatori mentono? Perché vogliono massimizzare la loro **utilità** (il loro profitto netto).

La formula ci dice che se un giocatore vince e paga un prezzo $p$, la sua utilità è:
$$u_i = t_i - p$$ 
_(quanto lo valutava davvero MENO quanto ha effettivamente pagato)_.

Se perde, l'utilità è zero. I giocatori sceglieranno l'offerta $r_i$ che credono massimizzerà questo numero.

**3. Cosa vuole il sistema: La Social-Choice Function**

Guardiamo ora la situazione legata al venditore

![center|400](img/Pasted%20image%2020260401111931.png)

Questa è la **Funzione di Scelta Sociale**, ovvero l'esito ideale che la società (o il venditore) vorrebbe raggiungere.

L'obiettivo dichiarato è: _"Il vincitore dovrebbe essere il tizio che **ha in mente** il valore più alto per il quadro"_.

Se guardiamo i pensieri ($t_i$), il quadro dovrebbe chiaramente andare al **Giocatore 2** (che lo valuta 12).

**4. Il problema: Il Meccanismo**

Il banditore non può leggere nel pensiero; può solo leggere le buste chiuse ($r_i$). Pertanto, deve definire un **Meccanismo** composto da due regole ferree:

1. **Regola di Allocazione:** Chi vince? (Di solito, chi fa l'offerta più alta nelle buste).
2. **Regola di Pagamento:** Quanto paga il vincitore $p$? (Paga quello che ha offerto? Paga un'altra cifra?). 

Il Meccanismo deve quindi definire queste due regole in modo tale da ***non poter essere manipolato***
- Il progettista del meccanismo vuole ottenere/calcolare un risultato specifico (definito in termini di valori reali e privati posseduti dai giocatori)

**Cosa va storto in questo esempio?**

Se il meccanismo usa la regola ovvia "vince l'offerta più alta", guarda le buste ($r_i$): vince il Giocatore 1 (che ha offerto 11)

Il nostro obiettivo sociale però ha fallito miseramente: il quadro è andato alla persona sbagliata perché il Giocatore 2 ha fatto il furbo cercando di risparmiare (offrendo 10) e il Giocatore 1 ha fatto un'offerta irrazionale (e ora si ritrova con un'utilità negativa: $u_1 = 10 - 11 = -1$, la cosiddetta "maledizione del vincitore").

Vediamo quindi ora una serie di esempi raffiguranti semplici Meccanismi.

Vedremo che questi semplici Meccanismi non funzionano, e che l'unica soluzione effettiva è che tutti paghino quanto avevano in mente (formalmente fare in modo che $r_i=t_i$)

**Esempio 1 : Nessun Pagamento**

La situazione è la seguente

![center|500](img/Pasted%20image%2020260401112624.png)

Il meccanismo è il seguente: **l'offerta più alta vince ed il prezzo dell'ogegtto è** $0$

Mettiamoci nei panni dei giocatori: se vincere non costa assolutamente un centesimo, quale cifra possiamo scrivere nella busta chiusa per assicurarci di battere gli altri? L'infinito! Non c'è nessuna penalità nell'offrire cifre astronomiche.
Quindi tutti i giocatori, indipendentemente dal loro vero valore ($t_1​=10, t_2​=12, t_3​=7$), scriveranno $+\infty$ ($r_i=+\infty$).

**Il Fallimento:** Il banditore apre le buste e trova tre infiniti. Si ritrova con un pareggio e, soprattutto, **non ha estratto nessuna informazione reale**. L'obiettivo di far rivelare le vere preferenze è fallito perché il meccanismo non crea nessun rischio nel dichiarare il falso al rialzo.

**Esempio 2 : Paga la tua offerta**

Un'altro esempio è il seguente

![center|500](img/Pasted%20image%2020260401112918.png)

Il meccanismo è il seguente: **l'offerta più alta vince e il vincitore paga quanto ha offerto**

In questo meccanismo, i giocatori sanno che se offrono il loro vero valore ($t_i​$) e vincono, la loro utilità sarà zero (es: se valuto il quadro 12, offro 12 e vinco, pago 12. Profitto $= 0$). 

Quindi, per avere un guadagno, **tutti i giocatori sono incentivati a mentire offrendo meno del loro vero valore** ($r_i\lt t_i$​). Questo si chiama _bid shading_ (ombreggiamento dell'offerta).

Il problema è che ognuno "abbassa" l'offerta di una quantità diversa in base a quanto vuole rischiare:

- Il Giocatore 2 (che lo valuta 12) fa troppo il furbo e offre solo 8, sperando di fare un mega-affare.
- Il Giocatore 1 (che lo valuta 10) rischia meno e offre 9.

**Il Fallimento:** Vince il Giocatore 1. 

Il meccanismo ha fallito il suo scopo sociale: l'oggetto è andato alla persona sbagliata perché la strategia (mentire al ribasso) ha completamente distorto il risultato

Vediamo ora qual'è l'unico meccanismo sensato, che ci garantirà il risultato ipotizzato dal progettista
## Vickray's second price auction

![center|500](img/Pasted%20image%2020260401124654.png)

Il meccanismo è il seguente: **Vince l'asta più alta, ed il vincitore paga quanto la seconda asta maggiore**

In questo modo, ad ogni giocatore conviene sempre dire la verità, ovvero dire $r_i=t_i$ 

Questo lo possiamo formalizzare con il seguente teorema

>[!teorem]- Teorema
>Nel sistema di aste Vickrey, per ogni giocatore $i,r_i=t_i$ è la **strategia dominante**

**dimostrazione**

Fissiamo $i$ e $t_i$, e guardiamo le strategie del player $i$. Sia $R=\max_{j\neq i}\{r_j\}$
(osserviamo che $R$ è *sconosciuto* al player $i$; inoltre $R$ indica la ***seconda offerta più alta***)

A questo punto definiamo due casistiche

***caso 1*** : $t_i\geq R$

In questo caso quindi il prezzo che aveva in mente il giocatore $i$ supera la massima offerta fra tutti gli altri players.
Si notano $3$ casi:
1. dichiarare $r_i=t_i$ porta ad una utilità pari a $u_i=t_i-R\geq0$ (notiamo che qui, se $t_i\gt R$ il giocatore ***vince***, mentre fintanto che $t_i=R$ il giocatore può sia **vincere** che **perdere**, a seconda delle regole di spareggio, ma la sua utilità sarebbe pari a $0$)
	1. dicendo la verità hai vinto l'asta e pagato quanto ti spettava; inoltre la tua utilità è positiva, quindi va bene.
2. dichiarare un qualunque $r_i\gt R,r_i\neq t_i$ porta ancora ad una utilità pari a $u_i=t_i-R\geq0$ (il giocatore **vince**)
	1. mentire e offrire più di quanto tu pensavi non ti porta a nessun vantaggio in più rispetto a dire semplicemente la verità
3. dichiarare un qualunque $r_i\lt R$ porta ad una utilità pari a $u_i=0$ (il giocatore **perde**)

***caso 2***: $t_i\lt R$

In questo caso il prezzo che aveva in mente il giocatore $i$ è strettamente più piccolo della massima offerta fatta dagli altri giocatori
Anche qui si notano $3$ casi:
1. dichiarare $r_i=t_i$ porta ad una utilità pari a $u_i=0$ (il giocatore **perde**)
2. dichiarare un qualunque $r_i\lt R,r_i\neq t_i$ porta ancora ad una utilità pari a $u_i=0$ (il giocatore **perde**)
3. dichiarare un qualunque $r_i\lt R$ porta ad una utilità pari a $u_i=t_i-R\lt0$ (il giocatore **vince**)
	1. si hai vinto, ma la tua utilità risulta essere negativa (non è proprio ottimale)

DI conseguenza, raggruppando tutto notiamo che al giocatore $i$ mentire sulla propria offerta non porta mai ad una situazione di vantaggio e ad una migliore utilità, di conseguenza dire **sempre la verità** porta ad una ***strategia dominante*** $\blacksquare$

**METTERE ESEMPIO VICKREY MINIMIZZAZIONE**

---
# Mechanism Desing Problem

## Definizione Formale

Definiamo formalmente quindi il MDP

Abbiamo $N$ agenti; ogni agente possiede alcune informazioni **private** $t_i \in T_i$ (in realtà, l’unica informazione privata) denominate `tipi`

Abbiamo inoltre un **insieme di esiti possibili** $F$

Per ogni vettore di tipi $t = (t_1, t_2, \dots, t_N)$, una **funzione di scelta sociale** $f(t) \in F$ specifica un risultato che dovrebbe essere attuato (il problema è che i tipi sono sconosciuti…)

Ogni agente ha uno **spazio strategico** $S_i$ ed esegue un' azione strategica; ci limitiamo ai meccanismi di rivelazione diretta, in cui l'azione consiste nel ***riportare un valore*** $r_i$ dallo spazio dei tipi (con $r_i$ eventualmente $r_i\neq t_i$), ovvero, $S_i=T_i$

>(piccola digressione)
>riprendiamo l'esempio dell'asta di Vickrey
>- L'insieme dei risultati fattibili è dato da tutti gli offerenti
>- La funzione di scelta sociale consiste nell'assegnare all'offerente con il costo reale più basso: $$f(t)=arg \min_i (t_1, t_2, \dots, t_N)$$


Per ogni risultato fattibile $x \in F$, ogni agente effettua una **valutazione** $v_i(t_i,x)$ (in termini di una valuta comune), esprimendo la propria preferenza riguardo a tale risultato

Per ogni vettore $r$ segnalato, ogni agente riceve un **pagamento** $p_i(r)$ in termini della valuta comune; i pagamenti vengono utilizzati dal sistema per incentivare gli agenti a collaborare. Quindi, l'utilità dell'agente se il risultato per $r$ è $x(r)$ sarà:
$$u_i(t_i,x(r)) = p_i(r) - v_i(t_i,x(r))$$
## Il Goal

Il **goal** quindi del Mechanism Desing è quello di ***implementare*** (secondo un dato concetto di equilibrio) la funzione di scelta sociale, ovvero fornire un **meccanismo** $M=\langle g(r), p(r)\rangle$, 
in modo tale che $x=g(r)=f(t)$ sia garantito in equilibrio rispetto alle utilità degli agenti.

Vediamo che 
- $g(r)$ è un **algoritmo** che calcola un risultato $x=g(r)$ in funzione dei tipi segnalati $r$
- $p(r)$ è uno ***schema di pagamento*** che specifica un pagamento (a ciascun agente) in relazione ai tipi segnalati $r$

## Visione generale

Vediamo ora la visione generale di questo problema

![center|500](img/Pasted%20image%2020260402103102.png)

Come vediamo, abbiamo che:
- Ogni agente ha due valori, uno **privato** $t_i$ e uno **pubblico** $r_i$. Quest'ultimo viene mandato al sistema (reported types)
	- Qui, ogni agente cerca di **massimizzare strategicamente la propria utilità**, che dipende (anche) dal pagamento, che è in funzione dei tipi riportati
- Il sistema propone il **meccanismo**, e rimanda ad ogni agente il pagamento $p_i$
- In output, il sistema manda l'implementazione della scelta di funzione sociale, che deve trovarsi in ***equilibrio*** con le utilità degli agenti
## Implementazione con strategie dominanti

Diamo prima di tutto una definizione formale

>[!definition]- Implementazione con Strategie Dominanti
>Un meccanismo $M=\langle g(),p()\rangle$ è detto **implementazione con strategie dominanti** se esiste un vettore di tipi riportati $r^\star=(r_1^\star,\dots,r_N^\star)$ tale per cui $f(t)=g(r^\star)$ nell'equilibrio a strategie dominanti; ovvero, per ogni agente $i$ e per ogni vettore di tipi riportati $r=(r_1,\dots,r_N)$ vale che: $$u_{i}(t_{i},(r_{-i},r_{i}^\star))\geq u_{i}(t_i,(r_{-i},r_{i}))$$

Sostanzialmente questa definizione ci sta dicendo che il meccanismo **implementa** il nostro obiettivo sociale $f(t)$ se l'esito dell'algoritmo coincide esattamente con quello che volevamo ottenere fin dall'inizio $(g(r^\star)=f(t))$.

Inoltre, l'ultima formula è semplicemente la traduzione in "matematichese" del concetto di **strategia dominante**. 
Ci dice che per ogni giocatore $i$, esiste una mossa "ottima" $r_i^\star$​ tale per cui la sua utilità $u_i$​ usando $r_i^\star$​ è _sempre_ maggiore o uguale ($\geq$) all'utilità che avrebbe usando qualsiasi altra mossa $r_i$​, e questo deve essere vero _qualunque_ cosa facciano gli altri giocatori (rappresentati dal termine $r_{-i}$​).
## Strategy-Proof Mechanism

Abbiamo detto che serve una strategia dominante $r^\star$. Ma cosa succede se questa strategia dominante consiste semplicemente nel **dire la verità**?

- Se l'azione migliore in assoluto per ogni giocatore è dichiarare il proprio vero valore ($r^\star=t$), allora il meccanismo prende il nome di **Strategy-Proof** (a prova di manipolazione), **Truthful** (veritiero) o **Incentive Compatible** (compatibile con gli incentivi).
- **I vantaggi enormi:** 
	1. I giocatori smettono di fare calcoli mentali complessi per cercare di fregare il sistema; si limitano a dire la verità. 
	2. L'algoritmo $g()$ non deve lavorare con dati sporchi o manipolati, ma esegue i suoi calcoli sui valori reali $(t)$, garantendo che l'esito sia davvero quello ottimale per la società.

_Nota: L'asta di Vickrey che abbiamo visto prima è esattamente un esempio di meccanismo Strategy-Proof._
### Truthful Mechanism Desing: Problemi Economici

Qui si fa da ponte verso la parte pratica e si pone la "domanda da un milione di dollari" 

- **La Domanda:** Sappiamo cos'è un meccanismo Truthful, ma **come si costruisce da zero?**
- Se io ho in mente un obiettivo sociale (es. "voglio instradare i pacchetti internet sul percorso più veloce"), come faccio a inventarmi:
    1. Un algoritmo di allocazione $g(r)$
    2. E soprattutto, una **regola di pagamento** $p(r)$ tali per cui i router egoisti non abbiano alcun incentivo a mentire sulle loro reali velocità di connessione?
- **Condizioni:** Sotto quali condizioni matematiche è fisicamente possibile creare queste regole? (Spoiler: non sempre è possibile).

Vediamo ora alcuni esempi contenenti 5 scenari del mondo reale in cui il Mechanism Design è assolutamente fondamentale. In ognuno di questi casi, abbiamo giocatori egoisti con informazioni private e un "pianificatore" che vuole raggiungere un obiettivo socialmente utile.

L'obiettivo (la sfida) in ciascuno di questi esempi è trovare una regola di pagamento che renda il meccanismo **Truthful** (cioè dove dire la verità è la strategia dominante).

Analizziamoli uno per uno

**Asta Multi-oggetto** (Multiunit Acution)

**Lo Scenario:** Abbiamo $N$ compratori e $k$ oggetti identici (es. 3 licenze per il 5G, 10 bot in edizione limitata). Ogni giocatore ne vuole solo uno.
    
- **La Verità** ($t_i$​): Il valore massimo reale che il giocatore attribuisce all'oggetto.
- **L'Obiettivo Sociale:** Dare gli oggetti a chi li valuta di più.
- **Perché l'approccio ingenuo fallisce:** Se fai un'asta "paga quello che offri" (pay-as-bid), i giocatori cercheranno di indovinare le offerte degli altri per offrire _appena un centesimo in più_ del necessario per rientrare nei primi $k$. Questo porta a speculazioni, offerte al ribasso e, spesso, all'assegnazione degli oggetti alle persone sbagliate (chi ha scommesso male resta fuori anche se valutava l'oggetto tantissimo).

**La Soluzione (L'Asta di Vickrey generalizzata):** 

- **Allocazione:** Si mettono in fila le offerte dalla più alta alla più bassa. I primi $k$ vincono l'oggetto.
 - **Pagamento:** Quanto pagano? Non quello che hanno offerto, e nemmeno la seconda offerta più alta tra di loro. **Tutti i $k$ vincitori pagano una cifra uguale alla ($k+1$)-esima offerta più alta** (ovvero la prima offerta perdente).
 - **Perché funziona:** Proprio come nell'asta per un quadro singolo, scorporare la tua offerta da quello che pagherai rimuove ogni incentivo a mentire. Se sei tra i vincitori, il prezzo che paghi è deciso da chi è rimasto fuori, quindi mentire al ribasso rischia solo di farti finire fuori dai primi $k$. Dire la verità è dominante.

![center|500](img/Pasted%20image%2020260402115045.png)

**Sponsored Search Auction**

**Lo Scenario:** Google ha $k$ slot pubblicitari. Lo slot 1 riceve molti click ($\alpha_1$​), lo slot 2 ne riceve meno ($\alpha_2$​), e così via.
    
- **La Verità** ($t_i$​): Il reale profitto netto che un'azienda ottiene da un singolo click.
- **L'Obiettivo Sociale:** Massimizzare il valore totale generato (mettere chi valuta di più i click nello slot che genera più click).
- **Perché l'approccio ingenuo fallisce:** Agli albori di internet (es. il motore di ricerca Overture), le aziende pagavano esattamente quello che offrivano. Risultato? Le famose "bidding wars". Un'azienda offriva 1.01$\$$ per superare chi offriva 1.00$\$$. L'altro rispondeva con 1.02$\$$. Quando uno dei due finiva il budget, l'altro crollava l'offerta a 0.01$\$$. I prezzi fluttuavano selvaggiamente ogni secondo, il sistema era instabile e l'algoritmo impazziva.

**La Soluzione (Il Meccanismo VCG / GSP):**
    
- **Allocazione:** Si ordinano le aziende per offerta. Chi offre di più va nello slot 1, il secondo nello slot 2, ecc.  
- **Pagamento (Logica VCG):** Ogni azienda paga per il "danno" che causa agli altri stando lì. Se l'azienda A non esistesse, l'azienda B salirebbe allo slot 1 (prendendo più click), l'azienda C allo slot 2, ecc. L'azienda A deve pagare esattamente il valore di quei click che sta "rubando" a B e C occupando lo slot superiore.    

![center|500](img/Pasted%20image%2020260402115518.png)

E così via
### Come progettare meccanismi Truthful?

Descriveremo i risultati relativi ai problemi di minimizzazione (i problemi di massimizzazione sono simili)

Abbiamo che:
- per ogni $x\in F$, la **funzione di valutazione** $v_i(t_i,x)$ rappresenta un costo sostenuto dal giocatore $i$ nella soluzione $x$
- la **funzione sociale** $f(t)$ mappa il vettore di tipi $t$ in una soluzione $x$ che *minimizza* una misura di $x$
- i pagamenti provengono dal meccanismo agli agenti

Diamo inoltre un'importante definizione

>[!definition]- Problemi Utilitari
>Un problema è definito **utilitario** se la sua funzione obiettivo è tale che $$f(t)=arg\min_{x\in F}\sum\limits_{i}v_i(t_{i},x)$$

**osservazione** : Il problema dell'asta è un problema *utilitario*, e per problemi utilitari essite una certa classe di meccanismi Truthful
### Vickrey-Clarke-Groves (VCG) Mechanism

Definiamo la classe per di meccanismi per i problemi utilitari, ovvero la classe **VCG**

Il meccanismo VCG è *l'unico* meccanismo strategy-proof per i problemi utilitari:
- L'algoritmo $g(r)$ calcola $$x=arg\min_{y\in F}\sum\limits_{i}v_{i}(r_{i},y)$$
- La funzione di pagamento per il giocatore $i$ è: $$p_i(r)=h_{i}(r_{-i})-\sum\limits_{j\neq i}v_{j}(r_{j},g(r))$$
Nella funzione di pagamento, la quantità $h_i(r_{-i})$ è una **funzione arbitraria** dei tipi dei giocatori segnalati diversi dal giocatore $i$

Cosa possiamo dire per i problemi **non-utilitari**? I meccanismi strategy-proof generali sono noti solo quando il tipo è un *singolo parametro*. (Lo vedremo.)

Vediamo ora il seguente teorema:

>[!teorem]- Teorema sui meccanismi VCG
>I meccanismi VCG sono **truthful** per problemi utilitari

**dimostrazione**

L'obiettivo della dimostrazione è far vedere che l'utilità del giocatore $i$ quando dice la verità ($t_i$​) è sempre maggiore o uguale all'utilità che avrebbe se dicesse una bugia ($r_i$​).

Fissiamo un giocatore $i$. Supponiamo che il suo vero costo sia $t_i$​. Tutti gli altri giocatori dichiarano le loro offerte, che chiamiamo $r_{-i}$​ (non importa se dicono il vero o il falso, le prendiamo come un dato di fatto).

Definiamo due possibili scenari per il giocatore $i$:

- **Lo scenario sincero** ($\hat{r}$): Il giocatore dichiara il suo vero costo $t_i$​. Il vettore di tutte le offerte diventa $\hat{r}=(r_{-i}​,t_i​)$. L'algoritmo di allocazione $g()$ elabora queste offerte e sceglie la soluzione ottima $x$.
	- $x=g(\hat{r})$
- **Lo scenario bugiardo:** Il giocatore dichiara un costo falso $r_i​\neq t_i$​. L'algoritmo elabora le nuove offerte e sceglie una soluzione (potenzialmente diversa) $x'$.
	- $x'=g(r_{-i},r_i)$

Ora calcoliamo l'utilità del giocatore $i$ nei due scenari. 

Ricordiamo che Utilità = Pagamento Ricevuto - Costo Vero.
La formula del pagamento VCG è fatta da una costante $h_i​(r_{-i}​)$ meno la somma dei costi dichiarati dagli _altri_ giocatori.

- **Utilità dicendo la verità:** L'equazione è: $$u_i​(t_i​,(r_{-i}​,t_i​))=\left[h_i​(r_{-i}​)-\sum\limits_{j\neq i}​v_j​(r_j​,x)\right]-v_i​(t_i​,x)$$La parte tra parentesi quadre è il pagamento VCG. La parte fuori è il vero costo per il giocatore $i$. Ora guardiamo cosa succede: poiché abbiamo definito $\hat{r}_j$​ come il vettore in cui tutti dicono $r_j$​ e il giocatore $i$ dice $t_i$​, possiamo "fondere" l'ultimo termine dentro la sommatoria. Otteniamo: $$h_i​(r_{-i}​)-\sum\limits_{j\neq i}​v_j​(\hat{r}_{j}​,x)$$
- **Utilità dicendo una bugia:** Facciamo la stessa identica cosa, ma valutata sulla soluzione $x'$ (quella uscita per colpa della bugia). Otteniamo quindi che: $$u_i​(t_i​,(r_{-i}​,r_i​))=h_i​(r_{-i}​)-\sum\limits_{j\neq i}v_j​(\hat{r}_j​,x')$$

**Il punto chiave fin qui:** L'utilità del giocatore in entrambi i casi è pari a una costante $h_i$​ (che dipende solo dagli altri e che lui non può influenzare) _MENO la somma totale dei costi reali_ di tutti i giocatori.

Ora entra in gioco l'ipotesi che l'algoritmo $g()$ sia "utilitaristico". Questo significa che l'algoritmo è progettato per scegliere sempre la soluzione che **minimizza la somma totale dei costi** basandosi sulle offerte ricevute.

Quando il giocatore $i$ dice la verità (vettore $\hat{r}$), l'algoritmo sceglie $x$. Quindi $x$ è per definizione la soluzione che minimizza la somma:
$$x=arg\min_{y\in F}\sum\limits_{i}​v_i​(\hat{r},y)$$

Cosa comporta questo? Che la somma dei costi calcolata su $x$ sarà **sempre minore o uguale** alla somma dei costi calcolata su _qualsiasi altra soluzione possibile_, inclusa la soluzione $x'$. 
Di conseguenza vale che:
$$\sum\limits_{j}​v_j​(\hat{r},x)\leq \sum\limits_{j}​v_j​(\hat{r},x')$$

E quindi, matematicamente, l'utilità del giocatore $i$ quando dice la verità sarà sempre maggiore o uguale alla sua utilità quando dice una bugia: 
$$\boxed{u_i​(t_i​,(r_{-i}​,t_i​))\geq u_i​(t_i​,(r_{-i}​,r_i​))}$$

Il teorema è dimostrato: in un meccanismo VCG applicato a problemi utilitaristici, mentire non potrà mai aumentare il tuo profitto. Dire la verità è una **strategia dominante** $\blacksquare$
#### I Pagamenti di Clarke

Nella dimostrazione precedente abbiamo visto che la formula di VCG funziona grazie a un "trucco" matematico: la presenza di una funzione misteriosa chiamata $h_i​(r_{-i}​)$.

Quella funzione, matematicamente, poteva essere qualsiasi cosa, purché non dipendesse da ciò che dichiara il giocatore $i$. Ma nel mondo reale, non possiamo scegliere una $h_i$​ a caso. Qui spieghiamo proprio **come scegliere quella funzione per rendere il meccanismo utilizzabile nella realtà**

**Il collegamento col teorema precedente:** Il teorema ci diceva che l'utilità di un giocatore in un meccanismo VCG è: $u_i​=h_i​(r_{-i}​)-\sum\limits_{j}​v_j​(r_j​,x)$ 
Ma cosa succede se scegliamo male $h_i​$? Se ad esempio mettessimo $h_i​=0$, il pagamento diventerebbe negativo per il banditore.

Inoltre, i giocatori potrebbero avere un'utilità negativa e rifiutarsi di partecipare al gioco.

**La soluzione: Il Meccanismo Pivot di Clarke** La genialità di Clarke è stata inventare la definizione perfetta per $h_i$​:
$$h_i​(r_{-i}​)=\sum\limits_{j\neq i}​v_j​(r_j​,g(r_{-i}​))$$

In parole povere: $h_i$​ **è il costo totale che la società avrebbe sostenuto se il giocatore $i$ NON fosse mai esistito** (o non avesse mai partecipato al gioco). L'algoritmo $g(r_{-i})$ è infatti la soluzione ottima calcolata ignorando l'esistenza del giocatore $i$.

**La formula finale del pagamento di Clarke:** Inserendo questa $h_i$​ nella formula dei pagamenti, otteniamo:
$$p_{i}(r)=\underbrace{\sum\limits_{j\neq i}​v_j​(r_j​,g(r_{-i}​))}_{\text{costo per gli altri SENZA i}=h_{i}(r_{-i})}-\underbrace{\sum\limits_{j\neq i}​v_j​(r_j​,g(r​))}_{\text{costo per gli altri CON i}}$$

Questo concetto si chiama **Esternalità**. Il giocatore i paga esattamente il "danno" (o l'aumento di costo) che la sua presenza causa al resto della società. 

_Il grande vantaggio:_ Con i pagamenti di Clarke si dimostra matematicamente che l'utilità di ogni agente è **sempre** $\geq0$.
Questa proprietà si chiama _Individual Rationality_: significa che gli agenti non ci rimetteranno mai a partecipare, quindi saranno ben felici di "giocare".

Chiudiamo il cerchio dimostrando che l'Asta di Vickrey che abbiamo visto in modo intuitivo all'inizio è, di fatto, **un caso speciale del meccanismo di Clarke**. Se applichiamo l'esternalità all'asta per comprare un servizio (minimizzazione):

- Qual è il costo per la società se la Macchina Vincente non partecipa? Il lavoro andrà alla seconda macchina più economica (il _secondo miglior prezzo_).
- Qual è il costo per gli altri se la Macchina Vincente partecipa? Zero, perché il lavoro lo fa lei.
- Differenza (il pagamento): La Macchina Vincente riceve esattamente il secondo miglior prezzo. I perdenti ricevono 0. La teoria generale di VCG/Clarke combacia perfettamente con l'esempio pratico!

---
# Mechanism Desing: Problemi Algoritmici

Finora abbiamo parlato come economisti. Ma un informatico guarda la formula di VCG e sbianca. Perché?

- Per trovare la soluzione ottima $g(r)$ serve eseguire un algoritmo.
- Ma per calcolare i pagamenti di Clarke per N giocatori, dobbiamo calcolare g(r−i​) per ogni singolo giocatore! Significa che **dobbiamo eseguire l'algoritmo di ottimizzazione $N+1$ volte** (una volta con tutti, e $N$ volte togliendo un giocatore alla volta).
- Se l'algoritmo di base è già lento (o peggio, ***NP-hard***, come nel problema del Commesso Viaggiatore), ripetere il calcolo $N$ volte renderebbe il meccanismo impossibile da usare nella realtà 

**L'applicazione ai Grafi:** Il campo dell'Algorithmic Mechanism Design (AMD) studia proprio questo.

Immaginiamo Internet: un grafo $G=(V,E)$ dove ogni arco (cavo di rete) è posseduto da un giocatore egoista. Il costo reale di quel cavo è il "tipo privato". Vogliamo risolvere problemi classici come lo **Shortest Path (SP)** o il **Minimum Spanning Tree (MST)** pagando i router per fargli dire la verità sui loro costi.

Come ultima parte vediam0o una tabella riassuntiva che rappresenta un vero trionfo dell'Informatica. Essa compara due cose:

1. **Centralized algorithm:** Il tempo necessario per risolvere il problema classicamente, se tutti dicessero la verità gratis (es. usare l'algoritmo di Dijkstra per il cammino minimo costa $O(m+n\log(n))$).
2. **Selfish-edge mechanism:** Il tempo necessario per risolvere il problema **E IN PIÙ** calcolare tutti gli $N$ pagamenti di Clarke per far dire loro la verità.

**Il risultato? Il tempo di calcolo è asintoticamente IDENTICO!** Nonostante sembri necessario ricalcolare tutto l'algoritmo $N$ volte (il che moltiplicherebbe il tempo per $N$), scienziati informatici hanno scoperto strutture dati e algoritmi super-ottimizzati che permettono di calcolare _tutti_ i pagamenti di Clarke "gratis" o quasi, nello stesso tempo che ci vuole a risolvere il problema base una sola volta.

**In conclusione:** Grazie a VCG sappiamo che è possibile far dire la verità a tutti; grazie a Clarke sappiamo come farlo senza mandare in bancarotta nessuno e garantendo utilità positive; e grazie all'Algorithmic Mechanism Design sappiamo che possiamo calcolare tutto questo in tempi velocissimi anche su reti enormi come Internet.

![center|500](img/Pasted%20image%2020260418142746.png)

