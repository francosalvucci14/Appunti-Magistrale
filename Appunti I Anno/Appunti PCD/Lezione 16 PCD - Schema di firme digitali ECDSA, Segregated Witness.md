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

Se conosciamo due messaggi distinti, $m_1$ e $m_2$, e due firme, $\sigma_1$ e $\sigma_2$ di $m_1$ e $m_2$ rispettivamente, ottenute con lo stesso valore $k$, allora possiamo ricavare la $sk$ con cui sono state generate le firme.

Per evitare tutto questo, invece che generare $k$ u.a.r lo generiamo deterministicamente ([vedi qui](https://www.rfc-editor.org/rfc/rfc6979.html#section-3.2)) a partire dal messaggio stesso e dalla chiave segreta, in modo da evitare l'accesso a uno "pseudorandom generator" sicuro ogni volta che bisogna firmare il messaggio e in modo da evitare la possibilità che ci siano due messaggi con stessa firma

Vediamo ora l'algoritmo di Verifica per ECDSA

**Verify_ECDSA**(msg,$pk$,$\sigma=(r,s$)
1. Calcola $h=Hash(msg)$ (anche qui SHA256)
2. Calcola $\begin{cases}u_1=s^{-1}h(\text{mod n})\\ u_2=s^{-1}r(\text{mod n})\end{cases}$
3. Calcola il punto sulla curva $\hat{R}=u_1G+u_2pk$
4. Ritorna **True** se la coordinata "x" di $\hat{R}$ è uguale a $r$, **False** altrimenti
