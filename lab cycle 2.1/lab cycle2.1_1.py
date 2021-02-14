num=int(input("Enter the number :"))
factorial=1
if num<0:
    print("fatorial not found for negetive number")
elif num==0:
    print("fatorial of 0 is :",factorial)
else:
    for i in range(2,num+1):
        factorial=factorial*i
    print("Fatorial of the number :",factorial)