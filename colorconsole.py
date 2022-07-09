from termcolor import colored
from typing import Iterable, Literal, Optional
from os import system
from sys import platform

Colors = Literal['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
Highlights = Literal['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']
Attributes = Literal['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']

if platform.lower() == 'win32': 
    system('color')

def error(*text: Iterable[str], brackets: Optional[bool]=True, end: Optional[str]="\n") -> None:
    """Print the 'text' in red and if 'brackets' is True, print '[ERROR]' before the 'text'."""
    before = ''
    if brackets: before = colored('[ERROR] ', 'red', attrs=['bold'])
    print(before + colored(" ".join(text), 'red'), end=end)

def warning(*text: Iterable[str], brackets: Optional[bool]=True, end: Optional[str]="\n") -> None:
    """Print the 'text' in yellow and if 'brackets' is True, print '[WARNING]' before the 'text'."""
    before = ''
    if brackets: before = colored('[WARNING] ', 'yellow', attrs=['bold'])
    print(before + colored(" ".join(text), 'yellow'), end=end)

def info(*text: Iterable[str], brackets: Optional[bool]=True, end: Optional[str]="\n") -> None:
    """Print the 'text' in blue and if 'brackets' is True, print '[INFO]' before the 'text'."""
    before = ''
    if brackets: before = colored('[INFO] ', 'blue', attrs=['bold'])
    print(before + colored(" ".join(text), 'blue'), end=end)

def success(*text: Iterable[str], brackets: Optional[bool]=True, end: Optional[str]="\n") -> None:
    """Print the 'text' in green and if 'brackets' is True, print '[SUCCESS]' before the 'text'."""
    before = ''
    if brackets: before = colored('[SUCCESS] ', 'green', attrs=['bold'])
    print(before + colored(" ".join(text), 'green'), end=end)

def cprint(*text: Iterable[str], color: Optional[Colors]='white', highlight: Optional[Highlights]=None, attributes: Optional[Iterable[Attributes]]=None, end: Optional[str]="\n") -> None:
    """Print colorize text.

    Available colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.
    """
    print(colored(" ".join(text), color, highlight, attributes), end=end)

def colorize(text: str, color: Colors, highlight: Optional[Highlights]=None, attributes: Optional[Iterable[Attributes]]=None) -> str:
    """Colorize text.

    Available colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.
    """
    return colored(text, color, highlight, attributes)

if __name__ == '__main__':
    error("This is an error...")
    warning("This is a warning...")
    info("This is an info...")
    success("This is a success...")
    msg = "Hello World"
    cprint("message:", msg + ".", color="magenta", attributes=["bold"])
    print(colorize(f"message: {msg}.", "magenta", None, ["bold"]))