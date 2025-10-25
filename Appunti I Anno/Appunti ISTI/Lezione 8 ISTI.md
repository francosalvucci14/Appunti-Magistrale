# Alcune questioni irrisolte

Questione $1$

Era rimasto da dimostrare che $$X_{n}\to_{d}X\implies X_{n}=O_{p}(1)$$
**dim** (presa dal file dispense)

Per ogni $\varepsilon\gt0$ esiste sicuramente un compatto $K=K_{\varepsilon}\subset\mathbb R$ tale per cui $Pr(X\in K_{\varepsilon})\gt1-\varepsilon$ 

Preso $\varepsilon\gt0$, scegliamo $M_{\frac{\varepsilon}{2}}$ punto di continuità di $F_{X}$ tale per cui 
$$Pr\left(X\in\left[-M_{\frac{\varepsilon}{2}},M_{\frac{\varepsilon}{2}}\right]\right)\gt1-\frac{\varepsilon}{2}$$
Scegliamo ora $n_{0}$ tale per cui $|F_{X_{n}}\left(-M_{\frac{\varepsilon}{2}}\right)-F_{X}\left(-M_{\frac{\varepsilon}{2}}\right)|,|F_{X_{n}}\left(M_{\frac{\varepsilon}{2}}\right)-F_{X}\left(M_{\frac{\varepsilon}{2}}\right)|\leq \frac{\varepsilon}{4}$ per tutti gli $n\gt n_{0}$, allora per un tale $n$ abbiamo che: 
$$\begin{align*}
&Pr\left(X\in\left[-M_{\frac{\varepsilon}{2}},M_{\frac{\varepsilon}{2}}\right]\right)\\=&F_{X_{n}}\left(-M_{\frac{\varepsilon}{2}}\right)+1-F_{X_{n}}\left(M_{\frac{\varepsilon}{2}}\right)\\\leq&|F_{X_{n}}\left(-M_{\frac{\varepsilon}{2}}\right)-F_{X}\left(-M_{\frac{\varepsilon}{2}}\right)|+F_{X}\left(-M_{\frac{\varepsilon}{2}}\right)+1-F_{X}\left(M_{\frac{\varepsilon}{2}}\right)\\&+|F_{X_{n}}\left(M_{\frac{\varepsilon}{2}}\right)-F_{X}\left(M_{\frac{\varepsilon}{2}}\right)|\\\leq&\frac{\varepsilon}{2}+\frac{\varepsilon}{4}+\frac{\varepsilon}{4}=\varepsilon
\end{align*}$$
da cui segue immediatamente che $X_{n}=O_p(1)\quad\blacksquare$

C'è anche il contrario, e vale per il teorema di Prohorov, che dice che $$X_{n}=O_p(1)\implies\exists X_{nk}\to_{d}X$$
**dim** 

Usa il th di Helly-Bray, che afferma quanto segue:

Data $\{F_{n}\}$ successione di funzioni di ripartizione $\exists F_{nk}\to F^{\star}$ con $F^{\star}$ **cadlag** (continua da dx, limitata a sx), $0\leq F^{\star}\leq 1$ non decrescente

Ora, se $X_{n}=O_p(1)\implies \exists k:F_{X_{n}}(-k)\lt\varepsilon$ e $F_{X_{n}}(k)\gt1-\varepsilon$

Ma questa cosa vale anche per $F^{\star}$, infatti $F^{\star}(-k)\lt\varepsilon$ e $F^{\star}(k)\gt1-\varepsilon$
Prendendo i limiti vediamo che $$\lim_{n\to\infty}F^{\star}(-n)=0,\lim_{n\to\infty}(k)=1$$
e quindi la condizione è verificata. (non so come, sulle dispense nse capisce un cazzo)

Questione $2$

Eravamo rimasti alla seguente osservazione

Se $X_{n}\to_{?}X$ ($\to_{?}$ tende a qualunque distribuzione) allora $g(X_{n})\to_{?}g(X)$, con $g$ continua

Ma questa cosa, per quali distribuzioni vale?
Risposta: vale per le sole distribuzioni in probabilità $(2)$ e in media $r$-esima $(3)$, per le altre non vale

---
# Metodo Delta

Vediamo come la convergenza in distribuzione si conserva

Prendiamo $X_{n}=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}$ con $\mathbb E[X_{i}]=\mu,Var(X_{i})=\sigma^{2},X_{i}\sim$ i.i.d
Per il CLT vale che $$\sqrt{n}\left(\frac{X_{n}-\mu}{\sigma}\right)\to_{d}N(0,1)$$
Se poi prendiamo il quadrato (che è una funzione continua) vale che $$\left\{\sqrt{n}\left(\frac{X_{n}-\mu}{\sigma}\right)\right\}^2\to_{d}\chi_{1}^{2}$$
dove $\chi_{1}^{2}$ è: prendi $Z_{i}\sim N(0,1)$ indipendenti, allora $$Z_{1}^{2}+Z_{2}^{2}+\dots+Z_{p}^{2}=\chi_{1}^{2}$$
La domanda ora è, come si comporta $X_{n}^{2}-\mu^{2}$ per $n\to\infty$ ?

**osservazione**

Invece che prendere $g\left(\sqrt{n}\left(\frac{X_{n}-\mu}{\sigma}\right)\right)$ prendiamo $g(X_{n})-g(\mu)$
Dalla legge dei grandi numeri sappiamo che $X_{n}\sim\mu+\frac{1}{\sqrt{n}}$
Se ipotizziamo che $g$ sia differenziabile, allora con l'espressione di Taylor [^1] otteniamo che $$g(X_{n})\simeq g(\mu)+g^{'}(\mu)(X_{n}-\mu)+R(1)$$
Sostiuisco e ottengo che $$g(X_{n})-g(\mu)\sim \cancel{g(\mu)}-\cancel{g(\mu)}+g^{'}(\mu)(X_{n}-\mu)=g^{'}(\mu)(X_{n}-\mu)$$
Usiamo ora quest'altro teorema

>[!teorem]- Metodo Delta ($v1$)
>Sia $X_{n}:\sqrt{n}\left(\frac{X_{n}-\mu}{\sigma}\right)\to_dN(0,1)$ e $g$ differenziabile, allora vale che 
>$$(\star)\sqrt{n}\left(g(X_{n})-g(\mu)\right)\to_{d}g^{'}(\mu)Z,\quad Z\sim N(0,1)$$
>Si può anche dire che $\star$ tende a $N(0,(g^{'}(\mu))^{2})$

Prima della dimostrazione diamo lo sketch dell'idea:

Sappiamo che $$g(X_{n})\sim g(\mu)+g^{'}(\mu)(X_{n}-\mu)+\dots$$
Se sfruttiamo l'enunciato del teorema otteniamo che:
$$\sqrt{n}\left(g(X_{n})-g(\mu)\right)\sim g^{'}(\mu)\sqrt{n}(X_{n}-\mu)$$e questo converge in distribuzione a una $N(0,1)$ per costante

Diamo ora la definizione di un lemma, che ci servià più avanti

>[!teorem]- Lemma
>Sia $\rho:\mathbb R^{n}\to\mathbb R^{n}$ continua con $\rho(X)=o(||X||)$ e $X_{n}\in\mathbb R^{n}:X_{n}\to_{p}0$
>Allora vale che $$\rho(X_{n})=o_p(||X||),\space\text{ovvero }\frac{\rho(X_{n})}{||X_{n}||}=o_{p}(1)$$

**dim lemma**

È sufficiente definire la funzione continua $$\rho(u)=\begin{cases}
\frac{\rho(u)}{||u||}&||u||\neq0\\0&||u||=0
\end{cases}$$
continua perchè se $||u||\to0$ allora $\frac{\rho(u)}{||u||}\to0$
Allora, se $X_{n}\to_p0,g(X_{n})\to_p0$ per il **Lemma di Slutzky** [^2] $\quad\blacksquare$

Siamo ora pronti a dimostrare il teorema Metodo Delta ($v_{1}$)

**dim Metodo Delta**

Prima di tutti scriviamo 
$$\sqrt{n}\left(g(X_{n})-g(\mu)\right)=\sqrt{n}\left(g(\mu+X_{n}-\mu)-g(\mu)\right)$$
Ma questo lo posso riscrivere come $$\sqrt{n}\left(\cancel{g(\mu)}+g^{'}(X_{n}-\mu)+\rho(X_{n}-\mu)-\cancel{g(\mu)}\right)$$
Che posso continuare a riscrivere come 
$$\sqrt{n}(X_n-\mu)\left(\underbrace{g^{'}(\mu)}_{\text{const}}+\overbrace{\frac{\rho(X_{n}-\mu)}{X_{n}-\mu}}^{=o_{p}(1)}\right)\to_{d}Z\sim N(0,1)\cdot const\quad\blacksquare$$
**Esempi**
1. $\sqrt{n}(X_n-\mu)\to_{d}N(0,1)$
2. $\sqrt{n}(X_n^{2}-\mu^2)\to_{d}2\mu Z,Z\sim N(0,4\mu^{2})$
3. $\sqrt{n}\left(e^{X_n}-e^\mu\right)\to_{d}e^\mu Z,Z\sim N\left(0,e^{2\mu}\right)$

Vediamo ora il Metodo Delta generale

>[!teorem]- Metodo Delta ($v_{2}$)
>Sia $a_{n}\uparrow\infty$ e $\exists X_{n}:a_{n}(X_{n}-\mu)\to_{d}X$ con $X_n\in\mathbb R^{p}$
>Sia inoltre $g:\mathbb R^{p}\to\mathbb R^{d}$ differenziabile 
>Allora
>$$a_{n}(g(X_{n})-g(\mu))\to_{d}(\nabla_{p\times d}g(\mu))^{T}X$$
>Dove $\nabla_{p\times d}$ e definita come la **matrice Jacobiana** [^3]

[^1]: https://it.wikipedia.org/wiki/Serie_di_Taylor

[^2]: https://it.wikipedia.org/wiki/Lemma_di_Slutsky

[^3]: https://it.wikipedia.org/wiki/Matrice_jacobiana

