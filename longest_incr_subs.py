n=int(input("Enter n:"))
print("Enter array:")
a=[int(i) for i in input().split()]
memo=[1 for i in range(n)]
for i in range(1,n):
	for k in range(i):
		if a[k]<a[i] and memo[k]+1>memo[i]:
			memo[i]=memo[k]+1
maxi=0
for i in range(n):
    maxi=max(maxi,memo[i])
print("Length of longest increasing subsequence:"+str(maxi
                                                      ))
