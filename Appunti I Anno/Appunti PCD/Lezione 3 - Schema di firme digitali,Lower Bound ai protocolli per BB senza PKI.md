# Schema di firme digitali

Uno schema di firme digitali consiste in 3 algoritmi efficienti, dove per efficienti si intende **poly-time nella size dell'input**

I 3 algoritmo sono i seguenti : 

## KeyGen

Algoritmo che genera la coppia di chiavi relative alla lunghezza della stringa

**KeyGen**($1^n$) ($1^n=n$ scritto in unario)
1. il parametro $n$ è chiamato ***security parameter***
2. L'input dell'algoritmo è la lunghezza della stringa

L'input quindi è la lunghezza della stringa, mentre l'output è la coppia $(\underbrace{sk}_{\text{chiave segreta}},\underbrace{pk}_{\text{chiave publica}})\in\{0,1\}^{l(n)}$, dove $l(n)$ è la lunghezza di $n$

## Signature

Algoritmo che ritorna la **firma** del messaggio

**Sign**($\underbrace{m}_{\text{msg}\in\{0,1\}^*},sk$)$\to\underbrace{\sigma}_{\text{firma}}$

>[!warning]- Attenzione
>La firma $\sigma$ è sempre relativa al messaggio $m$

## Verify

Ultimo algoritmo che verifica se la firma è valida

**Verify**($m,pk,\sigma$)$\to$ True/False

Gli algoritmi **KeyGen** e **Sign** sono algoritmi ***probabilistici***, mentre l'algoritmo **Verify** è ***deterministico***

Questi 3 algoritmi devono soddisfare : 
1. **Correttezza** : Dato un qualunque $n$, qualunque $(sk,pk)=KeyGen(1^n)$ e qualunque messaggio $m\in\{0,1\}^*$, deve valere che $$Verify(m,pk,Sign(m,sk))=True$$
2. **Sicurezza** : Per vedere sicurezza l'idea è che le firme non devono essere invertibili
	1. Lo vediamo con l'esperimento falsificazione firma, abbiamo bisogno di:
		1. $(sk,pk)$ generate con KeyGen
		2. Un avversario che ha "oracle access" alla funzione Sign($\cdot,sk$)
			1. Oracle access = accesso libero alla firma di m
			2. Avversario ha l'accesso alla funzione Sign($\cdot,sk$), ma questo non significa che l'avversario ha accesso alla $sk$, ma solo che ha accesso all'output di Sign($\cdot,sk$)
		3. Fissato m, l'avversario restituisce una coppia $(m,\sigma)$
	2. Il sistema si dice ***siciuro***