
# Codice vulnerabile

```php

<?php

if( isset( $_POST[ 'submit' ] ) ) {

    $target = $_REQUEST[ 'ip' ];

    // Determine OS and execute the ping command.
    if (stristr(php_uname('s'), 'Windows NT')) { 
    
        $cmd = shell_exec( 'ping  ' . $target );
        echo '<pre>'.$cmd.'</pre>';
        
    } else { 
    
        $cmd = shell_exec( 'ping  -c 3 ' . $target );
        echo '<pre>'.$cmd.'</pre>';
        
    }
    
}
?>
```

Per iniettare comandi arbitrari è sufficiente inserire il carattere `;` che termina l'attuale istruzione in bash, quindi iniziarne una nuova.

```bash
ping -c 3 127.0.0.1; whoami
```

![](attachments/Pasted%20image%2020250526121808.png)

