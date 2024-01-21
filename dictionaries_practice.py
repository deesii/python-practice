# Creating a dictionary

person = {"name" : "Donna" , "nationality" : "British", "Favourite_programming_language": "Python"}


#reading the individual values asscoiated with the key

print(person["name"])

capital_cities = {"England" : "London" , "Spain" : "Madrid", "France": "Paris", "Norway": "Oslo", "Sweden": "Stockholm"}

ages = {"12": "bobby", "13":"Sally"}

print(ages["12"])


ages_test = {12: "bobby", "13":"Sally"}
print(ages_test[12])

# Addimg key-value pairs

person["birthday"] = "31 January"

print(person)

# Dictionary methods:

# keys() -  probabaly outputs the keys as a VIEW OBJECT  and can set to a variable > make it a list via list() and set to another varaible to store the keys as a list
# values() - probably outputs the values VIEW OBJECT , and can probably set to a variable > make it a list via list() and set to another varaible to store the values as a list
# get(key) - outputs the value specifically associated with the key, and can set to a variable
# items() - outputs VIEW OBJECT of a list of tuples, and can probably set to a variable > make it a list via list() and set to another varaible to store the values as a list
# pop(key) - can get the key and value associated with it - mutable and immutable ? Can pop to a new variable, while changing the original dictionary?
# clear() - must clear out the original dictionary, whilst keep the variable in memory
# setdefault(key, default) - method in Python is used to retrieve the value for a given key in a dictionary. If the key is present in the dictionary, it returns the corresponding value. 
#If the key is not present, it inserts the key with a default value (which you provide) and returns that default value. Could be useful for counts!


# Example: Counting occurrences of words in a list
word_list = ["apple", "banana", "orange", "apple", "banana", "grape", "apple"]

word_count = {}

for word in word_list:
    # Increment the count for the word, defaulting to 0 if the word is not in the dictionary
    word_count[word] = word_count.setdefault(word, 0) + 1

print(word_count)



# What is a VIEW OBJECT - When you print(type(person.keys()) ---> the output is <class "dict_keys">

print(person.keys())
print(person.values())

person_keys_list = list(person.keys())
print(type(person.keys()))
print(person_keys_list)

blob = person.get("name")
print(blob)

#items() practice

print(type(person.items()))
print(list(person.items()))

list_tuples_person  = list(person.items())
print(type(list_tuples_person[0]))