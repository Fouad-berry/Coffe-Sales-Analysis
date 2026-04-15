# ☕ Coffee Sales — Data Analysis Project

Analyse des ventes d'un coffee shop (mars 2024 – mars 2025), avec visualisation sur **Looker Studio**.

---

## 📊 Dataset

| Champ | Description |
|---|---|
| `Date` | Date de la transaction |
| `Time` | Heure exacte |
| `hour_of_day` | Heure (int) |
| `Time_of_Day` | Morning / Afternoon / Evening |
| `Weekday` | Jour de la semaine |
| `Month_name` | Mois |
| `coffee_name` | Type de café (8 références) |
| `money` | Montant en devise locale |
| `cash_type` | Mode de paiement |

**Volume :** 3 547 transactions • **Période :** 12 mois

---

## 🏗️ Architecture du projet

```
coffee_sales_analysis/
│
├── data/
│   ├── raw/                  # Données brutes (ne jamais modifier)
│   │   └── coffee_sales.csv
│   ├── processed/            # Données nettoyées
│   │   └── coffee_sales_clean.csv
│   └── exports/              # Exports pour Looker Studio
│       ├── daily_sales.csv
│       ├── hourly_traffic.csv
│       ├── product_performance.csv
│       └── monthly_trends.csv
│
├── notebooks/
│   ├── 01_exploration.ipynb      # EDA — exploration initiale
│   ├── 02_cleaning.ipynb         # Nettoyage & transformation
│   └── 03_analysis.ipynb         # Analyses & insights
│
├── src/
│   ├── ingestion/
│   │   └── load_data.py          # Chargement & validation des données
│   ├── transformation/
│   │   └── clean_transform.py    # Pipeline de nettoyage
│   └── analysis/
│       └── metrics.py            # Calcul des KPIs
│
├── dashboard/
│   └── looker_schema.md          # Structure des vues Looker Studio
│
├── docs/
│   └── insights.md               # Résumé des insights clés
│
├── tests/
│   └── test_transformation.py    # Tests unitaires
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Utilisation

### 1. Cloner le repo
```bash
git clone https://github.com/TON_USER/coffee-sales-analysis.git
cd coffee-sales-analysis
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer le pipeline complet
```bash
python src/ingestion/load_data.py
python src/transformation/clean_transform.py
python src/analysis/metrics.py
```

Les fichiers CSV d'export seront générés dans `data/exports/` — prêts à être importés dans **Looker Studio**.

---

## 📈 KPIs analysés

- **Chiffre d'affaires** : total, par mois, par jour de semaine
- **Produits les plus vendus** : volume & revenus par référence
- **Pics de trafic** : heures, jours et périodes les plus chargés
- **Ticket moyen** : global et par type de café
- **Tendances mensuelles** : évolution sur 12 mois

---

## 🔗 Looker Studio

Les 4 tables d'export (`data/exports/*.csv`) sont uploadées dans **Google Drive** puis connectées à Looker Studio comme sources de données distinctes.

Voir `dashboard/looker_schema.md` pour la configuration détaillée.

---

## 🛠️ Stack technique

- **Python 3.11+**
- **pandas** — manipulation de données
- **numpy** — calculs numériques
- **matplotlib / seaborn** — visualisations exploratoires
- **Looker Studio** — dashboard final (Google)

---

## 📁 Données brutes

Fait par **Fouad MOUTAIROU**
Portfolio : https://portfolio-fouad.netlify.app/ 

Le fichier `data/raw/coffee_sales.csv` contient les données originales et **ne doit jamais être modifié**. Toute transformation se fait dans les scripts `src/`.