"""Action registry seed for purchase_order."""

from __future__ import annotations

from typing import Any


DOC_ID = "purchase_order"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'issue', 'receive', 'bill', 'close', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'issue': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'receive': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'bill': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'partially_received', 'received', 'billed'], 'transitions_to': 'archived'}}

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
