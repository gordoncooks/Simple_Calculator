from util import log, display_Main_Menu, add, mult, sub, div

log("Program Started")

while True:
    # Ask the user what they would like to do

    display_Main_Menu()

    try:
        task = int(input("Select option: "))

        if task == 1:
            log("Add selected. (n1 + n2)") # Log TASK

            result = add()

            print(f"Awnser: {result}")

        elif task == 2:
            log("Subtract selected. (n1 - n2)") # Log TASK
            
            result = sub()

            print(f"Awnser: {result}")

        elif task == 3:
            log("Multiply selected. (n1 * n2)") # Log TASK
            
            result = mult()

            print(f"Awnser: {result}")

        elif task == 4:
            log("Divide selected. (n1 / n2)") # Log TASK

            result = div()

            print(f"Awnser: {result}")

        elif task == 5:
            log("Program stoped running.") # Log TASK
            break
        else:
            log(f"Invalid option selected ... {task} ...") # Log Invalid selection
    except:
        log("Invalid input. Please enter a number.") # Log Invalid input

    