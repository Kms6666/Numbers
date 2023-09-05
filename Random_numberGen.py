import random
#imports libraries that add functionality

x = input("pick a number between 1 and 100: ")

y = random.randint(1,100)

print("You picked " + x + " and the number " + str(y) + " was generated")
#prints user input and random integer with regstring

print(f"You picked {x} and the number generated was {y}".format(x,y))
#print two values using f-string

if int(x) < y:
    print("too low")
if int(x) > y:
    print("too high")
if int(x) == y:
    print("correct!")
