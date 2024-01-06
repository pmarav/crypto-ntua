import random
import math

# input
n=0xb844986fc061a2c0baf528a960e208832625f725fa09bfe1ac4c15bccad6031d09f8f37bf00520bb59480070e59441ed34b7e3d118db67a035ac4b46a055a4963df4af0baa4dfab3f98566f2c09f7c83ffec458b63931ce311241c98614659172cfe9f21ecc7d7241aea1ae1e88f796568f49a645ffce12c87629e8783462e5dbeb52a85c95

e=0x369d89b820f2450462f21b02d91bcec9de528805bb22123d843fcd776ad57025980f1c3359d45d65c9a9e363a0a51eaf8873b3dc2ffab45787c5e86bacbf2a6bbca5106828eec95cb2ea534fa2e64d672a2c69e21589f84daa54a164db28ade473e8009972279cd89c5afaf1b312914256dac666e7f824db23f33a9867616898686a1fe63c5

# calculate coefficients of continuous fraction expansion
def continuous_fractions(nom,den):
    coeff=[]
    a=nom//den
    coeff.append(a)
    while nom%den!=0:
        temp=nom
        nom=den
        den=temp%den
        a=nom//den
        coeff.append(a)
    return coeff

# calculate convergents given continuous fraction expansion coefficients
def find_convergents(coeff):
    convergents=[]
    convergents.append((coeff[0],1))
    convergents.append((coeff[0]*coeff[1]+1,coeff[1]))
    for i in range(2,len(coeff)-1):
        convergents.append((coeff[i]*convergents[i-1][0]+convergents[i-2][0],coeff[i]*convergents[i-1][1]+convergents[i-2][1]))
    return convergents

# create a random message m and for each possible private key in convergents
# check if it is the right key by computing Dec(Enc(m))=? m
def find_d_optimized(e,n):
    m=420
    c=pow(m,e,n)
    coeff=continuous_fractions(e,n)
    convs=find_convergents(coeff)
    for i in convs:
        poss_d=i[1]
        if pow(c,poss_d,n)==m:
            return poss_d
    return -1 

# factorize n given e,d by picking random x in Z*_n and looking for a non trivial root of 1
def factorize(e,n):
    d=find_d_optimized(e,n)
    k=e*d-1
    # find r,u such that ed-1=2^r * u where u is odd
    r=0
    u=k
    while u%2==0:
        u//=2
        r+=1
    while True:
        x=random.randint(2,n-2)
        x=pow(x,u,n)
        for _ in range(r-1):
            if x!=1:
                temp=x
                x=pow(x,2,n)
            else:
                if temp!=n-1:
                    return (math.gcd(temp-1,n),math.gcd(temp+1,n))

print(find_d_optimized(e,n))
print(factorize(e,n))





