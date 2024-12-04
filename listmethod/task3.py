source_word="REGULATE"

target_words="LATER"

# kangaroo_word

character_count={}

for ch in source_word:

    if ch in character_count:

        character_count[ch]+=1


    else:

        character_count[ch]=1
    
print(character_count)

character_count={ch:source_word.count(ch) for ch in source_word}

is_kangarro=True

for ch in target_words:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:

         is_kangarro=False
         

         break

print(is_kangarro)
