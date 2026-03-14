"""Doc runtime hooks for vendor_review."""

class DocRuntime:
    doc_key = "vendor_review"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'archive']
