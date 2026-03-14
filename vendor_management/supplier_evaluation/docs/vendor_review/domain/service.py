"""Business-domain service seed for Vendor Review."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'posting_flow', 'supports_reconciliation': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['draft', 'reviewed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'posting_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'posting_date': 'posting_date', 'supplier': 'party_reference'}, 'search_fields': ['title', 'reference_no', 'description', 'review_code', 'supplier', 'review_period'], 'list_columns': ['title', 'reference_no', 'posting_date', 'workflow_state'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'reviewed', 'archived'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'review': 'reviewed', 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'maintain supplier master quality, review vendor performance, and resolve supplier issues proactively', 'actors': ['vendor manager', 'reviewer', 'legal/procurement owner'], 'start_condition': 'a supplier is onboarded or reviewed', 'ordered_steps': ['Review supplier performance and compliance status.'], 'primary_actions': ['create', 'review', 'close'], 'primary_transitions': ['vendor_review: opened -> reviewed -> closed'], 'downstream_effects': ['supports sourcing, purchase control, and risk management']}

class DomainService:
    doc_id = "vendor_review"
    archetype = "ledger"
    doc_kind = "ledger"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
