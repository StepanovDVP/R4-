class RobotMessages:
    SUCCESS_CREATE = 'Robot {serial} created successfully'
    ERROR_INVALID_JSON = 'Invalid JSON format'


class RobotFormMessages:
    ERROR_INVALID_DATE = 'The creation date cannot be in the future.'
    ERROR_INVALID_MODEL = 'Модель должна содержать только буквы и цифры.'
    ERROR_INVALID_VERSION = 'Версия должна содержать только буквы и цифры.'


MAX_LEN_VERSION = 2
MAX_LEN_MODEL = 2
MAX_LEN_SERIAL = 5

PATTERN_CHECK = r'^[a-zA-Z0-9]+$'
