from re import finditer

text="abbbabaaabbaaababababab"
      #01234567890123456789012
#pattern="b{2}"
pattern="b{1,3}"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())