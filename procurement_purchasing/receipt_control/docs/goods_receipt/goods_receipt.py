"""Doc runtime hooks for goods_receipt."""

class DocRuntime:
    doc_key = "goods_receipt"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'submit', 'accept', 'reject', 'close', 'archive']
