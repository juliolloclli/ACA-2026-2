def programa3(n):
    cnt=0
    i=1
    cnt+=1
    while i <=n:
        cnt+=1
        k=i
        cnt+=1
        while k<=n:
            cnt+=1
            k+=1 # k=k+1
            cnt+=1
        cnt+=1
        k=1 
        cnt+=1
        while k<=i:
            cnt+=1
            k+=1
            cnt+=1
        cnt+=1
        i+=1
        cnt+=1
    cnt+=1
    return cnt
def fprograma3(n):
    return 4*n+3+n*(n+3)+n*(n+1)
# numero de pruebas
for i in range(100,1100,100):
    print("%d\t%d\t%d"%(i,programa3(i),fprograma3(i)))