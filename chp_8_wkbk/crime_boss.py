#Class Crime Boss will be created; using the __init__() method properties will be declared and initialized immediately so that upon Object creation these properties can be set immediately 
#print("Young Tony Stark")

class Mob_Boss:
    def __init__(self, str_name, int_age, arr_fav_foods):
        self.str_name = str_name
        self.int_age = int_age
        self.arr_fav_foods = arr_fav_foods 

def mb_first_name():
    return input("\nWhat is your name?\n")

def mb_age():
    return int(input("\nHow old are you?\n"))

mb_carmine_lupertazzi = Mob_Boss("Carmine Lupertazzi", 33, ['Seafood Risotto', 'Lasagna'])
print(f"\nCiao Bella! My name is {mb_carmine_lupertazzi.str_name} and I am {mb_carmine_lupertazzi.int_age} years old\n")

mb_player = Mob_Boss(mb_first_name(), mb_age(), ['King Prawn Linguine', 'Mozarella Balls'])
print(f"\nMazel Tov! My name is {mb_player.str_name} and I am {mb_player.int_age} years old\n")


