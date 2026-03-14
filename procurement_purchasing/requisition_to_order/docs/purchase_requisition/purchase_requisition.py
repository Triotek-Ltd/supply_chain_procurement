"""Doc runtime hooks for purchase_requisition."""

class DocRuntime:
    doc_key = "purchase_requisition"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'convert', 'cancel', 'archive']
