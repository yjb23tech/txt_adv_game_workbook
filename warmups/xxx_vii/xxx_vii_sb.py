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



            

