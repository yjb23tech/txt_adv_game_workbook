print("\nForward\n")

def get_player_command(var_player_name):
    var_player_command = input(f"\nWhere are you headed {var_player_name}? Be quick about it!\n")
    return var_player_command 

def play():

    print("\nTo Asgard!\n")
    ui_player_name = input("\nWhat is your name Warrior?\n")

    ui_bool_game_is_on = True 

    while(ui_bool_game_is_on == True):
    
        ui_player_command = get_player_command(ui_player_name)

        if (ui_player_command.lower() == 'n') or (ui_player_command.lower() == 'north'):
            print(f"\n{ui_player_command} it is {ui_player_name}... let us move with haste!\n")
        elif (ui_player_command.lower() == 'e') or (ui_player_command.lower() == 'east'):
            print(f"\n{ui_player_command}? Are you sure? As you wish...\n")
        elif (ui_player_command.lower() == 'w') or (ui_player_command.lower() == 'west'):
            print(f"\nThe Wicked Witch of the {ui_player_command} lies in this direction - we must keep our guard up Asgardian!\n")
        elif (ui_player_command.lower() == 's') or (ui_player_command.lower() == 'south'):
            print(f"\n{ui_player_command} promises nothing but misery {ui_player_name}\n")
        else:
            print(f"\nRest {ui_player_name}. Your Odyssey has come to end.\n")
            ui_bool_game_is_on = False

play()

