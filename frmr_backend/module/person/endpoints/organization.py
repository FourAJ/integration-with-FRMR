from frmr_backend.utils.BasePayload import PayloadTypeA


class Organization(PayloadTypeA):
    def __init__(self, url: str, headers: dict):
        super().__init__(url, headers)
        self._endpoint: str = '/person/organization'
