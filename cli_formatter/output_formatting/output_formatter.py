import enum
import sys
import os
import platform


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
    MessageType.INFO: None,                 # None is no color / neutral
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


def debug(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.DEBUG, message=message, verbosity_level=verbosity_level)


def error(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.ERROR, message=message, verbosity_level=verbosity_level, output_handle=sys.stderr)


def warning(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.WARNING, message=message, verbosity_level=verbosity_level)


def info(message: str, verbosity_level: int = 10):
    __print(message_type=MessageType.INFO, message=message, verbosity_level=verbosity_level)


def __output_supports_ansi(output_handle) -> bool:
    """ returns True if the output handle supports ANSI colors otherwise False """
    if (hasattr(output_handle, "isatty") and output_handle.isatty()) or ('TERM' in os.environ and os.environ['TERM'] == 'ANSI'):
        if platform.system() == 'Windows' and not ('TERM' in os.environ and os.environ['TERM'] == 'ANSI'):
            return False
        else:
            return True
    else:
        return False


def colorize_string(text: str, color: Color, output_handle=sys.stdout) -> str:
    """ returns a colored strings """
    if color is not None and __output_supports_ansi(output_handle=output_handle):
        return COLOR_SEQ % (30 + color.value) + text + RESET_SEQ
    else:
        return text


def __print(message: str, message_type: MessageType = MessageType.INFO, verbosity_level: int = 10, output_handle=sys.stdout):
    global VERBOSITY_LEVEL
    if verbosity_level < VERBOSITY_LEVEL:
        return
    color = COLOR_MAPPING[message_type]
    symbol = '[{}] '.format(SYMBOL_MAPPINGS[message_type])
    output_text = colorize_string(text=symbol + message, color=color, output_handle=output_handle)
    print(output_text, file=output_handle)


def print_headline_banner(headline: str, color_border=None, color_headline=Color.BLUE):
    colorized_headline = colorize_string(text=headline, color=color_headline)
    colorized_headline_border = colorize_string(text=' ' + (len(headline) + 8) * '=', color=color_border)
    print(colorized_headline_border)
    print(colorize_string(text=' ||  ', color=color_border) + colorized_headline + colorize_string(text='  ||', color=color_border))
    print(colorized_headline_border)
