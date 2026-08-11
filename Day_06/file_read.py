#file location
#use absolute or relative location
#use \\ or / when giving file path

#reading text file
#file_path = "Day_06/data/patients.txt"

#to read contents of json
#import json
#reading json file
#file_path = "Day_06/data/patients.json"

#try:
#opening the file and reading contents of JSON
    #with open(file_path, "r") as file:
        #reading contents of JSON
        #content = json.load(file)
        #print(content[0])
        #o/p: {'name': 'John', 'age': 30, 'height': 1.75, 'weight': 72}

#to read contents of CSV
import csv
#reading csv file
file_path = "Day_06/data/patients.csv"

try:
#opening the file and reading contents of CSV
    with open(file_path, "r") as file:
        #reading contents of JSON
        content = csv.reader(file)
        for line in content:
            #print(line) #prints whole file
            print(line[0]) #prints particular column with that indes

except FileNotFoundError:
    print("The file doesn't exist")

except PermissionError:
  print("You do not have permission to read that file")