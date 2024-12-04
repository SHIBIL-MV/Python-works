from json import load

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\books.json")

data=load(f)

#for books in data:

    #print(books)

all_titles=[book.get("title")for book in data]
#print(all_titles)
# books with pages < 250

page_filter=[book.get("title") for book in data if book.get("pages") < 250]

print(page_filter)
# print all genres

all_genres=[book.get("genres") for book in data]

#print(all_genres)

#print(set(page_filter))

# print costly book

costly_books=max(data,key=lambda d:d.get("price"))

print(costly_books)

# author with more than one book
all_author=[book.get("author") for  book in data]

author_count={auth:all_author.count(auth) for auth in all_author}

print([k for k,v in author_count.items() if v > 1])



