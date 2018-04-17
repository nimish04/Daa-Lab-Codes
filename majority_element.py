def majorityElement(a):
    n=len(a)
    if len(a)==1:
        return a[0]
    elif len(a)==2:
        if a[0]==a[1]:
            return a[0]
        else :
            return None
    else :
        l=majorityElement(a[:n//2])
        r=majorityElement(a[n//2:])
        lf=rf=0
        for i in a :
            print(str(i)+"kk")
            print(str(r)+"rr")
            if i==l:
                print(str(l)+'ll')
                lf+=1
            
            if i==r:
                rf+=1
        if lf > n//2 :
            return l
        elif rf > n//2 :
            return r
        else  :
            return None

print("Enter the array")
arr=list(map(int,input().split()))
print(majorityElement(arr))
