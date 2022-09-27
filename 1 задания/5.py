n = (input("введите n: "))
n = int(n)
s = n
c1 = n*n
c2 = n*n*n
for i in range(2,4):
   c = n
   for g in range(0,i+1):
      c = c* n
   s = s + c
print("значение выражения: ",c1+c2+s)
