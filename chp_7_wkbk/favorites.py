#print("Apotheosis")

arr_favorites = []
arr_ui_options = ['add a new item', 'quit'] 
more_items = True 

def print_starred_list(arr_items_to_list):

    #[1] on Loop Counters: using an incrementable var outside of the for loop as a loop counter; once loop is run, var is incremented at very end and new value in i to be used during next loop iteration
    # i = 1   
    #for item in arr_items_to_list: 
        #print(f"*{i} " + str(item))
        #i += 1 

    #[2] on Loop Counters: uses the range() which takes an int [given by using len(arr) - which tells you the number of items in an arr aka the size] and then returns a zero indexed arr against the int
    #This approach is very similar to my arr_example.index(item) + 1 approach; I actually prefer mine better; in this [2] instance the loop is run on the array returned by range(), not the primary arr
    #You then use the indexes returned as the indices to feed into your get call on your primary arr 
    #range() returns a zero indexed based array of individual items which spans the width of the initial int input; so if the input into range() is the int '5' you will get an arr: [0, 1, 2, 3, 4] 
    #This returned range() object can acc be stored in a var and the var used as an arr within a standard for loop as normal
    #Trick is to use the items stored in the arr as indices which map to corresponding items in the primary array fed into len() ==> which was then fed into ==> range() 
    for i in range(len(arr_items_to_list)):
        print(f"{i+1}. {arr_items_to_list[i]}")
     


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

#What can a range object actually do? Can it be assigned and stored in a variable which will act as a pointer to this range object i.e. modded array (list)? 

arr_range_objects = range(len(arr_favorites))
print(" ")
for object in arr_range_objects:
    print(f"And here we have a: {object}")

#Who woulda thunk? Look UP ^^

print("\nThank you for shopping with us today - come back soon!\n")
