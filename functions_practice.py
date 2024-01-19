
# defining and executing adding two numbers together

def add_two_numbers(num_1, num_2):
    return num_1 + num_2

#testing using print and arguments
print(add_two_numbers(3,4))
print(add_two_numbers(7,4))
#------#

# adding three numbers together:

def add_three_numbers(num_1, num_2, num_3):
    return num_1 + num_2 + num_3

#testing using print and arguments

print(add_three_numbers(3,4,5))
print(add_three_numbers(-3,4,5))

#------#

# concatenate the names of a few of your closest friends:

def concat_names(name_1, name_2):
    return name_1 + name_2

#testing using print and arguments

print(concat_names("bob", "sally"))
#------#

# calculating the number of seconds in x weeks, where x is a number 

def num_of_seconds (weeks):
    return 60*60*24*7*weeks

#testing using print and arguments

print(num_of_seconds(5))
print(num_of_seconds(1))

#-----#

#testing understanding of return in functions

def superify(name):
    return "super" + name



dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"