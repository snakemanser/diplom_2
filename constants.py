URL = 'https://stellarburgers.nomoreparties.site'
CREATE_USER_DATA = {
"email": "test_bu4ka@yandex.ru",
"password": "123456",
"name": "Pudge"
}
CREATE_USER_DATA_NO_NAME = {
"email": "test_bu4ka@yandex.ru",
"password": "123456"
}
LOGIN_USER_DATA = {
"email": "test_bu4ka@yandex.ru",
"password": "123456"
}
WRONG_LOGIN_USER_DATA = {
"email": "QWE123QWEZXC@yandex.ru",
"password": "123456ASD"
}
PATCH_USER_DATA_EMAIL = {
"email": "test_bu4ka322@yandex.ru"
}
PATCH_USER_DATA_NAME = {
"name": "Pudge322"
}
PATCH_DELETE_DATA_EMAIL = {
"email": "test_bu4ka322@yandex.ru",
"password": "123456"
}
PATCH_DELETE_DATA_NAME = {
"email": "test_bu4ka@yandex.ru",
"password": "123456"
}

CREATE_ORDER_DATA = {
"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                "61c0c5a71d1f82001bdaaa6f"]
}
CREATE_ORDER_DATA_WRONG_HASH = {
"ingredients": ["61c0c5a71d1f820013",
                "61c0c5a71d1f820012"]
}
CREATE_ORDER_DATA_EMPTY = {
"ingredients": []
}

