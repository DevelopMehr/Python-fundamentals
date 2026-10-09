# write a python program to input student name and marks of 3 subjects. Print name and percentage in output?

# name = input("Enter student name: ")
# subj1 = float(input(" Enter subj1 marks "))
# subj2 = float(input(" Enter subj2 marks "))
# subj3 = float(input(" Enter subj3 marks "))

# percentage = (subj1 + subj2 + subj3) / 300 * 100

# print("your name is :",name)
# print("Your 3 subjects percentage is :",percentage,"%")

# write a python program that collects multiple types of data (e.g, name,age,height and student status)from user input, stores them in a dictionery , and then prints out the collected data?

#initializing a dictionary
user_data = {}

# input from user
user_data ['name'] = input("Enter your name:")
user_data ['age'] = int(input("Enter your age:"))
user_data ['height'] = float(input("Enter your height:"))
user_data ['status'] = input("Enter your status:")

# print the input from user
print(user_data)



