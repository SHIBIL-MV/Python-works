from re import fullmatch,finditer

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\Regular_expression_fieworks.py\\social.txt")


for line in f:

    hashtag=line.rstrip("\n")

    pattern="#\w+"


    matcher=finditer(pattern,hashtag)

    for obj in matcher:

        print(obj.group())

        

