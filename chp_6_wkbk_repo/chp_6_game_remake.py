print("Rebuilding the game once more, using details from Chp 6")

def play():
    inventory = ['Dagger', 'Gold(5)', 'Crusty Bread']
    ui_bool_game_is_on = True

    while (ui_bool_game_is_on == True):

        ui_player_action = input("\nWhat next, Sailor?\n")

        if ui_player_action in ['n', 'N', '^']:
            print("\nYou're now travelling North")
        elif ui_player_action in ['e', 'E', '>']:
            print("\nYou're now travelling East")
        elif ui_player_action in ['s', 'S']:
            print("\nYou're now travelling South")
        elif ui_player_action in ['w', 'W', '<']:
            print("\nYou're now travelling West")
        elif ui_player_action in ['i', 'I']:
            print(" ")
            for item in inventory:
                print(f"You can use your: {item} if you choose so")
        elif ui_player_action in ['q', 'Q']:
            print("\nJourney well, Sailor")
            ui_bool_game_is_on = False 
        else:
            print("Try again Sailor")


play()
print("Rest well, Sailor")
    
