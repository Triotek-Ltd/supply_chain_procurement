"""Doc runtime hooks for putaway_task."""

class DocRuntime:
    doc_key = "putaway_task"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'start', 'complete', 'close', 'archive']
