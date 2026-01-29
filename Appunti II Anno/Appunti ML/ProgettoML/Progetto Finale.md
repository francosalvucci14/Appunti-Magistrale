# PROGETTO MACHINE LEARNING: PHISING URL RECOGNITION

## Abstract: Rilevamento di URL di Phishing tramite Tecniche di Dimensionality Reduction e Apprendimento Supervisionato

Il presente studio analizza l'efficacia di diversi paradigmi di **Machine Learning** nella classificazione di URL malevoli, utilizzando il dataset ad alte prestazioni **Web Page Phishing Dataset**. 

La ricerca affronta la sfida della sicurezza informatica moderna attraverso un confronto sistematico tra modelli basati su iperpiani di separazione e architetture ensemble, operando su uno spazio vettoriale composto da **89 feature** estratte (caratteristiche lessicali, statistiche e comportamentali degli URL).

### Metodologia e Pre-processing

Data la complessità e la multidimensionalità del dataset, il workflow implementato non si limita all'addestramento diretto, ma prevede una fase critica di ottimizzazione del dato:

1. **Normalizzazione:** per garantire che l'ampiezza delle scale delle 89 feature non influenzi negativamente i gradienti dei modelli.
2. **Scaling** per garantire che tutte le feature convergano ad una Gaussiana Standard, ovvero $\mathcal N(0,1)$
3. **Principal Component Analysis (PCA):** utilizzata per ridurre la dimensionalità dello spazio delle feature, eliminando la ridondanza informativa e concentrando la varianza del dataset in un set ottimizzato di componenti principali.

### Classificatori a Confronto

Il task di classificazione binaria viene risolto attraverso due approcci algoritmici distinti:

* **Support Vector Machines (SVM):** esplorate nelle varianti con **Kernel Lineare**, **Polinomiale (Poly)** e **Radial Basis Function (RBF)**, per testare la capacità del modello di mappare i dati in spazi a dimensionalità superiore.
* **Metodi Ensemble:** implementati per massimizzare la robustezza predittiva tramite strategie di **Bagging** (**Random Forest**) e **Boosting** (**AdaBoost** e **Gradient Boosting**). 

Questi modelli sono stati scelti per la loro intrinseca capacità di gestire relazioni non lineari e per la resistenza all'overfitting rispetto ai singoli alberi di decisione.

## Baseline

Come Baseline, sono stati scelti due modelli:
1. **DummyClassifier** : la baseline più semplice fra tutte, questa darà sempre $0.5\%$ di accuracy
2. **LogisticRegression** : modello più semplice, ci servirà da base reale  
# Scaletta/Workflow

Il workflow è il seguente:
1) Analisi del dataset
2) Preprocessing del dataset
* Normalizzazione del dataset
* Scaling delle feature
* PCA Reduction
3) Implementazione dei modelli:
* Implementazione funzioni di appoggio
* Implementazione SVM con i vari Kernel
* Implementazione Ensamble Methods
4) Addestramento dei modelli, uno per uno
* Addestramento sia su dataset completo che su dataset PCA
5) Confronto finale

# Rimuovi o commenta la riga sotto
# %matplotlib inline 

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib as mpl
import seaborn as sns
from IPython.display import Image
import sklearn.preprocessing
import scipy.stats as stats  
import matplotlib.colors as mcolors
from matplotlib import cm
from sklearn.decomposition import PCA  
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, auc, accuracy_score, precision_recall_fscore_support
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.inspection import permutation_importance
import plotly.express as px  

print("Librerie caricate con successo!")
import matplotlib as mpl

plt.style.use('fivethirtyeight')

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12
plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['image.interpolation'] = 'none'
plt.rcParams['figure.figsize'] = (16, 8)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 8

colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd:goldenrod', 'xkcd:cadet blue', 
          'xkcd:scarlet']
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=colors) 
cmap_big = cm.get_cmap('Spectral', 512)
cmap = mcolors.ListedColormap(cmap_big(np.linspace(0.7, 0.95, 256)))
data = pd.read_csv('Dataset/web-page-phishing/dataset_phishing.csv')
data
data.shape
data.columns
## Analisi delle feature

Di seguito riportiamo una breve descrizione di ogni feature presente nel dataset

**osservazione**: non tutte le descrizioni erano presenti nel file del dataset, alcune di esse sono frutto di un mio ragionamento e pertanto potrebbero non essere corrette

### 1. Feature Strutturali dell'URL

Queste variabili analizzano la composizione testuale dell'indirizzo web.

* **url**: L'indirizzo URL completo analizzato.
* **length_url / length_hostname**: Lunghezza totale dell'URL e del solo nome dell'host.
* **ip**: Variabile binaria; indica se nell'URL è presente un indirizzo IP al posto del nome a dominio (spesso usato nel phishing).
* **nb_dots / nb_hyphens / nb_at / nb_qm / nb_and / nb_or / nb_eq / nb_underscore / nb_tilde / nb_percent / nb_slash / nb_star / nb_colon / nb_comma / nb_semicolumn / nb_dollar / nb_space**: Conteggio di caratteri speciali (punti, trattini, chiocciole, punti interrogativi, ecc.) presenti nell'URL.
* **nb_www / nb_com / nb_dslash**: Conteggio delle stringhe "www", ".com" e del doppio slash "//" all'interno del percorso.
* **http_in_path**: Presenza della stringa "http" all'interno del percorso dell'URL (tecnica per mascherare URL malevoli).
* **https_token**: Indica se il token "https" è presente nella parte dell'host (non nel protocollo).
* **ratio_digits_url / ratio_digits_host**: Rapporto tra caratteri numerici e lunghezza totale rispettivamente dell'URL e dell'host.
* **punycode**: Indica se l'URL utilizza la codifica Punycode per caratteri speciali (es. domini con accenti).
* **port**: Indica se nell'URL è specificata una porta non standard.

### 2. Feature del Dominio e Sottodomini

* **tld_in_path / tld_in_subdomain**: Presenza di un TLD (es. .com, .net) nel percorso o nel sottodominio.
* **abnormal_subdomain**: Indica se la struttura del sottodominio è anomala.
* **nb_subdomains**: Numero di sottodomini presenti.
* **prefix_suffix**: Presenza di trattini nel nome a dominio per separare prefissi o suffissi.
* **random_domain**: Indica se il dominio sembra generato casualmente.
* **shortening_service**: Indica se viene utilizzato un servizio di abbreviazione URL (es. bit.ly).

### 3. Feature Lessicali (Parole nell'URL)

* **length_words_raw**: Numero totale di parole identificate nell'URL.
* **shortest_words_raw / longest_words_raw**: Lunghezza della parola più corta e più lunga nell'intero URL.
* **shortest_word_host / longest_word_host**: Lunghezza della parola più corta e più lunga nell'host.
* **avg_words_raw / avg_word_host / avg_word_path**: Lunghezza media delle parole nell'URL, nell'host e nel percorso.
* **phish_hints**: Conteggio di parole tipicamente usate negli attacchi phishing (es. "login", "update", "secure").

### 4. Feature del Contenuto della Pagina (HTML/JS)

* **nb_hyperlinks**: Numero totale di link presenti nella pagina web.
* **ratio_intHyperlinks / ratio_extHyperlinks / ratio_nullHyperlinks**: Percentuale di link che puntano allo stesso dominio, a domini esterni o che sono vuoti/nulli.
* **nb_extCSS**: Numero di file CSS caricati da domini esterni.
* **ratio_intRedirection / ratio_extRedirection**: Rapporto di reindirizzamenti interni ed esterni.
* **login_form**: Presenza di form di inserimento credenziali (input di tipo password).
* **external_favicon**: Indica se la favicon (l'icona del sito) è caricata da un dominio esterno.
* **links_in_tags**: Percentuale di link presenti nei tag (meta, script, link) rispetto al totale.
* **submit_email**: Indica se il form invia i dati direttamente a una mail (tramite `mailto:`).
* **ratio_intMedia / ratio_extMedia**: Rapporto di file multimediali (immagini, video) interni ed esterni.
* **iframe / popup_window**: Presenza di tag iframe o script che generano finestre popup.
* **safe_anchor**: Percentuale di ancore (`<a>`) che puntano a URL sicuri o allo stesso dominio.
* **onmouseover / right_clic**: Presenza di script che intercettano il movimento del mouse o disabilitano il tasto destro.
* **empty_title / domain_in_title**: Indica se il titolo della pagina è vuoto o se contiene il nome a dominio.

### 5. Feature Esterne e di Reputazione

* **whois_registered_domain**: Indica se il dominio è regolarmente registrato nei database WHOIS.
* **domain_registration_length**: Durata (in giorni) della registrazione del dominio.
* **domain_age**: Età del dominio in giorni (i domini recenti sono più sospetti).
* **web_traffic**: Rilevanza del sito in base al traffico web (es. ranking Alexa).
* **dns_record**: Presenza di record DNS validi per il dominio.
* **google_index**: Indica se la pagina è indicizzata su Google.
* **page_rank**: Valore del PageRank del sito (misura dell'autorevolezza).

### Target

* **status**: La variabile da predire; indica se l'URL è **legitimate** (sicuro) o **phishing** (malevolo).
# con dataset dataset_phishing.csv

print('# URL leggittime:', len(data.loc[data['status']=='legitimate']))
print('# URL phising:', len(data.loc[data['status']=='phishing']))
print('Percentuale phising:', len(data.loc[data['status']=='phishing']) / (len(data.loc[data['status']=='legitimate']) + len(data.loc[data['status']=='phishing']))*100,'%')
print('Percentuale non phising:', len(data.loc[data['status']=='legitimate']) / (len(data.loc[data['status']=='legitimate']) + len(data.loc[data['status']=='phishing']))*100,'%')
# get all columns that have value != numeric
non_numeric_columns = data.select_dtypes(exclude=['number']).columns.tolist()
non_numeric_columns
numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
numeric_columns
# 1. Calcolo del conteggio dei valori non nulli per ogni colonna
# Questa operazione è molto veloce (O(n*m)) anche su 236k righe
presenza = data.notnull().sum().sort_values(ascending=True)

# 2. Setup del grafico
# Usiamo barh (orizzontale) perché con 54 feature i nomi sarebbero illeggibili in verticale
plt.figure(figsize=(16, 26)) 

# Colore Teal coerente con lo stile precedente
presenza.plot(kind='barh', color="#53868B", width=0.8)

# 3. Estetica e Annotazioni
plt.title("CONTEGGIO RECORD PRESENTI PER FEATURE", fontsize=15, fontweight='bold', pad=20)
plt.xlabel("Numero di record non nulli", fontsize=12, fontweight='bold')
plt.ylabel("Feature", fontsize=12, fontweight='bold')

# Aggiungiamo il valore numerico alla fine di ogni barra per precisione
for i, v in enumerate(presenza):
    plt.text(v + 1000, i - .25, str(v), color='black', fontweight='bold', fontsize=9)

# Limite asse X per dare respiro al testo (aggiungiamo un 10% di spazio)
plt.xlim(0, data.shape[0] * 1.15)

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
Come possiamo notare dal plot precedente, nel dataset scelto non ci sono valori mancanti di feature.

A questo punto, possiamo passare direttamente alla fase di **normalizzazione** e **riduzione** delle feature tramite **PCA**
# Normalizzazione

Prima di tutto notiamo che la feature `url` non serve nella trattazione del nostro problema, pertanto possiamo rimuoverla

Utilizziamo inoltre una tecnica di Labeling chiamata **LabelEnconder** di `scikit.learn`, che ci permette di trasformare la colonna **status** (che corrisponde alla nostra colonna dei target `y`) in tutti valori numerici `0/1`.

La mappatura della feature `status` avviene nel seguente modo:
- Lo status = `legitimate` viene mappato nel numero $0$
- Lo status = `phishing` viene mappato nel numero $1$
data.drop('url', axis=1, inplace=True)  # Rimuovi la colonna 'url' se non necessaria
non_numeric_columns.remove('url')
# gestiamo i valori vuoti
data['status'].fillna("NONE", inplace=True)
# inizializzamo l'encoder di sklearn
le = sklearn.preprocessing.LabelEncoder()
# fit + transform
data['status'] = le.fit_transform(data['status'])
data
## Analisi delle distribuzioni e differenze di scala nelle feature

Osservando più nel dettaglio il dataset, notiamo che alcune feature presentano una differenza di scala (fra i valori) parecchio elevata.

Ad esempio, la feature `web_traffic` presenta valori che vanno da $0$ a circa $10.000.000$

Se questa differenza di scala non verrà trattata, porterà ad una gestione non efficiace delle feature in fase di addestramento dei modelli, sopratutto delle versione di SVM (essendo il modello più sensibile ai valori numerici delle feature).

Infatti, se non avessimo trattato e gestito queste differenze di scala, avremmo rischiato che modelli come SVM trattasero queste tipologie di feature come feature "principali", ovvero avremmo rischiato che feature di questo tipo si "mangiassero" tutte le altre, andando così ad ottenere risultati inefficaci e incorretti.

Per tale motivo, la scelta è ricaduta nell'usare la `log-trasformazione` dei dati, per "schiacciare" i valori alti senza perdere informazioni importanti
# --- FASE 1: Analisi del problema (Differenza di Scala) ---
# Selezioniamo alcune feature per mostrare quanto sono diverse
plt.figure(figsize=(12, 5))
sns.boxplot(data=data[['web_traffic','domain_age','nb_dots']])
plt.title("Differenza di scala originale (Nota le magnitudo diverse)")
plt.show()
# --- FASE 2: Log-Transformation (Gestione Asimmetria) ---
# Poiché molte feature hanno outlier estremi, usiamo log(1+x) 
# per "schiacciare" i valori alti senza perdere l'informazione dello zero.
features = data.columns[:-1]
df_log = data.copy()
for col in features:
    df_log[col] = np.log1p(data[col]).clip(lower=0) # Calcola ln(1 + x), evitando scale di negativi
df_log
# --- FASE DI CORREZIONE (SISTEMATA) ---
# 1. Sostituiamo gli infiniti con NaN
df_log.replace([np.inf, -np.inf], np.nan, inplace=True)

# 2. Pulizia: Rimuoviamo le righe che contengono NaN in TUTTO il dataframe
# In questo modo 'features' e 'status' rimangono allineati
df_log.dropna(inplace=True)

df_log
# --- FASE DI TRAIN/TEST SPLIT ---
X = df_log.drop('status', axis=1)
y = df_log['status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"X_train.shape: {X_train.shape}")
print(f"y_train.shape: {y_train.shape}")
print(f"X_test.shape: {X_test.shape}")
print(f"y_test.shape: {y_test.shape}")
Analizziamo ora la matrice di correlazione, per identificare le feature troppo correlate fra loro e rimuoverle
def cor_matrix(X): #correlazione tra le features
    plt.figure(figsize=(20, 15))
    sns.heatmap(X.corr(), annot=True, annot_kws={"size": 6}, linewidths=.1, cmap='magma')
    plt.show()


def get_correlated_features(X,threshold=0.95):
    # Calcoliamo la matrice di correlazione
    corr_matrix = X.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    correlated_columns = [column for column in upper.columns if any(upper[column] > threshold)]
    if correlated_columns:
        print("Feature altamente correlate trovate:", correlated_columns)
        # Rimuoviamo una delle due feature altamente correlate
        X_filtered = X.drop(columns=correlated_columns)
        print("Feature rimosse:", correlated_columns)
        print("Nuova matrice di correlazione:")
        cor_matrix(X_filtered)
        return X_filtered
    else:
        print("Nessuna feature altamente correlata trovata.")
        return X

cor_matrix(X)

X_train = get_correlated_features(X_train)
X_test = X_test[X_train.columns] #Allineamento delle colonne del test set con il train set


X_train
# --- FASE 4: Visualizzazione del Risultato ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Confronto distribuzione prima e dopo su una feature critica
sns.histplot(data['web_traffic'], kde=True, ax=axes[0], color='red')
axes[0].set_title("Originale (Altamente asimmetrica)")

sns.histplot(df_log['web_traffic'], kde=True, ax=axes[1], color='green')
axes[1].set_title("Dopo Log-Trasformazione")

plt.tight_layout()
plt.show()
# Training & Evaluation

Dopo aver analizzato, normalizzato e diviso (train/test split) il nostro dataset originale, siamo pronti per addestrare i $3$ modelli descritti all'inizio di questo notebook.

Per ogni modello, faremo una duplice analisi (così da far vedere bene le differenze):
1) Addestramento e valutazione con dataset originale
2) Addestramento e valutazione su dataset ridotto tramite PCA

Alla fine, dopo aver addestratto tutti i modelli scelti, faremo proprio un confronto qualitativo fra essi, mettendo in luce caratteristiche come:
1) Tempi di addestramento
2) Precisione della predizione
3) F1-score
4) Precision e Recall
5) Deviazione standard ($\sigma$)

Al fine di evitare il più possibile situazioni critiche di overfitting, useremo la tecnica $K$-**fold Cross-validation**, con parametro $K=5$

Perchè questa tecnica?

1) Applicare questa tecnica garantisce la stabilità delle performance e la minimizzazione del bias dovuto alla selezione del training set.
2) Questo approccio divide il training set in $5$ sottogruppi (**fold**): ciclicamente, i vari modelli verranno addestrati su $4$ di essi e validati sul restante.
3) I risultati riportati rappresentano la media aritmetica delle prestazioni ottenute nelle $5$ iterazioni, fornendo una stima più affidabile delle capacità predittiva rispetto al singolo split statico.

Avendo quindi optato per la seguente strategia, eseguiremo **scaling** e **PCA** dentro ogni fold (usando la `Pipeline` di scikit.learn), in modo da evitare il più possibile "Data Leakage", ovvero "iniettare" dati nel validation set
# Definizioni di Precision, Recall e F1-Score

Abbiamo detto che valuteremo, oltre all'accuracy dei modelli, le metriche:
- Precision
- Recall
- F1-Score

Prima di definire rigorosamente le 3 metriche introdotte, definiamo il concetto di `Confusion Matrix` e come questo viene applicato nel calcolo di Precision, Recall e F1-Score

## Confusion Matrix

Sia $$\{(x_i,y_i)\}_{i=1}^{n}$$ il nostro dataset, con:
- $y_i\in\{0,1\}$ il target per l'elemento $i$-esimo del dataset
- $\hat{y}_i\in\{0,1\}$ il target **predetto** per l'elemento $i$-esimo del dataset

Definiamo la **Confusion Matrix** come la matrice
|       | $\hat{y}=0$ | $\hat{y}=1$ |
| ----- | ----------- | ----------- |
| $y=0$ | TN          | FP         |
| $y=1$ | FN         | TP          |

Dove:
- **TP** (True Positives): istanze di phishing correttamente classificate come tali (**Phishing bloccati**)
- **FP** (False Positives): istanze legittime classificate come di phishing (**Falso Allarme**)
- **FN** (False Negatives): istanze di phishing classificate come legittime (**Phishing mancati**)
- **TN** (True Negatives): istanze di siti legittimi correttamente classificate come tali (**Siti sicuri**)

## Precision

Definiamo la `Precision` come la frazione:
$$\boxed{\text{Precision}=\frac{TP}{TP+FP}}$$

Formalmente, la precision di una classe è la **probabilità** che un'istanza sia effettivamente positiva, sapendo che il classificatore l'ha predetta come positiva, ovvero:
$$\text{Precision}=Pr(y=1|\hat{y}=1)$$

## Recall

Definiamo la `Recall` come la frazione:
$$\boxed{\text{Recall}=\frac{TP}{TP+FN}}$$

Formalmente, la recall di una classe è la **probabilità** che il classificatore predica positivo, sapendo che l'istanza è effettivamente positiva, ovvero:
$$\text{Recall}=Pr(\hat{y}=1|y=1)$$

## F1-Score

Definiamo la `F1-Score` come la frazione:
$$\boxed{\text{F1-Score}=2\cdot\frac{\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}}}$$

Formalmente, la `F1-score` è la **media armonica** tra precision e recall, ed è massimo solo quando entrambe sono alte.
# Analisi decisionale del problema : Falsi Positivi o Falsi Negativi?

Classificazione binaria:

- Classe (1): URL di phishing
- Classe (0): URL legittimo

Errori possibili:

| Errore                  | Significato                              | Conseguenza reale        |
| ----------------------- | ---------------------------------------- | ------------------------ |
| **False Positive (FP)** | URL legittimo classificato come phishing | Blocco/alert inutile     |
| **False Negative (FN)** | URL phishing classificato come legittimo | Compromissione sicurezza |

**False Negative** (molto grave)

- L’utente clicca su un link malevolo
- Possibile:
    - furto credenziali
    - malware
    - compromissione account
    - danni economici
- Costo elevato e potenzialmente irreversibile

**False Positive** (fastidioso ma accettabile)

- L’utente vede un alert
- L’URL viene bloccato temporaneamente
- Può essere:
    - sbloccato manualmente
    - whitelistato
- Costo basso e reversibile

Data la trattazione del problema, quello che noi vogliamo che sia minimizzato è il numero di **Falsi Negativi**, di conseguenza, la metrica più importante fra tutte sarà la **Recall** della classe di Phishing

Di conseguenza, l'ordine corretto sarà

$$\boxed{\text{Recall}\gt\text{F1-score}\gt\text{Precision}}$$

**Recall**: sicurezza

**F1**: compromesso globale

**Precision**: usabilità

## Implementazioni funzioni di appoggio

In questa sezione, implementiamo alcune funzioni di appoggio che ci serviranno più avanti

Ad esempio, fra queste funzioni abbiamo quella per calcolare gli iperparametri ottimali del modello, in modo da ottenere la predizione migliore fra tutte
#versione pipelines
def iperparametri_ott_pipe(pipe, param_grid, X_train, y_train):
    inner_cv = StratifiedKFold(n_splits=5, shuffle=True,random_state=42)
    grid_search = GridSearchCV(pipe, param_grid, cv=inner_cv, return_train_score=True, n_jobs=-1,scoring='f1')
    grid_search.fit(X_train, y_train)
    # Estraiamo i risultati della Cross-Validation per tutte le combinazioni di parametri
    results = grid_search.cv_results_
    mean_train_scores = results['mean_train_score']  #media degli scores per il training
    mean_test_scores = results['mean_test_score']    #media degli scores per il test
    params = results['params']
    miglior_ext = grid_search.best_estimator_    #migliori parametri per lo stimatore considerato
    return mean_train_scores, mean_test_scores, params, miglior_ext
def evaluation(model, X, y):
    # Predizioni cross-validated (per CM, ROC, metriche aggregate)
    y_pred = cross_val_predict(model, X, y, cv=5)

    acc = accuracy_score(y, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y, y_pred, average='binary'
    )
    cfm = confusion_matrix(y, y_pred)

    # Accuracy per fold (per std corretta)
    acc_scores = cross_val_score(
        model, X, y, cv=5, scoring='accuracy'
    )

    std_dev = acc_scores.std()

    return cm, acc, precision, recall, f1, cfm, std_dev
# def evaluation_finale(model, X_train, y_train, X_test, y_test):
#     # Fit del modello sul training set
#     model.fit(X_train, y_train)
    
#     # Predizioni sul test set
#     y_pred = model.predict(X_test)

#     acc = accuracy_score(y_test, y_pred)
#     precision, recall, f1, _ = precision_recall_fscore_support(
#         y_test, y_pred, average='binary'
#     )
#     cfm = confusion_matrix(y_test, y_pred)

#     return cm, acc, precision, recall, f1, cfm

def evaluation_finale(model, X_test, y_test):
    
    # Predizioni sul test set
    y_pred = cross_val_predict(model, X_test, y_test, cv=5)

    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average='binary'
    )
    cfm = confusion_matrix(y_test, y_pred)

    return cm, acc, precision, recall, f1, cfm
#funzione che confronta graficamente gli scores del modello al variare dei suoi parametri
def plot_hyperp(mean_train_scores, mean_test_scores, params):
    edited_params = []  # Lista per salvare i parametri in formato leggibile

    for param_set in params:
        # Formatta i parametri come "param1: val1, param2: val2"
        param_str = ", ".join([f"{key.split('__')[-1]}: {param_set[key]}" for key in param_set])
        edited_params.append(param_str)  # Salva i parametri formattati

    lines = []
    for i in range(len(mean_train_scores)):
        lines.append({'param': i, 'score': mean_train_scores[i], 'set': 'train', 'hyperparams': edited_params[i]})
        lines.append({'param': i, 'score': mean_test_scores[i], 'set': 'val', 'hyperparams': edited_params[i]})

    df = pd.DataFrame(lines)

    fig = px.line(df, x='param', y='score', color='set', line_shape='vh', markers=True, 
                  hover_data={'param': False, 'hyperparams': True})  # Mostra solo i parametri al passaggio del mouse

    fig.update_traces(mode="markers+lines")
    fig.update_yaxes(range=[0.0, 1.05])
    fig.update_xaxes(title_text='', showticklabels=False)  # Rimuove etichette sull'asse X

    fig.show()
def plot_results(cm, acc, precision, recall, f1, cfm, std_dev):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cfm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix Training Set')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
    
    print(f'Accuracy: {acc:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    print(f'Standard Deviation: {std_dev:.4f}')
def plot_results_evaluation_finale(cm, acc, precision, recall, f1, cfm):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cfm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix Test Set')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
    
    print(f'Accuracy: {acc:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
def plot_svm_decision_boundary(clf, X, y, title):
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, h),
        np.arange(y_min, y_max, h)
    )

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.35, cmap=plt.cm.coolwarm)
    plt.scatter(
        X[:, 0], X[:, 1],
        c=y,
        cmap=plt.cm.coolwarm,
        edgecolors='k',
        s=40
    )
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(title)
    plt.tight_layout()
    plt.show()

## Appendice: Spiegazione StandardScaler di scikit.learn

Lo `StandardScaler` di scikit-learn implementa una trasformazione nota in statistica come **Standardizzazione** o **Z-score normalization**. 

### 1. Definizione Matematica

Lo `StandardScaler` agisce su ogni singola feature (colonna) del dataset in modo indipendente. Per ogni feature , il trasformatore calcola due parametri fondamentali durante la fase di `.fit()`:

1. **Media Campionaria ($\mu_j$):**

$$\mu_j​=\frac{1}{n}\sum_{i=1}^{n}​x_{ij}​$$

*Dove $n$ è il numero di campioni e $x_{ij}$ è il valore della feature $j$ per l'osservazione $i$.*

2. **Deviazione Standard Campionaria ($\sigma_j$):**

$$\sigma_j​=\sqrt{\frac{1}{n}\sum_{i=1}^{n}​(x_{ij}​−\mu_j​)^2​}$$

#### La Trasformazione (Z-score)

Durante la fase di `.transform()`, ogni valore  viene centrato e riscalato secondo la formula:

$$z_{ij}=\frac{x_{ij}-\mu_j}{\sigma_j}$$

**Proprietà Risultanti**

Dopo la trasformazione, la nuova distribuzione della feature $j$ (chiamiamola $Z$) avrà:

* **Media ($\mu$) = $0$**: I dati sono "centrati" nell'origine.
* **Varianza ($\sigma^2$) = $1$**: I dati hanno tutti la stessa dispersione (Unit Variance).

Ovvero $$Z\sim\mathcal N(0,1)$$

### 2. Perché usarla nel progetto?

Nel dataset abbiamo feature con unità di misura e ordini di grandezza totalmente diversi. 

Ad esempio:

* `web_traffic`: valori che possono arrivare a milioni.
* `nb_dots`: valori piccoli, solitamente tra 1 e 10.
* `domain_age`: valori in giorni (migliaia).

Senza `StandardScaler`, ci ritroveremo in situazioni poco piacevoli, che potrebbero portare ad un'addestramento sbagliato e di conseguenza una predizione sbagliata

#### A. Il predominio delle "Magnitudo" (Bias di Scala)

La **SVM** calcola distanze euclidee. 

Se una feature ha valori enormi (es. traffico web), essa dominerà il calcolo della distanza, rendendo le feature piccole (es. numero di punti nell'URL) praticamente invisibili al modello, anche se queste ultime sono più importanti per scovare il phishing. 

La standardizzazione "democratizza" le feature: tutte pesano allo stesso modo all'inizio del training.

#### B. Requisito Fondamentale per la PCA

Nella pipeline abbiamo inserito l'opzione di **PCA** per ridurre la dimensionalità. 

La PCA cerca le direzioni di massima varianza. 

Se non si standardizza, la PCA identificherà come "componente principale" semplicemente la feature con i numeri più grandi, poiché la varianza è sensibile alla scala.

### 3. Osservazione: Perché non il Min-Max Scaler?

Mentre il `MinMaxScaler` schiaccia i dati tra 0 e 1, lo `StandardScaler` è preferibile in questo caso perché:

1. **Gestione Outlier:** Il phishing ha spesso outlier estremi (es. URL lunghissimi). Lo `StandardScaler` non ha un limite massimo predefinito, quindi non "comprime" troppo gli outlier, permettendo al modello di riconoscerli come anomalie.
2. **Distribuzione Gaussiana:** Molti algoritmi (specialmente SVM) assumono implicitamente che i dati siano distribuiti in modo approssimativamente gaussiano e centrati sullo zero.
# Baseline - DummyClassifier & LinearRegression

Come `baseline` sono stati scelti due modelli:
1) `DummyClassifier` di scikit.learn: è un classificatore che qualunque dato vede lo classifica in una singola classe
2) `LogisticRegression` : regressione logistica, più solida

dc = DummyClassifier(strategy='most_frequent')

cm, acc, precision, recall, f1, cfm, std_dev = evaluation(dc, X_train, y_train)
plot_results(cm, acc, precision, recall, f1, cfm, std_dev)

cm, acc, precision, recall, f1, cfm = evaluation_finale(dc, X_test, y_test)
plot_results_evaluation_finale(cm, acc, precision, recall, f1, cfm)
pipe_lr = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("lr", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
param_grid = {"lr__C": [0.01, 0.1, 1, 10]}
mean_train_scores, mean_test_scores, params, best_lr = iperparametri_ott_pipe(
    pipe_lr, param_grid, X_train, y_train
)
print('C', best_lr.named_steps['lr'].C)
plot_hyperp(mean_train_scores, mean_test_scores, params)
cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr, std_dev_lr = evaluation(best_lr, X_train, y_train)
plot_results(cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr,std_dev_lr)

cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr = evaluation_finale(best_lr, X_test, y_test)
plot_results_evaluation_finale(cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr)
# Commmenti sui risultati della LogisticRegression
# SVM - Kernel Lineare, Poly, RBF
pipe_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('svm', SVC())
])

param_grid_svm = {
    'pca': [PCA(n_components=0.95),'passthrough'],
    'svm__kernel': ['linear','poly', 'rbf'],
    'svm__C': [0.01, 0.1, 1, 10, 100],
    'svm__gamma': ['scale',0.001,0.01,0.1,1]
}

mean_train_scores, mean_test_scores, params, best_svm = iperparametri_ott_pipe(pipe_svm, param_grid_svm, X_train, y_train)
plot_hyperp(mean_train_scores, mean_test_scores, params)

if best_svm.named_steps['pca'] == 'passthrough':
    clf  = best_svm.named_steps['svm']
    print("PCA: NO")
    print(f"Best pipeline\n\tKernel: {clf.kernel}\n\tC: {clf.C}")
    if clf.kernel != 'linear':
        print(f"\tGamma: {clf.gamma}\n")
else:
    print("PCA: SI")
    pca = best_svm.named_steps['pca']
    print(f"PCA components: {pca.n_components_}")
    print(f"Explained variance: {pca.explained_variance_ratio_.sum():.3f}")


Visualizzazione in 2D dei decision boundary dell'SVM
svm_best = best_svm.named_steps['svm']

pipe_vis = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2, random_state=42)),
    ('svm', SVC(
        kernel=svm_best.kernel,
        C=svm_best.C,
        gamma=svm_best.gamma
    ))
])

pipe_vis.fit(X_train, y_train)

X_test_2d = pipe_vis.named_steps['pca'].transform(
    pipe_vis.named_steps['scaler'].transform(X_test)
)
plot_svm_decision_boundary(
    pipe_vis.named_steps['svm'],
    X_test_2d,
    y_test,
    "SVM RBF — decision boundary (Pipeline-consistent PCA 2D)"
)

# Chiamata alla funzione di valutazione
cm , acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm, std_dev_svm = evaluation(best_svm, X_train, y_train)
plot_results(cm, acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm, std_dev_svm)

# valutazione sul test set
cm , acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm = evaluation_finale(best_svm, X_test, y_test)
plot_results_evaluation_finale(cm, acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm)
# Commmenti sui risultati della SVM

# Ensemble Methods - RandomForest, GradientBoosting

Un po di teoria su RandomForest e Gradient Boosting

Useremo RF per classificare, ma anche per selezionare le feature che hanno impattato più del dovuto sulla classificazione
pipe_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('rf', RandomForestClassifier(random_state=42))
])

param_grid_rf = {
    'pca': [PCA(n_components=0.95),'passthrough'],
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [None, 10, 15, 20],
    'rf__criterion': ['gini', 'entropy', 'log_loss']
}
mean_train_scores, mean_test_scores, params, best_rf = iperparametri_ott_pipe(pipe_rf, param_grid_rf, X_train, y_train)
plot_hyperp(mean_train_scores, mean_test_scores, params)

if best_rf.named_steps['pca'] == 'passthrough':
    clf  = best_rf.named_steps['rf']
    print("PCA: NO")
    print(f"Best pipeline\n\tn_estimators: {clf.n_estimators}\n\tmax_depth: {clf.max_depth}\n\tcriterion: {clf.criterion}\n")
else:
    print("PCA: SI")
    pca = best_rf.named_steps['pca']
    print(f"PCA components: {pca.n_components_}")
    print(f"Explained variance: {pca.explained_variance_ratio_.sum():.3f}")
# Chiamata alla funzione di valutazione
cm, acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf, std_dev_rf = evaluation(best_rf, X_train, y_train)
plot_results(cm, acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf, std_dev_rf)

# valutazione sul test set
cm , acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf = evaluation_finale(best_rf, X_test, y_test)
plot_results_evaluation_finale(cm, acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf)
# Commmenti sui risultati della RandomForest
# Analisi delle feature "importanti"

Grazie all'applicazione della RandomForest, siamo in grado di estrapolare le feature ritenute "importanti" ai fini della classificazione.

Quello che adesso andremo a fare è rimuovere dal dataset queste feature, e ri-addestrare nuovamente i modelli SVM.

La domanda a cui vogliamo rispondere è: 
$$\text{quanto queste feature fanno nella classificazione degli SVM? togliendole, otteniamo un calo drastico delle performance oppure no?}$$

Per poter fare ciò, calcoliamo la **permutation importance** sul training set
# Calcolo permutation importance sul training set
result = permutation_importance(
    best_rf,
    X_train,
    y_train,
    n_repeats=20,
    random_state=42,
    n_jobs=-1,
    scoring='accuracy'
)

perm_importances = pd.Series(
    result.importances_mean,
    index=X_train.columns
).sort_values(ascending=False)

perm_std = result.importances_std
# Mostriamo le feature più importanti

fig, ax = plt.subplots(figsize=(16, 6))

perm_importances.plot.bar(
    yerr=perm_std,
    ax=ax,
    capsize=3
)

ax.set_title("Permutation Feature Importance (Random Forest)")
ax.set_ylabel("Decrease in Accuracy")
ax.set_xlabel("Features")
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# Selezioniamo le feature con importanza positiva
selected_features = perm_importances[perm_importances > 0].index.tolist()

print(f"Numero feature originali: {X_train.shape[1]}")
print(f"Numero feature selezionate: {len(selected_features)}")
print("\nFeature selezionate:")
print(selected_features)

Quello subito sotto è la feature_importances usando MDI
# forest_importances = pd.Series(best_rf.named_steps['rf'].feature_importances_, index=X_train.columns)

# fig, ax = plt.subplots()
# forest_importances.plot.bar(yerr=std_dev, ax=ax)
# ax.set_title("Feature importances using MDI")
# ax.set_ylabel("Mean decrease in impurity")
# fig.tight_layout()
# # Salva le feature più importanti (ovvero quelle che superano una certa soglia) in un array per usi futuri
# feature_names = X_train.columns.tolist()
# important_features = forest_importances[forest_importances > 0.050].index.tolist()
# important_features
X_train_reduced = X_train.drop(columns=selected_features)
X_test_reduced  = X_test.drop(columns=selected_features)

X_train_reduced
# DA CAPIRE SE HA SENSO OPPURE NO

# """93 minuti cristo santo e ancora niente
# """

# pipe_svm_no_feature = Pipeline([
#     ('scaler', StandardScaler()),
#     ('pca', PCA(n_components=0.95)),
#     ('svm', SVC())
# ])

# param_grid_svm_no_feature = {
#     'pca': [PCA(n_components=0.95),'passthrough'],
#     'svm__kernel': ['linear','poly', 'rbf'],
#     'svm__C': [0.01, 0.1, 1, 10, 100],
#     'svm__gamma': ['scale', 0.001,0.01,0.1,1]
# }

# mean_train_scores, mean_test_scores, params, best_svm_no_feature = iperparametri_ott_pipe(pipe_svm_no_feature, param_grid_svm_no_feature, X_train_reduced, y_train)
# plot_hyperp(mean_train_scores, mean_test_scores, params)
# #print("best pipeline:", best_svm,best_svm.named_steps['svm'].kernel)
# if best_svm_no_feature.named_steps['pca'] == 'passthrough':
#     clf  = best_svm_no_feature.named_steps['svm']
#     print("PCA: NO")
#     print(f"Best pipeline\n\tKernel: {clf.kernel}\n\tC: {clf.C}")
#     if clf.kernel != 'linear':
#         print(f"\tGamma: {clf.gamma}\n")
    
# else:
#     print("PCA: SI")
#     pca = best_svm_no_feature.named_steps['pca']
#     print(f"PCA components: {pca.n_components_}")
#     print(f"Explained variance: {pca.explained_variance_ratio_.sum():.3f}")

best_svm.fit(X_train_reduced, y_train)

cm , acc_svm_reduced, precision_svm_reduced, recall_svm_reduced, f1_svm_reduced, cfm_svm_reduced = evaluation_finale(best_svm, X_test_reduced, y_test)
plot_results_evaluation_finale(cm, acc_svm_reduced, precision_svm_reduced, recall_svm_reduced, f1_svm_reduced, cfm_svm_reduced)
svm_best = best_svm.named_steps['svm']

pipe_vis = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2, random_state=42)),
    ('svm', SVC(
        kernel=svm_best.kernel,
        C=svm_best.C,
        gamma=svm_best.gamma
    ))
])

pipe_vis.fit(X_train_reduced, y_train)

X_test_2d = pipe_vis.named_steps['pca'].transform(
    pipe_vis.named_steps['scaler'].transform(X_test_reduced)
)
plot_svm_decision_boundary(
    pipe_vis.named_steps['svm'],
    X_test_2d,
    y_test,
    "SVM RBF — decision boundary (Pipeline-consistent PCA 2D) - feature removed"
)

# Plot dei risultati

Di seguito, il plot dei risultati sul TestSet di ogni modello provato
# # plot risultati finali - Metriche separate
# models = ['Logistic Regression', 'SVM', 'Random Forest','SVM Reduced Features']
# accuracies = [acc_lr, acc_svm, acc_rf, acc_svm_reduced]
# precisions = [precision_lr, precision_svm, precision_rf, precision_svm_reduced]
# recalls = [recall_lr, recall_svm, recall_rf, recall_svm_reduced]
# f1_scores = [f1_lr, f1_svm, f1_rf, f1_svm_reduced]

# fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# # Accuracy
# axes[0, 0].bar(models, accuracies, color='steelblue')
# axes[0, 0].set_title('Accuracy', fontweight='bold')
# axes[0, 0].set_ylim(0, 1)
# axes[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# # Precision
# axes[0, 1].bar(models, precisions, color='coral')
# axes[0, 1].set_title('Precision', fontweight='bold')
# axes[0, 1].set_ylim(0, 1)
# axes[0, 1].grid(axis='y', linestyle='--', alpha=0.7)

# # Recall
# axes[1, 0].bar(models, recalls, color='lightgreen')
# axes[1, 0].set_title('Recall', fontweight='bold')
# axes[1, 0].set_ylim(0, 1)
# axes[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# # F1 Score
# axes[1, 1].bar(models, f1_scores, color='mediumpurple')
# axes[1, 1].set_title('F1 Score', fontweight='bold')
# axes[1, 1].set_ylim(0, 1)
# axes[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

# for ax in axes.flat:
#     ax.set_xticklabels(models, rotation=45, ha='right')
#     ax.set_ylabel('Score')

# plt.tight_layout()
# plt.show()
models = ['Logistic Regression', 'SVM', 'Random Forest','SVM Reduced Features']
accuracies = [acc_lr, acc_svm, acc_rf, acc_svm_reduced]
precisions = [precision_lr, precision_svm, precision_rf, precision_svm_reduced]
recalls = [recall_lr, recall_svm, recall_rf, recall_svm_reduced]
f1_scores = [f1_lr, f1_svm, f1_rf, f1_svm_reduced]

metrics = {
    'Accuracy': accuracies,
    'Precision': precisions,
    'Recall': recalls,
    'F1 Score': f1_scores
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for ax, (metric_name, values) in zip(axes, metrics.items()):
    
    y_pos = np.arange(len(models))
    
    # Linee tratteggiate verso l'asse X
    for x, y in zip(values, y_pos):
        ax.hlines(y=y, xmin=0, xmax=x, linestyles='dashed', alpha=0.6)
    
    # Punti
    ax.plot(values, y_pos, 'o', markersize=8)
    
    # Assi e label
    ax.set_yticks(y_pos)
    ax.set_yticklabels(models)
    ax.set_xlim(0, 1)
    ax.set_xlabel(metric_name)
    ax.set_title(metric_name, fontweight='bold')
    
    ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Considerazioni Finali

Sebbene nel contesto del phishing detection l’obiettivo principale sia la massimizzazione della recall della classe phishing, i modelli sperimentati mostrano valori di precision e recall molto simili.

Ciò indica che il classificatore riesce a mantenere un’elevata capacità di individuazione degli URL malevoli senza introdurre un numero significativo di falsi positivi.
## Conclusioni

In questo progetto è stato affrontato il problema della **rilevazione automatica di URL di phishing** tramite tecniche di machine learning supervisionato, con l’obiettivo di confrontare diversi modelli di classificazione e valutarne l’efficacia su un dataset reale.

Come punto di partenza è stata utilizzata la **Regressione Logistica** come baseline, che ha già mostrato buone prestazioni, con valori delle metriche intorno a 0.94. Questo risultato indica che le feature estratte sono altamente informative e permettono una buona separazione tra URL legittimi e malevoli anche con modelli relativamente semplici.

L’analisi è stata poi estesa a modelli più complessi, in particolare **Support Vector Machine** e **Random Forest**, accompagnati da una procedura di ottimizzazione degli iperparametri tramite **cross-validation**. Tra questi, l’SVM con **kernel RBF** si è rivelata la soluzione più efficace, ottenendo sul test set valori di **Accuracy, Precision, Recall e F1-score prossimi a 0.95**. La scelta di un kernel non lineare risulta coerente con la struttura dei dati, che non appaiono linearmente separabili nello spazio delle feature originali.

Un aspetto fondamentale del lavoro è stato l’utilizzo di una **pipeline di preprocessing**, comprendente la standardizzazione delle feature tramite *StandardScaler* e, in alcuni esperimenti, la riduzione dimensionale con PCA. Questo approccio ha permesso di evitare fenomeni di *data leakage* e di garantire una valutazione corretta e robusta dei modelli, in particolare per quelli basati su distanze, come l’SVM.

Nel contesto della phishing detection, è stata posta particolare attenzione al ruolo delle metriche di valutazione. In questo tipo di applicazione, la **recall della classe phishing** riveste un’importanza centrale, poiché un falso negativo può avere conseguenze significative in termini di sicurezza. I risultati ottenuti mostrano tuttavia un buon equilibrio tra precision e recall, suggerendo che il modello riesce a individuare efficacemente gli URL malevoli senza generare un numero eccessivo di falsi positivi.

Infine, è stata condotta un’analisi sull’importanza delle feature mediante Random Forest, seguita da un esperimento di riaddestramento dell’SVM su un dataset modificato in cui le feature più rilevanti venivano rimosse.
I risultati mostrano un calo significativo delle prestazioni, in particolare della recall della classe phishing, che scende a valori intorno a 0.66.
Questo comportamento evidenzia come le feature individuate come più importanti contribuiscano in maniera sostanziale alla capacità del modello di individuare correttamente gli URL malevoli. La drastica riduzione della recall indica che, in assenza di tali variabili, il classificatore perde una parte significativa dell’informazione discriminante necessaria per il problema.
Tale risultato conferma la rilevanza delle feature selezionate e sottolinea come la feature selection debba essere utilizzata con cautela in contesti di sicurezza, dove la perdita di capacità di rilevazione dei casi positivi può avere conseguenze critiche.

Nel complesso, i risultati confermano che modelli non lineari, inseriti in pipeline di preprocessing adeguate, rappresentano una soluzione efficace e affidabile per il problema della rilevazione di URL di phishing, fornendo una solida base per eventuali sviluppi futuri.