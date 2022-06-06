f =open("lesson2.txt" ,'x')
#read the line
print(f.readline())

with open("lesson2.txt" , 'w') as f:
     f.write("this is a my new file\n")
     f.write("i amfrom nairobi\n")
     f.write("today is a cold day\n")

#reading a file
print(f.read())
f.close()

