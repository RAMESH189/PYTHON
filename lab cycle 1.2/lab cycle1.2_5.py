word=input("Enter a string :")
a=word[0]
for i in word:
    if i.lower()==a.lower():
        word=word.replace(i,"$")
str1=list(word)
str1[0]=a
word= ''.join([str(e) for e in str1])  # e stands for element
print("New string is : ",word)
