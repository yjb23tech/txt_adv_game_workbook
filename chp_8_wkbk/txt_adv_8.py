#print("Escape from Greed Island")

arr_action_options = ['N to travel North', 'E to travel East', 'W to travel West', 'S to travel South', 'I to view the items in your Inventory', 'Q to save and Quit the game'] 
arr_inventory_items = ['Dagger', 'Broad Sword', 'Healing Herbs', 'Crusty Bread', 'Gold(5)'] 

def play():

    bool_game_is_on = True 
    print("\nEscape from Greed Island -_____-\n")

    while (bool_game_is_on):
        print("Hurry Captain! What do we do?\nMake a decision - QUICK!\n")
        for x, action in enumerate(arr_action_options, 1):
            print(f"{x}.Press {action}")
            
        ui_action = input("\nWhat would you like to do\n")
        
        #Compare ui_action against available options; respond accordingly 
        if ui_action in ['NORTH', 'north', 'North', 'N', 'n', '^']:
            print("Excellent choice - we march NORTH!\n")
        elif ui_action in ['EAST', 'east', 'East', 'E', 'e', '>']:
            print("The Beast of the East is an unforgiving creature Captain! We must tread carefully :S\n")
        elif ui_action in ['SOUTH', 'south', 'South', 'S', 's' 'v']:
            print("The cannons to the South are particularly violent Honcho :'S never underestimate the people of the Southern waters XD\n")
        elif ui_action in ['WEST', 'west', 'West', 'W', 'w', '<']:
            print("The Wicked Witch of the West... may GxD be with us all\n")
        elif ui_action in ['INVENTORY', 'inventory', 'Inventory', 'I', 'i']:
            print("\nWelcome to your inventory :D here are all of the items you've collected during your pillaging:\n")
            for x in range(len(arr_inventory_items)):
                print(f"{x+1}. {arr_inventory_items[x]}")
            print(" ")
        elif ui_action in ['QUIT', 'quit', 'Quit', 'Q', 'q']:
            print("Jolly Roger! Looks like ya wanna quit - you sure you're ready to drop anchor and call it a day?\n")
            ui_action = input("If you wish to Quit please confirm by typing the word Q-U-I-T; if not, the game will resume as normal:\n")
            if ((ui_action.upper()) == "QUIT"):
                print("Until next time Captain!")
                bool_game_is_on = False
            else:
                print("Set sail once more ya bloody landlubbers XD")
        else:
            print("Invalid input, try again!")


play()
