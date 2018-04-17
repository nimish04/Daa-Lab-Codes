def count_inversions(a,low,high):
    mid=(low+high)//2
    il=ir=0
    al=a[:high//2]
    ar=a[high//2:]
    if low < high :
        il=count_inversions(al,0,mid)
        ir=count_inversions(ar,mid+1,high)
    isp=count_split(al,ar)
    return (isp+il+ir)

def count_split(a1,a2):
    sort1=sorted(a1)
    sort2=sorted(a2)
    count1=0
    i=0
    j=0
    while i<len(sort1) and j<len(sort2) :
        if sort1[i] > sort2[j] :
            count1+=(len(sort1)-i)
            j=j+1
        else :
            i=i+1
    return count1

print("Enter the larray")
arr=list(map(int, input().split(' ')))
high=len(arr)-1
count=count_inversions(arr,0,high)
print("The number of inversions are " + str(count))
