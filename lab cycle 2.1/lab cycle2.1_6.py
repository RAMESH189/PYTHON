dict={}

string=input("Enter the string :")
for n in string:       #for a character in string
    key=dict.keys()        #include all keys in dictionary to key
    if n in key:           #if char in key
        dict[n]=dict[n]+1
    else:
        dict[n]=1
print("Character frequency :",dict)
