num = int(input("Enter the number: "))

sum_even = 0
for i in range (2, num+1, 2) :
    sum_even += i
print("The sum of all even numbers between 1 and", num, "is:", sum_even)