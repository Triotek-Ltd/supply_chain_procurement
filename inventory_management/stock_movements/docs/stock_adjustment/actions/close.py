"""Action handler seed for stock_adjustment:close."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "stock_adjustment"
ACTION_ID = "close"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, verify, store, monitor, count, reconcile, and replenish inventory accurately', 'actors': ['storekeeper', 'warehouse operator', 'inventory controller', 'reviewer'], 'start_condition': 'stock is received, moved, counted, or adjusted', 'ordered_steps': ['Monitor stock levels and trigger recount or replenishment as needed.', 'Reconcile physical count variances and apply adjustments.'], 'primary_actions': ['review', 'create', 'approve', 'apply', 'close'], 'primary_transitions': ['stock_adjustment: opened', 'stock_adjustment: opened -> reviewed -> approved -> applied -> closed'], 'downstream_effects': ['inventory availability feeds purchasing, warehouse execution, logistics, and production planning'], 'action_actors': {'create': ['storekeeper'], 'review': ['reviewer'], 'approve': ['reviewer'], 'close': ['storekeeper'], 'archive': ['storekeeper']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
