# a = input()
# print(int(a)+int(a))

# input function always reads value as a string

# name = input("Enter Your Name ")
# print(f"Welcom {name} in python tutorial series")

# age = input("Enter your age :")
# print(f"your age is {age} ")

# age = input("Enter your age ")
# print(f"Next year your age will be {int(age)+1}")

# x = input("Enter first number :")
# y = input("Enter second number :")

# print(f"sum of {x} and {y} is {int(x) + int(y)}")

# write a program to input student name and marks of 3 subjects and print name and percentage

name = input("Enter your Name :")
subject1 = float(input("Enter your Marks1 :"))
subject2 = float(input("Enter your Marks2 :"))
subject3 = float(input("Enter your Marks3 :"))

percentage = ( subject1 + subject2 + subject3 ) / 300 * 100
print("Your name is ",name)
print("Percentage is",percentage,"%")
