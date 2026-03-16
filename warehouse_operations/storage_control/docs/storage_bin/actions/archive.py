"""Action handler seed for storage_bin:archive."""

from __future__ import annotations


DOC_ID = "storage_bin"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive goods into warehouse storage, put them away correctly, pick them for orders, and keep warehouse records current', 'actors': ['warehouse supervisor', 'receiving operator', 'picker', 'putaway operator'], 'start_condition': 'goods are received or outgoing orders require warehouse execution', 'ordered_steps': ['Receive goods into the warehouse and assign a storage destination.', 'Keep warehouse locations and stock context aligned.'], 'primary_actions': ['create', 'assign', 'update', 'review'], 'primary_transitions': [], 'downstream_effects': ['warehouse execution feeds shipment, fulfillment, replenishment, and inventory accuracy'], 'action_actors': {'create': ['warehouse supervisor'], 'update': ['warehouse supervisor'], 'review': ['receiving operator'], 'archive': ['warehouse supervisor']}}

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
