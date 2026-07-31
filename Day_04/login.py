# this file allows user to input the credentials only 3 times
#after that profile shall be locked
username = "admin"
password = "python123"

while True:
    name = str(input("Enter user name: "))
    pwd = str(input("Enter password: "))
    if name==username and pwd==password:
        print("Logged in Successfully!")
        break
    else:
        print("Enter correct user name or password")