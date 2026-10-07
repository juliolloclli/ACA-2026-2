import numpy as np
def insertion_sort(A):
    cnt=0
    for j in range(2,len(A)+1):
        cnt+=1
        i=j-1
        cnt+=1
        key=A[j-1]
        cnt+=1
        while i>0 and A[i-1]>key:
            cnt+=1 #incremente el bucle while
            A[i+1-1]=A[i-1]
            cnt+=1
            i=i-1
            cnt+=1
        cnt+=1
        A[i+1-1]=key
        cnt+=1
    cnt+=1 #retorna la salida del for
    return cnt

def f_best(n):
    return 5+n-4

def f_worst(n):
    return 1.5*n**2*3.5*n-4

def f_avarage(n):
    return 0.75*n**2+2.75*n-3.5

listaP=[9,10,1,2,7,8,12,3,4,5]
insertion_sort(listaP)
print(listaP)

def ordenado(n):
    lista=[]
    for i in range(0,n):
        lista.append(i)
    return lista

def ordenado_inverso(n):
    lista=[]
    for i in range(n,0,-1):
        lista.append(i)
    return lista

def validation():
    lista_n=[10,20,30,50,80,100,200,300,500,600,700,800,900,1000]
    for n in lista_n:
        err_o=ordenado(n)
        print("tamaño ", n)
        print("Mejor caso ", insertion_sort(err_o),f_best(n))
        arr_oi=ordenado_inverso
        print("Peor caso ", insertion_sort(arr_oi),f_worst(n))
        average=0
        for k in range(0,100):
            arr_av=np.random.randint(0,1000000,n)
            cnt_av=insertion_sort(arr_av)
            average+=cnt_av
        average/=100
        print("Caso Promedio ",average,f_avarage(n))
        print("********************")
        
    validation()