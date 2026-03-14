"""Report-service seed for supplier_profile."""

from __future__ import annotations


DOC_ID = "supplier_profile"
DOC_KIND = "master"

LIST_COLUMNS = ['title', 'reference_no', 'workflow_state', 'modified']

class ReportService:
    def supports_reporting_hooks(self) -> bool:
        return DOC_KIND in {"transaction", "ledger", "workflow_case"}

    def default_dimensions(self) -> list[str]:
        return LIST_COLUMNS

    def reporting_profile(self) -> dict:
        return {'supports_snapshots': False, 'supports_outputs': False}
