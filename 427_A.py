"""
contest=https://codeforces.com/contest/427/status
date= Tuesday, May 16, 2023 
Verdict =Accepted
"""

n=int(input())
l=list(map(int,input().split(" ")))
s,o=0,0

for i in range(n):

    if (l[i]!=-1):
        s+=l[i]
    else:
        if(s>=1):
            s-=1
        else:
            o+=1    
print(o)