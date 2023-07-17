#Example as shown in the book 
def say_hello():
    print("\nHello, World\n")

say_hello()

answer = input("\nWould you like another greeting?\n")
if answer == 'y':
    say_hello()

#Taking the example further 
def say_goodbye():
    print("\nGoodbye Dr Strange\n")

answer_2 = input("\nWould you like to say goodnight?\n")

if ((answer_2.lower()) == 'y') or ((answer_2.upper()) == 'YES'):
    say_goodbye()
else:
    print("fukumean")


