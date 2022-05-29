#get number of rows
rows = int(input("enter the number of rows:"))
for i in range (rows) :
    for j in range(i+1):
        print("*" ,end=" ")
    print("\n")

rows = int(input("enter number of rows"))
k = 0
for i in range (1,rows + 1):
    for space in range (1,(rows - i) + 1):
        print(end = " ")
    while k!= (2 * i - 1):
          print("* ",end= " ")
          k +=1
