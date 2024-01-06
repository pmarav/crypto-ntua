import math

# change path to the directory where text_3.txt (ciphertext) is located
ciphertext_path='C:\\Users\\marav\\OneDrive\\Έγγραφα\\σχολη\\κρυπτο\\1η σειρα\\code\\text_3.txt'
file=open(ciphertext_path)
ciphertext=file.read()

max_key_length = 12

real_frequencies=[8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074]

# convert letters to numbers 0-25
converted=[]
for char in ciphertext:
    if char.isalpha():
        converted.append((ord(char.upper())-65))

# define index of coincidence of a single row in number format
def index_of_coincidence(row):
    frequencies=[0]*26
    ic=0
    for i in row:
        frequencies[i]+=1
    for i in range(26):
        ic+=(frequencies[i]*frequencies[i])/(len(row)*len(row))
    return ic

# try all different keylengths on the ciphertext
# for each key length divide the ciphertext into that many rows and compute the index of coincidence for each
# the compute the mean index of coincidence and store it
mean_ic=[]
for key_length in range(1, max_key_length+1):
    # rows=[[]]*key_length WTFF
    rows=[[] for _ in range(key_length)]
    for row in range(key_length):
        i=row
        while i< len(converted):
            rows[row].append(converted[i])
            i+=key_length
    mean_coincidence=0
    for row in rows:
        mean_coincidence+=index_of_coincidence(row)
    mean_coincidence/=key_length
    mean_ic.append(mean_coincidence)

# the key length is equal to the one that corresponds to the maximum key_length
key_length=mean_ic.index(max(mean_ic)) + 1

# divide the ciphertext into rows according to the right key length
rows=[[] for _ in range(key_length)]
for row in range(key_length):
    i=row
    while i<len(converted):
        rows[row].append(converted[i])
        i+=key_length

# function that shifts each letter of a string "word" by "offset"
def shift(word,offset):
    shifted=[]
    for i in word:
        shifted.append((i+offset)%26)
    return shifted

# define the mutual index of coincidence between row1 shifted by j and row2
def mutual_ic(row1,row2,j):
    frequencies1=[0]*26
    frequencies2=[0]*26
    ic=0
    for i in shift(row1,j):
        frequencies1[i]+=1
    for i in row2:
        frequencies2[i]+=1
    for i in range(26):
        ic+=(frequencies1[i]*frequencies2[i])/(len(row1)*len(row2))
    return ic

# find the row with the maximum index of coincidence and keep it fixed while calculating mutual index of coincidence
max_ic=0
for i in range(key_length):
    if index_of_coincidence(rows[i])>index_of_coincidence(rows[max_ic]):
        max_ic=i
max_ic=0
# find the shift that maximizes the mutual index of coincidence between each row and the row that we kept fixed (calculated above)
key=[0]*key_length
for i in range(key_length):
    if i==max_ic:
        continue
    for j in range(26):
        if mutual_ic(rows[i],rows[max_ic],j)>mutual_ic(rows[i],rows[max_ic],key[i]):
            key[i]=j

# calculate the actual key used shifted by a number 0-25
for i in range(key_length):
    key[i]=(key[max_ic]-key[i])%26

# create an array containing the 26 possible shifts of the key calculated above
keys=[]
for i in range(26):
    keys.append(shift(key,i))

# define cost function to compare text frequencies to real frequencies (eucleidian distance)
def cost(real, text):
    cost=0
    for i in range(26):
        cost+=(real[i]-text[i])*(real[i]-text[i])
    return math.sqrt(cost)

# create an array of cost corresponding to each possible key
# the real key is the one corresponding to the minumum cost
key_cost=[]

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

used_key=""
for i in keys[key_cost.index(min(key_cost))]:
    used_key+=(chr(i+97))

# decrypt using the key calculating above the convert numbers to letters
plaintext=""
count_letters=0
for i in range(len(ciphertext)):
    if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
        plaintext+= chr(((converted.pop(0) - keys[key_cost.index(min(key_cost))][count_letters%len(key)])%26) + 65)
        count_letters+=1
    elif ord(ciphertext[i]) >=97 and ord(ciphertext[i]) <= 122:
        plaintext+= chr(((converted.pop(0) - keys[key_cost.index(min(key_cost))][count_letters%len(key)])%26) + 97)
        count_letters+=1
    else:
        plaintext+=ciphertext[i]

print(used_key, plaintext)