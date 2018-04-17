from heapq import *
class character:
    def __init__(self,s=None,l=None,r=None):
        self.freq=0
        self.symbol=s
        self.left=l
        self.right=r
    def __lt__(self,other):
        return self.freq<other.freq

def printTree(x,s=""):
    if x.symbol is not None:
        print(x.symbol,"\t"+s)
    if(x.left):
        printTree(x.left,s+"0")
    if(x.right):
        printTree(x.right,s+"1")

def main():
    print("Enter data to be encoded:")
    text=input()
    while True:
        l=input()
        if not l or l=='\n':
            break
        text+=l
    s=set(text)
    d={}
    for i in s:
        if i=='\n':
            d[i]=character("\\n")
        elif i==' ':
            d[i]=character("Space")
        else:
            d[i]=character(i)
        d[i].freq=text.count(i)
        
    chars=[d[i] for i in s]
    heapify(chars)
    for i in chars:
        print(i.freq)
    while len(chars)>1:
        u=heappop(chars)
        v=heappop(chars)
        n=character(None,u,v)
        heappush(chars,n)
    tree=chars[0]
    printTree(tree)

if __name__ == '__main__':
    main()
