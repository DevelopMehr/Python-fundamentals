#data types
a = 1
b = 2
print(a+b)
print(type(a))   # checking data type int:

c = "2"
d = "2"
print(c+d)
print(type(c))  # checking data type str:

# basic data types in python
#1. Numeric
a1 = 1  # 1a. integer
a2 = 1.5 #1b. float
print(type(a2))

a3 = complex(3,5) #a3. complex
print(type(a3))

# sequence
b1 = "rahul"  # 2a. string
print(type(b1))
b2 = [1,2,5,102,58] # 2b. list
print(type(b2))
b3 = (1,2,5,102,58) # 2c. tuple
print(type(b3))

#Dictionary
my_dict = {'name':'Mehr', 'city':'Karachi', 'age': '23'}
print(type(my_dict))

#set 
my_set = {1,2,3,4,5,'Rahul'}
print(type(my_set))

#boolean
bool1 =  True
bool2 =  False
print(type(bool1))

#Binary

#bytes, Bytearray , memoryview
byte1 = b"Rahul"
print(type(byte1))