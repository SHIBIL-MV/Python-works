f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\fruits.txt")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)