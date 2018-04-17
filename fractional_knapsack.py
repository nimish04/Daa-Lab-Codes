def fractional_knapsack(result,w):
    result.sort(key=lambda x:x[2],reverse=True)
    bag=[]
    weight=0
    total_weight=0
    while(len(result)>0 and w>weight):
        if w-weight>=result[0][1]:
            bag.append([1,result[0][0]])
            weight+=result[0][1]
            result.pop(0)

        else :
            rat=float(w-weight)/float(result[0][1])
            bag.append([float(rat),float(rat)*result[0][0]])
            weight+=float(rat)*result[0][1]
            result.pop(0)
            break
    print(bag)
    for i in range(len(bag)):
        total_weight+=bag[i][1]
    print(total_weight)
result=[]
w=int(input("Enter the total weight of thee bag"))
n=int(input("enter the number of the items"))
for i in range(n):
    val,wei=input().split()
    val=float(val)
    wei=float(wei)
    ratio=val/wei
    result.append([val,wei,float(ratio)])
print(result)
fractional_knapsack(result,w)
