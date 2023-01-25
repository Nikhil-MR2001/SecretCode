
import random
import string
word = input("Enter the word to be Encripted/Decripted :  ")

coding = input("For Encryption press 1  For Decription press 0 :")
coding = True if (coding == "1") else False
print(coding)
if(coding):
    if len(word)>=3:
        endword =  ''.join((random.choice(string.ascii_lowercase + string.digits) for codenum in range(3)))
        startword =  ''.join((random.choice(string.ascii_lowercase + string.digits) for codenum in range(3)))

        new_word = print(startword + word[1:] + word[0] + endword)
    else:
        print(word[ ::-1])

else:
    if len(word)<=3:
        print(word[ ::-1])
    else:
        endword =  ''.join((random.choice(string.ascii_lowercase + string.digits) for codenum in range(3)))
        startword =  ''.join((random.choice(string.ascii_lowercase + string.digits) for codenum in range(3)))
        new_word = (startword + word[1:] + word[0] + endword)
        print(word[-4] + new_word[5:-8])




