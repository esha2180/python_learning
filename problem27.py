a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if c - d != 0 :
    result = (a + b) / (c - d)
    print("The result of (a + b) / (c - d) is:", result)
else :
    print("Division by zero is not allowed")