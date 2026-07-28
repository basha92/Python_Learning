#this is the main file to use the math_utils.py file.
from math_utils import add, subtract, multiply, divide

#this function takes 2 numbers and do all calculations.
#def main():
    #num1 = float(input("Enter the first number: "))
    #num2 = float(input("Enter the second number: "))

    #print(f"{num1} + {num2} = {add(num1, num2)}")
    #print(f"{num1} - {num2} = {subtract(num1, num2)}")
    #print(f"{num1} * {num2} = {multiply(num1, num2)}")
    #print(f"{num1} / {num2} = {divide(num1, num2)}")

#if __name__ == "__main__":
    #main()

#this function takes 2 numbers and choice from user.
def main():
    print("Welcome to the calculator program!")
    print("Please choose an operation:")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Exiting the program. Goodbye!")
        return
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print(f"Sum of {num1} and {num2} is {add(num1, num2)}")
    elif choice == "2":
        print(f"Difference of {num1} and {num2} is {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Product of {num1} and {num2} is {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Quotient of {num1} and {num2} is {divide(num1, num2)}")

if __name__ == "__main__":
    main()