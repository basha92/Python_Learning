#this file used the functions from file handler.py

from pathlib import Path
from file_handler import find_files, find_text_files

def main():
    path_dir = Path("Day_06/patient_register")
    files = find_files(path_dir)
    txt_files = find_text_files(path_dir)

    print("=" * 32)
    print("Files in the directory")
    print("=" * 32)
    for file in files:
        print(file.name)

    print("=" * 32)
    print("Txt Files in the directory")
    print("=" * 32)
    for file in txt_files:
        print(file.name)

if __name__ == "__main__":
    main()
