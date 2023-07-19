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

ui_bool_calc_is_on = True 

while (ui_bool_calc_is_on == True):
    ui_calc_operation = input("\nWhat would you like to do?\n")

    if (ui_calc_operation.lower() == 'double'):
        ui_var_x = int(input("\nYou have chosen to double your input; what value would you like to double\n"))
        ui_var_x_doubled = double(ui_var_x)
        print(f"You chose to double {ui_var_x} and the result of this calculation is {ui_var_x_doubled} - congratulations!")
 
    elif (ui_calc_operation.lower() == 'add'):
        print("\nYou have chosen to add together a pair of values")
    elif (ui_calc_operation.lower() == 'subtract'):
        print("\nYou have chosen to subtract a value from another value\n") 
    elif (ui_calc_operation.lower() == 'multiply'): 
        print("\nYou have chosen to multiply a pair of values\n")
    elif (ui_calc_operation.lower() == 'divide'):
        print("\nYou have chosen to divide a pair of values\n")
    else:
        ui_calc_exit = input("\nYou have chosen an option out of the set range; are you sure you'd like to quit? Please press 'q' to confirm\n")

        if (ui_calc_exit.lower() == 'q'):
            print("Thank you for confirming your decision to turn off your calculator")
            ui_bool_calc_is_on = False 
        else:
            continue

print("\nGoodbye User\n")
 
