"""Doc runtime hooks for transport_booking."""

class DocRuntime:
    doc_key = "transport_booking"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'confirm', 'cancel', 'archive']
