"""Doc runtime hooks for stock_item."""

class DocRuntime:
    doc_key = "stock_item"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
