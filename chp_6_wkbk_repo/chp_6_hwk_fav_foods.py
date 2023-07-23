#print("Pushing On")

#Write code that allows users to enter their three favorite foods; store those foods in a list 

def fav_foods():

    ui_bool_searching_for_food = True 
    arr_fav_foods = [] 

    while (len(arr_fav_foods) < 3):
        ui_fav_food = input("\nName one of your favorite foods and add it to the list:\n")
        arr_fav_foods.append(ui_fav_food)

    print(" ")
    for food in arr_fav_foods:
        print(f"At number {(arr_fav_foods.index(food)) + 1} your favorite food is: {food}\n")
        

 
fav_foods()        
