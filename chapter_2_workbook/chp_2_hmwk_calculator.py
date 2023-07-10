print("Which numbers do you want to add?")

#This function takes an int value, doubles it and then returns the doubled value
def calc_doubler(var_x):
    doubler = var_x * 2
    return doubler

#User input is requested and a new line break is initiated in order to record the user input; the provided user input is then stored in the variable
player_1_input = input("Please provide a value to be used in the calculation\n")

#The recorded user input is then forcibly turned into an integer
player_1_input_int = int(player_1_input)

#The integer is fed into the function call; the returned double value is assigned into the variable response
response = calc_doubler(player_1_input_int)

#The returned value is then printed for the user's visibility 

print("\n")
print(f"The value you provided was: {player_1_input_int} ")
print("This value was then doubled to give: ")

print(response)


