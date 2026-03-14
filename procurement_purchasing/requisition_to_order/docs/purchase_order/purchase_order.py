"""Doc runtime hooks for purchase_order."""

class DocRuntime:
    doc_key = "purchase_order"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'issue', 'receive', 'bill', 'close', 'archive']
