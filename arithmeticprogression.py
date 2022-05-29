#first n term of AP 
#########################
#assignment on geometric progression



a=int(input("enter the first number"))
d=int(input("enter the common difference"))
n=int(input("number of terms"))
for i in range(1,n+1):
      n_term = a + (i - 1)*d
      print(n_term)
sum_n= (n_term/2)*(2*a + (n-1)*d)
print(sum_n)
