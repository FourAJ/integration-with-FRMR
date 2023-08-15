from frmr_backend.utils.BasePayload import PayloadTypeB


class Person(PayloadTypeB):
    def __init__(self, url: str, headers: dict):
        super().__init__(url, headers)
        self._endpoint: str = '/person'
