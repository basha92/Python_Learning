#this program is about different methods of class
#Class methods = Allow operations related to the class itself
#Take (cls) as the first parameter, which represents the class itself.
from itertools import count


#Instance methods = Best for operations on instances of the class (objects)
#Static methods = Best for utility functions that do not need access to class data
#Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        Student.count += 1 #need to call from class because this variable belongs to it.
        Student.total_gpa += gpa


    #instance method
    def get_info(self):
        return f"{self.id} {self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_gpa(cls):
        return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

student1 = Student(10, "SpongeBob", 3.2)
student2 = Student(11, "Patrick", 2.8)
student3 = Student(12, "Sandy", 4.0)

print(Student.get_count())
print(Student.get_gpa())