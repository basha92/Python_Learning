#this program calculates the BMI of a person based on their weight and height using functions
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

bmi = calculate_bmi(72.5, 1.60)
print(f"The BMI is: {bmi}")