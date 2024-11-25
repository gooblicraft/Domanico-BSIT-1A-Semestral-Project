def mathematicalOperation():
    num1 = eval(input("Enter the first number  : "))
    num2 = eval(input("Enter the second number : "))

    #addition 
    sum = num1 + num2
    print("\nThe sum of",  num1, "and", num2, "is", sum,"\b.")

    #subtraction
    diff = num1 - num2
    print("The difference of",  num1, "and", num2, "is", diff,"\b.")

    #product
    product = num1 * num2
    print("The product of",  num1, "and", num2, "is", product,"\b.")

    #division
    quotient = num1 / num2
    print("The quotient of",  num1, "and", num2, "is", quotient,"\b.")

    #Exponent
    exponent = num1 ** num2
    print(num1, "exponent by", num2, "is", exponent, "\b.")

    #modulus
    remainder = num1 % num2
    print("The remainder of",  num1, "and", num2, "is", remainder,"\b.")

    #floor division
    floorDivision = num1 // num2
    print("The floor division of",  num1, "and", num2, "is", floorDivision,"\b.")

