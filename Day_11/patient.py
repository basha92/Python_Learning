#Build a Patient Data Validation System
#Your program should:
#1. Create patient objects.
#2. Validate patient details.
#3. Reject invalid age, height, and weight.
#4. Calculate BMI dynamically.
#5. Display patient details and BMI category.
#6. Update a patient's weight and show the updated BMI.

#Exercise 1: Protect patient data

#Create a Patient class with:
#- name as a public attribute.
#- __age as a private attribute.
#- get_age() to return the age.
#- set_age() to update the age.
#- Reject age values below 1 or above 120.

class Patient:
    def __init__(self, name, age, weight, height):
        if not str(name).strip():
            raise ValueError("Name cannot be empty.")
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
#age getter and setter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or isinstance(new_age, bool):
            raise TypeError("Age must be an integer.")

        if not 1 <= new_age <= 120:
            raise ValueError("Age must be between 1 and 120.")

        self._age = new_age
#height getter and setter
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (int, float)) or new_height <= 0:
            raise ValueError("Height must be a positive number (cm).")
        self._height = new_height

#weight getter and setter
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Weight must be a positive number (kg).")
        self._weight = new_weight

    # Read-only property: Dynamically calculates BMI
    @property
    def bmi(self):
        height_m = self._height / 100
        return round(self._weight / (height_m ** 2), 2)

    # Read-only property: Determines category based on BMI
    @property
    def bmi_category(self):
        current_bmi = self.bmi
        if current_bmi < 18.5:
            return "Underweight"
        elif current_bmi < 25:
            return "Normal weight"
        elif current_bmi < 30:
            return "Overweight"
        return "Obesity"

#patient = Patient("Arun", 31, 70, 175)

#patient.age = -2 # Calls the @age.setter method
#print(patient.age) # Calls the @property getter -> Output: Age: 35 Yrs

#print(f"Patient: {patient.name}")
#print(f"BMI: {patient.bmi}")               # Output: BMI: 22.86
#print(f"Category: {patient.get_bmi_category}") # Output: Category: Normal weight

# Updating weight automatically updates BMI and BMI category
#patient.weight = 85
#print(f"New BMI: {patient.bmi}")           # Output: New BMI: 27.76
#print(f"New Category: {patient.get_bmi_category}") # Output: New Category: Overweight

#trying to access internal variable
patient = Patient("Arun", 31, 70, 175)

print(patient._age)

#patient.age = 150       # Setter runs, validation rejects it
#print(patient.age)      # Original value: 31

#patient._age = 150      # Bypasses the setter
#print(patient.age)      # Displays: 150