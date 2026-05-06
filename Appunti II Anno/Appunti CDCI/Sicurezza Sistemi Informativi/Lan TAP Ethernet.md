
# RJ45

Il connettore **RJ45** è costituito da contatti in rame separati da un isolamento in plastica.


![](attachments/Pasted%20image%2020250519125055.png)


I dati vengono trasmessi attraverso i collegamenti 1, 2, 3 e 6.

I collegamenti 4, 5, 7 e 8 servono per lo standard **POE** (Power Over Ethernet) che serve a trasmettere energia elettrica sufficiente ad alimentare piccoli dispositivi come telecamere IP, telefoni VoIP, Switch, Hub etc...


![](attachments/Pasted%20image%2020250519125103.png)



# Lan TAP


Un Lan TAP è un dispositivo hardware per il monitoraggio del traffico di rete.

![](attachments/Pasted%20image%2020250519125029.png)

Si puo' facilmente costruirne uno prendendo un qualunque cavo ethernet RJ45 e sdoppiando i collegamenti 1, 2, 3 e 6 verso una terza uscita RJ45.

Un attaccante collegato a questa terza uscita può abilitare un'interfaccia di rete in modalità promiscua per intercettare il traffico di rete che passa attraverso i restanti collegamenti.

```bash
ifconfig eth1 up
ifconfig eth1 promisc
```