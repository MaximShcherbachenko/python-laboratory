"""Дано число A(>1). Вивести найбільше із цілих чисел K, для яких сума 1+1/2 +...+1/K буде менше A, і саму цю суму."""
import re
re_integer = re.compile("\d+$")

def validator_1(pattern, promt):
    a_value = input(promt)
    while not bool(pattern.match(a_value)):
        a_value = input(promt)
    return a_value


def validator_2(prompt):
    number = float(validator_1(re_integer, prompt))
    while prompt == "Enter value of A:" and number <= 1:
        number = float(validator_1(re_integer, prompt))
    return number

q = 0
while q != "-":
    A = validator_2("Enter value of A:")
    k = validator_2("Enter value of k:")
    i = 1
    b = 0
    c = 0
    while i <= k:
        c = b + (1 / i)
        if c > A:
            print("K =", i - 1, "Sum =", b)
            break
        elif c <= A and i == k:
            print("K =", i, "Sum =", c)
            break
        else:
            b = c
            i += 1
    q = input("Press <<->> for exit or any button(s) to continue:")
