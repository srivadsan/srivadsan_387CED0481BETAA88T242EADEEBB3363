def factorial(x):
  if x == 1:
    return 1
  else:
    return (x * factorial(x - 1))


num = int(input("enter a value: "))
result = factorial(num)
print("The factorial of", num, "is", result)
