def edit_distance(str1,str2,s1,s2):
    dp=[[0 for i in range(s2+1)] for j in range(s1+1)]
    #print(dp)
    for i in range(s1+1):
        for j in range(s2+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp [i][j]=i
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else :
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    for i in range(s1+1):
        for j in range(s2+1):
            print(dp[i][j],end=" ")
        print()
    return dp[s1][s2]

str1=list(input().strip())
str2=list(input().strip())
s1=len(str1)
s2=len(str2)
r=edit_distance(str1,str2,s1,s2)
print("The minimum number of operations required " + str(r))
