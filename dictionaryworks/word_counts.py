text="ABBACB"

#print character count
#A:2
#B:3
#c:1

charactor_count={}

for ch in text:

    if ch in charactor_count:
         
         charactor_count[ch]+=1

    else:

         charactor_count[ch]=1
print(charactor_count)