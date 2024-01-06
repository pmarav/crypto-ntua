import bbs

def find_period(bbs):
    x=pow(bbs.x0,2,bbs.n)
    period=1
    while x!=bbs.x0:
        x=pow(x,2,bbs.n)
        period+=1
    return period

bbs=bbs.bbs()

print("seed is",bbs.x0)
print("p,q are",(bbs.p,bbs.q))
print("period should be",bbs.period())
print("period is",find_period(bbs))