class RobotMessages:
    SUCCESS_CREATE = 'Robot {serial} created successfully'
    ERROR_INVALID_JSON = 'Invalid JSON format'


class RobotFormMessages:
    ERROR_INVALID_DATE = 'The creation date cannot be in the future.'
    ERROR_INVALID_MODEL = 'Модель должна содержать только буквы и цифры.'
    ERROR_INVALID_VERSION = 'Версия должна содержать только буквы и цифры.'


REQUEST_WAIT_LIST = 'Ваш запрос добавлен в лист ожидания.'
ROBOT_EXIST = 'Робот в наличии! Поторопитесь его купить!'

EXM_EMAIL = 'star_wars@gmail.com'
EXM_MODEL = 'Модель (например, R2)'
EXM_VERSION = 'Версия (например, D2)'

MAX_LEN_VERSION = 2
MAX_LEN_MODEL = 2
MAX_LEN_SERIAL = 5
MAX_LEN_EMAIL = 254

PATTERN_CHECK = r'^[a-zA-Z0-9]+$'

MODEL = 'Модель'
VERSION = 'Версия'
COUNT_LAST_WEEK = 'Количество за неделю'
HEADERS_EXCEL = [
    MODEL, VERSION, COUNT_LAST_WEEK
]
CONTENT_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
