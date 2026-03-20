"""Action handler seed for shipment_record:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "shipment_record"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive goods into warehouse storage, put them away correctly, pick them for orders, and keep warehouse records current', 'actors': ['warehouse supervisor', 'receiving operator', 'picker', 'putaway operator'], 'start_condition': 'goods are received or outgoing orders require warehouse execution', 'ordered_steps': ['Create pick work for outgoing demand.'], 'primary_actions': ['create', 'assign'], 'primary_transitions': [], 'downstream_effects': ['warehouse execution feeds shipment, fulfillment, replenishment, and inventory accuracy'], 'action_actors': {'create': ['warehouse supervisor'], 'dispatch': ['putaway operator'], 'close': ['warehouse supervisor'], 'archive': ['warehouse supervisor']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
