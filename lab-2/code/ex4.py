import random

# Enter number to test
N=67280421310721

# Enter number of iterations
t=30

# Choose a random a in Z_N and check if a^(N-1) mod N=1
def is_prime(N):
    a=random.randint(1,N-1)
    if pow(a,N-1,N)!=1:
        return False
    return True

# Repeat t times
# Print "composite" if you found a witness, else print prime
def fermat_test(N,t):
    for _ in range(t):
        if not is_prime(N):
            print("composite")
            return
    print("prime")
    return

fermat_test(N,t)

