print("Щербаченко Максим Анатолійович \nЛабораторна робота №1 \nВаріант 23 \nОбчислення функції в залежності від значення введеної змінної\n")
print("Third task:")
print()
print("Enter x:")
x = int(input())
numerator = 0
denominator = 0
if x > 7:
    numerator = -x**2
    print(numerator)
elif x <= 7:
    if x == 3 or x == -3:
        print("Not suitable for designation area")
    elif x == 7:
        numerator = -x ** 2
        denominator = (2**(-x))/(x**2 - 9)
        print(numerator)
        print(denominator)
    else:
        denominator = (2 ** (-x)) / (x ** 2 - 9)
        print(denominator)