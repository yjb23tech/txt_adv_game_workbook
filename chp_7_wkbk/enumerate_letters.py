#print("Current weakness relates to enumerate() and tuples; will take a look here")

arr_letters = ['a', 'b', 'c', 'd', 'e'] 

print(" ")
for letter in arr_letters:
    print(f" Hello *{letter}")

print(" ")

#At each index location in the collection returned by the enumerate() you get access to two items
#You get access to the index location itself (which you can actually adjust i.e. set) which maps into i
#You also get access to the item that was stored at the corresponding index location based on the arr originally fed into the enumerate() 
#For example at index location '0' you had access to item 'a', at index location '1' you had access to item 'b' 
#In the enumerator object returned, you get both of these values coupled together at the index location 
#So at index location '0' you get access to both '0' and 'a' in the form (0, 'a') 

for i, value in enumerate(arr_letters):
    print(f"At {i} we have {value}")

    print(f"At {i+1} which is the original index location above +1 to make it readable we have {value}")

#I wonder if you can treat the enumerator object like a 2D array? How do I get access to 'a' by itself? Is that possible? 

#This works 
enum_arr_letters = enumerate(arr_letters) 
for i, value in enum_arr_letters:
    print(f"At {i} we have {value}")

#Doesn't seem to work 
#print(f"What do we have here? {enum_arr_letters[0][1]}")

