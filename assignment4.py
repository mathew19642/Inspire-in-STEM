#write a programme to withdraw 25000 if the account balance is between 100000 to 200000
#30% if account balance is between 500000 and 1000000
#above 1000000 deduct 700000
name = "mathew"
money = input("what ammount of money do you have")
account_balance = 150000
if(int(account_balance)>100000) and (int(account_balance)<200000):
  account_balance = account_balance - 25000
  print("we have deducted 25000")
if("int(account_balance) > 500000 and (int(account_balance)) < 1000000"):
   account_balance = float(account_balance) - (0.3 * account_balance)
   print("we have deducted 30 percent from your account")
else  : 
      account_balance = account_balance - 15000 
      print("we have deducted 15000")
      print("yor final balance is account balance")





