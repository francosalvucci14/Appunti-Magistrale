# Foundamentals

Le fondamenta del ***Machine Learning*** (**apprendimento automatico**) risiedono nel nostro accesso a una raccolta di punti dati, ciascuno dei quali rappresenta l'osservazione dei valori di un insieme di variabili predefinite, generate da un processo sconosciuto. 

Il punto cruciale di questo quadro è la premessa che questi dati, lungi dall'essere casuali, possiedono una **struttura intrinseca**, anche se **spesso difficile da identificare**.

L'essenza dell'apprendimento automatico risiede in due obiettivi primari, ciascuno dei quali affronta un aspetto diverso dell'analisi dei dati:

1) **Unsupervised Learning** : In questo caso, il nostro obiettivo è quello di estrarre approfondimenti significativi sulla struttura sottostante dei dati, approfondendo così la nostra comprensione della loro natura intrinseca. Questo approccio spesso comporta tecniche quali il ***clustering***, la ***riduzione della dimensionalità*** o la ***modellazione generativa***. Un'applicazione particolarmente interessante dell' apprendimento non supervisionato è la capacità di generare algoritmicamente nuovi punti di dati che sono, in larga misura, indistinguibili dal set di dati originale. Questi punti di dati sintetici sembrano essere prodotti dallo stesso processo sconosciuto, imitando efficacemente le caratteristiche intrinseche e le distribuzioni dei dati.
2) **Supervised Learning**: In questo paradigma, miriamo a prevedere informazioni aggiuntive per ogni elemento di dati sulla base delle conoscenze esistenti. Ciò comporta tipicamente l'addestramento di modelli su dati etichettati per fare previsioni su istanze non viste. L'apprendimento supervisionato comprende una vasta gamma di compiti, tra cui la ***classificazione***, la ***regressione*** e la ***previsione di sequenze***.

In entrambi questi scenari, partiamo da una serie di osservazioni già prodotte dal processo sconosciuto. 
Questo set di dati iniziale funge da base su cui costruiamo i nostri modelli e ricaviamo le nostre intuizioni.

Un quadro alternativo, distinto dai paradigmi supervisionati e non supervisionati, è l'**apprendimento per rinforzo**. (***Reinforcement Learning***)
In questo approccio, ipotizziamo una relazione interattiva con il processo sottostante.

Anziché lavorare con un set di dati statico, ci impegniamo in una procedura dinamica e iterativa:

1. Ad ogni passo, interagiamo con il processo scegliendo ed eseguendo un'azione da una serie di opzioni
	1. di conseguenza, otteniamo una risposta sotto forma di ricompensa
2. l'obiettivo generale è quello di identificare una strategia ottimale per interagire con il processo sconosciuto, che massimizzi la ricompensa cumulativa.

