print("\nHeil Ultron\n")

ui_string_name = input("\nWho're you, Warrior?\n")
print(f"\nYour name is {ui_string_name}? Son of Odin? I knew your father: he was a good man\n")

arr_war_chest = ['Sword', 'Gauntlets', 'Hammer', 'Mjolnir'] 

print("Use the number pad to choose your weapon\n")

int_war_chest_counter = 1 

for weapon in arr_war_chest: 
    print(f"To wield the {weapon}, choose {int_war_chest_counter}")
    int_war_chest_counter += 1 

ui_int_war_chest_selection = int(input("\nChoose.\n"))

print(f"I can see you have chosen {arr_war_chest[(ui_int_war_chest_selection) - 1]}; it is time to go to war {ui_string_name}, son of Odin")

print("Let me see your weapon... I can tell the strength by feel alone, greenhorn")

if (ui_int_war_chest_selection >= 1) and (ui_int_war_chest_selection < 3):
    print("This is an attack weapon... wield with caution") 
else: 
    print("HAMMER HAHAHA!")





