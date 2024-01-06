import bbs

def get_parity(n):
        x=bin(n)[2:]
        sum=0
        for bit in x:
            if int(bit)==1:
                sum+=1
        return sum%2

def test(bbs):
    count1=0
    count1_parity=0
    max1=0
    max1_parity=0
    temp1=0
    temp1_parity=0
    x=bbs.x0
    total=0
    while True:
        x=pow(x,2,bbs.n)
        out=x%2
        out_parity=get_parity(x)
        count1+=out
        count1_parity+=out_parity
        total+=1
        if out==1:
            temp1+=1
        else:
            temp1=0
        if out_parity==1:
            temp1_parity+=1
        else:
            temp1_parity=0
        if temp1>max1:
            max1=temp1
        if temp1_parity>max1_parity:
            max1_parity=temp1_parity
        if x==bbs.x0:
            break
    return count1*100/total,max1,count1_parity*100/total,max1_parity



bbs=bbs.bbs()
bbs.change_parameters(539159,555287)

print("seed is",bbs.x0)
print("p,q are",(bbs.p,bbs.q))
print(test(bbs))
