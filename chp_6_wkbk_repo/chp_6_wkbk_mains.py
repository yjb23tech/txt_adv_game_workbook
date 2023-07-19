print("Locked in once more")

#Here, the aim is to work with the list (array) data structure and apply the methods, functions that were described 

arr_nba_superstars_90s = ['Magic', 'Jordan', 'Bird', 'Malone', 'Olajuwon'] 
arr_nba_superstars_post_90s = ['Curry', 'Kobe', 'LeBron', 'Duncan', 'Shaq']

print("\nThe lates 80s and 90s was an amazing time for NBA basketball\n")

#The array is composed of string values 
#The individual string value mapped into the 'superstar_90s' variable can then be fed into the .index() method to return the index associated with that value
#Because the array is 0 indexed based, after returning the index value we then +1 to it so it better corresponds to the actual position a player played in basketball (very clever) 

#The work below offers an opportunity to get familiar with how to use the index method to return the 0 based index location of a known item within an array
for superstar_90s in arr_nba_superstars_90s:
    print(f"{superstar_90s} was the greatest at the {(arr_nba_superstars_90s.index(superstar_90s)) + 1} we'd ever seen up until the 2000s")

print("\nBut this is a young man's game and the modern era is here\n")
for superstar_post_90s in arr_nba_superstars_post_90s:
    print(f"{superstar_post_90s} is now the modern greatest at the {(arr_nba_superstars_post_90s.index(superstar_post_90s)) + 1} - oh how times have changed!")

#Using the .append() method 
print("\nAll is not lost however - even now, as we speak, the league is undergoing tectonic shifts and a changing of the guard is imminent\n")

#I declared and initialized an empty list (array) and then passed it into the len() function; I was accurately told the length i.e. size is 0 - I like that!
arr_nba_superstars_future = []
arr_nba_superstars_future_len = len(arr_nba_superstars_future)
print(f"\nThe current roster for the new superstars contains {arr_nba_superstars_future_len} players; are you ready to change this?\n")

var_arr_nba_superstars_future_counter = 0 

while ((len(arr_nba_superstars_future)) <= 4):

    ui_nba_superstars_future_selection = input(f"\nWho would you like to see at the {(var_arr_nba_superstars_future_counter) + 1} position?\n") 
    arr_nba_superstars_future.append(ui_nba_superstars_future_selection)
    print(f"\nSuper! You now have {ui_nba_superstars_future_selection} at the {(arr_nba_superstars_future.index(ui_nba_superstars_future_selection)) + 1} position!\n")
    var_arr_nba_superstars_future_counter += 1 

arr_nba_superstars_future_len = len(arr_nba_superstars_future)
print(f"\nYour roster for future superstars now contains {arr_nba_superstars_future_len} - here's your starting {arr_nba_superstars_future_len}:\n")


print("\nEnd\n") 

