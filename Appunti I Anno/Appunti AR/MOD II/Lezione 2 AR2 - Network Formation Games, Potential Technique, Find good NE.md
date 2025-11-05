```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# Network Formation Games

I vari NFG modellano modi distinti in cui agenti egoisti possono creare e valutare reti.

Vedremo due modelli:
- Gioco di connessione globale (Global connection game)
- Gioco di connessione locale (Local connection game)

Entrambi i modelli mirano a cogliere due questioni contrastanti: i giocatori vogliono
- minimizzare i costi sostenuti nella costruzione della rete
- garantire che la rete fornisca loro un servizio di alta qualità

I NFG possono essere usati per modellare:
- formazione di social network (gli archi rappresentano le relazioni sociali)
- come le sottoreti si connettono nelle reti informatiche
- formazione di reti che connettono gli utenti tra loro per il download di file (reti P2P)

Dovremmo rispondere alle seguenti domande

Che cos'è una rete stabile?
- Utilizziamo un NE come concetto di soluzione.
- Consideriamo *stabili* le reti corrispondenti agli equilibri di Nash.

Come valutare la qualità complessiva di una rete?
- Consideriamo il costo sociale: la *somma* dei costi dei giocatori.

**Il nostro obiettivo**: limitare la perdita di efficienza derivante dalla stabilità.
## Global Connection Game
