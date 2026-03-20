"""Action registry seed for transport_booking."""

from __future__ import annotations

from typing import Any


DOC_ID = "transport_booking"
ALLOWED_ACTIONS = ['create', 'submit', 'confirm', 'cancel', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': 'submitted'}, 'confirm': {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': 'confirmed'}, 'cancel': {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'confirmed', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
