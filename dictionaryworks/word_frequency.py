text="ABAABBCCDDEEA"

# character_frequency{A:4,B:3,...}

character_frequency={ch:text.count (ch) for ch in text}

print(character_frequency)

#non_recursive_element

non_recursive=[k for k,v in character_frequency.items() if v==1 ]
               
print(non_recursive)              

# if v==1:
  
  # print(k)