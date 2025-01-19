# Write a program to create a parent class Person (attributes - name, idnumber) with 
# a method display to display the attributes. 
# Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and idnumber.

#Parent class
class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print("Hello I am {} and my Id is {}".format(self.name,self.idnumber))

#child class
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        Person.__init__(self, name, idnumber)
        self.salary=salary
        self.post=post

emp1=Employee("Ali",12345,15000,"Intern")
emp1.display()
print("I am {} with salary {}".format(emp1.post,emp1.salary))
