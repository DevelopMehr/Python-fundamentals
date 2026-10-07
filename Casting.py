a = 1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(type(c))

print(a+int(b))

# all str type can't be casted into numerical type

# name = "Mehr"
# newname = int(name)

# all numerical type can be cast into str

mynum = 23
newnum = str(mynum)
print(type(newnum))

f1 = 22.33
f2 = int(f1)
print(f2)
print(type(f2))

in1 = 33
print(type(float(in1)))

# Implicit type casting
var1 = 22
var2 = 32.33
var3 = var1+var2
print(var3)
print(type(var3))

# explicit type casting
int_num = 101
str_num = str(int_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))