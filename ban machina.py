import math
a = 3
b = -14
c = -5
def funName(a,b,c):
    D = b*b - 4*a*c
   
if b < 0:
    print("БАН ТЕБЕ!!!!!!!!!!!!")
else:
    x1 = (-b + math.sqrt(D))/(2 * a)
    x2 = (-b - math.sqrt(D))/(2 * a)
    print(x1)
    print(x2)

funName(a,b,c)
