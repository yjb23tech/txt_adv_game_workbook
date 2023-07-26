#print("Apotheosis")

arr_favorites = []
arr_ui_options = ['add a new item', 'quit'] 
more_items = True 

def print_starred_list(arr_items_to_list):

    #[1] on Loop Counters: using an incrementable var outside of the for loop as a loop counter; once loop is run, var is incremented at very end and new value in i to be used during next loop iteration
    i = 1   
    for item in arr_items_to_list: 
        print(f"*{i} " + str(item))
        i += 1 

while more_items:
        
    print("\nYou have the following options available to you:\n")
    for option in arr_ui_options:
        print(f"You can {option}")

    ui_option = input(f"\nWhat would you like to do to?\n")

    if ui_option in ['Quit', 'quit', 'Q', 'q']:
        print("Thank you for shopping with us today :D")
        more_items = False
    else:
        arr_favorites.append(ui_option)


print("\nThat's a great big shop you have there! You have chosen to buy the following items:\n")

for fave in arr_favorites:
    print(f"{(arr_favorites.index(fave)) + 1}. {fave}")

if (len(arr_favorites) <= 5):
    print("Please proceed into the express lane - ZOOM ZOOM!")
else:
    print("\nYou have more than 5 items Sir! You'll have to join the back of the standard main cue I'm afraid!\n")

print_starred_list(arr_favorites)

print("\nThank you for shopping with us today - come back soon!\n")
