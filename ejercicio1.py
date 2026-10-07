import matplotlib.pyplot as plt

x=[x**2 for x in range(0,100)]
x1=[]

for i in range(0,100):
    x1.append(2*i**2)

x2=[]
for i in range(0,100):
    x2.append(i**2+2*i+1)

plt.figure(dpi=130)
plt.plot(range(0,100),x1)
plt.plot(range(0,100),x2)
plt.show()