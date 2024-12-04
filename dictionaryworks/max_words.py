text="this is a simple programming question to find word with maximum number of character"

# step1 split text to words

words=text.split(" ")

#words['this','is','a',

def get_lenght(w):

    return len(w)

srt_words=sorted(words,key=get_lenght,reverse=True)

print(srt_words)

