import random

nm = input("Enter your Name:- ")
print("******************************SNAKE--WATER--GUN  GAME******************************")
print("Give the input as per the following hiints:-|")
print("s for Snake\nw for Water\ng for Gun")

cha = 1
comp = 0
user = 0
while cha<=10:
    lst = ["s" , "w" , "g"]
    b = random.choice(lst)
    usr = input("Enter your Choice")
    
    if usr in "sS" and b == "w":
        user +=1
        print(f"{nm} gets 1 Point")
    elif usr in "sS" and b == "g":
        comp +=1
        print("Computer gets 1 Point")
    elif usr in "sS" and b == "s":
        print("Tie!!! Try again ///")
    elif usr in "wW" and b == "s":
        comp +=1
        print("Computer gets 1 Point")
    elif usr in "wW" and b == "g":   
        user +=1
        print(f"{nm} gets 1 Point")
    elif usr in "wW" and b == "w":
        print("Tie!!! Try again ///")
    elif usr in "gG" and b == "s":
        user +=1
        print(f"{nm} gets 1 Point")
    elif usr in "gG" and b == "w":
        comp +=1
        print("Computer gets 1 Point")
    elif usr in "gG" and b == "g":
        print("Tie!!! Try again ///")
    print(f"No. of chances left is {10 - cha}")
    print("\n")

    cha+=1

if comp > user:
    print("Computer is the WINNER!!!, by scorring:- ",comp)

elif user > comp:
    print(f"{nm} is the WINNER!!!, by scooring:-",user)
elif comp == user:
    print(f"Match tie by {user} scores")
