import re
print("Щербаченко Максим Анатолійович \nЛабораторна робота №1 \nВаріант 23 \nВизначення найближчої точки  \n")

re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    return number


first_value = validator_2("Enter dot a:")
second_value = validator_2("Enter dot b:")
third_value = validator_2("Enter dot c:")


if abs(second_value - first_value) < abs(third_value - first_value):
    print("b is closer to a.")
elif abs(second_value - first_value) == abs(third_value - first_value):
    print("Dot b = dot c.")
else:
    print("Dot c is closer to dot a.")