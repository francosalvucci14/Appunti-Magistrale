# Domanda 1

Qual è la complessità temporale dell'algoritmo `merge` nel caso in cui le sequenze da fondere abbiano dimensione `n` e `m`

Risposte:
- [ ] $O(n\log n)$
- [ ] $O(n\cdot m)$
- [ ] $O(\min(n,m))$
- [ ] $O(\max(n,m))$
- [ ] $O(m\log n)$
# Domanda 2

`a` è una lista Python contenente $\sqrt{n}$ interi ordinati in modo crescente seguiti da altri $\sqrt{n}$ interni non ordinati.

Qual è il costo del miglior algoritmo che ordini la lista `a`?

Risposte:
- [ ] $O(n)$
- [ ] $O(n^2)$
- [ ] $O(\sqrt{n})$
- [ ] $O(\sqrt{n}\log n)$
- [ ] $O(n\log n)$

# Domanda 3

Cosa viene stampato dal seguente codice Python?

```python
a = ['zero','one''two','three','four','five',\
	'six','seven','eight','nine','ten']

d={}

for i in range(len(a)):
	d[a[i]]=i

print(a[d['one']+3+d[a[4]]])
```

Risposte:
- [ ] eight
- [ ] 8
- [ ] Errore
# Domanda 4

`a` e `b` sono due liste concatenate contenenti interi e `d` un dizionario, inizialmente vuoto, implementanto con liste di trabocco

Gli elementi di `d` sono coppie $(k,v)$ dove la chiave $k$ è di tipo intero e il valore $v$ è di tipo puntatore

Vengono eseguite le seguenti operazioni
- per ogni elemento $x$ di `a`, la coppia ($x$,NULL) viene inserita in $d$
- per ogni elemento $x$ di `b`, la coppia ($x$,NULL) viene inserita in $d$

Se `a` contiene $n$ elementi e `b` ne contiene $m$, quanti elementi contiene `d`?

Risposte:
- [ ] almeno $n+m$
- [ ] $\max(n,m)$
- [ ] meno di $n+m+1$
- [ ] $\min(n,m)$
# Domanda 5

Sia `a` una stringa, qual è il risultato di `enigma(a)`?

```python
def enigma(x):
	if x == '':
		return 1
	else:
		return 1+enigma(x[1:])
```

Risposte:
- [ ] $len(a)$
- [ ] $len(a)+1$
- [ ] una stringa formata da $len(a)$ `1` (uni)
- [ ] $0$
# Domanda 6

Qual è il costo computazionale della seguente funzione C?

```C
void f(int n){
	int i,j;
	for(i=0;i<n;i++){
		j=i;
		while(j<n){
			j++;
		}
		while (j>0){
			j--;
		}
	}
}
```

Risposte:
- [ ] $n$
- [ ] $n^{2}$
- [ ] $n^{3}$
- [ ] $n\log(n)$
# Domanda 7

Sia $n$ un intero maggiore di $6$, qual è il risultato di `enigma(n)`?

```python
def enigma(n):
	a = list(range(n))
	A = set(a)
	if len(A)>0:
		B = set(a*6)
		return 1+enigma(len(B-A))
	else:
		return 0
```

Risposte:
- [ ] $n$
- [ ] $0$
- [ ] $1$
- [ ] $6$
# Domanda 8

Qual è il costo computazionale della seguente funzione C in termini di memoria supplementare?

```C
int f(int n){
    int i,j;
    int *a = malloc(sizeof(int)*n);
    int *b;
    for(i=1;i<n;i++){
        b = malloc(sizeof(int)*2);
        b[0] = i;
        b[1] = i+1;
        a[i] = b[0]+b[1];    
    }
    free(a);
    free(b);
    return a[n-1];
}
```

Risposte:
- [ ] Lineare in $n$
- [ ] Quadratica in $n$
- [ ] Cubica in $n$
- [ ] Costante
# Domanda 9

Si consideri il problema di ordinare una sequenza contenente $2n+3$ interi maggiori di $4n+4$  e minori di $6n+8$

Sia $A$ un algoritmo efficiente che risolve il problema, qual è l'ordine di grandezza del suo costo computazionale?

Risposte:
- [ ] $n$
- [ ] $n\log(n)$
- [ ] $n^{2}$
- [ ] costante
# Domanda 10

Siano `a` e `b` due dizionari Python tali che `a` è molto più piccolo di `b`

Qual è la complessità temporale dell'algoritmo più efficiente per calcolare l'intersezione tra le chiavi di `a` e `b`?

Risposte:
- [ ] $O(1)$
- [ ] $O(len(b))$
- [ ] $O(len(a))$
- [ ] $O(len(a)\cdot len(b))$
# Domanda 11

Si consideri la seguente funzione, quale tra le affermazioni è vera?

```C
char *f(char *a){
    int n= strlen(a);
    char *b= malloc(n);
    int i;
    for (i = 0; i < 10; i++)
    {
        b[i] = a[i];
    }
    b[i] = '\0';
    return b;
} 
```

Risposte:
- [ ] La funzione richiede spazio lineare e tempo costante
- [ ] La funzione richiede tempo costante e spazio supplementare costante
- [ ] La funzione richiede tempo lineare e spazio supplementare costante
- [ ] La funzione richiede tempo e spazio supplementare lineare in $n$

