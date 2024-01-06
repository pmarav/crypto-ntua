from numpy import log as ln
from math import pi,ceil

# find number of points using Chernoff bound
def find_N(k,d):
    return 12*pi*ln(2/d)/10**(-2*k)

for k in range(2,5):
    print("k=", k, "d=0.05: ", ceil(find_N(k,0.05)))