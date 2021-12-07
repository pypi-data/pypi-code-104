import sys
from collections import Counter

import lxml.html

from . import constants
from . import t

messages: t.Set[str]
messages = set()

messageCounts: t.Dict[str, int]
messageCounts = Counter()


def p(msg, sep=None, end=None):
    if constants.quiet == float("infinity"):
        return
    if isinstance(msg, tuple):
        msg, ascii = msg
    else:
        ascii = msg.encode("ascii", "replace").decode()
    if constants.asciiOnly:
        msg = ascii
    try:
        print(msg, sep=sep, end=end)
    except UnicodeEncodeError:
        if ascii is not None:
            print(ascii, sep=sep, end=end)
        else:
            warning = formatMessage(
                "warning",
                "Your console does not understand Unicode.\n  Messages may be slightly corrupted.",
            )
            if warning not in messages:
                print(warning)
                messages.add(warning)
            print(msg.encode("ascii", "xmlcharrefreplace"), sep=sep, end=end)


def die(msg, el=None, lineNum=None):
    if lineNum is None and el is not None and el.get("line-number"):
        lineNum = el.get("line-number")
    msg = formatMessage("fatal", msg, lineNum=lineNum)
    if msg not in messages:
        messageCounts["fatal"] += 1
        messages.add(msg)
        if constants.quiet < 3:
            p(msg)
    if constants.errorLevelAt("fatal"):
        errorAndExit()


def linkerror(msg, el=None, lineNum=None):
    if lineNum is None and el is not None and el.get("line-number"):
        lineNum = el.get("line-number")
    suffix = ""
    if el is not None:
        if el.get("bs-autolink-syntax"):
            suffix = "\n" + el.get("bs-autolink-syntax")
        else:
            suffix = "\n" + lxml.html.tostring(el, with_tail=False, encoding="unicode")
    msg = formatMessage("link", msg + suffix, lineNum=lineNum)
    if msg not in messages:
        messageCounts["linkerror"] += 1
        messages.add(msg)
        if constants.quiet < 2:
            p(msg)
    if constants.errorLevelAt("link-error"):
        errorAndExit()


def warn(msg, el=None, lineNum=None):
    if lineNum is None and el is not None and el.get("line-number"):
        lineNum = el.get("line-number")
    msg = formatMessage("warning", msg, lineNum=lineNum)
    if msg not in messages:
        messageCounts["warning"] += 1
        messages.add(msg)
        if constants.quiet < 1:
            p(msg)
    if constants.errorLevelAt("warning"):
        errorAndExit()


def say(msg):
    if constants.quiet < 1:
        p(formatMessage("message", msg))


def success(msg):
    if constants.quiet < 4:
        p(formatMessage("success", msg))


def failure(msg):
    if constants.quiet < 4:
        p(formatMessage("failure", msg))


def resetSeenMessages():
    global messages
    messages = set()
    global messageCounts
    messageCounts = Counter()


def printColor(text, color="white", *styles):
    if constants.printMode == "console":
        colorsConverter = {
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "magenta": 35,
            "cyan": 36,
            "light gray": 37,
            "dark gray": 90,
            "light red": 91,
            "light green": 92,
            "light yellow": 93,
            "light blue": 94,
            "light magenta": 95,
            "light cyan": 96,
            "white": 97,
        }
        stylesConverter = {
            "normal": 0,
            "bold": 1,
            "bright": 1,
            "dim": 2,
            "underline": 4,
            "underlined": 4,
            "blink": 5,
            "reverse": 7,
            "invert": 7,
            "hidden": 8,
        }

        colorNum = colorsConverter[color.lower()]
        styleNum = ";".join(str(stylesConverter[style.lower()]) for style in styles)
        return f"\033[{styleNum};{colorNum}m{text}\033[0m"
    return text


def formatMessage(type, text, lineNum=None):
    if constants.printMode == "markup":
        text = text.replace("<", "&lt;")
        if type == "fatal":
            return f"<fatal>{text}</fatal>"
        if type == "link":
            return f"<linkerror>{text}</linkerror>"
        if type == "warning":
            return f"<warning>{text}</warning>"
        if type == "message":
            return f"<message>{text}</message>"
        if type == "success":
            return f"<final-success>{text}</final-success>"
        if type == "failure":
            return f"<final-failure>{text}</final-failure>"
    else:
        if type == "message":
            return text
        if type == "success":
            return (
                printColor(" ✔ ", "green", "invert") + " " + text,
                printColor("YAY", "green", "invert") + " " + text,
            )
        if type == "failure":
            return (
                printColor(" ✘ ", "red", "invert") + " " + text,
                printColor("ERR", "red", "invert") + " " + text,
            )
        if type == "fatal":
            headingText = "FATAL ERROR"
            color = "red"
        elif type == "link":
            headingText = "LINK ERROR"
            color = "yellow"
        elif type == "warning":
            headingText = "WARNING"
            color = "light cyan"
        if lineNum is not None:
            headingText = f"LINE {lineNum}"
        return printColor(headingText + ":", color, "bold") + " " + text


def errorAndExit():
    failure("Did not generate, due to fatal errors")
    sys.exit(2)
