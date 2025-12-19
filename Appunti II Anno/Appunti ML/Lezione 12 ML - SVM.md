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
# Support Vector Machine

Il problema della classificazione binaria viene affrontato in modo diretto, ovvero cerchiamo di trovare un piano che separi le classi nello spazio delle feature (in realtà, un piano “ottimale”, secondo una caratteristica ragionevole). 

Se ciò non è possibile, adottiamo due approcci creativi:
- Ammorbidiamo il significato di “separare” e/o
- Arricchiamo e ampliamo lo spazio delle caratteristiche in modo che la separazione sia (più) possibile

Prima di tutto, osserviamo che la maggior parte degli algoritmi di classificazione non produce solo un'etichetta di classe, ma anche un punteggio, e l' etichetta prevista viene assegnata sulla base di tale punteggio, che viene confrontato con una soglia.

Nella classificazione lineare, il punteggio viene calcolato come una combinazione lineare $\mathbf{w}^T \mathbf x + b$ delle feature.

Ad esempio, la regressione logistica restituisce la probabilità di classe
$$p(y=1|\mathbf x)=\sigma(\mathbf w^{T}\mathbf x+b)\in[0,1]$$
e potremmo seguire la strategia di prevedere la classe $1$ se la probabilità della classe è $\gt 0,5$.

Essenzialmente, il punteggio è una stima della confidenza: più è lontano dalla soglia, più siamo sicuri della previsione. 

In termini geometrici, il punteggio rappresenta anche la distanza fra il punto corrispondente all'elemento dato e il confine decisionale, che è l'iperpiano $\mathbf{w}^T \mathbf x + b=0$

![center|500](img/Pasted%20image%2020251219155957.png)

Per esempio, nel seguente caso:

![center|400](img/Pasted%20image%2020251219160421.png)

$A$ può essere assegnato a $\mathbf C_1$ con maggiore sicurezza rispetto a $B$ e con ancora maggiore sicurezza rispetto a $C$.

Queste considerazioni, se applicate alla fase di addestramento, portano a preferire confini decisionali tali che tutti gli elementi nel training set siano classificati correttamente (si trovano nella regione decisionale corretta) e fare riferimento a quel confine ci rende sicuri di tale classificazione (si trovano abbastanza lontani dal confine).

Intuitivamente, vogliamo selezionare confini che classifichino correttamente gli elementi nel training set caratterizzati da un margine di spazio intorno a essi che non contenga alcun elemento.

Più in dettaglio, consideriamo un classificatore binario che, per qualsiasi elemento $\mathbf x$, restituisce un valore $y \in \{-1, 1\}$, dove supponiamo che $\mathbf x$ sia assegnato a $C_0$ se $y = -1$ e a $C_1$ se $y = 1$.

Inoltre, consideriamo classificatori lineari come
$$h(\mathbf x)=g(\mathbf w^{T}\mathbf x+b)=g(\overline{\pmb w}^{T}\overline{\pmb x})$$
dove $$g(z)=\begin{cases}1&z\geq0\\-1&z\lt0\end{cases}$$
La previsione sulla classe di $\mathbf x$ viene quindi fornita derivando un valore in $\{-1, 1\}$ proprio come nel caso di un percettrone, ovvero senza alcuna stima delle probabilità $p(C_i|\mathbf x)$ che $\mathbf x$ appartenga a ciascuna classe.

Per qualsiasi elemento del training set $(\mathbf x_i, t_i)$, il **margine funzionale** di $(\mathbf w, b) = \overline{\mathbf w}$ rispetto a tale elemento è definito come:
$$\overline{\gamma}_{i}=t_{i}(\mathbf w^{T}\mathbf x+b)=t_{i}\overline{\mathbf w}^{T}\overline{\mathbf x}_{i}$$

Si osservi che la previsione risultante è corretta se e solo se $\overline{\gamma}_i > 0$.

Inoltre, assumiamo che valori maggiori di $\overline{\gamma}_i$ indichino una maggiore confidenza nella previsione.

Dato un training set $\mathcal{T} = \{(\mathbf{x}_1, t_1), \dots, (\mathbf{x}_n, t_n)\}$, il margine funzionale di $\overline{\mathbf{w}}$ rispetto a $\mathcal{T}$ è il margine funzionale minimo tra tutti gli elementi in $\mathcal{T}$:

$$\overline{\gamma} = \min_{i} \overline{\gamma}_i$$

Tuttavia, abbiamo un problema con questa definizione:

- Se riscaliamo i parametri $\overline{\mathbf{w}}$ per uno scalare $\alpha > 0$, otteniamo nuovi parametri $\alpha\overline{\mathbf{w}}$, ovvero $\alpha\mathbf{w}, \alpha b$.    
- L'utilizzo di $\alpha\overline{\mathbf{w}}$ non cambia la classificazione dei punti.
- Tuttavia, il margine $\alpha\overline{\mathbf{w}}^T \overline{\mathbf{x}}_i = \alpha\mathbf{w}^T \mathbf{x}_i + \alpha b$ risulta ora scalato di $\alpha$.

Non ha senso che lo stesso confine di classificazione possa avere margini diversi quando lo riscaliamo.

Al fine di superare questo inconveniente, definiamo il **margine geometrico** $\gamma_i$ rispetto a un esempio di addestramento $(\mathbf{x}_i, t_i)$ come:
$$\gamma_{i}=t_{i}\left(\frac{\mathbf w^{T}}{||\mathbf w||}\mathbf x_{i}+\frac{b}{||\mathbf w||}\right)=\frac{\overline{\gamma_{i}}}{||\mathbf w||}$$
dove, come di consueto, $\|\mathbf{w}\| = \sqrt{\sum_{i=1}^d w_i^2}$. 

Il margine geometrico $\gamma_i$ equivale alla distanza (con segno) tra $\mathbf{x}_i$ e l'iperpiano definito da $\mathbf{w}, b$, ovvero la lunghezza del segmento di retta da $\mathbf{x}_i$ alla sua proiezione sull'iperpiano di confine, espressa utilizzando $\|\mathbf{w}\|$ come unità di distanza.

![center|400](img/Pasted%20image%2020251219162249.png)

Diversamente da $\overline{\gamma}_i$, il margine geometrico $\gamma_i$ è invariante rispetto al riscalamento dei parametri. 

Infatti, sostituendo $\alpha\overline{\mathbf{w}}$ a $\overline{\mathbf{w}}$, abbiamo:

$$t_i \overline{\mathbf{w}}^T \overline{\mathbf{x}}_i = t_i (\mathbf{w}^T \mathbf{x}_i + b) = \overline{\gamma}_i$$
$$t_i (\alpha\overline{\mathbf{w}})^T \overline{\mathbf{x}}_i = t_i (\alpha\mathbf{w}^T \mathbf{x}_i + \alpha b) = \alpha t_i (\mathbf{w}^T \mathbf{x}_i + b) = \alpha (t_i \overline{\mathbf{w}}^T \overline{\mathbf{x}}_i) = \alpha \overline{\gamma}_i$$

mentre

$$t_i \frac{\overline{\mathbf{w}}^T}{\|\mathbf{w}\|} \overline{\mathbf{x}}_i = t_i \left( \frac{\mathbf{w}^T}{\|\mathbf{w}\|} \mathbf{x}_i + \frac{b}{\|\mathbf{w}\|} \right) = \gamma_i$$

$$t_i \frac{(\alpha\overline{\mathbf{w}})^T}{\|(\alpha\mathbf{w})\|} \overline{\mathbf{x}}_i = t_i \left( \frac{\alpha\mathbf{w}^T}{\alpha\|\mathbf{w}\|} \mathbf{x}_i + \frac{\alpha b}{\alpha\|\mathbf{w}\|} \right) = t_i \left( \frac{\mathbf{w}^T}{\|\mathbf{w}\|} \mathbf{x}_i + \frac{b}{\|\mathbf{w}\|} \right) = \gamma_i$$

- Il margine geometrico rispetto al training set $\mathcal{T} = \{(\mathbf{x}_1, t_1), \dots, (\mathbf{x}_n, t_n)\}$ è quindi definito come il più piccolo margine geometrico tra tutti gli elementi $(\mathbf{x}_i, t_i)$:$$\gamma = \min_{i} \gamma_i$$
- Un'interpretazione utile di $\gamma$ è come la metà dell'ampiezza della fascia più larga, centrata sull'iperpiano $\mathbf{w}^T \mathbf{x} + b = 0$, che non contiene nessuno dei punti $\mathbf{x}_1, \dots, \mathbf{x}_n$.
- Gli iperpiani sul confine di tale fascia, ciascuno a distanza $\gamma$ dall'iperpiano e passanti (almeno uno di essi) attraverso qualche punto $\mathbf{x}_i$, sono detti **iperpiani a margine massimo** (maximum margin hyperplanes).

![center|500](img/Pasted%20image%2020251219162354.png)

## Optimal margin classifiers
