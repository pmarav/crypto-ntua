import random

# change path to the directory where text_2.txt (plaintext) is located
plaintext_path='C:\\Users\\marav\\OneDrive\\Έγγραφα\\σχολη\\κρυπτο\\1η σειρα\\code\\text_2.txt'
file = open(plaintext_path)
text = file.read()

key='cryptography'

# convert letters to numbers 0-25
converted=[]
for char in text:
    if char.isalpha():
        converted.append((ord(char.upper())-65))

# choose a random shift and use it on the key
shift = random.randint(0,25)

shifted_key=[]
for char in key:
    shifted_key.append((ord(char.upper())-65 + shift)%26)

# encrypt using the shifted key
ciphertext=""
count_letters=0
for i in range(len(text)):
    if ord(text[i]) >= 65 and ord(text[i]) <= 90:
        ciphertext+= chr(((converted.pop(0) + shifted_key[count_letters%len(shifted_key)])%26) + 65)
        count_letters+=1
    elif ord(text[i]) >=97 and ord(text[i]) <= 122:
        ciphertext+= chr(((converted.pop(0) + shifted_key[count_letters%len(shifted_key)])%26) + 97)
        count_letters+=1
    else:
        ciphertext+=text[i]

print("The ciphertext is:", ciphertext, sep="\n")





