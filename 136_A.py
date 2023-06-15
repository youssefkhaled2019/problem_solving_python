"""
contest=https://codeforces.com/contest/136/problem/A 
date= Thursday, June 15, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split()))
l_ =[]
ii=1
for i in range(n):
    l_.extend([l.index(i+1)+1])
print(*l_)