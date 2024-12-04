num1=int(input("enter num1")) #10)

num2=int(input("enter the num2"))#0

try:

    result=num1/num2 

    print(result)

except:

    num2=int(input("enter number2:"))

    result=num1/num2

    print(result)

finally:

    print("file operation")

print("dp commit")
             
 # new method for error handling            
            
num1=int(input("enter num1")) #10)

num2=int(input("enter the num2"))#0

try:

    result=num1/num2 

    print(result)

except Exception as e :

    print(e)

    num2=int(input("enter number2:"))

    result=num1/num2

    print(result)

finally:

    print("file operation")

print("dp commit")
             
            