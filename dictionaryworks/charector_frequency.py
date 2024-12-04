# most recursive charector

# non recursive charector

text="ABCDRSSAAC"

def get_count(char):

    return text.count(char)

most_frequent_charactor=max(text,key=get_count)

print(most_frequent_charactor)

least_recursive_charactor=min(text,key=get_count)

print(least_recursive_charactor)