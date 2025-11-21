# Traccia dell'esercizio 1

Avete in input una stringa, contenente sia parole che punteggiatura

Scrivere un programma che:

1.  Pulisca il testo rimuovendo la punteggiatura e convertendo tutto in minuscolo.
2.  Conti la frequenza di ogni parola.
3.  Stampi le parole ordinate **prima** per frequenza (dalla più alta alla più bassa) e, a parità di frequenza, in ordine **alfabetico**. (forse la parte dell'ordinamento da togliere)
Esempio di input: `"La mela, la pera. La banana! Mela, mela."`
# Soluzione esercizio 1

```python
def pulisci_testo(testo): #approccio banale, costo O(n^2)
    testo = testo.lower()
    for x in testo:
        if x in [',', '.', '!', '?', ';', ':']:
            testo = testo.replace(x, '')
    return testo


def conta_frequenza(testo): #conta frequenza delle parole, costo O(n)
    parole = testo.split()
    frequenza = {}
    for parola in parole:
        if parola in frequenza:
            frequenza[parola] += 1
        else:
            frequenza[parola] = 1
    return frequenza


def ordina_parole_per_frequenza(frequenza): #ordinamento banale, costo O(n^2)
    parole = list(frequenza.keys())
    n = len(parole)
    for i in range(n):
        for j in range(i + 1, n):
            if (frequenza[parole[i]] < frequenza[parole[j]]) or (frequenza[parole[i]] == frequenza[parole[j]] and parole[i] > parole[j]):
                parole[i], parole[j] = parole[j], parole[i]
    #parole_ordinate = [(parola, frequenza[parola]) for parola in parole]
    parole_ordinate = []
    for parola in parole:
        parole_ordinate.append((parola, frequenza[parola]))
    return parole_ordinate
testo = "La mela mel!a, mela, la pera. La banana! Mela, mela."
print(f"Testo originale: {testo}")
testo_pulito = pulisci_testo(testo)
print(f"Testo pulito: {testo_pulito}")
frequenza_parole = conta_frequenza(testo_pulito)
print(f"Frequenza parole: {frequenza_parole}")
parole_ordinate = ordina_parole_per_frequenza(frequenza_parole)
print(f"Parole ordinate: {parole_ordinate}")
```
## Spiegazione del codice step-by-step

### Funzione pulisci_testo

Questa funzione prende in input il testo ed esegue le seguenti operazioni:
1. con il metodo `testo.lower()` sostituisco tutti i caratteri **maiuscoli** con i corrispettivi **minuscoli**
2. il ciclo for invece controlla, per ogni *carattere* $x$ del testo se lui appartiene all'insieme `[',', '.', '!', '?', ';', ':']`, ovvero controlla se il carattere $x$ è un carattere di punteggiatura
3. se il carattere è un carattere di punteggiatura, allora lo rimuovo dalla stringa con il metodo `testo.replace(x,'')`, che sostituisce il carattere $x$ con il carattere `''`

### Funzione conta_sequenze

Questa funzione prende in input il testo ed esegue le seguenti operazioni:
1. con il metodo `testo.split()` vado a "splittare" la stringa data in input, ottenendo una lista dove per ogni cella abbiamo una parola, ad esempio: `x = "Hello World", parole = x.split() -> parole = ["Hello","World"]`
- la funzione `split()` senza parametro va a dividere la stringa ogni qual volta trova lo spazio `" "`
2. dopo aver diviso le parole, conto la loro frequenza con un semplice approccio con dizionario, ovvero:
- per ogni parola trovata, se quella parola già è presente nel dizionario, incremento la sua frequenza di una unità `frequenza[parola]+=1,frequenza[parola]=frequenza[parola]+1`
- se quella parola invece *NON* è presente nel dizionario, allora imposto la sua frequenza a `1`

### Funzione ordina_parole

a voce
# Traccia dell'esercizio 2

Hai una lista di stringhe, ad esempio:
`parole = ["roma", "taso", "amor", "sato", "ramo", "mora", "osat", "ciao"]`

Scrivi un programma che raggruppi le parole che sono anagrammi tra loro. 

**Versione 1**
Il risultato deve essere una lista di liste.

**Output atteso:**
`[['roma', 'amor', 'ramo', 'mora'], ['taso', 'sato', 'osat'], ['ciao']]`

**Versione 2**:
In output il dizionario con chiave la parola, e come valore tutti i rispettivi anagrammi

**Output atteso**
`{'amor': ['roma', 'amor', 'ramo', 'mora'], 'aost': ['taso', 'sato', 'osat'], 'acio': ['ciao']}`
## Soluzione esercizio 2

```python
def raggruppa_anagrammi_dict(parole):  # costo O(n * m log m) con n numero di parole e m lunghezza massima di una parola
    anagrammi = {}
    for parola in parole:
        chiave = ''.join(sorted(parola)) #genero la firma della parola, altro non è che la parola con le lettere ordinate
        if chiave in anagrammi:
            anagrammi[chiave].append(parola)
        else:
            anagrammi[chiave] = [parola]
    return anagrammi
parole = ["roma", "taso", "amor", "sato", "ramo", "mora", "osat", "ciao"]
anagrammi_raggruppati = raggruppa_anagrammi_dict(parole)
print("Anagrammi raggruppati (dizionario):")
print(anagrammi_raggruppati)
   
lista_anagrammi = list(anagrammi_raggruppati.values()) # per ottenere una lista di liste
print("\nAnagrammi raggruppati (lista di liste):")
print(lista_anagrammi)
```

# Traccia dell'esercizio 3

Avete in input una lista di elementi, ad esempio: `elementi = ["A","B","C"]`

Scrivere un programma ricorsivo che stampi tutti i sottoinsiemi degli elementi dati in input (ovvero stampare l' **Insieme Potenza** degli elementi in input)

**Output atteso** 
```
Input: ["A","B","C"], n=3
Output:
[]
['C']
['B']
['B', 'C']
['A']
['A', 'C']
['A', 'B']
['A', 'B', 'C']
```

**osservazione** : l'output non deve essere necessariamente in questo ordine (ricordate la teoria dell'insieme potenza)
## Soluzione esercizio 3

```python
def genera_sottoinsiemi_ricorsivo(elementi, indice=0, sottoinsieme_corrente=[]):  # con backtracking, costo O(2^n)
    
    if indice == len(elementi):
        print(sottoinsieme_corrente)
        return

    genera_sottoinsiemi_ricorsivo(elementi, indice + 1, sottoinsieme_corrente)
    sottoinsieme_corrente.append(elementi[indice])
    genera_sottoinsiemi_ricorsivo(elementi, indice + 1, sottoinsieme_corrente)
    sottoinsieme_corrente.pop()
```
