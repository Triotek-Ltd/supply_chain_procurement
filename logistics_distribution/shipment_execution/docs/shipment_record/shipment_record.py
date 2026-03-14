"""Doc runtime hooks for shipment_record."""

class DocRuntime:
    doc_key = "shipment_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'pack', 'dispatch', 'deliver', 'close', 'archive']
