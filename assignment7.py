#calculate the geometric progression
###############################


a =int(input("enter the first number"))
r =int(input("enter the common ratio"))
n =int(input("enter the number of terms"))

total = (a * (1 - pow(r,n)))
tn = a * pow(r,n-1)
print(total)
print(tn)
