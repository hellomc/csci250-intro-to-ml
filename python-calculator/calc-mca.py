# Date: 2019-09-08
# 
# Description: Calculator takes in two integer values.
# User chooses an option to carry out an equation.

import sys

def greeting():
    print("******************************")
    print("Welcome to the Calculator")

# Gets the first number in the equation
def operand1():
    operand1 = input("Please enter the first number: ")
    operand1 = int(operand1)
    return operand1

# Gets the second number in the equation
def operand2():
    operand2 = input("Please enter the second number: ")
    operand2 = int(operand2)
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

# Prompts for user to input a numbered option
def optionOperator():
    value = True
    while value == True:
        optionOp = input("Enter an Option between 1-7: ")
        if int(optionOp) in range(1, 8):
            value = False
            return optionOp

# Remember to include format for decimal points!!!
def add(a, b):
    c = a + b
    return ("%d + %d = %d" % (a, b, c))

def subtract(a, b):
    c = a - b
    return ("%d - %d = %d" % (a, b, c))

def multiply(a, b):
    c = a * b
    return ("%d * %d = %d" % (a, b, c))

def divide(a, b):
    c = a / b
    return ("%d / %d = %d" % (a, b, c))

def power(a, b):
    c = a ** b
    return ("%d ^ %d = %d" % (a, b, c))

def modulo(a, b):
    c = a % b
    return ("%d %% %d = %d" % (a, b, c))

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
        return quit()
    else:
        optionOperator()  
  
def calculator():
    print("******************************")
    op1 = operand1()
    op2 = operand2()
    optionMenuDisplay()
    optNum = optionOperator()
    print(operation(optNum, op1, op2))
    print("******************************")

def playCalc():
    game = True
    while game == True:
      value = input("Would you like to calculate an equation? Y / N\n")
      if value == "Y":
        calculator()
      else:
        game == False
        print(quit())
        sys.exit("****End Calculator Program****")
      

greeting()
playCalc()

#Need to do decimal places...
#Fix format on %
