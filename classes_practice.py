# Defining a class

class GreeterHello(): # this is defining the class itself, but without the defining of hell0, this does not do much. 
    def __init__(self):
        print("Hello i am happening automatically without the need to invoke a method!!")
    def __str__(self):
        return "I am a GreeterHello object!" # introduced to customise the string representation, so that it is more readable reppresentation of object
    def hello(self): # def hello(self) is a method with the parameter of self, which is the first argument of any of your class methods. "self" for referring back to the instance of the class, i.e access the attributes of the object it is called on
        return "Hello!"
    
    def good_bye(self):
        return "Good bye!"

new = GreeterHello()
greeter = GreeterHello() # what does this actually do?  - "instantiates - almost like it introduces it into the code .. " the GreeterHello class, and assigns it to a variable called greeter, which is an object

print(greeter) # prints out the address of the greeter object in memory : <__main__.GreeterHello object at 0x1047bb6d0>; main indicates that this the module where the script is executed.
# thememory address may be different upon the running of the scipt on different runs
print(greeter.hello()) # .hello is the invoking of the method "hello", the "." is used to access methods and attributes of an object. self refers to the instance of the class (greeter in this case). 
#The method doesn't take any additional arguments besides self.

# error if there is no argument :
    

class GreeterHelloTest():

    def hello():
        return "Hello!"
    
    def good_bye():
        return "Good bye!"
    

testing = GreeterHelloTest()


#testing.hello() # returns TypeError: GreeterHelloTest.hello() takes 0 positional arguments but 1 was given

#testing the --init__() Method (The constructor)

class BuildingToys():
    def __init__(self):
        print("testing building toys!")

instantiating_class = BuildingToys()

#instance variables are declared inside the constructor method

class Person():
    def __init__ (self, name, birthday, favourite_programming_language):
        self.name = name 
        self.birthday = birthday
        self.favourite_programming_language = favourite_programming_language


person1 = Person("Sally Lockhart", "August 31 1989", "Python")

person2 = Person("Bobby Brown", "September 23 1999", "JavaScript")

print(person2.name)

print(person1.birthday)

#creating some classes with their own instance variables 

class Animal():
    def __init__ (self, species, colour, weight):
        self.species = species
        self.colour = colour
        self.weight = weight

tiger = Animal("cat", "orange", "100kg")
human = Animal("human", "various", "various")

print(tiger.weight)

# further work on class

class Greeter():
    def __init__(self , name):
        self.name = name
    
    def hello(self):
        return f"hello, {self.name}"
    
greeter_2 = Greeter("Alan")

print(greeter_2.hello())

# testing the following and seeing what goes wrong... the scope is important,

#the local variables first_name and surname were only avaialble with the __init__() method

#instance variables have a broader scope-  available anywhere within the instance of a class.

class PersonTest():
    def __init__ (self, first_name, surname):
        self.first_name = first_name # if self is not used here(instance variables and was just first_name, there will be an error in the next definition of the method should you want to output the insstance attribute
        self.surname = surname 
    def full_name(self):

        return f"{self.first_name} {self.surname}" # if isntance variables not used , then a name error will occur that the variable has not been defined
    
alan_turing = PersonTest("Alan", "Turing")

alan_turing.full_name() # upon executing  this , it will say first_name is not defined if you did not 

print(alan_turing.full_name())
    