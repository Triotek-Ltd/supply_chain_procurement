"""Workflow service seed for supplier_profile."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "supplier_profile"
ARCHETYPE = "master"
INITIAL_STATE = 'active'
STATES = ['active', 'suspended', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}, 'update': {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}, 'review': {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}, 'suspend': {'allowed_in_states': ['active', 'suspended'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['active', 'suspended'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain supplier master quality, review vendor performance, and resolve supplier issues proactively', 'actors': ['vendor manager', 'reviewer', 'legal/procurement owner'], 'start_condition': 'a supplier is onboarded or reviewed', 'ordered_steps': ['Create or update the supplier profile.'], 'primary_actions': ['create', 'update', 'review'], 'primary_transitions': ['supplier_profile: draft -> active'], 'downstream_effects': ['supports sourcing, purchase control, and risk management'], 'action_actors': {'create': ['vendor manager'], 'update': ['vendor manager'], 'review': ['reviewer'], 'archive': ['legal/procurement owner']}}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return cast(str | None, rule.get("transitions_to"))

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'entity_lifecycle', 'case_management': False}
