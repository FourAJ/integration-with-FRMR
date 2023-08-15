from frmr_backend.utils.RequestSender import RequestSender
from frmr_backend.utils.ResponseSender import Response400
from requests.models import Response


class Card(RequestSender):
    def get(self, mo: str = None, lastName: str = None, oid: str = None, snils: str = None,
            documentId: int = None, serial: str = None, number: str = None, passDate: str = None) -> Response:
        """

        Название   | Описание                                             | обязательность
        :param lastName: фамилия                                          да, если не указан ДУЛ
        :param mo: идентификатор организации                              нет
        :param oid: OID медицинского работника                            да, если не указан СНИЛС или ДУЛ
        :param snils: СНИЛС                                               да, если не указан oid или ДУЛ
        :param documentId: Код документа, удостоверяющего личность        да, если не указан lastName и (oid, или СНИЛС)
        :param serial: Серия документа, удостоверяющего личность          нет
        :param number: Номер документа, удостоверяющего личность          да, если указан documentId
        :param passDate: Дата выдачи документа, удостоверяющего личность  нет
        :return:
        """
        # payload: dict = {
        #     'mo': mo,
        #     'lastName': lastName,
        #     'oid': oid,
        #     'snils': snils,
        #     'documentId': documentId,
        #     'serial': serial,
        #     'number': number,
        #     'passDate': passDate
        # }
        payload: dict = {}

        if mo:
            payload['mo']: str = mo
        if oid:
            payload['oid']: str = oid
        if snils:
            payload['snils']: str = snils
        if documentId:
            payload['documentId']: int = documentId
            if number:
                payload['number']: str = number
            else:
                return Response400("number is missing or was not provided.")
            if serial:
                payload['serial']: str = serial
        if lastName:
            payload['lastName']: str = lastName
        if not (documentId or lastName):
            return Response400('You need to provide the lastName or documentId.')
        if not (oid or snils or documentId):
            return Response400("You need to provide the oid, snils, or documentId.")
        if passDate:
            payload['passDate']: int = passDate
        return self._sendGetRequest(endpoint='/person/card', payload=payload)
