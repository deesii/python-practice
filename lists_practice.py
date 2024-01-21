list_names = ["Will", "Simo", "Alex", "Eddie", "Kay"]

print(list_names)

#adding to the list 

list_names.append("Bob")

print(list_names)


print(list_names[-1])

# by choosing an index that is out of the range of the list, will provide an IndexError : list index out of range

# slicing works in the same way for lists as strings

print(list_names[0:4])

# the above methods are not changing the original list. 

# however the following modify the original list (MUTATING or modifying IN PLACE)

#.pop() : unique - if set to a new variable then you are immutable; but also mutable because if left on its own , it will remove the last element from the list.
# .index(item) : immutable yes , because if you call up the original list then you will see that it has NOT changed 
# .reverse() : mutable? yes , because if you call up the original list then you will see that it has changed (reverse the order)
# .sort(): mutable? yes , because if you call up the original list then you will see that it has changed (sorted alphabetically)
#.clear() @ mutable because if you call up the original list after carrying out this function, then it has changed - removed everything  from the list



