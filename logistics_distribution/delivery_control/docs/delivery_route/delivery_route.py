"""Doc runtime hooks for delivery_route."""

class DocRuntime:
    doc_key = "delivery_route"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'optimize', 'dispatch', 'close', 'archive']
