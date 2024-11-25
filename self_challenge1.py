to_sum = eval(input("Enter an integer ---> "))
sumDigits = 0

for i in str(to_sum):
    sumDigits += int(i)

print(f"Sum of the digits are ---> {sumDigits}")

