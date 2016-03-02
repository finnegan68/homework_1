def function():
    a = input().split()
    if a[0] == "stop":
        print("Работа программы прекращена")

    else:
        product = 1
        i = 0
        while i < len(a):
            product = int(a[i]) * product
            i+=1
        print(product)
