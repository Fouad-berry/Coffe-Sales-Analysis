"""
tests/test_transformation.py
-----------------------------
Tests unitaires pour le pipeline de transformation.
"""

import pytest
import pandas as pd
from io import StringIO
from src.transformation.clean_transform import clean

SAMPLE_CSV = """hour_of_day,cash_type,money,coffee_name,Time_of_Day,Weekday,Month_name,Weekdaysort,Monthsort,Date,Time
10,card,38.7,Latte,Morning,Fri,Mar,5,3,2024-03-01,10:15:50.520000
13,card,28.9,Americano,Afternoon,Fri,Mar,5,3,2024-03-01,13:46:33.006000
18,card,32.8,Cappuccino,Evening,Sat,Mar,6,3,2024-03-02,18:05:10.000000
"""


@pytest.fixture
def sample_df():
    return pd.read_csv(StringIO(SAMPLE_CSV))


def test_clean_adds_month_year(sample_df):
    df = clean(sample_df)
    assert "month_year" in df.columns


def test_clean_adds_quarter(sample_df):
    df = clean(sample_df)
    assert "quarter" in df.columns


def test_clean_date_is_datetime(sample_df):
    df = clean(sample_df)
    assert pd.api.types.is_datetime64_any_dtype(df["Date"])


def test_clean_no_rows_lost(sample_df):
    df = clean(sample_df)
    assert len(df) == len(sample_df)


def test_clean_money_unchanged(sample_df):
    df = clean(sample_df)
    assert df["money"].sum() == sample_df["money"].sum()