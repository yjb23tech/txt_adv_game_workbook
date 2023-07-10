#This file will contain code solving tasks issued in the mains section of Chapter 4

#Mains: Exercise 1 

#ideally the player_1_ID would be object/class and the age of the player would be an attribute associated with the object; using a constant variable to model that for now
print("Can I have some ID Sailor? \n")
player_1_ID_age = 45

#Collect the age of the player using the input function and immediately convert it into an int
player_1_input_age = int(input("How old are you exactly? \n"))

#Print this value back to the user as confirmation their age was acknowledge by the NPC
print(f"\nAccording to your ID you are {player_1_ID_age} years old?")

#NPC compares the age on the ID against the verbally volunteered age
if player_1_ID_age == player_1_input_age:
    print("Here's your rum and coke - have a great day Sailor!")
else:
    print("I think you need a better fake ID mate - sod off")


#Mains: Exercise 2 
#Working with a single if/elif/else triad 

print("Back again I see; I suggest you stick to soft drinks - what would you like?")

#Player_1 provides a string and this is stored in a variable
player_1_drink = input("Hurry up ffs I have paying customers to attend to!\n")
print(f"You want a {player_1_drink}; let me see what we have...")

#NPC drink options are strings; also stored in variables
npc_drink_option_1 = "Coke" 
npc_drink_option_2 = "Fanta"

#NPC runs through an if/elif/else block to see whether the bar has the desired drink; if not, Sailor gets kicked to the curb
if player_1_drink == npc_drink_option_1:
    print("Can't go wrong with a classic - now bugger off")
elif player_1_drink == npc_drink_option_2:
    print("This is actually my fave drink too XD")
else: 
    print("Soz mate; now scarper before I clobber ya ears for ya!")




