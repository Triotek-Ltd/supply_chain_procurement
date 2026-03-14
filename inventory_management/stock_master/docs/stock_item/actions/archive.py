"""Action handler seed for stock_item:archive."""

from __future__ import annotations


DOC_ID = "stock_item"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, verify, store, monitor, count, reconcile, and replenish inventory accurately', 'actors': ['storekeeper', 'warehouse operator', 'inventory controller', 'reviewer'], 'start_condition': 'stock is received, moved, counted, or adjusted', 'ordered_steps': ['Receive goods and verify quantity and condition.'], 'primary_actions': ['create', 'review', 'accept'], 'primary_transitions': [], 'downstream_effects': ['inventory availability feeds purchasing, warehouse execution, logistics, and production planning']}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
