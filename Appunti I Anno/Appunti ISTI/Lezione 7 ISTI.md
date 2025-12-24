# Teorema del limite centrale

Diamo ora la definizione del **Teorema del Limite Centrale** [^1]


>[!teorem]- Teorema del Limite Centrale
>Siano $\{X_{i}\}_{i=1,\dots,n}\sim$ i.i.d con $\mathbb E[X_{i}]=\mu,Var(X_{i})=\sigma^{2}$ e $\hat{X}_{n}=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i}$
>Allora vale che $$\sqrt{n}\frac{\hat{X}_{n}-\mu}{\sqrt{\sigma^{2}}}\to_{d}N(0,1)$$
>Che possiamo riscrivere come $$\frac{\hat{X}_{n}-\mu}{\sqrt{\frac{\sigma^{2}}{n}}}\to_{d}N(0,1)$$
>Oppure più in generale come $$\frac{\hat{X}_{n}-\mathbb E[\hat{X}_{n}]}{\sqrt{Var(\hat{X}_{n})}}\to_{d}N(0,1)$$

Vediamo ora il th CLT - versione LL (**Lindeberg e Lévy**)

>[!teorem]- LL-CLT
>Prendiamo $X_{i}$ indipendenti ma *non necessariamente* identicamente distribuite con $Var(X_{i})=\sigma_{i}^{2}$
>Allora se vale questa condizione, chiamata **condizione di Lindeberg** [^2] $$\lim_{n\to\infty}\frac{1}{\sum\limits_{i=1}^{n}\sigma_{i}^{2}}\sum\limits_{i=1}^{n}\mathbb E\left[|X_{i}^{2}|\mathbb 1_{\left[X_{i}^{2}\gt\varepsilon\sqrt{\sum\limits_{i=1}^{n}\sigma_{i}^{2}}\right]}\right]=0\space\forall\varepsilon\gt0$$allora vale che $$\frac{\sum\limits_{i=1}^{n}X_{i}-\sum\limits_{i=1}^{n}\mu_{i}}{\sqrt{\sum\limits_{i=1}^{n}\sigma_{i}^{2}}}\to_{d}N(0,1)$$

Notiamo che nel teorema LL-CLT, la condizione di Lindeberg è condizione ***necessaria e sufficiente*** affinchè valga il teorema CLT

Esiste un'altra variante del CLT, ovvero la **variante di Lyapunov**, che sfrutta proprio la **condizione di Lyapunov**, espressa di seguito

>[!teorem]- Condizione di Lyapunov
>Siano $\{X_{i}\}_{i=1,\dots,n}$ con $\mathbb E[X_{i}^{2}]\lt\infty$ indipendenti
>Allora vale che
>$$\lim_{n\to\infty}\frac{1}{s_{n}^{2+\delta}}\sum\limits_{i=1}^{n}\mathbb E\left[|X_{i}|^{2+\delta}\right]=0,\quad s_{n}^{2}=\sum\limits_{i=1}^{n}Var(X_{i})$$per qualche $\delta\gt0$

A differenza della condizione di Lindeberg, quella di Lyapunov è solo condizione ***sufficiente***

Vediamo alcuni esempi di applicazione di questi teoremi

**Esempio 1**

Prendiamo $\mathcal E_{i}$ indipendenti con $\mathbb E[\mathcal E_{i}]=0$, $\mathbb E[\mathcal E_{i}^{4}]\lt\infty$, $\mathbb E[\mathcal E_{i}^{2}]=1$ e $Var(\mathcal E_{i})=1$

Definiamo $$\sum\limits_{i=0}^{n}i^{\alpha}\mathcal E_{i}=\sum\limits_{i=1}^{n}w_{i}$$con:
- $w_{i}=i^{\alpha}\mathcal E_{i}$
- $\mathbb E[w_{i}]=0$
- $Var(w_{i})=i^{2\alpha}Var(\mathcal E_{i})$

L'obiettivo è far vedere che vale il LL-CLT, ovvero che $$\frac{\sum\limits_{i=0}^{n}i^{\alpha}\mathcal E_{i}-\overbrace{\sum\limits_{i=1}^{n}\mathbb E[w_{i}]}^{=0}}{\sqrt{Var\left(\sum\limits_{i=0}^{n}i^{\alpha}\mathcal E_{i}\right)}}\to_{d}N(0,1)$$
Vediamo però che la quantità $$s_{n}^2=Var\left(\sum\limits_{i=0}^{n}i^{\alpha}\mathcal E_{i}\right)=\sum\limits_{i=0}^{n}i^{2\alpha}=\frac{n^{2\alpha+1}}{2\alpha+1}$$se $\alpha\gt- \frac{1}{2}$, altrimenti la somma non converge e non vale il teorema

Vediamo quindi se vale la condizione di Lyapunov:
$$\lim_{n\to\infty}\frac{1}{n^{4\alpha+2}}\sum\limits_{i=1}^{n}\mathbb E\left[|i^{4\alpha}\mathcal E_{i}^{4}|\right]=\lim_{n\to\infty}cost\cdot\frac{n^{4\alpha+1}}{n^{4\alpha+2}}=0$$
La condizione è stat verificata, quindi vale il LL-CLT.

**Esempio 2**

Prendiamo $\sum\limits_{k=1}^{n}e^{k}\mathcal E_{k}$

Così facendo, vale che $$Var\left(\sum\limits_{k=1}^{n}e^{k}\mathcal E_{k}\right)=\sum\limits_{k=1}^{n}e^{2k}\underbrace{Var(\mathcal E_{k})}_{\text{costante}}=\frac{e^{2n+1}-1}{e-1}$$
ma questa quantità, per $n\to\infty$ non tende a zero, e quindi non viene verificata la condizione di Lyapunov, e di conseguenza non vale il LL-CLT

[^1]: Qui ci sono anche le sue varianti -> https://en.wikipedia.org/wiki/Central_limit_theorem

[^2]: https://en.wikipedia.org/wiki/Lindeberg%27s_condition


