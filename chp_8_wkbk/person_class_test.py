print("I will create a Class to model a Person")

class Person:
    age = 15 
    name = "Dmitri"

    def birth_year(self):
        return (2015 - self.age)

russian_person = Person()

print(f"Hello my name is {russian_person.name}\n")
print(f"I was born in the year {russian_person.birth_year()}")

