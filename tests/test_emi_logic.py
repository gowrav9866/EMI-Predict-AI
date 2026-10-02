import pandas as pd

from app.logic import calculate_requested_emi, series_to_chart_df


def test_calculate_requested_emi():
    emi = calculate_requested_emi(250000, 12.0, 24)
    assert emi > 0
    assert abs(emi - 11040.17) < 5.0


def test_series_to_chart_df():
    series = pd.Series({"Eligible": 12, "High_Risk": 3, "Not_Eligible": 15})

    result = series_to_chart_df(series, index_name="Status", value_name="Applicants")

    assert list(result.columns) == ["Status", "Applicants"]
    assert result["Applicants"].tolist() == [12, 3, 15]
    assert result["Status"].tolist() == ["Eligible", "High_Risk", "Not_Eligible"]
