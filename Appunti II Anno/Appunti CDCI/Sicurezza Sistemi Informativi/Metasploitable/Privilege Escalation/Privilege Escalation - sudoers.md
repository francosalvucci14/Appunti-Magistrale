
Il file `/etc/sudoers` è il file di configurazione per il comando **sudo**. 

Definisce quali utenti possono eseguire comandi con privilegi di root (o di altri utenti specifici) e quali comandi possono essere eseguiti.

Un utente puo' visualizzare la propria configurazione sudoers con `sudo -l`.

![](attachments/Pasted%20image%2020250515172421.png)

In questo caso, vediamo che l'utente **www-data** puo' eseguire `/usr/bin/vim` come utente **user**.

# Abuse sudo vim

Questa configurazione è sfruttabile per ottenere i privilegi dell'utente **user**.

Per eseguire **vim** come **user** è necessario il comando:

```bash
sudo -u user /usr/bin/vim
```

Il parametro `-u` definisce con quale utente eseguire il comando.

Dato che per il binario *vim* è impostata la direttiva **NOPASSWD** non verrà richiesta alcuna password.

All'interno di vim si puo' usare la sequenza `:q!/bin/sh` per ottenere una shell.

![](attachments/Pasted%20image%2020250515172924.png)

Dato che vim è stato eseguito come utente **user** (sudo -u user), la shell avrà quel privilegio.

![](attachments/Pasted%20image%2020250515172951.png)