num=int(input("enter the number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num>num2 and num>num3:
    print(f"{num}is greatest")
elif num2>num and num2>num3:
    print(f"{num2}is greatest")
elif num3>num and num3>num2:
    print (f"{num3}is greatest")
elif num1==num2 and num1==num3:
    print("three numbers equal")