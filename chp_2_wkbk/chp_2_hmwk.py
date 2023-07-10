#Homework: Requires you to set up a basic calc; all they want you to do is print text 
#Will try and use my knowledge to see how far I can stretch it without needing help 

print("This is a basic calculator; I will take user input and then return double the value provided")

#This function takes a single variable and then doubles the variable; the generated doubled value is then assigned into a new variable and returned 
def calc_doubler(var_x):
    doubled_val = var_x * 2 
    return doubled_val 

#The input method prints text and collects user input; the collected user input is then assigned into the var 
player_1_input = input("Please provide a number to be doubled: \n")

#The collected user input is then wrapped and converted into an int so it can be used in the function 
player_1_input_int = int(player_1_input)

#The function is called and the int player 1 input supplied into the function; the returned output from the func is then assigned into a new variable
response = calc_doubler(player_1_input_int)

print(f"The value you provided was: {player_1_input_int}")
print("\n")

#New variable is then printed for the user to see 
print(f"Your doubled value is: {response}")

