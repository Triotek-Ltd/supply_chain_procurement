"""Doc runtime hooks for procurement_request."""

class DocRuntime:
    doc_key = "procurement_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'issue', 'close', 'archive']
