#this has 2 programs: 
# 1.printing from 10 to 1
#while True:
    #for num in range(10, 0, -1):
        #print(num)
    #break

# 2.asking user positive number input until he provides.
number = int(input("Enter a positive number: "))
while number <= 0:
    print("You entered a negative number. Please enter a positive number.")
    number = int(input("Enter a positive number: "))

print("You entered a positive number.")
