p = float(input("Enter principle (amount): "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

CI = p * (1 + r / 100) ** t

print("Compound Interest:", CI)