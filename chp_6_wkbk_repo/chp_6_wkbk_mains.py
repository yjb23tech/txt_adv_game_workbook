print("Locked in once more")

#Here, the aim is to work with the list (array) data structure and apply the methods, functions that were described 

arr_nba_superstars_90s = ['Magic', 'Jordan', 'Bird', 'Malone', 'Olajuwon'] 
arr_nba_superstars_post_90s = ['Curry', 'Kobe', 'LeBron', 'Duncan', 'Shaq']

print("\nThe lates 80s and 90s was an amazing time for NBA basketball\n")

#The array is composed of string values 
#The individual string value mapped into the 'superstar_90s' variable can then be fed into the .index() method to return the index associated with that value
#Because the array is 0 indexed based, after returning the index value we then +1 to it so it better corresponds to the actual position a player played in basketball (very clever) 
for superstar_90s in arr_nba_superstars_90s:
    print(f"{superstar_90s} was the greatest at the {(arr_nba_superstars_90s.index(superstar_90s)) + 1} we'd ever seen up until the 2000s")

print("\nEnd\n") 

