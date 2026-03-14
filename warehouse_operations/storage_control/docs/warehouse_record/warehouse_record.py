"""Doc runtime hooks for warehouse_record."""

class DocRuntime:
    doc_key = "warehouse_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
