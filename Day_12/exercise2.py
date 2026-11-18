#Exercise 2: Method overriding
#Create:
#- Person
#- Patient
#- Doctor
#All three should have a display_details() method.
#Make the child methods print their own record heading and then call the parent method using super()

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

    def display_details(self):
        print("\nPatient Details")
        super().display_details()
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight}")

class Doctor(Person):
    def display_details(self):
        print("\nDoctor Details")
        super().display_details()

patient = Patient(name="Arun", age=31, height=1.2, weight=70)
doctor = Doctor("Kumar", 45)

patient.display_details()
doctor.display_details()