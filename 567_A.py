"""
contest=https://codeforces.com/contest/567/problem/A
date= Wednesday, May 24, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
for i in range(n):
    if (i==0):
        mn,mx=abs(l[i]-l[1]),abs(l[i]-l[-1])
        print(mn,mx)
    elif(0<i<n-1):
        mn=min(abs(l[i]-l[i+1]) ,abs(l[i]-l[i-1]))         
        mx=max(abs(l[i]-l[0]) ,abs(l[i]-l[-1])) 
        print(mn,mx)
    else:
        mn,mx=abs(l[i]-l[i-1]),abs(l[i]-l[0])
        print(mn,mx)



