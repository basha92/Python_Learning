#Static methods = A method that belong to a class rather than any object from that class (instance)
#Usually used for general utility functions

#Instance methods - Best for operations on instances of the class (objects)
#Static methods - Best for utility functions that do not need access to class data

#to use instance method, we need to create object of the class and call it
#to use static method, we need to call the class itself. No need to create object.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def get_position(position):
        valid_positions = ["Manager", "Dev", "QA", "HR"]
        return position in valid_positions

#accessing static method
print(Employee.get_position("HR"))
print(Employee.get_position("Scientist"))

employee1 = Employee("Shweta", "Manager")
employee2 = Employee("Nithin", "Dev")
employee3 = Employee("Basha", "QA")
employee4 = Employee("Kurt", "CEO")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())