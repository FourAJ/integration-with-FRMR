from frmr_backend.utils.config import JWT_FRMR_API_TOKEN
from frmr_backend.module.person.personAPI import PersonAPI


class frmro:
    def __init__(self):
        """

         Устанавливает заголовки запроса, включая авторизацию с помощью JWT-токена.
        """
        self.__headers: dict = {
            'Authorization': f'Bearer {JWT_FRMR_API_TOKEN}'
        }

    def personAPI(self) -> PersonAPI:
        """

        :return: PersonAPI: Экземпляр класса PersonAPI, связанный с заголовками запроса объекта frmroAPI.
        """
        return PersonAPI(self.__headers)
