# dictionary methods
# employee id,name,department,age,salary

employee={"id":100,"name":"rahul","department":"hr","age":22,"salary":25000}

print(employee.get("salary"))

employee.pop("salary")

print(employee)

for k in employee.keys():

    print(k)

for v in employee.values():

    print(v)

for k,v in employee.items():

    print(k,v)