#introduction to conditional statements

gold = 0
miner = input("Hi, what is your name : ")
isGold = input("Is the mineral gold ? ")

#if yes is not in lower case the program will then proceed to the else statement
if isGold.lower() == "yes":
    gold += 1
    print(f"Hi {miner}, Your Total number of Gold is {gold}")
else:
    print(f"Hi {miner}, Your Total number of Gold is {gold}")