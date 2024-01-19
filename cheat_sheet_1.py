#examples of conditionals

name = "Edward"
print(len(name))
if len(name) > 25:
    print("That is a very long name")
elif len(name) > 20:
    print("That is a long name")
elif len(name) > 10:
    print("blablabla")


#example of a while loop
    
from random import randint

fav_number = 77
guess_correct = False

while not guess_correct:
    guess = randint(0, 100)
    if guess == fav_number:
        print("You guessed right: 77!")
        guess_correct = True
    else:
        print(f"{guess} is wrong! Try again.")

#using a for loop to print out the numbers between 50 and 100 in steps of 3 to demo for loop and range()
        
for num in range(50, 101, 3):
    print(num)