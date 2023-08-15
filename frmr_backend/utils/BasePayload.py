from frmr_backend.utils.RequestSender import RequestSender
from frmr_backend.utils.ResponseSender import Response400
from frmr_backend.utils.helpers import getTime
from requests.models import Response
from datetime import datetime


class PayloadTypeA(RequestSender):
    def get(self, mo: str = None, oid: str = None, snils: str = None,
            documentId: int = None, serial: str = None, number: str = None, passDate: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type A.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.

        Название   | Описание                                              | обязательность
        :param mo: идентификатор организации                                да
        :param oid: OID медицинского работника                              да, если не указан СНИЛС или ДУЛ
        :param snils: СНИЛС                                                 да, если не указан OID или ДУЛ
        :param documentId: Код документа, удостоверяющего личность          да, если не указан OID или СНИЛС
        :param serial: Серия документа, удостоверяющего личность            нет
        :param number: Номер документа, удостоверяющего личность            да, если указан DocumentId
        :param passDate: Дата выдачи документа, удостоверяющего личность    нет
        :return: Объект ответа на GET-запрос
        """
        payload: dict = {}

        if mo:
            payload['mo']: str = mo
        else:
            return Response400("mo is missing or was not provided.")
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
            if passDate:
                date = getTime(passDate)
                if date is None:
                    return Response400('Error passDate is missing or was not provided.')
                payload['passDate']: datetime = date
        if not (oid or snils or documentId):
            return Response400("You need to provide the oid, snils, or documentId.")

        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)


class PayloadTypeB(RequestSender):
    def get(self, *, mo: str = None, mr: bool = False, oid: str = None, snils: str = None,
            documentId: int = None, serial: str = None, number: str = None, passDate: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type B.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.

        Название   | Описание                                              | обязательность
        :param mo: идентификатор организации                                да, если mr=True
        :param mr: принадлежность к медицинскому работнику                  да
        :param oid: OID медицинского работника                              да, если не указан СНИЛС или ДУЛ
        :param snils: СНИЛС                                                 да, если не указан OID или ДУЛ
        :param documentId: Код документа, удостоверяющего личность          да, если не указан OID или СНИЛС
        :param serial: Серия документа, удостоверяющего личность            нет
        :param number: Номер документа, удостоверяющего личность            да, если указан DocumentId
        :param passDate: Дата выдачи документа, удостоверяющего личность    нет
        :return: Объект ответа на GET-запрос
        """

        payload: dict = {'mr': mr}

        if mo:
            payload['mo']: str = mo
        else:
            if mr:
                return Response400("mo is missing or was not provided.")
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
            if passDate:
                date = getTime(passDate)
                if date is None:
                    return Response400('Error retrieving passDate, incorrect input data format.')
                payload['passDate']: datetime = date
        if not (oid or snils or documentId):
            return Response400("You need to provide the oid, snils, or documentId.")

        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)


class PayloadTypeC(RequestSender):
    def get(self, oid: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type C.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.
        :param oid:
        :return:
        """
        if oid:
            payload: dict = {'oid': oid}
        else:
            return Response400("oid is missing or was not provided.")
        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)


class PayloadTypeD(RequestSender):
    def get(self, oid: str = None, entityId: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type D.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.
        :param oid:
        :param entityId:
        :return:
        """
        if oid and entityId:
            payload: dict = {
                'oid': oid,
                'entityId': entityId
            }
        else:
            return Response400("oid or entityId is missing or was not provided.")
        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)


class PayloadTypeE(RequestSender):
    def get(self, oid: str = None, guid: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type E.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.
        :param oid:
        :param guid:
        :return:
        """
        if oid and guid:
            payload: dict = {
                'oid': oid,
                'guid': guid
            }
        else:
            return Response400("oid or guid is missing or was not provided.")
        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)


class PayloadTypeF(RequestSender):
    def get(self, eo: str = None) -> Response:
        """
        Отправляет GET-запрос с заданным payload type F.

        - Создает словарь payload на основе переданных аргументов.
        - Вызывает метод _sendGetRequest родительского класса, передавая текущий путь _endpoint и созданный payload.
        :param eo:
        :return:
        """
        if eo:
            payload: dict = {'eo': eo}
        else:
            return Response400("eo is missing or was not provided.")
        return self._sendGetRequest(endpoint=self._endpoint, payload=payload)
