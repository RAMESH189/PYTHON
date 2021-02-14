names=["jose","raman","Abijith"]
count=0
for name in names:
    for letters in name:
        if letters=="a" or letters=="A":
            count=count+1
print("Number of A's in the list :",count)