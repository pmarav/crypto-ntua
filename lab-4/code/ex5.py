import random
import hashlib

# parameters used
n=512 # security parameter
p=22226795912827167471485832074054815177102483805022173503365260236572886980774855788428424697657189963898292466501002906802672265528967617992469214739064139
q=11113397956413583735742916037027407588551241902511086751682630118286443490387427894214212348828594981949146233250501453401336132764483808996234607369532069
g=2312912455357601680616371992191436189870660099793485752068713401163103536947882676560443254078156911635174497711984135879613596929216065630260909354456774
h=2146676388298897674343482129720750041055852316747362070786277200235020101806837256016305514076709939680701481499416622218233984604763596895727677755447744
x=4071610964523655558956291845789439169839672055434825328225194737756700007506713353730774615968120270333011592875786745609224267911301851319332799633040462
filename='C:\\Users\\marav\\OneDrive\\Έγγραφα\\σχολη\\κρυπτο\\4η σειρα\\code\\large_file.bin'




# primality test
def miller_rabin(n):
    if n==2:
        return True
    if n%2==0:
        return False
    r=0
    u=n-1
    while u%2==0:
        r+=1
        u//=2
    for _ in range(30):
        a=random.randint(1,n-1)
        temp=pow(a,u,n)
        if temp==1 or temp==n-1:
            continue
        counter=0
        for i in range(r-1):
            temp=pow(temp,2,n)
            if temp==n-1:
                break
            counter+=1
        if counter==r-1:
            return False
    return True

# create n-bit prime orders for the groups Z_p*, Z_q* such that p=2q+1
def generate_orders(n):
    while True:
        q=random.randint(2**(n-1),2**n)
        if miller_rabin(q):
            p=2*q+1
            if miller_rabin(p):
                return p,q

# find generator of G (order q subgroup of Zp*) where p=2q+1 
def find_generator(p):
    while True:
        g=random.randint(2,p-2)
        if pow(g,(p-1)//2,p)==p-1:
            return pow(g,2,p)

# generate the perameters of schnorr
def schnorr_gen(n):
    p,q=generate_orders(n)
    g=find_generator(p)
    x=random.randint(1,q-1)
    h=pow(g,x,p)
    return p,q,g,x,h

# find the sha512 hash of a file
def get_sha512(filename):
    with open(filename) as f:
        content = f.read()
    sha512=hashlib.sha512()
    sha512.update(content.encode("ascii"))
    hash=sha512.hexdigest()
    return hash
    

# sign a message m
def sign(m,g,p,q,x):
    t=random.randint(1,q-1)
    y=pow(g,t,p)
    sha512=hashlib.sha512()
    sha512.update(str(y).encode("ascii"))
    sha512.update(m.encode("ascii"))
    c=sha512.hexdigest()
    c=int(c,16)%q
    s=(t-c*x)%q
    return c,s

# verify the signature
def verify(m,g,c,s,h):
    value=(pow(g,s,p)*pow(h,c,p))%p
    sha512=hashlib.sha512()
    sha512.update(str(value).encode("ascii"))
    sha512.update(m.encode("ascii"))
    hash=sha512.hexdigest()
    hash=int(hash,16)%q
    if hash==c:
        return True
    return False

# uncomment to generate new parameters
# p,q,g,x,h=schnorr_gen(n)

m=get_sha512(filename)

c,s=sign(m,g,p,q,x)
if verify(m,g,c,s,h):
    print("Valid")
else:
    print("Invalid")




