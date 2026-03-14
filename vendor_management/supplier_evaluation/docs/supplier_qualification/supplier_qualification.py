"""Doc runtime hooks for supplier_qualification."""

class DocRuntime:
    doc_key = "supplier_qualification"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'reject', 'close', 'archive']
