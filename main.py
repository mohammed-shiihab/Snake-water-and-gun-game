import random
'''
Snake = 1
water = -1
gun = 0

'''
a = [-1, 0, 1]
computer = random.choice(a)
youstr = input("Enter your choise: ")

youDict = {"s" : 1,  "w" : -1,  "g" : 0} 
ReverseDict = {1 : "snake",  -1 : "water",  0 : "gun"}

you = youDict[youstr]
print(f"You chose {ReverseDict[you]} \nComputer chose {ReverseDict[computer]}")

if (computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == -1):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You lose")

    else:
        print("Something went wrong")
