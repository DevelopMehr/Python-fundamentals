# Dictionary is Mutable

info = {
    "key": "value",
    "name": "Mehr",
    "learning": "coding",
    "age": "35",
    "isadult": "True",
    "marks": "90.9",
    12.88 : 232
}

#   print(type(info))
info["isadult"] = False    # overwrite
info["istopic"] = "Deep learning"    # adding new key pair
print(info)

#  Nested Dictionary

dict = {
    "name": "Raj",
    "subjects": {
        "phy": "54",
        "chem": "80",
        "Maths": "99"
    }
}
print(dict)
print(dict["subjects"]["chem"])
print(dict.keys())                   # shows how many keys are in program
print(len(list(dict.keys())))        # shows in numbers
print(list(dict.items()))             # shows all items in pairs as tuple
new_dict = {"city": "Hyderabad", "built": 1903}      # insert items into dictionary
dict.update(new_dict)
print(dict)                                  



marks = {}
x = int(input("Enter phy marks"))
marks.update({"phy": x})
x = int(input("Enter phy marks"))
marks.update({"chem": x})
x = int(input("Enter phy marks"))
marks.update({"eng": x})

print(marks)