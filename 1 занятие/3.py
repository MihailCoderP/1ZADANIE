age = int(input("введите возраст: "))
if (age>0) and (age<75):
 if (age>=16) :
          print ("поздравляем ы поступили в ВГУИТ")
 if (age<16):
          print("Сначала нужно окончить школу!")
          s = 16 - age
          print(" осталось учиться: ", s,"лет")
else :
    print("возраст не подходит")
name =(input("введите имя: "))
if (name=='иван')or (name=='Иван'):
    print("поступающего зовут Иван")
if (name!='иван') and (name!='Иван'):
    print("поступающего не зовут иван")
