

# inbuilt functions
number = max(89, 70, 12, 30)
print(number)

x = min(78, 43, 34, 1)
print(x)

z = pow(2, 3)
print(z)


# user-defined functions
def name():
    print("Mark")


name()  # calling a function


def student():
    name = "vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# parameters/variables
def students(name, age, course):
    print(name, age, course)


students("vincent", 18, "MIT")
students("Grace", 17, "Cyber security")
students("Allan", 19, "MIT")
students("Mark", 16, "Full stack")
students("Dedan", 18, "MIT")
students("vincent", 18, "MIT")
students("vincent", 18, "MIT")


def employee(fullname,age,position,salary):
    print(fullname,age,position,salary)
employee("John",35,"HR",150000)
employee("Mark",38,"CEO",160000)
employee("Nelly",25,"Clerk",60000)
employee("Winnie",30,"Nurse",500000)
employee("Faith",28,"Networkadmin",150000)
