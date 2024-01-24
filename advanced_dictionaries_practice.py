# using a for loop to create a dictionary


square_dict = {}
for num in range(1, 11):
    square_dict[num] = num*num

print(square_dict)

# using dictionary comprehension

square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)


for i in square_dict.items():
    print(i)

import random
# prints out tuples for of the individual key : value pairs
friends = ["Will", "Bernie", "Garth", "Suze"]
card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
random_dict = {friend:random.choice(card_suit) for friend in friends}
print(random_dict)

# to make sure there was no overlap of suits, you can use zip to zip up the list? 

friends = ["Will", "Bernie", "Garth", "Suze"]
card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
from random import shuffle
shuffle(card_suit)

card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}
print(card_friends)


shuffle(card_suit)

card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}

print(card_friends)

# The task below where you have to add the scores to the individiual values within the dictionary

tourny_dict = {"Dan":2, "Wolfgang":14, "June":43, "Tany":32, "Sharon": 8}
scores = [1, 3, 4, 3, 5]
index = 0
for team in tourny_dict:
    tourny_dict[team] += scores[index]
    index += 1

print(tourny_dict)

# filtering by a condition, using the standard for loop and then putting into a new dictionary:

tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}
next_round = {}
for player, score in tourny_dict.items():
    if score > 20:
        next_round[player] = score

print(next_round)


# And now using filter()
tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}
next_round = {}
next_round = dict(filter(lambda player: player[1] > 20, tourny_dict.items())) # the tourney_dict.items() produces the object of a list of the tuples! Can be used in teh filter()
print(next_round)

print(tourny_dict.items())

# using dictionary comprehension:

tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}

next_round = {key:value for (key,value) in tourny_dict.items() if value > 20} #The tourney_dict.items() produces the object of a list of the tuples! 

print(next_round)

# from the classes practice

list_pets = [{'name' : 'Arthur', 'animal' : 'cat'},
        {'name' : 'Judith', 'animal' : 'dog'},
        {'name' : 'Gwen', 'animal' : 'goldfish'}]


summary = ""
index = 0
print(len(list_pets))

for pet in list_pets[:-1]:
    summary += f"a {pet['animal']} called {pet['name']}, "
        

last_pet = list_pets[-1]

summary += f"a {last_pet['animal']} called {last_pet['name']}"

print(f"Bobby has {len(list_pets)} pets: {summary}")

