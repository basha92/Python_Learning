'''
Requriements:
Receive a folder path.
Convert it to a Path.
Find files.
Return the list of Path objects.
'''
from pathlib import Path

def find_files(folder_path):
   #defining folder path
    folder = Path(folder_path)

    #storing files
    files = []

    #finding files
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)

    return files

def find_text_files(folder_path):
    folder = Path(folder_path)
    txt_files = []

    for item in folder.iterdir():
        if item.suffix == ".txt":
            txt_files.append(item)

    return txt_files