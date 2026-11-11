#this program adds patient details in a class.

class Patient_Details:
    def __init__(self, name, age, height, weight):
        if not str(name).strip():
            raise ValueError("Name cannot be empty.")
        if not isinstance(age, int) or not (0 < age < 130):
            raise ValueError("Age must be a whole number between 1 and 129.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number (kg).")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number (meters).")

        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.bmi = round((self.weight / (self.height ** 2)),2)

    def get_bmi_category(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        return "Obesity"

    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "category": self.get_bmi_category()
        }

    def __str__(self):
        return (f" {self.name}, {self.age} yrs | "
                f" {self.height} m, {self.weight} kg |"
                f"BMI: ({self.bmi}) {self.get_bmi_category()} ")

# Create objects
#patient_a = Patient_Details("Arun", 31, 1.65, 69)
#patient_b = Patient_Details("Kumar", 28, 1.72, 75)

# Display reports
#patient_a.display_details()
#patient_b.display_details()