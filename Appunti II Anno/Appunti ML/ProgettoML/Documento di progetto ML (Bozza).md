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

## 4. Teoria Sottostante: Ottimizzazione e Probabilità

Per l'esame teorico, ecco come collegare i concetti matematici ai modelli scelti.

### A. Discesa del Gradiente (Gradient Descent)

- **Dove si trova:** Le SVM classiche usano solutori analitici (SMO), non la discesa del gradiente standard.
    
- **Come integrarla:** Usare `SGDClassifier` di Scikit-Learn.
    
    - Impostando `loss='hinge'`, si ottiene una SVM lineare addestrata con **Discesa del Gradiente Stocastica (SGD)**.
        
    - Utile per confrontare la velocità di convergenza rispetto al solutore analitico.
        

### B. Verosimiglianza (Maximum Likelihood Estimation - MLE)

- **Dove si trova:** La Regressione Logistica basa il suo addestramento sulla massimizzazione della verosimiglianza (minimizzazione della Log-Loss).
    
- **Confronto:**
    
    - **SVM:** Approccio **Geometrico** (margini).
        
    - **Regressione Logistica:** Approccio **Probabilistico** (verosimiglianza).
        
    - Il confronto dimostra che per le immagini, l'approccio geometrico (SVM + Kernel) batte spesso quello probabilistico lineare.
        