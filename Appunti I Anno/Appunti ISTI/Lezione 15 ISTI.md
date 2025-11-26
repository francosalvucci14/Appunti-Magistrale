# Efficienza degli stimatori ML

Per parlare di efficienza degli stimatori ML, osserviamo che la matrice di informazione è strettamente legata all'efficienza

introduciamo il concetto di **stimatori B.U.E**

>[!definition]- Stimatori B.U.E (Best Unbiased Estimator)
>Uno stimatore si dice B.U.E se vale la non distorsione (ovvero $\mathbb E[T_{n}]=\theta_{0}$) e per ogni altro stimatore $T_{n}^{'}:\mathbb E[T_{n}^{'}]=\theta_{0}$ allora vale che $$Var(T_{n})\leq Var(T_{n}^{'})$$

Vediamo subito il seguente lemma

>[!teorem]- Lemma 1
>Se esiste lo stimatore B.U.E, allora lui è unico.
>In altre parole, non esistono due stimatori B.U.E in contemporanea

**dimostrazione lemma 1**

Assumiamo che esistano altri due stimatori B.U.E oltre a $T_n$, ovvero $T_{n}^{'},T_{n}^{''}$
Riscriviamo quindi $T_{n}^{''}=\alpha T_{n}+(1-\alpha)T_{n}^{'}$ (se $\alpha\in[0,1]$ allora è non distorto)
Dove sta l'assurdo? L'assurdo sta nel fatto che, come vedremo, la varianza di $T_{n}^{''}$ potrebbe essere più piccola di quella di $T_{n}^{'},T_{n}$

Calcoliamo la varianza di $T_{n}^{''}$:
$$\begin{align*}
Var(T_{n}^{''})&=\alpha^{2}Var(T_{n})+(1-\alpha)^{2}Var(T_n^{'})+2\alpha Cov(T_{n},T_{n}^{'})\\
(Var(T_{n})=Var(T_{n}^{'})=\sigma^{2})&=\sigma^{2}(\alpha^{2}+(1-\alpha)^{2})+2\alpha(1-\alpha)^{2}Cov(T_{n},T_{n}^{'})\\
\text{Per Cauchy-Schwartz}&=\sigma^{2}\left(\overbrace{\alpha^{2}+(1-\alpha)^{2}+2\alpha(1-\alpha)}^{=1}\underbrace{\frac{Cov(T_{n},T_{n}^{'})}{\sqrt{Var(T_{n})Var(T_{n}^{'})}}}_{\star}\right) 
\end{align*}$$
Ora, se $(\star)$ fosse $\lt1$, allora tutto il calcolo verrebbe $\lt1$, e di conseguenza risulterebbe che $T_n^{''}$ migliore sia di $T_n$ che $T_{n}^{'}$, ma questo è **assurdo** perchè per ipotesi $T_n$ è B.U.E
## Limite inferiore di Cramer-Rao

Un risultato notevole riguarda la determinazione della varianza minima degli stimatori non-distorti, sotto condizioni di regolarità; in particolare, emerge che tale varianza minima coincide con quella degli stimatori di massima verosimiglianza, sotto condizioni di regolarità.

Per tale motivo, gli stimatori di massima verosimiglianza sotto opportune ipotesi (che coprono gran parte delle distribuzioni di uso comune, almeno nei casi più semplici) risultano essere non solo consistenti ed asinotitcamente Gaussiani, ma anche efficienti in senso assoluto.

**oss**
È evidente che porsi la questione sulla varianza minima ha senso solo per stimatori che siano non-distorti; altrimenti qualsiasi stimatore con valore identicamente costante non potrebbe essere migliorato, avendo varianza identicamente pari a zero.

Vediamo quindi questo risultato, chiamato **Teorema di Cramer-Rao**

>[!teorem]- Teorema di Cramer-Rao
>Sotto condizioni di regolarità, prendiamo $T_{n}:\mathbb E[T_{n}]=\theta_{0}$
>Allora:
>1. (Se stimatore non distorto) : $$Var(T_{n})\geq\frac{1}{I_{n}(\theta_{0})}\quad\text{oppure }\frac{1}{nI_{1}(\theta_{0})}$$
>2. (Se stimatore distorto) : $$Var(T_{n})\geq\frac{\left(\frac{\partial}{\partial\theta_0}\mathbb E[T_{n}]\big|_{\theta=\theta_{0}}\right)^{2}}{I_{n}(\theta_{0})}$$

**dimostrazione teorema** (sempre nel caso $p=1$)

Sappiamo che $Cov^{2}(X,Y)\leq Var(X)Var(Y)$, e quindi, per la **disuguaglianza di Cauchy-Schwartz** vale che $$Var(Y)\geq\frac{Cov^{2}(X,Y)}{Var(X)}$$
Prendiamo ora $Y=T_{n}$ come definito dal teorema, e $X=s_{n}=\frac{\partial}{\partial\theta}\log L_{n}(\theta;X_{1},\dots,X_{n})$
Ricordiamo le proprietà fondametali della funzione punteggio, e quindi otteniamo che:
1. $\mathbb E[s_{n}]\big|_{\theta=\theta_{0}}=0$
2. $\mathbb E[s^{2}_{n}]\big|_{\theta=\theta_{0}}=I_{n}(\theta_{0})=-\mathbb E\left[\frac{\partial^{2}\log L}{\partial\theta^{2}}\right]\big|_{\theta=\theta_{0}}$

Presi quindi $X,Y$ in questo modo, otteniamo che $$Var(T_{n})\geq\frac{Cov^{2}(s_{n},T_{n})}{I_{n}(\theta_{0})}$$
A questo punto ci resta solamente da dimostrare che $Cov(s_{n},T_{n})=\frac{\partial}{\partial\theta_0}\mathbb E[T_{n}]$

Vediamo quindi che:
$$\begin{align*}
\frac{\partial}{\partial\theta_0}\mathbb E[T_{n}]&=\frac{\partial}{\partial\theta_0}\int T(x_1,\dots,x_{n})f(x_{1},\dots,x_{n};\theta)dx_1,\dots,dx_{n}\\
\text{scambio int-der.}\to&=\int T(x_1,\dots,x_{n})\frac{\partial}{\partial\theta_0}f(x_{1},\dots,x_{n};\theta)dx_1,\dots,dx_{n}\\
\text{molt. e div. per }f(x,\dots,\theta)\to&=\int T(x_1,\dots,x_{n})\underbrace{\frac{\frac{\partial}{\partial\theta_0}f(x_{1},\dots,x_{n};\theta)}{f(x_{1},\dots,x_{n})}}_{\text{derivata }\log L}f(x_{1},\dots,x_{n})dx_1,\dots,dx_{n}\\
&=\mathbb E[s_{n}T_{n}]
\end{align*}$$

Abbiamo quindi ottenuto che $Cov(s_{n},T_{n})=\frac{\partial}{\partial\theta_0}\mathbb E[T_{n}]=\mathbb E[s_{n}T_{n}]$, e quindi possiamo concludere la dimostrazione perchè :
$$Var(T_{n})\geq\frac{(\frac{\partial}{\partial\theta}\mathbb E[T_{n}])^{2}}{I_{n}(\theta_{0})}$$
che è proprio l'enuniciato del teorema. $\blacksquare$

Vale ora la seguente osservazione:
**osservazione**
Sotto le condizioni di regolarità, preso uno stimatore non distorto, lui raggiungerà il limite inferiore di Cramer-Rao se 
$$\exists\alpha(\theta):\alpha(\theta)(T_{n}-\theta)=s_{n}(\theta)$$

Altra domanda, come cambia l'enunciato del teorema se trattiamo il caso $p\gt1$?
Risposta:
1. $\mathbb E[(T_n-\theta)(T_{n}-\theta)^{T}]\geq I_{n}^{-1}(\theta_0)$
2. $\mathbb E[(T_n-\theta)(T_{n}-\theta)^{T}]\leq\underbrace{(D\psi)}_{\text{Jacobiana}}I_{n}^{-1}(\theta_{0})(D\psi)^{T}$ 

---
# Statistiche Sufficienti

Una domanda naturale che possiamo porci, specialmente in un momento in cui masse enormi di dati sono a disposizione, è la seguente: posso comprimere un campione di dati osservati senza perdere informazione sul parametro che mi interessa? Questa domanda ci porta alla nozione di statistiche sufficienti.

>[!definition]- Statistiche Sufficienti
>Supponiamo che $X_{1},\dots,X_{n}$ sia un campione i.i.d preso da un certo modello $(\Omega,\mathcal F,P_{\theta})$
>Il campione ha **legge congiunta** $f(X_{1},\dots,X_{n})$
>Un certo stimatore $T=T_{n}(X_{1},\dots,X_{n})$ è detto **statistica sufficiente** se e solo se $h(X_{1},\dots,X_{n}|T)$ ***non dipende da*** $\theta$

Avremo quindi che 
$$L(\theta;X_{1},\dots,X_{n})=f(X_{1},\dots,X_{n}|\theta)=h(X_{1},\dots,X_{n}|T)g(T;\theta)$$
dalla definizione di probabilità condizionata è immediato verificare che T è sufficiente se e solo se $p(X_1,\dots,X_n;\theta )=q(T (X_1,\dots,X_n;\theta)$ non dipende da $\theta$

Vediamo quindi un esempio:

**Esempio**

$X_1,\dots,X_n\sim Ber(\theta)$ i.i.d
La loro legge congiuta è $$p(X_1,\dots,X_n;\theta)=\theta^{\sum\limits_{i=1}^{n}X_i}(1-\theta)^{n-\sum\limits_{i=1}^{n}X_{i}}$$
Verifichiamo che $T_{n}:=\sum\limits_{i=1}^{n}X_i$ è una statistica sufficiente
La sua funzione di probabilità è una binomiale, data quindi da:
$$q(T;\theta)={n \choose \sum_{i=1}^{n}X_{i}}\theta^{\sum\limits_{i=1}^{n}X_i}(1-\theta)^{n-\sum\limits_{i=1}^{n}X_{i}}$$
e quindi:
$$\frac{p(X_1,\dots,X_n;\theta)}{q(T;\theta)}=\frac{1}{{n\choose \sum_{i=1}^{n}X_{i}}}$$
che è indipendente da $\theta$ 
