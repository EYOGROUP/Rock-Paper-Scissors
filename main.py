import random
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

#Write your code below this line 👇

choose = input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if choose == "0":
    print(rock)

elif choose =="1":
    print(paper)

else:
    print(scissors)

print("Computer Chose: ")

computer = random.randint(0,2)

if computer == 0:
    print(rock)

elif computer ==1:
    print(paper)

else:
    print(scissors)

if choose == "0" and computer == 1:

    print("You lose")

elif choose =="1" and computer ==0:
    print("You win")

if choose == "2" and computer == 1:
    print("You win")

elif choose =="1" and computer ==2:
    print("You lose")

if choose == "0" and computer == 2:
    print("You win")

elif choose =="2" and computer ==0:
    print("You lose")

elif choose =="0" and computer ==0 or choose =="1" and computer ==1 or choose =="2" and computer ==2:
     print("Repaet")


    
    