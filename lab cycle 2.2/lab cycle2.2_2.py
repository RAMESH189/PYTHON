word=input("Enter the words(comma seperated) :")
WORD=word.split(',')
print(WORD)
W=WORD[0]
for i in WORD:
    if len(W)< len(i):
        W=i
print("length of the longest word is ",len(W))