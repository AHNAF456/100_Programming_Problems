# A problem of codeforces
n_k=input()
all=input()
alls=all.split()
abc=n_k.split()
k=int(abc[1])
n=abc[0]
kth=alls[k-1]

ans=0
for x in alls:
    if int(x)>= int(kth) and int(x)> 0:
        ans+=1
    else:
        pass
print(ans)


