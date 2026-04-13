"""
src/ingestion/load_data.py
--------------------------
Chargement et validation des données brutes.
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/coffee_sales.csv")

EXPECTED_COLUMNS = {
    "hour_of_day", "cash_type", "money", "coffee_name",
    "Time_of_Day", "Weekday", "Month_name", "Weekdaysort",
    "Monthsort", "Date", "Time"
}


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Charge le CSV brut et effectue des validations de base."""
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    df = pd.read_csv(path)

    # Validation colonnes
    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Colonnes manquantes : {missing}")

    print(f"✅ Données chargées — {len(df):,} lignes × {df.shape[1]} colonnes")
    print(f"   Période : {df['Date'].min()} → {df['Date'].max()}")
    print(f"   Produits : {sorted(df['coffee_name'].unique())}")
    return df


if __name__ == "__main__":
    df = load_raw()
    print(df.head())