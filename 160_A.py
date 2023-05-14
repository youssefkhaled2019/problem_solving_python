"""
contest=https://codeforces.com/contest/160/problem/A 
date=  Sunday, May 14, 2023 
Verdict =Accepted
"""


n=int(input())
l_temp=sorted(list(map(int,input().split(" "))),reverse=True)
s=sum(l_temp)
l,c=0,0
for i in range(n):
    if(l<=(s/2)):
        c+=1
        l+=l_temp[i]
print(c)        

      
