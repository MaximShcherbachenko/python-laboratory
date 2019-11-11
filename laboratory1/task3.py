"""F(x) = {(-x^2 if x>=7) or (2^(x)/(x^2 - 9))}"""
import re

re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    return number

q = 0
while q != "-":
    x = validator_2("Enter variable x:")


    def variations(value):
        if value > 7:
            print(-value ** 2)
        elif value <= 7:
            while value == 3 or value == -3:
                value = validator_2("Enter variable x:")
            if value == 7:
                print(-value ** 2)
                print((2 ** (-value)) / (value ** 2 - 9))
        else:
            print((2 ** (-value)) / (value ** 2 - 9))


    variations(x)
    q = input("Press <<->> for exit or any button(s) to continue:")
