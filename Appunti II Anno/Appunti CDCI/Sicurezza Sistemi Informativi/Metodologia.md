Come si conduce un attacco nei confronti di un target (e.g. società contoso.com).

# Information Gathering

Si definisce la superficie di attacco, l'obiettivo è di allargarla il più possibile.
Se il nostro target è la società **Contoso** il cui dominio è **contoso.com**, la prima fase riguarda l'**enumerazione dei sottodomini** (mail.contoso.com, dev.contoso.com, app.contoso.com etc...).
Quando l'attenzione si sposta verso un singolo server (target.contoso.com), si effettua una scansione dei servizi esposti.
Per le scansioni uno strumento comunemente utilizzato è **nmap** https://nmap.org/, con il quale è possibile verificare quali porte TCP e UDP sono aperte su uno o più target. 

# Ricerca di vulnerabilità

Quando si è a conoscenza dei servizi esposti dal target, si possono cercare vulnerabilità su di essi.
Il metodo più immediato è quello di verificare la presenza di vulnerabilità note pubblicate online come **CVE** (Common Vulnerability and Exposure https://cve.mitre.org/).
Altrimenti, se ne possono trovare di nuove (**0day**) sfruttando diverse tecniche che tratteremo nel corso.

# Exploitation

In questa fase, sulla base delle risultanze rilevate nelle fase precedente, l’attività si concentra nello stabilire un primo accesso al sistema.
   
Qui svolge un ruolo importante l'esperienza dell'attaccante il quale dovrà sfruttare le vulnerabilità rilevate, e al'occasione scrivere degli exploit, per garantirsi un accesso al sistema e/o ai dati contenuti in esso.
   
# Post-Exploitation

L'ultima fase consiste nell'ottenere i privilegi massimi all'interno della macchina su cui si atterra, successivamente ci si sposta sugli altri server della rete fino a prenderne il controllo.

La fase di Post-Exploitation prevede pure delle operazioni per ottenere persistenza, che è ciò che permetterà ad un attaccante di ritornare all'interno della rete pure in futuro senza dover ripetere la fase di Exploitation.

Questo prevede l'utilizzo di beacon e di un'infrastruttura C2 (command and control).