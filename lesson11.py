#print even numbers 
for numbers in range(0,10):
    print(numbers)
for numbers in range(0,10):
    print(numbers%2)
for numbers in range(0,10):
    if(numbers%2==0):
        print(numbers)
#get the sum of all even numbers between 0 and 50

sum_nums = 0
prod_nums = 1
#product of odd numbers between 0 and 20
for numbers in  range(0,20):
    if (numbers %2 == 1):    #odd numbers
        prod_nums = prod_nums * numbers
print(prod_nums)
#calculate the factorile of 6!
number = int(input("enter the number"))
factorial= 1
if number <0:
    print("factorial of negative number desnt exist")
elif number==0:
     print("factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
print("factorial of number :",factorial)
