#print("Over the course of the book, the mains of the book will invite me to add to the central game file; this will be done here")
#This is titled sandbox as it's a great place to practice; I'll be building the real game in it's entirety elsewhere in due course

print("\nEscape from Wano!")

#Input func is used to record user input
#action_input = input("Samurai! Where to next? \n")

ui_bool_game_on = True 

while (ui_bool_game_on == True):

    action_input = input("\nWhere to next, Samurai?\n")

    if ((action_input.lower()) == "north") or ((action_input.upper()) == "N"): 
        #The user input provided is then printed back to the User
        print(f"\nYou're now travelling North! Be careful... there is danger ahead\n")
    elif ((action_input.lower()) == "south") or ((action_input.upper()) == "S"):
        print(f"You're now travelling South my killy")
    elif ((action_input.lower()) == "west") or ((action_input.upper()) == "W"):
        print(f"West LunDun stanna up!")
    elif ((action_input.lower()) == "east") or ((action_input.upper()) == "E"):
        print(f"I'm from East London where the mandem are BOOP!")
    else:
        print("Now you die")
        ui_bool_game_on = False 

print("\nThe End\n")




