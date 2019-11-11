"""З рядка видалити всі цифри і малі букви."""
import re

q = 0

re_integer = re.compile("\w+$")

def validator_1(pattern, promt):
    value = input(promt)
    while not bool(pattern.match(value)):
        value = input(promt)
    return value


def validator_2(prompt):
    string = str(validator_1(re_integer, prompt))
    return string

our_string = validator_2("Enter string:")


def deleting_incorrect_symbols():
    global our_string
    for i in range(0, len(our_string)):
        if our_string[i].islower() or our_string[i].isdigit():
            our_string = our_string[:i] + " " + our_string[i + 1:]
    return str(our_string)

while q != "-":
    deleting_incorrect_symbols()
    if our_string.replace(" ", "") == our_string:
        print(our_string, "- result")
    else:
        print(our_string, "- for clarity")
        print(our_string.replace(" ", ""), "- without spaces")
    q = input("Press <<->> for exit or any button(s) to continue:")
    if q == "-":
        break
