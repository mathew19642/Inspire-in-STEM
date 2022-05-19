motorcycle=['honda','yamaha','suzuki']
motorcycle_owner = "mathew"
print(motorcycle)
motorcycle[0] = "bugati"
print(motorcycle)
#adding element in a list
print(motorcycle[2])
print("i love" + str(motorcycle[2]))
motorcycle.append('bugati')
print(motorcycle)
print(motorcycle)
plate_number = ('HSFD','GHF','FGE')
print(motorcycle[0] + " " + plate_number[0])
#deleting an item from a list  ..del
del motorcycle[0]
print(motorcycle)
#del motorcycle[2] #deleting an item from a list
#popped method deletse the last index
popped_motorcycle = motorcycle.pop()   
print(motorcycle)
# ask print a statement : my name is mathew  and i own a mtorcycle plate number
print("my name is " + motorcycle_owner + " and i own a " + motorcycle[0] + " " + plate_number[0])
#removing an item from a list
motorcycle.remove([0])
print(motorcyle)
motor