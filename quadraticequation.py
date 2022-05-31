
import math
a=int(input("enter the number a"))
b=int(input("enter the number b"))
c=int(input("enter the number c"))
w=math.sqrt((b**2) - 4* a*c)
y_1 =(-b + w) /(2 * a)
y_2=(-b - w) / (2 * a)
print("the answer is :",y_1,y_2)
