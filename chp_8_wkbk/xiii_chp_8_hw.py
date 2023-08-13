#print("Family Ties")
#Recipe hw piece 

class Recipe:
    def __init__(self, str_name, arr_ingredients):
        self.str_name = str_name
        self.arr_ingredients = arr_ingredients 

    def __str__(self):
        return self.str_name

    def calories(self):
        
        total_recipe_calorie_count = 0 

        for ingredient in self.arr_ingredients:
            
            ui_macro_group = input(f"\nYou have included {ingredient} within your recipe; is this ingredient primarily a carbohydrate, protein or fat?\n") 

            if ui_macro_group in ['Carbohydrate', 'CARBOHYDRATE', 'carbohydrate']:
                ui_carb_mass = int(input(f"How much {ingredient} do you need in your recipe?\n"))
                total_carb_calories = ui_carb_mass * 4
                total_recipe_calorie_count += total_carb_calories
 
                print(f"Your recipe contains {ingredient} with {total_carb_calories} calories coming from {ui_carb_mass} grams of carbohydrates")          

            elif ui_macro_group in ['Protein', 'PROTEIN', 'protein']:
                ui_protein_mass = int(input(f"How much {ingredient} do you need in the recipe?\n"))
                total_protein_calories = ui_protein_mass * 4 
                total_recipe_calorie_count += total_protein_calories 

                print(f"Your recipe contains {ingredient} with {total_protein_calories} calories coming from {ui_protein_mass} grams of proteins")

            elif ui_macro_group in ['Fat', 'FAT', 'fat']:
                ui_fat_mass = int(input(f"How much {ingredient} do you need in your recipe?\n"))
                total_fat_calories = ui_fat_mass * 9 
                total_recipe_calorie_count += total_fat_calories 

                print(f"Your recipe contains {ingredient} with {total_fat_calories} calories coming from {ui_fat_mass} grams of fat") 
            else:
                print("nothing to show so far")


        print(f"Your recipe for {self.str_name} has a total calorie count of {total_recipe_calorie_count} across carbohydrates, proteins and fats\n")
        return (total_recipe_calorie_count)        


def func_recipe_name():

    return input(f"\nWhat recipe would you like to make today?\n")

def func_recipe_ingredients():

    const_ingredient_list_MAX_SIZE = 3 
    arr_recipe_ingredients = [] 

    while (len(arr_recipe_ingredients) < const_ingredient_list_MAX_SIZE):
        
        ui_recipe_ingredient = input("\nWhat would you like to include in your recipe?\n")
        arr_recipe_ingredients.append(ui_recipe_ingredient)

    print(f"\nYour recipe has {len(arr_recipe_ingredients)} ingredients inside it - nice!")
    print("\nYour recipe contains the following ingredients:\n")

    for ingredient in arr_recipe_ingredients:
        print(f"{(arr_recipe_ingredients.index(ingredient)) + 1}. {ingredient}")

    return arr_recipe_ingredients     

def play():

    bool_game_is_on = True

    while (bool_game_is_on):

        print("\nWelcome to Cooking Mama! Are you ready to cook?")
        ui_start_game = input("\nPress 'Y' to start the game or 'N' to exit the game\n")

        if ui_start_game == 'Y':
            print("\nLet's start cooking!")
            ui_recipe = Recipe(func_recipe_name(), func_recipe_ingredients())
            print(" ")
            print(ui_recipe)
            ui_recipe_total_calories = ui_recipe.calories()
            print(f"{ui_recipe} has a total calorie count of: {ui_recipe_total_calories}")
        else:
            print("\nSee you soon!\n")
            bool_game_is_on = False 

play()

#test_recipe = Recipe("Soufle", ['Cheese', 'Eggs', 'Potatoes'])
#print(test_recipe)
#test_recipe_total_calorie_count = test_recipe.calories()
#print(f"{test_recipe} has a total calorie count of: {test_recipe_total_calorie_count}")


#Need to figure out how to calculate the total calorie count for a Recipe 
#Ideally, each recipe ingredient should be initially evaluated to determine whether it is primarily a carb, protein or fat 
#Once the categorisation is determined for the ingredient, the mass for the ingredient should be established
#Based on mass in grams and categerisation, the total calorie count for a given ingredient should be calculated 
#This value can then be stored in array
#Once the calories for the carb, protein and fat portion of the recipe has been calculated and stored these values should be accessed and looped through to add them all together
#Should result in total calorie count for the Recipe 

#test_recipe_ingredients = ['Chicken Thighs', 'Baked Potatoes', 'Butter'] 
#int_total_calorie_count = 0 

#for ingredient in test_recipe_ingredients:

#ui_macro_group = input(f"\nYou have included the ingredient {ingredient} in your recipe; is this ingredient primarily a carbohydrate, protein or fat?\n")
    
#if ui_macro_group in ['Carbohydrate', 'CARBOHYDRATE', 'carbohydrate', 'Carb', 'carb']:
#print(f"The ingredient {ingredient} has been classified as a Carbohydrate\n")
#ui_carb_mass = int(input(f"What is the mass of {ingredient} to be included in your recipe?\n"))
#total_carb_calories = ui_carb_mass * 4 
#int_total_calorie_count += total_carb_calories

    #elif ui_macro_group in ['Protein', 'PROTEIN', 'protein', 'Pro', 'pro']:
        #print(f"The ingredient {ingredient} has been classified as a Protein\n")
        #print(f"The ingredient {ingredient} has been classified as a Protein\n")
        #ui_protein_mass = int(input(f"What is the mass of {ingredient} to be included in your recipe?\n"))
        #total_protein_calories = ui_protein_mass * 4 
        #int_total_calorie_count += total_protein_calories
    #elif ui_macro_group in ['Fat', 'FAT', 'fat']:
        #print(f"The ingredient {ingredient} has been classified as a Fat\n")
        #ui_fat_mass = int(input(f"What is the mass of {ingredient} to be included in your recipe?\n"))
        #total_fat_calories = ui_fat_mass * 9 
        #int_total_calorie_count += total_fat_calories
    #else:
        #print("You have not chosen a valid macro grouping")

#print(f"\nThe total calorie count for your recipe is: {int_total_calorie_count}\n")

