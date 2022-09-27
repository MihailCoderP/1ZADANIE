def fiveEx():
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    c = input("Введите третье число:")
    if(int(a)>=int(b)):
        if(int(a)>=int(c)):
            print("Наибольшее число:%s"%a)
        else:
            print("Наибольшее число:%s"%c)
    else:
        if(int(b)>=int(c)):
            print("Наибольшее число:%s"%b)
        else:
            print("Наибольшее число:%s"%c)
fiveEx()