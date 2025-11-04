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
	2. Il sistema si dice ***siciuro*** (existantially chosen-msg attack unforgiable) se: 
		1. Per ogni avversario $A$ (algoritmo probabilistico polinomiale) esiste una funzione ***negligible*** tale che : $$\mathbb P[Verify(m,pk,A(\cdot))=True]\leq negl(n)$$ dove "negligible" tende a $0$ più velocemente di qualunque polinomio in $n$

**Esempio schema di firme (RSA)**

- KeyGen($1^n$)
	- Scegli $p,q$ primi di grandezza $l(n)$
	- Calcola $n=pq$
	- Scelgi $e(=2^{16}+1)$ coprimo con $(p-1)(q-1)$
	- Calcola l'inversa di $e$ mod $(p-1)(q-1)$
		- Ovvero, trovare $d$ t.c $de\equiv 1$ mod $(p-1)(q-1)$
	- Ritorna la coppia : 
		- $sk=(n,d)$
		- $pk=(n,e)$
- Sign(m,sk):
	- Calcola $x=H(m)$, dove $H$ è  una funzione **hash crittografica**, ad esempio $$H:\{0,1\}^*\to\{0,1\}^{256}=sha256$$
		- $H(\cdot)$ deve essere collision-free
	- Ritorna $x^d$ mod $n$
- Verify(m,pk,$\sigma$):
	- Calcola $x=H(m)$
	- Ritorna $\sigma^e$ mod $n==x$

**dimostrazione**

*correttezza: su verify*
$$\sigma^e=(x^d)^{e}=x^{de}=x^{1+\overbracket{k((p-1)(q-1))}^{\text{multiplo di ((p-1)(q-1))}}}=x\cdot \underbracket{x^{k((p-1)(q-1))}}_{(*)}=x\cdot(x^{p-1})^{k(q-1)}\cdot(x^{q-1})^{k(p-1)}\underbrace{=}_{(*)}x\to\sigma^e=x$$
dove per $(*)$ abbiamo usato il **piccolo teorema di Fermat** : $x^{p-1}\equiv 1$ mod $p,p$ primo

*sicurezza: su sign*

In questo caso la situazione è tutt'altro che facile da dimostrare, dato che non esiste uno schema di dimostrazione effettiva

**oss** : con BItcoin non si usa RSA perchè la block-chain sarebbe troppo grande. Infatti si usa la crittografia a curve ellittiche (vedremo dopo)

--- 

# Lower Bound al problema BB senza PKI

>[!teorem]- Teorema
>Senza assunzione PKI nel modello sincrono, nessun protocollo per BB può soddisfare *validity* e *consistency* se ci sono $\geq \frac{n}{3}$ nodi corrotti

**dimostrazione per assurdo**

![center|400](img/Pasted%20image%2020250313101707.png)

Consideriamo questi due scenari.

Supponiamo per assurdo che $\exists$ protocollo $\Pi$ per BB che soddisfa validity e consistency, anche in presenza di un nodo corrotto, nel sistema distribuito $G$

Immaginiamo di avere un'altro sistema distribuito, tale $H$. In questo SD, abbiamo che :
- $x,u$ sono copie del nodo $A$
- $y,v$ sono copie del nodo $B$
- $z,w$ sono copie del nodo $C$

Dal punto di vista dei nodi, loro non sanno se si trovano nel sistema $G$ o nel sistema $H$

A questo punto, eseguiamo il protocollo per BB sul sistema $H$, con il primo $A$ che ha $b=0$ in input, e il secondo $A$ con $b=1$

A questo punto abbiamo 3 scenari : 
1. **Scenario (1)** : A, B sono onesti; C è corrotto e simula il comportamento dei nodi : $z-u-v-w$
	1. A e B danno in output 0
2. **Scenario (2)** : A,C onesti; B è corrotto e simula il comportamento dei nodi $y-x-w-v$
	1. A e C danno in output 1
3. **Scenario (3)** : B,C onesti; A corrotto e simula il comportamento dei nodi $x-w-v-u$
	1. B e C devono dare lo stesso output

I 3 scenari sono in conflitto tra loro, e quindi assurdo
Quindi $\not\exists$ protocollo $\Pi$ per BB che soddisfa validity e consistency se il numero di nodi corrotti è $\leq\frac{n}{3}$ $\blacksquare$
