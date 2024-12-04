read_path=("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\word.txt")

write_path=("C:\\Users\\SHIBIL mv\\Desktop\\Pythonworks\\data_sets\\palindrome.txt")

f_read=open(read_path,"r")

f_palindrome=open(write_path,"w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_palindrome.write(word+"\n")

f_read.close()

f_palindrome.close()