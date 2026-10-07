def programa(n):
    cnt=0
    i=1
    cnt+=1
    while i<=n:
        cnt+=1
        j=1
        cnt+=1
        while j<=n:
            cnt+=1
            cnt+=1
            j=j+1
            cnt+=1
        cnt+=1
        i+=1
        cnt+=1
    cnt+=1
    return cnt

def fprograma1(n):
    return 3*n+2+n*(n+1)+2*n**2

for n in range(100,1100,100):
    T=programa(n)
    print(f"{n}, {T}, {fprograma1(n)}, {T/fprograma1(n)}")