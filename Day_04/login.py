# this file allows user to input the credentials only 3 times
# after that profile shall be locked
#userid, password and counter variables.
username = "admin"
password = "python123"
attempts = 0

while attempts < 3:
    name = str(input("Enter user name: "))
    pwd = str(input("Enter password: "))

    if name == username and pwd == password:
        print("Logged in Successfully!")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Account locked")
        else:
            print("Enter correct user name or password")