'''This program has following requirements:
create a function: read_patient_file(file_path)
It should:
    Check whether the file exists.
    Read the contents.
    Return the data.
    Handle a missing file.'''

def read_patient_file(file_path):
    #2.Reading contents, return data along with exception handling
    try:
        with open(file_path,'r') as file:
            content = file.read()
            print(content)
    #checking file existance
    except FileNotFoundError:
        print("The file doesn't exist")

    except PermissionError:
        print("You do not have permission to read that file")

read_patient_file(file_path = "Day_06/data/patients.txt")
        