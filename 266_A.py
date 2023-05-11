"""
contest= https://codeforces.com/contest/266/problem/A   
date= Thursday, May 11, 2023
Verdict =Accepted
"""

n=int(input())
s=input()
x=s[0]
c,m=0,-1
for i in s[1:]:
    if (x==i):
        c+=1
    elif(x!=i )  :
        if (m>c or m==0 ):
             m=c 
    x=i         

if(m==-1):
    print(c)
else:    
 print(m)