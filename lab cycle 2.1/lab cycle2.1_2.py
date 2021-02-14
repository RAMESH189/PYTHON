n= int(input("Enter the number of terms :"))
a=0
b=1
if n<=0:
    print("Enter a positive number :")
elif n==1:
    print("fibonacci series is :",a)
elif n==2:
    print("fibonacci series is :", a,b)
else:
    print("fibonoci series is")
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c




