# This program calculates BMI and shows a simple health summary.

#from pathlib import Path
#import sys

#if __package__:
    #from .bmi_calculator import calculate_bmi
#else:
    #sys.path.append(str(Path(__file__).resolve().parent))
    #from bmi_calculator import calculate_bmi
from bmi_calculator import calculate_bmi

def calculate_weight_to_lose(weight, target_weight):
    return weight - target_weight


def calculate_daily_water(weight):
    return weight * 0.033


def display_summary(bmi, weight, target_weight):
    print("====================")
    print("Health Summary")
    print("====================")
    print(f"BMI : {bmi:.2f}")
    print(f"Weight to Lose : {calculate_weight_to_lose(weight, target_weight):.2f} kg")
    print(f"Daily Water Intake : {calculate_daily_water(weight):.2f} liters")


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    target_weight = float(input("Enter your target weight in kg: "))

    bmi = calculate_bmi(weight, height)
    display_summary(bmi, weight, target_weight)


if __name__ == "__main__":
    main()