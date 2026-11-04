"""Tests for every number quoted in the manual.

Each test mirrors a formula or result documented in docs/, computed here
with Python from the same example files. If a test fails, either the docs
or the data drifted — fix one of them.

Run:  python3 -m pytest tests/ -v        (or: python3 tests/test_examples.py)
"""

import csv
import datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXAMPLES = ROOT / "examples"

orders = pd.read_csv(EXAMPLES / "orders.csv", parse_dates=["Date"])
_raw_orders_columns = list(orders.columns)
orders["LineTotal"] = orders["Qty"] * orders["UnitPrice"]
catalog = pd.read_csv(EXAMPLES / "catalog.csv")

# ---------------------------------------------------------------- datasets


def test_orders_shape_and_columns():
    """docs/index.md: 12 rows of data, 8 columns with documented names."""
    assert len(orders) == 12
    assert _raw_orders_columns == [   # the file itself has exactly these 8
        "OrderID", "Date", "Customer", "Product", "Qty", "UnitPrice",
        "Category", "Region",
    ]
    assert orders["OrderID"].min() == 1001
    assert orders["OrderID"].max() == 1012


def test_catalog_shape():
    """ch03: catalog has 4 products, headers in row 1, data rows 2-5."""
    assert len(catalog) == 4
    assert list(catalog.columns) == ["Product", "UnitPrice", "Category"]


# ------------------------------------------------------- chapter 1 numbers


def test_line_total_spotchecks():
    """ch01: OrderID 1010 = 3 * 42.00 = 126.00; 1002 = 18.50."""
    got_1010 = orders.loc[orders["OrderID"] == 1010, "LineTotal"].iloc[0]
    got_1002 = orders.loc[orders["OrderID"] == 1002, "LineTotal"].iloc[0]
    assert got_1010 == 126.00
    assert got_1002 == 18.50


def test_grand_total_584():
    """ch01: =SUM(I2:I13) should be 584.00 (matches manual, 3 decimal-free)."""
    assert round(orders["LineTotal"].sum(), 2) == 584.00


# ------------------------------------------------------- chapter 3 vlookup


def test_vlookup_beeswax_24():
    """ch03: VLOOKUP for 'Beeswax Pillars' returns 24.00 from the catalog."""
    match = catalog.loc[catalog["Product"] == "Beeswax Pillars", "UnitPrice"]
    assert not match.empty
    assert match.iloc[0] == 24.00


def test_every_order_product_exists_in_catalog():
    """ch03: with relationships intact, zero #N/A for the 12 order rows."""
    in_catalog = set(catalog["Product"])
    for product in orders["Product"]:
        assert product in in_catalog, f"missing from catalog: {product!r}"


def test_lookup_absent_product_is_na():
    """ch03: a product outside the catalog is the genuine-#N/A case."""
    absent = "Wick Trimmer Set"
    assert absent not in set(catalog["Product"])


# --------------------------------------------- chapter 4 sumif and countif


def test_sumif_gift_sets_294():
    got = orders.loc[orders["Category"] == "Gift Sets", "LineTotal"].sum()
    assert round(got, 2) == 294.00


def test_countif_candles_5():
    got = (orders["Category"] == "Candles").sum()
    assert got == 5


def test_sumif_midwest_193():
    got = orders.loc[orders["Region"] == "Midwest", "LineTotal"].sum()
    assert round(got, 2) == 193.00


def test_sumifs_gift_sets_and_west_126():
    got = orders.loc[
        (orders["Category"] == "Gift Sets") & (orders["Region"] == "West"),
        "LineTotal",
    ].sum()
    assert round(got, 2) == 126.00


# ----------------------------------------------------------- chapter 5 dates


def test_date_arithmetic_b2_plus_20():
    """ch05: =B2+20 where B2 is 2026-01-05 gives 2026-01-25."""
    b2 = datetime.date(2026, 1, 5)
    assert b2 + datetime.timedelta(days=20) == datetime.date(2026, 1, 25)


def test_days_between_20():
    """ch05: =DAYS(B13,B2) = Jan 5 to Jan 25 = 20 days."""
    assert orders["Date"].max() - orders["Date"].min() == datetime.timedelta(days=20)


def test_eomonth_january_31():
    """ch05: =EOMONTH(B2,0) gives the last day of B2's month (2026-01-31)."""
    last_day = datetime.date(2026, 1, 1) + datetime.timedelta(days=30)
    assert last_day == datetime.date(2026, 1, 31)


def test_sumifs_date_window_253_six_orders():
    """ch05: orders Jan 11-20 sum to 253.00 across 6 orders (1004-1009)."""
    window = orders[
        (orders["Date"] >= "2026-01-11") & (orders["Date"] <= "2026-01-20")
    ]
    assert len(window) == 6
    assert set(window["OrderID"]) == {1004, 1005, 1006, 1007, 1008, 1009}
    assert round(window["LineTotal"].sum(), 2) == 253.00


# ------------------------------------------------------ chapter 6 pivots


def test_pivot_by_category():
    """ch06: revenue per category (three rows, in the manual's table)."""
    pivot = orders.groupby("Category")["LineTotal"].sum().round(2)
    assert dict(pivot) == {"Candles": 216.00, "Gift Sets": 294.00, "Refills": 74.00}


def test_pivot_by_region():
    """ch06: revenue per region (four rows, in the manual's table)."""
    pivot = orders.groupby("Region")["LineTotal"].sum().round(2)
    assert dict(pivot) == {
        "Midwest": 193.00, "Northeast": 79.00, "South": 114.00, "West": 198.00,
    }


def test_pivots_reconcile_to_grand_total():
    """ch06: every pivot view sums to the 584.00 grand total."""
    assert round(orders.groupby("Category")["LineTotal"].sum().sum(), 2) == 584.00
    assert round(orders.groupby("Region")["LineTotal"].sum().sum(), 2) == 584.00


# --------------------------------------------------------- chapter 7 cleaning


def _clean(name: str) -> str:
    """=PROPER(TRIM(A2)) behavior: trim ends, collapse inner runs of spaces."""
    collapsed = " ".join(name.split())  # strips ends, squeezes inner spaces
    return " ".join(w.capitalize() for w in collapsed.split(" "))


def test_cleaning_produces_six_unique_names():
    """ch07: 7 messy rows clean to 6 unique people; Omar Haddad is a dupe."""
    with open(EXAMPLES / "messy_names.csv", newline="", encoding="utf-8") as fh:
        messy = [row["MessyName"] for row in csv.DictReader(fh)]
    assert len(messy) == 7
    cleaned = [_clean(m) for m in messy]
    assert cleaned == [
        "Maya Chen", "Luis Ortega", "Priya Patel", "June Tanaka",
        "Omar Haddad", "Omar Haddad", "Grace Okafor",
    ]
    assert cleaned.count("Omar Haddad") == 2          # the duplicated person
    assert len(set(cleaned)) == 6                      # six unique people
    assert messy[0].startswith("  ") and messy[0].endswith(" ")  # raw is messy


# ---------------------------------------------- docs reference the numbers


def test_docs_mention_the_tested_numbers():
    """If the data changes, these documented figures must change with it."""
    expected_numbers = [
        "584.00",   # grand total (ch01, ch06)
        "294.00",   # SUMIF Gift Sets (ch04, ch06)
        "193.00",   # SUMIF Midwest (ch04)
        "24.00",    # VLOOKUP Beeswax Pillars (ch03)
        "126.00",   # SUMIFS Gift Sets+West, order 1010 (ch03, ch04)
        "253.00",   # SUMIFS date window (ch05)
        "216.00",   # pivot Candles (ch04, ch06)
        "74.00",    # pivot Refills (ch04, ch06)
    ]
    everything = "\n".join(
        p.read_text(encoding="utf-8") for p in sorted(DOCS.glob("*.md"))
    )
    for number in expected_numbers:
        assert number in everything, f"{number} missing from docs/"
