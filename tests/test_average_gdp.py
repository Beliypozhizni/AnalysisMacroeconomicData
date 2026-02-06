from macro_analyzer.reports.average_gdp import AverageGdpReport

def test_average_gdp_aggregates_and_sorts_desc():
    rows = [
        {"country": "A", "gdp": "10"},
        {"country": "B", "gdp": "100"},
        {"country": "A", "gdp": "30"},
        {"country": "B", "gdp": "50"},
        {"country": "C", "gdp": "1"},
    ]
    report = AverageGdpReport().build(rows)

    assert tuple(report.headers) == ("country", "avg_gdp")
    assert report.rows == [("B", 75.0), ("A", 20.0), ("C", 1.0)]
