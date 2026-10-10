# create a function to add 2 numbers

def add2numbers (a,b):   # (a,b)  are parameters
    result = a+b
    print("sum is :",result)

#Call function (use function)
add2numbers(5,3)                  # Arguments

add2numbers(a = 10, b = 100)
add2numbers(b = 89, a = 1)


#function with return statement
def add2num(a,b):
    return a+b

sum = add2num(3,4)
print(sum)

#function to convert celcius to fahrenheit   using return
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

temp_f = celcius_to_fahrenheit(25)
print(temp_f)

#function to convert celcius to fahrenheit  without using return
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(fahrenheit)

celcius_to_fahrenheit(88)

# Without return values the data type of output values would be null values so good to use return 


# Pass statement              code to be updated later

def anything():
    pass

print("What is this")    
