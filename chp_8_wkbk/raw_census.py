#Leaning
#print("UTOPIA")

class Person():
    def __init__(self, str_name, int_age, arr_best_cities):
        self.str_name = str_name
        self.int_age = int_age
        self.arr_best_cities = arr_best_cities 

    def __str__(self):
        return (f"Name: {self.str_name}, Age: {self.int_age}, Best Cities: {self.arr_best_cities}")

    def birth_year(self):
        return (2023 - self.int_age)

def ui_name():
    return input("\nWhat is your name?\n")

def ui_age():
    return (int(input("\nHow old are you?\n")))

def ui_best_cities():
    arr_ui_best_cities = [] 
    while (len(arr_ui_best_cities) < 3):
        ui_best_city = input("\nName one of your favorite cities:\n")
        arr_ui_best_cities.append(ui_best_city)
    print(" ")
    return arr_ui_best_cities

print("Hello HI")

ui_player_avatar = Person(ui_name(), ui_age(), ui_best_cities())
print(ui_player_avatar)

