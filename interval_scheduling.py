n=int(input("Enter the number of processes"))
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=input().split()
    a[i]=int(a[i])
    b[i]=int(b[i])

for i in range(n):
    for j in range(n-i-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]

for i in range(n):
    print(a[i],b[i])


print("[" + str(a[0]) + "," + str(b[0]) + "]",end=" ")
j=0
for i in range(1,n):
    if a[i]>b[j]:
        print("[" + str(a[i]) + "," + str(b[i]) + "]",end=" ")
        j=i

