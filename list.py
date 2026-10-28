# lists are mutable and strings are immutable

marks = [13,43,56,22,14.3]
print(len(marks))
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

# slicing

marks = [12,45,66,44,32]
print(marks[0:3])
print(marks[0:])
print(marks[:5])
print(marks[-3:-1])

# List methods
list = [1,2,3,4]
print(list.append(5))
print(list.sort(reverse=True))
print(list)

# q store fav movies by taking input from user and store them in list
movies = []
movies.append(input("Enter you 1st favourite movie: "))
movies.append(input("Enter you 2nd favourite movie: "))
movies.append(input("Enter you 3rd favourite movie: "))
print(movies)

