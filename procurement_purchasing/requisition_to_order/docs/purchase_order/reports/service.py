"""Report-service seed for purchase_order."""

from __future__ import annotations


DOC_ID = "purchase_order"
DOC_KIND = "transaction"

LIST_COLUMNS = ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state']

class ReportService:
    def supports_reporting_hooks(self) -> bool:
        return DOC_KIND in {"transaction", "ledger", "workflow_case"}

    def default_dimensions(self) -> list[str]:
        return LIST_COLUMNS

    def reporting_profile(self) -> dict:
        return {'supports_snapshots': True, 'supports_outputs': True}
