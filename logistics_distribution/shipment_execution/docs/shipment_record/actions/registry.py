"""Action registry seed for shipment_record."""

from __future__ import annotations

from typing import Any


DOC_ID = "shipment_record"
ALLOWED_ACTIONS = ['create', 'pack', 'dispatch', 'deliver', 'close', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': None}, 'pack': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': None}, 'dispatch': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': None}, 'deliver': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['draft', 'packed', 'dispatched', 'delivered', 'exception'], 'transitions_to': 'archived'}}

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
