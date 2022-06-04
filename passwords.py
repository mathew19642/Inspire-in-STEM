import random
print("welcome to our password generator")
character = "Mathew Murithi"
num_passwords = int(input("how many numbers do you want"))
len_passwords = int(input("ask user for password length"))
print(num_passwords)
print(len_passwords)
for passwords in range(num_passwords):
    passwords=" "
for c in range(len_passwords):
    passwords += random.choice(character)
    #print(passwords)
####create an account and generate its passwords
#password generator using classes
import random
character = "Mathew Murithi"
num_passwords = int(input("how many numbers do you want"))
len_passwords = int(input("what is the length of your passwords"))
class Passwords :
    def __init__(self,account):
        self.account = account
    
password1 = Passwords(input("enter your email account: "))
print("your password is: ")
for passwords in range(num_passwords):
    passwords = " "
for c in range(len_passwords):
    passwords += random.choice(character)
print(passwords)



