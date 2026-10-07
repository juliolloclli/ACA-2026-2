import numpy as np

def insertion_sort(A):
    cnt=0
    cnt+=1
    for j in range(2,len(A)+1):
        cnt+=1
        key=A[j-1]
        cnt+=1
        i=j-1
        cnt+=1
        while i>0 and A[i-1]>key:
            cnt+=1
            A[i]=A[i-1]
            cnt+=1
            i=i-1
            cnt+=1

        cnt+=1
        A[i]=key
        cnt+=1
    return cnt
lista=[3,4,8,1,6,12,9,14,20,7,2,5,10]
insertion_sort(lista)
print(lista)

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 20]
def f_mejor_caso(n):
    return n+4*(n-1)
print(f"Mejor caso: {f_mejor_caso(len(lista))} {insertion_sort(lista)}")

lista=[20, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def f_peor_caso(n):
    return n+3*(n-1)+(n+2)*(n-1)/2+(n-1)*n
print(f"Peor caso: {f_peor_caso(len(lista))} {insertion_sort(lista)}")

def f_caso_promedio(n):
    return n+3*(n-1)+(n-1)*n/4+0.5*(n-1)*n/2-(n-1)

for n in [10,20,30,50,80,100,200,300,500,600,700,800,900,1000]:
    exp=100
    tiemp=0
    for i in range(exp):
        lista=np.random.randint(0,1000000,n)
        
        tiemp+=insertion_sort(lista)
    tiemp+=tiemp/exp
    print(f"Peor caso: {f_caso_promedio(len(lista))} {insertion_sort(lista)}")
