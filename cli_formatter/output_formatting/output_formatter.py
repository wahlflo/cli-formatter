import enum


class MessageType(enum.Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3


class Color(enum.Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7


RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"


COLOR_MAPPING = {
    MessageType.DEBUG: Color.BLUE,
    MessageType.INFO: Color.WHITE,
    MessageType.WARNING: Color.YELLOW,
    MessageType.ERROR: Color.RED
}


SYMBOL_MAPPINGS = {
    MessageType.DEBUG: '+',
    MessageType.INFO: '+',
    MessageType.WARNING: '!',
    MessageType.ERROR: '!'
}


VERBOSITY_LEVEL = 10


def set_verbosity_level(level: int):
    global VERBOSITY_LEVEL
    VERBOSITY_LEVEL = level


def __print(message: str, message_type: MessageType = MessageType.INFO, verbosity_level: int = 10):
    global VERBOSITY_LEVEL
    if verbosity_level < VERBOSITY_LEVEL:
        return
    start_color = COLOR_SEQ % (30 + COLOR_MAPPING[message_type].value)
    symbol = '[{}] '.format(SYMBOL_MAPPINGS[message_type])
    print(start_color + symbol + message + RESET_SEQ)


def debug(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.DEBUG, message=message, verbosity_level=verbosity_level)


def error(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.ERROR, message=message, verbosity_level=verbosity_level)


def warning(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.WARNING, message=message, verbosity_level=verbosity_level)


def info(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.INFO, message=message, verbosity_level=verbosity_level)


def colorize_string(text: str, color: Color) -> str:
    """ returns a colored strings """
    return COLOR_SEQ % (30 + color.value) + text + RESET_SEQ
