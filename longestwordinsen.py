#display longest word in a sentence
sentence=str(input("enter a sentence"))
strsplit=sentence.split()
longest=0
i=0
w=0
while i < len(strsplit):
    if len(strsplit[i]) > longest:
        longest=len(strsplit[i])
        w=strsplit[i]
    i=i+1
print("The longest word in a sentence is ' "+str(w)+" ' and the length of word is :"+str(longest))
