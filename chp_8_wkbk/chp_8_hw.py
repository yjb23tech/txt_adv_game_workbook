#print("Still completing homework at age 29")

class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein 
        self.fat = fat

    def __str__(self):
        return (f"This piece of {self.name} has {self.carbs} grams of carbs, {self.protein} grams of protein and {self.fat} grams of fat")

test_chicken_thigh = Food("Chicken Thigh", 100, 200, 300)

print(test_chicken_thigh)
