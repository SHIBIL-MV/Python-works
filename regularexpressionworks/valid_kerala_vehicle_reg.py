
# start with KL
# 2digit
# alphabetic minimum1 maximum 2
# 4 digit
from re import fullmatch

reg_num=input("enter registration number :")

pattern="(kL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,reg_num)

if matcher==None:

    print("invalid")

else:

    print("valid")