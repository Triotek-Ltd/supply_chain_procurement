"""Action handler seed for supplier_qualification:review."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "supplier_qualification"
ACTION_ID = "review"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['supplier_profile', 'vendor_review', 'vendor_contract'], 'borrowed_fields': ['supplier identity from supplier_profile'], 'inferred_roles': ['compliance officer', 'procurement officer']}, 'actors': ['compliance officer', 'procurement officer'], 'action_actors': {'create': ['compliance officer'], 'review': ['procurement officer'], 'approve': ['compliance officer'], 'reject': ['compliance officer'], 'close': ['compliance officer'], 'archive': ['compliance officer']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
