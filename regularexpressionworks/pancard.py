# 3 alphabets
# 4th place alphabets[pcafht]
#1 alphabets
#4 digit
#1 alphabets
from re import fullmatch

pancard_num=input("enter  pan number :")

pattern="[A-Z]{3}[PCAFHT][A-Z][{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_num)

if matcher==None:

    print("invalid")

else:

    print("valid")