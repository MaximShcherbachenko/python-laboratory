"""На осі ОХ розташовані три точки а, b, с (ввести з клавіатури). Визначити, яка з точок b або  cрозташована ближче до а."""
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


while True:
    first_value = validator_2("Enter dot a:")
    second_value = validator_2("Enter dot b:")
    third_value = validator_2("Enter dot c:")

    if abs(second_value - first_value) < abs(third_value - first_value):
        print("b is closer to a.")
    elif abs(second_value - first_value) == abs(third_value - first_value):
        print("Dot b = dot c.")
    else:
        print("Dot c is closer to dot a.")

    q = input("Press <<->> for exit or any button(s) to continue:")
    if q == "-":
        break
