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

def add():
    """Will add two numbers together"""
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))
    # Add the two number together
    result = num1 + num2
    return result
    
def mult():
    """Will multiply two numbers together"""
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))
    # Multiply the two number together
    result = num1 * num2
    return result

def sub():
    """Will subtract two numbers from each other"""
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))
    # Subtract the second number from the first number
    result = num1 - num2
    return result

def div():
    """Will divide two numbers together"""
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))
    # Divide the one number from an other
    result = num1 / num2
    return result
   