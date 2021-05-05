##userinput:
import random
"""
PartI Code:

userinput = input("please input one of the items: rock,paper,scissors: ")
userinput = userinput.upper()
##The all options for machine pick:
options = ["ROCK","PAPER","SCISSORS"]
ranIndex = random.randint(0,2)
PcPick = options[ranIndex]
if userinput not in options:
    print("Please input correct value")
elif userinput == PcPick:
    print("it is even/equal and no winner.")
elif (userinput == "ROCK" and PcPick == "SCISSORS") or (userinput == "SCISSORS" and PcPick == "PAPER") or (userinput == "PAPER" and PcPick == "ROCK"):
    print(f"user pcicked {userinput} and PC picked {PcPick}. So, user is the winner.")
else:
    print(f"user pcicked {userinput} and PC picked {PcPick}. So, PC is the winner.")
"""

"""
PartII:
"""
userWinNum = 0
PCWinNum = 0
options = ["ROCK","PAPER","SCISSORS"]

while userWinNum < 3 and PCWinNum < 3:
    ranIndex = random.randint(0,2)
    PcPick = options[ranIndex]
    userinput = input("please input one of the items: rock,paper,scissors: ")
    userinput = userinput.upper()
    if userinput not in options:
        print("Please input correct value")
    elif userinput == PcPick:
        print("it is even/equal and no winner.")
    elif (userinput == "ROCK" and PcPick == "SCISSORS") or (userinput == "SCISSORS" and PcPick == "PAPER") or (userinput == "PAPER" and PcPick == "ROCK"):
        print(f"user pcicked {userinput} and PC picked {PcPick}. So, user is the winner.")
        userWinNum += 1
    else:
        print(f"user pcicked {userinput} and PC picked {PcPick}. So, PC is the winner.")
        PCWinNum += 1

if userWinNum>=3:
    print("user is the Winner!")
else:
    print("PC is the Winner!")