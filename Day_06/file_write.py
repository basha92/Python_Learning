#creating a text file
#txt_Data = "I like Pizza!"
#employees = ["Eugene", "Devon", "Chris", "Raj"]
#file_path = "Day_06/data/output.txt"

#w to write or create file
#with open(file_path, "w") as file:
    #file.write(txt_Data)
    #print(f"txt file '{file_path}' is created!")

#x - creates file if not there; else gives warning
#try:
    #with open(file_path, "x") as file:
        #file.write(txt_Data)
        #print(f"txt file '{file_path}' is created!")

#except FileExistsError:
    #print(f"File already exists in {file_path}")

#a - appends text to the file.
#try:
#with open(file_path, "a") as file:
    #file.write("\n" + txt_Data)  #adds the info in next line
    #print(f"txt file '{file_path}' is updated!")

#except FileExistsError:
    #print(f"File already exists in {file_path}")

#updating the text file with list
#with open(file_path, "w") as file:
    #for employee in employees:
        #file.write(employee + " ")
    #print(f"txt file '{file_path}' is updated")

#-----------------updating JSON file-------------------------#
'''import json

file_path = "Day_06/data/output.json"

employee = {
  "firstName": "Joe",
  "lastName": "Jackson",
  "gender": "male",
  "age": 28,
  "address": {
    "streetAddress": "101",
    "city": "San Diego",
    "state": "CA"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "7349282382"
    }
  ]
}

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"The JSON file {file_path} is created/updated!")'''

#-----------------updating CSV file-------------------------#
import csv
file_path = "Day_06/data/output.csv"
employees = [["Name", "Age", "Job"],
             ["Sponge Bob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)

    print(f"The CSV file {file_path} is created!")
