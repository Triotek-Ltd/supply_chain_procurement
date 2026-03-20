"""Action registry seed for goods_receipt."""

from __future__ import annotations

from typing import Any


DOC_ID = "goods_receipt"
ALLOWED_ACTIONS = ['create', 'review', 'submit', 'accept', 'reject', 'close', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': 'submitted'}, 'accept': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'reject': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': 'archived'}}

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
