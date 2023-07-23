#Find the middle value of an array of any given odd length 
#print("The Roaring 20s")

def middle_value(arr_odd_len):

    print("\nThis function will search and find the middle value of an array on the condition the array is of odd length")
    print("How long is this array?")
    print(" ")

    for item in arr_odd_len:
        print(f"{(arr_odd_len.index(item)) + 1}. {item}")

    print(f"\nThis array has {len(arr_odd_len)} items\n")

    if ((len(arr_odd_len) % 2) == 0):
        print("\nThis array has an even number of items; we cannot at present accurately provide the middle value :S\n")
    else:
        print("\nThis array has an even number of items: we can provide the middle value :D\n")

        middle_value_loc_lit = int((len(arr_odd_len) + 1) / 2)
        middle_value_loc_index = int(middle_value_loc_lit - 1)

        print(f"The middle item in this array is {arr_odd_len[middle_value_loc_index]}") 

arr_test_even = ['Magic', 'Bird', 'Olajuwon', 'Jordan', 'Ewing', 'Kobe']
arr_test_odd = ['Kyrie', 'Wade', 'LeBron', 'Giannis', 'Jokic']

middle_value(arr_test_even)
middle_value(arr_test_odd)
