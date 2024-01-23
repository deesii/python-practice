# In this section, you'll learn to:

# Search for elements in a list using filter
# Search for elements in a list using list comprehensions
# Transform elements in a list using map

passwords = [
{"service": "takeaway", "password": "asdf", "added_on": "21/03/22"},
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
{'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]
def is_acebook(password):
    return password['service'] == 'acebook' # returns true if the value to the key "service" is "acebook"

print((list(filter(is_acebook, passwords))[0])) # filter takes the true element, and filters the list by that

# next item in the iterable having done filter via the function is_acebook(facebook) - # To grab the first element of an iterable, we use `next()`.

print((next(filter(is_acebook, passwords))))


#using lambda as a function with "no name":



print(next(filter(lambda password: password['service'] == 'acebook', passwords))) # lambda declares function with single argument password, filtering by those that satisfy the boolean statment

#A lambda function will automatically return the value of the expressionin its body.

# practice using list comprehensions

print([password for password in passwords if password['service'] == 'acebook'][0])

print(next(iter([password for password in passwords if password['service'] == 'acebook']))) # if you do next([]), you have error that the list is not iterator Therefore have to make it iter([list_comprehension])

#Iterator:

# An iterator is an object representing a stream of data. It maintains state and produces the next value when the __next__() method is called.
# You obtain an iterator from an iterable using the iter() function.

# ---- # 

def are_all_passwords_long_enough (passwords):
    for password in passwords:
        if len(password["password"]) < 8:
            return False
    return True

print(are_all_passwords_long_enough(passwords))

def is_too_short(password):
    return len(password["password"]) < 8

def are_all_passwords_long_enough(passwords):
    return len(list(filter(is_too_short, passwords))) == 0 # if the length of the list is 0, it means no passwords were less than 8. 

print(are_all_passwords_long_enough(passwords))

def are_all_passwords_long_enough(passwords):
    return len(list(filter(lambda password: len(password["password"]) < 8, passwords))) == 0


print(are_all_passwords_long_enough(passwords))


def are_all_passwords_long_enough(passwords):
    return len([password for password in passwords if len(password["password"]) < 8] ) == 0


print(are_all_passwords_long_enough(passwords))


# ---Write a function that checks whether any passwords were added on 21/03/22 --# 

#using list comprehension: 

def check_date_password (passwords,date):
    return len([password for password in passwords if password["added_on"] == date]) > 0

print(check_date_password(passwords,"21/03/22"))

#using lambda function:

def check_date_password (passwords,date):
    return len(list(filter(lambda password: password["added_on"] == date, passwords))) > 0


print(check_date_password(passwords,"21/03/22"))

#using any function

def check_is_date (passwords):
    return any(password for password in passwords if password["added_on"] =="21/03/22")
        

print(check_is_date(passwords))

#using for loops

def check_is_date(passwords):
    for password in passwords:
        if password["added_on"] == "21/03/22":
            return True
    return False

print(check_is_date(passwords))

# using boolean function for individual element in the list to be applied via the filter function 

def check_date(password):
    return password["added_on"] == "21/03/22"

def check_date_password(passwords):
    return len(list(filter(check_date, passwords))) > 0

# Write a function that returns a list of all passwords added on 22/03/22

# using list comprehension

def list_passwords_date (passwords):
    return [password["password"] for password in passwords if password["added_on"] == "22/03/22"]

print(list_passwords_date(passwords))

#using lambda

def list_passwords_date (passwords):
    list_password_satisfied = []
    for password in passwords:
        if password["added_on"] == "22/03/22":
            list_password_satisfied.append(password["password"])
    return list_password_satisfied

print(list_passwords_date(passwords))

#map

#applying a function to eveery element in that list, and return a new result --> not in place

result = map(lambda number: number * 2, [1, 2, 3, 4])
print(list(result))


#alternately, using list comprehension!

print([number * 2 for number in [1, 2, 3, 4]])


# to achieve the above:

list_numbers = [1,2,3,4]

list_numbers_doubled = []
for num in list_numbers:
    list_numbers_doubled.append(num * 2)

print(list_numbers_doubled)
