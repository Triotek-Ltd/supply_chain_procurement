"""Action handler seed for transport_booking:archive."""

from __future__ import annotations


DOC_ID = "transport_booking"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'plan, dispatch, track, and confirm outbound delivery execution', 'actors': ['logistics coordinator', 'warehouse team', 'carrier', 'dispatcher', 'recipient'], 'start_condition': 'a delivery request or shipping order is ready for execution', 'ordered_steps': ['Assign route and transport method.'], 'primary_actions': ['create', 'assign', 'submit', 'confirm'], 'primary_transitions': ['transport_booking: draft -> submitted -> confirmed'], 'downstream_effects': ['delivery completion feeds billing, customer service, and performance reporting'], 'action_actors': {'create': ['logistics coordinator'], 'submit': ['logistics coordinator'], 'confirm': ['warehouse team'], 'cancel': ['logistics coordinator'], 'archive': ['logistics coordinator']}}

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
