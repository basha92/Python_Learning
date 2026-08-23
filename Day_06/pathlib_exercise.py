#this program has following requirements:
'''
Write a program that produces something like:
Folder: data
Number of files: 3

Files:
patient1.txt
patient2.txt
test.txt

TXT files:
patient1.txt
patient2.txt
test.txt

Use only:
Path()
exists()
is_file()
iterdir()
name
suffix
'''

#printing the folder name and no of files
from pathlib import Path
folder = Path("Day_06/data")
if folder.exists() and folder.is_dir():
    files = [f for f in folder.iterdir() if f.is_file()]
    print(f"Folder: {folder.name}")
    print(f"Number of files: {len(files)}\n")
    
    #printing the file names
    print("Files:")
    for f in files:
        print(f.name)
    
    #printing the txt files
    print("\nTXT files:")
    for f in files:
        if f.suffix == ".txt":
            print(f.name)