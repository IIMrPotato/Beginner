#while 1==1:
    #print("Love me more")

#for i in range(10):
    #print(i+1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Anderson":
    #print(i)

#import time
#for seconds in range(10,0,-2):
    #print(seconds)
    #time.sleep(1)
#print("Happy Birthday Bro")

#rows = int(input("How many rows?:"))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

#while True:
    #name = input("Enter your name: ")
    #if name := "":
        #break

#phone_number = "0123456789"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):
    #if i == 4:
        #pass
    #else:
        #print(i)

#food = ["Pizza","Fries","Cola","cake"]

#food[0]="sushi"
#food.add("Desserts")
#food.remove("Fries")
#food.pop()
#food.insert(1,"Curry")
#food.clear()

#print(food[0])
#for x in food:
    #print(x) \ #print(food.difference(.......))

#Drinks = ["Boba", "milk tea", "Sprite"]
#dinner = ["Pizza", "Mcd", "Kfc"]
#deserts = ["BBQ", "Steak", "Wings"]

#food = [Drinks,dinner,deserts]
#print(food[0][2])
#print(food[1][2])

#People = ("Market",12,"rain")

#print(People.count("Market"))
#print(People.index("rain"))

#for x in People:
    #print(x)

#if "Market" in People:
    #print("Market is raining.")

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie!")
        user_wins += 0

    elif user_input == "rock" and computer_pick == "rock":
        print("Tie!")
        user_wins += 0

    elif user_input == "paper" and computer_pick == "paper":
        print("Tie!")
        user_wins += 0


    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")









