from sympy import totient

# Input
Z=548
M=3

# Calculate (factor^exp)^a^b mod 10^M
def calc_pow(factor,exp,mod):
    a=1998000
    b=100**10
    count_common=0          # Count divisions until coprime
    while mod%factor==0:
        mod//=factor
        count_common+=1
    phi_mod=totient(mod)
    return pow(factor,count_common)*pow(factor, ((pow(a,b,phi_mod)*exp) -count_common)%phi_mod, mod)

def find_time(Z,M):
    # return [(2,a),(5,b),(c,1)] such that number =2^a x 5^b x c
    def factors(number):
        factors=[]
        count_2=0
        count_5=0
        while number%2==0:
            count_2+=1
            number//=2
        if count_2!=0:
            factors.append((2,count_2))
        while number%5==0:
            count_5+=1
            number//=5
        if count_5!=0:
            factors.append((5,count_5))
        factors.append((number,1))
        return factors
    mod=10**M
    factors=factors(Z)
    time=1
    for factor in factors:
        time*=calc_pow(factor[0],factor[1],mod)
    return time%mod

print(find_time(Z,M))