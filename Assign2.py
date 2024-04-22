"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

n = input("enter a number")
n = float(n)

nn = input("enter another number")
nn = float(nn)


question = input("is one of the numbers a hypotenuse of a right triangle")

a = ""
b = ""
c = ""

l = (a*a + b*b)**0.5
l = str(l)
l = int(l)

h = (a**2 + b**2)**0.5 
h = str(h)
h = int(h)

if a == n and b == nn:
    print(f"the missing length would be {c}")