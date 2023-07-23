#Find the middle value of an array of any given odd length 
#print("The Roaring 20s")

def middle_value(arr_odd_len):

    print("\nThis function will search and find the middle value of an array on the condition the array is of odd length")
    print("How long is this array?")
    print(" ")

    for item in arr_odd_len:
        print(f"{(arr_odd_len.index(item)) + 1}. {item}")

    print(f"\nThis array has {len(arr_odd_len)} items\n")


arr_test = ['Magic', 'Bird', 'Olajuwon', 'Jordan', 'Ewing']

middle_value(arr_test)
 
