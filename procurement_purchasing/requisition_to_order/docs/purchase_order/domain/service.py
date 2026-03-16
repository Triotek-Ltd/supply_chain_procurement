"""Business-domain service seed for Purchase Order."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'transaction_flow', 'supports_submission': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': True}, 'integration_profile': {'external_sync_enabled': True, 'tracks_external_refs': True}, 'lifecycle_states': ['draft', 'submitted', 'partially_received', 'received', 'billed', 'closed', 'archived'], 'is_transactional': True}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state', 'transaction_date'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'transaction_date': 'transaction_date', 'party': 'primary_party', 'currency': 'currency_code', 'total_amount': 'total_amount', 'supplier': 'party_reference', 'order_date': 'schedule_marker', 'schedule_date': 'schedule_marker', 'totals': 'structured_payload', 'related_purchase_requisition': 'relation_collection', 'related_goods_receipt': 'relation_collection', 'related_supplier_invoice': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'order_code', 'supplier', 'order_date'], 'list_columns': ['title', 'reference_no', 'transaction_date', 'party', 'total_amount', 'workflow_state'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'submitted', 'partially_received', 'received', 'billed', 'closed', 'archived'], 'terminal_states': ['closed', 'archived'], 'action_targets': {'create': None, 'review': None, 'approve': None, 'issue': None, 'receive': None, 'bill': None, 'close': 'closed', 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'convert an internal purchasing need into an approved purchase order issued to the right supplier', 'actors': ['requesting department', 'procurement officer', 'reviewer', 'approver', 'supplier'], 'start_condition': 'a department raises a purchasing need', 'ordered_steps': ['Create and issue the purchase order.', 'Record the committed procurement obligation.'], 'primary_actions': ['create', 'review', 'approve', 'issue'], 'primary_transitions': ['purchase_order: draft -> submitted -> approved'], 'downstream_effects': ['purchase orders feed goods receipt, supplier invoice matching, and vendor performance tracking'], 'action_actors': {'create': ['requesting department'], 'review': ['reviewer'], 'approve': ['approver'], 'issue': ['requesting department'], 'close': ['requesting department'], 'archive': ['requesting department']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['purchase orders feed goods receipt, supplier invoice matching, and vendor performance tracking'], 'related_docs': ['purchase_requisition', 'goods_receipt', 'supplier_invoice', 'supplier_profile'], 'action_targets': {'create': None, 'review': None, 'approve': None, 'issue': None, 'receive': None, 'bill': None, 'close': 'closed', 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "purchase_order"
    archetype = "transaction"
    doc_kind = "transaction"

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

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
