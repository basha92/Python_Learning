#this program specifically gives notes about pathlib.
'''
The pathlib module in Python provides an object-oriented approach to interacting 
with file systems, replacing traditional string-based path manipulation.
It consolidates tools from older modules like os.path, glob, and shutil into 
a single, unified interface.
Why Use pathlib?
Cross-platform consistency: Automatically handles differences between Windows 
backslashes and Unix forward slashes (/).
Readable syntax: Uses the division operator / to join paths cleanly instead of clunky function calls.
Paths as objects: Allows you to access attributes like extensions or parent directories 
directly from the path variable
'''
import os
from pathlib import Path

#to see current working directory
#print(Path.cwd())

#to see all files and folders in the directory
#for p in Path().iterdir():
    #print(p)

my_dir = Path("data")
my_file = Path("patients.txt")

#create a new file within dorectory method 1 - using backslash
#new_file = my_dir/ "new_file.txt"

#method 2 - using join
#new_file = my_dir.joinpath("new_file.txt")
#to get the file name without extension
#print(my_dir.stem)
#print(my_file.stem)
#print(new_file.stem)

#to check whether the file exists - returns true or false
#print(my_dir.exists())
#print(my_file.exists())
#print(new_file.exists())

#to see the parents - returns dot if the file is in current working directory;
#  else returns parent folder
#print(my_dir.parent)
#print(my_file.parent)
#print(new_file.parent)

#use absolute method to see the file path; use it on parent or the original object
#print(my_dir.parent.absolute()) #o/p: F:\Python_Git\Python_Learning
#print(my_file.parent.absolute()) #o/p: F:\Python_Git\Python_Learning
#print(new_file.parent.absolute()) #o/p: F:\Python_Git\Python_Learning\data

#on the object
#print(my_dir.absolute()) #o/p: F:\Python_Git\Python_Learning\data
#print(my_file.absolute()) #o/p: F:\Python_Git\Python_Learning\patients.txt
#print(new_file.absolute()) #o/p: F:\Python_Git\Python_Learning\data\new_file.txt

# to get absolute path of current file
#p = Path(__file__).resolve() #o/p: \\fs4\UsersR-Z\Sikkandar.Basha\Python_Git\Python_Learning\Day_06\pathlib_tutorial.py
#print(p)

'''
Path("../dotfiles"): Points to a folder named dotfiles one level up from 
your current working directory.
.expanduser(): Looks for a tilde (~ or ~user) to swap out for a user's home folder.
The Result: Since there is no tilde, the method simply returns the original 
relative path object without any errors.
'''
#p = Path("../dotfiles").expanduser() #o/p: ..\dotfiles
#print(p)

'''
The code p = Path("~/dotfiles").expanduser() creates a pathlib.Path object where 
the ~ (tilde) is expanded to the current user's absolute home directory path. 
Behavior: It converts relative paths starting with ~ or ~user into absolute paths 
(e.g., /home/username/dotfiles on Linux or C:Users username dotfiles on Windows). 
Return Type: The method returns a new Path object (specifically PosixPath or WindowsPath),
not a string.
both the below produce the same result.
'''
#p = Path("~/dotfiles").expanduser() #o/p: C:\Users\sikkandar.basha\dotfiles
#print(p)

#p = Path.home() / "dotfiles" #o/p: C:\Users\sikkandar.basha\dotfiles
#print(p)

'''
The Path.glob("*vscode*") method matches all files and directories in the current 
directory whose names contain the substring "vscode". 
Non-recursive: It only searches the immediate directory; it does not search subdirectories.
Use rglob() for recursive searches(search sub directories).
If no files match the glob pattern *vscode* in the directory represented by the path 
object, pathlib.Path().glob() returns an empty iterator (specifically, an empty generator).
'''
#dotfiles = Path.home() / "dotfiles"
#for p in dotfiles.rglob("*vscode*", case_sensitive=False):
    #print(p)

'''
A dot-file is a file with a dot as the first character in its name. 
Normal directory listings omit the dotted files to keep them from being seen or 
edited by everyday users.

These dotted files are normally used for configuration, so they hide themselves 
to avoid inadvertent editing or deletion.
'''


#dotfiles = Path.home() / "dotfiles" / "settings/VSCode-Settings.json"

#with dotfiles.open() as file:
    #print(file.read())

#making directory
p = Path("TempDir/SubDir")
#p.mkdir()

#remove directory
#p.rmdir()

#create sub directory; parents = true - creates parent if not existing. To remove it,
#delete sub dir first then parent.
#p.mkdir(parents=True)

#create files - touch will create new file. If already exists it simply update the modification time
#p = Path("TempFile.txt")
#p.touch()

#renaming file - this may work on mac or linux. On windows it will give error. So use replace
#p.rename("tempfile.txt")
#p.replace("temp_file.txt")

#to remove the replaced file:
#p = Path("temp_file.txt")
#p.unlink()