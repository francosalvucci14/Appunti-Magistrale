# Index Construction

Le domande che ci poniamo in questa sezione sono:
- Come costruiamo un indice?
- Che strategie possiamo usare avendo memoria limitata?

Ricordiamo le basi di costruzione gettate qualche lezione fa
1) Vengono estratte le parole dai documenti, e salvate in un dizionario con entrate *<Term;DocID>*
2) Quando tutti i documenti sono stati elaborati, il dizionario viene ordinato in base ai termini

Prendiamo anche come base il dataset RCV1: lo useremo per un pò

Guardando un po le statistiche di RCV1 notiamo la seguente situazione

![center|400](img/Pasted%20image%2020260324121706.png)

Vediamo subito due valolri molto strani, ovvero : 4.5 bytes per word token vs. 7.5 bytes per word type

Perchè questa distinzione?

Per capire la differenza tra 4.5 e 7.5, dobbiamo prima chiarire bene la differenza tra **Token** e **Type** (o Termine):

- **Token (Occorrenza):** È ogni singola parola così come appare nel testo. Se la parola "il" compare 10.000 volte nei documenti, conterai 10.000 token.
- **Type / Term (Vocabolo univoco):** È la parola inserita nel "dizionario" dell'indice. Se la parola "il" compare 10.000 volte, nel dizionario verrà inserita **una sola volta**. È un _type_.

Ecco perché le medie sono così diverse
1. La media sui Token (4.5 bytes)
	1. In quasi tutte le lingue naturali (inglese incluso, che è la lingua del dataset RCV1), **le parole usate più di frequente sono molto corte**. Pensa ad articoli, preposizioni e congiunzioni come _the_, _a_, _of_, _to_, _in_, _and_. Quando calcoli la lunghezza media dei _token_, stai contando queste paroline di 1, 2 o 3 lettere milioni di volte. Questa valanga di parole cortissime "tira giù" inesorabilmente la media matematica, portandola a circa 4.5 caratteri (in questo contesto, 1 byte = 1 carattere standard ASCII).
2. La media sui Type / Term (7.5 bytes)
	1. Quando calcoli la media sui _type_, stai guardando la lista del vocabolario (i 400.000 termini unici indicati nella slide). In questa lista, la parolina "the" (3 lettere) vale esattamente quanto la parola "information" (11 lettere) o "unconstitutional" (16 lettere): ciascuna conta per uno. Poiché in qualsiasi lingua esistono molte più parole lunghe (termini tecnici, nomi, aggettivi complessi) rispetto alle poche decine di particelle grammaticali corte, la media della lunghezza si alza notevolmente, arrivando a 7.5 caratteri.

**In sintesi:** Leggiamo in continuazione parole corte (ecco perché i token sono di 4.5 bytes in media), ma il nostro vocabolario è composto per la stragrande maggioranza da parole lunghe che usiamo raramente (ecco perché i type sono di 7.5 bytes in media).