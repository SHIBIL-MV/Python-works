class person:
    
    name:str

    age:int

    def __init__(self,name,age):

        self.name=name

        self.age=age
    
    def display_person_info(self):

        print(self.name,self.age)

class Employee:

    eid:int

    salary:int

    def __init__(self,eid,salary):
        self.eid=eid
        self.salary=salary
    
    def display_employee_info(self):

        print(self.eid,self.salary)

class Manager(person,Employee):

    department:str

    def __init__(self,age,name,eid,salary,department):

        person.__init__(self,age,name)

        Employee.__init__(self,eid,salary)

        self.department=department

    def display_manager_info(self):

        self.display_person_info()

        self.display_employee_info()

        print(self.department)

manage_instance=Manager(32,"hari","eo1",5400,"hr")

manage_instance.display_manager_info()
    