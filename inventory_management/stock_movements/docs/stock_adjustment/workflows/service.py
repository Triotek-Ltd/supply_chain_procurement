"""Workflow service seed for stock_adjustment."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "stock_adjustment"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'reviewed', 'approved', 'applied', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'approved'}, 'apply': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'reviewed', 'approved', 'applied'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, verify, store, monitor, count, reconcile, and replenish inventory accurately', 'actors': ['storekeeper', 'warehouse operator', 'inventory controller', 'reviewer'], 'start_condition': 'stock is received, moved, counted, or adjusted', 'ordered_steps': ['Monitor stock levels and trigger recount or replenishment as needed.', 'Reconcile physical count variances and apply adjustments.'], 'primary_actions': ['review', 'create', 'approve', 'apply', 'close'], 'primary_transitions': ['stock_adjustment: opened', 'stock_adjustment: opened -> reviewed -> approved -> applied -> closed'], 'downstream_effects': ['inventory availability feeds purchasing, warehouse execution, logistics, and production planning'], 'action_actors': {'create': ['storekeeper'], 'review': ['reviewer'], 'approve': ['reviewer'], 'close': ['storekeeper'], 'archive': ['storekeeper']}}

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
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
