"""Action handler seed for pick_list:close."""

from __future__ import annotations


DOC_ID = "pick_list"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['draft', 'assigned', 'in_progress', 'completed'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive goods into warehouse storage, put them away correctly, pick them for orders, and keep warehouse records current', 'actors': ['warehouse supervisor', 'receiving operator', 'picker', 'putaway operator'], 'start_condition': 'goods are received or outgoing orders require warehouse execution', 'ordered_steps': ['Create pick work for outgoing demand.', 'Pick and complete warehouse execution.'], 'primary_actions': ['create', 'assign', 'start', 'complete', 'close'], 'primary_transitions': ['pick_list: draft -> assigned', 'pick_list: assigned -> in_progress -> completed -> closed'], 'downstream_effects': ['warehouse execution feeds shipment, fulfillment, replenishment, and inventory accuracy'], 'action_actors': {'create': ['warehouse supervisor'], 'assign': ['warehouse supervisor'], 'close': ['warehouse supervisor'], 'archive': ['warehouse supervisor']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
