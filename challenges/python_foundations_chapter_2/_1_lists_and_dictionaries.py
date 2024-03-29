# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions.
#
# Most functions will take a list or a dictionary as an argument, but some will
# take other arguments and some won't take any.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1

def first_element(list):
    return list[0]


# Method name: second_element
# Purpose: returns the second element of the given list
# Arguments: one list
# Example:
#   Call:    second_element([1, 2, 3])
#   Returns: 2

def second_element(list):
    return list[1]

# Method name: last_element
# Purpose: returns the last element of the given list
# Arguments: one list
# Example:
#   Call:    last_element([1, 2, 3])
#   Returns: 3

def last_element(list):
    return list[-1]


# Method name: first_two_elements
# Purpose: returns the first two elements of the given list
# Arguments: one list
# Example:
#   Call:    first_two_elements([1, 2, 3])
#   Returns: [1, 2]

def first_two_elements(list):
    return list[0:2]

# Method name: first_three_elements
# Purpose: returns the first three elements of the given list
# Arguments: one list
# Example:
#   Call:    first_three_elements([1, 2, 3, 4])
#   Returns: [1, 2, 3]

def first_three_elements(list):
    return list[0:3]

# Method name: total
# Purpose: returns the sum of all the elements in the given list
# Arguments: one list
# Example:
#   Call:    total([1, 2, 3])
#   Returns: 6

def total (list):
    return sum(list)

# Method name: lowest_number
# Purpose: returns the lowest number in the given list
# Arguments: one list
# Example:
#   Call:    lowest_number([4, 2, 6])
#   Returns: 2

def lowest_number(list):
    return min(list)

# Method name: highest_number
# Purpose: returns the highest number in the given list
# Arguments: one list
# Example:
#   Call:    highest_number([4, 6, 2])
#   Returns: 6

def highest_number(list):
    return max(list)


# Method name: the_beatles
# Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# Arguments: none
# Example:
#   Call:    the_beatles()
#   Returns: ['john', 'paul', 'george', 'ringo']



def the_beatles():
    the_beatles = ["john", "paul", "george", "ringo"]
    return the_beatles

# Method name: i_joined_the_beatles
# Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one string
# Example:
#   Call:    i_joined_the_beatles('yoko')
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']

def i_joined_the_beatles(name):
    the_beatles = ["john", "paul", "george", "ringo"]
    the_beatles.append(name)
    return the_beatles

# Method name: we_joined_the_beatles
# Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one list
# Example:
#   Call:    we_joined_the_beatles(['yoko', 'stuart'])
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']

def we_joined_the_beatles(list_names_to_add):
    the_beatles = ["john", "paul", "george", "ringo"]
    for name in list_names_to_add:
        the_beatles.append(name)
    return the_beatles

# Method name: remove_nones_from_list
# Purpose: removes all the None values from the given list
# Arguments: one list
# Example:
#   Call:    remove_nones_from_list([1, None, 2, None, 3])
#   Returns: [1, 2, 3]

def remove_nones_from_list(list_to_filter):
    return  list(filter(lambda x : x is not None, list_to_filter)) 

# using a lambda function for filtering, note list() is appropriate here to converthe filter object into a list; 
#[filter()] creates a list with a single element, which is the filter object itself!

#[element for element in list if element != None] # using list comprehension 

# Method name: double_list
# Purpose: returns a list with all the elements of the given list repeated twice
# Arguments: one list
# Example:
#   Call:    double_list([1, 2, 3])
#   Returns: [1, 2, 3, 1, 2, 3]

def double_list(single_list):
    return 2 * single_list

# Method name: unique_elements
# Purpose: returns a list with all the unique elements of the given list
# Arguments: one list
# Example:
#   Call:    unique_elements([1, 2, 1, 3, 2, 3])
#   Returns: [1, 2, 3]

def unique_elements(list_original):
    return set(list_original)

# Method name: add_to_list
# Purpose: adds the given element to the given list
# Arguments: one list and one element
# Example:
#   Call:    add_to_list(["a", "b", "c"], "d")
#   Returns: ["a", "b", "c", "d"]

def add_to_list(one_list, to_add):
    one_list.append(to_add)
    return one_list


# == DICTIONARY EXERCISES ==

# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}

def new_band_member(dictionary_to_add):
    band_dictionary = {"vocalist": "miss piggy", "lead_guitar": "scooter"}
    band_dictionary.update(dictionary_to_add)
    return band_dictionary

# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]

    #outputs the keys as a VIEW OBJECT  and can set to a variable > make it a list via list() and set to another varaible to store the keys as a list
def all_values(dictionary):
    dictionary_values = dictionary.values()
    return list(dictionary_values)

# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]

def all_keys(dictionary):
    return list(dictionary.keys()) # rather than create a new variable, and make a list from the view object, I went straight to list()

# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}

def remove_nones_from_dictionary(dictionary):
    #iterate across the keys in dictionary
    # if value ! = None , add to the updated dictionary
    updated_dictionary={}
    for key in dictionary:
        if dictionary[key] != None:
            updated_dictionary[key] = dictionary[key] 
    return updated_dictionary

    # more succinct, refactored code:

    # can also use .items() method and dictionary comprehension --> view object is iterable! 

    #return {key: value for key, value in dictionary.items() if value != None}


# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}

def touch_in(station, time):
    dictionary_touch_in = {}
    dictionary_touch_in["entrypoint"] = station
    dictionary_touch_in["time"] = time
    return dictionary_touch_in