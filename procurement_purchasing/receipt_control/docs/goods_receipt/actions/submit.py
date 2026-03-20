"""Action handler seed for goods_receipt:submit."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "goods_receipt"
ACTION_ID = "submit"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': 'submitted'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive goods into warehouse storage, put them away correctly, pick them for orders, and keep warehouse records current', 'actors': ['warehouse supervisor', 'receiving operator', 'picker', 'putaway operator'], 'start_condition': 'goods are received or outgoing orders require warehouse execution', 'ordered_steps': ['Receive goods into the warehouse and assign a storage destination.'], 'primary_actions': ['create', 'assign'], 'primary_transitions': [], 'downstream_effects': ['warehouse execution feeds shipment, fulfillment, replenishment, and inventory accuracy'], 'action_actors': {'create': ['warehouse supervisor'], 'review': ['receiving operator'], 'submit': ['warehouse supervisor'], 'reject': ['warehouse supervisor'], 'close': ['warehouse supervisor'], 'archive': ['warehouse supervisor']}}

def handle_submit(payload: dict, context: dict | None = None) -> dict:
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
