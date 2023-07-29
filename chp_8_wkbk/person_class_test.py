print("I will create a Class to model a Person")

class Person:
    age = 15 
    name = "Dmitri"

    #To use a Class based property within a Class based method, you need to pass the keyword 'self' into the method
    #I imagine what this does is that it grants the Class based method access to all of the properties and methods within the class; it is effectively explicit self-referencing 
    #The Class based method is explicitly instructed to access the described Class based property referenced i.e. use the 'age' property associated with the self-referencing object 
    def birth_year(self):
        return (2015 - self.age)

russian_person = Person()

print(f"Hello my name is {russian_person.name}\n")
print(f"I was born in the year {russian_person.birth_year()}")

