
# PROGETTO MACHINE LEARNING: PHISING URL RECOGNITION

## Abstract: Rilevamento di URL di Phishing tramite Tecniche di Dimensionality Reduction e Apprendimento Supervisionato

Il presente studio analizza l'efficacia di diversi paradigmi di **Machine Learning** nella classificazione di URL malevoli, utilizzando il dataset ad alte prestazioni **Web Page Phishing Dataset**. 

La ricerca affronta la sfida della sicurezza informatica moderna attraverso un confronto sistematico tra modelli basati su iperpiani di separazione e architetture ensemble, operando su uno spazio vettoriale composto da **89 feature** estratte (caratteristiche lessicali, statistiche e comportamentali degli URL).

### Metodologia e Pre-processing

Data la complessità e la multidimensionalità del dataset, il workflow implementato non si limita all'addestramento diretto, ma prevede una fase critica di ottimizzazione del dato:

1. **Analidi della skewness e magnitudo delle feature:** per garantire che l'ampiezza delle scale delle 89 feature non influenzi negativamente i gradienti dei modelli.
2. **Scaling** per garantire che tutte le feature convergano ad una Gaussiana Standard, ovvero $\mathcal N(0,1)$

### Classificatori a Confronto

Il task di classificazione binaria viene risolto attraverso due approcci algoritmici distinti:

* **Support Vector Machines (SVM):** esplorate nelle varianti con **Kernel Lineare**, **Polinomiale (Poly)** e **Radial Basis Function (RBF)**, per testare la capacità del modello di mappare i dati in spazi a dimensionalità superiore.
* **Metodi Ensemble:** implementati per massimizzare la robustezza predittiva tramite strategie di **Bagging** (**Random Forest**) e **Boosting** (**AdaBoost** e **Gradient Boosting**). Questi modelli sono stati scelti per la loro intrinseca capacità di gestire relazioni non lineari e per la resistenza all'overfitting rispetto ai singoli alberi di decisione.

## Baseline

Come Baseline, sono stati scelti due modelli:
1. **DummyClassifier** : la baseline più semplice fra tutte
2. **LogisticRegression** : modello più semplice, ci servirà da base reale (farà anche da **strong baseline**) 

```python
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
from scipy.stats import skew
import matplotlib.colors as mcolors
from matplotlib import cm
from sklearn.decomposition import PCA  
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.inspection import permutation_importance
import plotly.express as px  

print("Librerie caricate con successo!")
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
data.head()
data.shape
data.columns
data.describe()
```
---
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
```python
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
tmp = data.isnull().sum().reset_index(name='missing_val')
tmp[tmp['missing_val']!= 0]
```
# Analisi delle distribuzioni delle feature

## Label Encoding Target

Prima di tutto notiamo che la feature `url` non serve nella trattazione del nostro problema, pertanto possiamo rimuoverla

Utilizziamo inoltre una tecnica di Labeling chiamata **LabelEnconder** di `scikit.learn`, che ci permette di trasformare la colonna **status** (che corrisponde alla nostra colonna dei target `y`) in tutti valori numerici `0/1`.

La mappatura della feature `status` avviene nel seguente modo:
- Lo status = `legitimate` viene mappato nel numero $0$
- Lo status = `phishing` viene mappato nel numero $1$

```python
data.drop('url', axis=1, inplace=True)  # Rimuovi la colonna 'url' se non necessaria
non_numeric_columns.remove('url')
# gestiamo i valori vuoti
data['status'].fillna("NONE", inplace=True)
# inizializzamo l'encoder di sklearn
le = sklearn.preprocessing.LabelEncoder()
# fit + transform
data['status'] = le.fit_transform(data['status'])
data
```
## Separazione delle feature

Andiamo ora ad analizzare le nostre feature, dividendole in due gruppi
- feature **numeriche**: feature che indicano misurazioni/conteggi; possono essere *continue* o *discrete*
- feature **categoriali**: feature che descrivono caratteristiche qualitative, etichette o gruppi non numerici; possono essere identificate con valori numerici, anche se non hanno un significato numerico intrinseco; possono essere dei flag booleani e indicati con $0/1$ nel dataset.

```python
"""
Separa le feature in numeriche e categoriali.

Args:
    df: Il dataframe da analizzare.
    target_col: Nome della colonna target.
    id_col: Nome della colonna identificativo (URL).
    threshold: Numero massimo di valori unici per considerare una feature come categoriale.
"""
# Escludiamo le colonne che non sono feature di input
features_df = data.drop(columns=['status'])

categorical_features = []
numerical_features = []

for col in features_df.columns:
    # Se la colonna è di tipo 'object' o ha pochi valori unici (es. flag 0/1), è categoriale
    if features_df[col].dtype == 'object' or features_df[col].nunique() <= 2:
        categorical_features.append(col)
    else:
        numerical_features.append(col)
        
print(len(categorical_features), "feature categoriali:", categorical_features)
print(len(numerical_features), "feature numeriche:", numerical_features)
Visualizziamo la distribuzione quindi delle feature numeriche in relazione allo status
df_distr =data.groupby('status')[numerical_features].mean().reset_index().T
df_distr.rename(columns={0:'legitimate',1:"phishing"}, inplace=True)

#plt.style.use('ggplot')
plt.rcParams['axes.facecolor']='w'
ax = df_distr[1:-3][['legitimate','phishing']].plot(kind='bar', title ="Distribution of Average values across Target", figsize=(12, 8), legend=True, fontsize=12)
ax.set_xlabel("Numerical Features", fontsize=14)
ax.set_ylabel("Average Values", fontsize=14)
#ax.set_ylim(0,500000)
plt.show()
```

Osservazioni
- Più grande è la feature `lenght_url`, più è probabile che la url in questione sia `Phishing`
- C'è una differenza molto elevata per la feature `nb_hyperlinks`. Più grande significa più probabile che sia `Legitimate`
- L'alto volume delle feature `links_in_tags` ,`safe_anchor` segnala che la URL sia più propensa vero lo status `Legitmate`
- Similmente alla feature `lenght_url`, più la feature `domain_registration_lenght` è elevata e più è probabile che il sito sia `Legitimate`
## Skewness & Magitudo delle feature

Analizziamo ora le differenze fra le varie feature.

Ci concentreremo per lo più su due fattori fondamentali, che sono:
- **skewness** delle feature
- **magnitudo** delle feature

### Skenwess : Definizione e Soluzione

La skewness di una feature ci indica quanto la distribuzione di quella feature ***si discosta*** da una distribuzione normale (la classica "campana" Gaussiana)

Possiamo identificare $3$ tipi di skewness nelle feature, che sono

| Tipo                    | Descrizione                                                                                                 | Relazione tra Media e Mediana |
|-------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------|
| Positiva (Right-skewed) | La "coda" della distribuzione è più lunga verso destra. La maggior parte dei dati è concentrata a sinistra. | Media > Mediana               |
| Zero (Symmetrical)      | La distribuzione è perfettamente simmetrica (come una Gaussiana).                                           | Media ≈ Mediana               |
| Negativa (Left-skewed)  | La "coda" è più lunga verso sinistra. La maggior parte dei dati è concentrata a destra.                     | Media < Mediana               |

Perchè questo fattore è fondamentale nella trattazione del nostro problema? 

Perchè molti modelli di Machine Learning, tra cui il modello **SVM** (scelto per la risoluzione del task), sono sensibili all'asimmetria delle feature; questo potrebbe portare a situazioni spiacevoli quali:
- **Distorsione del/dei modello/i**
- **Performance ridotte**
- **Instabilità**

Per tali ragioni, verrà eseguito un controllo/calcolo dell'asimmetria delle feature presenti nel dataset. A quelle feature che hanno skewness elevata verrà applicata la tecnica della **log-trasformazione** ($log1p$ di scikit.learn)

Questa tecnica permette di applicare il logaritmo naturale $\ln(x)$ ai valori di una feature; questo permette di:
- Ridurre la skewness positiva
- Stabilizza la varianza

Inoltre, dato che ci sono valori vicini allo zero, e altri che sono esattamente zero, si è optato per l'applicazione di $\log(1+x)$ piuttosto che $\log(x)$

### Magnitudo: Definizione e Soluzione

Il magnitudo di una feature indica la grandezza dei valori di quella feature (ovvero la scala di valori).

Perchè questo fattore è di fondamentale trattazione?

Perchè i modelli basati su **distanza** (come il kNN e/o SVM) o su **discesa del gradiente** (come Regressione Lineare e/o Reti Neurali), se addestrati su un dataset avente feature con magnitudo estremamente diversi, potrebbero portare a risultati molto spiacevoli.

Prendiamo come esempio il modello SVM: lui cerca di trovare l'iperpiano che **massimizza il margine** tra le classi.

Se prendiamo due feature $x_1$  (es. reddito) e $x_2$ (es. età) tali per cui $mag(x_1)\gt\gt mag(x_2)$, ($mag(x_i)=$magnitudo della feature $x_i$) allora la prima dominerà sulla seconda. L'algoritmo quindi "ignorerà" la seconda feature perchè, matematicamente, le sue variazioni sembrano irrilevanti rispetto a quelle del reddito

Per risolvere questo problema si è fatto uso della tecnica di **Standardizzazione (Z-Score Scaling)** di scikit.learn, che trasforma i dati in modo che abbiano **media=0** e **deviazione standard = 1**; cioè comprime i dati in modo che seguano una **distribuzione Gaussiana Standard** $\mathcal N(0,1)$

Vedere appendice [qui](#appendice-spiegazione-standardscaler-di-scikitlearn)
## Train/Test Split

Diviamo il dataset originale in:
- Training Set: insieme di valori del dataset originale che ci servirà per addestrare i nostri modelli
- Test Set: insieme di valori del dataset originale, separato dal training set, che ci servirà per valutare le prestazioni e le performance dei nostri modelli

Il test set rappresenta quindi "nuovi" dati per il modello, dati che lui $\textit{NON deve mai vedere}$ prima della fine dell'addestramento.

```python
# --- FASE DI TRAIN/TEST SPLIT ---
X = data.drop('status', axis=1)
y = data['status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"X_train.shape: {X_train.shape}")
print(f"y_train.shape: {y_train.shape}")
print(f"X_test.shape: {X_test.shape}")
print(f"y_test.shape: {y_test.shape}")
```
## Calcolo Skewness e Magnitudo

Calcoliamo quindi la skenwess e la magintudo delle feature.

Per quanto detto prima, prenderemo in considerazione le feature con skewness maggiore e ne fearemo la log trasformazione.

Poi applicheremo lo StandardScaler a tutte le feature.

Il tutto verrà eseguito tramite il processo `Pipeline` di scikit.learn, in modo da evitare il `Data Leakage` quando faremo la divisione con cross-validation.

```python
numeric_features = X.select_dtypes(include=np.number).columns.tolist()

skewness = X_train[numeric_features].apply(lambda x: skew(x.dropna()))

skew_threshold = 1.0

skewed_features = [
    col for col in skewness[skewness > skew_threshold].index.tolist()
    if X_train[col].min() >= 0
]

#skewed_features = skewness[skewness > skew_threshold].index.tolist()
non_skewed_features = [col for col in numeric_features if col not in skewed_features]

print("Feature con skew elevata:", skewed_features)
print("Feature senza skew elevata:", non_skewed_features)

# Selezioniamo alcune feature per mostrare quanto sono diverse

plt.figure(figsize=(12, 5))
sns.boxplot(data=data[['web_traffic','domain_registration_length','nb_hyperlinks']])
plt.title("Differenza di scala originale (Nota le magnitudo diverse)")
plt.show()
```
## Definizione preprocessor

Definiamo quindi il nostro preprocessor, da inserire in fase di Training all'interno della Pipeline (in modo da garantire che ogni operazione venga fatta correttamente all'interno dei fold, così evitiamo **Data Leakage**)

Il preprocessor avrà quindi la seguente forma:
- alle feature estreme verrà applicato log-trasformazione
- a tutte le feature verrà applicato lo StandardScaler (comprese le feature estreme)

Per implementarlo, applicheremo la funzione **ColumnTransformer**

Prima vediamo se le feature selezionate e messe in log\_features presentano valori negativi; se si, le togliamo dall'array log\_features e non ne facciamo la log-trasformazione (altrimenti faremmo il logaritmo di un valore negativo che porterebbe a valori -inf)

```python
log_transformer = FunctionTransformer(np.log1p, validate=False)

preprocessor = ColumnTransformer(
    transformers=[
        ("log", log_transformer, skewed_features),
        ("num", "passthrough", non_skewed_features)
    ]
)
```

# Training & Evaluation

Dopo aver analizzato e diviso (train/test split) il nostro dataset originale, siamo pronti per addestrare i $2$ modelli descritti all'inizio di questo notebook.

Per ogni modello, verrà applicata una Pipeline contenente:
1) Per SVM - Preprocessor + Scaler + PCA
2) Per RandomForest - Preprocessor

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

Di conseguenza, l'ordine che i nostri modelli dovranno rispettare sarà:

$$\boxed{\text{Recall}\gt\text{F1-score}\gt\text{Precision}}$$

**Recall**: sicurezza

**F1**: compromesso globale

**Precision**: usabilità

---
## Implementazioni funzioni di appoggio

In questa sezione, implementiamo alcune funzioni di appoggio che ci serviranno più avanti

Ad esempio, fra queste funzioni abbiamo quella per calcolare gli iperparametri ottimali del modello, in modo da ottenere la predizione migliore fra tutte

```python
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
    # -------- Evidenziazione migliore combinazione --------
    best_idx = np.argmax(mean_test_scores)

    fig.add_scatter(
        x=[best_idx],
        y=[mean_test_scores[best_idx]],
        mode='markers',
        marker=dict(
            size=18,
            color='blue',
            symbol='circle-open',
            line=dict(width=3, color='blue')
        ),
        name='Best hyperparams'
    )
    fig.show()
    
def plot_results(cm,model, acc, precision, recall, f1, cfm, std_dev):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cfm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix Training Set for model: {}'.format(model.__class__.__name__))
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
    
    print(f'Accuracy: {acc:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    print(f'Standard Deviation: {std_dev:.4f}')
    
def plot_results_evaluation_finale(cm,model, acc, precision, recall, f1, cfm):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cfm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix Test Set for model: {}'.format(model.__class__.__name__))
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
    
    print(f'Accuracy: {acc:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    
def plot_svm_decision_boundary(clf, X, y, title, n_points=300):
    """
    Visualizza il decision boundary della SVM in uno spazio 2D.
    
    Args:
        clf: Classificatore SVM già addestrato (su spazio 2D)
        X: Feature array 2D (n_samples, 2)
        y: Target labels
        title: Titolo del grafico
        n_points: Numero di punti per asse della griglia
    """
    
    # Range delle due componenti
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    # Griglia numericamente controllata
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, n_points),
        np.linspace(y_min, y_max, n_points)
    )

    # Predizione su griglia
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = clf.predict(grid)
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(10, 8))

    # Decision regions
    plt.contourf(
        xx, yy, Z,
        alpha=0.3,
        cmap=plt.cm.RdYlBu_r
    )

    # Punti reali
    scatter = plt.scatter(
        X[:, 0], X[:, 1],
        c=y,
        cmap=plt.cm.RdYlBu_r,
        edgecolors='black',
        s=50,
        linewidth=1,
        alpha=0.85
    )

    # Legenda
    handles, _ = scatter.legend_elements()
    plt.legend(
        handles,
        ['Legitimate (0)', 'Phishing (1)'],
        loc='upper right',
        fontsize=10
    )

    plt.xlabel("PC1", fontsize=12)
    plt.ylabel("PC2", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
```
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
---
# Baseline - DummyClassifier & LinearRegression

Come `baseline` sono stati scelti due modelli:
1) `DummyClassifier` di scikit.learn: è un classificatore che qualunque dato vede lo classifica in una singola classe
2) `LogisticRegression` : regressione logistica, più solida

```python
dc = DummyClassifier(strategy='most_frequent')

cm, acc, precision, recall, f1, cfm, std_dev = evaluation(dc, X_train, y_train)
plot_results(cm, dc, acc, precision, recall, f1, cfm, std_dev)

cm, acc, precision, recall, f1, cfm = evaluation_finale(dc, X_test, y_test)
plot_results_evaluation_finale(cm, dc, acc, precision, recall, f1, cfm)
```

```python
pipe_lr = Pipeline(
    [
        ('scaler', StandardScaler()),
        ("lr", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
param_grid = {"lr__C": [0.01, 0.1, 1.0, 10.0]}
mean_train_scores, mean_test_scores, params, best_lr = iperparametri_ott_pipe(
    pipe_lr, param_grid, X_train, y_train
)
print('C', best_lr.named_steps['lr'].C)
plot_hyperp(mean_train_scores, mean_test_scores, params)
cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr, std_dev_lr = evaluation(best_lr, X_train, y_train)
plot_results(cm, best_lr.named_steps['lr'],acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr,std_dev_lr)

cm, acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr = evaluation_finale(best_lr, X_test, y_test)
plot_results_evaluation_finale(cm,best_lr.named_steps['lr'], acc_lr, precision_lr, recall_lr, f1_lr, cfm_lr)
```
# Commmenti sui risultati della LogisticRegression

I risultati ottenuti dal classificatore di **Logistic Regression** forniscono un quadro solido e coerente delle prestazioni del modello, agendo come un'ottima baseline per il rilevamento di URL di phishing.

## 1. Capacità di Generalizzazione

Il modello presenta un'accuratezza sul **Training Set** del **94.82%** e sul **Test Set** del **94.02%**.

* Lo scarto ridotto (inferiore all'1%) tra le due fasi indica un'ottima **capacità di generalizzazione**.
* Si può escludere la presenza di *overfitting* significativo, confermando che il preprocessing (scaling e log-trasformazione) ha permesso al modello di apprendere pattern statistici reali e non rumore specifico dei dati.

## 2. Bilanciamento tra Precision e Recall

Uno degli aspetti più rilevanti è l'equilibrio quasi perfetto tra **Precision** (0.9401) e **Recall** (0.9401) sul test set.

* **Recall (Sicurezza):** Un valore del 94% indica che il modello identifica correttamente la stragrande maggioranza degli URL malevoli, riducendo i Falsi Negativi (phishing mancati).
* **Precision (Usabilità):** Il valore speculare garantisce che il tasso di Falsi Positivi sia contenuto, minimizzando i falsi allarmi per l'utente su siti legittimi.
* **F1-Score:** Il valore di **0.9401** sintetizza efficacemente l'ottimo compromesso raggiunto tra queste due metriche.

## 3. Stabilità e Affidabilità

La **Deviazione Standard** registrata durante la cross-validation è estremamente contenuta ($\sigma=0.0055$).

* Questo dato dimostra la **stabilità del modello**: le prestazioni non oscillano drasticamente al variare dei dati di addestramento, confermando che il classificatore è robusto e affidabile.

## 4. Considerazioni sulla Linearità del Problema

Il fatto che un modello lineare come la Logistic Regression raggiunga performance superiori al 94% suggerisce che lo spazio delle feature presenti una buona **separabilità lineare**.
Le 89 feature estratte contengono segnali discriminanti molto forti. Questo risultato pone una sfida interessante per i modelli successivi (SVM non lineari e Random Forest): l'obiettivo sarà verificare se architetture più complesse riescano a catturare relazioni non lineari residue per migliorare ulteriormente questo già ottimo punteggio di partenza.

---
# SVM - Kernel Lineare, Poly, RBF

Il classificatore **Support Vector Machine** è un modello di apprendimento supervisionato basato sulla ricerca dell'iperpiano di separazione ottimo in uno spazio vettoriale ad alta dimensionalità.

## 1. Formulazione Matematica (Caso Lineare)

Sia dato un dataset di addestramento $\mathcal T=\{(\mathbf{x}_i,y_i)\}_{i=1}^n$ , dove $\mathbf{x}_i\in\mathbb R^d$ rappresenta il vettore delle feature e $y_i\in\{-1,1\}$ è l'etichetta di classe. L'obiettivo della SVM è individuare un iperpiano definito dall'equazione:
$$\mathbf w^T\mathbf x+b=0$$

che separi le classi massimizzando il **margine** geometrico, ovvero la distanza tra l'iperpiano e i punti più vicini di ogni classe (i vettori di supporto).

Il problema di ottimizzazione per una SVM a margine "soffice" (*Soft-Margin SVM*) è formulato come segue:
$$\min_{\mathbf w,b,\xi}\frac{1}{2}||\mathbf w||^2+C\sum_{i=1}^n\xi_i$$

soggetto ai vincoli:
$$y_i(\mathbf w^T\mathbf x+b)\geq1-\xi_i,\quad\xi_i\geq0$$

Dove:

* $\frac{2}{||\mathbf w||}$ rappresenta l'ampiezza del margine.
* $\xi_i$ sono le **variabili di slack** che permettono la classificazione errata di alcuni punti per gestire dati non perfettamente separabili (rumore).
* $C\gt0$ è il parametro di regolarizzazione che controlla il trade-off tra la massimizzazione del margine e la minimizzazione dell'errore di addestramento.

## 2. Rappresentazione Duale e Kernel Trick

Attraverso l'uso dei moltiplicatori di Lagrange $\alpha_i$, il problema può essere espresso nella sua **forma duale**, che dipende esclusivamente dal prodotto scalare tra i vettori di input:
$$\max_\alpha\sum_{i=1}^n\alpha_i-\frac{1}{2}\sum_{i,j=1}^n\alpha_i\alpha_jy_iy_j(\mathbf{x}_i^T\mathbf x_j)$$

Questa formulazione permette l'applicazione del **Kernel Trick**. Se i dati non sono linearmente separabili nello spazio originale, vengono mappati in uno spazio di Hilbert ad alta dimensionalità $\mathcal H$ tramite una funzione non lineare $\phi(\mathbf x)$. Il prodotto scalare $\phi(\mathbf x_i)^T\phi(\mathbf x_j)$ viene sostituito da una funzione **Kernel** $\mathcal K(\mathbf x_i,\mathbf x_j)$:
$$\mathcal K(\mathbf x_i,\mathbf x_j)=\phi(\mathbf x_i)^T\phi(\mathbf x_j)$$

## 3. Tipologie di Kernel

La scelta della funzione Kernel determina la geometria del confine di decisione (*decision boundary*). Le principali funzioni utilizzate sono:

### A. Kernel Lineare

Utilizzato quando i dati sono già linearmente separabili nello spazio delle feature originale.
$$\mathcal K(\mathbf x,\mathbf z)=\mathbf x^T\mathbf z$$

### B. Kernel Polinomiale

Permette di modellare interazioni tra feature fino al grado $d$.
$$\mathcal K(\mathbf x,\mathbf z)=(\gamma\mathbf x^T\mathbf z+r)^d$$

### C. Radial Basis Function (RBF / Gaussiano)

È il kernel più diffuso e potente per gestire relazioni non lineari complesse. Mappa i dati in uno spazio a dimensionalità infinita.
$$\mathcal K(\mathbf x,\mathbf z)=\exp(-\gamma||\mathbf x-\mathbf z||^2)$$


Il parametro $\gamma$ controlla l'ampiezza della campana gaussiana: valori elevati portano a un adattamento molto stretto ai dati (rischio overfitting).

```python
pipe_svm = Pipeline([
    ('preprocessor',preprocessor),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('svm', SVC())
])

param_grid_svm = {
    'pca': [PCA(n_components=0.95),'passthrough'],
    'svm__kernel': ['linear','poly', 'rbf'],
    'svm__C': [0.01, 0.1, 1.0,10.0],
    'svm__gamma': ['scale',0.001,0.01,0.1],
    'svm__class_weight': [None,'balanced']
}

mean_train_scores, mean_test_scores, params, best_svm = iperparametri_ott_pipe(pipe_svm, param_grid_svm, X_train, y_train)
plot_hyperp(mean_train_scores, mean_test_scores, params)

if best_svm.named_steps['pca'] == 'passthrough':
    clf  = best_svm.named_steps['svm']
    print("PCA: passthrough")
    print(f"Best pipeline\n\tKernel: {clf.kernel}\n\tC: {clf.C}\n\tClass weight: {clf.class_weight}")
    if clf.kernel != 'linear':
        print(f"\tGamma: {clf.gamma}\n")
else:
    print("PCA: 0.95 variance")
    pca = best_svm.named_steps['pca']
    print(f"PCA components: {pca.n_components_}")
    print(f"Explained variance: {pca.explained_variance_ratio_.sum():.3f}")
```

Visualizzazione in 2D dei decision boundary dell'SVM

```python
svm_best = best_svm.named_steps['svm']

pipe_vis = Pipeline([
    ('preprocessor', preprocessor),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2, random_state=42)),
    ('svm', SVC(
        kernel=svm_best.kernel,
        C=svm_best.C,
        gamma=svm_best.gamma
    ))
])

pipe_vis.fit(X_train, y_train)

# X_test_2d = pipe_vis[:-1].named_steps['pca'].transform(
#     pipe_vis.named_steps['scaler'].transform(X_test)
# )
X_test_2d = pipe_vis.named_steps['preprocessor'].transform(X_test)
X_test_2d = pipe_vis.named_steps['scaler'].transform(X_test_2d)
X_test_2d = pipe_vis.named_steps['pca'].transform(X_test_2d)

plot_svm_decision_boundary(
    pipe_vis.named_steps['svm'],
    X_test_2d,
    y_test,
    "SVM RBF — decision boundary (Pipeline-consistent PCA 2D)"
)
```

Valutazione SVM

```python
# Chiamata alla funzione di valutazione
cm , acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm, std_dev_svm = evaluation(best_svm, X_train, y_train)
plot_results(cm,best_svm.named_steps['svm'], acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm, std_dev_svm)

# valutazione sul test set
cm , acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm = evaluation_finale(best_svm, X_test, y_test)
plot_results_evaluation_finale(cm, best_svm.named_steps['svm'], acc_svm, precision_svm, recall_svm, f1_svm, cfm_svm)
```
# Commmenti sui risultati della SVM

L'implementazione del modello Support Vector Machine (SVM) mostra un incremento prestazionale rispetto alla baseline lineare, confermando l'efficacia del mapping dei dati in spazi a dimensionalità superiore.

## 1. Capacità di Generalizzazione

Il modello presenta un'accuratezza sul **Training Set** del 96.32% e sul **Test Set** del 95.30%.
- Lo scarto ridotto (circa l'1%) tra le due fasi indica un'ottima capacità di generalizzazione.
- Nonostante l'aumento della complessità del modello rispetto alla Logistic Regression, si può escludere la presenza di overfitting, validando la scelta degli iperparametri effettuata in fase di tuning.

## 2. Bilanciamento tra Precision e Recall

Le metriche sul test set mostrano un bilanciamento eccellente tra **Precision** (0.9541) e **Recall** (0.9516).
- **Recall (Sicurezza)**: Un valore del 95.16% indica che il modello SVM è estremamente efficace nel rilevare gli URL di phishing, riducendo ulteriormente il rischio di "Phishing mancati" rispetto alla baseline.
- **Precision (Usabilità)**: Il valore di 0.9541 garantisce che il tasso di "Falsi Allarmi" rimanga molto basso, preservando l'esperienza d'uso dell'utente.
- **F1-Score**: Il valore di 0.9528 riflette un classificatore molto robusto, capace di gestire con successo il trade-off tra sensibilità e precisione.

## 3. Stabilità e Affidabilità

La Deviazione Standard registrata durante la cross-validation è estremamente contenuta ($\sigma=0.0021$).
- Questo dato è particolarmente significativo: l'SVM risulta ancora più stabile della Logistic Regression ($\sigma=0.0055$). Le performance rimangono quasi invariate attraverso i diversi fold, a dimostrazione di una configurazione degli iperpiani di separazione molto solida.

## 4. Considerazioni sull'apporto della Non-Linearità

Il superamento della soglia del 95% di accuratezza conferma che il problema del phishing non è puramente lineare. L'utilizzo di un kernel (come quello RBF o Polinomiale) ha permesso alla SVM di catturare relazioni complesse tra le 89 feature che sfuggivano alla regressione logistica. Questo incremento di performance giustifica il maggior costo computazionale richiesto per l'addestramento di questo modello.

---
# Ensemble Methods - RandomForest, GradientBoosting

Il **Random Forest** è un algoritmo di apprendimento supervisionato basato su un paradigma di **Ensemble Learning** chiamato **Bagging** (Bootstrap Aggregating). Il modello consiste in una vasta collezione (foresta) di alberi di decisione non correlati, i cui risultati vengono aggregati per fornire una predizione robusta.

## 1. Architettura Ensemble: Bagging e Feature Randomness

L'obiettivo del Random Forest è ridurre la varianza del modello senza aumentarne il bias. Questo viene ottenuto attraverso due meccanismi principali:

### A. Bootstrap Aggregating (Bagging)

Dato un dataset di addestramento $\mathcal T$ di dimensione $n$, il modello genera $\mathcal B$ nuovi set di dati $\mathcal T_b$ (campioni bootstrap) selezionando $n$ osservazioni da $\mathcal T$ con reinserimento (*replacement*).
Per ogni campione $b=1,\dots,\mathcal B$, viene addestrato un albero di decisione $T_b$.

### B. Feature Randomness (Metodo dei Sottospazi Casuali)

A differenza dei normali alberi di decisione, durante la costruzione di ogni nodo di ogni albero, l'algoritmo non cerca la migliore feature tra tutte le $d$ variabili disponibili. Al contrario, seleziona un sottoinsieme casuale di feature di dimensione $m$ (tipicamente $m\approx\sqrt{d}$ per la classificazione).

Il criterio di split viene quindi calcolato solo su questo sottoinsieme:
$$\text{Best Split}=arg\max_{j\in\{1,\dots,m\}}\Delta I(j,s)$$

## 2. Criteri di Suddivisione (Split)

Per ogni nodo, l'albero cerca di massimizzare la "purezza" dei nodi figli. I due criteri più comuni per misurare l'impurità in un task di classificazione binaria ($y\in\{0,1\}$) sono:

1. **Indice di Gini (Gini Impurity):**
$$G=1-\sum_{i\in\{0,1\}}p_i^2$$

2. **Entropia (Information Gain):**
$$H=-\sum_{i\in\{0,1\}}p_i\log_2(p_i)$$


Dove  rappresenta la frazione di campioni appartenenti alla classe  nel nodo corrente. Lo split ottimale è quello che massimizza la riduzione dell'impurità (Information Gain).

## 3. Aggregazione Finale

Una volta addestrati tutti i  alberi, la predizione finale per un nuovo input  viene ottenuta tramite **voto di maggioranza** (Majority Voting):
$$\hat{y}=\text{vote}\{T_1(\mathbf x),T_2(\mathbf x),\dots,T_\mathcal B(\mathbf x)\}$$

Useremo RF per classificare, ma anche per selezionare le feature che hanno impattato più del dovuto sulla classificazione

```python
pipe_rf = Pipeline([
    ('rf', RandomForestClassifier(random_state=42))
])

param_grid_rf = {
    'rf__n_estimators': [50, 100, 200,500],
    'rf__max_depth': [None, 10, 15, 20,50],
    'rf__criterion': ['gini', 'entropy', 'log_loss']
}
mean_train_scores, mean_test_scores, params, best_rf = iperparametri_ott_pipe(pipe_rf, param_grid_rf, X_train, y_train)
plot_hyperp(mean_train_scores, mean_test_scores, params)

clf  = best_rf.named_steps['rf']
print("PCA: NO")
print(f"Best pipeline\n\tn_estimators: {clf.n_estimators}\n\tmax_depth: {clf.max_depth}\n\tcriterion: {clf.criterion}\n")
```

Valutazione RandomForest

```python
# Chiamata alla funzione di valutazione
cm, acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf, std_dev_rf = evaluation(best_rf, X_train, y_train)
plot_results(cm,best_rf.named_steps['rf'], acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf, std_dev_rf)

# valutazione sul test set
cm , acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf = evaluation_finale(best_rf, X_test, y_test)
plot_results_evaluation_finale(cm, best_rf.named_steps['rf'], acc_rf, precision_rf, recall_rf, f1_rf, cfm_rf)
```

RandomForest con log-trasformazione

```python
pipe_rf_log = Pipeline([
    ('preprocessor',preprocessor),
    ('rf', RandomForestClassifier(random_state=42))
])

param_grid_rf_log = {
    'rf__n_estimators': [50, 100, 200,500],
    'rf__max_depth': [None, 10, 15, 20,50],
    'rf__criterion': ['gini', 'entropy', 'log_loss']
}
mean_train_scores, mean_test_scores, params, best_rf_log = iperparametri_ott_pipe(pipe_rf_log, param_grid_rf_log, X_train, y_train)
plot_hyperp(mean_train_scores, mean_test_scores, params)

clf  = best_rf_log.named_steps['rf']
print("PCA: NO")
print(f"Best pipeline\n\tn_estimators: {clf.n_estimators}\n\tmax_depth: {clf.max_depth}\n\tcriterion: {clf.criterion}\n")
```

Valutazione RandomForest con log-transformazione

```python
# Chiamata alla funzione di valutazione
cm, acc_rf_log, precision_rf_log, recall_rf_log, f1_rf_log, cfm_rf_log, std_dev_rf_log = evaluation(best_rf_log, X_train, y_train)
plot_results(cm,best_rf_log.named_steps['rf'], acc_rf_log, precision_rf_log, recall_rf_log, f1_rf_log, cfm_rf_log, std_dev_rf_log)

# valutazione sul test set
cm , acc_rf_log, precision_rf_log, recall_rf_log, f1_rf_log, cfm_rf_log = evaluation_finale(best_rf_log, X_test, y_test)
plot_results_evaluation_finale(cm, best_rf_log.named_steps['rf'], acc_rf_log, precision_rf_log, recall_rf_log, f1_rf_log, cfm_rf_log)
best_rf_model = best_rf_log.named_steps['rf'] if acc_rf_log > acc_rf else best_rf.named_steps['rf']

print("Miglior modello Random Forest:", "RandomForest con log transform" if acc_rf_log > acc_rf else "RandomForest senza log transform")
```
# Commmenti sui risultati della RandomForest

I risultati ottenuti mostrano un modello estremamente bilanciato e performante, capace di superare la semplicità dei modelli lineari e di offrire una protezione di alto livello contro gli URL di phishing.

## 1. Eccellente Capacità di Generalizzazione

Il modello presenta un'accuratezza sul **Training Set** del **96.67%** e sul **Test Set** del **95.30%**.

* **Analisi dello scarto:** La differenza tra le due fasi è di circa l'**1.3%**. Questo valore è ideale: indica che il modello ha "imparato" bene le caratteristiche distintive dei siti malevoli senza cadere nella trappola della memorizzazione (overfitting).
* **Affidabilità:** Il modello si comporta in modo coerente sia sui dati noti che su quelli nuovi, garantendo che le performance dichiarate siano mantenute anche in scenari reali.

## 2. Analisi della Sicurezza e dell'Usabilità (Precision vs Recall)

Le metriche sul test set evidenziano un equilibrio quasi perfetto tra la capacità di rilevamento e la riduzione dei falsi allarmi.

* **Recall (Sicurezza):** Con un valore del **95.16%**, il modello garantisce che la stragrande maggioranza degli attacchi venga bloccata. In un contesto di cybersecurity, minimizzare i Falsi Negativi (phishing non rilevato) è la priorità assoluta per proteggere l'integrità dei dati degli utenti.
* **Precision (Usabilità):** Il valore di **0.9541** assicura che il sistema non sia troppo "aggressivo", evitando di segnalare come pericolosi i siti legittimi. Questo equilibrio è fondamentale per evitare che l'utente, infastidito dai falsi allarmi, inizi a ignorare le segnalazioni di sicurezza.
* **F1-Score:** Il valore di **0.9528** è una prova matematica della solidità del classificatore nel gestire il trade-off tra queste due necessità contrapposte.

## 3. Stabilità nelle Prestazioni

La **Deviazione Standard** registrata durante la cross-validation è molto bassa ($\sigma=0.0035$).

* Questo indica che il modello è **molto stabile**: le sue performance non variano in modo significativo a seconda di quali dati vengono usati per l'addestramento. È un segno di un processo di apprendimento robusto e di un dataset ben preprocessato.

### 4. Conclusioni sull'efficacia del modello

Il raggiungimento della soglia del **95%** su tutte le metriche principali nel test set posiziona questo modello tra i migliori candidati per l'implementazione in un sistema reale. La capacità di catturare le sottili relazioni non lineari tra le 89 feature (grazie probabilmente a un approccio basato su alberi o kernel complessi) permette di ottenere una barriera difensiva estremamente affidabile e precisa.

---
# Analisi delle feature "importanti"

Dopo aver identificato le feature più rilevanti attraverso la **Random Forest**, è fondamentale validare quanto queste variabili siano determinanti per la capacità predittiva di altri modelli, come la **SVM**. Per fare ciò, utilizzeremo una tecnica di valutazione robusta chiamata **Permutation Importance**.

## Cos'è la Permutation Importance?

La **Permutation Importance** è un metodo model-agnostic per misurare l'importanza di una feature calcolando l'aumento dell'errore di previsione del modello dopo che i valori di quella specifica feature sono stati permutati casualmente.

### Il meccanismo logico

Il concetto alla base è semplice ma potente:

1. Se una feature è **importante**, permutare casualmente i suoi valori (mantenendo costanti gli altri) distrugge la relazione esistente tra quella variabile e il target. Di conseguenza, il punteggio del modello (**Accuracy**, **F1-score**, ecc.) subirà un **calo drastico**.
2. Se una feature è **irrilevante** (rumore), la sua permutazione non influenzerà significativamente le previsioni del modello, e il punteggio rimarrà pressoché invariato.

### Vantaggi rispetto alla Feature Importance standard

A differenza della "Gini Importance" utilizzata nativamente dalle Random Forest (che può essere influenzata dalla cardinalità delle variabili), la Permutation Importance:

* È calcolata sul **Validation/Test set** (o tramite cross-validation), riflettendo la capacità di generalizzazione.
* Non è legata alla struttura interna del modello, permettendo confronti equi tra SVM, modelli lineari e alberi.

## L'Esperimento: Stress-test degli SVM

L'obiettivo di questa fase è condurre uno "stress-test" sui modelli SVM per capire la loro dipendenza dalle feature identificate come dominanti.

### La domanda di ricerca

Vogliamo rispondere rigorosamente al seguente quesito:

> *"Qual è il contributo marginale delle feature top-ranked nella classificazione SVM? Rimuovendole dal dataset, il modello è ancora in grado di discriminare il phishing o subisce un collasso delle prestazioni?"*

### Workflow operativo

1. **Calcolo:** Eseguiamo la Permutation Importance sul training set per identificare le variabili chiave per l'SVM.
2. **Rimozione:** Escludiamo dal dataset le feature che hanno ottenuto il punteggio di importanza più elevato.
3. **Rivalutazione:** Riaffiniamo e testiamo nuovamente i modelli SVM sullo spazio delle feature ridotto.

Questo processo ci permetterà di distinguere tra feature che offrono un contributo informativo unico e feature che, se rimosse, possono essere compensate da altre variabili correlate presenti nel dataset.

```python
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
```

```python
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
```

```python
# Selezioniamo le feature con importanza positiva
selected_features = perm_importances[perm_importances > 0].index.tolist()

print(f"Numero feature originali: {X_train.shape[1]}")
print(f"Numero feature selezionate: {len(selected_features)}")
print("\nFeature selezionate:")
print(selected_features)

X_train_reduced = X_train.drop(columns=selected_features) # TrainSet senza feature importanti
X_test_reduced  = X_test.drop(columns=selected_features)
X_train_reduced
numeric_features = X_train_reduced.select_dtypes(include=np.number).columns.tolist()

skewness = X_train_reduced[numeric_features].apply(lambda x: skew(x.dropna()))

skew_threshold = 1.0

skewed_features = [
    col for col in skewness[skewness > skew_threshold].index.tolist()
    if X_train_reduced[col].min() >= 0
]

#skewed_features = skewness[skewness > skew_threshold].index.tolist()
non_skewed_features = [col for col in numeric_features if col not in skewed_features]

print("Feature con skew elevata:", skewed_features)
print("Feature senza skew elevata:", non_skewed_features)
log_transformer = FunctionTransformer(np.log1p, validate=False)

preprocessor = ColumnTransformer(
    transformers=[
        ("log", log_transformer, skewed_features),
        ("num", "passthrough", non_skewed_features)
    ]
)

pipe_best_svm = Pipeline([
    ('preprocessor', preprocessor),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('svm', SVC(
        kernel=best_svm.named_steps['svm'].kernel,
        C=best_svm.named_steps['svm'].C,
        gamma=best_svm.named_steps['svm'].gamma
    ))
])

pipe_best_svm.fit(X_train_reduced, y_train)

cm , acc_svm_reduced, precision_svm_reduced, recall_svm_reduced, f1_svm_reduced, cfm_svm_reduced = evaluation_finale(pipe_best_svm, X_test_reduced, y_test)
plot_results_evaluation_finale(cm,pipe_best_svm.named_steps['svm'], acc_svm_reduced, precision_svm_reduced, recall_svm_reduced, f1_svm_reduced, cfm_svm_reduced)


X_test_2d = pipe_vis.named_steps['pca'].transform(
    pipe_vis.named_steps['scaler'].transform(X_test_reduced)
)
plot_svm_decision_boundary(
    pipe_vis.named_steps['svm'],
    X_test_2d,
    y_test,
    "SVM RBF — decision boundary (Pipeline-consistent PCA 2D) - feature removed"
)
svm_best = best_svm.named_steps['svm']

pipe_vis = Pipeline([
    ('preprocessor', preprocessor),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2, random_state=42)),
    ('svm', SVC(
        kernel=svm_best.kernel,
        C=svm_best.C,
        gamma=svm_best.gamma
    ))
])

pipe_vis.fit(X_train_reduced, y_train)

X_test_2d = pipe_vis.named_steps['preprocessor'].transform(X_test)
X_test_2d = pipe_vis.named_steps['scaler'].transform(X_test_2d)
X_test_2d = pipe_vis.named_steps['pca'].transform(X_test_2d)
plot_svm_decision_boundary(
    pipe_vis.named_steps['svm'],
    X_test_2d,
    y_test,
    "SVM RBF — decision boundary (Pipeline-consistent PCA 2D) - feature removed"
)
```

# Analisi dello Stress-Test: Impatto della Rimozione delle Feature Dominanti

I risultati ottenuti dal ri-addestramento del miglior modello SVM, in seguito alla rimozione delle feature identificate come "top-ranked" dalla Permutation Importance, mostrano una degradazione significativa e sistematica di tutte le metriche di performance.

## 1. Crollo della Capacità Predittiva

Il modello passa da un'accuratezza del **95.30%** a circa il **75.03%**.

* **Perdita di Informazione:** Un calo del **20%** nell'accuratezza conferma che le feature rimosse non erano semplicemente "utili", ma costituivano la struttura portante del segnale discriminante nel dataset.
* **Assenza di Ridondanza:** Il fatto che le restanti 80+ feature non siano riuscite a compensare la perdita indica che l'informazione contenuta nelle variabili rimosse è unica e non è distribuita in modo ridondante tra le altre variabili.

## 2. Il Collasso della Recall (Criticità di Sicurezza)

La metrica che ha subito il calo più preoccupante è la **Recall**, scesa a **0.6699**.

* **Phishing Mancati:** Una Recall del 67% significa che il modello ora **manca 1 attacco di phishing su 3**. In un contesto di cybersecurity, questo livello di performance è considerato inaccettabile, poiché espone l'utente a un rischio elevatissimo.
* **Sbilanciamento verso i Falsi Negativi:** Mentre la Precision tiene meglio (0.7977), il crollo della Recall suggerisce che, senza le feature chiave, il modello diventa estremamente "conservativo" o incapace di riconoscere i pattern tipici della classe malevola.

## 3. Analisi della F1-Score

L'**F1-Score** si attesta a **0.7282**.

* Questo valore rappresenta un calo drastico rispetto al precedente **0.9528**. La media armonica tra precision e recall evidenzia come il classificatore abbia perso la sua robustezza, trasformandosi da un sistema di difesa affidabile a uno strumento con un'efficacia poco superiore al caso fortuito.

### 4. Conclusioni sull'Importanza delle Feature

Questo esperimento di "ablazione" fornisce la prova definitiva della validità della nostra analisi di feature importance:

1. **Validazione del Metodo:** La Permutation Importance ha correttamente individuato le variabili fondamentali; la loro rimozione ha infatti "ciecato" il modello.
2. **Dipendenza dal Segnale:** Nonostante il dataset sia multidimensionale (89 feature), il potere decisionale è concentrato in un ristretto sottoinsieme di variabili.
3. **Lezione per il Modello:** Il risultato sottolinea che, per il problema del phishing, alcune caratteristiche lessicali o strutturali dell'URL sono insostituibili. Senza di esse, anche il miglior modello (SVM RBF) non è in grado di mappare correttamente lo spazio del problema.
---

# Plot dei risultati

```python
Di seguito, il plot dei risultati sul TestSet di ogni modello provato
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

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 1. Preparazione dei dati (usiamo i tuoi modelli e metriche)
data = []
for metric_name, values in metrics.items():
    best_val = max(values)
    for i, model in enumerate(models):
        data.append({
            'Model': model,
            'Value': values[i],
            'Metric': metric_name,
            'is_best': values[i] == best_val  # Flag per il miglior modello
        })

df = pd.DataFrame(data)

# 2. Creiamo il grafico base con Plotly Express
fig = px.scatter(
    df, 
    x='Value', 
    y='Model', 
    facet_col='Metric', 
    facet_col_wrap=2,
    color_discrete_sequence=['#FFB347'], # Colore arancione
    labels={'Value': 'Score', 'Model': 'Modello'},
    title="Confronto Performance Modelli",
    height=800,
    # Il pop-up (hover) è configurato qui:
    hover_data={'Value': ':.3f', 'Metric': False, 'is_best': False} 
)

# 3. Aggiungiamo il cerchio rosso per i "Best Models"
# Filtriamo il dataframe per prendere solo i vincitori
best_df = df[df['is_best'] == True]

for _, row in best_df.iterrows():
    # Identifichiamo in quale "sottopiano" (facet) aggiungere il cerchio
    # Plotly numera i facet da 1 in poi
    metric_list = list(metrics.keys())
    col_idx = (metric_list.index(row['Metric']) % 2) + 1
    row_idx = 2 - (metric_list.index(row['Metric']) // 2) # Inverte perché Plotly conta dal basso
    
    fig.add_trace(
        go.Scatter(
            x=[row['Value']],
            y=[row['Model']],
            mode='markers',
            marker=dict(
                color='rgba(0,0,0,0)', # Trasparente dentro
                size=15,
                line=dict(color='red', width=2) # Cerchio rosso
            ),
            name='Best Model',
            showlegend=False,
            hoverinfo='skip' # Evita che il cerchio rosso interferisca con il pop-up
        ),
        row=row_idx, col=col_idx
    )

# 4. Estetica e linee tratteggiate (hlines)
fig.update_xaxes(range=[0, 1.05], gridcolor='lightgrey', showgrid=True)
fig.update_yaxes(gridcolor='lightgrey', showgrid=True)

# Aggiungiamo le linee tratteggiate orizzontali per ogni punto
for i in range(len(df)):
    row = df.iloc[i]
    metric_list = list(metrics.keys())
    c = (metric_list.index(row['Metric']) % 2) + 1
    r = 2 - (metric_list.index(row['Metric']) // 2)
    
    fig.add_shape(
        type="line",
        x0=0, y0=row['Model'], x1=row['Value'], y1=row['Model'],
        line=dict(color="orange", width=1, dash="dash"),
        xref=f"x{((r-1)*2+c) if ((r-1)*2+c)>1 else ''} domain", # Logica complessa per i facet
        row=r, col=c
    )

fig.update_layout(
    plot_bgcolor='rgba(240,240,240,0.5)', # Sfondo grigio chiaro
    showlegend=False
)

fig.show()
```

---
# Conclusioni Finali: Confronto tra i Modelli

In questo studio abbiamo messo a confronto tre diversi paradigmi di Machine Learning per la classificazione di URL di phishing: un modello lineare (**Logistic Regression**), un modello basato su iperpiani in spazi kernelizzati (**SVM**) e un'architettura ensemble (**Random Forest**).

## 1. Tabella Riassuntiva delle Performance (Test Set)

| Modello | Accuracy | Precision | Recall | F1-Score | Stabilità ($\sigma$) |
| --- | --- | --- | --- | --- | --- |
| **Logistic Regression** | 94.02% | 0.9401 | 0.9401 | 0.9401 | 0.0055 |
| **SVM (Kernel RBF)** | 95.30% | 0.9541 | 0.9516 | 0.9528 | **0.0021** |
| **Random Forest** | 95.16% | 0.9524 | 0.9507 | 0.9515 | 0.0035 |

*(Nota: I modelli non lineari hanno raggiunto prestazioni di picco identiche sul test set, evidenziando il raggiungimento di un limite superiore di separabilità per questo specifico dataset).*

## 2. Analisi Comparativa

### A. La Forza della Baseline (Logistic Regression)

La **Logistic Regression** ha dimostrato che il problema del phishing possiede una forte componente di **separabilità lineare**. Ottenere un'accuratezza del 94% con un modello così semplice valida la qualità del preprocessing e delle 89 feature estratte. Rappresenta la scelta ottimale in scenari dove la velocità di esecuzione è più critica della precisione estrema.

### B. Il Salto di Qualità (SVM e Random Forest)

Il passaggio a modelli non lineari ha permesso di recuperare un ulteriore **1.3%** di accuratezza. In ambito cybersecurity, questo incremento si traduce nel blocco di migliaia di potenziali minacce aggiuntive.

* **SVM** si è distinto per la **massima stabilità** ($\sigma=0.0021$), dimostrando di essere il modello meno influenzato dal rumore nei dati.
* **Random Forest** ha mostrato un'ottima capacità di adattamento, sebbene con una tendenza leggermente superiore alla memorizzazione del training set rispetto alla SVM.

## 3. Validazione tramite Stress Test (Ablazione Feature)

Per verificare quanto il modello dipenda realmente dalle feature individuate tramite la **Permutation Importance**, abbiamo condotto uno stress test sul miglior modello SVM, rimuovendo le variabili più importanti. I risultati hanno confermato l'importanza critica di tali feature:

* **Accuracy:** crollata dal 95.30% al **75.03%**.
* **Recall:** collassata a **0.6699** (il modello manca 1 attacco su 3).

Questo esperimento di ablazione fornisce la prova definitiva che il potere decisionale è concentrato in un ristretto sottoinsieme di variabili insostituibili. La totale incapacità delle restanti 80+ feature di compensare la perdita dimostra che il segnale del phishing è netto e localizzato.

## 4. Considerazioni sulla Sicurezza: La Recall

La metrica critica del progetto, la **Recall**, è stata elevata dai modelli avanzati dal 94% al **95.16%**. Questo miglioramento riduce drasticamente il rischio di **Falsi Negativi**, garantendo che l'utente finale sia protetto con un'efficacia superiore rispetto a un approccio lineare standard.

## 5. Verdetto Finale

Il modello **SVM con kernel RBF** è quello consigliato per la messa in produzione per tre ragioni chiave:

1. **Stabilità Massima:** La deviazione standard più bassa garantisce che il modello si comporti in modo prevedibile su diversi set di dati.
2. **Affidabilità:** Presenta il miglior bilanciamento tra performance e generalizzazione (minor rischio di overfitting rispetto a Random Forest).
3. **Robustezza Provata:** Lo stress test ha dimostrato che il modello ha imparato correttamente i segnali fondamentali della minaccia.