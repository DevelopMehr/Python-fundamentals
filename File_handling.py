#File handling
#mode : r- read, w- write, a- append

#Open File
file = open('example.txt', 'r')     # Read Mode

# Read file
file = open('example.txt', 'r')
content = file.read()   # read entire data
print(content)
file.close()       # Best practice



file = open('example.txt', 'r')
content = file.readline()   # read first line
print(content)
file.close()       # Best practice



file = open('example.txt', 'r')
content = file.readlines()   # list entire data
print(content)
file.close()       # Best practice

# Write to a file
file = open('example2.txt', 'w')     # Write Mode    
file.write("How the time passes !")
file.close()

file = open('example2.txt', 'a')     # Append Mode    
file.write("Very Well how about you !")
file.close()