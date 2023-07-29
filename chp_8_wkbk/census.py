#Census.py
#print("Working with Classes and Objects")

class Person:
    str_name = "Frank"
    int_age = 47 
    arr_fav_foods = ['Spaghetti', 'Gabagool', 'Baked Zitti', 'Artichokes', 'Carbonara'] 

    def birth_year(self):
        return (2023 - self.int_age)

    def list_fav_foods(self):
        for food in self.arr_fav_foods:
            print(f"I like to eat {food}")
        print(" ")

person_frank_soprano = Person()

print(f"\nMy name is {person_frank_soprano.str_name} and I was born in the year {person_frank_soprano.birth_year()}\n")
print("Food is a large part of my culture; here is a list of my favorite foods:\n")

person_frank_soprano.list_fav_foods()

