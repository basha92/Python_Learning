def calculate_bmi(weight, height):
    """weight in kg, height in meters. Returns rounded BMI."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)