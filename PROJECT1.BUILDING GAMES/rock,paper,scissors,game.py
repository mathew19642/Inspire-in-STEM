# THE ROCK , PAPER , SCISS0RS , GAME
import random
#Rock
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
user_choice = input("Do you choose 'rock' or 'paper'' or 'scissors'? ")
user_choice = user_choice.lower()
if user_choice == "rock" :
    print("your choice is rock")
elif user_choice == "paper" :
    print("your choice is paper")
elif user_choice == "scissors" :
    print("ypur choice is scissors")
else :
     print("wrong choice")

computer_choices = ['rock','paper','scissors']
computer_choice = random.choice(computer_choices)
if computer_choice == computer_choices[0] :
    print("the computer choice is: Rock ", rock)
elif computer_choice == computer_choices[1] :
    print("the computer choice is: Paper ", paper)
else :
    print("the computer choice is : Scissors ", scissors)
if computer_choice == computer_choices[0] and user_choice == "rock" :
    print("it is a draw")
elif computer_choice == computer_choices[0] and user_choice =="paper" :
    print("user wins")
elif computer_choice == computer_choices[0] and user_choice =="scissors" :
    print("coputer wins")
elif computer_choice == computer_choices[1] and user_choice =="rock" :
    print("computer wins")
elif computer_choice == computer_choices[1] and user_choice =="paper" :
    print("it is a draw")
elif computer_choice == computer_choices[1] and user_choice =="scissors" :
    print("user wins")
elif computer_choice == computer_choices[2] and user_choice =="rock" :
    print("user wins")
elif computer_choice == computer_choices[2] and user_choice =="paper" :
    print("computer wins")
elif computer_choice == computer_choices[2] and user_choice =="scissors" :
    print("it is a draw")





