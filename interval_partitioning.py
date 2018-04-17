class interval :
    def __init__(self,s,e):
        self.start=s
        self.end=e


def schedule(l,n):
        l.sort(key=lambda x:x.end)
        available=[ True for i in range(n)]
        schedule_count=n
        #rnum=0
        count=0
        while schedule_count >0:
            #rnum+=1
            s=[]
            t=0
            for i in range(n):
                if l[i].start>t and available[i]:
                    schedule_count-=1
                    available[i]=False
                    s.append(l[i])
                    t=l[i].end
            print("---")
            count+=1
            for i in s:
                print("["+str(i.start)+","+ str(i.end)+"]")
            print(count)
                
n=int(input("Enter the number of processes"))
l=[]
for i in range(n):
    s,e=input().split()
    s,e=int(s),int(e)
    l.append(interval(s,e))

schedule(l,n)
