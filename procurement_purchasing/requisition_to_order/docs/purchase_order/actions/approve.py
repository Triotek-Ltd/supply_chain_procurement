"""Action handler seed for purchase_order:approve."""

from __future__ import annotations


DOC_ID = "purchase_order"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'convert an internal purchasing need into an approved purchase order issued to the right supplier', 'actors': ['requesting department', 'procurement officer', 'reviewer', 'approver', 'supplier'], 'start_condition': 'a department raises a purchasing need', 'ordered_steps': ['Create and issue the purchase order.', 'Record the committed procurement obligation.'], 'primary_actions': ['create', 'review', 'approve', 'issue'], 'primary_transitions': ['purchase_order: draft -> submitted -> approved'], 'downstream_effects': ['purchase orders feed goods receipt, supplier invoice matching, and vendor performance tracking']}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
