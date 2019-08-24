import requests

def vk_api_requests(user_token, *args, **kwargs):
    """Функция для обращения к API Вконтакте, возвращает json в зависимости от методаы"""

    COUNT = '5'
    METHOD_NAME = kwargs['method']
    VERSION_API = '5.101'
    FIELDS = 'photo_100, domain'
    ORDER = 'random'

    response = requests.get(
        "https://api.vk.com/method/{METHOD_NAME}?&fields={FIELDS}&count={COUNT}&order={ORDER}&access_token={user_token}&v={VERSION_API}".format(
            ORDER=ORDER,
            FIELDS=FIELDS,
            METHOD_NAME=METHOD_NAME,
            COUNT=COUNT,
            user_token=user_token,
            VERSION_API=VERSION_API
        ))

    return response.json()
