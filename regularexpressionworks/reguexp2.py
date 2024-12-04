from re import finditer

text="I have 3 cars,2 bikes and 1-Cycle"

#pattern="\w" #[a-zA-Z0-9] alphanumeric

#pattern="\d" #"[^0-9]"  for numeric

#pattern="\D" # exclude digits

#pattern="\w" # special charactors [^a-zA-Z0-9]
pattern="\s" # white space

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())