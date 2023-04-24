import os


def calculator():
    try:
        # asking the user about the numbers and operators they want to use for the calculation
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        # using ecept value in case that user input unexpected behavior 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # using the if statement to make those calculations:
    # sum
    if operator == "+":
        result = num1 + num2
    # subtraction
    elif operator == "-":
        result = num1 - num2
    # multiplication
    elif operator == "*":
        result = num1 * num2
    # division
    elif operator == "/":
        result = num1 / num2
    # if user input something else than an operator
    else:
        print("You have input an invalid operator!")
        return

    # printing result
    print("Result:", result)

    # adding equation to txt file called equations.txt
    with open("equations.txt", "a") as file:
        file.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")

# defining function to open writen txt file
def open_file():
    try:
        file_name = input("Enter the file name: ")
        with open(file_name, "r") as file:
            # reading the file contents as a list of lines
            lines = file.readlines()

            # printing every calculation in separate line
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")


choice = input("Input 'c' to calculate ,'o' to open txt file  or 'e' to exit calculator: ").lower()
# creating a loop to continue counting or opening file and taking from def()
while choice == "o" or choice == "c":
    #this choice mean that user whant open a txt file
    if choice == "o":
            open_file()
    #this choice mean that user whant make a calculation
    elif choice == "c":
            calculator()
    
    #this will happend when user write wrong name of file
    else:
        print("You have write an invalid file name")
    #looping question what user whant to do. If user put something diffrent that program stop
    choice = input("Input 'c' to calculate or 'o' to open txt file: ").lower()
    #this choice will let user exit the calculator
    if choice == "e":
        break
