"""Workflow service seed for goods_receipt."""

from __future__ import annotations


DOC_ID = "goods_receipt"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'submitted', 'completed', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': 'submitted'}, 'accept': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'reject': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'completed'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive goods into warehouse storage, put them away correctly, pick them for orders, and keep warehouse records current', 'actors': ['warehouse supervisor', 'receiving operator', 'picker', 'putaway operator'], 'start_condition': 'goods are received or outgoing orders require warehouse execution', 'ordered_steps': ['Receive goods into the warehouse and assign a storage destination.'], 'primary_actions': ['create', 'assign'], 'primary_transitions': [], 'downstream_effects': ['warehouse execution feeds shipment, fulfillment, replenishment, and inventory accuracy'], 'action_actors': {'create': ['warehouse supervisor'], 'review': ['receiving operator'], 'submit': ['warehouse supervisor'], 'reject': ['warehouse supervisor'], 'close': ['warehouse supervisor'], 'archive': ['warehouse supervisor']}}

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
