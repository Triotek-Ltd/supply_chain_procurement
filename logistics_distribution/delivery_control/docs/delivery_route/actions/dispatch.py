"""Action handler seed for delivery_route:dispatch."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "delivery_route"
ACTION_ID = "dispatch"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'plan, dispatch, track, and confirm outbound delivery execution', 'actors': ['logistics coordinator', 'warehouse team', 'carrier', 'dispatcher', 'recipient'], 'start_condition': 'a delivery request or shipping order is ready for execution', 'ordered_steps': ['Assign route and transport method.', 'Dispatch the shipment.'], 'primary_actions': ['create', 'assign', 'submit', 'confirm', 'dispatch'], 'primary_transitions': ['delivery_route: draft -> assigned', 'delivery_route: assigned -> dispatched'], 'downstream_effects': ['delivery completion feeds billing, customer service, and performance reporting'], 'action_actors': {'create': ['logistics coordinator'], 'assign': ['logistics coordinator'], 'dispatch': ['recipient'], 'close': ['logistics coordinator'], 'archive': ['logistics coordinator']}}

def handle_dispatch(payload: dict, context: dict | None = None) -> dict:
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
