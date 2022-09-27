def sixEx():
    r1 = int(input("Введите номер столбца для первой клетки:"))
    s1 = int(input("Введите номер строки для первой клетки:"))
    r2 = int(input("Введите номер столбца для второй клетки:"))
    s2 = int(input("Введите номер строки для второй клетки:"))
    if (r1 > 8 or s1 > 8 or r2 > 8 or s2 > 8):
        print("Вы ввели некорректное номер/номера клеток")
        return
    if (r1 % 2 == 0 and s1 % 2 == 0):
        CELL1 = "black"
    elif (r1 % 2 != 0 and s1 % 2 != 0):
        CELL1 = "black"
    elif (r1 % 2 == 0 and s1 % 2 != 0):
        CELL1 = "white"
    else:
        CELL1 = "white"

    if (r2 % 2 == 0 and s2 % 2 == 0):
        CELL2 = "black"
    elif (r2 % 2 != 0 and s2 % 2 != 0):
        CELL2 = "black"
    elif (r2 % 2 == 0 and s2 % 2 != 0):
        CELL2 = "white"
    else:
        CELL2 = "white"
    if (CELL1 == CELL2):
        print("Да")
    else:
        print("Нет")


sixEx()
