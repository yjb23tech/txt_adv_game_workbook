#Class Crime Boss will be created; using the __init__() method properties will be declared and initialized immediately so that upon Object creation these properties can be set immediately 
#print("Young Tony Stark")

class Mob_Boss:
    def __init__(self, str_name, int_age, arr_fav_foods):
        self.str_name = str_name
        self.int_age = int_age
        self.arr_fav_foods = arr_fav_foods 

    def birth_year(self):
        return (2023 - self.int_age)

def mb_first_name():
    return input("\nWhat is your name?\n")

def mb_age():
    return int(input("\nHow old are you?\n"))

def mb_fav_foods():
    arr_ui_fav_foods = [] 
    while (len(arr_ui_fav_foods) < 3):
        arr_ui_fav_food = input("\nWhat is your fave food Boss?\n")
        arr_ui_fav_foods.append(arr_ui_fav_food)

    print("Your collection of fave foods is now complete; gracias Senor")
    return arr_ui_fav_foods 

mb_carmine_lupertazzi = Mob_Boss("Carmine Lupertazzi", 33, ['Seafood Risotto', 'Lasagna'])
print(f"\nCiao Bella! My name is {mb_carmine_lupertazzi.str_name} and I am {mb_carmine_lupertazzi.int_age} years old\n")

#Although both the Objects 'mb_carmine_lupertazzi' and 'mb_player' both use the same Class for instantiation, the manner in which each Object leverages the __init__() method is different
#In the former, we explicitly declare the params as soon as the Object is created 
#In the latter, as seen below, we call functions to handle the provision of each parameter; the __init__() method for the Mob_Boss Class takes a str, an int and an arr respectively 
#The return types of each function called below perfectly maps to the desired data types for the params; this shows us as long as there is parity between the return type of a function and the data types
#--> required by the function the returnees are being fed into, this architechture will work! Great success! 

mb_player = Mob_Boss(mb_first_name(), mb_age(), mb_fav_foods())

print(f"\nMazel Tov! My name is {mb_player.str_name} and I am {mb_player.int_age} years old\n")
print(f"I was born in the year {mb_player.birth_year()} - a great year to be a gangster")
print("My fave foods can be found below:\n")

for food in mb_player.arr_fav_foods:
    print(f"I like to eat {food}")
print(" ")



