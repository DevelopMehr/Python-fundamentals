# sets are mutable, set  elements are immutable, and uses unique values only

set = {1,2,3,4,4, "Hello", "world" ,"hi" ,"hi"}
print(type(set))
print(len(set))       # total numbers of items

collection = {}         # it is an empty dict not set
collection = set ()      # empty set : syntax
print(type(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)
collection.remove(2)
collection.add([1,2,3,4])            # elements are immutable so it would not run 

collection.clear()                    # 0
print(len(collection))


# List Methods

set1 = {1,2,3}
set2 = {3,4,5}

#print(set1.union(set2))       # {1,2,3,4,5}
print(set1.intersection(set2))     #{3}

# store following word meanings in a python dictionary
dict = {
    "cat": "small animal",
    "furniture": ["a piece of furniture", "facts and figures"]
}
print(dict)