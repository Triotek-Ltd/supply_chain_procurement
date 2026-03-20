"""Action registry seed for stock_item."""

from __future__ import annotations

from typing import Any


DOC_ID = "stock_item"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['active'], 'transitions_to': None}, 'update': {'allowed_in_states': ['active'], 'transitions_to': None}, 'review': {'allowed_in_states': ['active'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['active'], 'transitions_to': 'archived'}}

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
