from typing import Protocol

from macro_analyzer.models import Report


class ReportBuilder(Protocol):
    """Interface for report builders.

    A builder must have:
      - name: stable CLI name
      - build(rows) -> Report
    """

    name: str

    def build(self, rows: list[dict[str, str]]) -> Report:
        pass
