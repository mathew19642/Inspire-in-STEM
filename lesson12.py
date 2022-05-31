num =int(input("what is your number"))
if (num%5==0):
    print("number is divisile by 5")
num = int(input("what is your number"))
if (num%7==0):
    print("number is divisible by 7")
else :
     print("number is not divisble by 5 or 7")

###simpler method
number = int(input("enter the number"))
if(number%7==0) and (number%5==0):
   print(f"the number{number} is divisible by 5 and 7")
else :
     print(f"the  number{number} is not divisble by 5 or 7")


###enter your name so we can customize your name
name =input("enter your name")
print("hello"+ str(name))

num = 20
num +=num
print(num)
###########################
prompt =("enter your name so we can customize")
prompt += "\n enter your name"
print(" hello "  + input(prompt))


