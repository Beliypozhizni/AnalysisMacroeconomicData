from macro_analyzer.reports.average_gdp import AverageGdpReport
from macro_analyzer.reports.base import ReportBuilder

_REPORTS: dict[str, ReportBuilder] = {
    AverageGdpReport.name: AverageGdpReport(),
}


def available_reports() -> list[str]:
    return sorted(_REPORTS.keys())


def get_report(report_name: str) -> ReportBuilder:
    try:
        return _REPORTS[report_name]
    except KeyError:
        raise ValueError(
            f"Unknown report: {report_name!r}. Available: {', '.join(available_reports())}"
        )
