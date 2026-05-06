
# SUID

Oltre al tradizionale set di permessi di read, write e execute (**rwx**), i file in un sistema Linux possono anche avere alcuni permessi speciali come i bit SUID o SGID.

```bash
user@hostname:~$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 63736 jul 27  2018 /usr/bin/passwd
```

La **s** in **rws** indica la presenza del SUID sul file insieme al permesso execute.

Un file con il bit SUID impostato viene sempre eseguito con l'ID dell'**owner** del file.

Per cercare i file che dispongono del bit SUID in un file system si puo' usare:

```bash
find / -perm /4000 2>/dev/null
```

![](attachments/Pasted%20image%2020250515114919.png)

# Privilege Escalation con SUID su nmap

Il binario `/usr/bin/nmap` dispone del bit SUID e il suo owner risulta essere l'utente **root**.

![](attachments/Pasted%20image%2020250515115015.png)

Quest implica che il binario verrà eseguito da qualsiasi utente come se fosse root.

Nmap puo' eseguire script in python e dispone di una modalità interattiva, entrambe queste funzionalità possono essere sfruttate per ottenere una escalation all'utente root.

![](attachments/Pasted%20image%2020250515121301.png)

