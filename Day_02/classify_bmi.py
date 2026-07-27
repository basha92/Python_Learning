#this program classifys person based on their BMI using functions
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

bmi = calculate_bmi(72.5, 1.60)
classification = classify_bmi(bmi)
print(f"The BMI is: {bmi}")
print(f"The classification is: {classification}")