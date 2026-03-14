"""Doc runtime hooks for vendor_contract."""

class DocRuntime:
    doc_key = "vendor_contract"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'renew', 'archive']
