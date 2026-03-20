"""Action handler seed for supplier_profile:suspend."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "supplier_profile"
ACTION_ID = "suspend"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain supplier master quality, review vendor performance, and resolve supplier issues proactively', 'actors': ['vendor manager', 'reviewer', 'legal/procurement owner'], 'start_condition': 'a supplier is onboarded or reviewed', 'ordered_steps': ['Create or update the supplier profile.'], 'primary_actions': ['create', 'update', 'review'], 'primary_transitions': ['supplier_profile: draft -> active'], 'downstream_effects': ['supports sourcing, purchase control, and risk management'], 'action_actors': {'create': ['vendor manager'], 'update': ['vendor manager'], 'review': ['reviewer'], 'archive': ['legal/procurement owner']}}

def handle_suspend(payload: dict, context: dict | None = None) -> dict:
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
