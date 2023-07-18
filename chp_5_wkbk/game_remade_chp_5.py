print("Forward")

def get_player_command(var_player_name):
    var_player_command = input(f"\nWhere are you headed {var_player_name}? Be quick about it!\n")
    return var_player_command 

ui_player_name = input("\nWhat is your name Warrior?\n")

ui_player_command = get_player_command(ui_player_name)

print(f"\n{ui_player_command} it is {ui_player_name}... let us move with haste!\n")

