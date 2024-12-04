# caliculator(10,20,30,operation="+")

#caliculator(10,20,30,40,operation="*")

def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num
        
        return result

print(calculator(10,20,30,operation="*"))

# def student_info(45,43,44,operation="avg")

#def student_info(45,43,44,operation="total")

def students_info(*args,**kwargs):

    if kwargs.get("operation")=="total":

        return sum(args)
    
    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)

print(students_info(45,43,44,operation="avg"))

# def_sort number(1,2,6,4,15,11,reverse="true")decenting order
# def_sort number(1,2,6,4,15,11,reverse="false")acenting order

def sort_numbers(*args,**kwargs):

    if kwargs.get("revrese")=="True":
     

        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="false":

        return sorted(args)

print(sort_numbers(1,2,6,4,15,11,reverse="True"))






    