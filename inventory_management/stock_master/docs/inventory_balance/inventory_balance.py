"""Doc runtime hooks for inventory_balance."""

class DocRuntime:
    doc_key = "inventory_balance"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'archive']
