mydict = {
    "damon":"vampire",
    "klause":"original & hybrid",
    "number":"100",
    "list": [1,23,"damon"]
}
# print(mydict)
# print(mydict["klause"])
# print(mydict["list"])

# methods of dictionary

print(mydict.items())
print(mydict.keys())
print(mydict.values())
updateddict = {
"tony":"iron man"
}
mydict.update(updateddict)
print(mydict)

print(mydict.get("damon"))
print(mydict["damon"])
#this both will give us same output

# so, what's the different between this two

print(mydict.get("damon2"))  #it will return none 
print(mydict["damon2"])      #  and it will return an error






