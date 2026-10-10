# if statement only works when condition is true.
a = 19
b = 77
if a<b:
    print("b is greater than a:")

age = int(input("Enter your age"))
if age >19:
    print("you are adult:")

# if else statement
# else handles false condition

age = int(input("Enter your age:")) 
if age > 19:
    print("you are adult:")
else:
    print("you are not an adult:")  

# if-elif-else condition
# multiple conditions

marks = int(input("Enter your marks-100 "))

if marks >=90:
    print("your grade is A+")
elif marks >=80:
    print("your grade is A")
elif marks >=70:
    print("your grade is B")
else:
    print("your grade is C")

# Nested if-else statement
# if-else inside if-else statement
# multiple conditions depend on each other

number = int(input("Enter a number:"))
if number > 0:
    if number % 2 == 0:
        print("The is even number:")
    else:
        print("This is an odd number:")
else:
    if number == 0:
        print("this is zero")
    else:
        print("this is a negative number:")

#conditional expressions (ternary operator)

age = 16
status = "Major" if age>=18 else "Minor"
print(status) 

# what should be the expected output
value = None
if value:
    print("value is true:")
else:
    print("value is false")

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