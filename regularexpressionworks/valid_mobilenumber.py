from re import fullmatch

phonenum=input("enter phone num:")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,phonenum)

if matcher==None:

    print("invalid number")

else:

    print("valid number")