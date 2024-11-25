#Code Challenge 14 by Domanico
#Continue to ask for a Number

isContinue = True
total = 0
while isContinue == True:
    ask = eval(input("Input a Number ------> "))
    
    if ask == 0:
        print("Loop Has Terminated", f"\nThe sum of all the numbers given is {total}")
        break
        isContinue = False
    else:
        total += ask
        continue
