
"""
contest=https://codeforces.com/contest/770/problem/A 
date=Saturday, May 13, 2023
Verdict =Accepted
"""   
a,b=map(int,input().split(" "))
alph=[ chr(i) for i in range(97,97+b)]
s=""
for i in range(a):
    s+=alph[i%b]

print(s)    
