print("Take your craft serious")

def double(var_x):
    var_doubled = var_x * 2
    return var_doubled

def add(var_x, var_y):
    var_result_add = var_x + var_y 
    return var_result_add 

def subtract(var_x, var_y):
    var_result_subtract = var_x - var_y 
    return var_result_subtract

def multiply(var_x, var_y):
    var_result_multiply = var_x * var_y 
    return var_result_multiply 

def divide(var_x, var_y):
    var_result_divide = (var_x / var_y)
    return var_result_divide 

arr_calc_options = ['Double', 'Add', 'Subtract', 'Multiply', 'Divide']

ui_bool_calc_is_on = True 

while (ui_bool_calc_is_on == True):

    print("\nThe following options are available to you:\n")

    for option in arr_calc_options:
        print(f"You can {option} values")
    print("You can also Quit and turn the calculator off")
    print("If you make a submission not recognised by the calculator, you will be presented with the options again and asked to provide a valid option")

    ui_calc_operation = input("\nWhat would you like to do?\n")

    if (ui_calc_operation.lower() == 'double'):
        ui_var_x = int(input("\nYou have chosen to double your input; what value would you like to double?\n"))
        ui_var_x_doubled = double(ui_var_x)
        print(f"You chose to double {ui_var_x} and the result of this calculation is {ui_var_x_doubled} - congratulations!\n")
 
    elif (ui_calc_operation.lower() == 'add'):
        print("\nYou have chosen to add together a pair of values\n")
        ui_var_x = int(input("\nWhat is your first value in this calculation?\n")) 
        ui_var_y = int(input("\nWhat is your second value in this calculation?\n"))

        ui_var_x_y_added = add(ui_var_x, ui_var_y)
        print(f"\nYou submitted {ui_var_x} and {ui_var_y} to be added together; the result of this calculation is {ui_var_x_y_added}\n")

    elif (ui_calc_operation.lower() == 'subtract'):
        print("\nYou have chosen to subtract a value from another value\n")
        ui_var_x = int(input("\nWhat is your first value in this calculation?\n"))
        ui_var_y = int(input("\nWhat is your second value in this calculation?\n"))

        ui_var_x_y_subtracted = subtract(ui_var_x, ui_var_y) 
        print(f"\nYou submitted {ui_var_x} and {ui_var_y} to be subtracted from one another; the result of this calculation is {ui_var_x_y_subtracted}")
 
    elif (ui_calc_operation.lower() == 'multiply'): 
        print("\nYou have chosen to multiply a pair of values\n")
        ui_var_x = int(input("\nWhat is your first submission into this calculation?\n"))
        ui_var_y = int(input("\nWhat is your second submission into this calculation?\n"))

        ui_var_x_y_multiplied = multiply(ui_var_x, ui_var_y)
        print(f"\nYou provided the values {ui_var_x} and {ui_var_y} multiplication; the result is {ui_var_x_y_multiplied}\n")

    elif (ui_calc_operation.lower() == 'divide'):
        print("\nYou have chosen to divide a pair of values\n")
        ui_var_x = int(input("\nWhat is your first value in this calculation?\n"))
        ui_var_y = int(input("\nWhat is your second value in this calculation?\n"))

        ui_var_x_y_divided = divide(ui_var_x, ui_var_y)
        print(f"\nYou submitted {ui_var_x} and {ui_var_y} for division; the result of this calculation is {ui_var_x_y_divided}\n")
    elif (ui_calc_operation.lower() == 'quit'):
        ui_calc_exit = input("\nYou have chosen to quit and turn your calculator off; are you sure you'd like to quit? Please press 'q' to confirm\n")

        if (ui_calc_exit.lower() == 'q'):
            print("Thank you for confirming your decision to turn off your calculator")
            ui_bool_calc_is_on = False 
        else:
            print("\nYou will be presented with the calculator options again :D\n")
            continue
    else:
        print("\nYou have chosen an operation that is not recognised by this calculator program; please choose from the calculator options available\n")
        continue

print("\nGoodbye User\n")
 
