def programa2(n):
    cnt=0
    s=1
    cnt+=1
    i=1
    cnt+=1
    while i <=n:
        cnt+=1
        t=1
        cnt+=1
        j=1
        cnt+=1
        while j<=i:
            cnt+=1
            t+=1 # t=t+1
            cnt+=1
            j=j+1
            cnt+=1
        cnt+=1
        s=s+t
        cnt+=1
        i=i+1
        cnt+=1
    cnt+=1
    return cnt
def fprograma2(n):
    return 5*n+3+n*(n+3)/2+n*(n+1)
# numero de pruebas
for i in range(0,105,5):
    print("n= ", i, "pesos=",programa2(i),"f(n)=",fprograma2(i))