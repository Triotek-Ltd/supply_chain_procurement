"""Doc runtime hooks for delivery_confirmation."""

class DocRuntime:
    doc_key = "delivery_confirmation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
