import math

# change path to the directory where text_1.txt (ciphertext) is located
ciphertext_path='C:\\Users\\marav\\OneDrive\\Έγγραφα\\σχολη\\κρυπτο\\1η σειρα\\code\\text_1.txt'
file=open(ciphertext_path)
text=file.read()

key='cryptography'

# convert ciphertext to numbers 0-25
converted=[]
for char in text:
    if char.isalpha():
        converted.append((ord(char.upper())-65))

# create an array of the 26 possible keys
keys=[]
for i in range(26):
    temp_key=[]
    for char in key:
        temp_key.append((ord(char.upper())-65 + i)%26)
    keys.append(temp_key)

real_frequencies=[8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074]

# cost function to measure if the text's frequencies are close to the real frequencies
def cost(real, text):
    cost=0
    for i in range(26):
        cost+=(real[i]-text[i])*(real[i]-text[i])
    return math.sqrt(cost)

# create an array with the cost of each of the 26 different keys
key_cost=[]

# for each key find the plaintext, count the frequencies and compute the cost function
for key in keys:
    possible_plaintext=[]
    for i in range(len(converted)):
        possible_plaintext.append((converted[i]-key[i%len(key)])%26)
    frequencies=[0]*26
    for char in possible_plaintext:
        frequencies[char]+=1
    for i in range(26):
        frequencies[i]/=len(converted)
        frequencies[i]*=100
    key_cost.append(cost(real_frequencies,frequencies))

# the key with the minimum value of cost is the key actually used
# convert it to string
used_key=""
for i in keys[key_cost.index(min(key_cost))]:
    used_key+=(chr(i+97))

print("The key was", used_key)
key_used= keys[key_cost.index(min(key_cost))]

# decrypt the ciphertext using the right key
plaintext=""
count_letters=0
for i in range(len(text)):
    if ord(text[i]) >= 65 and ord(text[i]) <= 90:
        plaintext+= chr(((converted.pop(0) - key_used[count_letters%len(key_used)])%26) + 65)
        count_letters+=1
    elif ord(text[i]) >=97 and ord(text[i]) <= 122:
        plaintext+= chr(((converted.pop(0) - key_used[count_letters%len(key_used)])%26) + 97)
        count_letters+=1
    else:
        plaintext+=text[i]

print("The plaintext was:", plaintext, sep="\n")
    


