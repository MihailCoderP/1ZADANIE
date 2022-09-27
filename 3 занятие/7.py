def sevenEx():
    num = int(input("Введите натуральное число:"))
    if(num<0):
        print("Некорректное число")
        return
    if(num%4==0):
        if(num%100==0):
            if(num%400==0):
                print("Да")
            else:print("Нет")
        else:print("Да")
    else: print("Нет")

sevenEx()
