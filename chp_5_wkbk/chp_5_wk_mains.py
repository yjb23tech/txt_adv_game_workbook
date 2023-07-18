print("\nAnytime, anyplace\n")

def say_hello(var_name):
    print("\nSAY HELLO TO MA LUH FWEND " + var_name)

say_hello('GID')

ui_user_name = input("\nWho are you?\n")

ui_bool_game_on = True

while (ui_bool_game_on == True):
    ui_chosen_one = input(f"\n{ui_user_name}... it cannot be! Are you, the child of prophecy?\n")

    if (ui_chosen_one.lower() == 'y') or (ui_chosen_one.lower() == 'yes'):
        say_hello(ui_user_name)
    else:
        print("Live another day, and never return")
        ui_bool_game_on = False  

print("The spell has been broken")


