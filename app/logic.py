from __future__ import annotations

import pandas as pd


def calculate_requested_emi(
    principal: float,
    annual_interest_rate: float,
    tenure_months: int,
) -> float:
    """Return the EMI for a standard reducing-balance loan."""
    if principal <= 0 or tenure_months <= 0:
        raise ValueError("Principal and tenure must be positive values.")

    monthly_rate = annual_interest_rate / 12 / 100

    if monthly_rate == 0:
        return principal / tenure_months

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** tenure_months
    ) / ((1 + monthly_rate) ** tenure_months - 1)

    return float(emi)


def series_to_chart_df(series: pd.Series, index_name: str = "index", value_name: str = "value") -> pd.DataFrame:
    """Convert a pandas Series to a chart-friendly DataFrame."""
    chart_df = series.reset_index()
    if chart_df.shape[1] == 2:
        chart_df.columns = [index_name, value_name]
    else:
        chart_df = pd.DataFrame({index_name: series.index, value_name: series.values})
    return chart_df
