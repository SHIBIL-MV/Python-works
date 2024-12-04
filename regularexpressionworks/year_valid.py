from re import fullmatch

year=input("enter year:")

#pattern="([12][89][0-9]{2}|[2][0][0-2][0-4]{1})"

pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,year)

if matcher==None:

    print("invalid")

else:

    print("valid")
    
# 1800 t0 2024