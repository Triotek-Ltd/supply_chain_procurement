"""Action registry seed for delivery_route."""

from __future__ import annotations


DOC_ID = "delivery_route"
ALLOWED_ACTIONS = ['create', 'assign', 'optimize', 'dispatch', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}, 'optimize': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}, 'dispatch': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'assigned', 'dispatched', 'completed'], 'transitions_to': 'archived'}}

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
