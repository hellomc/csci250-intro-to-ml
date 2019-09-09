# Description: Calculator takes in two values that
# can be a floating point or integer number.
# User chooses an option to carry out an equation.
# Computer prints out the equation and resulting answer.

import sys

def greeting():
    print("******************************")
    print("Welcome to the Calculator")
    print("******************************")

# Gets the first number in the equation and checks if it is a floating point or integer number.
def operand1():
    while True:
        try:
            operand1 = input("Please enter the first number: ")
            if "." in operand1:
                operand1 = float(operand1)
                print("User entered the floating point number: %.5f" % operand1)
                break
            else:
                operand1 = int(operand1)
                print("User entered the integer number: %d" % operand1)
                break
        except ValueError:
            print("Invalid Value. Enter a floating point or integer number!")
    return operand1

# Gets the second number in the equation and checks if it is a floating point or integer number.
def operand2():
    while True:
        try:
            operand2 = input("Please enter the second number: ")
            if "." in operand2:
                operand2 = float(operand2)
                print("User entered the floating point number: %.5f" % operand2)
                break
            else:
                operand2 = int(operand2)
                print("User entered the integer number: %d" % operand2)
                break
        except ValueError:
            print("Invalid Value. Enter a floating point or integer number!")
    return operand2

# Displays the menu of operations on the calculator
def optionMenuDisplay():
    print("******************************")
    print("Choose an Option between 1-7: ")
    operations = ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulo", "Quit"]
    # for loop goes through 7 times 1-7
    for x in range (1, 8):
        print("%d) %s" % (x, operations[x-1]))
    print("******************************")

# Prompts the user to input a numbered option
def optionOperator():
    while True:
        try:
            optionOp = input("Enter an Option between 1-7: ")
            if int(optionOp) in range(1, 8):
                break
        except ValueError:
            print("Invalid Option. Enter 1-7!")
    return optionOp

# Operation for addition.
def add(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a + b
        statement = ("%s %.5f + %.5f = %.2f" % ("ADDITION: ", a, b, c))
    else:
        c = a + b
        statement = ("%s %d + %d = %d" % ("ADDITION: ", a, b, c))
    return statement

# Operation for subtraction.
def subtract(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a - b
        statement = ("%s %.5f - %.5f = %.2f" % ("SUBTRACTION: ", a, b, c))
    else:
        c = a - b
        statement = ("%s %d - %d = %d" % ("SUBTRACTION: ", a, b, c))
    return statement

# Operation for multiplication.
def multiply(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a * b
        statement = ("%s %.5f * %.5f = %.2f" % ("MULTIPLICATION: ", a, b, c))
    else:
        c = a * b
        statement = ("%s %d * %d = %d" % ("MULTIPLICATION: ", a, b, c))
    return statement

# Operation for division.
def divide(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a / b
        statement = ("%s %.5f / %.5f = %.2f" % ("DIVISION: ", a, b, c))
    else:
        c = a / b
        statement = ("%s %d / %d = %d" % ("DIVISION: ", a, b, c))
    return statement

# Operation for power.
def power(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a ** b
        statement = ("%s %.5f ^ %.5f = %.2f" % ("POWER: ", a, b, c))
    else:
        c = a ** b
        statement = ("%s %d ^ %d = %d" % ("POWER: ", a, b, c))
    return statement

# Operation for modulo
def modulo(a, b):
    if type(a).__name__ == "float" or type(b).__name__ == "float":
        a = float(a)
        b = float(b)
        c = a % b
        statement = ("%s %.5f %% %.5f = %.2f" % ("MODULO: ", a, b, c))
    else:
        c = a % b
        statement = ("%s %d %% %d = %d" % ("MODULO: ", a, b, c))
    return statement

def quit():
    return ("Calculator Program Quit")

# Takes in the user's input for math operation and performs calculation on 2 previously input numbers
def operation(optionOp, num1, num2):
    if optionOp == "1":
        return add(num1, num2)
    elif optionOp == "2":
        return subtract(num1, num2)
    elif optionOp == "3":
        return multiply(num1, num2)
    elif optionOp == "4":
        return divide(num1, num2)
    elif optionOp == "5":
        return power(num1, num2)
    elif optionOp == "6":
        return modulo(num1, num2)
    elif optionOp == "7":
        #return quit()
        sys.exit("****End Calculator Program****") 
  
def calculator():
    print("******************************")
    op1 = operand1()
    op2 = operand2()
    optionMenuDisplay()
    optNum = optionOperator()
    print(operation(optNum, op1, op2))
    print("******************************")

def playCalc():
    greeting()
    while True:
        try:
            value = input("Would you like to calculate an equation? Y / N\n")
            if value == "Y":
                calculator()
            elif value == "N":
                print(quit())
                sys.exit("****End Calculator Program****")
                break
        except ValueError:
            print("Invalid Input. Y or N?")

playCalc()
