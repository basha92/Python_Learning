'''
write_report(file_path, content)
The function should:
    Accept a file path.
    Accept report content.
    Create/write the file.
    Handle errors.
'''

def write_report(file_path, content):
    try:
        with open(file_path, "a") as file:
            file.write("\n" + content)
            print(f"txt file '{file_path}' is updated!")
    except FileExistsError:
        print(f"The file doesn't exist in {file_path}")

    except PermissionError:
        print("You do not have permission to read that file")

def main():
    file_path = "Day_06/data/patients.txt"
    content = "Aegon,44,1.50,65"

    write_report(file_path, content)

if __name__ == "__main__":
    main()