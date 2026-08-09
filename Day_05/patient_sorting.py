#this program sorts patients based on BMI
patients = [{"Name": "John", "BMI": 18.5},
    {"Name": "Alice", "BMI": 22.1},
    {"Name": "David", "BMI": 31.5}]

sorted_patients = sorted(patients, key=lambda p:p[BMI])

for p in sorted_patients:
    print(f"{p['Name']}: {p['BMI']}")