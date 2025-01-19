# Write a program to create a parent class Person (attributes - fname, lname) with 
# a method printname to display the full name. 
# Create a child class Student (attributes - fname, lname, year). 
# Access the attributes of parent class in child class using super() function. 
# Then, create an object for the child class and call the display method to display the full name.
#  Also, print the graduation year

# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Made the method public
    def display(self):
        print("Hello, my full name is {} and my last name is {}".format(self.fname, self.lname))

# Child Class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

# Create an instance of Student
emp1 = Student("Ali", "Khan", 17)

# Call the display method
emp1.display()

# Print additional information
print("I am {} and my last name is {} and my age is {}".format(emp1.fname, emp1.lname, emp1.year))