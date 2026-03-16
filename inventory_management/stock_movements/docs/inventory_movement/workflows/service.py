"""Workflow service seed for inventory_movement."""

from __future__ import annotations


DOC_ID = "inventory_movement"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'approved', 'posted', 'reversed', 'archived']
TERMINAL_STATES = ['reversed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': 'approved'}, 'post': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': None}, 'reverse': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': 'reversed'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'posted'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, verify, store, monitor, count, reconcile, and replenish inventory accurately', 'actors': ['storekeeper', 'warehouse operator', 'inventory controller', 'reviewer'], 'start_condition': 'stock is received, moved, counted, or adjusted', 'ordered_steps': ['Record inventory movement into storage.', 'Reconcile physical count variances and apply adjustments.'], 'primary_actions': ['create', 'review', 'approve', 'post', 'apply', 'close'], 'primary_transitions': ['inventory_movement: draft -> approved -> posted'], 'downstream_effects': ['inventory availability feeds purchasing, warehouse execution, logistics, and production planning'], 'action_actors': {'create': ['storekeeper'], 'review': ['reviewer'], 'approve': ['reviewer'], 'post': ['reviewer'], 'reverse': ['storekeeper'], 'archive': ['storekeeper']}}

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
        return rule.get("transitions_to")

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
        return {'mode': 'transaction_flow', 'supports_submission': True}
