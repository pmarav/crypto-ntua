import random
import math

class bbs():

    def __init__(self):
        self.p,self.q=self.generate_primes(20)
        self.n=self.p*self.q
        self.x0=self.find_seed()

    # miller rabin primality test (max 30 iterations for 1/2^30 probability of mistake)
    def miller_rabin(self,n):
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

    # choose a random n bit number and check if it is a safesafe prime
    def find_safesafe_prime(self,n):
        while True:
            p=random.randint(2**(n-1),2**n)
            if p%4==3 and self.miller_rabin(p):
                p1=(p-1)//2
                if self.miller_rabin(p1):
                    p2=(p1-1)//2
                    if self.miller_rabin(p2):
                        return p
    
    # find a pair p,q of distinct safesafe primes
    # do not accept if 2 is a quadratic residue in both Z*_p1 and Z*_q1 
    def generate_primes(self,n):
        p=self.find_safesafe_prime(n)
        p1=(p-1)//2
        p2=(p1-1)//2
        q=p
        while True:
            q=self.find_safesafe_prime(n)
            q1=(q-1)//2
            q2=(q1-1)//2
            if (pow(2,p2,p1)!=1 or pow(2,q2,q1)!=1) and p!=q:
                return p,q
    
    
    def period(self):
        p=(((self.p-1)//2)-1)//2
        q=(((self.q-1)//2)-1)//2
        return 2*p*q
    
    # find optimal seed x_0 given n=pq such that order_n(x_0)=λ(n)/2
    def find_seed(self):
        n=self.n
        while True:
            p1=(self.p-1)//2
            q1=(self.q-1)//2
            x=random.randint(2,n-2)
            y=pow(x,2,n)
            if n%y!=0 and pow(y,p1,n)!=1 and pow(y,q1,n)!=1 and pow(y,p1*q1,n)==1:
                return y
    
    #generate n pseudorandom bits
    def generate_bits(self,n):
        bits=[]
        for _ in range(n):
            self.x0=pow(self.x0,2,self.n)
            bits.append(self.x0%2)
        return bits

    def get_parity(self,n):
        x=bin(n)[2:]
        sum=0
        for bit in x:
            if int(bit)==1:
                sum+=1
        return sum%2
    
    #generate n pseudorandom bits by using the parity of x instead of lsb
    def generate_bits_parity(self,n):
        bits=[]
        for _ in range(n):
            self.x0=pow(self.x0,2,self.n)
            parity=self.get_parity(self.x0)
            bits.append(parity)
        return bits

    def change_parameters(self,p,q,):
        self.p=p
        self.q=q
        self.n=p*q
    

    



