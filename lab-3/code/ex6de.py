import bbs
import math
from copy import deepcopy

def binary_to_float(bstr, m, n):
    return int(bstr, 2) / 2 ** n

def inside_circle(x,y):
    r=math.sqrt((x-127.5)**2+(y-127.5)**2)
    if r<=127.5:
        return True
    return False

def approximate_pi(gen,decimals):
    pi=math.pi
    pi_approx=0
    inside=0
    total=0
    while abs(pi-pi_approx)>=10**(-decimals-1):
        bits_x=''.join(str(x) for x in gen.generate_bits(16))
        bits_y=''.join(str(y) for y in gen.generate_bits(16))
        x=binary_to_float(bits_x,8,8)
        y=binary_to_float(bits_y,8,8)
        if inside_circle(x,y):
            inside+=1
        total+=1
        pi_approx=4*(inside/total)
    return total,pi_approx

def approximate_pi_parity(gen,decimals):
    pi=math.pi
    pi_approx=0
    inside=0
    total=0
    while abs(pi-pi_approx)>=10**(-decimals-1):
        bits_x=''.join(str(x) for x in gen.generate_bits_parity(16))
        bits_y=''.join(str(y) for y in gen.generate_bits_parity(16))
        x=binary_to_float(bits_x,8,8)
        y=binary_to_float(bits_y,8,8)
        if inside_circle(x,y):
            inside+=1
        total+=1
        pi_approx=4*(inside/total)
    return total,pi_approx


gen1=bbs.bbs()
gen2=deepcopy(gen1)
print("x0:",gen1.x0)
print("p,q:",(gen1.p,gen1.q))
print("lsb: total points, pi_approx", approximate_pi(gen1,4))
print("parity: total points, pi_approx", approximate_pi_parity(gen2,4))



    



