"""Action handler seed for inventory_movement:approve."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "inventory_movement"
ACTION_ID = "approve"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, verify, store, monitor, count, reconcile, and replenish inventory accurately', 'actors': ['storekeeper', 'warehouse operator', 'inventory controller', 'reviewer'], 'start_condition': 'stock is received, moved, counted, or adjusted', 'ordered_steps': ['Record inventory movement into storage.', 'Reconcile physical count variances and apply adjustments.'], 'primary_actions': ['create', 'review', 'approve', 'post', 'apply', 'close'], 'primary_transitions': ['inventory_movement: draft -> approved -> posted'], 'downstream_effects': ['inventory availability feeds purchasing, warehouse execution, logistics, and production planning'], 'action_actors': {'create': ['storekeeper'], 'review': ['reviewer'], 'approve': ['reviewer'], 'post': ['reviewer'], 'reverse': ['storekeeper'], 'archive': ['storekeeper']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
