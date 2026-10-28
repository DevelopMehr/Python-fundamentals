#tuple are immutable

tup = (1,2,3,4)
print(tup[0])
print(tup[1])
tup[0] = 5

tup = (1,)              # right way to initialize or py would consider it as interger
print(type(tup))

# Tuple methods 

tup = (1,2,3,4)
print(tup.index(3))

tup  = (1,2,3,3,4)
print(tup.count(3))

