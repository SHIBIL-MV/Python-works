from re import findall

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\Regular_expression_fieworks.py\\text.txt")

content=f.read()

#pattern="\d+/\d+/\d+"
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
dates=findall(pattern,content)

for d in dates:

    print(d)