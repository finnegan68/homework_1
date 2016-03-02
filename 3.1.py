height = int(input("Введите значение высоты прямоугольника "))
width = int(input("Введите значение ширины прямоугольника "))
i = 0
j = 0
for i in range(0, height):
    for j in range(0, width):
        print("*", end="")
        j += 1
    print("")
    i += 1
