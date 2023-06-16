"""
contest=https://codeforces.com/contest/218/problem/A
date= Friday, June 16, 2023 
Verdict =Accepted
"""
n,m=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
for i in range(1,len(l)-1):
    if (l[i-1]<l[i]-1>l[i+1] and m>0):
        l[i]-=1
        m-=1
print(*l)