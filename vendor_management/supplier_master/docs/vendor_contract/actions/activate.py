"""Action handler seed for vendor_contract:activate."""

from __future__ import annotations


DOC_ID = "vendor_contract"
ACTION_ID = "activate"
ACTION_RULE = {'allowed_in_states': ['draft'], 'transitions_to': 'active'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['supplier_profile', 'vendor_review', 'purchase_order'], 'borrowed_fields': ['supplier identity', 'payment terms from supplier_profile'], 'inferred_roles': ['compliance officer', 'procurement officer', 'account owner', 'finance officer']}, 'actors': ['compliance officer', 'procurement officer', 'account owner', 'finance officer'], 'action_actors': {'create': ['compliance officer'], 'review': ['procurement officer'], 'approve': ['compliance officer'], 'activate': ['account owner'], 'archive': ['account owner']}}

def handle_activate(payload: dict, context: dict | None = None) -> dict:
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
