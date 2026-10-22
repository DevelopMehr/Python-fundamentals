# Loops in python -- While and for loop

# while loop

# while + looping
count = 0
while count < 5:
    print(count)
    count += 1

# while - looping
count = 5
while count > 0:
    print(count)
    count -= 1 

# Check conditions to avoid infinit loop

# For loop 

language = 'python'
for i in language:
    print(i)    

# range (start, stop , step)
for i in range (5,10,2):
    print(i)    

# Loop control statements

# Pass
for i in range(5):
    # Not Now
    pass

count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= count


# break statement
for i in range (5):
    if i == 3:
        break
    print(i)


    