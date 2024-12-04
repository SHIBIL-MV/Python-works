from re import fullmatch

date=input("enter date:")

#pattern="([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])"
pattern="(0?[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(pattern,date)

if matcher==None:

    print("invalid")

else:

    print("valid")
    
    