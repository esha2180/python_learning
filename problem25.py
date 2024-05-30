maths = float(input("Enter marks in Maths: "))
phy = float(input("Enter marks in Physics: "))
chem = float(input("Enter marks in Chemistrys: "))

total = maths + phy + chem

if (maths >= 65 and phy >= 55 and chem >=50) or (total >= 180) or (maths + phy >= 140) :
    print("Eligible for admission")
else :
    print("Not eligible for admission")