import os
import time
import datetime

# Define the base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def log(log):
    """Will write a log to the log.txt file and print to console"""

    # Generate the current time stamp
    time_satmp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    # Path to the file
    file_path = os.path.join(BASE_DIR, "logs/logs.txt")

    # Open the file
    logs_txt = open(file_path, 'a')

    # Add the log to the text file
    logs_txt.write(time_satmp + "; Description: " + log + "\n")

    # Display the log in the console
    print("\n" + time_satmp + "; Description: " + log)

def display_Main_Menu():
    """Will display the main menu of the program. 1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit"""

    menu_text = """
Main Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
"""

    print(menu_text)

def collect_numbers():
    """Will collect 2 numbers."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))     # Get the first number from the user
            num2 = float(input("Enter the second number: "))    # Get the second number from the user
            return num1, num2
        except:
            log("Invalid input")
    

def add():
    """Will add two numbers together"""
    # Collet numbers from user
    num1, num2 = collect_numbers()
    # Add the two number together
    result = num1 + num2
    return result
    
def mult():
    """Will multiply two numbers together"""
    """Will add two numbers together"""
    # Collet numbers from user
    num1, num2 = collect_numbers()
    # Add the two number together
    result = num1 * num2
    return result

def sub():
    """Will subtract two numbers from each other"""
    """Will add two numbers together"""
    # Collet numbers from user
    num1, num2 = collect_numbers()
    # Add the two number together
    result = num1 - num2
    return result

def div():
    """Will divide two numbers together"""

    while True:
        try:
            """Will add two numbers together"""
            # Collet numbers from user
            num1, num2 = collect_numbers()
            # Add the two number together
            result = num1 / num2
            return result
        except ZeroDivisionError:
            log("You can't divide by zero!")
   