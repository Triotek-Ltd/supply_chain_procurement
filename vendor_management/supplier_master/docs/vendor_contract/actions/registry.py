"""Action registry seed for vendor_contract."""

from __future__ import annotations

from typing import Any


DOC_ID = "vendor_contract"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'activate', 'renew', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': 'approved'}, 'activate': {'allowed_in_states': ['draft'], 'transitions_to': 'active'}, 'renew': {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': 'renewed'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': 'archived'}}

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
