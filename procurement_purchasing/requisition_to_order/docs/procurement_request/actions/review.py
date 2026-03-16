"""Action handler seed for procurement_request:review."""

from __future__ import annotations


DOC_ID = "procurement_request"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'active'], 'transitions_to': 'reviewed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['purchase_requisition', 'purchase_order', 'supplier_profile'], 'borrowed_fields': ['demand details from purchase_requisition'], 'inferred_roles': ['procurement officer', 'account owner']}, 'actors': ['procurement officer', 'account owner'], 'action_actors': {'create': ['procurement officer'], 'review': ['account owner'], 'issue': ['account owner'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
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
