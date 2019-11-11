import re
re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text
