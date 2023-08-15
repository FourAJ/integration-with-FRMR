import json
import requests
from datetime import datetime as dt


class Response400(requests.models.Response):
    def __init__(self, message):
        super().__init__()
        self.status_code = 400
        self.headers['Content-Type'] = 'application/json'
        self._content = json.dumps({
            "timestamp": dt.now().strftime("%Y-%m-%dT%H:%M:%S.%f+03:00"),
            "code": 400,
            "reasonPhrase": "Bad Request",
            "message": message
        }).encode('utf-8')


class Response500(requests.models.Response):
    def __init__(self):
        super().__init__()
        self.status_code = 500
        self.headers['Content-Type'] = 'application/json'
        self._content = json.dumps({
            "timestamp": dt.now().strftime("%Y-%m-%dT%H:%M:%S.%f+03:00"),
            "code": 500,
            "reasonPhrase": "Internal Server Error",
            "message": "An unexpected error occurred on the server."
        }).encode('utf-8')
