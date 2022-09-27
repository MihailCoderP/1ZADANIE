def thirdEx():
    n = input("Введите количество минут прошедшее с начала суток:")
    hours = int(n)//60
    if(hours>24):
        hours = hours%24
    minuts = int(n)%60
    if(hours<10):
        hours = "0" + str(hours)
    elif(hours==24):
        hours = "00"
    if(minuts<10):
        minuts = "0"+str(minuts)
    print("Время - %s:%s"%(hours,minuts))
thirdEx()