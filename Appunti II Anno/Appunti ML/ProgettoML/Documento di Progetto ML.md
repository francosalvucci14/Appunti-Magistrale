# DOCUMENTO DI PROGETTO: Classificatore e Riconoscitore di volti (classificazione multi-classe - Face Detection)

## 1. Obiettivo e Strategia

L'obiettivo è sviluppare un classificatore di immagini robusto evitando l'uso di Deep Learning (CNN), dimostrando padronanza delle tecniche di **Feature Engineering** e dei modelli di **Machine Learning tradizionali**.

## 2. Il Dataset: "Olivetti Faces" o simili

Olivetti Faces (già incluso in Scikit-Learn). già normalizzato

- **Cosa contiene:** 400 immagini.
- **Soggetti:** 40 persone diverse (10 foto per persona).
- **Vantaggio:** È leggero, pulito, in scala di grigi e perfetto per dimostrare PCA e SVM.

## 3. La Baseline: "Eigenfaces"

Nel riconoscimento facciale classico, non si usano quasi mai i pixel grezzi. Si usa una tecnica leggendaria chiamata **Eigenfaces** (che è sostanzialmente la PCA applicata alle facce).

**Struttura del progetto:**

1. **Input:** Foto 64x64 pixel (4096 feature).
    
2. **Feature Extraction (PCA):** Riduciamo le 4096 feature a circa 150 "Componenti Principali" (Eigenfaces). Queste rappresentano le caratteristiche salienti (forma del viso, illuminazione dominante).
    
3. **Classificatori a Confronto:**
    
    - **SVM:** Lavora sulle 150 feature della PCA.
        
    - **k-NN:** Calcola la distanza Euclidea sulle 150 feature.
        
    - **Random Forest:** Cerca regole decisionali sulle feature.

## 4. Teoria Sottostante: Ottimizzazione e Probabilità

Per l'esame teorico, ecco come collegare i concetti matematici ai modelli scelti.
### A. Discesa del Gradiente (Gradient Descent)

- **Dove si trova:** Le SVM classiche usano solutori analitici (SMO), non la discesa del gradiente standard.
    
- **Come integrarla:** Usare `SGDClassifier` di Scikit-Learn.
    
    - Impostando `loss='hinge'`, si ottiene una SVM lineare addestrata con **Discesa del Gradiente Stocastica (SGD)**.
        
    - Utile per confrontare la velocità di convergenza rispetto al solutore analitico.