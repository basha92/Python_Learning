#Exercise 1: Person and Patient

#Create a Person parent class with:
#- Name
#- Age
#- display_details()
#Create a Patient child class with:
#- Height
#- Weight
#- BMI property
#Use super() to initialize the parent attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Patient(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.height = height
        self.weight = weight

    def bmi(self):
        bmi = round(self.weight / (self.height ** 2), 2)
        print(bmi)


p1 = Patient(name="Arun", age=31, height=1.2, weight=70)
p1.display_details()
p1.bmi()