# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# The first ones will be familiar, do them without looking at your previous
# work. The later ones will be more complex.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: ExampleGreeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = ExampleGreeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution:
# class ExampleGreeter():
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return 'Hello, ' + self.name + '!'
#     def say_goodbye(self):
#         return 'Goodbye, ' + self.name + '!'



# == EXERCISES ==

# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'

class Greeter():
    def __init__(self):
        pass
    def hello(self,name):
        return f"Hello, {name}!"
    def goodbye(self, name):
        return f"Goodbye, {name}!"
    def good_night(self, name):
        return f"Good night, {name}!"
    def good_morning(self, name):
        return f"Good morning, {name}!"

# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']

class Basket():
    def __init__(self):
        self.basket = []
    def add(self,item):
        return self.basket.append(item)
    def list_items(self):
        return self.basket
        

# Class name: Calculator
# Purpose: perform simple calculations and track the history
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]

class Calculator():
    def __init__(self):
        self.history_calculator = []
    def add(self, num1, num2):
        result_add = num1+num2
        self.history_calculator.append(result_add)
        return result_add
    def multiply(self, num1, num2):
        result_multiply = num1*num2
        self.history_calculator.append(result_multiply)
        return result_multiply
    def subtract(self, num1, num2):
        result_subtract= num1-num2
        self.history_calculator.append(result_subtract)
        return result_subtract
    def divide(self, num1, num2):
        result_divide= num1/num2
        self.history_calculator.append(result_divide)
        return result_divide
    def list_history(self):
        return self.history_calculator

# Class name: Cohort
# Purpose: store a list of students
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]

class Cohort():
    def __init__(self):
        self.students = []
        self.list_students_employers = []
    def add_student(self, student_dict):
        self.students.append(student_dict)
    def list_students(self):
        return self.students
    def list_employed_by(self, employer):
        # iterate across the list of students
        for student in self.students: 
            # iterate across the keys within each student (i,e across the elements within the list)
            for (key,value) in student.items():
                if value == employer:
                    self.list_students_employers.append(student)
            
        return self.list_students_employers
        

# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
#   > person = Person({
#       'name' : 'Alex',
#       'pets' : [
#         {'name' : 'Arthur', 'animal' : 'cat'},
#         {'name' : 'Judith', 'animal' : 'dog'},
#         {'name' : 'Gwen', 'animal' : 'goldfish'}
#       ],
#       'addresses' : [
#         {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
#         {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
#       ]
#     })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'


class Person():
    def __init__(self, complex_dictionary):
        self.complex_dictionary = complex_dictionary
        self.addresses = self.complex_dictionary.get("addresses")
        self.pets = self.complex_dictionary.get("pets")
        self.name = self.complex_dictionary.get("name")
    def get_work_address(self):
        for place in self.addresses:
            for key in place:
                if place[key] == "work":
                    work_list = list(place.values())
        return f"{work_list[1]} {work_list[2]}"
            
    def get_home_address(self):
        for place in self.addresses:
            for key in place:
                if place[key] == "home":
                    home_list = list(place.values())
        return f"{home_list[1]} {home_list[2]}"
    
    def get_pets(self):
        summary = ""

        for pet in self.pets[:-1]:
            summary += f"a {pet['animal']} called {pet['name']}, "
        
        last_pet = self.pets[-1]

        summary += f"a {last_pet['animal']} called {last_pet['name']}"

        return f"{self.name} has {len(self.pets)} pets: {summary}"


