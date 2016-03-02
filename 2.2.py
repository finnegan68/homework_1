a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите c "))
D = b ** 2 - 4 * a * c
if D > 0:
    x_1 = (-b + D ** (1 / 2)) / 2 * a
    x_2 = (-b - D ** (1 / 2)) / 2 * a
    print("x_1 = " + str(x_1))
    print("x_2 = " + str(x_2))
elif D == 0:
    x = -b / 2 * a
    print("x = " + str(x))
else:
    print("Решений в действительный числах нет")
