# PREFIX

PREFIX osr: <http://dati.senato.it/osr/>
PREFIX se: <http://example.com/OWL-Senato/#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX wd: <http://www.wikidata.org/entity/>

### Percentuali ROSA - Orientamento

SELECT (xsd:float(?countDonne)/xsd:float(?countAll) AS ?percentualiRosa) ?orientamento
WHERE {
    {
        SELECT ?orientamento (COUNT(?s) AS ?countAll)
    WHERE {
        ?s a osr:Senatore .
        ?s se:appartieneAGruppo ?gruppo .
        ?gruppo se:haAllineamentoPolitico ?orientamento .
    }
    GROUP BY ?orientamento
    }
    {
    SELECT ?orientamento (COUNT(?s) AS ?countDonne)
    WHERE {
        ?s a osr:Senatore .
        ?s osr:sesso "F" .
        ?s se:appartieneAGruppo ?gruppo .
        ?gruppo se:haAllineamentoPolitico ?orientamento .
    }
    GROUP BY ?orientamento
    }
}

### Percentuali ROSA - Gruppo

SELECT (xsd:float(?countDonne)/xsd:float(?countGruppo) AS ?percentualiRosa) ?orientamento ?gruppo
WHERE {
    {
        SELECT ?orientamento (COUNT(?s) AS ?countGruppo) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
        }
        GROUP BY ?orientamento ?gruppo
    }
    {
        SELECT ?orientamento (COUNT(?s) AS ?countDonne) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s osr:sesso "F" .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
        }
        GROUP BY ?orientamento ?gruppo
    }
}

### Percentuali Stranieri - Franco

SELECT (xsd:float(?countStranieri)/xsd:float(?countAll) AS ?percentualiStranieri) ?orientamento ?gruppo
WHERE {
    {
    SELECT ?orientamento (COUNT(?s) AS ?countAll) ?gruppo
    WHERE {
        ?s a osr:Senatore .
        ?s se:appartieneAGruppo ?gruppo .
        ?gruppo se:haAllineamentoPolitico ?orientamento .
    }
    GROUP BY ?orientamento ?gruppo
    }
    {
    SELECT ?orientamento (COUNT(?s) AS ?countStranieri) ?gruppo
    WHERE {
        ?s a osr:Senatore .
        ?s osr:nazioneNascita ?nazione .
        ?s se:appartieneAGruppo ?gruppo .
        ?gruppo se:haAllineamentoPolitico ?orientamento .
        FILTER(?nazione != "Italia")
    }
    GROUP BY ?orientamento ?gruppo
    }
}

### Percentuali Stranieri - Luca

SELECT (xsd:float(?countStranieri)/xsd:float(?countAll) AS ?percentualiStranieri) ?orientamento ?gruppo
WHERE {
    {
        SELECT ?orientamento (COUNT(?s) AS ?countAll) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
        }
        GROUP BY ?orientamento ?gruppo
    }
    {
        SELECT ?orientamento (COUNT(?s) AS ?countStranieri) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s osr:nazioneNascita ?nazione .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
            FILTER(?nazione != "Italia")
        }
        GROUP BY ?orientamento ?gruppo
    }
}

### Percentuale ExtraComunitari

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX osr: <http://dati.senato.it/osr/>
PREFIX se: <http://example.com/OWL-Senato/#>

SELECT ( (xsd:float(?countExtraUE) / xsd:float(?countAll)) AS ?percentualeExtraUE )
WHERE {
    # 1. Calcolo del totale dei senatori (limitato a quelli di cui abbiamo il dato sulla nascita)
    {
        SELECT (COUNT(DISTINCT ?s) AS ?countAll) 
        WHERE {
            ?s a osr:Senatore .
            ?s osr:nazioneNascita ?nazioneNascita . 
        }
    }
    # 2. Calcolo dei senatori nati FUORI dall'Unione Europea
    {
        SELECT (COUNT(DISTINCT ?s) AS ?countExtraUE) 
        WHERE {
            ?s a osr:Senatore .
            ?s osr:nazioneNascita ?nazioneNascita .
            FILTER(STR(?nazioneNascita) NOT IN (
                "Italia", "Francia", "Germania", "Spagna", "Portogallo", 
                "Belgio", "Paesi Bassi", "Lussemburgo", "Austria", "Irlanda", 
                "Finlandia", "Svezia", "Danimarca", "Grecia", "Polonia", 
                "Repubblica Ceca", "Slovacchia", "Ungheria", "Romania", 
                "Bulgaria", "Croazia", "Slovenia", "Estonia", "Lettonia", 
                "Lituania", "Cipro", "Malta"
            ))
        }
    }
}

### Percentuali Extracomunitari - Gruppo

SELECT ( (xsd:float(?countExtraUE) / xsd:float(?countAll)) AS ?percentualeExtraUE ) ?orientamento ?gruppo
WHERE {
    # 1. Calcolo del totale dei senatori (limitato a quelli di cui abbiamo il dato sulla nascita)
    {
        SELECT ?orientamento (COUNT(?s) AS ?countAll) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
        }
        GROUP BY ?orientamento ?gruppo
    }
    # 2. Calcolo dei senatori nati FUORI dall'Unione Europea
    {
        SELECT ?orientamento (COUNT(DISTINCT ?s) AS ?countExtraUE) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
            ?s osr:nazioneNascita ?nazioneNascita .
            FILTER(STR(?nazioneNascita) NOT IN (
                "Italia", "Francia", "Germania", "Spagna", "Portogallo", 
                "Belgio", "Paesi Bassi", "Lussemburgo", "Austria", "Irlanda", 
                "Finlandia", "Svezia", "Danimarca", "Grecia", "Polonia", 
                "Repubblica Ceca", "Slovacchia", "Ungheria", "Romania", 
                "Bulgaria", "Croazia", "Slovenia", "Estonia", "Lettonia", 
                "Lituania", "Cipro", "Malta"
            ))
        }
        GROUP BY ?orientamento ?gruppo
    }
}

### Distribuzione per Età

SELECT (xsd:float(?countEta)/xsd:float(?countAll) AS ?distribuzioneEta) ?orientamento ?gruppo ?eta
WHERE {
    {
        SELECT ?orientamento (COUNT(?s) AS ?countAll) ?gruppo
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
        }
        GROUP BY ?orientamento ?gruppo
    }
    {
        SELECT ?orientamento (COUNT(?s) AS ?countEta) ?gruppo ?eta
        WHERE {
            ?s a osr:Senatore .
            ?s se:appartieneAGruppo ?gruppocod .
            ?gruppocod osr:titolo ?gruppo .
            ?gruppocod se:haAllineamentoPolitico ?orientamento .
            ?s osr:dataNascita ?datanascitasenatore .
            bind( now() as ?adesso).
            bind( year(?adesso)-year(?datanascitasenatore) as ?eta)
        }
        GROUP BY ?eta ?orientamento ?gruppo
    }
}
ORDER BY ?eta