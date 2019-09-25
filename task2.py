print("Щербаченко Максим Анатолійович \nЛабораторна робота №1 \nВаріант 23 \nВизначення найближчої точки  \n")

print("Second task:")
print()
print("Enter dot a:")
first_value = int(input())
print("Enter dot b:")
second_value = int(input())
print("Enter dot c:")
third_value = int(input())
if abs(second_value - first_value) < abs(third_value - first_value):
    print("b is closer to a")
elif abs(second_value - first_value) == abs(third_value - first_value):
    print("Dot b = dot c")
else:
    print("Dot c is closer to dot a")