from dataclasses import dataclass

from macro_analyzer.models import Report

FIELD_COUNTRY = "country"
FIELD_GDP = "gdp"
FIELD_AVG_GDP = "avg_gdp"


@dataclass(frozen=True)
class AverageGdpReport:
    name: str = "average-gdp"

    def build(self, rows: list[dict[str, str]]) -> Report:
        agg: dict[str, tuple[int, int]] = {}

        for r in rows:
            country = r[FIELD_COUNTRY]
            gdp = int(r[FIELD_GDP])

            total, count = agg.get(country, (0, 0))
            agg[country] = (total + gdp, count + 1)

        result_rows = [
            (country, round(total / count, 2))
            for country, (total, count) in agg.items()
        ]
        result_rows.sort(key=lambda x: x[1], reverse=True)

        return Report(headers=(FIELD_COUNTRY, FIELD_AVG_GDP), rows=result_rows)
