# Ancora su Hypercube

>[!definition]- Hypercube scalabile
>L'architettura Hypercube si dice **scalabile** se vale che $$deg(\mathcal H)=Diam(\mathcal H)=\text{ploy-log}$$

Ricordiamo che in $\mathcal H$ abbiamo che : 
- $|V|=n=2^d$
- $|E|=\frac{n\log(n)}{2}=\frac{2^dd}{2}$

Definiamo ora la distanza tra due nodi $\hat{x},\hat{y}\in\mathcal H$, usando la metrica **distanza di Hamming**

>[!definition]- Distanza di Hamming
>Siano $\hat{x},\hat{y}\in\{0,1\}^d$ due stringhe di bit (ovvero due nodi in $\mathcal H$)
>Allora, definiamo la distanza di Hamming tra questi due nodi come $$d_{H}(\hat{x},\hat{y})=\left|\{i\in[d]:x_i\neq y_i\}\right|$$

A questo punto possiamo definire il vicinato di un nodo $\hat{x}$ negli Hypercube

>[!definition]- Vicinato di un nodo
>Sia $\hat{x}\in\{0,1\}^d$ un nodo in $\mathcal H$.
>Il suo vicinato è $$N(\hat{x})=\{\hat{y}\in\{0,1\}^d:d_{H}(\hat{x},\hat{y})=1\}$$
>
