height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / ((height / 100) ** 2)
print(f"Your BMI is: {bmi:.2f}")