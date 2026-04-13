"""
src/transformation/clean_transform.py
--------------------------------------
Nettoyage, typage et enrichissement des données.
Génère les exports CSV pour Looker Studio.
"""

import pandas as pd
from pathlib import Path
from src.ingestion.load_data import load_raw

PROCESSED_PATH = Path("data/processed/coffee_sales_clean.csv")
EXPORTS_PATH = Path("data/exports")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage et typage des colonnes."""
    df = df.copy()

    # Types datetime
    df["Date"] = pd.to_datetime(df["Date"])
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S.%f", errors="coerce")
    df["hour_of_day"] = df["hour_of_day"].astype(int)

    # Colonnes enrichies
    df["week_number"] = df["Date"].dt.isocalendar().week.astype(int)
    df["day_of_month"] = df["Date"].dt.day
    df["quarter"] = df["Date"].dt.quarter
    df["year"] = df["Date"].dt.year
    df["month_year"] = df["Date"].dt.to_period("M").astype(str)

    print(f"✅ Nettoyage terminé — {len(df):,} lignes")
    return df


def export_for_looker(df: pd.DataFrame) -> None:
    """Génère les tables agrégées pour Looker Studio."""
    EXPORTS_PATH.mkdir(parents=True, exist_ok=True)

    # 1. Ventes journalières
    daily = (
        df.groupby("Date")
        .agg(
            total_revenue=("money", "sum"),
            nb_transactions=("money", "count"),
            avg_ticket=("money", "mean"),
        )
        .reset_index()
    )
    daily["Date"] = daily["Date"].astype(str)
    daily.to_csv(EXPORTS_PATH / "daily_sales.csv", index=False)
    print("  → daily_sales.csv")

    # 2. Trafic par heure
    hourly = (
        df.groupby(["hour_of_day", "Time_of_Day"])
        .agg(
            nb_transactions=("money", "count"),
            total_revenue=("money", "sum"),
        )
        .reset_index()
    )
    hourly.to_csv(EXPORTS_PATH / "hourly_traffic.csv", index=False)
    print("  → hourly_traffic.csv")

    # 3. Performance produit
    products = (
        df.groupby("coffee_name")
        .agg(
            nb_sold=("money", "count"),
            total_revenue=("money", "sum"),
            avg_price=("money", "mean"),
        )
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )
    products.to_csv(EXPORTS_PATH / "product_performance.csv", index=False)
    print("  → product_performance.csv")

    # 4. Tendances mensuelles
    monthly = (
        df.groupby(["month_year", "Monthsort", "Month_name", "year"])
        .agg(
            total_revenue=("money", "sum"),
            nb_transactions=("money", "count"),
            avg_ticket=("money", "mean"),
        )
        .sort_values(["year", "Monthsort"])
        .reset_index()
    )
    monthly.to_csv(EXPORTS_PATH / "monthly_trends.csv", index=False)
    print("  → monthly_trends.csv")

    print(f"\n✅ Exports générés dans {EXPORTS_PATH}/")


if __name__ == "__main__":
    df_raw = load_raw()
    df_clean = clean(df_raw)
    df_clean.to_csv(PROCESSED_PATH, index=False)
    print(f"💾 Données nettoyées sauvegardées → {PROCESSED_PATH}")
    export_for_looker(df_clean)