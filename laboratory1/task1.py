import re
""" Розрахуйте значення виразу (a + 4b) (a-3b) + a2 при a = 2 і b = 3. """

re_integer = re.compile("\d+$")

re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    return number

while True:
    a = validator_2("Enter value of a:")
    b = validator_2("Enter value of b:")
    print((a + 4 * b) * (a - 3 * b) + 2 * a)
    q = input("Press <<->> for exit or any button(s) to continue:")
    if q == "-":
        break
