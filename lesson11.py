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



num = 0
while num < 10:
      print(num)
      num = num + 2
while num <10:
      print(num)
      num = num + 1
if(num%2==0):
   print(num)
