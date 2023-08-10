#print("Still completing homework at age 29")

class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein 
        self.fat = fat

    def __str__(self):
        return (f"This piece of {self.name} has {self.carbs} grams of carbs, {self.protein} grams of protein and {self.fat} grams of fat")

    def total_calorie_count(self):
        total_calories = (self.carbs * 4) + (self.protein * 4) + (self.fat * 9)
        return str(f"If you were to consume this piece of {self.name} you would be eating {total_calories} worth of calories")

test_chicken_thigh = Food("Chicken Thigh", 100, 200, 300)

print(test_chicken_thigh)
print(test_chicken_thigh.total_calorie_count())
