#a dictionary is a collection of key pair values
#syntax : dictionary = {'key :'value'}
list_names = {'mathew','crystal'}
colors = {'color' : 'red'}
# for color in colors :
#     if(colors=="red"):
#        print(colors.upper())
vehicle = {'type':'toyota','plate number':'KYZ'}
print(colors)
#print(type(names) #we use the type method to read the the data
#accesing values in a dictionary
print(vehicle['type'])  #you can acces the value of an element isisde a dictionary using the key
print(vehicle['plate number'])
person = {'name' : 'mathew'}
person['age']='19'
person['favfood'] = 'chapati'
person['phno'] = '0110089335'
person['color'] = 'white'
id_number = {'no':'0198'}
adress = {'add':'462'}
print(person['name'])
print(person['name'] , adress['add'] , id_number['no'])
print(person)
del [person['phno']]
print(person)
#print(person)
#loopng over dictionaries
for key, value in person.items():
    print(f"{key}:{value}")
colors = ['red','green','blue','purple']
i=0
i = 1
while i < len(colors):
     if(colors[1]=='green'):
       print(colors[1].upper())
       i +=1
i = 2
while i < len(colors):
     if(colors[2]=='blue'):
       print(colors[2].upper())
       i +=1
i = 3
while i < len(colors):
     if(colors[3]=='purple'):
       print(colors[3].upper())
       i +=1