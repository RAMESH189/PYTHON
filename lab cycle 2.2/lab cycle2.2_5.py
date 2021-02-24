a=int(input("Enter the side :"))

x=lambda a:a*a

print("Area of the given squere is :",x(a))

b=int(input("Enter the length :"))
c=int(input("Enter the bredth :"))

y=lambda b,c:b*c
print("Area of the given rectangle is :",y(b,c))

d=int(input("Enter the base length:"))
e=int(input("Enter the height :"))

z=lambda d,e:0.5*d*e

print("Area of the given triangle is :",z(d,e))