"""Action registry seed for stock_adjustment."""

from __future__ import annotations


DOC_ID = "stock_adjustment"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'apply', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'approved'}, 'apply': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'archived'}}

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
