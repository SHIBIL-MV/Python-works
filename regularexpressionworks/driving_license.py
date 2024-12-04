from re import fullmatch

license_num=input("enter the number :")

pattern="(kL)[0-9]{2}[1-9][0-9]{3}[0-9]{7}"

matcher=fullmatch(pattern,license_num)

if matcher==None:

    print("invalid")

else:

    print("valid")