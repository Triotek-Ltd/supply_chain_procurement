"""Relation service seed for goods_receipt."""

from __future__ import annotations

from manifold.core.services.relation_resolution import RelationResolutionService


DOC_ID = "goods_receipt"
RELATED_DOCS = [{'doc_id': 'purchase_order', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'supplier_invoice', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'warehouse_record', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'stock_item', 'relation_type': 'related', 'show_in_related_panel': True}]
FETCH_RULES = [{'field_id': 'supplier', 'source_doc_id': 'supplier_invoice', 'fetch_profile': 'supplier_profile', 'fetch_fields': ['title', 'reference_no', 'supplier_code', 'email', 'phone', 'contact_email', 'contact_phone'], 'purpose': 'party_reference'}, {'field_id': 'warehouse', 'source_doc_id': 'warehouse_record', 'fetch_profile': 'supplier_profile', 'fetch_fields': ['title', 'reference_no', 'supplier_code', 'email', 'phone', 'contact_email', 'contact_phone'], 'purpose': 'relation_reference'}]

BORROWED_FIELDS = [{'description': 'order lines'}, {'description': 'supplier from purchase_order'}]

class RelationService:
    def _bridge(self, context: dict | None = None) -> RelationResolutionService | None:
        viewset = (context or {}).get("viewset")
        return RelationResolutionService(viewset) if viewset is not None else None

    def resolve_create_relations(self, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_create_relations(payload) if bridge else {"data": payload}

    def resolve_update_relations(self, instance, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_update_relations(instance, payload) if bridge else {"data": payload}

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.serialize_related(instance, serialized_data) if bridge else serialized_data

    def related_targets(self) -> list:
        return RELATED_DOCS

    def borrowed_field_notes(self) -> list:
        return [item.get("description") for item in BORROWED_FIELDS if isinstance(item, dict)]

    def relation_profile(self) -> dict:
        return {
            "related_docs": self.related_targets(),
            "borrowed_fields": self.borrowed_field_notes(),
            "fetch_rule_count": len(FETCH_RULES),
        }
