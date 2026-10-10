# write a simple program to determine if given year is a leap year using user input

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")



# Login authentication using conditional statement.
# Assume you have predefined username and password. 
# write a program that prompts the user to enter a username and password and checks whether they match.
# Provide appropriate messages for following cases?
# 1. Both username and password are correct
# 2. username is correct but password is incorrect
# 3. username is incorrect 

predefined_username = "salman"
predefined_password = 123

username = input("Enter username:")
password = int(input("Enter password"))

if username == predefined_username:
    print("your username is matched")
else:
    print("username is incorrect")

if password == predefined_password:
    print("your password is matched:")
else:
    print("your password is incorrect:")

# write a program that takes marks in  3 subjects as input and prints whether student is eligible for # addmission


print("Enter you PCM marks ")
physics_marks = (int(input("Enter physics marks:")))
english_marks = (int(input("Enter english marks:")))
arts_marks = (int(input("Enter arts marks:")))

if (physics_marks >= 65 and 
    english_marks >= 55 and
    arts_marks >= 50 and
    (physics_marks + english_marks + arts_marks) >= 180) or \
    (physics_marks + english_marks) >=140:
    print("you are eligible")
else:
    print("you are not eligible:")

