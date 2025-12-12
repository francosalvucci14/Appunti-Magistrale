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

---
# Classificatore di Volti con PCA

### 1. Il "Problema" k-Means (e la soluzione)

Tu hai citato **SVM** e **k-Means**.

- **SVM** è un **Classificatore** (Supervisionato): Gli dai le foto con i nomi, lui impara a distinguere i nomi.
    
- **k-Means** è un algoritmo di **Clustering** (Non Supervisionato): Lui non conosce i nomi. Raggruppa solo le foto simili.
    

Come usarlo nel progetto?

Hai due strade per inserire k-Means nel confronto:

1. **L'alternativa corretta (k-NN):** Probabilmente intendevi **k-NN (k-Nearest Neighbors)**. Questo è un classificatore supervisionato ("Se assomigli ai miei 3 vicini che sono Brad Pitt, allora sei Brad Pitt"). Questo è perfetto da confrontare con SVM.
    
2. **L'approccio ibrido (Bag of Visual Words):** Usi k-Means per trovare dei "pattern ricorrenti" (es. un occhio, un naso) e poi usi questi cluster come feature per addestrare una SVM. (Più complesso, forse troppo per questo esame).
    

**Consiglio:** Confronta **SVM** contro **k-NN** e **Random Forest**. Usa k-Means solo se vuoi fare una sezione extra di "Analisi esplorativa non supervisionata" (es. "Vediamo se l'algoritmo raggruppa da solo le facce simili senza sapere i nomi").

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
        

---

### 4. Codice Python: SVM vs k-NN su Volti

Ecco lo scheletro pronto per il copia-incolla che implementa questa logica.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# 1. Caricamento Dataset Volti
print("Caricamento Olivetti Faces...")
faces_data = fetch_olivetti_faces(shuffle=True, random_state=42)
X = faces_data.data  # Le immagini appiattite
y = faces_data.target # Le etichette (ID della persona: 0, 1, ..., 39)
images = faces_data.images # Le immagini 64x64 per visualizzazione

# 2. Split Train/Test
# Usiamo stratify=y per assicurarci che ci siano foto di tutte le persone sia in train che in test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 3. Definizione della PCA (Eigenfaces)
# Riduciamo la complessità mantenendo il 95% dell'informazione (varianza)
pca = PCA(n_components=0.95, whiten=True, random_state=42)

# 4. Definizione dei Classificatori da confrontare
classifiers = {
    "SVM (RBF Kernel)": SVC(kernel='rbf', class_weight='balanced', C=10, gamma=0.01),
    "k-NN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

print(f"\n--- Inizio Confronto su {len(y)} immagini ---")

# 5. Loop di Training e Valutazione
results = {}
for name, clf in classifiers.items():
    # Pipeline: PCA -> (Scaler opzionale con PCA whiten=True) -> Classificatore
    # Nota: La PCA va fatta DENTRO la pipeline per evitare data leakage
    model = make_pipeline(pca, clf)
    
    # Training
    model.fit(X_train, y_train)
    
    # Test
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    
    print(f"\nModello: {name}")
    print(f"Accuracy: {acc:.2%}")
    # print(classification_report(y_test, y_pred)) # Scommenta per dettagli

# 6. Visualizzazione "Eigenfaces" (Bonus per l'esame)
# Mostriamo quali sono le "facce fantasma" che il computer vede
print("\nVisualizzazione delle prime Eigenfaces (Componenti Principali)...")
pca_fitted = model.named_steps['pca']
eigenfaces = pca_fitted.components_.reshape((pca_fitted.n_components_, 64, 64))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(eigenfaces[i], cmap='gray')
    plt.title(f"Eigenface {i+1}")
    plt.axis('off')
plt.show()

print("\nVincitore:", max(results, key=results.get))
```

### 5. Punti di Forza di questo progetto (da dire all'esame)

1. **Dimensionality Reduction (PCA):** Spiega che i volti hanno tantissimi pixel ridondanti. La PCA ti permette di dire: _"Professore, ho compresso l'informazione. Non classifico i pixel, classifico la struttura del volto."_
    
2. **Confronto Parametrico vs Non-Parametrico:**
    
    - **SVM (Parametrico):** Costruisce un modello matematico complesso dei confini tra le facce. Solitamente vince.
        
    - **k-NN (Non-Parametrico/Instance-based):** Non costruisce un modello, guarda solo chi è più simile in memoria. Funziona bene se hai poche facce, ma scala male.
        
3. **Visualizzazione delle Eigenfaces:** Quando mostri l'immagine delle "facce fantasma" generate dalla PCA (vedi codice sopra), dimostri di aver capito cosa succede dentro la "scatola nera".
    
## Parte 2

Esatto, il piano è solido. Hai una pipeline logica, teoricamente valida e perfetta per un esame di Magistrale perché dimostri di saper gestire il dato (non buttandolo a caso in una black box).

Ecco il riassunto definitivo della struttura del tuo progetto "chiavi in mano":

### 1. Il Dataset

- **Olivetti Faces:** 400 immagini, 40 persone. Ideale perché leggero e permette di vedere bene l'effetto della PCA.
    

### 2. Preprocessing & Feature Extraction (Il cuore teorico)

- **PCA (Eigenfaces):** Non usi i 4096 pixel grezzi. Riduci a circa 100-150 componenti (che spiegano il 95% della varianza).
    
- _Per l'esame:_ Preparati a mostrare le immagini delle "Eigenfaces" (le facce fantasma). È la parte visiva che colpisce di più.
    

### 3. I Tre Moschettieri (Confronto Modelli)

Confronterai tre paradigmi diversi di Machine Learning:

1. **SVM (Kernel RBF):** Approccio **Geometrico**. Cerca i margini ottimi. Probabilmente sarà il più accurato.
    
2. **k-NN:** Approccio **Basato sulla Memoria (Instance-based)**. Non "impara", ricorda. Buono come baseline.
    
3. **Random Forest:** Approccio **Ensemble/Logico**. Usa alberi decisionali. Utile per vedere se un approccio non geometrico funziona sui pixel/feature.
    

### 4. Metriche di Valutazione

Non limitarti all'**Accuracy**. Stampa per ognuno il `classification_report` per vedere:

- **Precision/Recall:** Il modello confonde spesso la persona A con la persona B?
    
- **Tempi di training:** SVM vs k-NN (k-NN è istantaneo in training ma lento in predizione, SVM il contrario).
