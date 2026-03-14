"""Doc runtime hooks for storage_bin."""

class DocRuntime:
    doc_key = "storage_bin"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
