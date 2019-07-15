import random as rand

x = rand.randrange(1,100)
userCorrect = False

while(userCorrect == False):
    print("Please input a number!")
    user = input()
    user_int = int(user)

    if (user_int == x):
        print("equal!")
        quit()

    if (user_int > x):
        print ("greater!")

    if (user_int < x):
        print ("lesser!")




