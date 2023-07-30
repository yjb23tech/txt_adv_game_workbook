print("Sandbox actvities")

#First 10 multiples of numbers 1 to 7 

for x in range(1,8):
    print(f"Here are the first 10 multiples of {x}:\n")
    for y in range(1, 11):
        print(f"{x*y}")
    print(" ") 

#Print all of the factors for each number between 1 to 10 

for x in range(1, 11):
    arr_factors = [] 
    print(f"Here are all of the factors of {x}")
    for y in range(1, x+1): 
        if ((x % y) == 0):
            print(f"The number {y} is a factor of the number {x}")
            arr_factors.append(y)
        else:
            print(f"The number {y} is not a factor of the number {x}")
    print(f"\nHere are all of the factors of {x}: {arr_factors}\n")

#Find the middle item within an arr of odd length 

arr_odd = ['Luffy', 'Red Shanks', 'Kaido', 'Big Mom', 'Black Beard'] 

print("Within my array, I have the following items:\n")
for odd in arr_odd:
    print(f"{(arr_odd.index(odd)) + 1}. {odd}") 
print(" ")

def middle_of_arr(arr_x):
    middle_item_loc = int((len(arr_x) + 1) / 2) 
    middle_item_index = middle_item_loc - 1

    middle_item_value = arr_x[middle_item_index] 
    return middle_item_value 

print(f"The middle value of my collection is: {middle_of_arr(arr_odd)}")



