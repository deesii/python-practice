# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will require a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    return string[0].upper() == "A"



# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    return string[-1].upper() == "A"


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    # your code goes here (delete the pass below)
    # subsequent to more research, there is also an inbuilt method called .find() which can be used
    i = 0
    if len(string) >= 5:
        while i < (len(string) - 4):
            if string[i: i + 5].upper() ==  "HELLO":
                return True
            i += 1
        return False
    else:
        return False
    

print(contains_hello(("HELLO WORLD")))                                                                                                                                                                                                                                                 
print(contains_hello(("WOR")))
print(contains_hello(("hello WORLD")))
print(contains_hello(("WORLD hello")))



# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    # your code goes here (delete the pass below)
    return string.replace("hello", "goodbye")

print(substitute_hello_with_goodbye("hello, world"))

# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    # your code goes here (delete the pass below)
    new_string = ""
    for char in string:
        if char.upper() != "X":
            new_string += char
    return new_string
            


print(remove_x("xoxoopogfbfbg"))
print(remove_x("OXO"))

# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    # your code goes here (delete the pass below)
    return string[:int(len(string)/2 )]

print(first_half("codingrt"))

# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    # your code goes here (delete the pass below)
    return string[int(len(string)/2) :len(string)]

print(second_half("codingsd"))
# Congrats, you're done with this file. Move on to the next one.
