f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\student.txt","r")

for line in f:
    print(line)

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\words.txt")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

word_count={w:words.count(w) for w in words}

nested_word_count=[[v,k] for k,v in word_count.items()]

print(sorted(nested_word_count,reverse=True))