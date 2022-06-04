def print_name(name= "mathew murithi"):
    print(name)
print_name()
print_name("crystal")

def get_sum(num1,num2):
    sum_nums= num1 + num2
    return sum_nums
print(get_sum(7,12))
#####################
#write a function that gets the square of numbers

def  powers(number,power):
     power_nums = number **power
     return power_nums
print(powers(6,4))

def get_full_name(f_name,s_name):
    full_name = f_name + s_name
    return full_name
print(get_full_name("mathew " , "murithi"))
#####################################
#returning a dictionary from a function
def create_full_name(first_name,second_name):
    person={'first':first_name,'second':second_name}
    return person
student= create_full_name ("mathew","murithi")
print(student)

#passing a list in a function

def greet_friends(names):
    for name in names:
        msg = " hello! " + name.title() + "!"
        print(msg)
friends = ['crystal','marvin',]
greet_friends(friends)