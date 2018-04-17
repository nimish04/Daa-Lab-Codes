import math
v=int(input("Enter the number of vertices"))
e=int(input("Enter the number of edges"))

d0=[]
for i in range(v):
    d0.append([math.inf]*v)
    
for i in range(e):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d0[a][b]=c
    
for i in range(v):
    for j in range(v):
        print(d0[i][j],end=" ")
    print()
print()

d1=[]
for i in range(v):
    d1.append([math.inf]*v)
for k in range(1,v):
    for i in range(v):
        for j in range(v):
            if i==j:
                d1[i][j] = int(0)
            else:
                d1[i][j]=min(d0[i][j],d0[i][k]+d0[k][j])
    d0=d1
    
for i in range(v):
    for j in range(v):
        print(d1[i][j],end=" ")
    print()
