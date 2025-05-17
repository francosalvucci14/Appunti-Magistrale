# Elliptic Curve Digital Signature Algorithm (ECDSA)

Sia $(\mathbb F_p, +, \cdot)$, con $p$ primo il campo dei numeri ${0, 1, \dots , p − 1}$ con le usuali operazioni di somma e prodotto modulo $p$. 
Sia $\mathcal C = \{(x, y) \in \mathbb F_2^p : y^2 = x^3 + ax + b\} \cup \{\infty\}$ una curva ellittica. 
Sia $G \in \mathcal C$ un punto della curva tale che **l’ordine** $n$ del gruppo $\langle G\rangle$ generato da $G$ sia primo. Sia $(sk, pk)$, con $sk \in \{1,\dots , n − 1\}$ e $pk = sk \cdot G$, una coppia di chiavi. 
Sia **Hash** una funzione hash crittografica. (SHA256)

L’algoritmo di firma digitale ***ECDSA*** di un messaggio ⟨msg⟩ funziona in questo modo :

**SIGN_ECDSA**(msg,sk):
1. Calcolo $h=Hash(msg)$ (SHA256)
2. Scegli $k\lt n$ u.a.r (e possibilmente con uno schema random sicuro)
	1. Sia ora $R=kG$ e sia $r$ la coordinata "x" di $R$
3. Calcola $s=k^{-1}(h+r\cdot sk) (mod(n))$
4. Restituisci $\sigma=(r,s)$

Osserviamo che è cruciale che il valore $k$ scelto alla linea 2 rimanga segreto, altrimenti dal messaggio ⟨msg⟩, dalla firma $\sigma = (r, s)$ e da $k$ si può ricavare la chiave segreta $sk$ invertendo l’equazione alla linea 3.

Questo non è l’unico fatto a cui bisogna fare attenzione, infatti bisogna assicurarsi che il valore di $k$ deve essere diverso ad ogni esecuzione, infatti vediamo questo breve esempio

Se conosciamo due messaggi distinti, $m_1$ e $m_2$, e due firme, $\sigma_1$ e $\sigma_2$ di $m_1$ e $m_2$ rispettivamente, ottenute con lo stesso valore $k$, allora possiamo ricavare la $sk$ con cui sono state generate le firme. (per soluzione vedi sotto)

Per evitare tutto questo, invece che generare $k$ u.a.r lo generiamo deterministicamente ([vedi qui](https://www.rfc-editor.org/rfc/rfc6979.html#section-3.2)) a partire dal messaggio stesso e dalla chiave segreta, in modo da evitare l'accesso a uno "pseudorandom generator" sicuro ogni volta che bisogna firmare il messaggio e in modo da evitare la possibilità che ci siano due messaggi con stessa firma

Vediamo ora l'algoritmo di Verifica per ECDSA

**Verify_ECDSA**(msg,$pk$,$\sigma=(r,s$)
1. Calcola $h=Hash(msg)$ (anche qui SHA256)
2. Calcola $\begin{cases}u_1=s^{-1}h(\text{mod n})\\ u_2=s^{-1}r(\text{mod n})\end{cases}$
3. Calcola il punto sulla curva $\hat{R}=u_1G+u_2pk$
4. Ritorna **True** se la coordinata "x" di $\hat{R}$ è uguale a $r$, **False** altrimenti

# L'Upgrade Segregated Witness (SegWit) in Bitcoin

Prima di parlare di SegWit, dobbiamo parlare di Soft Fork.

Una **Soft Fork** è una modifica al protocollo che risulta essere ***retrocompatibile***, infatti se alcuni nodi non fanno l'upgrade possono comunque vedere i blocchi generati dai nodi che hanno fatto l'upgrade, e per loro quei blocchi saranno comunque validi
- In caso contrario si parla di **Hard Fork**

Nell’upgrade al protocollo Bitcoin denominato **Segregated Witness (SegWit)** sono state apportate numerose modifiche.

Una delle modifiche principali è stata una diversa serializzazione delle transazioni, per risolvere il problema della [malleabilità](https://en.wikipedia.org/wiki/Transaction_malleability_problem).
Per fare ciò, sono state spostate le firme nelle transazioni in un altro posto, e sono stati aggiunti due byte, il primo chiamato **Marker** e l'altro **Flag**

Il nuovo formato di Transazioni diventa quindi 
```
[nVersion][marker][flag][txins][txouts][witness][nLockTime]
```

Il formato di nVersion, txins, txouts e nLockTime è lo stesso della serializzazione tradizionale.

Il **marker** DEVE essere un valore zero a 1 byte: $0x00$.
Il **flag** DEVE essere un valore non nullo a 1 byte. Attualmente si DEVE usare $0x01$.

Il **witness** è una serializzazione di tutti i campi witness della transazione. A ogni input della transazione (TxIN) è associato un campo witness. Un campo witness inizia con un **var_int** per indicare il numero di elementi in pila per la TxIN. 
È seguito da elementi di pila, e ogni elemento inizia con una **var_int** per indicare la lunghezza. 
I dati del **testimone** NON sono script.
$
Dopo l'upgrade SegWit sono stati cambiati anche i tipi di Scritp, infatti vale : 
- $\text{p2pk}\to None$ : infatti lo script $\text{p2pk}$ è stato rimosso
- $\text{p2pkh}\to \text{p2wpkh}$ : **pay-to-witness-public-key-hash**
- $\text{p2sh}\to\text{p2wsh}$ : **pay-to-witness-script-hash**

L'upgrade SegWit è stato un Soft Fork
# Esercizi

## Esercizio 1

Siano $m_1 \neq m_2$, firmati entrambi con lo stesso $k$, e sia:
- $h_1=Hash(m_1),h_3=Hash(m_2)$
- $\sigma_1=(r,s_1​)$ : firma di $m_1$​
- $\sigma_2=(r,s_2)$ : firma di $m_2$

Poiché $k$ è lo stesso, anche $r$ è lo stesso
Per la firma di $m_1$:

$$s_1 = k^{-1}(h_1 + sk \cdot r)\mod (n)\implies k⋅s_1=h_1+sk⋅r\mod (n)\quad(1)
$$

Per la firma di $m_2$​:

$$s_1 = k^{-1}(h_1 + sk \cdot r)\mod (n)\implies k⋅s_1=h_1+sk⋅r\mod (n)\quad(2)
$$

Sottraiamo (2) da (1):

$$k⋅s_1−k⋅s_2=h_1−h_2\mod (n)\implies k(s_1−s_2)=h_1−h_2\mod  (n)
$$
A questo punto possiamo calcolare $k$:

$$k=\frac{h_1-h_2}{s_1-s_2}\quad(\iff s_1\neq s_2)$$
e di conseguenza, una volta calcolato $k$, possiamo calcolare $sk$:

$$\text{Da (1)}: sk = \frac{k \cdot s_1 - e_1}{r} \mod (n)$$
