import math
a=eval(input("Enter coefficient of x2 value "))
b=eval(input("Enter coefficient of x value "))
c=eval(input("Enter constant value "))
sr=b*b-4*a*c
sqrt_of=sr**(1/2)
x1=-(b-sqrt_of)/2*a
x2=-(b+sqrt_of)/2*a
print(x1,"",x2)
