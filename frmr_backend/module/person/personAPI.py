from frmr_backend.module.person.endpoints.common import Common
from frmr_backend.module.person.endpoints.postgraduate import Postgraduate
from frmr_backend.module.person.endpoints.ext import Ext
from frmr_backend.module.person.endpoints.cert import Cert
from frmr_backend.module.person.endpoints.qualification import Qualification
from frmr_backend.module.person.endpoints.nomination import Nomination
from frmr_backend.module.person.endpoints.organization import Organization
from frmr_backend.module.person.endpoints.person import Person
from frmr_backend.module.person.endpoints.prof import Prof
from frmr_backend.module.person.endpoints.accreditation import Accreditation
from frmr_backend.module.person.endpoints.full import Full
from frmr_backend.module.person.endpoints.card import Card
from frmr_backend.module.person.endpoints.list import List
from frmr_backend.utils.config import BaseURLfrmr


class PersonAPI:
    """
    Класс для работы с API ФРМР.

    Аргументы:
    - headers (dict): Заголовки запроса в виде словаря.

    Примечания:
    - Класс предоставляет методы для работы с различными типами данных.
    - Все методы возвращают экземпляры соответствующих классов API с заданными заголовками и базовым URL.
    """
    def __init__(self, headers):
        """

        :param headers:
        """
        self.__headers: dict = headers
        self.__url: str = f'{BaseURLfrmr}'

    # Type A
    def common(self) -> Common:
        return Common(url=self.__url, headers=self.__headers)

    def postgraduate(self) -> Postgraduate:
        return Postgraduate(url=self.__url, headers=self.__headers)

    def ext(self) -> Ext:
        return Ext(url=self.__url, headers=self.__headers)

    def cert(self) -> Cert:
        return Cert(url=self.__url, headers=self.__headers)

    def qualification(self) -> Qualification:
        return Qualification(url=self.__url, headers=self.__headers)

    def nomination(self) -> Nomination:
        return Nomination(url=self.__url, headers=self.__headers)

    def organization(self) -> Organization:
        return Organization(url=self.__url, headers=self.__headers)

    # type B

    def person(self) -> Person:
        return Person(url=self.__url, headers=self.__headers)

    def prof(self) -> Prof:
        return Prof(url=self.__url, headers=self.__headers)

    def accreditation(self) -> Accreditation:
        return Accreditation(url=self.__url, headers=self.__headers)

    def full(self) -> Full:
        return Full(url=self.__url, headers=self.__headers)

    # Type Custom

    def card(self) -> Card:
        return Card(url=self.__url, headers=self.__headers)

    def list(self) -> List:
        return List(url=self.__url, headers=self.__headers)
