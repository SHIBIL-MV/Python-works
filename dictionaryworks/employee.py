# create dictionary employee with keys eid,name,salary,department,experience

employee={"eid":100,"name":"rahul","salary":15000,"department":"hr","experience":5}

print(employee)

#print salary
  
print(employee["salary"])


# add contact details

employee["contact"]=324567

print(employee)

# if experience > 5 update employee salary as current_salary+10000 else current_salary+5000

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

    print(employee)

    # add role as SDE if exp > 5 else add role as JDE

    if employee["experience"]>5:

        employee["role"]="SDE"
    
    else:

        employee["role"]="JDE"

    print(employee)


