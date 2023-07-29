class Person: 
    str_first_name = "Lucky"
    str_last_name = "Lucciano"
    int_age = 47 
    arr_fav_foods = ['Seafood Risotto', 'German Riesling'] 

    def birth_year(self):
        return (2023 - self.int_age)

    def list_fav_foods(self):
        i = 1 
        for food in self.arr_fav_foods:
            print(f"{i}. {food}")
            i += 1 
       
p_lucky_lucciano = Person()

print(f"\nCiao! My name is {p_lucky_lucciano.str_first_name} {p_lucky_lucciano.str_last_name} and I am {p_lucky_lucciano.int_age}\n")
print(f"On a good day, when the business is running smooth, I like to eat the following:\n")
p_lucky_lucciano.list_fav_foods()

crime_bosses = [Person(), Person(), Person(), Person()] 

print(f"\nIn New York there are {(len(crime_bosses) + 1)} mob bosses in total")
print(f"In an ideal world, the heads of each crime family would look like this:\n")

for crime_boss in crime_bosses:
    print(f"{crime_bosses.index(crime_boss) + 1}. {crime_boss.str_first_name} {crime_boss.str_last_name}" + str(crime_boss))

print("\nBut as this isn't possible - sigh - each Family has it's own unique leader. Come and meet the Head of each family:\n")

for crime_boss in crime_bosses:
    crime_boss.str_first_name = input(f"My first name is:\n")
    crime_boss.str_last_name = input(f"My last name is:\n") 
    crime_boss.int_age = input(f"My age is:\n")
    print(" ")

for id in range(len(crime_bosses)):
    print(f"Here we have {crime_bosses[id].str_first_name} of the {crime_bosses[id].str_last_name} family")
    print(f"He was {crime_bosses[id].int_age} when he became Head of the organisation")
    print(" ")


        

 
