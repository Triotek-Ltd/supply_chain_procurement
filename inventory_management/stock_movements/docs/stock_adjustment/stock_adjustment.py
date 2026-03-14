"""Doc runtime hooks for stock_adjustment."""

class DocRuntime:
    doc_key = "stock_adjustment"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'apply', 'close', 'archive']
