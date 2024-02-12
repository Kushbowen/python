temperature = 13

if temperature > 25:
    print("it is cold")
else:
    print("it is cold")

# a program that returns the largest
num1 = 45
num2 = 56
num3 = 21

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# a program that checks whether a number is even or odd
number = 45
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# a program that checks whether a number is prime or not
num = 9
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


def is_prime(number):
    if number < 2:
        return False
    for i in range (2,int(number**0.5)+1):
        if number % i ==0:
            return False
        return True
user_input = input(95)
try:
    number = int(user_input)
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number}is not a prime number")
except ValueError:
 print("please enter a valid integer")
