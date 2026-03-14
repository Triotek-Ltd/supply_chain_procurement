"""Action registry seed for supplier_qualification."""

from __future__ import annotations


DOC_ID = "supplier_qualification"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'reject', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': None}, 'review': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': None}, 'reject': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': 'rejected'}, 'close': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'in_review', 'qualified', 'rejected'], 'transitions_to': 'archived'}}

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
