#file location
#use absolute or relative location
#use \\ or / when giving file path

#reading text file
#file_path = "Day_06/data/patients.txt"

#reading json file
#file_path = "Day_06/data/patients.json"

#reading csv file
file_path = "Day_06/data/patients.csv"

try:
#opening the file and reading contents
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file doesn't exist")

except PermissionError:
  print("You do not have permission to read that file")