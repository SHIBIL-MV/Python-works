from re import findall

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\Regular_expression_fieworks.py\\sample.txt")

content=f.read()

pattern="http?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)

    