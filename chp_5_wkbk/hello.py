#Example as shown in the book 
def say_hello(var_name):
    print("\nHello " + var_name)

answer = input("\nWould you like a greeting?\n")
if answer == 'y':
    say_hello('Tino')

#Taking the example further 
def say_goodbye():
    print("\nGoodbye Dr Strange\n")

answer_2 = input("\nWould you like to say goodnight?\n")

if ((answer_2.lower()) == 'y') or ((answer_2.upper()) == 'YES'):
    say_goodbye()
else:
    print("fukumean")


answer_3 = input("\nWho're you, Warrior?\n")

say_hello(answer_3)

