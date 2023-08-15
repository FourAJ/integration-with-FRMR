from frmr_backend.module.frmro import frmro


def getRequestParams():
    return {
        0: getFuncParamsMr('/person'),
        1: getFuncParamsList('/person/list'),
        2: getFuncParams('/person/common'),
        3: getFuncParamsMr('/person/prof'),
        4: getFuncParams('/person/postgraduate'),
        5: getFuncParams('/person/ext'),
        6: getFuncParams('/person/cert'),
        7: getFuncParamsMr('/person/accreditation'),
        8: getFuncParams('/person/qualification'),
        9: getFuncParamsLastName('/person/card'),
        10: getFuncParams('/person/nomination'),
        11: getFuncParams('/person/organization'),
        12: getFuncParamsMr('/person/full')
    }


def getFuncParams(endpoint: str):
    return {
        'endpoint': endpoint,
        'params': {
            'str': ['mo', 'oid', 'snils', 'serial', 'number'],
            'int': ['documentId'],
            'date': ['passDate']
        }
    }


def getFuncParamsMr(endpoint: str):
    return {
        'endpoint': endpoint,
        'params': {
            'str': ['mo', 'oid', 'snils', 'serial', 'number'],
            'bool': ['mr'],
            'int': ['documentId'],
            'date': ['passDate']
        },
    }


def getFuncParamsLastName(endpoint: str):
    return {
        'endpoint': endpoint,
        'params': {
            'str': ['mo', 'lastName', 'oid', 'snils', 'serial', 'number'],
            'int': ['documentId'],
            'date': ['passDate']
        }
    }


def getFuncParamsList(endpoint: str):
    return {
        'endpoint': endpoint,
        'params': {
            'str': ['mo'],
            'int': ['offset', 'limit']
        },
    }


def getResponseAPI(payload):
    api = frmro().personAPI()
    match payload['endpoint']:
        case '/person':
            return api.person().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                mr=None if payload['mr'] is None else bool(payload['mr']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/list':
            return api.list().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                limit=None if payload['limit'] is None else int(payload['limit']),
                offset=None if payload['offset'] is None else int(payload['offset'])
            )
        case '/person/common':
            return api.common().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/prof':
            return api.prof().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                mr=None if payload['mr'] is None else bool(payload['mr']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/postgraduate':
            return api.postgraduate().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/ext':
            return api.ext().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/cert':
            return api.cert().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/accreditation':
            return api.accreditation().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                mr=None if payload['mr'] is None else bool(payload['mr']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/qualification':
            return api.qualification().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/card':
            return api.card().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate']),
                lastName=None if payload['lastName'] is None else str(payload['lastName'])
            )
        case '/person/nomination':
            return api.nomination().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/organization':
            return api.organization().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )
        case '/person/full':
            return api.full().get(
                mo=None if payload['mo'] is None else str(payload['mo']),
                mr=None if payload['mr'] is None else bool(payload['mr']),
                oid=None if payload['oid'] is None else str(payload['oid']),
                snils=None if payload['snils'] is None else str(payload['snils']),
                documentId=None if payload['documentId'] is None else int(payload['documentId']),
                serial=None if payload['serial'] is None else str(payload['serial']),
                number=None if payload['number'] is None else str(payload['number']),
                passDate=None if payload['passDate'] is None else str(payload['passDate'])
            )


def getSpecification():
    return {
        0: {
            'name': 'mo',
            'type': 'str',
            'description': 'Идентификатор организации',
            'required': 'да | да, если указан mr'
        },
        1: {
            'name': 'mr',
            'type': 'bool',
            'description': 'Принадлежность к медицинскому работнику',
            'required': 'да'
        },
        2: {
            'name': 'oid',
            'type': 'str',
            'description': 'OID медицинского работника',
            'required': 'да, если не указан СНИЛС или ДУЛ'
        },
        3: {
            'name': 'snils',
            'type': 'str',
            'description': 'СНИЛС',
            'required': 'да, если не указан OID или ДУЛ'
        },
        4: {
            'name': 'documentId',
            'type': 'int',
            'description': 'Код документа, удостоверяющего личность',
            'required': 'да, если не указан OID или СНИЛС | и lastName'
        },
        5: {
            'name': 'serial',
            'type': 'str',
            'description': 'Серия документа, удостоверяющего личность',
            'required': 'нет'
        },
        6: {
            'name': 'number',
            'type': 'str',
            'description': 'Номер документа, удостоверяющего личность',
            'required': 'да, если указан DocumentId'
        },
        7: {
            'name': 'passDate',
            'type': 'date',
            'description': 'Дата выдачи документа, удостоверяющего личность',
            'required': 'нет'
        },
        8: {
            'name': 'offset',
            'type': 'int',
            'description': 'Количество записей, которые нужно пропустить',
            'required': 'нет'
        },
        9: {
            'name': 'limit',
            'type': 'int',
            'description': 'Количество записей, которые нужно получить. Не более 100',
            'required': 'нет'
        },
        10: {
            'name': 'lastName',
            'type': 'str',
            'description': 'Фамилия',
            'required': 'да, если не указан ДУЛ'
        }
    }