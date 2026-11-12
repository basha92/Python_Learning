#Exercise 1: Instance method
#Create a PatientDetails class with:
#- Name
#- Age
#- Height
#- Weight
#Add an instance method: def update_weight(self, new_weight):
#It should update the patient's weight.
#Then calculate BMI again and display the new result.


class PatientDetails:
    count = 0

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        PatientDetails.count += 1

    #exercise1 - instance method solution
    def calculate_bmi(self):
        return round((self.weight / (self.height ** 2)), 2)

    def update_weight(self, new_weight):
        self.weight = new_weight
        bmi = self.calculate_bmi()
        return f"Name: {self.name} | Age: {self.age} | Height: {self.height}m | New Weight: {self.weight}Kg | New BMI:{bmi}"

    def display_details(self):
        return f"Name: {self.name} | Age: {self.age} | Height: {self.height}m | Weight: {self.weight}Kg | BMI:{self.calculate_bmi()}"

    #Exercise 2: Class method - add four patient objects and return the total count
    @classmethod
    def get_count(cls):
        return f"Total # of patients: {cls.count}"

    #Exercise 3: Static method - validate age - greater than zero, not exceed 120, Return True or False, Test it with ages 31, 0, -5 and 130.
    @staticmethod
    def validate_patient_age(age):
        if not (0 < age < 120):
            return False
        else:
            return True

    #Exercise 4: Alternative constructor - Pass this dictionary, Use it to create a patient object without manually passing each value.
    @classmethod
    def from_dictionary(cls):
        patient_data = {
            "name": "Ravi",
            "age": 35,
            "height": 1.70,
            "weight": 80
        }
        return patient_data

patient1 = PatientDetails("Arun", 31, 1.65, 69)
patient2 = PatientDetails("Kumar", 28, 1.72, 75)
patient3 = PatientDetails("Padmini", 35, 1.5, 50)
patient4 = PatientDetails("Kumari", 30, 1.6, 63)

print(PatientDetails.display_details(patient1))
print(PatientDetails.display_details(patient4))

#updating patient 1 weight
print(PatientDetails.update_weight(patient1, 73))

#calling  class method
print(PatientDetails.get_count())

#accessing static method
print(PatientDetails.validate_patient_age(31))
print(PatientDetails.validate_patient_age(0))
print(PatientDetails.validate_patient_age(-5))
print(PatientDetails.validate_patient_age(130))

#exercise 4
print(PatientDetails.from_dictionary())

