
# Rappresentazione simbolica **rwx**

 **Read**: 4 - leggere / elencare

 **Write**: 2 - scrivere / modificare / cancellare

**eXecute**: 1 - eseguire


## Classi utente **ugo**

**User**: Proprietario del file.

**Group**: Membri del gruppo assegnato.

**Others**: Tutti gli altri utenti.

## Rappresentazione numerica (ottale)

Si somma il valore dei permessi per ogni classe:

- `7` (4+2+1): **rwx**
    
- `6` (4+2): **rw-**
    
- `5` (4+1): **r-x**
    
- `4`: (4): **r--**

### Esempi

```bash
chmod 754 file
u=rwx (7), g=r-x (5), o=r-- (4)`.
```

### Comandi Principali

- `chmod`: Modifica i permessi.
    
- `chown`: Modifica il proprietario.
    
- `umask`: Definisce i permessi predefiniti per i nuovi file.

# Permessi speciali (sticky bit, Set GID, Set UID)


I permessi speciali possono alterare il modo in cui funziona una directory o come viene eseguito un programma.

In modalità numerica i permessi speciali vengono specificati in notazione a “4 cifre” (es. **1755**), quindi di fatto la cifra del permesso speciale viene posta davanti alla tripletta che specifica i permessi **rwx**.


![](attachments/Pasted%20image%2020260504104534.png)


Il **SUID** è un permesso speciale applicabile ai file eseguibili. Quando impostato, il file viene eseguito con i privilegi del **proprietario del file** anziché con quelli dell'utente che lancia il comando.

### Rappresentazione

- **Simbolica:** La `x` dell'utente diventa `s` (es. `-rwsr-xr-x`).

- **Numerica:** Si aggiunge il valore **4** all'inizio della terna (es. `4755`).