"""
src/analysis/metrics.py
------------------------
Calcul des KPIs et génération du rapport d'insights.
"""

import pandas as pd
from pathlib import Path

PROCESSED_PATH = Path("data/processed/coffee_sales_clean.csv")


def load_clean() -> pd.DataFrame:
    df = pd.read_csv(PROCESSED_PATH, parse_dates=["Date"])
    return df


def compute_kpis(df: pd.DataFrame) -> dict:
    """Calcule les indicateurs clés de performance."""
    kpis = {}

    # Revenus
    kpis["total_revenue"] = df["money"].sum()
    kpis["avg_daily_revenue"] = df.groupby("Date")["money"].sum().mean()
    kpis["avg_ticket"] = df["money"].mean()
    kpis["nb_transactions"] = len(df)

    # Produit le plus vendu
    top_product = df["coffee_name"].value_counts()
    kpis["top_product_by_volume"] = top_product.index[0]
    kpis["top_product_volume"] = int(top_product.iloc[0])

    # Produit le plus rentable
    top_revenue = df.groupby("coffee_name")["money"].sum().sort_values(ascending=False)
    kpis["top_product_by_revenue"] = top_revenue.index[0]

    # Heure de pointe
    peak_hour = df["hour_of_day"].value_counts().index[0]
    kpis["peak_hour"] = int(peak_hour)

    # Jour le plus chargé
    peak_day = df["Weekday"].value_counts().index[0]
    kpis["peak_day"] = peak_day

    # Meilleur mois (revenus)
    best_month = df.groupby("Month_name")["money"].sum().sort_values(ascending=False)
    kpis["best_month"] = best_month.index[0]
    kpis["best_month_revenue"] = best_month.iloc[0]

    return kpis


def print_report(kpis: dict) -> None:
    print("=" * 50)
    print("       ☕ COFFEE SALES — KPI REPORT")
    print("=" * 50)
    print(f"  Transactions totales  : {kpis['nb_transactions']:,}")
    print(f"  Chiffre d'affaires    : {kpis['total_revenue']:,.2f}")
    print(f"  CA moyen / jour       : {kpis['avg_daily_revenue']:,.2f}")
    print(f"  Ticket moyen          : {kpis['avg_ticket']:,.2f}")
    print(f"  Produit top ventes    : {kpis['top_product_by_volume']} ({kpis['top_product_volume']} unités)")
    print(f"  Produit top revenus   : {kpis['top_product_by_revenue']}")
    print(f"  Heure de pointe       : {kpis['peak_hour']}h")
    print(f"  Jour le plus chargé   : {kpis['peak_day']}")
    print(f"  Meilleur mois         : {kpis['best_month']} ({kpis['best_month_revenue']:,.2f})")
    print("=" * 50)


if __name__ == "__main__":
    df = load_clean()
    kpis = compute_kpis(df)
    print_report(kpis)