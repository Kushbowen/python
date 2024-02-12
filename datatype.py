# Data Types
number = 45  # int
bun = 56.78  # float
greeting = "Hello there"  # str
isPythonIntreresting = True  # boot

# variable storing multiple values
languages = ["python", "PHP", "Java"] # list
fruits = ("apple", "banana", "pineapple") # Tuple
countries = {"Kenya", "China", "USA"} # set
# Dictionary
details = {
    "firstname" : "Mark",
    "age" : 17,
    "course" : "MIT",
    "Nationality" : "North American"
}

print(details["course"])
print(details["Nationality"])
print(number)
print(greeting)
print(countries)
print(isPythonIntreresting)

# Determining the data type
print(type(details))
print(type(countries))

# Type casting - Converting one data type to another
print(float(number))
print(int(bun))



