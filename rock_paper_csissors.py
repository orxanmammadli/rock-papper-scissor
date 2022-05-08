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


import random
x=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
y=int(x)
if y==0:
  print(rock)
elif y==1:
  print(paper)
elif y>2:
  print("You  enter invalid number!")
else:
  print(scissors)
print("Computer Choose: ")  
a= random.randint(0,2)  
if a==0:
  print(rock)
elif a==1:
  print(paper)
else:
  print(scissors)
if y==0 and a==2:
  print("You win")
elif y==2 and a==1:
  print("You win")
elif y==1 and a==0:
  print("You win")
else:
  print("You lose")