"""Doc runtime hooks for inventory_movement."""

class DocRuntime:
    doc_key = "inventory_movement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'post', 'reverse', 'archive']
