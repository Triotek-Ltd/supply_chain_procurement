"""Doc runtime hooks for supplier_profile."""

class DocRuntime:
    doc_key = "supplier_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'suspend', 'archive']
