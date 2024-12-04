from json import load

f=open("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\employee.json")

data=load(f)

for emp in data:

    print(emp)