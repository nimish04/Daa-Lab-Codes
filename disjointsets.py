class Node :
    def __init__(self,index=None,rank=None):
        self.index=index
        self.parent=None
        self.rank=rank

class DSU :
    def __init__(self):
        self.nodes=[]

    def make_set(self,x):
        t=Node(x,0)
        t.parent=t
        self.nodes.append(t)

    def find_set(self,x):
        if x.parent==x:
            return x
        else :
            return self.find_set(x.parent)

    def union_set(self,x,y):
        x=self.find_set(x)
        y=self.find_set(y)
        if x.rank > y.rank :
            y.parent=x
        elif x.rank < y.rank :
            x.parent=y
        else :
            x.parent=y
            y.rank+=1


d=DSU()
for i in range(7):
    d.make_set(i)
n=d.nodes
d.union_set(n[0],n[1])
d.union_set(n[0],n[2])
d.union_set(n[2],n[3])
d.union_set(n[2],n[3])
d.union_set(n[4],n[6])
d.union_set(n[4],n[5])
d.union_set(n[2],n[4])
for i in range(7):
    print(d.find_set(n[i]).index)

