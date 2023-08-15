from frmr_backend.utils.RequestSender import RequestSender
from frmr_backend.utils.ResponseSender import Response400
from requests.models import Response


class List(RequestSender):
    def get(self, *, mo: str = None, offset: int = None, limit: int = None) -> Response:
        """

        Название   | Описание                                                       | обязательность
        :param mo: идентификатор организации                                        да
        :param offset: количество записей, которые нужно пропустить                 нет
        :param limit: количество записей, которые нужно получить. Максимум - 100    нет ( не более 100 записей )
        :return:
        """
        payload: dict = {}
        if mo:
            payload['mo']: str = mo
        else:
            return Response400("mo is missing or was not provided.")
        if offset:
            payload['offset']: int = offset
        if limit:
            payload['limit']: int = min(limit, 100)

        return self._sendGetRequest(endpoint='/person/list', payload=payload)
