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




