from sympy import totient
import sys
import math
sys.setrecursionlimit(2000)

# input
num=1707
exp=1783
mod=10**17

# function for factorization
def prime_factors(number):
    prime_factors=[]
    while number%2==0:
        prime_factors.append(2)
        number//=2
    possible_factor=3
    while possible_factor**2 <= number:
        if number%possible_factor==0:
            prime_factors.append(possible_factor)
            number//=possible_factor
        else:
            possible_factor+=2
    if number!=1:
        prime_factors.append(number)
    s=set(prime_factors)
    result=[]
    for item in s:
        result.append((item,prime_factors.count(item)))
    return result

# check if gcd(num,mod)=1, otherwise factorize num
if math.gcd(num,mod)!=1:
    factors=prime_factors(22)

def solve(num,exp,mod):
    if exp==1:
        return num%mod
    elif mod==1:
        return 0
    else:
        if math.gcd(num,mod)==1:
            return pow(num, solve(num, exp-1, totient(mod)),mod)
        else:
            result=1
            for item in factors:
                count_common=0
                mod2=mod
                factor=item[0]
                while mod2%factor==0:
                    mod2//=factor
                    count_common+=1
                phi_mod=totient(mod2)
                result*= (pow(factor,count_common)%mod)*pow(factor, ((solve(num,exp-1,phi_mod)*item[1])%phi_mod -count_common)%phi_mod, mod)
            return result%mod   
        
print(solve(num,exp,mod))
