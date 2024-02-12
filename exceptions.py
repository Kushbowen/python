try:
    print(x)
except:
    print("Name error occurred")



try:
    num1 = 20
    num2 = 2
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")
finally:
    print("success")

# user defined program
try:
  def sum(first,second):
    return first+second
except:
  print("Exception occurred")
finally:
    print("success")

print(sum(10,20))





