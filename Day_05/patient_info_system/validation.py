#this program validates all inputs givenby user
def validate_name(value):
    if not value.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters.")
    return value

def validate_age(value):
    if value <= 0:
        raise ValueError("Age must be positive")
    return value

def validate_height(value):
    if value <= 0 or value >= 2:
        raise ValueError("Enter valid height")
    return value

def validate_weight(value):
    if value <= 0 or value >= 150:
        raise ValueError("Enter valid weight")
    return value

# THE MAGIC LOOP: Reusable for ANY input and ANY validation function
def get_valid_input(prompt, cast_type, validation_func):
    while True:
        try:
            # 1. Take raw input
            raw_input = input(prompt)
            
            # 2. Convert to the right type (str, int, or float)
            converted_value = cast_type(raw_input)
            
            # 3. Pass it to your specific validation function
            validated_value = validation_func(converted_value)
            
            # 4. If everything passes, return the value and exit the loop
            return validated_value
            
        except ValueError as error:
            # Catches both type conversion errors AND your custom messages
            if "could not convert" in str(error):
                print("Error: Invalid formatting. Please enter a valid number.\n")
            else:
                print(f"Error: {error}\n")