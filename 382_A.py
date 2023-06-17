"""
contest=https://codeforces.com/contest/382/problem/A
date= Saturday, June 17, 2023 
Verdict =Accepted
"""
a,b=input().split("|")
c=input()
for i in range(len(c)):
    if(len(a)<len(b)):
        a+=c[i]
    elif(len(a)>len(b)):
        b+=c[i]    
    else: 
        a+=c[i]  

if(len(a)==len(b)):
    o=a+"|"+b
    print(o)
else:
    print("Impossible")
