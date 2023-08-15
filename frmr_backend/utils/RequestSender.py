import requests
from requests.models import Response
from requests.exceptions import ConnectionError
from frmr_backend.utils.ResponseSender import Response500
from frmr_backend.utils.config import MODULE_API_URL, JWT_MODULE_API_TOKEN


class RequestSender:
    def __init__(self, url: str, headers: dict):
        """
        :param url: Базовый URL для отправки запросов
        :param headers: Заголовки запроса в виде словаря
        """
        self.__baseURL: str = url
        self.__headers: dict = headers
        self._endpoint: str = ''

    def _sendGetRequest(self, endpoint: str, payload: dict) -> Response:
        """
        Отправляет GET-запрос к указанному endpoint с заданным payload

        :param endpoint: Путь для отправки GET-запроса
        :param payload: Параметры запроса в виде словаря
        :return: Объект ответа на GET-запрос
        """
        url: str = self.__baseURL + endpoint
        try:
            response = requests.get(url=url, headers=self.__headers, params=payload)
            if response.status_code == 200:
                requests.post(
                    url=f'{MODULE_API_URL}{endpoint}',
                    json=response.json()['content'],
                    params=payload,
                    headers={
                        'Authorization': f'Bearer {JWT_MODULE_API_TOKEN}'
                    }
                )
            return response
        except ConnectionError:
            return Response500()

    def _sendPostRequest(self, endpoint, payload, data) -> Response:
        """
        Отправляет POST-запрос к указанному endpoint с заданным payload

        :param endpoint: Путь для отправки POST-запроса
        :param payload: Параметры запроса в виде словаря
        :return: Объект ответа на POST-запрос
        """
        url: str = self.__baseURL + endpoint
        try:
            return requests.post(url=url, headers=self.__headers, params=payload, json=data)
        except ConnectionError:
            return Response500()

    def _sendPutRequest(self, endpoint, payload) -> Response:
        """
        Отправляет PUT-запрос к указанному endpoint с заданным payload

        :param endpoint: Путь для отправки PUT-запроса
        :param payload: Параметры запроса в виде словаря
        :return: Объект ответа на PUT-запрос
        """
        url: str = self.__baseURL + endpoint
        try:
            return requests.put(url=url, headers=self.__headers, params=payload)
        except ConnectionError:
            return Response500()

    def _sendDeleteRequest(self, endpoint, payload) -> Response:
        """
        Отправляет DELETE-запрос к указанному endpoint с заданным payload

        :param endpoint: Путь для отправки DELETE-запроса
        :param payload: Параметры запроса в виде словаря
        :return: Объект ответа на DELETE-запрос
        """
        url: str = self.__baseURL + endpoint
        try:
            return requests.delete(url=url, headers=self.__headers, params=payload)
        except ConnectionError:
            return Response500()
