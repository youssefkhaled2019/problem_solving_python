"""
contest=https://codeforces.com/contest/231/problem/A
date= Tuesday, May 9, 2023
Verdict  = Accepted
"""
n=int(input())
s=0
for i in range(n):
    a,b,c=map(int,input().split(" "))
    if (a+b+c>=2):
        s+=1
print(s)        
