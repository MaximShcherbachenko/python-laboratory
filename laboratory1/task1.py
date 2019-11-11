import re
print("Щербаченко Максим Анатолійович \nЛабораторна робота №1 \nВаріант 23 \nЗнаходження результату виразу з заданими змінними  \n")
print("Firts task:")

re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = int(validator_1(re_integer, prompt))
    return number

a = validator_2("Enter value of a:")
b = validator_2("Enter value of b:")
print((a + 4 * b) * (a - 3 * b) + 2 * a)
