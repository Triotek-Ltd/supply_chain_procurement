"""Doc runtime hooks for pick_list."""

class DocRuntime:
    doc_key = "pick_list"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'start', 'complete', 'close', 'archive']
