x= int(input("enter first number :"))
y= int(input("enter second number :"))
operator = input("Enter operator :")
if operator == "+":
    print("Result is:", x+y)
elif operator == "-":
    print("Result is:", x-y)
elif operator == "*":
    print("Result is:", x*y)
elif operator == "/":
    print("Result is:", x/y)
else:
    print("invalid")
