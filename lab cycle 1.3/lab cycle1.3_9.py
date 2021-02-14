data={"zebra":100,"bat":200,"lion":35}
list1=list(data.items())
list1.sort()
print("Ascending order",list1)
list2=list(data.items())
list2.sort(reverse=true)
print("Descending order",list2)