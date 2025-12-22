# DOCUMENTO DI PROGETTO: Classificazione di Immagini con Metodi Classici

**Corso di Laurea Magistrale in Computer Science**

## 1. Obiettivo e Strategia

L'obiettivo è sviluppare un classificatore di immagini robusto evitando l'uso di Deep Learning (CNN), dimostrando padronanza delle tecniche di **Feature Engineering** e dei modelli di **Machine Learning tradizionali**.

### Il Dataset Scelto: Fashion-MNIST

Invece del banale MNIST (cifre), si utilizza **Fashion-MNIST**:

- **Contenuto:** 70.000 immagini in scala di grigi (28x28 pixel).
    
- **Classi (10):** T-shirt, pantaloni, maglioni, vestiti, cappotti, sandali, camicie, sneaker, borse, stivali.
    
- **Sfida:** Richiede di distinguere forme complesse (es. la differenza tra un cappotto e una camicia) che i semplici pixel grezzi non rivelano facilmente.
    

---
## 2. La Pipeline di Elaborazione

Il successo del progetto non risiede solo nel modello, ma nella trasformazione dei dati.

### A. Preprocessing & Feature Extraction

I classificatori classici (SVM, RF) non gestiscono bene i pixel grezzi ("Raw Pixels") a causa dell'alta dimensionalità e della sensibilità alle variazioni di luce/posizione.

1. **HOG (Histogram of Oriented Gradients):**
    
    - _Tecnica:_ Divide l'immagine in celle e calcola l'istogramma dell'orientamento dei gradienti (bordi).
        
    - _Perché:_ Cattura la **forma** e la struttura dell'oggetto, rendendolo invariante all'illuminazione. È la tecnica regina pre-Deep Learning.
        
2. **PCA (Principal Component Analysis) - Opzionale:**
    
    - Da usare se il training è troppo lento. Riduce le feature mantenendo il 95% della varianza (riduzione del rumore).
        

---

## 3. Analisi Comparativa dei Modelli

### Modello Principale: Support Vector Machine (SVM)

- **Configurazione:** Kernel RBF (Radial Basis Function) o Polinomiale.
    
- **Perché è il vincitore:**
    
    - Lavora bene in spazi ad alta dimensionalità (creati dall'HOG).
        
    - Massimizza il **margine** tra le classi, riducendo l'overfitting.
        
    - Grazie al Kernel Trick, gestisce confini decisionali non lineari.
        
- **Probabilità:** Di base SVM è geometrico, ma si può usare il **Platt Scaling** (`probability=True`) per ottenere output probabilistici.
    

### Lo Sfidante: Random Forest

- **Configurazione:** Ensemble di alberi decisionali (es. 100 estimatori).
    
- **Punti di forza:**
    
    - **Interpretabilità:** Permette di calcolare la _Feature Importance_ (capire quali parti dell'immagine contano di più).
        
    - Robusto agli outlier e non richiede scaling dei dati.
        
- **Punti deboli:** Su dati sparsi o ad altissima dimensionalità tende a performare leggermente peggio di una SVM ben ottimizzata.
    

### Le Baseline (Da battere):

- **k-NN:** Usato solo come riferimento. Lento in fase di test, non "impara" un modello ma memorizza i dati.
    
- **Perceptron/Regressione Logistica:** Usati per dimostrare che un modello lineare semplice non basta per classificare immagini complesse.
    

---


### 2. Il Dataset: "Olivetti Faces" (o LFW)

Per i volti, Fashion-MNIST non va bene.

Usa Olivetti Faces (già incluso in Scikit-Learn).

- **Cosa contiene:** 400 immagini.
    
- **Soggetti:** 40 persone diverse (10 foto per persona).
    
- **Vantaggio:** È leggero, pulito, in scala di grigi e perfetto per dimostrare PCA e SVM.
    

---

### 3. La Pipeline Aggiornata: "Eigenfaces"

Nel riconoscimento facciale classico, non si usano quasi mai i pixel grezzi. Si usa una tecnica leggendaria chiamata **Eigenfaces** (che è sostanzialmente la PCA applicata alle facce).

**Il tuo progetto sarà:**

1. **Input:** Foto 64x64 pixel (4096 feature).
    
2. **Feature Extraction (PCA):** Riduciamo le 4096 feature a circa 150 "Componenti Principali" (Eigenfaces). Queste rappresentano le caratteristiche salienti (forma del viso, illuminazione dominante).
    
3. **Classificatori a Confronto:**
    
    - **SVM:** Lavora sulle 150 feature della PCA.
        
    - **k-NN:** Calcola la distanza Euclidea sulle 150 feature.
        
    - **Random Forest:** Cerca regole decisionali sulle feature.

### 5. Punti di Forza di questo progetto (da dire all'esame)

1. **Dimensionality Reduction (PCA):** Spiega che i volti hanno tantissimi pixel ridondanti. La PCA ti permette di dire: _"Professore, ho compresso l'informazione. Non classifico i pixel, classifico la struttura del volto."_
    
2. **Confronto Parametrico vs Non-Parametrico:**
    
    - **SVM (Parametrico):** Costruisce un modello matematico complesso dei confini tra le facce. Solitamente vince.
        
    - **k-NN (Non-Parametrico/Instance-based):** Non costruisce un modello, guarda solo chi è più simile in memoria. Funziona bene se hai poche facce, ma scala male.
        
3. **Visualizzazione delle Eigenfaces:** Quando mostri l'immagine delle "facce fantasma" generate dalla PCA (vedi codice sopra), dimostri di aver capito cosa succede dentro la "scatola nera".
    
