#calculate the geometric progression
#calculate the sum of the geometric expression
#calculate the t_n ter / no of term
###############################


a =int(input("enter the first number"))
r =int(input("enter the common ratio"))
n =int(input("enter the number of terms"))

total = (a * (1 - pow(r,n)))/(1-r)   #sum of the GP
tn = a * pow(r,n-1)    #t_n term of the GP
print(total)
print(tn)
