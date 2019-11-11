"""∑(from i=1 to n) ((x+2)^i)/(x-n)"""
import re

re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    if prompt == "Enter the final value of iterations:" or prompt == "Enter number of first iteration:":
        while number <= 0:
            number = float(validator_1(re_integer, prompt))
    return number
c = 0
while True:
    x = validator_2("Enter value of x:")
    i = validator_2("Enter number of first iteration:")
    n = validator_2("Enter the final value of iterations:")
    while n == x or n < i:
        n = validator_2("Enter the final value of iterations:")

    for i in range(1, int(n + 1)):
        c += (n * x - 1) ** i / (x - n)
        i += 1
    print("Result is", round(c, 3))
    q = input("Press <<->> for exit or any button(s) to continue:")
    if q == "-":
        break
