#starting with an alphabetic from p-t

# in second place must be a number this is \ by 3

# followed by any number alphabetics,numbers,@

from re import fullmatch


pattern="[p-tp-T][369][a-zA-Z0-9@]*"

user_input=input("enter variable name:")

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")

     